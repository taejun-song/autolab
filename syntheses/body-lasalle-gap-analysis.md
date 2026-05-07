---
type: synthesis
title: "Body LaSalle Gap Analysis: V_body Antitonicity"
created: 2026-05-05
updated: 2026-05-08
status: corrected
sources:
  - "[[continuum-stability-debate]]"
  - "[[lean-proof-status]]"
tags:
  - dynamical-systems
  - stability
  - open-problem
  - lean4
aliases:
  - body-lasalle-gap
---

# Body LaSalle Gap Analysis: V_body Antitonicity

Deep analysis of Strategy A0 (Body LaSalle via MVT on each truncation) reveals that the "single remaining gap" identified in `program.md` (Leibniz integral rule) is actually **PROVED** by `body_leibniz_hasDerivAt` in `BodyLeibnizProof.lean`. The REAL remaining gap is different and more subtle.

## 1. What is proved (0 sorry)

| Component | File | Status |
|---|---|---|
| Body Leibniz: HasDerivAt for V_body(M) | `BodyLeibnizProof.lean` | **PROVED** |
| MVT: derivative vanishes on subsequence | `WeakStarLaSalle.lean` | **PROVED** |
| Abstract LaSalle: V_body antitone + MVT + coercivity → V→0 | `BodyLaSalleConvergence.lean` | **PROVED** |
| Body coercivity: P_body ≥ c(M)·V_body eventually | `PairCoercivity.lean` | **PROVED** |
| Tail vanishing: tail_mass(M) → 0 | `ContinuumLyapunov` | **PROVED** |
| Full V antitone (integrable γ): dV/dt ≤ 0 | `ContinuumSolvedContinuum.lean` | **PROVED** for ∫γg < ∞ |

## 2. The actual gap: V_body antitonicity

`BodyODEData.h_Vb_hasDerivAt` requires:
$$\text{HasDerivAt}\ (V_{\text{body}}\ M)\ (-(K \cdot P_{\text{body}}\ M\ t))\ t$$
with $P_{\text{body}} \geq 0$ (field `hPb_nn`).

This means $V_{\text{body}}(M,\cdot)$ must be **antitone** (derivative ≤ 0 everywhere).

### Why this fails for the body-restricted case

The body derivative from `body_leibniz_hasDerivAt`:
$$\frac{dV_{\text{body}}}{dt} = \int_{\gamma \leq M} 2(\alpha - \alpha^*) \cdot \alpha'\ g\, d\omega$$

Using the per-$\omega$ identity (`per_omega_identity` in `GeneralGMainTheorem.lean`):
$$= K(-r^* \cdot Q_{\text{body}} + D \cdot S_{\text{body}})$$

where:
- $Q_{\text{body}} = \int_{\text{body}} (\alpha-\alpha^*)^2(\alpha + 1/\alpha^*)g \geq 0$ (dissipation)
- $S_{\text{body}} = \int_{\text{body}} (\alpha-\alpha^*)(1-\alpha^2)g$ (bounded, either sign)
- $D = r(t) - r^* = \int_{\text{ALL}} (\alpha - \alpha^*)g$ (GLOBAL deviation)

The pair bound for the **full** integral: $r^*Q \geq D \cdot S$ (proved via `continuum_lyapunov_deriv_nonpos`). But for the **body-restricted** case: $r^*Q_{\text{body}} \geq D \cdot S_{\text{body}}$ is **NOT guaranteed** because the pair bound uses self-consistency $r = \int_{\text{ALL}} \alpha\, g$, which does not hold for the restricted measure.

### Physical interpretation

The coupling error $K \cdot D \cdot S_{\text{body}}$ represents energy transfer between body and tail through the global order parameter $r(t)$. When $r > r^*$ ($D > 0$) and the body has net positive deviation ($S_{\text{body}} > 0$), energy flows INTO the body, temporarily increasing $V_{\text{body}}$.

## 3. Obstruction hierarchy

```
  Full V antitone (from pair bound + full self-consistency)
      ↓ [proved for integrable γ, requires Leibniz for full V]
  V_body antitone (from body pair bound + ...?)
      ↓ [OPEN — self-consistency mismatch for restricted measure]
  BodyODEData instantiation
      ↓ [automatic]
  V → 0 (BodyLaSalleConvergence)
```

## 4. Why this was misidentified

`program.md` states: "The SINGLE remaining gap: Leibniz integral rule for $d/dt \int_{|\omega|\leq M'} (\alpha-\alpha^*)^2 g$."

This Leibniz step IS proved by `body_leibniz_hasDerivAt`. But the **sign** of the resulting derivative (non-positivity) was implicitly assumed. The true gap is:

