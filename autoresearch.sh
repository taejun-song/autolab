#!/bin/bash
LOG="/tmp/autoproof-loop.log"
DIR="/Users/taejunsong/workspace/autoproof"
QA="/tmp/debate"
mkdir -p "$QA"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
nvm use 20 2>/dev/null

cd "$DIR"
echo "[$(date)] Codex+Gemini loop started (no Claude tokens)" > "$LOG"

TURN=0
while true; do
  TURN=$((TURN + 1))
  echo "[$(date)] === Turn $TURN ===" >> "$LOG"

  # Phase 1: Codex implements + asks questions
  echo "[$(date)] Codex implementing..." >> "$LOG"
  PREV_GEMINI=$(cat "$QA/gemini-latest.txt" 2>/dev/null | tail -20)

  codex exec -C /Users/taejunsong/workspace/kuramoto-lean --dangerously-bypass-approvals-and-sandbox "You are a Lean 4 proof engineer working in /Users/taejunsong/workspace/kuramoto-lean/KuramotoLean/.
Read program.md at /Users/taejunsong/workspace/autoproof/program.md for full research context.

PREVIOUS GEMINI FEEDBACK: $PREV_GEMINI

CONTEXT: We proved local stability (kuramoto_stability in KuramotoFinal.lean, 0 sorry).
Now attempting TRUE GLOBAL stability: remove V(0) < r*² assumption.
The scaffolding is in KuramotoGlobal.lean with 5 sorry.
The KEY gap: r_stays_positive — prove r(t) ≥ r_min > 0 for all t when r(0) > 0.
Strategy: energy identity Ψ = ∫-log(1-α²)g, show Ψ stays positive → r can't collapse.

Key files to read first:
- KuramotoGlobal.lean (the target — 5 sorry to close)
- KuramotoFinal.lean (the local version — 0 sorry, the template)
- GeneralGMainTheorem.lean (lyapunov_antitone, pair bound)
- BodyPersistenceFromODE.lean (body persistence from r bound)

YOU MUST WRITE LEAN 4 CODE. Do not just analyze — create or edit .lean files.

YOUR TASKS (in order):
1. Read the files above to understand the current proof state
2. Write a NEW Lean 4 file or extend an existing one that makes progress on h_body_absorb
3. Use 'sorry' for any sub-goals you cannot close — that is fine, it marks exactly where gaps remain
4. Run 'cd /Users/taejunsong/workspace/kuramoto-lean && lake build' to check your code compiles
5. Git commit your work with a descriptive message
6. State ONE precise mathematical question for Gemini to answer

RULES:
- Output VALID Lean 4 code that imports Mathlib
- Every new theorem must have a docstring explaining what it proves
- Use sorry freely — partial progress with sorry is better than no code at all
- Always compile-check with lake build before committing" > "$QA/codex-latest.txt" 2>&1
  echo "[$(date)] Codex done: $(wc -l < $QA/codex-latest.txt) lines" >> "$LOG"
  echo "Codex output:" >> "$LOG"
  tail -20 "$QA/codex-latest.txt" >> "$LOG"

  # Phase 2: Gemini reviews + answers + proposes
  echo "[$(date)] Gemini reviewing + answering..." >> "$LOG"
  CODEX_OUT=$(cat "$QA/codex-latest.txt" | tail -30)

  echo "You are collaborating with Codex (GPT) on proving Kuramoto stability. Codex said:

$CODEX_OUT

YOUR TASKS:
1. Answer any questions Codex asked — be rigorous and specific
2. Evaluate whether Codex's approach is correct
3. Propose a DIFFERENT strategy if Codex is stuck
4. Think about analogies from kinetic theory, Vlasov equations, or hypocoercivity

State:
- Your answer to Codex's question
- Whether Codex's approach is valid
- Your alternative suggestion (if any)
- What Codex should try next turn" | gemini --skip-trust -p "$(cat)" > "$QA/gemini-latest.txt" 2>&1
  echo "[$(date)] Gemini done: $(wc -l < $QA/gemini-latest.txt) lines" >> "$LOG"
  echo "Gemini output:" >> "$LOG"
  tail -20 "$QA/gemini-latest.txt" >> "$LOG"

  # Phase 3: Update wiki with findings
  echo "[$(date)] Updating wiki..." >> "$LOG"
  CODEX_SUMMARY=$(tail -10 "$QA/codex-latest.txt" | grep -v "hook:\|tokens\|codex$")
  GEMINI_SUMMARY=$(tail -10 "$QA/gemini-latest.txt" | grep -v "hook:\|tokens")
  WIKI_DIR="/Users/taejunsong/workspace/autoproof"
  cat >> "$WIKI_DIR/log.md" << LOGEOF

## [$(date +%Y-%m-%d)] experiment | autoresearch turn $TURN

- codex: $(echo "$CODEX_SUMMARY" | head -3 | tr '\n' ' ')
- gemini: $(echo "$GEMINI_SUMMARY" | head -3 | tr '\n' ' ')
- commit: $(git -C /Users/taejunsong/workspace/kuramoto-lean log --oneline -1 --format="%h %s" 2>/dev/null)
LOGEOF

  # Log commits if any
  COMMIT=$(git -C /Users/taejunsong/workspace/kuramoto-lean log --oneline -1 --format="%h %s" 2>/dev/null)
  echo "[$(date)] Latest commit: $COMMIT" >> "$LOG"

  echo "[$(date)] Turn $TURN complete" >> "$LOG"

  # Stop after 10 turns
  if [ $TURN -ge 10 ]; then
    echo "[$(date)] MAX TURNS — writing summary" >> "$LOG"
    echo "Summarize the collaboration: what was proved, what questions remain open, what is the most promising path forward." | codex exec "$(cat)" > "$QA/final-summary.txt" 2>&1
    break
  fi
done

echo "[$(date)] Loop ended" >> "$LOG"
