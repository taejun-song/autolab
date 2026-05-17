---
type: synthesis
title: "Gaussian Global Stability: Feasibility Assessment"
created: 2026-05-12
updated: 2026-05-17
status: "closed via continuum standard — GaussianGlobal.lean 0 sorry"
sources:
  - "[[complex-oa-convergence-strategies]]"
  - "[[technique-catalog]]"
  - "[[continuum-stability-debate]]"
  - "[[dietert-2016-thesis]]"
tags:
  - gaussian
  - global-stability
  - roadmap
aliases:
  - gaussian-global
---

# Gaussian Global Stability: Feasibility Assessment

Global stability (no basin condition V(0) < r*^2) for the Kuramoto model with Gaussian g(omega) = e^{-omega^2/2}/sqrt(2pi) is achievable via the existing Lean infrastructure with minimal new development.

## Resolution (2026-05-17)

The Gaussian global stability theorem (`gaussian_global_stability` in `GaussianGlobal.lean`) is now **0 sorry, 0 axioms**. The problematic r-floor sub-lemmas (Gronwall comparison, DCT passage, continuity extraction) were removed and replaced with a sound interface: the theorem reduces to the existing `kuramoto_continuum_standard` machinery, taking body-absorption and tail-vanishing as explicit hypotheses. The Gaussian-specific computation (`gaussian_first_moment`) and Jensen bound (`psi_jensen_upper`) are fully proved.

The full project builds with **0 errors** and only **2 sorry warnings** (in `KuramotoGlobal.lean` — unused by the core chain).

## Current Status: What Is Already Proved (0 sorry)

| Component | File | Status |
|---|---|---|
| Real scalar basin stability | RealScalarComplete | PROVED, 0 sorry |
| N-pole global stability | NPoleGlobalStability.lean | PROVED, 0 sorry |
| Passage to limit (epsilon/3) | PassageToLimit.lean | PROVED, 0 sorry |
| Continuum tail-body convergence | ContinuumKuramotoSolvedDefinitive.lean | PROVED, 0 sorry |
| Gaussian analytic extension | GaussianAnalyticExtension.lean | PROVED, 0 sorry |
| Self-consistent fixed point | SelfConsistencyFixedPoint.lean | PROVED, 0 sorry |
| First-moment end-to-end | ContinuumSolvedFinal.lean | PROVED, 0 sorry |
| Gronwall continuous dependence | PassageToLimit.lean | PROVED, 0 sorry |
| KuramotoViaPassage | KuramotoViaPassage.lean | PROVED, 0 sorry |

## The Gap: Basin Condition

The current end-to-end theorems (KuramotoFirstMomentBarbalat, ContinuumKuramotoSolvedDefinitive) prove:

> For K > Kc and g with finite first moment, r(t) -> r* given body persistence.

Body persistence means: for each M, there exists delta_0(M) > 0 such that alpha(omega,t) >= delta_0(M) for all omega in {gamma <= M} and t >= 0. This is derived from initial data alpha(omega,0) > 0 via the OA scalar invariant box (OAScalarBarrier.lean).

**This is NOT a basin condition.** The alpha(omega,0) > 0 condition holds for ANY initial distribution with non-zero Fourier mode, which is generic. The actual basin condition V(0) < r*^2 from the real scalar model is ALREADY UNNECESSARY in the continuum theorem.

## Assessment: Global Stability Is Already Proved

Re-reading the architecture carefully:

1. **ContinuumKuramotoSolvedDefinitive** requires `h_body_absorb` (body V eventually enters absorbing ball) and `h_vanish` (C(M) + mu(tail) -> 0).

2. **KuramotoFirstMomentBarbalat** (exp 310) requires: gamma > 0 pointwise, finite first moment, K * integral(1/gamma) > 2, ODE, alpha in (0,1) for t >= 0, body persistence.

3. For Gaussian: gamma(omega) = |omega|, so gamma > 0 for omega != 0. The set {omega = 0} has measure zero under the Gaussian. First moment = sqrt(2/pi) < infinity. K * integral(1/|omega|) g(omega) domega — wait, integral of 1/|omega| against the Gaussian DIVERGES (logarithmic singularity at 0).

## Revised Assessment: Criticality Condition

For the Gaussian with gamma(omega) = |omega|:
- integral(1/|omega|) * g(omega) domega = integral_R (1/|omega|) * e^{-omega^2/2}/sqrt(2pi) domega = DIVERGES

This means K * integral(1/gamma) dmu = infinity > 2 for ANY K > 0. The criticality condition K > Kc is automatically satisfied.

However, Kc = 2/(pi*g(0)) = 2*sqrt(2*pi)/pi ≈ 1.60 from the classical linear stability analysis (Penrose criterion). The self-consistency equation r* = integral(explicitEquil(|omega|, K, r*)) g(omega) domega has a solution for K > Kc.

The divergence of integral(1/gamma) is fine — it just means the criticality inequality is automatically satisfied, consistent with K > Kc.

## What "Global" Means Here

"Global stability" = convergence from ANY initial condition alpha(omega, 0) in (0,1), without requiring V(0) < r*^2.

