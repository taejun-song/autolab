#!/bin/bash
# Autonomous proof search loop.
# Runs claude in --print mode repeatedly until the proof is done.
# Each iteration reads program.md, attempts progress, logs results.

cd /Users/taejunsong/workspace/autoproof
LOG=/tmp/autoproof-loop.log
echo "=== Autoproof loop started $(date) ===" >> "$LOG"

PROMPT='You are an autonomous research agent. Read program.md for your research instructions.

Current status (from tools/run_one.py --status):
'"$(python tools/run_one.py --status 2>&1)"'

The problem is NOT solved. The hypotheses in FullKuramotoData (especially hslaving_bound, h_decomp, htail_decay) SMUGGLE the conclusion. Moving a sorry into a structure field is not a proof.

Your job: PROVE these hypotheses from the actual Kuramoto ODE structure, or find published theorems that establish them verbatim. Each iteration:

1. Read MainTheorem.lean, ProofAssembly.lean, SelfConsistencyDecay.lean
2. Identify one hypothesis of FullKuramotoData to close
3. Either: (a) prove it as a theorem from more primitive assumptions, or (b) find a published paper whose main theorem matches it exactly and make it an axiom with citation
4. Write LEAN code, build with "cd /Users/taejunsong/workspace/kuramoto-lean && lake build KuramotoLean.ProofAssembly 2>&1 | tail -20"
5. Run critic pass: is any hypothesis still smuggling the conclusion?
6. Report what you did and what remains

Focus on hslaving_bound: the claim that locked oscillators track equilibrium with error ≤ 2e^{-γΨ}. This is the core mathematical content. Can you prove it from the Riccati ODE structure, or find a published theorem?

Write your findings to the wiki. Update results with: python tools/run_one.py --build --file ProofAssembly --desc "your description"'

for i in $(seq 1 50); do
    echo "=== Iteration $i started $(date) ===" >> "$LOG"
    claude --dangerously-skip-permissions -p "$PROMPT" >> "$LOG" 2>&1
    echo "=== Iteration $i finished $(date) ===" >> "$LOG"

    # Check if solved
    SORRY=$(cd /Users/taejunsong/workspace/kuramoto-lean && lake build 2>&1 | grep -c "declaration uses.*sorry")
    AXIOMS=$(grep -c "^axiom" /Users/taejunsong/workspace/kuramoto-lean/KuramotoLean/ProofAssembly.lean 2>/dev/null || echo 0)
    HYPS=$(grep -c "hslaving_bound\|h_decomp\|htail_decay" /Users/taejunsong/workspace/kuramoto-lean/KuramotoLean/ProofAssembly.lean 2>/dev/null || echo 0)

    echo "After iteration $i: sorry=$SORRY axioms=$AXIOMS smuggling_hyps=$HYPS" >> "$LOG"

    # If all smuggling hypotheses are eliminated, we might be done
    if [ "$HYPS" -eq 0 ] && [ "$SORRY" -eq 0 ]; then
        echo "=== POSSIBLE PROOF COMPLETE — running critic ===" >> "$LOG"
        claude --dangerously-skip-permissions -p "Read /Users/taejunsong/workspace/kuramoto-lean/KuramotoLean/ProofAssembly.lean and run a HOSTILE critic pass. List every hypothesis of FullKuramotoData. For each one: is it a published theorem (cite it), a provable ODE property (explain how), or is it smuggling the conclusion? Be maximally skeptical. If ANY hypothesis is not grounded, say FAILED. If all are grounded, say PASSED." >> "$LOG" 2>&1
        echo "=== PROOF CHECK DONE ===" >> "$LOG"
        break
    fi
done

echo "=== Autoproof loop finished $(date) ===" >> "$LOG"
