#!/bin/bash
LOG="/tmp/autoproof-loop.log"
DIR="/Users/taejunsong/workspace/autoproof"
PROMPT="Read program.md. The Lorentzian case is DONE. Your task: close the CONTINUUM proof for general g. Three steps: (1) Use Mathlib's Analysis.ODE.PicardLindelof (which works in Banach spaces) to prove ODE existence for the OA equation in L²(g). Show the RHS is locally Lipschitz, apply IsPicardLindelof, extract HasDerivAt. (2) Use Mathlib's MeasureTheory.Integral.Prod (Fubini) to prove the continuum Lyapunov V∞ = ∫∫ pair dg dg satisfies dV∞/dt ≤ 0, then fill the ContinuumGlobalStability structure fields. (3) Add 1 axiom for rational approximation rate of analytic g (Padé/AAK), then close PassageToLimit. Do NOT prove more abstract ODE theorems — fill existing structure fields."

cd "$DIR"
echo "[$(date)] autoresearch started" > "$LOG"

TURN=0
while true; do
  TURN=$((TURN + 1))
  echo "[$(date)] Turn $TURN starting..." >> "$LOG"

  claude --dangerously-skip-permissions -p --verbose "$PROMPT" >> "$LOG" 2>&1

  EXIT_CODE=$?
  echo "[$(date)] Turn $TURN ended (exit=$EXIT_CODE)" >> "$LOG"

  if [ $EXIT_CODE -ne 0 ]; then
    echo "[$(date)] Non-zero exit, waiting 30s before retry..." >> "$LOG"
    sleep 30
  fi
done
