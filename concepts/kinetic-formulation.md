---
type: concept
title: "Kinetic Formulation"
created: 2026-04-14
updated: 2026-04-14
sources:
  - "[[strogatz-2000-from-kuramoto-to-crawford]]"
  - "[[ha-ko-park-zhang-2016-collective-synchronization]]"
tags: [dynamical-systems, statistical-physics, plasma-physics, kinetic-theory, synchronization]
aliases: ["continuum limit", "density-PDE formulation", "Eulerian formulation"]
---

# Kinetic Formulation

The kinetic formulation describes a population of interacting particles or oscillators in the thermodynamic limit $N \to \infty$ by a density evolving under a continuity equation whose velocity field is sourced by a self-consistent mean field, replacing the $N$-body ODE system with a single nonlinear integro-differential PDE.

## The idea

For a particle / oscillator population, let $\rho(x, t, \omega)\,\mathrm{d}x$ be the fraction of units of type $\omega$ whose state lies in $[x, x + \mathrm{d}x]$ at time $t$. If each unit moves under a velocity field $v(x, t, \omega)$ that depends on $\rho$ through a mean-field functional, then by conservation of units

$$
\frac{\partial \rho}{\partial t} \;=\; -\frac{\partial}{\partial x}\!\left(\rho\, v[\rho]\right),
$$

the nonlinearity hiding in the $\rho$-dependence of $v$. This is the Eulerian picture: instead of tracking $N$ trajectories, one tracks the density and lets the mean field close the system. The trade is exact in the $N \to \infty$ limit by the law of large numbers, so the kinetic formulation is the clean setting in which to ask questions about existence, stability, and bifurcations of different kinds of solutions.

The approach is an old one in kinetic theory: the Vlasov equation for collisionless plasmas, the Boltzmann equation for dilute gases, and the McKean–Vlasov equation for interacting diffusions all have the same shape. What differs is the choice of state variable ($x$ = position, momentum, phase, …) and the form of the mean-field velocity.

## In the Kuramoto model: the Kuramoto–Sakaguchi equation

[[strogatz-2000-from-kuramoto-to-crawford]] attributes the kinetic formulation of the [[kuramoto-model]] to Strogatz and Mirollo (1991); in the modern literature the resulting PDE is named the [[kuramoto-sakaguchi-equation|Kuramoto–Sakaguchi equation]] after Sakaguchi's 1988 noisy precursor. The state variable is the oscillator phase $\theta \in [0, 2\pi)$, the population is stratified by native frequency $\omega$ with distribution $g(\omega)$, and the density $\rho(\theta, t, \omega)$ satisfies

$$
\int_0^{2\pi} \rho(\theta, t, \omega)\, \mathrm{d}\theta \;=\; 1 \quad \text{for all } t, \omega,
$$

together with the continuity equation

$$
\frac{\partial \rho}{\partial t} \;=\; -\frac{\partial}{\partial \theta}(\rho v), \qquad v(\theta, t, \omega) \;=\; \omega + K r(t)\, \sin(\psi(t) - \theta),
$$

where the complex mean field $re^{i\psi}$ is determined self-consistently by

$$
r(t)\, e^{i\psi(t)} \;=\; \int_0^{2\pi}\!\!\int_{-\infty}^{\infty} e^{i\theta}\, \rho(\theta, t, \omega)\, g(\omega)\, \mathrm{d}\omega\, \mathrm{d}\theta.
$$

Substituting the mean-field expression back into $v$ yields a single closed nonlinear integro-differential equation for $\rho$. This PDE is the infinite-$N$ version of Kuramoto's ODE model, and all questions about existence, stability, bifurcation, and continuous / discrete spectrum can be formulated and attacked systematically in its language.

## Noisy version: Fokker–Planck

Sakaguchi (1988) extended the formulation to independent white noise on each phase variable, giving a Fokker–Planck equation:

$$
\frac{\partial \rho}{\partial t} \;=\; D\, \frac{\partial^2 \rho}{\partial \theta^2} \;-\; \frac{\partial}{\partial \theta}(\rho v),
$$

