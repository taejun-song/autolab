---
type: synthesis
title: "Continuum L² Lyapunov Function for the OA Flow"
created: 2026-04-26
updated: 2026-04-26
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

## Label

**argument** (pair bound proved in LEAN 4; continuum transfer proved; Fubini connection and V∞ → 0 are rigorous arguments not yet machine-checked)
