"""Main proving loop: orchestrate Claude (plan) → Codex (tactics) → Lean (verify) → Wiki (log)."""
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from .pantograph import PantographClient, GoalState, TacticResult
from .orchestrator import Orchestrator
from .tactician import Tactician
from .wiki_retriever import WikiRetriever


@dataclass
class ProveResult:
    sorry_count: int
    status: str  # "complete" | "partial" | "stuck"
    attempts_used: int
    closed: list[str]
    remaining: list[str]


class ProverRunner:
    """Main loop: find sorries → generate tactics → verify → repeat."""

    def __init__(self, project_root: Path, wiki_root: Path, max_attempts: int = 50):
        self.project_root = project_root
        self.wiki_root = wiki_root
        self.max_attempts = max_attempts
        self.pantograph = PantographClient(project_root)
        self.orchestrator = Orchestrator(wiki_root)
        self.tactician = Tactician()
        self.retriever = WikiRetriever(wiki_root)

    def run(self, file_path: Path) -> ProveResult:
        """Attempt to close all sorries in a file."""
        sorries = self.pantograph.find_sorries(file_path)
        if not sorries:
            self._log_success(file_path, [])
            return ProveResult(sorry_count=0, status="complete", attempts_used=0, closed=[], remaining=[])

        closed = []
        attempts = 0
        for goal in sorries:
            if attempts >= self.max_attempts:
                break
            success = self._try_close_goal(goal, attempts)
            attempts += 1
            if success:
                closed.append(goal.theorem_name)

        remaining_sorries = self.pantograph.find_sorries(file_path)
        remaining = [s.theorem_name for s in remaining_sorries]
        status = "complete" if not remaining else ("partial" if closed else "stuck")

        if status == "complete":
            self._log_success(file_path, closed)
        elif status == "stuck":
            self._log_failure(file_path, remaining)

        return ProveResult(
            sorry_count=len(remaining),
            status=status,
            attempts_used=attempts,
            closed=closed,
            remaining=remaining,
        )

    def _try_close_goal(self, goal: GoalState, attempt_num: int) -> bool:
        """Try to close a single sorry goal."""
        context = self._get_context(goal)
        errors = []
        for _ in range(min(self.tactician.retries, self.max_attempts - attempt_num)):
            tactics = self.tactician.generate_tactics(goal, context, errors)
            for tactic in tactics:
                if tactic == "sorry":
                    continue
                result = self.pantograph.try_tactic(goal, tactic)
                if result.is_complete:
                    return True
                if result.error:
                    errors.append(f"{tactic}: {result.error}")
        return False

    def _get_context(self, goal: GoalState) -> str:
        """Retrieve wiki context relevant to this goal."""
        pages = self.retriever.retrieve(f"{goal.theorem_name} {goal.goal_type}", top_k=2)
        if not pages:
            return ""
        return "\n".join(p.content[:200] for p in pages)

    def _log_success(self, file_path: Path, closed: list[str]):
        """Append success to wiki log."""
        log = self.wiki_root / "log.md"
        if not log.exists():
            return
        entry = (
            f"\n## [{date.today()}] experiment | prover closed {len(closed)} sorry in {file_path.stem}\n"
            f"- closed: {', '.join(closed) or 'all already done'}\n"
        )
        with open(log, "a") as f:
            f.write(entry)

    def _log_failure(self, file_path: Path, remaining: list[str]):
        """Log failure for wiki synthesis."""
        log = self.wiki_root / "log.md"
        if not log.exists():
            return
        entry = (
            f"\n## [{date.today()}] experiment | prover stuck on {file_path.stem}\n"
            f"- remaining: {', '.join(remaining)}\n"
        )
        with open(log, "a") as f:
            f.write(entry)
