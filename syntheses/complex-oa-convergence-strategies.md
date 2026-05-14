---
type: synthesis
title: "Complex OA Convergence: Strategies to Close hV_zero"
created: 2026-05-15
updated: 2026-05-15
sources:
  - "[[dietert-2016-thesis]]"
  - "[[dietert-fernandez-2018-asymptotic-stability]]"
  - "[[cestnik-martens-2024-riccati-array]]"
  - "[[kuehn-landi-2025-oa-unstable-manifold]]"
  - "[[body-lasalle-gap-analysis]]"
  - "[[continuum-stability-debate]]"
tags:
  - complex-oa
  - convergence
  - open-problem
  - stability
aliases:
  - complex-oa-strategies
  - hV-zero-strategies
---

# Strategies to Close hV_zero for Complex OA

The single remaining gap in the end-to-end complex OA stability theorem: prove V(t) → 0 where V = ∫|z-z*|²·g dω.

## The obstacle

**The L² pair bound FAILS for complex z.** Numerical evidence (raw/scripts/complex_pair_bound_test.py):
- K/Kc = 1.1: 47% violation rate, max residual 0.259
- K/Kc = 1.5: 11% violation rate
- K/Kc = 5.0: 0% violations (only strong coupling)

**Root cause**: The pair integrand involves Re((z̄₁-z̄₁*)(z₂-z₂*)·coupling) which can be negative for complex z. The real pair bound crucially uses (α₁-α₁*)(α₂-α₂*) being a product of real numbers.

**What IS proved**: Rotation cancels in V' (rotation_zero_in_error, 0 sorry). After that, V' has the same K-coupling structure. But the coupling doesn't give V' ≤ 0 for all complex z.

## Strategy A: Cooperative n-pole + passage to limit (MOST PROMISING)

**Source**: [[cooperative-oa-global-stability]], Cestnik-Martens 2024

