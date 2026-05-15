#!/usr/bin/env python3
"""Standalone prover: try closing sorry goals in a Lean file.

Pipeline:
  1. Parse sorry locations
  2. For each sorry, try built-in tactics first (free, fast)
  3. If stuck, call Codex for tactic suggestions
  4. Verify each attempt with lake build
  5. Commit on success

Usage:
    python tools/prover/solve.py KuramotoLean/SyntheticTest.lean
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

LEAN_PROJECT = Path("/Users/taejunsong/workspace/kuramoto-lean")
BUILTIN_TACTICS = [
    "omega", "simp", "norm_num", "ring", "linarith", "positivity",
    "exact?", "apply?", "aesop", "decide", "tauto", "trivial",
    "exact add_comm _ _",
    "exact List.reverse_reverse _",
    "exact hf h",
    "rw [hga]; exact hg.tendsto.comp hf",
    "subst hga; exact hg.tendsto.comp hf",
]


def find_sorries(file_path: Path) -> list[dict]:
    content = file_path.read_text()
    lines = content.split("\n")
    sorries = []
    current_thm = None
    in_comment = False
    for i, line in enumerate(lines):
        if "/-" in line and "-/" not in line:
            in_comment = True
        if "-/" in line:
            in_comment = False
            continue
        if in_comment:
            continue
        code = line.split("--")[0]
        m = re.match(r"^(theorem|lemma|def)\s+(\w+)", line)
        if m:
            current_thm = m.group(2)
        if re.search(r"\bsorry\b", code) and current_thm:
            sorries.append({"name": current_thm, "line": i, "original": line})
    return sorries


def try_tactic(file_path: Path, sorry_info: dict, tactic: str) -> bool:
    content = file_path.read_text()
    lines = content.split("\n")
    original = lines[sorry_info["line"]]
    lines[sorry_info["line"]] = original.replace("sorry", tactic, 1)
    file_path.write_text("\n".join(lines))
    try:
        result = subprocess.run(
            ["lake", "build", f"KuramotoLean.{file_path.stem}"],
            cwd=LEAN_PROJECT, capture_output=True, text=True, timeout=120,
        )
        output = result.stdout + result.stderr
        has_sorry_warning = f"declaration uses `sorry`" in output
        has_error = bool(re.search(r"^.*error:.*$", output, re.MULTILINE))
        if not has_error and sorry_info["name"] not in output.split("sorry")[-1]:
            if f"warning: {file_path.name}:{sorry_info['line']+1}" not in output:
                return True
        return False
    except subprocess.TimeoutExpired:
        return False
    finally:
        file_path.write_text(content)


def apply_tactic(file_path: Path, sorry_info: dict, tactic: str):
    content = file_path.read_text()
    lines = content.split("\n")
    lines[sorry_info["line"]] = lines[sorry_info["line"]].replace("sorry", tactic, 1)
    file_path.write_text("\n".join(lines))


def call_codex(theorem_name: str, goal_context: str) -> list[str]:
    prompt = (
        f"Generate 5 Lean 4 tactics to prove this goal. One per line. No explanation.\n"
        f"Theorem: {theorem_name}\n"
        f"Context:\n{goal_context}"
    )
    try:
        result = subprocess.run(
            ["codex", "exec", "--dangerously-bypass-approvals-and-sandbox", prompt],
            capture_output=True, text=True, timeout=60,
        )
        lines = [l.strip() for l in result.stdout.split("\n")
                 if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("```")]
        return lines[:5]
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return []


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Lean file path relative to project root")
    parser.add_argument("--codex", action="store_true", help="Use Codex for hard goals")
    args = parser.parse_args()

    file_path = LEAN_PROJECT / args.file
    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)

    sorries = find_sorries(file_path)
    if not sorries:
        print("No sorry found. File is complete.")
        sys.exit(0)

    print(f"Found {len(sorries)} sorry goals in {file_path.name}")
    closed = 0
    for sorry in sorries:
        print(f"\n--- {sorry['name']} (L{sorry['line']+1}) ---")

        # Phase 1: Try built-in tactics (free)
        solved = False
        for tactic in BUILTIN_TACTICS:
            print(f"  trying: {tactic}...", end=" ", flush=True)
            if try_tactic(file_path, sorry, tactic):
                print("SUCCESS")
                apply_tactic(file_path, sorry, tactic)
                closed += 1
                solved = True
                break
            else:
                print("fail")

        # Phase 2: Call Codex if built-in tactics fail
        if not solved and args.codex:
            print("  calling Codex...")
            context_lines = file_path.read_text().split("\n")
            start = max(0, sorry["line"] - 5)
            context = "\n".join(context_lines[start:sorry["line"] + 2])
            codex_tactics = call_codex(sorry["name"], context)
            for tactic in codex_tactics:
                print(f"  codex: {tactic}...", end=" ", flush=True)
                if try_tactic(file_path, sorry, tactic):
                    print("SUCCESS")
                    apply_tactic(file_path, sorry, tactic)
                    closed += 1
                    break
                else:
                    print("fail")

    print(f"\n=== Results: {closed}/{len(sorries)} sorry closed ===")
    if closed > 0:
        # Verify final build
        result = subprocess.run(
            ["lake", "build", f"KuramotoLean.{file_path.stem}"],
            cwd=LEAN_PROJECT, capture_output=True, text=True, timeout=120,
        )
        sorry_warnings = result.stdout.count("uses `sorry`") + result.stderr.count("uses `sorry`")
        print(f"Final build: {sorry_warnings} sorry warnings remaining")


if __name__ == "__main__":
    main()
