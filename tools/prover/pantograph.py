"""Lean 4 interface via Pantograph (or fallback to grep-based sorry extraction)."""
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class GoalState:
    theorem_name: str
    goal_type: str
    hypotheses: list[str]
    file_path: Path
    line: int
    is_solved: bool = False


@dataclass
class TacticResult:
    success: bool
    new_goals: Optional[list[GoalState]]
    error: Optional[str]

    @property
    def is_complete(self) -> bool:
        return self.success and (self.new_goals is None or len(self.new_goals) == 0)


class PantographClient:
    """Interface to Lean 4 proof states. Falls back to regex extraction if Pantograph unavailable."""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self._pantograph_available = self._check_pantograph()

    def _check_pantograph(self) -> bool:
        try:
            result = subprocess.run(
                ["pantograph", "--version"],
                capture_output=True, text=True, timeout=5,
            )
            return result.returncode == 0
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False

    def find_sorries(self, file_path: Path) -> list[GoalState]:
        """Extract sorry locations from a Lean file."""
        if not file_path.exists():
            return []
        content = file_path.read_text()
        lines = content.split("\n")
        sorries = []
        current_theorem = None
        current_type = ""
        in_block_comment = False
        for i, line in enumerate(lines, 1):
            if "/-" in line and "-/" not in line:
                in_block_comment = True
                continue
            if "-/" in line:
                in_block_comment = False
                continue
            if in_block_comment:
                continue
            code = line.split("--")[0]
            thm_match = re.match(
                r"^(theorem|lemma|def)\s+(\w+)", line
            )
            if thm_match:
                current_theorem = thm_match.group(2)
                # Extract type: everything after the first `:` up to `:=` or `where`
                type_match = re.search(r":\s*(.+?)(?:\s*:=|\s*where\s*$|$)", line)
                current_type = type_match.group(1).strip() if type_match else ""
                # Multi-line type: scan forward
                if not current_type or current_type.endswith(","):
                    for j in range(i, min(i + 10, len(lines))):
                        next_line = lines[j].split("--")[0].strip()
                        if ":=" in next_line or "sorry" in next_line:
                            break
                        current_type += " " + next_line
            if re.search(r"\bsorry\b", code) and current_theorem:
                sorries.append(GoalState(
                    theorem_name=current_theorem,
                    goal_type=current_type,
                    hypotheses=[],
                    file_path=file_path,
                    line=i,
                ))
        return sorries

    def try_tactic(self, goal: GoalState, tactic: str) -> TacticResult:
        """Try a tactic on a goal state. Uses Pantograph if available, else lake build."""
        if self._pantograph_available:
            return self._try_via_pantograph(goal, tactic)
        return self._try_via_build(goal, tactic)

    def _try_via_pantograph(self, goal: GoalState, tactic: str) -> TacticResult:
        """Use Pantograph JSON-RPC to try a tactic."""
        # TODO: implement full Pantograph protocol
        # For now, fall back to build
        return self._try_via_build(goal, tactic)

    def _try_via_build(self, goal: GoalState, tactic: str) -> TacticResult:
        """Replace sorry with tactic and try lake build."""
        content = goal.file_path.read_text()
        lines = content.split("\n")
        original_line = lines[goal.line - 1]
        lines[goal.line - 1] = original_line.replace("sorry", tactic, 1)
        goal.file_path.write_text("\n".join(lines))
        try:
            result = subprocess.run(
                ["lake", "build", f"KuramotoLean.{goal.file_path.stem}"],
                cwd=self.project_root,
                capture_output=True, text=True, timeout=300,
            )
            output = result.stdout + result.stderr
            if result.returncode == 0 and "error" not in output.lower():
                return TacticResult(success=True, new_goals=[], error=None)
            else:
                error_lines = [l for l in output.split("\n") if "error" in l.lower()]
                return TacticResult(
                    success=False, new_goals=None,
                    error="\n".join(error_lines[:3]) or "build failed",
                )
        except subprocess.TimeoutExpired:
            return TacticResult(success=False, new_goals=None, error="timeout")
        finally:
            goal.file_path.write_text(content)