For rational g with poles ω_j = σ_j - iγ_j (γ_j > 0):
1. OA reduces to finite n-dimensional ODE on D^n
2. At |z_j| = 1: d|z_j|²/dt = -2γ_j < 0 (strictly repelling boundary)
3. The system is **cooperative** (Hirsch's theorem applies)
4. Almost every trajectory → PLS (proved for n=1, argument-level for general n)

**Gap**: Uniform entering time T_n ≤ T* as n → ∞. Three-phase argument:
- Phase 1: Linear instability of incoherence (spectral gap from K > Kc)
- Phase 2: Ψ-monotonicity forces escape from near-incoherence
- Phase 3: Basin entry (V(T_n) < r*²)

**New literature**: Kuehn-Landi 2025 (arXiv:2511.03833) proves OA manifold IS the unstable manifold of incoherence in the continuum limit. This strengthens Phase 1: near incoherence, the OA dynamics is exactly the unstable manifold dynamics.

**Lean status**: PassageToLimit.lean has framework, 3 True placeholders.

## Strategy B: Dietert spectral approach + Hypothesis (H)

**Source**: Dietert 2016 thesis §5.6, Dietert-Fernandez 2018

For analytic g:
1. PLS has uniform spectral gap λ > 0 (Dietert §5.6.1)
2. Local exponential convergence in Z^a norm (analyticity strip)
3. Global convergence IF Hypothesis (H) holds: sup_{ω,t} |α(ω-iτ,t)| < R*(τ)

**Hypothesis (H)**: The analytic continuation of z to the strip Im(ω) ∈ [-a, 0] stays in the trapping disk. The trapping radius R*(τ) = (τ + √(τ²+K²))/K comes from the damping d|z|²/dt = -2τ|z|² + K·Re(rz)(1-|z|²) at complex frequency.

**Gap**: Proving Hypothesis (H) requires uniform-in-time bounds on the analytic continuation. Dietert's Theorem 6.11 gives it conditionally.

**New literature**: Cestnik-Martens 2024 (PRL 132, 057201) proves integrability of globally coupled complex Riccati arrays, giving exact solutions in some cases. May provide bounds for Hypothesis (H).

## Strategy C: Ψ + compactness (NOVEL)

**Idea**: Use Ψ monotonicity (dΨ/dt = K|η|² ≥ 0, proved) differently:
1. Ψ(t) → L (monotone + bounded above by ∫-log(1-R*²)g for trapping radius R*)
2. dΨ/dt = K|η|² → 0 (Barbalat, if d²Ψ/dt² bounded)
3. |η(t)| → 0 (from step 2)
4. BUT we want |η| → r* > 0, not → 0

**Resolution**: Step 3 gives the WRONG limit (incoherence, not PLS). Ψ is a Lyapunov for instability of incoherence, not for convergence to PLS.

**However**: If we can show Ψ is UNBOUNDED (Ψ → +∞), then:
- dΨ/dt = K|η|² > 0 for all time (since Ψ → +∞ requires energy input)
- |η| stays bounded below
- Combined with V Cauchy-Schwarz: |η| bounded below + V bounded → V cannot grow
- Eventually V enters basin V < r*²

**Gap**: Showing Ψ → +∞ requires proving locked oscillators have |z| → 1, which is circular (needs convergence).

## Strategy D: Real V antitone + imaginary decay (NOVEL)

**Idea**: Decompose V = V_x + V_y where V_x = ∫(Re(z)-Re(z*))²·g and V_y = ∫(Im(z)-Im(z*))²·g.

On the symmetric subspace:
- The order parameter r = ∫Re(z)·g (imaginary parts cancel)
- V_x controls |r - r*| via Cauchy-Schwarz
- V_y is the "phase error" that doesn't affect the order parameter

**Question**: Is V_x antitone? Its derivative involves the coupling terms from Re(z) dynamics:
dx/dt = ωy + (K/2)r(1-x²+y²)

The ωy term is the rotation coupling x ↔ y. After integration with symmetric g:
∫(x-x*)·ωy·g dω — is this zero by symmetry?

For symmetric g: x is even, y is odd, ω is odd → ωy is even → (x-x*)ωy is even → integral is NOT zero.

**Status**: sketch. The rotation coupling between x and y components does not vanish per ω.

## Strategy E: Direct order parameter ODE (SIMPLEST)

**Idea**: Don't prove V → 0. Instead, derive an ODE/inequality for r(t) directly.

r(t) = Re(∫conj(z)·g) = ∫Re(z)·g (for symmetric case)

dr/dt = ∫(dx/dt)·g = ∫[ωy + (K/2)r(1-x²+y²)]·g

The ωy term: ∫ωy·g = 0 (odd × odd × even = even... wait, y is odd, ω is odd, g is even, so ωyg is even, NOT zero per ω).

Actually: ∫ω·Im(z)·g dω over symmetric measure. Under ω ↦ -ω: ω → -ω, Im(z(-ω)) = -Im(z(ω)), g(-ω) = g(ω). So ω·Im(z(ω))·g(ω) → (-ω)·(-Im(z(ω)))·g(ω) = ω·Im(z(ω))·g(ω). EVEN. Does NOT vanish.

**Status**: blocked. The rotation coupling ∫ωy·g does not simplify for the order parameter ODE.

## Recommendation

**Priority 1**: Strategy A (cooperative n-pole + passage to limit). All building blocks exist in Lean. The Kuehn-Landi result strengthens the argument. Main gap is uniform entering time.

**Priority 2**: Strategy B (Dietert spectral). Requires Hypothesis (H) which may follow from Cestnik-Martens integrability results.

**Priority 3**: Formalize the cooperative structure for finite n (Hirsch's theorem for OA) and prove V_n → 0 for each n. Then address the n → ∞ limit.

## Key references

- Dietert 2016 thesis: spectral gap, Hypothesis (H), Z^a norms
- Dietert-Fernandez 2018: OA manifold attractivity (our axiom)
- Cestnik-Martens 2024: complex Riccati integrability, PRL 132
- Kuehn-Landi 2025: OA = unstable manifold of incoherence
- Pietras-Daffertshofer 2016: OA attractiveness for parameter-dependent systems
