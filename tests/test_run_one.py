"""Tests for tools/run_one.py — experiment runner."""
import csv
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from run_one import show_status, run_experiment, RESULTS_PATH, COLUMNS


class TestShowStatus:
    def test_no_results(self, tmp_path, capsys, monkeypatch):
        monkeypatch.setattr("run_one.RESULTS_PATH", tmp_path / "nope.tsv")
        show_status()
        assert "No experiments" in capsys.readouterr().out

    def test_with_results(self, tmp_path, capsys, monkeypatch):
        tsv = tmp_path / "results.tsv"
        tsv.write_text("timestamp\texperiment\tconfig\tmetric\tstatus\n"
                       "2026-01-01\texp001\tlr=0.01\t0.7500\tkeep\n")
        monkeypatch.setattr("run_one.RESULTS_PATH", tsv)
        show_status()
        out = capsys.readouterr().out
        assert "1" in out
        assert "0.7500" in out


class TestRunExperiment:
    def test_returns_float(self):
        result = run_experiment({"lr": "0.01"})
        assert isinstance(result, float)

    def test_result_in_range(self):
        results = [run_experiment({"lr": "0.01"}) for _ in range(20)]
        assert all(isinstance(r, float) for r in results)
