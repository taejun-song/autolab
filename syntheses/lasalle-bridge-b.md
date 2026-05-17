---
type: synthesis
title: "Bridge B: LaSalle + Instability of Incoherence"
created: 2026-05-17
updated: 2026-05-17
status: "active — proof skeleton complete, formalization pending"
sources:
  - "[[gaussian-global-stability]]"
  - "Strogatz & Mirollo 1991 (instability of incoherence)"
  - "Kuehn & Landi 2025 (OA = unstable manifold)"
  - "Hsiao, Lo, Zhu 2025 (synchronization equivalence)"
tags:
  - global-stability
  - lasalle
  - bridge
  - hPsi-floor
aliases:
  - bridge-b
---

# Bridge B: LaSalle + Instability of Incoherence

## Goal

Discharge the `hΨ_floor` hypothesis in `KuramotoGlobal.lean`:
```
∃ T₀ : ℝ, 0 ≤ T₀ ∧ (∫ ω, (α ω T₀ - α_star ω)² ∂μ) < r_star²
```

Without assuming V(0) < r*², prove V eventually enters the basin.

## Ontological Concept Map

```
ACCEPTED AXIOMATIC SPACE                    TARGET
════════════════════════                    ══════
V antitone (lyapunov_antitone)         ┐
V ≥ 0 (integral of squares)           ├─► V∞ := lim V(t) exists
V continuous                           ┘
                                            │
On ω-limit set Ω:                          ▼
  dV/dt = 0 identically               ─► ∫ 2(α-α*)·f(α) dμ = 0
                                            ��
Pair bound structure:                       ▼
  integrand ≥ 0 (SOS)                  ─► each term = 0 a.e.
                                            │
Fixed point analysis:                       ▼
  (α-α*)·f(α) = 0 ⟹                  ─► α = α* or α at OTHER equil
                                            │
Other equilibria:                           ▼
  α = 0 is only other fixed point     ─► On Ω: α = α*(ω) or α = 0
  for the scalar ODE                        │
                                            ▼
Self-consistency on Ω:                 ─► r_Ω = ∫ α·g = ∫ α*·g = r*
  (if α = α* a.e.)                         OR r_Ω = 0 (if α = 0 a.e.)
                                            │
INSTABILITY OF INCOHERENCE:                 ▼
  (Strogatz-Mirollo 1991)             ─► r_Ω ≠ 0 (r=0 unstable)
  K > Kc ⟹ linearized growth               │
                                            ▼
Therefore r_Ω = r*                     ─► V∞ = 0 < r*²
Therefore ∃ T₀, V(T₀) < r*²          ═══ TARGET PROVED
```

## Proof Skeleton

### Step 1: V converges (trivial)

V : ℝ → ℝ is antitone (non-increasing) and bounded below by 0.
Therefore V∞ := lim_{t→∞} V(t) exists and V∞ ≥ 0.

**Lean**: `Monotone.tendsto_of_bddBelow` (or antitone dual).

### Step 2: Characterize the ω-limit set via dV/dt = 0

Since V is antitone and converges, on any ω-limit point (a configuration
that the system approaches along a subsequence), V must equal V∞.
Since V is continuously differentiable and its derivative is ≤ 0,
on the ω-limit set dV/dt = 0.

The derivative integrand is:
```
dV/dt = ∫ 2(α(ω,t) - α*(ω)) · oaScalarRHS(γ(ω), K, r(t), α(ω,t)) dμ
```

On the ω-limit set, this equals 0.

**Key subtlety**: The integrand is the SOS pair bound — it's a sum of
non-negative terms (proved in `continuum_lyapunov_deriv_nonpos`). So dV/dt = 0
means EACH TERM is 0 a.e.

### Step 3: Fixed point classification

For the scalar ODE dα/dt = -γα + (K/2)r(1-α²) with r fixed:
- If r > 0: unique equilibrium α*(ω,r) ∈ (0,1) for each ω
- If r = 0: unique equilibrium α = 0

On the ω-limit set where dV/dt = 0:
- Either α(ω) = α*(ω) for a.e. ω (synchronized state)
- Or α(ω) = 0 for a.e. ω (incoherent state)

Mixed states (some ω synchronized, some not) contribute positive terms
to dV/dt unless they happen to be at the correct equilibrium for
the ACTUAL value of r on the ω-limit set.

### Step 4: Self-consistency eliminates mixed states

On the ω-limit set, r = ∫ α·g dμ (self-consistency).

Case A: If α(ω) = α*(ω) a.e., then r = ∫ α*·g dμ = r* > 0. ✓

Case B: If α(ω) = 0 a.e., then r = 0. Need to exclude this.

### Step 5: Instability of incoherence excludes r = 0

**Claim**: r = 0 cannot be in the ω-limit set.

**Proof by contradiction**: Suppose r(tₙ) → 0 along a subsequence.

The linearized equation around α = 0 is: dα/dt = -γα + (K/2)r.
For the collective variable: dr/dt ≈ -⟨γ⟩r + (K/2)r·∫g/(γ) dμ... 

Actually, the correct linearized instability argument for the continuum:

For α small, the nonlinear term α² is negligible, so:
  dα/dt ≈ -��(ω)·α + (K/2)·r
  r = ∫ α·g dμ

This gives a Volterra integral equation. The Laplace transform gives:
  r̂(s) = r(0) / (1 - (K/2)·∫ g(ω)/(s + γ(ω)) dμ(ω))

The characteristic equation 1 = (K/2)·∫ g(ω)/(s + γ(ω)) dμ(ω) has a
positive real root when K > Kc = 2/∫(g/γ)dμ (or Kc = 2/(π·g(0)) for
the Penrose criterion with γ = |ω|).

