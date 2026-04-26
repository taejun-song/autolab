---
type: concept
title: "Landau Damping"
created: 2026-04-14
updated: 2026-04-17
sources:
  - "[[strogatz-2000-from-kuramoto-to-crawford]]"
  - "[[fernandez-gerard-varet-giacomin-2016-landau-damping]]"
  - "[[faou-rousset-2014-vlasov-hmf]]"
tags: [dynamical-systems, statistical-physics, plasma-physics, kinetic-theory, synchronization]
aliases: ["Landau damping"]
---

# Landau Damping

Landau damping is the exponential decay of macroscopic perturbations in a system whose linearization has a neutrally stable continuous spectrum on the imaginary axis, produced not by true eigenmodes but by phase mixing of a continuum of neutral modes with slightly different frequencies.

## The phenomenon

Identified by Landau in 1946 for the collisionless Vlasov equation of plasma physics: small perturbations of an equilibrium electron distribution decay exponentially in time even though the linearized Vlasov operator has no eigenvalues in the left half plane — the continuous spectrum sits on the imaginary axis. The decay of the macroscopic density is real, but it is a statement about a coarse moment of the distribution, not about the underlying microstate, which never actually relaxes: the fine structure in phase space simply oscillates faster and faster and integrates to zero against smooth test functions.

Landau's original argument used a contour-integral / Laplace-transform approach. The modern language attributes the decay to a pole of the *analytic continuation* of the resolvent into the left half plane — a pole not of the integrand but of its continuation, which shows up as a growth factor in the inverse-Laplace integral and picks up a genuine exponential as $t \to \infty$.

## Why it is counterintuitive

Naively, exponential decay of $r(t) \sim e^{-\gamma t}$ means "$-\gamma$ is in the spectrum." Landau's surprise is that it need not be: a neutrally stable continuous spectrum can mimic the behaviour of a stable point spectrum without containing any actually-stable modes. This is the origin of the slogan "Landau damping is not damping" — no information is lost, no entropy is produced, and the decay is reversible in principle (Landau echoes).

## Appearance in the Kuramoto model

[[strogatz-2000-from-kuramoto-to-crawford]] reports the following sequence of discoveries that made the Kuramoto–Vlasov analogy explicit:

1. **Strogatz–Mirollo (1991)** linearized the [[kinetic-formulation|continuum Kuramoto model]] about the incoherent state $\rho_0 = 1/(2\pi)$ and found its spectrum has a pure-imaginary continuous component and an isolated discrete eigenvalue that crosses into the right half plane at $K = K_c$.
2. **Matthews**, running numerics below threshold ($K < K_c$), observed exponential decay of the order parameter $r(t)$ at a rate $\lambda(K) < 0$ — the *analytic continuation* of the growth rate formula for $K > K_c$, evaluated below threshold where it has no right to predict anything.
3. **Rowlands** identified this as Landau damping during a lecture Matthews gave at Warwick. Strogatz writes:

> There definitely was a link between Landau damping and the relaxation phenomena we were seeing. It was awe-inspiring: the same mathematics describes the violent world of plasmas and the silent, hypnotic pulsing of fireflies perched along a riverbank.

4. **Strogatz–Mirollo–Matthews (1992)** proved the Kuramoto analogue rigorously: for $K < K_c$, the [[kuramoto-model|Kuramoto model]]'s incoherent state is only neutrally stable, yet $r(t) \to 0$ exponentially via Landau damping, with the decay rate given by the analytic continuation of the discrete eigenvalue.

For the Lorentzian native-frequency distribution $g(\omega) = \gamma/[\pi(\omega^2 + \gamma^2)]$, the explicit rate is $\lambda = K/2 - \gamma$, which is negative for $K < 2\gamma = K_c$ and drives the damped exponential decay.

## Nonlinear Landau damping in the Kuramoto model

The linear Landau damping result of Strogatz–Mirollo–Matthews (1992) was extended to the **full nonlinear** K-S dynamics by [[fernandez-gerard-varet-giacomin-2016-landau-damping|Fernandez, Gérard-Varet, and Giacomin (2016)]]. Their main result (Theorem 3.1): for $g \in C^n(\mathbb{R})$ with $n \geq 4$ satisfying the Penrose-type stability criterion $1 - \frac{K}{2}\int_{\mathbb{R}^+} \hat{g}(t)e^{-i\omega t}dt \neq 0$ for all $\omega$ in the closed lower half-plane, the order parameter decays as $\mathrm{R}(t) = O(t^{-n})$ from sufficiently small $C^n$ perturbations of incoherence. For symmetric unimodal $g$, the criterion reduces to the standard threshold $K < K_c = 2/(\pi g(0))$.

The proof uses a Volterra integral equation for the rescaled order parameter and a bootstrap argument adapted from Faou–Rousset's work on the Vlasov-HMF model, rather than the spectral-theoretic / rigged Hilbert space approach of [[chiba-2015-kuramoto-conjecture|Chiba (2015)]]. Chiba's method yields **exponential** decay for analytic $g$; FGG's yields **polynomial** decay but applies to finitely-smooth $g$ with explicit regularity-dependent rates.

The perturbation also converges weakly in $\mathcal{H}^{n-2}$ to a free-transport solution — the Kuramoto analogue of scattering in Vlasov theory.

The Faou-Rousset bootstrap approach for the Vlasov-HMF model ([[faou-rousset-2014-vlasov-hmf]]) inspired both the FGG and Dietert proofs. The Vlasov-HMF has the same two-mode coupling structure as Kuramoto, making it a natural testing ground for nonlinear Landau damping techniques.

## Why it matters beyond physics

Landau damping is the common grammar of a surprisingly wide class of problems: Vlasov plasmas, ideal fluid stability, solitary waves, bubbly fluids, resonance poles in atomic systems, and — via Strogatz–Mirollo and Crawford — the Kuramoto model. Every one of them features a neutral continuous spectrum at the linearized level, every one exhibits macroscopic exponential relaxation, and every one requires analytic continuation and careful handling of non-normal linear operators. Crawford's contribution to the Kuramoto story (see [[kuramoto-stability-problem]]) was essentially to import plasma-physics tools — center manifold reduction in the presence of a neutral continuous spectrum, singular amplitude equations — and adapt them to oscillator populations.

The deep lesson is that a continuous spectrum on the imaginary axis is a structural feature of mean-field / kinetic models ([[mean-field-coupling]] + [[kinetic-formulation]]) rather than a pathology to be engineered away. It is the generic picture one should expect, and it changes which tools are appropriate — contour integrals and analytic continuation rather than spectral expansions.
