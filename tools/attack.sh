#!/bin/bash
# attack.sh — One-command automated proof research loop
# Usage: ./tools/attack.sh [TARGET_FILE] [MAX_TURNS]
#
# Integrates all three layers:
#   Layer 1 (wiki): logs experiments, updates syntheses
#   Layer 2 (lean): writes/builds proof attempts
#   Layer 3 (loop): Codex implements, Gemini reviews, iterate

set -euo pipefail

TARGET="${1:-ComplexPairBoundProof}"
MAX_TURNS="${2:-20}"
LEAN_DIR="/Users/taejunsong/workspace/kuramoto-lean"
WIKI_DIR="/Users/taejunsong/workspace/autoproof"
LOG="$WIKI_DIR/results/attack-${TARGET}-$(date +%Y%m%d-%H%M%S).log"
QA="/tmp/attack-$$"

mkdir -p "$QA" "$(dirname "$LOG")"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
nvm use 20 2>/dev/null || true

# --- Metrics ---
get_sorry_count() {
  cd "$LEAN_DIR"
  lake build "KuramotoLean.${TARGET}" 2>&1 | grep -c "declaration uses.*sorry" || echo 0
}

get_error_count() {
  cd "$LEAN_DIR"
  lake build "KuramotoLean.${TARGET}" 2>&1 | grep -c "^error:" || echo 0
}

# --- Initial state ---
INITIAL_SORRY=$(get_sorry_count)
echo "[$(date)] attack.sh started" | tee "$LOG"
echo "[$(date)] target: $TARGET | sorry: $INITIAL_SORRY | max_turns: $MAX_TURNS" | tee -a "$LOG"

if [ "$INITIAL_SORRY" -eq 0 ]; then
  echo "[$(date)] ALREADY SOLVED (0 sorry). Nothing to do." | tee -a "$LOG"
  exit 0
fi

# --- Read context ---
TARGET_FILE="$LEAN_DIR/KuramotoLean/${TARGET}.lean"
TARGET_CONTENT=$(cat "$TARGET_FILE")
PROGRAM=$(cat "$WIKI_DIR/program.md" | head -50)

# --- Loop ---
TURN=0
while [ $TURN -lt $MAX_TURNS ]; do
  TURN=$((TURN + 1))
  echo "[$(date)] === Turn $TURN ===" | tee -a "$LOG"

  PREV_GEMINI=$(cat "$QA/gemini-latest.txt" 2>/dev/null | tail -30 || echo "No previous feedback.")
  CURRENT_FILE=$(cat "$TARGET_FILE")
  SORRY_NOW=$(get_sorry_count)

  if [ "$SORRY_NOW" -eq 0 ]; then
    echo "[$(date)] SOLVED at turn $TURN!" | tee -a "$LOG"
    break
  fi

  # --- Phase 1: Codex implements ---
  echo "[$(date)] Codex implementing..." | tee -a "$LOG"

  codex --approval-mode full-auto -q "You are a Lean 4 proof engineer. Your ONLY job: close the sorry in this file.

TARGET FILE: $LEAN_DIR/KuramotoLean/${TARGET}.lean

CURRENT CONTENT:
$CURRENT_FILE

PREVIOUS GEMINI FEEDBACK:
$PREV_GEMINI

RULES:
- Edit ONLY the target file
- Run 'cd $LEAN_DIR && lake build KuramotoLean.${TARGET}' to verify
- If you cannot close the sorry fully, make PARTIAL progress (replace one sorry with a proof + smaller sorry)
- Commit with 'git -C $LEAN_DIR add KuramotoLean/${TARGET}.lean && git -C $LEAN_DIR commit -m \"progress: turn $TURN\"'
- State ONE precise mathematical question for the next iteration

