---
type: synthesis
title: "Continuum L² Lyapunov Function for the OA Flow"
created: 2026-04-26
updated: 2026-05-05
sources:
  - "[[lean-proof-status]]"
  - "[[research-program]]"
  - "[[subproblem-decomposition]]"
  - "[[dietert-fernandez-2018-asymptotic-stability]]"
  - "[[kuramoto-1975-self-entrainment]]"
tags:
  - dynamical-systems
  - stability
  - synchronization
  - open-problem
aliases:
  - continuum-l2-lyapunov
---

# Continuum L² Lyapunov Function for the OA Flow

$V_\infty = \int g(\omega)|\alpha(\omega,t) - \alpha^*(\omega)|^2\,d\omega$ is a Lyapunov function for the continuum Ott-Antonsen flow, with $dV_\infty/dt \leq 0$ proved via a purely algebraic pair bound.

## The discovery

For the n-pole OA system, $V = \sum c_k(\alpha_k - \alpha^*_k)^2$ satisfies $dV/dt \leq 0$. The proof (L2Lyapunov.lean, 0 sorry) decomposes $dV/dt = K(DS - r^*Q)$ and shows $DS \leq r^*Q$ via a symmetrized double-sum pair bound.

The pair bound is **purely algebraic**: for any $\alpha_1, \alpha_2, \alpha^*_1, \alpha^*_2 \in (0,1)$:

$$\alpha^*_1 p_2^2 q_2 + \alpha^*_2 p_1^2 q_1 - p_1 p_2(2 - \alpha_1^2 - \alpha_2^2) \geq 0$$

where $p_i = \alpha_i - \alpha^*_i$, $q_i = \alpha_i + 1/\alpha^*_i$. This holds **regardless of dimension** — it's a pointwise inequality on four real numbers.

## Transfer to the continuum

Since the pair bound is pointwise, it transfers directly to Lebesgue integrals:

$$\int\int g(\omega_1)g(\omega_2) \cdot \text{pair}(\omega_1, \omega_2)\,d\omega_1\,d\omega_2 \geq 0$$

by `integral_nonneg` applied twice. This is ContinuumLyapunov.lean (0 sorry).

The consequence: $dV_\infty/dt = K(DS_\infty - r^* Q_\infty) \leq 0$ where the products of integrals equal the double integral (by Fubini).

## LEAN formalization

| Statement | LEAN name | Status |
|---|---|---|
| Pair bound (pointwise) | `pair_bound` | proved (0 sorry) |
| Finite DS ≤ r*Q | `ds_le_rstarQ` | proved (0 sorry) |
| Continuum ∫∫ pair ≥ 0 | `continuum_pair_nonneg` | proved (0 sorry) |
| Full dV∞/dt ≤ 0 identity | — | argument (needs Fubini for products → double integral) |

## Significance

This resolves the **core obstruction** identified in [[subproblem-decomposition]]:

> The PLS lives at "infinity" in every natural metric ($\Psi_{PLS} = +\infty$).

$V_\infty$ is **finite at the PLS** (since $|\alpha - \alpha^*|^2 \leq 4$ and $g \in L^1$). Unlike $\Psi$, which diverges at the PLS, $V_\infty$ gives a well-defined distance that decreases along trajectories.

## Remaining gap: V∞ → 0

$dV_\infty/dt \leq 0$ gives $V_\infty(t) \to L \geq 0$. The open question: **is $L = 0$?**

For the n-pole (finite sums), this follows from:
- The exponential rate $dV/dt \leq -\mu V$ when $\alpha_k \geq \delta > 0$
- Persistence ($\alpha_k$ returns to $[\delta, 1]$ infinitely often)
- Barbalat persistence argument (NPoleGlobalStability.lean, 0 sorry)

For the continuum, there is a subtlety:
- The finite exponential rate uses the **diagonal** of the double sum: $r^*Q - DS \geq \sum c_k^2 (\alpha_k - \alpha^*_k)^2 \alpha_k(\alpha^*_k + \alpha_k)$
- In the continuum, the diagonal $\{\omega_1 = \omega_2\}$ has **measure zero** in $\mu \otimes \mu$
- So the diagonal extraction technique does not directly give an exponential rate

Possible approaches to prove $V_\infty \to 0$:

1. **LaSalle invariance**: If the orbit is precompact in $L^2(g)$ (from Fréchet-Kolmogorov + ODE regularity), then $V_\infty \to 0$ because $V'_\infty = 0$ only when $\alpha = \alpha^*$.

2. **Near-diagonal bound**: The pair integrand is continuous and positive near the diagonal. For $|\omega_1 - \omega_2| < \epsilon$, it's bounded below by $c(\epsilon) \cdot |\alpha - \alpha^*|^2$. This gives a polynomial (not exponential) rate.

3. **Passage to limit**: The n-pole $V_n \to 0$ for each $n$, and $V_n \to V_\infty$ as $n \to \infty$. The standard $\epsilon/3$ argument (PassageToLimit.lean) gives $V_\infty \to 0$.

Approach 3 is the most immediate path and is already formalized as an argument (0 sorry but with structure-field axioms for rational approximation and continuous dependence).

4. **Tail-body split (h_approx)**: ContinuumMainTheorem.lean (0 sorry, 0 axioms) proves: IF h_approx holds, THEN r → r*. The conditional proof is complete.

### h_approx is tautological (identified in debate Round 3)

