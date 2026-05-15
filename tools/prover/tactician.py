"""Codex's role: generate tactic candidates for a given goal state."""
import subprocess
from dataclasses import dataclass
from pathlib import Path

from .pantograph import GoalState, TacticResult


@dataclass
class TacticAttempt:
    goal: GoalState
    tactic: str
    result: TacticResult

    @property
    def succeeded(self) -> bool:
        return self.result.success and self.result.is_complete

    @property
    def error_message(self) -> str:
        return self.result.error or ""


class Tactician:
    """Uses Codex (GPT-5.4) to generate tactic candidates for Lean 4 goals."""

    def __init__(self, model: str = "codex", retries: int = 5):
        self.model = model
        self.retries = retries

    def generate_tactics(self, goal: GoalState, context: str = "", errors: list[str] = None) -> list[str]:
        """Generate candidate tactics for a goal state."""
        prompt = self._build_prompt(goal, context, errors or [])
        return self._call_model(prompt)

    def _build_prompt(self, goal: GoalState, context: str, errors: list[str]) -> str:
        parts = [
            f"Goal: {goal.goal_type}",
            f"Hypotheses: {', '.join(goal.hypotheses) or 'none'}",
        ]
        if context:
            parts.append(f"Context: {context}")
        if errors:
            parts.append(f"Previous failures: {'; '.join(errors)}")
        parts.append(
            "Generate 3-5 Lean 4 tactics that could close this goal. "
            "One tactic per line. No explanation."
        )
        return "\n".join(parts)

    def _call_model(self, prompt: str) -> list[str]:
        """Call Codex via CLI to generate tactics."""
        try:
            result = subprocess.run(
                ["codex", "exec", "--dangerously-bypass-approvals-and-sandbox", prompt],
                capture_output=True, text=True, timeout=60,
            )
            output = result.stdout.strip()
            tactics = [l.strip() for l in output.split("\n") if l.strip() and not l.startswith("#")]
            return tactics[:5] if tactics else ["sorry"]
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return ["sorry"]
