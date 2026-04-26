---
type: source-summary
title: "Campa (2022): OA Dynamics for Generic Frequency Distributions"
created: 2026-04-25
updated: 2026-04-25
sources: []
tags: [dynamical-systems, synchronization, dimension-reduction, ott-antonsen]
aliases: ["Campa 2022"]
source_file: ""
source_kind: url
source_date: 2022-08-30
---

# Campa (2022): OA Dynamics for Generic Frequency Distributions

Extends the Ott-Antonsen dimensional reduction to non-rational frequency distributions (e.g., Gaussian) via rational approximation of $g(\omega)$ by Taylor-matching polynomials.

## Source

A. Campa, "The study of the dynamics of the order parameter of coupled oscillators in the Ott-Antonsen scheme for generic frequency distributions," *Chaos* 32, 083104 (2022). arXiv:2208.14171.

## The approximation scheme

For the Gaussian $g(\omega) = \frac{1}{\sqrt{\pi}}e^{-\omega^2}$, replace $e^{\omega^2}$ by its Taylor polynomial of degree $P$:

$$g_P(\omega) = \frac{1}{C_P\sqrt{\pi}}\left[\sum_{s=0}^P \frac{\omega^{2s}}{s!}\right]^{-1}$$

This gives a rational function with $2P$ poles in the complex plane ($P$ in each half-plane). The first $2P$ derivatives of $g_P$ at $\omega = 0$ match those of $g$ exactly.

## The ODE system

Applying the [[ott-antonsen-ansatz]] residue reduction to $g_P$ gives $P$ coupled complex ODEs:

$$\dot{r}^{(m)*} = -i\omega_m r^{(m)*} - \frac{K}{2}\bigl[r(t)[r^{(m)*}]^2 - r^*(t)\bigr], \quad r^*(t) = \sum_{m=1}^P a_m r^{(m)*}(t)$$

where $\omega_m$ are the poles of $g_P$ in the lower half-plane and $a_m$ are the corresponding residue weights. This is structurally identical to the OA reduction for Lorentzian mixtures.

## Convergence: numerical only

- **Taylor sense**: $g_P$ matches the first $2P$ derivatives of $g$ at $\omega = 0$. Rigorously proved.
- **Phase diagram**: $R_P(K) \to R(K)$ pointwise as $P \to \infty$. Heuristic, based on the self-consistency equation depending only on derivatives of $g$ at 0.
- **Dynamics**: the ODE for $g_{12}$ ($P = 12$, 24 real equations) numerically reproduces the continuum PDE dynamics and the $N$-body simulation to high accuracy ($R^* \approx 0.84$ at $K = 3K_c/2$).
- **No rigorous error bounds**: no $L^p$ convergence of $g_P \to g$, no uniform-in-$t$ bound on $|r_P(t) - r(t)|$.

## Self-consistency

The stationary value $R^*$ satisfies the same self-consistency equation for $g_P$ as for $g$:

$$K\int_{-\pi/2}^{\pi/2} \cos^2\theta\, g_P(KR\sin\theta)\,d\theta = 1$$

Because $g_P$ Taylor-matches $g$, the self-consistency curves $R_P(K)$ converge to $R(K)$, with the error vanishing like $(K-K_c)^{2P}$ near onset.

## Relevance to [[kuramoto-stability-problem]]

This paper is the **numerical implementation** of our Path B (rational approximation + passage to limit). Key observations:
- The rational approximation scheme works well numerically, confirming the approach
- The derivative-matching property gives exponential-quality approximation near $K_c$
- But no rigorous convergence theorem is provided — this is exactly the gap in our Path B
- The long-time value $R^*$ is captured correctly by the ODE, even for initial data not on the OA manifold (contributions from outside $\mathcal{G}_2$ decay exponentially by Laplace analysis)

The paper provides **evidence** for the passage-to-limit approach but not a proof.

## Key technical point

The poles $\omega_m$ of $g_P$ are NOT purely imaginary (unlike Lorentzian poles $-i\gamma_k$). They are complex with both real and imaginary parts. This means the $P$-pole ODE system is NOT a real system on $(0,1)^P$ — it's a complex system on $\mathbb{D}^P$. The cooperativity and $L^2$ Lyapunov results that work for Lorentzian mixtures (imaginary poles, real dynamics) do NOT directly transfer.
