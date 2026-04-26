---
type: concept
title: "Mean-Field Coupling"
created: 2026-04-14
updated: 2026-04-14
sources:
  - "[[kuramoto-1975-self-entrainment]]"
  - "[[strogatz-2000-from-kuramoto-to-crawford]]"
tags: [dynamical-systems, statistical-physics, synchronization]
aliases: ["all-to-all coupling", "global coupling", "infinite-range interaction"]
---

# Mean-Field Coupling

Mean-field coupling is the modelling ansatz in which every pair of units in a population interacts with the same strength scaled as $1/N$, so that each unit effectively sees a global average rather than individual neighbours.

## Definition

For a population of $N$ units with pair interaction $v_{rs}$, mean-field coupling is the choice

$$v_{rs} = \frac{v}{N}, \qquad r \neq s,$$

independent of the pair. The $1/N$ scaling is essential: it keeps each unit's total input bounded as $N \to \infty$, so the thermodynamic limit is well-defined. Without the scaling the interaction energy per unit would diverge.

## Why it is used

Mean-field coupling trades physical realism (nearest-neighbour or distance-decaying interactions) for analytic tractability. The pairwise sum becomes a single self-consistent field that every unit couples to, and the $N$-body problem reduces to a one-body problem in an effective drive. In the thermodynamic limit the self-consistency equation is typically a fixed-point equation for a small number of order parameters.

This is the same logic that underlies mean-field theory for the Ising model in statistical mechanics — infinite-range interactions make a model exactly soluble at the cost of removing spatial structure and fluctuations.

## In the Kuramoto model

[[kuramoto-1975-self-entrainment]] uses this ansatz to reduce the $N$-oscillator phase system to an equation each oscillator satisfies against a common rotating complex mean field. The pairwise $\sin(\varphi_r - \varphi_s)$ interaction in the [[kuramoto-model]] collapses via $v_{rs} = v/N$ into a sine drive against a self-consistently-determined phase, and the partially-synchronized state becomes a fixed point that is solvable in closed form for a Lorentzian native-frequency distribution.

The self-consistency is cleanest in the modern complex-mean-field form (see [[order-parameter]]): defining $re^{i\psi} = (1/N)\sum_j e^{i\theta_j}$ and multiplying by $e^{-i\theta_i}$, the pairwise sum rewrites exactly as

$$\dot{\theta}_i \;=\; \omega_i + K r\, \sin(\psi - \theta_i).$$

This is the payoff of mean-field coupling made literal: each oscillator is **uncoupled from the others**, interacting only through the two global numbers $(r, \psi)$. The effective forcing on oscillator $i$ is $K r$, so the coupling has been effectively rescaled by the coherence it produces. As more oscillators become locked, $r$ grows, $Kr$ grows, more oscillators get pulled in — a positive feedback loop [[strogatz-2000-from-kuramoto-to-crawford]] calls the underlying mechanism of spontaneous synchronization (first identified by Winfree 1967, and especially clean in the Kuramoto case).

## Limitations

Removing spatial structure means mean-field coupling cannot describe patterns, waves, or locality-driven phenomena — no chimera states on rings, no lattice-wave propagation, no network-topology effects. It is a first-order caricature whose value is that it makes [[synchronization]] mathematically tractable and sets the baseline against which more realistic coupling topologies are compared.