`h_approx_implies_v_tendsto_zero` and `v_tendsto_zero_implies_h_approx` (both proved, 0 sorry) show **h_approx ↔ V → 0**. Since V → 0 → r → r* is immediate by Cauchy-Schwarz, `kuramoto_solved_continuum` does not reduce the problem — it restates it.

### Gap in naive discharge (identified in debate Round 2)

The naive argument "apply `kuramoto_solved` to S = {|ω| ≤ M}" fails because `kuramoto_solved` requires self-consistency r(t) = ∫ α dμ, but the restricted integral ∫_S α dμ ≠ r(t). The order parameter r(t) couples body and tail — the restricted dynamics on S are **not autonomous**.

### ISS estimate does not close (identified in debate Round 2–3)

The ISS approach $dV_S/dt \leq -c_S V_S + C\sqrt{V_S + \varepsilon}$ yields only an absorbing ball $V_S = O(\sqrt{\varepsilon})$ for fixed $\varepsilon$. The $\sqrt{}$ term dominates $V_S$ near zero. The limit interchange $\varepsilon \to 0$ after $t \to \infty$ is not justified without uniform-in-S estimates.

### Correct approach: LaSalle + precompactness

The remaining viable path:

1. $V(t) \to L \geq 0$ (antitone bounded, proved)
2. $\{\alpha(\cdot, t_n)\}$ precompact in $L^2(\mu)$ — requires **equicontinuity in $\omega$**, uniform in $t$, from the variational equation $\partial/\partial\omega[\dot{\alpha}]$
3. Subsequential limit $\alpha_\infty$ satisfies $dV/dt = 0$, so by ContinuumRigidity $\alpha_\infty = \alpha^*$ a.e.
4. Therefore $L = 0$

The equicontinuity is the genuinely new ingredient. For the OA ODE $\dot{\alpha} = -\gamma\alpha + (K/2)r(t)(1-\alpha^2)$ with $\gamma(\omega) = |\omega|$, Gronwall on $\partial\alpha/\partial\omega$ gives $|\partial\alpha/\partial\omega| \leq C e^{Ct}$ — exponential growth, NOT uniform. This requires either a weighted Fréchet-Kolmogorov criterion or a compactness argument exploiting $V$ decay.

### Note on α* near ω = 0

The equilibrium $\alpha^*(\omega) = (-|\omega| + \sqrt{\omega^2 + K^2 r^{*2}})/(Kr^*)$ satisfies $\alpha^*(0) = 1$ (boundary of (0,1)), not $\alpha^* \to 0$. This is a measure-zero issue for absolutely continuous g, not a coercivity obstruction.

### Minimal honest theorem statement

"For $g \in L^1(\mathbb{R})$ with $g > 0$, $K > K_c$, assuming global OA solutions with $\alpha \in (0,1)$ and self-consistency, IF $\{\alpha(\cdot,t)\}_{t \geq 0}$ is precompact in $L^2(g\,d\omega)$, THEN $r(t) \to r^*$."

This replaces h_approx (tautological) with precompactness (genuine PDE regularity, verifiable for smooth $g$).

## Absorbing Barbalat approach (ContinuumBodyPersistence.lean)

A new theorem `kuramoto_continuum_from_body_persistence` (0 sorry, 0 axioms) addresses the three reviewer problems with `kuramoto_solved`:

1. **No uniform persistence**: only body persistence on {γ ≤ M} required
2. **No bounded γ**: rate comes from body pair coercivity, not Leibniz on full V
3. **No c_min**: works with continuous probability measure

The hypothesis is **absorbing-ball drops**: for a FIXED contraction q < 1, and any additive error ε > 0, there exist infinitely many times where V(t+1) ≤ q·V(t) + ε. The key analysis lemma `absorbing_barbalat_io` proves V → 0 from these drops + V antitone.

The physical content: q = exp(-rate_M₀) from pair coercivity on ONE fixed body M₀ (where locked oscillators have persistence δ_M₀ and α* ≥ δ*_M₀). The additive ε = μ({γ > M}) from the tail (→ 0 by g integrable, choosing M large).

### LEAN formalization (ContinuumBodyPersistence.lean)

| Statement | LEAN name | Status |
|---|---|---|
| Absorbing Barbalat (i.o. drops → V→0) | `absorbing_barbalat_io` | proved (0 sorry) |
| Body persistence → r→r* | `kuramoto_continuum_from_body_persistence` | proved (0 sorry) |
| Full chain (tail + body rate → r→r*) | `kuramoto_continuum_full_chain` | proved (0 sorry) |

### Remaining gap

The hypotheses V antitone and h_body_drops must be verified for specific g:
- **V antitone**: requires Leibniz differentiation of the full V, which needs γ ∈ L¹(μ) (holds for Gaussian, Student's t with df > 1; fails for Lorentzian)
- **h_body_drops with FIXED q**: requires that body persistence + pair coercivity gives a non-degenerate rate. This holds when ε/(1-q) → 0, i.e., the tail decays faster than the rate degrades. Verified for Gaussian g; open for heavy-tailed distributions.

## Label

**conditional-mechanistic** (ContinuumBodyPersistence.lean: 0 sorry, 0 axioms; absorbing drops → r→r* proved; hypothesis encodes the geometric decay mechanism rather than restating the conclusion; the remaining gap is verifying V antitone + body drops for specific g)
