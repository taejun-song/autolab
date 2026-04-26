---
type: source-summary
title: "Chen, Engelbrecht, Mirollo (2017) — Hyperbolic Geometry of Kuramoto Oscillator Networks"
created: 2026-04-17
updated: 2026-04-17
sources: []
tags: [dynamical-systems, synchronization, dimension-reduction, group-theory]
aliases: ["Chen-Engelbrecht-Mirollo 2017", "hyperbolic geometry Kuramoto"]
source_file: "../raw/papers/1707.00713.pdf"
source_kind: pdf
source_date: 2017-07-03
---

# Chen, Engelbrecht, Mirollo (2017) — Hyperbolic Geometry of Kuramoto Oscillator Networks

The $d = 2$ precursor to [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere|Lipton–Mirollo–Strogatz (2021)]]: proves that the standard Kuramoto model for identical oscillators on $S^1$ is a **gradient flow on the hyperbolic disk** $\Delta$ (the Poincaré disk model), with the hyperbolic metric $ds^2 = 4|dw|^2/(1 - |w|^2)^2$.

## Bibliographic details

- **Authors:** Bolun Chen (Boston College, Physics), Jan R. Engelbrecht (Boston College, Physics), Renato Mirollo (Boston College, Mathematics).
- **Venue:** *J. Phys. A: Math. Theor.* **50**(35), 355101 (2017). arXiv:1707.00713.
- **Length:** 25 pages.
- **Pages read:** pp 1–5 (introduction, reduction to 3D system, Möbius group action, $w$-equation on the disk).

## Key results

### Reduction to the hyperbolic disk

For $N$ identical Kuramoto oscillators, trajectories are confined to 3D Möbius group orbits in the $N$-torus $T^N$. The Möbius group $G$ acts on $T^N$ by $M(z_1, \ldots, z_N) = (Mz_1, \ldots, Mz_N)$ where $Mz = \zeta(z - w)/(1 - \bar{w}z)$ with $|w| < 1$, $|\zeta| = 1$. The $w$-coordinate on the orbit satisfies:

$$\dot{w} = -\frac{1}{2}(1 - |w|^2)\bar{\zeta}\,\overline{\mathcal{a}}(\zeta M_w p),$$

where $\mathcal{a}$ is the order parameter functional evaluated at the transformed configuration. For Kuramoto phase models (coupling satisfying the homogeneity $\mathcal{a}(\zeta p) = \zeta\,\mathcal{a}(p)$), the $\zeta$-dependence drops out and the $w$-equation decouples:

$$\dot{w} = -\frac{1}{2}(1 - |w|^2)\overline{\mathcal{a}}(M_w p).$$

The factor $(1 - |w|^2)$ is the conformal factor of the hyperbolic metric, which is the first hint that the flow has hyperbolic-geometric structure.

### Gradient flow on the hyperbolic disk

For the $Z_1$ model (standard Kuramoto coupling $\mathcal{a} = e^{i\alpha}Z_1$ with $\alpha = \pi/2 - \delta$), the function $\mathcal{H} = R^2\sin\delta$ (where $R = |Z_1|$ is the order parameter magnitude) is:
- A **Lyapunov function** when $\sin\delta \neq 0$ (the flow is gradient w.r.t. the hyperbolic metric)
- A **conserved quantity** when $\sin\delta = 0$ (the flow is Hamiltonian w.r.t. the hyperbolic metric)

For the pure Kuramoto model ($\delta = 0$, i.e., $\sin$-coupling), $\mathcal{H} = 0$ and the flow is **completely integrable Hamiltonian**. For $\delta = \pm\pi/2$ ($\cos$-coupling), $\mathcal{H} = R^2$ is a Lyapunov function and the flow is gradient. These are the two extreme cases; general $\delta$ interpolates.

### Uniqueness of fixed points

For a generic 2D reduced group orbit, the $Z_1$ model has a **unique fixed point** corresponding to the **hyperbolic barycenter** of the oscillator configuration — the point $w^*$ minimizing $\sum_j d_{\text{hyp}}(w, \beta_j)^2$ where $\beta_j$ are the base-point phases. This confirms a conjecture of Watanabe and Strogatz.

## Relationship to the hypothesis

This paper provides the **finite-$N$, $d = 2$ foundation** for the [[hyperbolic-lyapunov-attack-on-kuramoto-stability|Lyapunov hypothesis]]:

- The $w$-equation $\dot{w} = -\frac{1}{2}(1 - |w|^2)\overline{\mathcal{a}}(M_w p)$ is exactly the finite-$N$ version of the OA ODE for identical oscillators.
- The gradient-flow structure gives the Lyapunov function for identical oscillators that the hypothesis seeks to generalize to non-identical ones.
- The factor $(1 - |w|^2)$ — the hyperbolic conformal factor — appears in both the $w$-equation and the log-ratio kernel $\log[(1 - |w|^2)/|w - p_i|^2]$ of Lipton's potential.
- For non-identical oscillators, the gradient-flow structure breaks because $\mathcal{a}$ depends on the time-varying mean field $r(t)$, which is the principal technical obstacle identified in the synthesis page.

## Cross-links

- [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]] — the higher-dimensional generalization that builds directly on this paper
- [[ott-antonsen-ansatz]] — the continuum-limit face of the same Möbius-group reduction
- [[kuramoto-model]] — the finite-$N$ system analyzed here
- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — the candidate log-ratio kernel originates from this paper's gradient-flow structure
