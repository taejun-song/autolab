---
type: source-summary
title: "Kuramoto (1975) — Self-Entrainment of a Population of Coupled Non-Linear Oscillators"
created: 2026-04-14
updated: 2026-04-14
sources: []
tags: [dynamical-systems, synchronization, statistical-physics, mathematical-biology]
aliases: ["Kuramoto 1975", "self-entrainment of a population of coupled non-linear oscillators"]
source_file: "../raw/papers/selfentrainment-of-a-population-of-coupled-nonlinear-oscillators.pdf"
source_kind: pdf
source_date: 1975-01-01
---

# Kuramoto (1975) — Self-Entrainment of a Population of Coupled Non-Linear Oscillators

Three-page conference contribution in which Yoshiki Kuramoto introduces and exactly solves the mean-field phase-oscillator model that now bears his name, establishing [[synchronization]] as a phase transition with a closed-form threshold and order parameter.

## Bibliographic details

- **Author:** Yoshiki Kuramoto (Department of Physics, Kyushu University, Fukuoka, Japan).
- **Venue:** Proceedings contribution, published 1975. The three pages read in the file are numbered 420–422 in the original volume, which together with the references (Kuramoto & Tsuzuki 1974; Winfree 1967; Wiener *Cybernetics* 1948) identifies it as the 1975 International Symposium on Mathematical Problems in Theoretical Physics contribution (Lecture Notes in Physics vol. 39, ed. H. Araki).
- **Pages read:** all three (the entire paper).
- **Length:** 3 pages of dense prose and equations; no figures.

## What the paper does

Kuramoto starts from a population of $N$ Stuart–Landau limit-cycle oscillators with linear pairwise coupling and reduces them — under mean-field coupling, large-damping, and thermodynamic-limit assumptions — to a pure phase model. He then solves that phase model in closed form for a Lorentzian distribution of native frequencies. The details of the derivation, the capture-window condition, and the closed-form formulas live on [[kuramoto-model]]; this summary records only what is distinctive about the source.

## Bullet distillation

- **Starting model (eq. 2).** Coupled complex oscillators $\dot{Q}_s = (i\omega_s + \alpha)Q_s + \sum_{r\neq s} v_{rs} Q_r - \beta|Q_s|^2 Q_s$. Kuramoto motivates this as the simplest nontrivial macroscopic self-sustained oscillator (citing an earlier 1974 Kuramoto–Tsuzuki chemical-instability study) extended to a population.
- **Three reductions.** (I) mean-field coupling $v_{rs} = v/N$; (II) large-damping limit $\alpha,\beta \to \infty$ with ratios held finite, which slaves the amplitudes $\rho_s$ to $\sqrt{\alpha/\beta}$; (III) $N \to \infty$.
- **Phase equation (eq. 3).** The three reductions give $\dot{\varphi}_s = \omega_s + (v/N)\sum_r \sin(\varphi_r - \varphi_s)$ — the equation now universally known as the Kuramoto model.
- **Threshold (eq. 4).** For a Lorentzian native-frequency distribution with width $\gamma$ centred on $\omega_0$, the dimensionless parameter $\eta \equiv 2|\gamma/v|$ controls the transition. Synchronization exists only for $\eta < 1$, i.e. when coupling strength exceeds twice the frequency spread.
- **Two populations (A/B).** Below threshold, oscillators inside the capture window $|\omega_s - \omega_0|/(v\sqrt{1-\eta}) < 1$ lock to the common frequency $\tilde{\omega}_s = \omega_0$ (group A, eqs. 5–6); those outside fail to lock but have pulled effective frequencies and residual periodic motion (group B, eqs. 7–9).
- **Order parameter (eq. 10).** $\sigma = (2/\pi)\arctan(2\sqrt{1-\eta}/\eta)$ for $\eta < 1$, else zero — the fraction of locked oscillators. Continuous rise from threshold signals a second-order transition.
- **Effective-frequency spectrum (eq. 11).** Delta peak at $\omega_0$ of weight $\sigma$ plus a continuous background whose intensity near the peak is suppressed by a factor $|\tilde{\omega} - \omega_0|$. Kuramoto remarks that this spectral shape qualitatively resembles the α-rhythm of human EEG — an explicit callback to Wiener's *Cybernetics* speculation.

## Why this source matters

This three-page note is the origin point of the modern mathematical theory of synchronization. Winfree had argued in 1967 that mutual synchronization should be a phase transition but had no exactly-soluble example. Kuramoto supplies exactly that: a model simple enough to yield closed-form formulas, general enough to retain the essential physics (distributed frequencies, weak global coupling, a threshold, a continuously-rising order parameter). Everything downstream — the modern complex-mean-field formulation, finite-$N$ corrections, non-Lorentzian frequency distributions, network extensions, chimera states, applications to Josephson arrays and EEG — is built on top of this paper.

## What the paper does not address

- **General frequency distributions.** The Lorentzian assumption is essential to the derivation. Kuramoto gives no hint of whether the qualitative picture (threshold + continuous order parameter + locked/drifting split) generalizes. It does, but the rigorous theory came later.
- **Stability.** The paper exhibits the partially-synchronized solution but does not prove it is dynamically stable. The stability of the incoherent and partially-synchronized branches is a subtle and still-incomplete story (Strogatz–Mirollo and successors).
- **Finite $N$.** Everything uses $N \to \infty$. Finite-population corrections, fluctuations, and whether they eat the threshold are not discussed.
- **Non-sinusoidal coupling or noise.** Pure $\sin(\varphi_r - \varphi_s)$ coupling, no noise. Later work adds higher harmonics, phase shifts (Sakaguchi–Kuramoto), and stochastic forcing.
- **Topology.** Strict all-to-all coupling. No lattice, no network, no locality.

## Notable quote

> It is very interesting to notice that our spectrum resembles that of the α-rhythm of human brain wave.

— closing remark, connecting the mathematical spectrum to Wiener's 1948 speculation in *Cybernetics* that neural ensembles produce the α-rhythm through collective synchronization.

## References (as given in the paper)

1. Y. Kuramoto and T. Tsuzuki, *Prog. Theor. Phys.* **52** (1974), 1399.
2. A. T. Winfree, *J. Theor. Biol.* **16** (1967), 15.
3. N. Wiener, *Cybernetics*, MIT Press, Cambridge, Mass., 1948.

None of these references has a source-summary in the wiki yet.
