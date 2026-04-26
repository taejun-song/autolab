---
type: source-summary
title: "Bronski & Wang (2020) — Partially Phase-Locked Solutions to the Kuramoto Model"
created: 2026-04-17
updated: 2026-04-17
sources: []
tags: [dynamical-systems, synchronization, statistical-physics]
aliases: ["Bronski-Wang 2020", "partially locked solutions finite-N"]
source_file: "../raw/papers/2007.05485.pdf"
source_kind: pdf
source_date: 2020-07-10
---

# Bronski & Wang (2020) — Partially Phase-Locked Solutions to the Kuramoto Model

Derives analytical criteria for the existence of partially phase-locked states in the finite-$N$ Kuramoto model by constructing **nested invariant balls**: a larger trapping region and a smaller attracting ball around the locked oscillator subset. The closest result in the literature to a global stability statement for the PLS.

## Key results

1. **Invariant ball existence**: For sufficiently strong coupling $\gamma > \gamma_{\mathrm{critical}}$, there exists an attracting ball around the locked fixed point and a larger invariant region that traps all nearby trajectories.
2. **Deterministic partial entrainment**: In the large-$N$ limit with i.i.d. frequencies, a deterministic condition guarantees a partially entrained subset of positive density.

## Pages read

pp 1–5 (introduction, background, semi-norm definitions, invariant ball construction sketch).

## Relationship to the project

The nested-ball construction is the finite-$N$ analogue of what we need for the continuum case: showing that trajectories enter a neighborhood of the PLS. The gap (present in both Bronski-Wang and our work) is the same: the outer trapping ball does not collapse to the PLS — trajectories enter the ball but are not proved to converge to the fixed point within it.

## Cross-links

- [[kuramoto-stability-problem]] — the closest finite-$N$ result to global PLS stability
- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — our continuum analogue of the nested-ball approach
- [[phase-locked-state]] — the PLS whose existence this paper establishes