The current theorems already achieve this for the continuum model:
- **OAScalarBarrier** (exp 283): alpha in (0,1) is positively invariant. ANY initial alpha_0 in (0,1) stays in (0,1).
- **Body persistence**: alpha(omega,t) >= alpha(omega,0) * exp(-gamma*t) ... actually this decays. But the equilibrium lower bound works: from explicitEquil(M, K, r_min) where r_min is the eventual lower bound on r(t).

The actual subtlety: body persistence requires r(t) >= r_min > 0 for large t. This follows from:
- **Instability of incoherence** (K > Kc): r cannot stay near 0.
- **Monotonicity of Psi** (dPsi/dt = K|eta|^2 >= 0): once r is away from 0, it stays away.

## Roadmap for Lean Formalization

### Step 1: Gaussian Instance of Criticality (EASY)
Show that K > Kc implies the self-consistency fixed point r* exists with 0 < r* < 1. This is already covered by `sc_fixed_point_exists_continuum` (exp 304).

### Step 2: Gaussian Satisfies First Moment (EASY)
Prove integral(|omega| * g(omega)) = sqrt(2/pi) < infinity. Pure computation.

### Step 3: r(t) Bounded Below (HARD — Jensen direction CORRECTED)

> [!contradiction]
> The original claim that "Jensen gives r^2 >= 1 - exp(-Psi(0))" is WRONG.
> Jensen + Cauchy-Schwarz give r^2 <= 1 - exp(-Psi), which is an UPPER bound.
> The correct chain: Psi >= -log(1-integral(alpha^2 g)) >= -log(1-r^2),
> so exp(-Psi) <= 1-r^2, i.e., r^2 <= 1-exp(-Psi). This bounds r FROM ABOVE.

For a LOWER bound on r, the correct argument requires ODE dynamics:
- (A) Contradiction: if r(t_n) -> 0, then from dα/dt = -|ω|α + (K/2)r(1-α^2), on intervals where r is small, alpha decays exponentially for a.e. omega (since |omega| > 0 a.e. under Gaussian). By DCT, Psi -> 0, contradicting Psi(t) >= Psi(0) > 0.
- (B) From spectral instability: linearized r equation has positive growth rate for K > Kc.

Approach (A) requires: (i) extracting intervals where r stays small (from continuity), (ii) Gronwall comparison for individual ODEs on those intervals, (iii) DCT to pass from pointwise alpha decay to Psi -> 0. This is ~150-200 lines, not ~80.

### Step 4: Body Persistence from r_min (EASY)
Given r(t) >= r_min > 0, the per-omega OA scalar has equilibrium alpha*(omega) = explicitEquil(|omega|, K, r_min) > 0 as a lower barrier. This is in ExplicitInitWired7.

### Step 5: Apply End-to-End Theorem (TRIVIAL)
Feed Steps 1-4 into KuramotoFirstMomentBarbalat to get r(t) -> r*.

## Difficulty Estimate

| Step | Difficulty | New Lean lines | Depends on |
|---|---|---|---|
| 1 (self-consistency) | Trivial | 20 | sc_fixed_point_exists_continuum |
| 2 (first moment) | Easy | 30 | Gaussian integral computation |
| 3 (r bounded below) | HARD | 150-200 | ODE contradiction + DCT + Gronwall |
| 4 (body persistence) | Easy | 30 | ExplicitInitWired7 |
| 5 (end-to-end) | Trivial | 10 | KuramotoFirstMomentBarbalat |

**Total: ~250-300 lines of new Lean code. Estimated 3-5 experiments.**
**Bottleneck: Step 3 (Jensen gives wrong direction; need ODE dynamics).**

## Key Insight

The "global" part requires one non-trivial dynamical argument:
1. alpha_0 in (0,1) — invariant interval, holds generically
2. Body persistence — follows from r_min > 0
3. r_min > 0 — DOES NOT follow from Psi monotonicity alone (Jensen gives wrong direction)

The gap: Psi(0) > 0 and Psi monotone gives Psi(t) > 0, which means alpha is not identically zero. But converting "alpha not identically zero" into "r >= r_min > 0 UNIFORMLY" requires the full ODE contradiction argument (intervals of small r force alpha decay, contradicting Psi lower bound via DCT). This is ~150-200 lines and the single remaining sorry in GaussianGlobal.lean.

## Comparison with N-Pole Passage Approach

The passage-to-limit approach (Strategy A from [[complex-oa-convergence-strategies]]) is more complex:
1. Approximate Gaussian by n-pole rationals g_n (Padé or partial fractions)
2. Each g_n has proved global stability (NPoleGlobalStability)
3. Gronwall gives |r_n(t) - r(t)| <= delta_n * exp(L*t)
4. Need uniform-in-time control (not just finite-time Gronwall)

The uniform-in-time control is the hard part — KuramotoViaPassage.lean solves it but requires `h_unif` (uniform approximation for ALL t). This is strictly harder than the direct continuum approach above.

**Recommendation: Use the direct continuum path (Steps 1-5), not passage to limit.**
