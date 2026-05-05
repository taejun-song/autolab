---
type: synthesis
title: "h_approx ↔ V→0: The Tail-Body Hypothesis Is Equivalent to L² Convergence"
created: 2026-05-05
updated: 2026-05-05
sources:
  - "[[lean-proof-status]]"
  - "[[dietert-2016-stability-bifurcation]]"
  - "[[dietert-fernandez-2018-asymptotic-stability]]"
tags:
  - dynamical-systems
  - synchronization
  - formal-verification
aliases:
  - h-approx-equivalence
---

# h_approx ↔ V→0: The Tail-Body Hypothesis Is Equivalent to L² Convergence

The hypothesis `h_approx` in `kuramoto_solved_continuum` is logically equivalent to V(t) → 0, where V = ∫(α−α*)²dμ is the L² Lyapunov function.

## The hypothesis

```
h_approx : ∀ ε > 0, ∃ (S : Set Ω),
  MeasurableSet S ∧ (μ Sᶜ).toReal < ε ∧
  Tendsto (fun t => ∫ ω in S, (α ω t - α_star ω)² dμ) atTop (nhds 0)
```

Informally: for any tolerance, there exists a "body" S with small complement such that the restricted Lyapunov V_S → 0.

## Equivalence (proved in Lean, 0 sorry)

**V→0 ⟹ h_approx** (`v_tendsto_zero_implies_h_approx`): Take S = Ω. Then μ(Sᶜ) = 0 < ε and V_Ω = V → 0.

**h_approx ⟹ V→0** (`h_approx_implies_v_tendsto_zero`): Given ε > 0, get S with μ(Sᶜ) < ε/2 and V_S → 0. Then V = V_S + V_{Sᶜ} ≤ V_S + μ(Sᶜ) < ε/2 + ε/2 = ε for large t. (Uses |α−α*|² ≤ 1.)

## Consequence for the debate

`kuramoto_solved_continuum` essentially proves: **V→0 ⟹ r→r*** (via Cauchy-Schwarz). This is the easy direction. The hard direction — ODE ⟹ V→0 — is what h_approx assumes.

However, h_approx correctly resolves the reviewer's three objections:

| Concern | kuramoto_solved | kuramoto_solved_continuum |
|---|---|---|
| Uniform persistence δ ≤ α(ω,t) ∀ω | Required (impossible for standard model) | Not required |
| c_min (minimum weight) | Required (n-pole concept) | Not required |
| Bounded γ_max | Required (violated by γ=\|ω\|) | Not required |

The hypotheses of `kuramoto_solved` are UNSATISFIABLE for the standard model. The hypothesis `h_approx` is SATISFIABLE — it follows from V→0, which is the content of global stability.

## Where the hard work lives

`kuramoto_solved` (GeneralGMainTheorem.lean) DERIVES V→0 from uniform persistence + bounded γ via coercive Barbalat drops. This proof strategy genuinely cannot work for unbounded γ because the pair integrand bound C = 2 + 2γ_max/(Kr*) diverges.

For the standard model with unbounded γ, proving V→0 requires either:
1. Dietert's exponential norm approach (analytic g, PDE formulation)
2. A body-tail perturbation argument showing body coercivity dominates tail coupling
3. An asymptotic autonomy argument (requires r→r* first — potentially circular unless bootstrapped)

## LEAN formalization

| Statement | LEAN name | Status |
|---|---|---|
| V→0 ⟹ h_approx | `v_tendsto_zero_implies_h_approx` | proved |
| h_approx ⟹ V→0 | `h_approx_implies_v_tendsto_zero` | proved |
| h_approx ⟹ r→r* | `kuramoto_solved_continuum` | proved |
| ODE ⟹ V→0 (bounded γ) | `kuramoto_solved` (internal) | proved |
| ODE ⟹ V→0 (unbounded γ) | — | sketch |
