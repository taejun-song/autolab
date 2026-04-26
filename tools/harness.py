#!/usr/bin/env python3
"""AutoLab Harness — manages agent session lifecycle.

The harness launches Claude sessions, monitors them, and cycles
them when needed. Each session reads the latest program.md, runs
a fixed number of experiments, then exits cleanly. The harness
restarts with a fresh context.

Why this exists: LLMs drift from instructions over long sessions.
Short sessions + wiki = reliable instruction-following + persistent knowledge.

Usage:
    # Run the harness (manages agent sessions automatically)
    python tools/harness.py --program program.md --max-experiments 5 --max-duration 1800

    # With multiple agents
    python tools/harness.py --program program.md --agents 3

    # With git sync
    python tools/harness.py --program program.md --git-pull
"""
import argparse
import os
import signal
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path


def get_program_mtime(path):
    """Get modification time of program file. Returns 0.0 if missing."""
    try:
        return os.path.getmtime(path)
    except OSError:
        return 0.0


def should_cycle(experiments_run, max_experiments, session_start,
                 max_duration, program_changed):
    """Decide if the current session should cycle.

    Returns reason string or None.
    """
    if program_changed:
        return "program_changed"
    if experiments_run >= max_experiments:
        return "max_experiments"
    if time.time() - session_start > max_duration:
        return "timeout"
    return None


def build_session_summary(wiki_dirs, results_path, session_number,
                          experiments_run, cycle_reason):
    """Build a summary of what happened in this session."""
    wiki_count = 0
    for d in wiki_dirs:
        if d.exists():
            wiki_count += len(list(d.glob("*.md")))
    results_count = 0
    if results_path.exists():
        results_count = sum(1 for _ in open(results_path)) - 1
    return (
        f"Session {session_number}: {experiments_run} experiments run, "
        f"{wiki_count} wiki pages, {results_count} total results. "
        f"Cycle reason: {cycle_reason}"
    )


class SessionManager:
    """Manages agent session lifecycle."""

    def __init__(self, program_path, max_experiments=5, max_duration=1800):
        self.program_path = Path(program_path)
        self.max_experiments = max_experiments
        self.max_duration = max_duration
        self.session_number = 0
        self.experiments_run = 0
        self.session_start = 0.0
        self.program_mtime = 0.0

    def start_session(self):
        """Begin a new session. Snapshots program mtime."""
        self.session_number += 1
        self.experiments_run = 0
        self.session_start = time.time()
        self.program_mtime = get_program_mtime(self.program_path)

    def check_cycle(self):
        """Check if current session should cycle. Returns reason or None."""
        current_mtime = get_program_mtime(self.program_path)
        program_changed = current_mtime > self.program_mtime
        return should_cycle(
            self.experiments_run,
            self.max_experiments,
            self.session_start,
            self.max_duration,
            program_changed,
        )

    def run_session(self, claude_path="claude", git_pull=False, extra_args=None):
        """Run one Claude session. Returns cycle reason."""
        if git_pull:
            subprocess.run(["git", "pull"], capture_output=True, timeout=30)

        self.start_session()
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{ts}] Session {self.session_number}: starting "
              f"(max {self.max_experiments} experiments, {self.max_duration}s timeout)")

        prompt = (
            f"Read {self.program_path} and run up to {self.max_experiments} experiments. "
            f"After completing {self.max_experiments} experiments, stop and say DONE. "
            f"This is session {self.session_number} — check index.md for prior knowledge."
        )

        cmd = [claude_path, "--dangerously-skip-permissions", "-p", prompt]
        if extra_args:
            cmd.extend(extra_args)

        try:
            proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            while proc.poll() is None:
                reason = self.check_cycle()
                if reason and reason != "max_experiments":
                    # Force cycle on program change or timeout
                    ts = datetime.now().strftime("%H:%M:%S")
                    print(f"[{ts}] Cycling session: {reason}")
                    proc.send_signal(signal.SIGTERM)
                    try:
                        proc.wait(timeout=30)
                    except subprocess.TimeoutExpired:
                        proc.kill()
                    return reason
                time.sleep(10)
            return self.check_cycle() or "session_ended"
        except Exception as e:
            print(f"Session error: {e}", file=sys.stderr)
            return "error"

    def run_loop(self, claude_path="claude", git_pull=False):
        """Run sessions in a loop forever."""
        while True:
            reason = self.run_session(claude_path=claude_path, git_pull=git_pull)
            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            wiki_dirs = [Path(d) for d in ["concepts", "syntheses", "comparisons", "entities"]]
            summary = build_session_summary(
                wiki_dirs=wiki_dirs,
                results_path=Path("results/results.tsv"),
                session_number=self.session_number,
                experiments_run=self.experiments_run,
                cycle_reason=reason,
            )
            print(f"[{ts}] {summary}")
            print(f"[{ts}] Restarting with fresh context in 5s...")
            time.sleep(5)


def main():
    parser = argparse.ArgumentParser(description="AutoLab Harness — agent session manager")
    parser.add_argument("--program", default="program.md", help="Path to program.md")
    parser.add_argument("--max-experiments", type=int, default=5,
                        help="Max experiments per session before cycling")
    parser.add_argument("--max-duration", type=int, default=1800,
                        help="Max session duration in seconds before cycling")
    parser.add_argument("--claude", default="claude", help="Path to claude binary")
    parser.add_argument("--git-pull", action="store_true", help="Git pull before each session")
    parser.add_argument("--agents", type=int, default=1, help="Number of parallel agents")
    args = parser.parse_args()

    if args.agents == 1:
        sm = SessionManager(args.program, args.max_experiments, args.max_duration)
        sm.run_loop(claude_path=args.claude, git_pull=args.git_pull)
    else:
        import multiprocessing
        procs = []
        for i in range(args.agents):
            sm = SessionManager(args.program, args.max_experiments, args.max_duration)
            p = multiprocessing.Process(target=sm.run_loop,
                                        kwargs={"claude_path": args.claude, "git_pull": args.git_pull})
            p.start()
            procs.append(p)
            time.sleep(3)
        for p in procs:
            p.join()


if __name__ == "__main__":
    main()
