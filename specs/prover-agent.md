# Prover Agent Architecture

## Overview

A multi-model proving system that uses Pantograph for Lean 4 interaction, wiki for strategic memory, and tiered token budgets.

## Roles

| Role | Model | When Called | Token Budget |
|------|-------|-------------|--------------|
| **Orchestrator** | Claude (Opus/Sonnet) | Once per theorem | Low (plan only) |
| **Tactician** | Codex (GPT-5.4) | Per sorry goal | Medium (bulk work) |
| **Reviewer** | Gemini 2.5 | After N failures | Low (strategy pivot) |
| **Verifier** | Lean 4 / Pantograph | Every tactic attempt | Free |

## Claude's Role: Orchestrator

Claude reads the wiki, identifies the current gap, decomposes into sub-goals, and dispatches work. It does NOT generate Lean tactics directly (too expensive). Instead it:

1. Reads `index.md` + relevant concept/synthesis pages
2. Produces a proof sketch (informal, 5-10 lines)
3. Decomposes into ordered sub-goals with dependencies
4. Assigns each sub-goal to Tactician with relevant context
5. After all sub-goals attempted: reviews results, updates wiki

## Pipeline

```
Claude (plan) → Codex (implement per-sorry) → Lean (verify) → Wiki (log)
                     ↑                              |
                     └── retry with error ──────────┘
```

## Interface: Pantograph

Instead of `lake build` (whole-project pass/fail), use Pantograph for:
- Extract goal state at each `sorry`
- Execute single tactics and get resulting state
- Backtrack on failure without rebuilding

## Token Savings

| Current System | New System |
|----------------|------------|
| Codex reads ALL files each turn | Codex gets only the goal state + retrieved premises |
| 245K tokens per turn | ~20K per sorry (goal + 5 retries) |
| No feedback on which sorry failed | Exact goal state per sorry |
| 10 turns blind | Stop early when all sorry closed |

## Wiki Integration

Before proving:
- Retrieve relevant `concepts/` pages (e.g., pair-bound, tail-body-split)
- Check `syntheses/` for failed strategies on this goal

After proving:
- Success: update `log.md`, add lemma to skill index
- Failure: add to `syntheses/` with WHY it failed

## Module Structure

```
tools/
  prover/
    __init__.py
    orchestrator.py    # Claude: plan + decompose
    tactician.py       # Codex: per-sorry tactic generation
    reviewer.py        # Gemini: strategy when stuck
    pantograph.py      # Lean 4 interface via Pantograph
    wiki_retriever.py  # Retrieve relevant wiki context
    runner.py          # Main loop: orchestrate the pipeline
```

## CLI

```bash
python -m tools.prover --theorem h_body_absorb   # Prove specific theorem
python -m tools.prover --file ContinuumBodyAbsorbBridge  # Close all sorry in file
python -m tools.prover --status  # Show sorry count + progress
```