where $D \geq 0$ is the noise intensity. This regularises the operator — diffusion pushes the continuous spectrum into the left half plane — and is technically friendlier. The deterministic limit $D \to 0^+$ recovers the pure Kuramoto continuum PDE.

## Why it unlocks Kuramoto analysis

Three hard questions about the $N$-oscillator model become tractable once one is in the PDE setting:

1. **Stationary states.** Fixed points of the continuum PDE are the steady densities $\rho(\theta, \omega)$; the partially-synchronized state corresponds to a delta mass at a locked phase for oscillators with $|\omega| \leq Kr$ plus a $1/|\omega - Kr \sin\theta|$ profile for drifting oscillators. These coincide with what Kuramoto guessed in 1975 via self-consistency.
2. **Linear stability.** Linearising about the uniform incoherent state $\rho_0 = 1/(2\pi)$ gives a non-normal linear operator whose spectrum turns out to have a purely imaginary continuous component plus at most one real eigenvalue. This is the calculation that exposes [[landau-damping]] and underlies [[kuramoto-stability-problem]].
3. **Finite-$N$ convergence.** The continuum PDE is the formal $N \to \infty$ target for the particle model, and [[kuramoto-finite-n-convergence]] asks whether trajectories of the finite-$N$ system actually approach this target and with what fluctuations.

## Well-posedness theory

Turning the kinetic formulation into a rigorous PDE means proving existence, uniqueness, and regularity of solutions. For the [[kuramoto-sakaguchi-equation|Kuramoto–Sakaguchi equation]] this has been done at several regularity levels ([[ha-ko-park-zhang-2016-collective-synchronization]] §4.5):

- **Measure-valued solutions.** Lancellotti (2005), Cañizo–Carrillo–Rosado (2011), Carrillo–Choi–Ha–Kang–Kim (2014) — treat the density as a Radon measure on the phase space, supporting empirical-measure arguments and the $N \to \infty$ mean-field limit.
- **$L^\infty$-weak solutions.** Standard-regularity weak solutions.
- **BV / entropy weak solutions.** Amadori–Ha–Park, for the identical-oscillator case — uses the wave-front tracking method from hyperbolic conservation laws with a nonlocal flux, and gives $L^1$-stability of entropy solutions.
- **Fokker–Planck (noisy) version.** Lavrentiev–Spigler (2000) — existence and uniqueness of strong solutions for the diffusive $D > 0$ case.

These results are the PDE-side complement to the finite-$N$ convergence questions in [[kuramoto-finite-n-convergence]], and underlie the rigorous [[landau-damping|Landau-damping]] results in [[kuramoto-stability-problem]].

## Exact dimension reduction on the Ott–Antonsen submanifold

Orthogonal to the rigorous PDE analysis above, the [[kuramoto-sakaguchi-equation]] admits an **exact reduction on a distinguished invariant submanifold** — the [[ott-antonsen-ansatz|Ott–Antonsen ansatz manifold]] of Poisson-kernel densities (for the classical $d = 2$ case) or hyperbolic Poisson densities (for the $d \geq 3$ [[kuramoto-on-a-sphere|sphere generalization]]). Restricted to this manifold, the infinite-dimensional PDE collapses to a finite-dimensional ODE for a single complex parameter. This is not a weakened form of kinetic theory; it is a complete restriction to an invariant subset of the state space. The reduction does not address dynamics off the ansatz manifold, so it is complementary to — not a substitute for — the kinetic-theory well-posedness and stability analysis above.

## Limitations

The kinetic formulation is exact only as $N \to \infty$. Finite-$N$ corrections, fluctuations of order $O(N^{-1/2})$, and the possibility that these fluctuations destabilize the would-be equilibrium are beyond the PDE — they live in the residual particle problem, which the PDE has thrown away. The kinetic formulation is also closed only under [[mean-field-coupling]]; with structured networks, locality, or delays the velocity field no longer collapses to a single self-consistent mean, and a higher-dimensional density or a true network PDE is needed.
