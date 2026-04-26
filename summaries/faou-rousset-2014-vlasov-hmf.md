---
type: source-summary
title: "Faou & Rousset (2014) — Landau Damping in Sobolev Spaces for the Vlasov-HMF Model"
created: 2026-04-17
updated: 2026-04-17
sources: []
tags: [dynamical-systems, pde, kinetic-theory, plasma-physics]
aliases: ["Faou-Rousset 2014", "Vlasov-HMF Landau damping"]
source_file: "../raw/papers/1403.1668.pdf"
source_kind: pdf
source_date: 2014-04-18
---

# Faou & Rousset (2014) — Landau Damping in Sobolev Spaces for the Vlasov-HMF Model

Proves nonlinear Landau damping with polynomial rate for the Vlasov-HMF model under Sobolev regularity, using a bootstrap argument on the Volterra equation for the order parameter. The HMF model is structurally analogous to the Kuramoto model (both have sinusoidal coupling with only two Fourier modes), and this paper's techniques directly inspired [[fernandez-gerard-varet-giacomin-2016-landau-damping|FGG 2016]] and [[dietert-2017-pls-sobolev|Dietert 2017]].

## Key result

**Theorem 1.1.** For $s \geq 7$ and initial perturbation satisfying $Q_{0,s}(g) \leq R_0$ under a Penrose-type stability condition (H), the solution scatters and the order parameter decays polynomially.

The proof uses energy estimates (Proposition 2.4) with the key bound $N_{T,s}(g) \leq (R_0 + \varepsilon R^2)(1+\varepsilon R)e^{C\varepsilon R}$, which closes the bootstrap for small $\varepsilon$.

## Pages read

All 10 pages.

## Relationship to the project

Read for techniques transferable to the global stability problem. The bootstrap is LOCAL (small perturbations only). The "plasma echo" cancellation (§2, eq. 2.6) is specific to two-mode interactions and doesn't help with the moment hierarchy closure problem identified in SP2.

## Cross-links

- [[fernandez-gerard-varet-giacomin-2016-landau-damping]] — adapted this paper's techniques to Kuramoto
- [[landau-damping]] — the physical phenomenon proved rigorously here for Vlasov-HMF
