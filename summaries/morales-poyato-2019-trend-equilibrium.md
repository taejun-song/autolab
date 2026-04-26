---
type: source-summary
title: "Morales & Poyato (2019) — On the Trend to Global Equilibrium for Kuramoto Oscillators"
created: 2026-04-17
updated: 2026-04-17
sources: []
tags: [dynamical-systems, synchronization, pde, statistical-physics]
aliases: ["Morales-Poyato 2019", "entropy production Kuramoto"]
source_file: "../raw/papers/1908.07657.pdf"
source_kind: pdf
source_date: 2019-08-22
---

# Morales & Poyato (2019) — On the Trend to Global Equilibrium for Kuramoto Oscillators

Quantitative convergence rates to the global equilibrium (fully synchronized state) for the K-S equation in a **large coupling regime** using entropy production methods inspired by Otto's Riemannian structure on probability measure spaces and Desvillettes-Villani's work on Boltzmann equation trend to equilibrium.

## Key contributions

1. **Entropy production estimate** via a fibered Wasserstein distance adapted to the Kuramoto model (the K-S equation is NOT a Wasserstein gradient flow, so this requires new tools).
2. **Instability of antipodal equilibria** (Section 4) via sliding norms.
3. **Quantitative concentration estimates** for the finite-$N$ particle system (Section 6).

The paper works in the **full synchrony** regime ($r \to 1$, all oscillators locked), not the partially locked state ($r \to r^* < 1$). The entropy methods target the Dirac delta (complete sync) as the global equilibrium, which is qualitatively different from the PLS.

## Pages read

pp 1–5 (introduction, gradient flow structure, main results, ingredients).

## Relationship to the project

The entropy production / fibered Wasserstein approach is the most sophisticated variational method applied to Kuramoto. However, it targets full synchrony, not partial locking. Adapting these methods to the PLS regime would require a new entropy functional centered on the PLS rather than the Dirac delta — precisely the coercivity estimate identified as the remaining gap in our proof.

## Cross-links

- [[kuramoto-stability-problem]] — addresses full synchrony regime, not the PLS stability problem
- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — the fibered Wasserstein idea could inspire a solution to SP2
- [[order-parameter]] — quantitative bounds on the order parameter convergence
