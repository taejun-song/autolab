---
type: entity
title: "Winfree Model"
created: 2026-04-14
updated: 2026-04-14
sources:
  - "[[ha-ko-park-zhang-2016-collective-synchronization]]"
tags: [dynamical-systems, synchronization, mathematical-biology]
aliases: ["Winfree model", "Winfree coupled-oscillator model", "Winfree phase model"]
year_stated: 1967
---

# Winfree Model

The Winfree model is the first mathematical model of collective synchronization of a population of weakly-coupled biological oscillators, introduced by Arthur Winfree in 1967 via a sensitivity-function / influence-function coupling that captures the pulsatile interaction of biological rhythms.

## Governing equations

Each oscillator at node $j$ is described by a scalar phase $\theta_j \in S^1$ with its own natural frequency $\Omega_j$. Interactions are built from two $2\pi$-periodic functions: an **influence function** $I(\theta)$ specifying the stimulus each oscillator emits as a function of its phase, and a **sensitivity function** $S(\theta)$ (sometimes called a response function) specifying how each oscillator's frequency responds to a given stimulus. Winfree's assumptions:

1. The stimulus $I_c(\Theta)$ on oscillator $j$ is a weighted sum of influences from all other oscillators:
   $$I_c(\Theta) \;=\; \sum_{k=1}^{N}c_{kj}\,I(\theta_k).$$
2. The frequency perturbation $\omega_j^{\text{per}}$ is the product of the local sensitivity and the total stimulus:
   $$\omega_j^{\text{per}} \;=\; K\,S(\theta_j)\,I_c(\Theta).$$

Combining, the Winfree model is the coupled ODE system

$$
\dot{\theta}_j \;=\; \Omega_j \;+\; K\, S(\theta_j)\,\sum_{k=1}^{N} c_{kj}\,I(\theta_k), \qquad j = 1, \dots, N.
$$

The canonical Winfree choice is

$$S(\theta) = -\sin\theta, \qquad I(\theta) = 1 + \cos\theta,$$

giving the all-to-all version

$$
\dot{\theta}_j \;=\; \Omega_j - \frac{K}{N}\sin\theta_j\sum_{k=1}^{N}(1 + \cos\theta_k).
$$

See [[ha-ko-park-zhang-2016-collective-synchronization]] §2.2.1 and §3.

## Gradient flow structure

Unlike the [[kuramoto-model]], the Winfree model has no conservation laws in general (no balanced-law for total phase), and it is not a gradient flow for generic analytic $S$ and $I$. However, [[ha-ko-park-zhang-2016-collective-synchronization]] Proposition 2.1 shows:

**Proposition (Gradient flow criterion).** If the network is symmetric ($c_{kj} = c_{jk}$) and $S = I'$, then the Winfree model is a gradient flow:

$$\dot{\Theta} \;=\; -\nabla_\Theta V(\Theta), \qquad V(\Theta) \;=\; -\sum_{k=1}^{N}\Omega_k\theta_k - \frac{K}{2}\sum_{k, l=1}^{N}c_{kl}\,I(\theta_k)\,I(\theta_l).$$

The canonical choice $S = -\sin$, $I = 1 + \cos$ satisfies $I' = S$, so the canonical Winfree model *is* a gradient flow, which makes its analysis tractable. The absence of gradient structure for general $(S, I)$ pairs is what makes the general model substantially harder than Kuramoto.

## Four asymptotic patterns