> Prove $\int_{\gamma \leq M} 2(\alpha-\alpha^*) \cdot \text{oaScalarRHS}\ g\, d\mu \leq 0$ for all $M, t > 0$.

This is equivalent to V_body antitonicity and requires extending the pair bound to body-restricted integrals.

## 5. Viable approaches to close

### 5a. Eventual antitonicity (most promising)

As $t \to \infty$: $D(t) = r(t) - r^* \to 0$ (if V → 0) or $|D| \leq \sqrt{V(0)}$ (Cauchy-Schwarz). The coupling error $K \cdot D \cdot S_{\text{body}}$ is bounded. For large $M$: the dissipation term $-Kr^*Q_{\text{body}}$ grows (more oscillators contribute), eventually dominating the coupling.

This gives: $\exists M_0, T_0$ such that $dV_{\text{body}}(M)/dt \leq 0$ for $M \geq M_0$, $t \geq T_0$.

**Problem**: both $M_0$ and $T_0$ may depend on the trajectory (V→0 not yet proved).

### 5b. Modified BodyODEData without antitonicity

Remove `hPb_nn ≥ 0` from `BodyODEData`. Use the FULL V antitonicity plus body-restricted derivative information to get a weaker convergence argument.

Specifically: V antitone → V(n)-V(n+1) → 0. This equals (body drop) + (tail drop). If body drop can be bounded below by -C (some constant), then body drops don't accumulate, and the tail drops must also → 0. Combined with tail coercivity... complex but potentially viable.

### 5c. Passage to limit (independent approach)

Use the n-pole theorem (V_n → 0, proved) + quantitative approximation V_n → V. This bypasses the body derivative sign issue entirely. Gap: 3 True placeholders in `PassageToLimit.lean` for continuous dependence.

### 5d. Lorentzian closed-form (special case)

For the specific case of Lorentzian $g$: the Bernoulli reduction gives $r \to r^*$ directly, without needing the Lyapunov approach. This is PROVED in `MainTheorem.lean`.

## 6. Updated status by distribution (corrected exp 289)

**Correction**: The original table incorrectly listed Student-t ν=2 as having ∫|ω|g = ∞. The correct statement:

For Student-t ν: g(ω) ∝ (1+ω²/ν)^{-(ν+1)/2}. Substituting u = ω²/ν:
∫₀^∞ ω·g dω ∝ ∫₀^∞ (1+u)^{-(ν+1)/2} du = [(−2/(ν−1))(1+u)^{-(ν-1)/2}]₀^∞ = 2/(ν−1), convergent iff **ν > 1**.

For ν=2: ∫|ω|g = 2/(2-1) · C = 2C < ∞. So Student-t ν=2 has **finite first moment**.

Similarly, ∫ω²g converges iff the integrand ∼ ω²·ω^{-(ν+1)} = ω^{-(ν-1)} is integrable at ∞, i.e., ν > 2. So Student-t ν=2 has **infinite second moment**.

| Distribution | ∫\|ω\|g | ∫ω²g | V → 0 | Method |
|---|---|---|---|---|
| Bounded support | < ∞ | < ∞ | PROVED (abstract) | ContinuumFiniteMoment / wired6 |
| Gaussian | < ∞ | < ∞ | PROVED (abstract) | ContinuumFiniteMoment / wired6 |
| Student-t ν>2 | < ∞ | < ∞ | PROVED (abstract) | ContinuumFiniteMoment / wired6 |
| Student-t 1<ν≤2 | < ∞ | = ∞ | PROVED (abstract) | ContinuumFiniteMoment (∫\|ω\|g < ∞ suffices) |
| Lorentzian ν=1 | = ∞ | = ∞ | **PROVED** (0 sorry, 0 axioms) | Bernoulli (exp 287) |
| Student-t ν<1 | = ∞ | = ∞ | OPEN | Neither approach applies |

**"PROVED (abstract)"** means the abstract theorem `kuramoto_solved_continuum_definitive` in `ContinuumFiniteMoment.lean` applies modulo external hypotheses `hV_anti` and `h_leibniz_drop` that remain as structural inputs (not derived from ODE data). For Lorentzian, the full chain is closed with 0 sorry, 0 axioms.

**Consequence**: The original classification of Student-t ν=2 as "OPEN" was wrong — it has the same status as ν>2 (finite first moment, covered by the abstract theorem). The only genuinely open case is ν < 1 (super-Cauchy distributions), which are not physically standard in the Kuramoto literature.

## 7. Label

**open** — The body LaSalle argument (BodyLaSalleConvergence.lean) is proved from BodyODEData, but BodyODEData cannot be instantiated for non-integrable γ due to the V_body antitonicity gap. The gap is the pair bound for body-restricted integrals under global (not body-local) self-consistency.
