---
type: source-summary
title: "Dietert (2017) — Stability of Partially Locked States in the Kuramoto Model through Landau Damping with Sobolev Regularity"
created: 2026-04-17
updated: 2026-04-17
sources: []
tags: [dynamical-systems, synchronization, pde, kinetic-theory]
aliases: ["Dietert 2017", "PLS Sobolev stability"]
source_file: "../raw/papers/1707.03475.pdf"
source_kind: pdf
source_date: 2020-01-14
---

# Dietert (2017) — Stability of Partially Locked States in the Kuramoto Model through Landau Damping with Sobolev Regularity

Extends nonlinear Landau damping from the homogeneous (incoherent) state to the **partially locked state** (PLS) under Sobolev regularity, proving local nonlinear stability of the PLS for $b > 3/2$ with polynomial decay rate $|\eta(t)| \leq C(1+t)^{1/2-b}$.

## Key result

**Theorem 1.** For $b > 3/2$, $b_g > b+3$ (or $b > 3$, $b_g > b+5$), and a linearly stable PLS $f_{\mathrm{st}}$ with Sobolev-regular frequency density $g$, sufficiently small perturbations converge to a nearby PLS with polynomial decay of the order parameter perturbation.

The proof constructs a bootstrap argument on the nonlinear Volterra equation for the order parameter, incorporating the nonlinearity into the transport kernel rather than the forcing. This handles the Sobolev case where the analytic approach of the earlier Dietert-Fernandez-Gérard-Varet paper does not apply.

## Pages read

pp 1–10 (introduction, main theorem, overview, setup, linear analysis, Volterra equation, bootstrap sketch).

## Relationship to the project

Subsumed by the review [[dietert-fernandez-2018-asymptotic-stability]] (Theorem 2.3). The primary source for the **local** stability result that our [[hyperbolic-lyapunov-attack-on-kuramoto-stability|Lyapunov hypothesis]] seeks to extend to **global** stability.

## Cross-links

- [[kuramoto-stability-problem]] — resolves Assertion 2 (local stability along the branch)
- [[landau-damping]] — the Landau damping mechanism for PLS, not just incoherence
- [[dietert-fernandez-2018-asymptotic-stability]] — the review that subsumes this paper
