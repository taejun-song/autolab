"""Claude's role: decompose theorems into sub-goals and manage proof strategy."""
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from .wiki_retriever import WikiRetriever


@dataclass
class SubGoal:
    name: str
    goal: str
    dependencies: list[str] = field(default_factory=list)
    status: str = "pending"  # pending | proved | stuck


@dataclass
class ProofPlan:
    theorem: str
    sketch: str
    subgoals: list[SubGoal]

    def to_prompt(self) -> str:
        lines = [
            f"Theorem: {self.theorem}",
            f"Sketch: {self.sketch}",
            "Sub-goals:",
        ]
        for i, sg in enumerate(self.subgoals, 1):
            lines.append(f"  {i}. [{sg.name}] {sg.goal}")
        return "\n".join(lines)


class Orchestrator:
    """Uses Claude (Sonnet) to plan proof strategy. Minimizes token usage."""

    def __init__(self, wiki_root: Path, model: str = "sonnet"):
        self.wiki_root = wiki_root
        self.model = model
        self.retriever = WikiRetriever(wiki_root)

    def plan(self, theorem_name: str, goal_state: str) -> ProofPlan:
        """Generate a proof plan by consulting wiki and decomposing the goal."""
        wiki_context = self._gather_context(theorem_name)
        failures = self._gather_failures(theorem_name)
        prompt = self._build_planning_prompt(theorem_name, goal_state, wiki_context, failures)
        response = self._call_claude(prompt)
        return self._parse_plan(theorem_name, response)

    def _gather_context(self, theorem_name: str) -> str:
        pages = self.retriever.retrieve(theorem_name, top_k=3)
        if not pages:
            return "(no wiki context found)"
        parts = []
        for p in pages:
            parts.append(f"## {p.title}\n{p.content[:500]}")
        return "\n\n".join(parts)

    def _gather_failures(self, theorem_name: str) -> str:
        failures = self.retriever.retrieve_failures(theorem_name)
        if not failures:
            return "(no recorded failures)"
        return "\n".join(f"- FAILED: {f.title}" for f in failures)

    def _build_planning_prompt(self, theorem: str, goal: str, context: str, failures: str) -> str:
        return f"""You are a proof strategist. Decompose this Lean 4 theorem into sub-goals.

THEOREM: {theorem}
GOAL STATE: {goal}

WIKI CONTEXT:
{context}

KNOWN FAILED STRATEGIES:
{failures}

Output a proof sketch (1-3 sentences) then a numbered list of sub-goals.
Each sub-goal: name, formal goal statement, dependencies on other sub-goals.
Be concise. Do NOT generate Lean code — just the plan."""

    def _call_claude(self, prompt: str) -> str:
        """Call Claude via CLI. Uses sonnet to save tokens."""
        try:
            result = subprocess.run(
                ["claude", "-p", "--model", self.model, prompt],
                capture_output=True, text=True, timeout=60,
            )
            return result.stdout.strip()
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return ""

    def _parse_plan(self, theorem: str, response: str) -> ProofPlan:
        """Parse Claude's response into a structured plan."""
        lines = response.strip().split("\n")
        sketch = lines[0] if lines else "No sketch"
        subgoals = []
        for line in lines[1:]:
            line = line.strip()
            if not line or not (line[0].isdigit() or line.startswith("-")):
                continue
            # Extract name in brackets if present
            import re
            m = re.match(r'[\d.\-]+\s*\[(\w+)\]\s*(.*)', line)
            if m:
                subgoals.append(SubGoal(name=m.group(1), goal=m.group(2)))
            else:
                name = f"step_{len(subgoals)+1}"
                subgoals.append(SubGoal(name=name, goal=line.lstrip("0123456789.-) ")))
        if not subgoals:
            subgoals = [SubGoal(name="main", goal=theorem)]
        return ProofPlan(theorem=theorem, sketch=sketch, subgoals=subgoals)
