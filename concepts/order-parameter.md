---
type: concept
title: "Order Parameter"
created: 2026-04-14
updated: 2026-04-14
sources:
  - "[[kuramoto-1975-self-entrainment]]"
  - "[[strogatz-2000-from-kuramoto-to-crawford]]"
tags: [statistical-physics, dynamical-systems, synchronization]
aliases: ["order parameter"]
---

# Order Parameter

An order parameter is a scalar (or low-dimensional) quantity whose value distinguishes the phases of a many-body system and serves as the dependent variable in a phase-transition description.

## The idea

In statistical mechanics an order parameter is identically zero in the disordered phase and rises continuously (second-order transition) or jumps discontinuously (first-order transition) once a control parameter crosses threshold. Magnetization for the Ising ferromagnet and the density difference in the liquid–gas transition are the classical examples. The order parameter compresses the full microstate into a single number whose behaviour near the critical point obeys scaling laws.

The same object plays the analogous role in non-equilibrium collective phenomena such as [[synchronization]], where the control parameter is coupling strength rather than temperature.

## In the Kuramoto model: the complex mean field

The standard modern order parameter for the [[kuramoto-model]] is the complex mean field

$$
r\, e^{i\psi} \;=\; \frac{1}{N}\sum_{j=1}^{N} e^{i\theta_j},
$$

a single complex number $re^{i\psi} \in \mathbb{C}$ with $r \in [0, 1]$. The modulus $r$ measures phase coherence and the argument $\psi$ is the population's average phase. Geometrically, plot each phase $\theta_j$ as a point on the unit circle; then $re^{i\psi}$ is the centroid of that swarm of points. If the swarm is tightly clumped, $r \approx 1$ and the population acts like a single giant oscillator; if the points are scattered uniformly around the circle, $r \approx 0$ and the individual oscillations add incoherently.

This form was introduced in later papers (see [[strogatz-2000-from-kuramoto-to-crawford]]), not the original [[kuramoto-1975-self-entrainment]]. Its usefulness is that the pairwise governing equation

$$\dot{\theta}_i \;=\; \omega_i + \frac{K}{N}\sum_{j=1}^{N}\sin(\theta_j - \theta_i)$$

can be rewritten exactly as the mean-field form

$$\dot{\theta}_i \;=\; \omega_i + K r\, \sin(\psi - \theta_i),$$

multiplying $r e^{i\psi}$ by $e^{-i\theta_i}$ and equating imaginary parts. In this form each oscillator is coupled only to the common mean field $(r, \psi)$, and the effective coupling strength $Kr$ produces a positive-feedback loop: as coherence grows, the effective drive grows, which recruits more oscillators into synchrony. This makes the self-consistency argument (see [[kuramoto-model]]) transparent.

## The 1975 order parameter vs. the modern one

[[kuramoto-1975-self-entrainment]] used a different observable — the fraction $\sigma$ of oscillators that become mutually locked:

$$
\sigma \;=\;
\begin{cases}
\dfrac{2}{\pi}\arctan\!\left(\dfrac{2\sqrt{1-\eta}}{\eta}\right), & \eta < 1, \\[6pt]
0, & \eta \geq 1,
\end{cases}
$$

where $\eta = 2\gamma/|v|$ for the Lorentzian case. The locked fraction $\sigma$ and the complex mean field magnitude $r$ are *different observables* of the same underlying partially-synchronized state, and they take different numerical values in general. For the Lorentzian, Kuramoto's self-consistency calculation in the modern formulation gives

$$r \;=\; \sqrt{1 - \frac{K_c}{K}}, \qquad K \geq K_c = 2\gamma,$$

and this formula has been confirmed by simulations. Both quantities vanish continuously as $K \searrow K_c$ (equivalently $\eta \nearrow 1$), so both witness the same second-order phase transition. The choice between them is a matter of analytical convenience — the modern $r$ wins because it lives in the ambient complex plane and the governing equation rewrites neatly in its terms.

## Why a single scalar suffices

Mean-field symmetry — every oscillator equivalent to every other, as in [[mean-field-coupling]] — makes the problem rotationally invariant in phase space, so the collective state is characterized by a single complex amplitude. In more structured settings (spatial lattices, heterogeneous networks) one can need vector or field order parameters, but the mean-field case collapses to a scalar.
