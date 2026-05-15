"""TDD tests for the prover agent system."""
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

from prover.pantograph import PantographClient, GoalState, TacticResult
from prover.wiki_retriever import WikiRetriever
from prover.orchestrator import Orchestrator, ProofPlan, SubGoal
from prover.tactician import Tactician, TacticAttempt
from prover.runner import ProverRunner


class TestPantographClient:
    def test_extract_sorries_from_file(self, tmp_path):
        lean_file = tmp_path / "Test.lean"
        lean_file.write_text(
            "theorem foo : 1 + 1 = 2 := by sorry\n"
            "theorem bar : 2 + 2 = 4 := by\n  sorry\n"
        )
        client = PantographClient(project_root=tmp_path)
        sorries = client.find_sorries(lean_file)
        assert len(sorries) == 2
        assert sorries[0].theorem_name == "foo"
        assert sorries[1].theorem_name == "bar"

    def test_goal_state_from_sorry(self):
        state = GoalState(
            theorem_name="foo",
            goal_type="1 + 1 = 2",
            hypotheses=[],
            file_path=Path("Test.lean"),
            line=1,
        )
        assert state.goal_type == "1 + 1 = 2"
        assert state.is_solved is False

    def test_tactic_result_success(self):
        result = TacticResult(success=True, new_goals=[], error=None)
        assert result.success is True
        assert result.is_complete is True

    def test_tactic_result_failure(self):
        result = TacticResult(success=False, new_goals=None, error="unknown tactic")
        assert result.success is False
        assert result.is_complete is False

    def test_tactic_result_partial(self):
        remaining = [GoalState("foo", "n = n", [], Path("T.lean"), 1)]
        result = TacticResult(success=True, new_goals=remaining, error=None)
        assert result.success is True
        assert result.is_complete is False


class TestWikiRetriever:
    def test_retrieve_relevant_pages(self, tmp_path):
        concepts = tmp_path / "concepts"
        concepts.mkdir()
        (concepts / "pair-bound.md").write_text(
            "---\ntype: concept\ntitle: Pair Bound\ntags: [lyapunov]\n---\n"
            "# Pair Bound\nThe pair bound shows dV/dt <= 0.\n"
        )
        (concepts / "tail-body-split.md").write_text(
            "---\ntype: concept\ntitle: Tail-Body Split\ntags: [continuum]\n---\n"
            "# Tail-Body Split\nSplit integral into body and tail.\n"
        )
        retriever = WikiRetriever(wiki_root=tmp_path)
        results = retriever.retrieve("Lyapunov function dV/dt", top_k=1)
        assert len(results) == 1
        assert "pair-bound" in results[0].slug

    def test_retrieve_returns_empty_for_no_match(self, tmp_path):
        retriever = WikiRetriever(wiki_root=tmp_path)
        results = retriever.retrieve("quantum gravity", top_k=5)
        assert results == []

    def test_retrieve_syntheses_for_failed_strategies(self, tmp_path):
        syntheses = tmp_path / "syntheses"
        syntheses.mkdir()
        (syntheses / "continuum-stability-debate.md").write_text(
            "---\ntype: synthesis\ntitle: Debate\ntags: [h_body_absorb]\n---\n"
            "# Debate\nFailed: uniform persistence is impossible.\n"
        )
        retriever = WikiRetriever(wiki_root=tmp_path)
        results = retriever.retrieve_failures("h_body_absorb")
        assert len(results) == 1
        assert "impossible" in results[0].content


class TestOrchestrator:
    def test_decompose_produces_subgoals(self):
        orch = Orchestrator(wiki_root=Path("."), model="sonnet")
        plan = ProofPlan(
            theorem="h_body_absorb",
            sketch="Use Gronwall on body, control tail by integrability",
            subgoals=[
                SubGoal(name="body_gronwall", goal="V_body(t) ≤ V_body(0) * exp(-ct) + err"),
                SubGoal(name="tail_vanish", goal="∫_{|ω|>M} |α-α*|² g → 0 as M→∞"),
            ],
        )
        assert len(plan.subgoals) == 2
        assert plan.subgoals[0].name == "body_gronwall"

    def test_plan_serializes_to_prompt(self):
        plan = ProofPlan(
            theorem="h_body_absorb",
            sketch="Gronwall + tail",
            subgoals=[SubGoal(name="g1", goal="goal1")],
        )
        prompt = plan.to_prompt()
        assert "h_body_absorb" in prompt
        assert "goal1" in prompt


class TestTactician:
    def test_generate_tactics_returns_candidates(self):
        tact = Tactician(model="codex")
        goal = GoalState("foo", "1 + 1 = 2", [], Path("T.lean"), 1)
        with patch.object(tact, '_call_model', return_value=["norm_num", "simp", "omega"]):
            candidates = tact.generate_tactics(goal, context="")
            assert len(candidates) == 3
            assert "norm_num" in candidates

    def test_attempt_records_success(self):
        attempt = TacticAttempt(
            goal=GoalState("foo", "1+1=2", [], Path("T.lean"), 1),
            tactic="norm_num",
            result=TacticResult(success=True, new_goals=[], error=None),
        )
        assert attempt.succeeded is True

    def test_attempt_records_failure(self):
        attempt = TacticAttempt(
            goal=GoalState("foo", "1+1=2", [], Path("T.lean"), 1),
            tactic="ring",
            result=TacticResult(success=False, new_goals=None, error="type mismatch"),
        )
        assert attempt.succeeded is False
        assert "type mismatch" in attempt.error_message


class TestProverRunner:
    def test_runner_stops_when_no_sorries(self, tmp_path):
        runner = ProverRunner(
            project_root=tmp_path,
            wiki_root=tmp_path,
            max_attempts=10,
        )
        with patch.object(runner.pantograph, 'find_sorries', return_value=[]):
            result = runner.run(Path("Test.lean"))
            assert result.sorry_count == 0
            assert result.status == "complete"

    def test_runner_respects_max_attempts(self, tmp_path):
        runner = ProverRunner(
            project_root=tmp_path,
            wiki_root=tmp_path,
            max_attempts=1,
        )
        fake_sorry = GoalState("foo", "False", [], Path("T.lean"), 1)
        fake_sorry2 = GoalState("bar", "False", [], Path("T.lean"), 2)
        with patch.object(runner.pantograph, 'find_sorries', return_value=[fake_sorry, fake_sorry2]):
            with patch.object(runner.tactician, 'generate_tactics', return_value=["sorry"]):
                with patch.object(runner.pantograph, 'try_tactic',
                                  return_value=TacticResult(False, None, "fail")):
                    result = runner.run(Path("T.lean"))
                    assert result.status == "stuck"
                    assert result.attempts_used == 1

    def test_runner_logs_to_wiki_on_success(self, tmp_path):
        log_file = tmp_path / "log.md"
        log_file.write_text("# Log\n")
        runner = ProverRunner(
            project_root=tmp_path,
            wiki_root=tmp_path,
            max_attempts=10,
        )
        with patch.object(runner.pantograph, 'find_sorries', return_value=[]):
            runner.run(Path("Test.lean"))
        assert log_file.read_text() != "# Log\n"
