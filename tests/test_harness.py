"""Tests for tools/harness.py — agent session manager."""
import json
import time
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from harness import (
    SessionManager,
    should_cycle,
    get_program_mtime,
    build_session_summary,
)


class TestGetProgramMtime:
    def test_returns_mtime(self, tmp_path):
        f = tmp_path / "program.md"
        f.write_text("hello")
        mt = get_program_mtime(f)
        assert isinstance(mt, float)
        assert mt > 0

    def test_returns_zero_for_missing(self, tmp_path):
        assert get_program_mtime(tmp_path / "nope.md") == 0.0


class TestShouldCycle:
    def test_cycles_on_program_change(self):
        assert should_cycle(
            experiments_run=1,
            max_experiments=10,
            session_start=time.time(),
            max_duration=3600,
            program_changed=True,
        ) == "program_changed"

    def test_cycles_on_max_experiments(self):
        assert should_cycle(
            experiments_run=10,
            max_experiments=10,
            session_start=time.time(),
            max_duration=3600,
            program_changed=False,
        ) == "max_experiments"

    def test_no_timeout(self):
        assert should_cycle(
            experiments_run=1,
            max_experiments=10,
            session_start=time.time() - 7200,
            max_duration=3600,
            program_changed=False,
        ) is None

    def test_no_cycle_when_ok(self):
        assert should_cycle(
            experiments_run=3,
            max_experiments=10,
            session_start=time.time(),
            max_duration=3600,
            program_changed=False,
        ) is None


class TestBuildSessionSummary:
    def test_includes_fields(self, tmp_path):
        wiki_dir = tmp_path / "concepts"
        wiki_dir.mkdir()
        (wiki_dir / "test.md").write_text("---\ntitle: Test\n---\n# Test\nSummary.")
        results = tmp_path / "results.tsv"
        results.write_text("h1\th2\nv1\tv2\n")
        summary = build_session_summary(
            wiki_dirs=[wiki_dir],
            results_path=results,
            session_number=3,
            experiments_run=5,
            cycle_reason="max_experiments",
        )
        assert "session 3" in summary.lower() or "Session 3" in summary
        assert "5" in summary
        assert "max_experiments" in summary

    def test_empty_wiki(self, tmp_path):
        summary = build_session_summary(
            wiki_dirs=[tmp_path / "concepts"],
            results_path=tmp_path / "nope.tsv",
            session_number=1,
            experiments_run=0,
            cycle_reason="timeout",
        )
        assert isinstance(summary, str)


class TestSessionManager:
    def test_init(self, tmp_path):
        program = tmp_path / "program.md"
        program.write_text("# Test")
        sm = SessionManager(
            program_path=program,
            max_experiments=5,
            max_duration=1800,
        )
        assert sm.experiments_run == 0
        assert sm.session_number == 0

    def test_check_cycle_returns_none_initially(self, tmp_path):
        program = tmp_path / "program.md"
        program.write_text("# Test")
        sm = SessionManager(program_path=program, max_experiments=5, max_duration=1800)
        sm.start_session()
        assert sm.check_cycle() is None

    def test_check_cycle_on_experiment_count(self, tmp_path):
        program = tmp_path / "program.md"
        program.write_text("# Test")
        sm = SessionManager(program_path=program, max_experiments=3, max_duration=1800)
        sm.start_session()
        sm.experiments_run = 3
        assert sm.check_cycle() == "max_experiments"

    def test_detects_program_change(self, tmp_path):
        program = tmp_path / "program.md"
        program.write_text("# Version 1")
        sm = SessionManager(program_path=program, max_experiments=10, max_duration=1800)
        sm.start_session()
        time.sleep(0.1)
        program.write_text("# Version 2 — added new tool")
        assert sm.check_cycle() == "program_changed"

    def test_log_session_writes_jsonl(self, tmp_path):
        program = tmp_path / "program.md"
        program.write_text("# Test")
        log = tmp_path / "harness.jsonl"
        sm = SessionManager(program_path=program, max_experiments=5, max_duration=1800,
                            log_path=log)
        sm.start_session()
        sm.experiments_run = 3
        sm.log_session("max_experiments", 120.5)
        assert log.exists()
        import json
        entry = json.loads(log.read_text().strip())
        assert entry["session"] == 1
        assert entry["experiments_run"] == 3
        assert entry["cycle_reason"] == "max_experiments"
        assert entry["duration_seconds"] == 120.5

    def test_history_accumulates(self, tmp_path):
        program = tmp_path / "program.md"
        program.write_text("# Test")
        sm = SessionManager(program_path=program, max_experiments=5, max_duration=1800,
                            log_path=tmp_path / "h.jsonl")
        sm.start_session()
        sm.log_session("max_experiments", 60.0)
        sm.start_session()
        sm.log_session("program_changed", 30.0)
        assert len(sm.history) == 2
        assert sm.history[0]["cycle_reason"] == "max_experiments"
        assert sm.history[1]["cycle_reason"] == "program_changed"

    def test_session_counter_increments(self, tmp_path):
        program = tmp_path / "program.md"
        program.write_text("# Test")
        sm = SessionManager(program_path=program, max_experiments=5, max_duration=1800)
        sm.start_session()
        assert sm.session_number == 1
        sm.start_session()
        assert sm.session_number == 2
