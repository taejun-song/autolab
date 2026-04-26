---
type: source-summary
title: "Haraux & Jendoubi (2015) — The Convergence Problem for Dissipative Autonomous Systems"
created: 2026-04-18
updated: 2026-04-18
sources: []
tags: [dynamical-systems, pde, functional-analysis]
aliases: ["Haraux-Jendoubi 2015", "convergence problem dissipative systems", "Łojasiewicz-Simon"]
source_file: "../raw/papers/1502.06841.pdf"
source_kind: pdf
source_date: 2018-06-11
---

# Haraux & Jendoubi (2015) — The Convergence Problem for Dissipative Autonomous Systems

A comprehensive monograph on the convergence problem: when does a bounded trajectory of an autonomous evolution equation converge to a single equilibrium? Covers classical Lyapunov methods, gradient-like systems, LaSalle invariance, and the Łojasiewicz-Simon gradient inequality approach, with applications to semilinear heat and wave equations in infinite dimensions.

## Key results for the Kuramoto stability problem

### Corollary 6.2.2 (p.56) — Convergence from $L^p$ velocity bound

If a trajectory $u(t)$ has precompact range and its time derivative $u' \in L^p(\mathbb{R}^+, X)$ for some $p \geq 1$, then $\omega(u_0) \subset \mathcal{F}$ (the equilibrium set). Combined with isolated equilibria, this gives convergence to a single equilibrium.

**Relevance**: Our $\dot{\Psi} = K|r|^2$ gives $r \in L^2$ in Case A ($\Psi$ bounded). If the OA orbit is precompact in the right topology, this corollary gives convergence. The precompactness is the gap.

### Lemma 6.6.2 (p.60) — Precompactness via contraction semigroup + compact forcing

If $T(t)$ is a contraction semigroup with $\|T(t)\|_{L(X)} \leq Me^{-\sigma t}$ ($\sigma > 0$), and the forcing $H(t) \in K$ (compact set) a.e., then $V(t) = T(t)u_0 + \int_0^t T(t-s)H(s)ds$ has precompact range.

**Relevance**: The Kuramoto linearization around the PLS has spectral gap $\sigma = \lambda > 0$ (Dietert). The nonlinear forcing $Q(u)$ is bounded. If $Q(u)$ takes values in a compact set (finite-dimensional range, since only the $l=1$ mode couples), then this lemma gives precompactness of the orbit in Dietert's norm. This would close the topology gap.

### Chapter 10 (pp.91-104) — Łojasiewicz-Simon gradient inequality

Abstract convergence results for evolution equations where a Łojasiewicz-type inequality $|E(u) - E(u^*)|^{1-\theta} \leq C\|E'(u)\|$ holds near the equilibrium $u^*$. For analytic nonlinearities, this inequality is automatic (Theorem 10.2.1). The convergence results (Theorems 10.3.1, 10.3.2) give $u(t) \to u^*$ WITHOUT requiring precompactness of the orbit — the Łojasiewicz inequality provides the missing compactness.

**Relevance**: If $\Psi$ can be shown to satisfy a Łojasiewicz-Simon inequality near the PLS (plausible since $g$ is analytic), convergence follows without the topology-bridging gap. This is the most promising approach but requires verifying the abstract hypotheses for the OA equation.

## The gradient-like structure (Chapter 6)

A system is **gradient-like** if there exists a continuous function $E : Z \to \mathbb{R}$ (a Lyapunov function) such that $E(S(t)x)$ is nonincreasing (or nondecreasing) and $E(S(t)x) = E(x)$ for all $t$ implies $x$ is an equilibrium. Our $-\Psi$ is a Lyapunov function for the OA flow: $-\Psi$ is nonincreasing ($\dot{\Psi} = K|r|^2 \geq 0$), and $\dot{\Psi} = 0$ iff $r = 0$, which (by the no-periodic-orbits result) forces $\alpha \equiv 0$ (incoherence). So the OA system is gradient-like with Lyapunov function $-\Psi$ and equilibrium set $\{$incoherence, PLS$\}$.

For gradient-like systems, Theorem 6.1.1 gives: if the orbit has precompact range, then $\omega(u_0) \subset \mathcal{F}$. Combined with $\mathcal{F} = \{$incoherence, PLS$\}$ and local stability of the PLS, convergence follows.

## The fundamental solution identity (new result, 2026-04-18)

Applying the convergence theory to the OA equation revealed a new exact identity: the fundamental solution $\Phi$ of the $\beta = \partial_\omega\alpha$ ODE satisfies

$$|\Phi(\omega,t)| = \frac{1 - |\alpha(\omega,t)|^2}{1 - |\alpha(\omega,0)|^2}$$

This follows from integrating $d/dt\log(1-|\alpha|^2) = -K\text{Re}(\bar{r}\alpha)$ (the Psi identity) and connecting it to $d/dt|\Phi|^2 = -2K\text{Re}(\bar{r}\alpha)|\Phi|^2$. The identity links the slope energy $B(t) = \int|\partial_\omega\alpha|^2 g$ to the Psi functional.

**Consequence**: $|\beta|$ is bounded for locked oscillators (damping) and drifters (averaging). BUT: at the locked/drifting boundary $\omega = Kr^*$, the saddle-node singularity gives $|\beta|^2 \sim 1/|\omega_{\text{eff}}|$ (non-integrable). So $B(t)$ diverges logarithmically, and the Kolmogorov-Riesz equicontinuity route to precompactness FAILS.

**Structural insight**: the PLS itself has a boundary singularity at $\omega = Kr^*$ (locking transition). The $L^2(g)$ topology is the WRONG topology for precompactness — one needs a topology that doesn't resolve this singularity.

## Pages read

pp 1-5 (preface, table of contents), pp 55-60 (Chapter 6: gradient-like systems, Corollaries 6.2.1-6.2.2, Lemma 6.6.2), pp 91-100 (Chapter 10: Łojasiewicz-Simon inequality, abstract convergence results Theorems 10.2.5-10.3.1).

## Cross-links

- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — the Ψ functional makes the OA system gradient-like; Lemma 6.6.2 could bridge the topology gap
- [[kuramoto-stability-problem]] — the convergence problem for the PLS is an instance of the general theory in this book
- [[dietert-fernandez-2018-asymptotic-stability]] — Dietert's spectral gap provides the σ > 0 for Lemma 6.6.2
- [[landau-damping]] — the Volterra/semigroup structure of the K-S linearization is the contraction semigroup T(t)
