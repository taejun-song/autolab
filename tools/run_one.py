#!/usr/bin/env python3
"""Template experiment runner for AutoLab.

Replace this with your domain-specific experiment tool.
The agent calls this CLI to run individual experiments.

Usage:
    python tools/run_one.py --status              # Show experiment status
    python tools/run_one.py --config lr=0.01 bs=32  # Run one experiment
"""
import argparse
import csv
import random
import sys
from datetime import datetime
from pathlib import Path

RESULTS_PATH = Path("results/results.tsv")
COLUMNS = ["timestamp", "experiment", "config", "metric", "status"]


def show_status():
    if not RESULTS_PATH.exists():
        print("No experiments yet.")
        return
    best = None
    count = 0
    with open(RESULTS_PATH) as f:
        for row in csv.DictReader(f, delimiter="\t"):
            count += 1
            val = float(row.get("metric", 0))
            if best is None or val > best:
                best = val
    print(f"Experiments: {count}")
    print(f"Best metric: {best:.4f}" if best else "No results")


def run_experiment(config):
    """Replace this with your actual experiment logic."""
    # This is a placeholder — replace with your domain code
    metric = random.gauss(0.5, 0.1)
    return metric


def main():
    parser = argparse.ArgumentParser(description="AutoLab experiment runner")
    parser.add_argument("--status", action="store_true")
    parser.add_argument("--config", nargs="*", help="key=value pairs")
    args = parser.parse_args()

    if args.status:
        show_status()
        return

    if not args.config:
        parser.error("Provide --config or --status")

    config = dict(kv.split("=") for kv in args.config)
    config_str = " ".join(f"{k}={v}" for k, v in config.items())

    print(f"Running experiment: {config_str}")
    metric = run_experiment(config)

    RESULTS_PATH.parent.mkdir(exist_ok=True)
    write_header = not RESULTS_PATH.exists()
    with open(RESULTS_PATH, "a") as f:
        if write_header:
            f.write("\t".join(COLUMNS) + "\n")
        exp_id = f"exp{sum(1 for _ in open(RESULTS_PATH)) if RESULTS_PATH.exists() else 1:03d}"
        f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S}\t{exp_id}\t{config_str}\t{metric:.4f}\tkeep\n")

    print(f"Result: metric={metric:.4f}")


if __name__ == "__main__":
    main()
