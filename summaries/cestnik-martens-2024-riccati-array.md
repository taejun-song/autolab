---
type: source-summary
title: "Cestnik & Martens (2024) — Integrability of a Globally Coupled Complex Riccati Array"
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [dynamical-systems, synchronization, dimension-reduction, riccati-equation, integrability]
aliases: ["Cestnik-Martens 2024", "complex Riccati array"]
source_file: "../raw/papers/cestnik-martens-2024-riccati-array.pdf"
source_kind: pdf
source_date: 2024-02-09
---

# Cestnik & Martens (2024) — Integrability of a Globally Coupled Complex Riccati Array

Exact dimensionality reduction for arbitrary arrays of globally coupled complex-valued Riccati equations, generalizing Watanabe-Strogatz (1993) to complex amplitudes.

## Core result

An array of $N$ globally coupled complex Riccati equations

$$\dot{x}_j = ax_j^2 + bx_j + c, \quad a, b, c \in \mathbb{C}, \quad j = 1,\ldots,N$$

with arbitrary complex coefficients $a(t), b(t), c(t)$ admits an exact reduction via the Möbius transformation

$$x_j = Q + \frac{y\xi_j}{1 + s\xi_j}$$

where $Q, y, s$ are three complex macroscopic variables and $\xi_j \in \mathbb{C}$ are $N$ constants of motion. The reduced dynamics is six-dimensional (three complex ODEs):

$$\dot{Q} = aQ^2 + bQ + c, \quad \dot{y} = (b + 2aQ)y, \quad \dot{s} = -ay.$$

This generalizes:
- **Watanabe-Strogatz** (1993): the real-valued phase oscillator case ($x_j = e^{i\varphi_j}$, $|x_j| = 1$)
- **Ott-Antonsen** (2008): the thermodynamic limit $N \to \infty$ with Cauchy-Lorentzian frequency distributions

## Invariant disk property

For the special case of phase-amplitude oscillators with $x_j = r_j e^{i\varphi_j}$:

$$\dot{r}_j = (1 - r_j^2)\operatorname{Re}[h e^{-i\varphi_j}]$$

where $h$ encodes the coupling. The surface $r_j = 1$ is invariant: **oscillators that start inside the unit disk stay inside the disk forever**. This is the Möbius-geometric reason why the [[ott-antonsen-ansatz]] unit disk $|\alpha(\omega)| < 1$ is preserved.

## Connection to Kuramoto

For ensembles of pure phase oscillators, the complex Kuramoto order parameter is

$$Z_1 = \frac{1}{N}\sum_{j=1}^N x_j$$

which is expressed as a Möbius function of $Q, y, s$. The OA reduction arises in the thermodynamic limit by incorporating Cauchy-Lorentzian frequency heterogeneity, which can be absorbed into complex-valued coefficients $a, b, c$.

The paper notes that "complex-valued frequencies can be incorporated" and that "the generalization to complex numbers is substantial and provides room for qualitatively different dynamics." This is directly relevant to studying the OA equation at complex frequencies $\omega = \sigma - i\tau$ for Hypothesis (H).

## Relevance to [[kuramoto-stability-problem]]

- The Riccati formulation $\dot{\alpha} = -i\omega\alpha + \frac{K}{2}(\bar{r} - r\alpha^2)$ is exactly the $N = 1$ case with $a = -Kr/2$, $b = -i\omega$, $c = K\bar{r}/2$
- The invariant disk property $d/dt|\alpha|^2 = K\operatorname{Re}(\bar{r}\alpha)(1-|\alpha|^2)$ is the rotation cancellation identity proved in `GlobalMonotone.lean`
- For complex $\omega$ with $\operatorname{Im}(\omega) < 0$, the additional damping term gives $d/dt|\alpha|^2 = -2\tau|\alpha|^2 + K\operatorname{Re}(r\alpha)(1-|\alpha|^2)$, which makes the unit disk strictly attracting
