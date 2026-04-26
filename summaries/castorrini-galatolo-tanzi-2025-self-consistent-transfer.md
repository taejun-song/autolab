---
type: source-summary
title: "Castorrini-Galatolo-Tanzi (2025): Self-Consistent Transfer Operators and Convergence to Equilibrium"
created: 2026-04-25
updated: 2026-04-25
sources: []
tags: [dynamical-systems, statistical-physics, mean-field, convergence]
aliases: ["CGT 2025"]
source_file: ""
source_kind: url
source_date: 2025-06-01
---

# Castorrini-Galatolo-Tanzi (2025): Self-Consistent Transfer Operators and Convergence to Equilibrium

Proves local exponential convergence to equilibrium for mean-field coupled dynamical systems via spectral analysis of the self-consistent transfer operator differential, even in the strong coupling regime.

## Source

R. Castorrini, S. Galatolo, M. Tanzi, "The differential of self-consistent transfer operators and the local convergence to equilibrium of mean field strongly coupled dynamical systems," *J. Nonlinear Sci.* (2025). arXiv:2407.09314.

## Framework

The **self-consistent transfer operator (STO)** is $\mathcal{L}_\delta(f) := L_{\delta,f}(f)$, where $L_{\delta,f}$ is a Markov operator parameterized by a probability measure $f$ and coupling strength $\delta$. A fixed point $h$ satisfying $\mathcal{L}_\delta(h) = h$ is an equilibrium state. The paper asks: when does $\mathcal{L}_\delta^n(\mu) \to h$ exponentially for $\mu$ near $h$?

The function space architecture uses nested Banach spaces $B_{ss} \subset B_s \subset B_w$ with norms $\|\cdot\|_{ss} \geq \|\cdot\|_s \geq \|\cdot\|_w$.

## Main result (Proposition 6)

Under assumptions (a)--(f) including:
- Sequential Lasota-Yorke inequality: $\|L_{\delta,f_1} \circ \cdots \circ L_{\delta,f_n}(g)\|_s \leq A\lambda^n \|g\|_s + B\|g\|_w$ with $\lambda < 1$
- Fréchet differentiability of the coupling map at $h$
- Spectral contraction: $\exists n, \lambda < 1$ with $\|d\mathcal{L}_{\delta,h}^n(g)\|_s \leq \lambda \|g\|_s$

Then: **local strong contraction to $h$** — measures in a neighborhood converge exponentially: $\|h - \mathcal{L}_\delta^n(\mu)\|_s \leq Ce^{-\gamma n}\|h - \mu\|_s$.

## The differential formula

$$d\mathcal{L}_{\delta,h}(g) = L_{\delta,h}(g) + \partial L_{\delta,h}(g)$$

The first term is the uncoupled transfer action; the second captures how coupling changes when the distribution shifts.

## Examples

Only **expanding maps** (piecewise expanding maps on intervals, with deterministic or random coupling). No oscillator or Kuramoto examples.

## Relevance to [[kuramoto-stability-problem]]

The STO framework is the right mathematical language for the Kuramoto self-consistency problem: the OA dynamics define a self-consistent operator whose fixed point is the PLS. However:
- Kuramoto involves circle maps (not expanding maps), so the Lasota-Yorke inequality doesn't directly apply
- The spectral contraction condition (the key hypothesis) would need to be verified for the Kuramoto transfer operator — an open problem
- The result is LOCAL (convergence near $h$), matching Dietert's local stability; the GLOBAL question remains

The paper establishes the **abstract framework** that a Kuramoto convergence proof would ideally fit into, but does not provide the specific estimates needed for oscillator systems.

## Limitations

- Only locally valid (convergence near $h$, not global)
- Verifying the spectral contraction condition is the main difficulty in applications
- No explicit convergence rate formula
- Expanding maps only; no treatment of neutral or contracting dynamics
