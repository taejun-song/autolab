---
type: source-summary
title: "Villani (2009) — Hypocoercivity"
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [pde, kinetic-theory, functional-analysis, convergence]
aliases: []
source_file: "../raw/papers/villani-2009-hypocoercivity.pdf"
source_kind: pdf
source_date: 2009-01-01
---

# Villani (2009) — Hypocoercivity

Systematic study of convergence to equilibrium for degenerate diffusive equations via modified Lyapunov functionals combining dissipation and transport.

## Overview

AMS Memoirs monograph, 141 pages. Develops the theory of **hypocoercivity**: convergence to equilibrium for equations that are not themselves coercive, but become so when the interplay between a dissipative part and a conservative part is exploited.

## Framework

The generator is decomposed as $L = A^*A + B$ where $A$ is the dissipative component and $B$ is the conservative (skew-symmetric) component. The key construction is a **modified entropy** (Lyapunov functional):

$$H[f] = \frac{1}{2}\|f\|^2 + \varepsilon\langle Af, f\rangle$$

which satisfies $\frac{dH}{dt} \leq -\lambda H$ for suitable $\varepsilon > 0$ and $\lambda > 0$, yielding exponential convergence.

## Structure

- **Part I**: Abstract $L = A^*A + B$ theory. Conditions on commutators $[A,B]$, $[A,[A,B]]$, etc. (Hörmander-type bracket conditions at the functional level).
- **Part II**: Auxiliary operator method — a more flexible variant using operators $\tilde{A}$ built from $A$ and $B$.
- **Part III**: Nonlinear equations, including Vlasov–Fokker–Planck (§17), Boltzmann equation, and fluid limits.

## Relevance to Kuramoto

The hypocoercive framework **requires some dissipation** — collision operators, diffusion terms, or damping. The noiseless Kuramoto equation in its continuum PDE form lacks such dissipation. However, the $n$-pole Ott–Antonsen system has damping terms $-\gamma_j$, which could serve as the dissipative component in a hypocoercive analysis. See [[landau-damping]] for the related phase-mixing mechanism and [[kuramoto-stability-problem]] for the target application.

## MSC

35B40, 35K65, 76P05.
