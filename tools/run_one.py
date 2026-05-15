#!/usr/bin/env python3
"""LEAN 4 proof experiment runner for Autoproof.

Usage:
    python tools/run_one.py --status                    # Show proof status
    python tools/run_one.py --build                     # Build and measure sorry count
    python tools/run_one.py --build --file MainTheorem  # Build specific file
    python tools/run_one.py --audit                     # Audit axioms and hypotheses
"""
import argparse
import csv
import subprocess
import re
import sys
from datetime import datetime
from pathlib import Path

LEAN_PROJECT = Path("/Users/taejunsong/workspace/kuramoto-lean")
LEAN_SRC = LEAN_PROJECT / "KuramotoLean"
RESULTS_PATH = Path("results/results.tsv")
COLUMNS = ["timestamp", "experiment", "file", "sorry_count", "axiom_count", "error_count", "status", "description"]


def run_lake_build(file_name=None):
    """Run lake build and return (sorry_count, axiom_count, error_count, output)."""
    cmd = ["lake", "build"]
    if file_name:
        cmd.append(f"KuramotoLean.{file_name}")

    result = subprocess.run(cmd, cwd=LEAN_PROJECT, capture_output=True, text=True, timeout=600)
    output = result.stdout + result.stderr

    sorry_count = len(re.findall(r"declaration uses.*sorry", output))
    error_count = len(re.findall(r"^error:", output, re.MULTILINE))
    # Don't count "Build completed" or "build failed" as errors
    error_count = max(0, error_count - (1 if "build failed" in output else 0))

    return sorry_count, error_count, output


def count_axioms(file_name=None):
    """Count axiom declarations in LEAN files."""
    if file_name:
        files = [LEAN_SRC / f"{file_name}.lean"]
    else:
        files = list(LEAN_SRC.glob("*.lean"))

    total = 0
    for f in files:
        if f.exists():
            content = f.read_text()
            total += len(re.findall(r"^axiom\s", content, re.MULTILINE))
    return total


def count_hypotheses(file_name):
    """Count structure fields (hypotheses) in a LEAN file."""
    f = LEAN_SRC / f"{file_name}.lean"
    if not f.exists():
        return 0
    content = f.read_text()
    return len(re.findall(r"^\s+h\w+\s*:", content, re.MULTILINE))


def show_status():
    """Show current proof status."""
    sorry, errors, output = run_lake_build("MainTheorem")
    axioms = count_axioms("MainTheorem")
    hyps = count_hypotheses("MainTheorem")

    print(f"MainTheorem: {sorry} sorry, {axioms} axioms, {errors} errors, {hyps} hypotheses")

    if RESULTS_PATH.exists():
        with open(RESULTS_PATH) as f:
            rows = list(csv.DictReader(f, delimiter="\t"))
        print(f"Experiments: {len(rows)}")
        if rows:
            best = min(rows, key=lambda r: int(r.get("sorry_count", 999)))
            print(f"Best: {best.get('sorry_count', '?')} sorry ({best.get('description', '')})")
    else:
        print("No experiments yet.")

    # Full project
    sorry_full, errors_full, _ = run_lake_build()
    axioms_full = count_axioms()
    print(f"Full project: {sorry_full} sorry, {axioms_full} axioms, {errors_full} errors")


def audit():
    """Audit all axioms for grounding on published theorems."""
    files = sorted(LEAN_SRC.glob("*.lean"))
    print("=== AXIOM AUDIT ===")
    total = 0
    for f in files:
        content = f.read_text()
        axioms = re.findall(r"^(axiom\s+\w+.*?)(?=\n\n|\ntheorem|\naxiom|\ndef|\nend|\Z)",
                           content, re.MULTILINE | re.DOTALL)
        if axioms:
            print(f"\n--- {f.name} ---")
            for ax in axioms:
                lines = ax.strip().split("\n")
                name = lines[0].split()[1] if len(lines[0].split()) > 1 else "?"
                has_citation = bool(re.search(r"\[.*\d{4}.*\]", ax))
                status = "CITED" if has_citation else "UNCITED"
                print(f"  {status}: {name}")
                total += 1
    print(f"\nTotal axioms: {total}")

    # Check hypotheses in proof assembly
    assembly = LEAN_SRC / "ProofAssembly.lean"
    if assembly.exists():
        content = assembly.read_text()
        hyps = re.findall(r"^\s+(h\w+)\s*:", content, re.MULTILINE)
        print(f"\nFullKuramotoData hypotheses: {len(hyps)}")
        for h in hyps:
            print(f"  {h}")


def build_experiment(file_name=None, description=""):
    """Run a build experiment and log results."""
    target = file_name or "full"
    sorry, errors, output = run_lake_build(file_name)
    axioms = count_axioms(file_name) if file_name else count_axioms()

    status = "keep" if errors == 0 else "crash"
    print(f"sorry={sorry} axioms={axioms} errors={errors} status={status}")

    if "Build completed" in output:
        print("Build: SUCCESS")
    else:
        print("Build: FAILED")
        # Show last errors
        for line in output.split("\n"):
            if "error:" in line:
                print(f"  {line.strip()}")

    # Log to results
    RESULTS_PATH.parent.mkdir(exist_ok=True)
    write_header = not RESULTS_PATH.exists()
    with open(RESULTS_PATH, "a") as f:
        if write_header:
            f.write("\t".join(COLUMNS) + "\n")
        exp_num = sum(1 for _ in open(RESULTS_PATH)) if RESULTS_PATH.exists() else 1
        f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S}\texp{exp_num:03d}\t{target}\t{sorry}\t{axioms}\t{errors}\t{status}\t{description}\n")

    return sorry


def main():
    parser = argparse.ArgumentParser(description="Autoproof LEAN experiment runner")
    parser.add_argument("--status", action="store_true", help="Show proof status")
    parser.add_argument("--build", action="store_true", help="Build and measure")
    parser.add_argument("--audit", action="store_true", help="Audit axioms")
    parser.add_argument("--file", type=str, default=None, help="Specific LEAN file (without .lean)")
    parser.add_argument("--desc", type=str, default="", help="Experiment description")
    args = parser.parse_args()

    if args.status:
        show_status()
    elif args.audit:
        audit()
    elif args.build:
        build_experiment(args.file, args.desc)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