Winfree dynamics are richer than Kuramoto because of the possibility of **oscillator death** — regimes in which some or all oscillators asymptotically stop ($\rho_j = 0$). [[ha-ko-park-zhang-2016-collective-synchronization]] classifies asymptotic states by [[phase-locked-state#Rotation numbers|rotation number]] into four regimes:

| Code | Name | Rotation-number condition |
|---|---|---|
| **COD** | Complete oscillator death | All $\rho_i = 0$ |
| **POD** | Partial oscillator death | $\rho_i = 0$ for $\geq 2$ but not all $i$ |
| **CPLS** | Complete phase-locked state | All $\rho_i = \rho \neq 0$ |
| **PPLS** | Partially phase-locked state | $\rho_i = \rho \neq 0$ for $\geq 2$ but not all $i$ |

## Sufficient-condition frameworks

Under structural conditions on $S$ and $I$ — $S$ odd, $I$ even, both $2\pi$-periodic and analytic, with monotonicity / convexity conditions on a subinterval $[0, \theta^*]$ — [[ha-ko-park-zhang-2016-collective-synchronization]] states the following theorems.

### Emergence of COD (Theorem 3.1, originally [Ha–Park–Ryoo, Ha–Ko–Park–Ryoo])

For a geometrically-determined value $\alpha^\infty$ and a threshold

$$K_c(\alpha^\infty) \;=\; -\frac{\Omega^\infty}{S(\alpha^\infty)I(\alpha^\infty)},$$

if $K > K_c(\alpha^\infty)$ and the initial data lies in a corresponding rectangle $\overline{\mathcal{R}}(\alpha)$, then every rotation number is zero: the population arrives at complete oscillator death. The mechanism is a confinement argument: sufficient coupling traps each oscillator inside an interval on which $\dot{\theta}_j \leq 0$.

### Emergence of PPLS (Theorem 3.2)

For a sub-ensemble $\mathcal{S}$ forming a majority (size $n/N > 4/(4 + \pi)$), initial phases confined within a small window, and the relative coupling strength in an intermediate range, one gets *exponential* convergence of phase differences within $\mathcal{S}$:

$$\max_{k, l \in \mathcal{S}}|\theta_k(t) - \theta_l(t)| \;\leq\; Ce^{-\lambda t}, \qquad t \geq 0.$$

The restriction to a majority sub-ensemble mirrors the Kuramoto "strong black-hole" mechanism: a dense enough seed group pulls additional oscillators in, and enough seed members guarantee the pulling effect dominates the drifting effect.

### Existence of periodic locked orbits (Theorem 3.4, Oukil–Kessi–Thieullen)

For natural frequencies in an interval $(1 - \gamma, 1 + \gamma)$ and coupling in a bifurcation range, there exists a positively invariant neighbourhood of complete phase synchronization within which the Winfree flow has periodic phase-locked orbits. This is an existence result — not a basin-of-attraction or stability result.

## Reduction to Kuramoto

In the low-coupling regime $\Omega_j = 1 + \varepsilon\omega_j$, $K = \varepsilon\kappa$ with $\varepsilon \ll 1$, averaging over one period of the free flow $\dot{\theta} = 1$ reduces the Winfree model to

$$
\dot{\theta}_j^1 \;\simeq\; \varepsilon\omega_j + \frac{\varepsilon\kappa}{4N\pi}\sum_{k=1}^{N}\sin(\theta_k^1 - \theta_j^1),
$$

which is (up to a rescaling $K \leftrightarrow \varepsilon\kappa/(4\pi)$) the [[kuramoto-model]]. For the canonical $S, I$ pair this reduction uses a single trigonometric identity and one period average, and the result holds only for short-time windows: the averaging kills high-frequency effects but leaves the slow phase dynamics alone. **Over long times the two models diverge** — Kuramoto cannot produce oscillator death, while Winfree can — which is why Winfree's asymptotic classification (COD / POD / CPLS / PPLS) is richer than Kuramoto's (which has only synchronization vs. incoherence).

## Historical position

Winfree (1967) is the paper $\dot{\theta}_j = \Omega_j + (\sum X(\theta_j))Z(\theta_i)$ that [[strogatz-2000-from-kuramoto-to-crawford]] credits with the first phenomenological articulation of synchronization as a threshold phenomenon. [[kuramoto-1975-self-entrainment]] replaced Winfree's $X \cdot Z$ coupling with the simpler pairwise sine $\sin(\theta_r - \theta_s)$, trading physical realism for a gradient-flow structure and exact solubility. The Winfree model survived as the "harder but more biologically accurate" sibling of Kuramoto.

## Open questions (as of 2016)

[[ha-ko-park-zhang-2016-collective-synchronization]] §3 lists the Winfree model as having *fewer* rigorous results than Kuramoto, precisely because it lacks the gradient-flow structure for general $(S, I)$. Specific gaps:

- Sufficient conditions for PPLS beyond the majority-sub-ensemble regime.
- A global basin of attraction for CPLS in the strong-coupling regime without the geometric conditions $(\mathcal{B}_1), (\mathcal{B}_2)$.
- Uniqueness of phase-locked states and their explicit structure.
- Stability of POD configurations and bifurcation from COD to POD as coupling decreases.

These are not major open problems in the sense of [[kuramoto-stability-problem]] or [[kuramoto-finite-n-convergence]] — they are research directions inherited from the better-understood Kuramoto case.
