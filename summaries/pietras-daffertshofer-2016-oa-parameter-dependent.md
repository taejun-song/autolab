---
type: source-summary
title: "Pietras & Daffertshofer (2016) — Ott-Antonsen Attractiveness for Parameter-Dependent Oscillatory Networks"
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [dynamical-systems, synchronization, dimension-reduction, ott-antonsen, neuroscience]
aliases: ["Pietras-Daffertshofer 2016", "OA attractiveness parameter-dependent"]
source_file: "../raw/papers/1608.02723.pdf"
source_kind: pdf
source_date: 2016-08-09
---

# Pietras & Daffertshofer (2016) — OA Attractiveness for Parameter-Dependent Oscillatory Networks

Rigorous proof that the [[ott-antonsen-ansatz]] manifold remains asymptotically attractive when oscillator dynamics depend on additional oscillator-specific parameters beyond the natural frequency.

## Setting

The Kuramoto-like model with parameter dependence:

$$\dot{\theta}_j = \Omega(\omega_j, \eta_j) + \operatorname{Im}[H(\eta_j, t)e^{-i\theta_j}]$$

where $\eta_j$ is an oscillator-specific parameter (e.g., shear, excitability) drawn from a distribution $g(\eta)$. Both the natural frequency $\Omega$ and the driving field $H$ may depend on $\eta$. In the continuum limit:

$$\partial_t\theta(\eta, t) = \omega(\eta, t) + \operatorname{Im}[H(\eta, t)e^{-i\theta}]$$

The OA ansatz gives Poisson-kernel densities $\rho = \frac{\hat{g}(\eta)}{2\pi}[1 + \sum_n \alpha^n e^{in\theta} + \text{c.c.}]$ with amplitude $\alpha(\eta, t)$ satisfying:

$$\partial_t\alpha + i\eta\alpha + \frac{1}{2}(H\alpha^2 - H^*) = 0$$

## Main result

For Lorentzian-distributed parameter $g(\eta) \sim L(\eta_0, \Delta)$ with width $\Delta > 0$:

**Theorem**: The off-manifold component $\hat{\rho}'_+(\theta, \eta, t)$ satisfies $\lim_{t \to \infty}\int \hat{\rho}'_+(\theta, \eta, t)\hat{g}(\eta)d\eta = 0$, i.e., the OA manifold is asymptotically attractive.

**Proof technique**: Decompose $\rho_+ = \hat{\rho}_+ + \hat{\rho}'_+$ where $\hat{\rho}_+$ is the OA component and $\hat{\rho}'_+$ is the off-manifold perturbation. The perturbation satisfies a continuity equation (eq. 9) that, after evaluation at the Lorentzian pole $\eta = -i\Delta$ via residue theorem, acquires a damping factor $e^{-\Delta t}$ from the analytic continuation into the lower half $\eta$-plane.

The key condition: $\hat{\rho}'_+$ must be analytic in $\operatorname{Im}(\eta) < 0$ and decay as $\operatorname{Im}(\eta) \to -\infty$. This is ensured by the initial data being a well-behaved probability distribution.

## Extensions

1. **Time-dependent parameters**: The proof extends to $\omega(\eta, t)$ and $H(\eta, t)$ varying in time, as long as analyticity conditions are preserved.
2. **Multi-dimensional parameters**: Multiple parameters $\eta \in \mathbb{R}^d$ with Lorentzian marginals.
3. **Non-global coupling**: Heterogeneous mean field $H$ depending on oscillator index via the parameter $\eta$, covering non-all-to-all network topologies.

## Connection to theta neurons and QIF

A network of theta neurons $\dot{\theta}_j = 1 - \cos\theta_j + (1+\cos\theta_j)(\eta_j + I_s(t))$ is a parameter-dependent Kuramoto-type system with $\Omega(\eta) = \eta$ and $H = I_s(t) + i$. The Lorentzian ansatz for $\eta$ (excitability parameter) gives the exact macroscopic dynamics via the OA reduction, linking to networks of quadratic integrate-and-fire (QIF) neurons.

## Relevance to [[kuramoto-stability-problem]]

This paper complements [[dietert-fernandez-2018-asymptotic-stability]] Proposition 4.1 (which proves OA attractiveness for the standard Kuramoto model with analytic $g(\omega)$). The Pietras-Daffertshofer result extends attractiveness to parameter-dependent systems, confirming that the OA manifold remains the correct target for global stability analysis even in generalized settings.

For Approach 22 (rational approximation + cooperativity): the $n$-pole approximation $g_n$ can be viewed as a parameter-dependent system where each pole contributes a Lorentzian component. The OA attractiveness for each component is guaranteed by this paper's result, supporting the validity of the pole-reduction approach.