For K > Kc, the positive root λ > 0 gives exponential growth:
r(t) ~ C·exp(λ·t) near r = 0.

This means any trajectory approaching r = 0 would eventually be
repelled exponentially. Contradiction with r(tₙ) → 0 being an
ω-limit point (ω-limit is positively invariant — trajectories on it
stay on it).

**Formal version**: The ω-limit set is invariant under the flow.
If r = 0 is in the ω-limit set, then the trajectory starting at
(r=0, α=0) is in the ω-limit set. But this trajectory has
exponential growth (instability), so it leaves any neighborhood of
r = 0. The ω-limit set must be closed and invariant — a trajectory
leaving the set contradicts invariance. ∎

### Step 6: Conclusion

From Steps 4-5: on the ω-limit set, r = r* and α = α*.
Therefore V∞ = ∫(α* - α*)² dμ = 0.
Since V(t) → 0 and r*² > 0, there exists T₀ with V(T₀) < r*². ∎

## Critical Lemmas Needed

| # | Lemma | Difficulty | Status |
|---|---|---|---|
| 1 | V converges (antitone + bounded below) | Easy | Mathlib has this |
| 2 | dV/dt = 0 on ω-limit implies integrand = 0 a.e. | Medium | Need SOS structure |
| 3 | Fixed point classification for scalar ODE | Easy | Already proved |
| 4 | Self-consistency on ω-limit set | Medium | Continuity argument |
| 5 | Linear instability of r = 0 for K > Kc | HARD | Volterra integral eq |
| 6 | ω-limit positively invariant + closed | Easy | Mathlib topology |

## Subtleties and Potential Issues

### Issue 1: ω-limit in function space

The ω-limit set lives in L²(μ) (the space of configurations α(ω)).
Compactness requires either:
- Finite-dimensional reduction (e.g., for n-pole rational g)
- Weak sequential compactness in L²
- Direct argument without explicit ω-limit set

### Issue 2: LaSalle for infinite-dimensional systems

Classical LaSalle requires:
- Pre-compact trajectories (bounded in H¹ or compact embedding)
- Continuous semigroup
- Proper Lyapunov function

For the OA continuum, trajectories are bounded (α ∈ (0,1)) but
infinite-dimensional. Need Barbalat's lemma variant instead.

### Issue 3: Instability ≠ repulsion from ω-limit

Linear instability gives exponential growth from EXACTLY r = 0.
But trajectories near r = 0 (not at it) might oscillate.
Need: if r(tₙ) → 0, then for large n, r is small on long intervals,
and on those intervals the instability drives r away. Quantitative
version needed.

## Simplified Approach (avoiding ω-limit set theory)

Instead of full LaSalle machinery, use:

1. V(t) → V∞ (monotone convergence)
2. If V∞ < r*²: done (hΨ_floor with T₀ = any t where V(t) < r*²)
3. If V∞ ≥ r*²: derive contradiction
   - V∞ ≥ r*² means (r(t) - r*)² ≤ V(t) → V∞ ≥ r*², so |r(t) - r*| ≥ √V∞ ≥ r*... wait, Cauchy-Schwarz gives (r-r*)² ≤ V, not ≥.
   - Actually: V∞ ≥ r*² does NOT directly constrain r. We need a different argument.

**Better**: Use Barbalat's lemma directly.
- V antitone + bounded → V converges → dV/dt → 0 (if uniformly continuous)
- dV/dt → 0 + structure of integrand → r(t) → r* (via the SOS pair bound)

This is essentially what `ContinuumSolvedFinal.lean` already does, BUT
it requires a positive lower bound on r to get uniform continuity of dV/dt.

## The Real Bottleneck

Every approach eventually needs: **r(t) ≥ r_min > 0 for large t**.

- LaSalle needs it to classify the ω-limit set
- Barbalat needs it for uniform continuity of dV/dt  
- Body persistence needs it to get exponential decay

The ONLY way to get r_min > 0 without assuming it is:
1. Instability of incoherence (r can't stay near 0)
2. Continuity of r (r can't jump to 0)
3. Combine: r has a positive lim inf

**Lean formalization plan**: Prove lim inf r(t) > 0 via contradiction
using the linearized Volterra instability.

## Lean Formalization Plan

### File 1: `IncoherenceInstability.lean`

```lean
theorem r_liminf_positive [IsProbabilityMeasure μ]
    (γ : Ω → ℝ) (K : ℝ) (r : ℝ → ℝ) (α : Ω → ℝ → ℝ)
    (hK_super : K > Kc γ g μ)  -- supercritical
    (hα_ode : ...)
    (hα_inv : ∀ ω t, 0 ≤ t → 0 < α ω t ∧ α ω t < 1)
    (hr_cont : Continuous r)
    (h_sc : ∀ t ≥ 0, r t = ∫ ω, α ω t ∂μ) :
    ∃ r_min : ℝ, 0 < r_min ∧ ∀ᶠ t in atTop, r_min ≤ r t
```

### File 2: `LaSalleBridgeGlobal.lean`

Wire `r_liminf_positive` + V antitone + Barbalat → V → 0 → hΨ_floor.

## References

- Strogatz & Mirollo, "Stability of incoherence" (1991)
- Chiba, "A proof of the Kuramoto conjecture" (2015)
- Kuehn & Landi, "OA manifold is unstable manifold" (2025)
- Hsiao, Lo, Zhu, "Equivalence of synchronization definitions" (2025)
- Giacomin, Lucon, Poquet, "Global attractor" (2012)
- Dietert & Fernandez, "Mathematics of asymptotic stability" (2018)