DO NOT create new files. DO NOT modify other files." > "$QA/codex-latest.txt" 2>&1 || true

  echo "[$(date)] Codex done ($(wc -l < "$QA/codex-latest.txt") lines)" | tee -a "$LOG"

  # --- Check progress ---
  SORRY_AFTER=$(get_sorry_count)
  ERRORS_AFTER=$(get_error_count)
  echo "[$(date)] sorry: $SORRY_NOW -> $SORRY_AFTER | errors: $ERRORS_AFTER" | tee -a "$LOG"

  if [ "$SORRY_AFTER" -eq 0 ]; then
    echo "[$(date)] SOLVED at turn $TURN!" | tee -a "$LOG"
    break
  fi

  # --- Phase 2: Gemini reviews ---
  echo "[$(date)] Gemini reviewing..." | tee -a "$LOG"

  CODEX_OUT=$(tail -30 "$QA/codex-latest.txt")
  CURRENT_FILE=$(cat "$TARGET_FILE")

  echo "You are a mathematician reviewing a Lean 4 proof attempt for the Kuramoto complex pair bound.

THE PROBLEM: Prove that V'(t) ≤ 0 for the complex OA equation on the symmetric subspace.
Key fact already proved: rotation cancels (Re(-iω|z-z*|²) = 0).
After rotation cancels, V' involves K-coupling terms.
The real pair bound (for α ∈ (0,1)) IS proved. Need complex extension.

CURRENT LEAN FILE:
$CURRENT_FILE

CODEX OUTPUT:
$CODEX_OUT

YOUR TASKS:
1. Is the approach mathematically correct?
2. If stuck, suggest a DIFFERENT decomposition or inequality
3. Identify the exact algebraic obstacle
4. Propose a concrete next step (state as a Lean theorem signature if possible)

Key insight: on symmetric subspace z(-ω) = conj(z(ω)), so z = x+iy with x even, y odd.
Self-consistency: r = ∫x·g (imaginary parts cancel by oddness).
Challenge: cross terms (y-y*)·(2xy) are EVEN and do NOT vanish." | gemini -p "$(cat)" > "$QA/gemini-latest.txt" 2>&1 || true

  echo "[$(date)] Gemini done ($(wc -l < "$QA/gemini-latest.txt") lines)" | tee -a "$LOG"

  # --- Phase 3: Log to wiki ---
  cd "$WIKI_DIR"
  python tools/run_one.py --build --file "$TARGET" --desc "attack turn $TURN" 2>/dev/null || true

  COMMIT=$(git -C "$LEAN_DIR" log --oneline -1 --format="%h %s" 2>/dev/null || echo "no commit")
  cat >> "$WIKI_DIR/log.md" << LOGEOF

## [$(date +%Y-%m-%d)] experiment | attack $TARGET turn $TURN

- sorry: $SORRY_NOW → $SORRY_AFTER (errors: $ERRORS_AFTER)
- codex: $(echo "$CODEX_OUT" | grep -v "^$" | tail -3 | tr '\n' ' ')
- gemini: $(tail -3 "$QA/gemini-latest.txt" | tr '\n' ' ')
- commit: $COMMIT
LOGEOF

  echo "[$(date)] Turn $TURN complete (sorry: $SORRY_AFTER)" | tee -a "$LOG"
done

# --- Final status ---
FINAL_SORRY=$(get_sorry_count)
echo "" | tee -a "$LOG"
echo "[$(date)] === FINAL STATUS ===" | tee -a "$LOG"
echo "[$(date)] target: $TARGET | sorry: $INITIAL_SORRY -> $FINAL_SORRY | turns: $TURN" | tee -a "$LOG"

if [ "$FINAL_SORRY" -eq 0 ]; then
  echo "[$(date)] SUCCESS — all sorry closed!" | tee -a "$LOG"
  cd "$LEAN_DIR" && git push 2>/dev/null || true
  cd "$WIKI_DIR" && git add -A && git commit -m "wiki: attack $TARGET solved in $TURN turns" && git push autolab main 2>/dev/null || true
else
  echo "[$(date)] INCOMPLETE — $FINAL_SORRY sorry remain after $TURN turns" | tee -a "$LOG"
  cd "$LEAN_DIR" && git push 2>/dev/null || true
fi

rm -rf "$QA"
echo "[$(date)] attack.sh finished" | tee -a "$LOG"
