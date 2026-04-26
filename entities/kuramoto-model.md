---
type: entity
title: "Kuramoto Model"
created: 2026-04-14
updated: 2026-04-15
sources:
  - "[[kuramoto-1975-self-entrainment]]"
  - "[[strogatz-2000-from-kuramoto-to-crawford]]"
  - "[[ha-ko-park-zhang-2016-collective-synchronization]]"
  - "[[ha-kim-ryoo-2016-emergence-phase-locked-states]]"
  - "[[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]]"
tags: [dynamical-systems, synchronization, statistical-physics, mathematical-biology]
aliases: ["Kuramoto model", "Kuramoto phase-oscillator model", "Kuramoto self-entrainment model"]
---

# Kuramoto Model

The Kuramoto model is a system of $N$ mean-field-coupled phase oscillators with distributed native frequencies, introduced by Yoshiki Kuramoto in 1975 as the first exactly-soluble model of [[synchronization]] as a phase transition.

## Derivation from Stuart–Landau oscillators

Kuramoto starts from a population of complex Stuart–Landau limit-cycle oscillators with pairwise linear coupling:

$$
\dot{Q}_s \;=\; (i\omega_s + \alpha)\, Q_s \;+\; \sum_{r \neq s} v_{rs}\, Q_r \;-\; \beta\, |Q_s|^2\, Q_s,
\qquad s = 1,\dots,N.
$$

Three simplifying assumptions reduce this to a pure phase equation:

1. [[mean-field-coupling]]: $v_{rs} = v/N$, identical for every pair.
2. Large damping: $\alpha, \beta \to \infty$ with the ratio $\alpha/\beta$ and $\omega_s, v$ held finite, which pins each amplitude $\rho_s$ at the limit-cycle radius $\sqrt{\alpha/\beta}$.
3. Thermodynamic limit: $N \to \infty$.

Writing $Q_s = \rho_s e^{i\varphi_s}$ and dropping the (now slaved) amplitudes, the dynamics become

$$
\dot{\varphi}_s \;=\; \omega_s \;+\; \frac{v}{N}\sum_{r=1}^{N} \sin(\varphi_r - \varphi_s).
$$

This phase equation is the Kuramoto model. Each $\omega_s$ is drawn from a given distribution $g(\omega)$, and the coupling strength $v$ is the control parameter.

## Exact solution for Lorentzian frequencies

Kuramoto solves the model in closed form when $g(\omega)$ is a Lorentzian of width $\gamma$ centred on $\omega_0$:

$$g(\omega) \;=\; \frac{\gamma/\pi}{(\omega - \omega_0)^2 + \gamma^2}.$$

Define the dimensionless ratio

$$\eta \;\equiv\; \frac{2\gamma}{|v|}.$$

Then:

- **Above threshold ($\eta \geq 1$).** No collective synchronization. Every oscillator drifts at its own effective frequency, the [[order-parameter]] $\sigma$ equals zero, and the effective-frequency distribution is continuous.
- **Below threshold ($\eta < 1$).** The population splits into two groups.
    - **Locked group.** Oscillators whose native frequency lies within the capture window $|\omega_s - \omega_0|/(v\sqrt{1-\eta}) < 1$ become mutually synchronized and rotate at the common effective frequency $\tilde{\omega}_s = \omega_0$.
    - **Drifting group.** Oscillators outside the capture window fail to lock but have pulled effective frequencies $\tilde{\omega}_s = \omega_0 + (\omega_s - \omega_0)\sqrt{1 - v^2(1-\eta)/(\omega_s - \omega_0)^2}$, with periodic residual motion $f_s(t) = f_s(t + 2\pi/\tilde{\omega}_s)$.
- **Order parameter.** The fraction $\sigma$ of locked oscillators is

$$\sigma \;=\; \frac{2}{\pi}\, \arctan\!\left(\frac{2\sqrt{1-\eta}}{\eta}\right), \qquad \eta < 1,$$

rising continuously from $\sigma = 0$ at $\eta = 1$ to $\sigma = 1$ as $\eta \to 0$.

- **Effective-frequency distribution.** Writing $\chi = 1 - \eta$ for $\eta < 1$ and $\chi = 0$ otherwise,

$$
f(\tilde{\omega}) \;=\; \sigma\, \delta(\tilde{\omega} - \omega_0) \;+\; \frac{\gamma}{\pi}\, \frac{|\tilde{\omega} - \omega_0|}{\big[(\tilde{\omega} - \omega_0)^2 + \gamma^2 + v^2\chi\big]\sqrt{(\tilde{\omega} - \omega_0)^2 + v^2\chi}}.
$$

The delta peak at $\omega_0$ represents the macroscopic synchronized mode; the continuous background is the drifting population. The prefactor $|\tilde{\omega} - \omega_0|$ strongly suppresses the background near $\omega_0$ — Kuramoto notes the resulting spectrum qualitatively resembles the α-rhythm of the human EEG, echoing an earlier speculation by Wiener.

## Modern formulation: complex mean field

The standard bookkeeping used in the literature from the 1980s onward is the complex mean field (see [[order-parameter]])

$$
r\, e^{i\psi} \;=\; \frac{1}{N}\sum_{j=1}^{N} e^{i\theta_j},
$$

with $r \in [0, 1]$ the coherence and $\psi$ the average phase. Multiplying each side by $e^{-i\theta_i}$ and equating imaginary parts shows that the pairwise-sum governing equation is equivalent to

$$
\dot{\theta}_i \;=\; \omega_i + K r\, \sin(\psi - \theta_i),
$$

where $K$ is the coupling strength (the normalisation $K = v$ is standard in this formulation). In this form each oscillator appears to feel only a common sinusoidal drive toward $\psi$, with effective coupling $Kr$. This sets up a positive-feedback mechanism: as the population becomes more coherent $r$ grows, so the effective coupling $Kr$ grows, which recruits more oscillators into the synchronized pack — the mechanism Winfree first identified and the reason [[mean-field-coupling]] makes the Kuramoto model soluble.

## General symmetric unimodal $g(\omega)$

When $g(\omega)$ is symmetric about its mean (shifted to zero by a change of frame), unimodal, and nowhere increasing on $[0, \infty)$, Kuramoto's self-consistency argument yields a critical coupling

$$
K_c \;=\; \frac{2}{\pi g(0)},
$$

and a bifurcating branch whose amplitude obeys the square-root scaling

$$
r \;\approx\; \sqrt{\frac{16}{\pi K_c^3}}\, \sqrt{\frac{\mu}{-g''(0)}}, \qquad \mu \;\equiv\; \frac{K - K_c}{K_c},
$$

close to onset. The bifurcation is supercritical when $g''(0) < 0$ (the generic case for smooth unimodal densities) and subcritical when $g''(0) > 0$. For the Lorentzian special case $g(\omega) = \gamma/[\pi(\omega^2 + \gamma^2)]$ the self-consistency integral is exactly solvable and gives $K_c = 2\gamma$ (equivalently $\eta = 1$) along with the explicit closed form

$$
r \;=\; \sqrt{1 - \frac{K_c}{K}}, \qquad K \geq K_c,
$$

which matches Kuramoto's 1975 result for the locked fraction via $\sigma = (2/\pi)\arctan(2\sqrt{1-\eta}/\eta)$ at the level of the same underlying solution — they are two different observables of the same state.

## Continuum limit: the Kuramoto–Sakaguchi equation

The $N \to \infty$ version of the Kuramoto model is the nonlinear integro-differential PDE known as the [[kuramoto-sakaguchi-equation|Kuramoto–Sakaguchi equation]]:

$$
\partial_t f + \partial_\theta(\omega[f] f) \;=\; 0, \qquad \omega[f](\theta, \Omega, t) \;=\; \Omega - K\int_{\mathbb{T}}\sin(\theta - \theta_*)\rho(\theta_*, t)\,d\theta_*,
$$

for the density $f(\theta, \Omega, t)$ of oscillators with phase $\theta$ and native frequency $\Omega$, with local phase density $\rho = \int f\, d\Omega$. Strogatz and Mirollo (1991) formulated this PDE in the equivalent form $\partial_t\rho = -\partial_\theta(\rho v)$ with $v = \omega + Kr\sin(\psi - \theta)$ and used it to frame stability questions rigorously. Sakaguchi (1988) added independent white noise on the phases, yielding the Kuramoto–Sakaguchi–Fokker–Planck equation whose $D \to 0^+$ limit recovers the deterministic PDE. Well-posedness theory (measure-valued, $L^\infty$-weak, and BV/entropy weak solutions) is now substantially developed for identical oscillators; see [[kuramoto-sakaguchi-equation]] and [[kinetic-formulation]].

## Gradient flow structure

Under symmetric network capacity ($c_{kj} = c_{jk}$) and the zero-sum-of-natural-frequencies condition $\sum_k \Omega_k = 0$ (obtainable by choosing a rotating frame), the Kuramoto model is a gradient flow with analytic potential:

$$
\dot{\Theta} \;=\; -\nabla_\Theta V(\Theta), \qquad V(\Theta) \;=\; -\sum_{k=1}^{N}\Omega_k \theta_k + \frac{K}{2N}\sum_{k, l = 1}^{N}c_{kl}\,(1 - \cos(\theta_k - \theta_l)).
$$

This structural fact has two consequences. First, it rules out chaotic behaviour: gradient flows with analytic potentials have convergent orbits whenever they are uniformly bounded (Łojasiewicz-type arguments). Second, it converts the complete-synchronization question into a uniform-boundedness question: to prove that every generic trajectory converges to a phase-locked state, it is enough to prove that the fluctuations $\hat{\theta}_j = \theta_j - \theta_c$ around the centre of mass $\theta_c = N^{-1}\sum_k \theta_k$ stay uniformly bounded in time (Theorem 2.2 in [[ha-ko-park-zhang-2016-collective-synchronization]]).

## Complete synchronization for generic initial data

The gradient-flow dichotomy reduces complete synchronization to a uniform-boundedness question, and [[ha-kim-ryoo-2016-emergence-phase-locked-states]] resolves it for generic initial data at large coupling:

**Theorem 1.1** ([Ha–Kim–Ryoo 2016]). Suppose $\sum_i \Omega_i = 0$, the initial configuration $\Theta^0 \in [-\pi, \pi)^N$ satisfies $r_0 := |N^{-1}\sum_j e^{i\theta_{j0}}| > 0$ and $\theta_{j0} \neq \theta_{k0}$ for $j \neq k$, and $\max_j|\Omega_j| < \infty$. Then there exists a coupling threshold $K_\infty > 0$ such that for $K \geq K_\infty$ there is a phase-locked state $\Theta^\infty$ with

$$\lim_{t \to \infty}||\Theta(t) - \Theta^\infty||_\infty = 0.$$

This **extends previous results** (Choi–Ha–Jung–Kim 2012, Ha–Kim–Park 2015, Dörfler–Bullo 2011) which all required $D(\Theta^0) < \pi + \varepsilon$ with $\varepsilon \ll 1$ — i.e. initial configurations confined to a half-circle. Ha–Kim–Ryoo removes that restriction entirely, allowing configurations scattered anywhere on $S^1$, at the cost of driving $K$ sufficiently large. The only excluded initial data is the measure-zero set $r_0 = 0$ (which includes splay states and symmetric balanced configurations).

**Proof strategy (three ingredients).** The full argument rescales time $\tau = Kt$ and natural frequencies $\tilde{\Omega}_j = \Omega_j/K$ so that the problem with large $K$ and finite $\Omega$ becomes a problem with $K = 1$ and small $\tilde{\Omega}$ — bounded by $L/K_\infty$ for a chosen small $L_\infty$. The $K = 1$ small-frequency case is then handled by combining:

1. **Bipolar dichotomy for identical oscillators.** For identical oscillators ($\Omega_j \equiv 0$) with $r_0 > 0$ and distinct initial phases, asymptotic behaviour is either complete phase synchronization (all oscillators coincide) or a bipolar configuration with at most one oscillator located $\pi$ away from the main cluster. The "synchronous set" $\mathcal{I}_s$ has at least $N - 1$ elements and contracts to a single phase exponentially at rate $Ke^{-K\lambda(t - T_2)}$ for an explicit $\lambda > 0$ (Lemmas 3.3, 3.4 of the paper).

2. **Finite-time continuity between identical and non-identical systems.** Let $\Theta^I$ and $\Theta^{NI}$ be solutions of the identical ($\Omega = 0$) and non-identical ($\Omega \neq 0$) Kuramoto systems with the same initial data. A Gronwall estimate gives
$$||\Theta^{NI}(t) - \Theta^I(t)||_\infty \;\leq\; \frac{||\Omega||_\infty}{2K}\left(e^{2Kt} - 1\right), \qquad t > 0$$
(Lemma 4.2). This blows up exponentially with $t$, but on any fixed finite window $[0, T]$ and for $||\Omega||_\infty$ small enough, the non-identical solution stays arbitrarily close to its identical counterpart — long enough to inherit the bipolar dichotomy from step 1.

3. **Strong-black-hole confinement** (Proposition 4.1). Once the finite-time continuity places $N - 1$ non-identical oscillators inside an arc of length $\ell$, sufficient coupling $K > D(\Omega)/(\frac{n_0}{N}\sin\ell - \frac{2(N - n_0)}{N}\sin\frac{\ell}{2})$ with $n_0 = N - 1$ traps those oscillators there forever and bounds the lone remaining oscillator's phase within a $4\pi$-neighbourhood of the arc — *uniformly in time*. Uniform boundedness of $D(\Theta(t))$ then triggers the gradient-flow dichotomy (Theorem 2.2), and convergence to a phase-locked state follows.

The **$N = 2$ base case** is independently handled via the Adler equation $\dot{\theta} = \Omega - K\sin\theta$ (with $\theta = \theta_2 - \theta_1$, $\Omega = \Omega_2 - \Omega_1$): for $K > |\Omega|$, the Adler equation has a stable equilibrium $\theta_s^1 \in (0, \pi/2)$ and an unstable one $\theta_u^1 \in (\pi/2, \pi)$, and every initial datum in $[-\pi, \pi) \setminus \{\theta_u^1\}$ converges to $\theta_s^1$ (Lemma 2.5). This is the scalar toy model that makes the large-coupling intuition precise.

**Limitations.** The theorem is strictly an *existence* statement for the limit $\Theta^\infty$. It does not give: (a) an explicit value or even a useful bound on $K_\infty$, (b) uniqueness of the limit up to phase-shift (which holds only in the half-circle regime per Remark 1.1 of the paper), or (c) linear or orbital stability of $\Theta^\infty$. Together with earlier half-circle results (Choi et al., Ha–Kim–Park, Dörfler–Bullo), this essentially closes the large-$K$ *existence* question for complete synchronization; the large-$K$ *optimal-threshold* and *stability* questions remain open.

## Dimension reduction via Möbius group orbits

A parallel line of attack on the Kuramoto model, orthogonal to the functional-analytic / PDE toolkit surveyed above, is the **dimension reduction via Möbius transformations**. The observation is that for **identical** Kuramoto oscillators ($\Omega_j = \Omega$ for all $j$), the $N$-body dynamics on the $N$-torus are confined to group orbits of the 3-dimensional Möbius group of the unit disk — independent of $N$. This is the Watanabe–Strogatz transformation (1993) and Marvel–Mirollo–Strogatz (2009).

In the continuum limit $N \to \infty$, the orbit of the uniform density on $S^1$ under the same Möbius group action consists of **Poisson-kernel densities** $\rho(\theta) = (2\pi)^{-1}(1 - |z|^2)/|e^{i\theta} - z|^2$ parameterised by $z \in \mathbb{D}$. This is the Ott–Antonsen ansatz (2008), and on this invariant submanifold the [[kuramoto-sakaguchi-equation|Kuramoto–Sakaguchi equation]] collapses to a closed ODE for $z(t)$. The finite-$N$ and infinite-$N$ reductions are **the same group action** just parameterised differently — a fact made explicit in [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]], who generalise the entire story to the [[kuramoto-on-a-sphere|Kuramoto model on $S^{d-1}$]] for arbitrary $d \geq 2$ using the Möbius group of the unit ball $B^d$ with its hyperbolic metric.

The reduction is **exact**, not an approximation: dynamics restricted to the ansatz manifold are reproduced by the reduced ODE with no error. Its limitation is equally sharp: it says **nothing** about dynamics that leave the ansatz manifold, so by itself it does not resolve the [[kuramoto-stability-problem]] or [[kuramoto-finite-n-convergence]] for generic initial data. What it does give is (i) exactly-solvable model dynamics to test conjectures against, and (ii) in special cases with positive-weight linear order parameters, a **hyperbolic Lyapunov potential** that proves global convergence to complete synchronization on the ansatz manifold. See [[ott-antonsen-ansatz]] for the full framework.

## Finiteness of phase-locked states

How many distinct phase-locked states does the Kuramoto model have? For $K \geq ||\Omega||_\infty$ there is a clean parameterisation in terms of a pair $(\beta, \Sigma) \in [||\Omega||_\infty/K, 1] \times \{-1, 1\}^N$, and the cardinality is bounded in Theorem 4.3 of [[ha-ko-park-zhang-2016-collective-synchronization]]:

$$2^{N-1} \;\leq\; |\mathcal{P}| \;\leq\; 2^N \qquad \text{for } K \gg ||\Omega||_\infty,$$

where $\mathcal{P}$ is the set of phase-locked states up to rigid rotation. Each $\Sigma \in \{-1, 1\}^N$ records a combinatorial "sign choice" for each oscillator; the full count is this $2^N$ minus configurations eliminated by the geometric self-consistency $\beta = N^{-1}\sum_j \sigma_j\sqrt{1 - (\Omega_j/(K\beta))^2}$. See [[phase-locked-state]] for the details.

## Stability arc: Kuramoto–Nishikawa → Strogatz–Mirollo → Crawford

[[strogatz-2000-from-kuramoto-to-crawford]] tells the 25-year story of how the stability questions Kuramoto flagged but did not resolve were gradually clarified:

- **Kuramoto–Nishikawa (1987, 1989).** Two heuristic attempts to derive an evolution equation for $r(t)$ near bifurcation. Both contained uncontrolled approximations; the first predicted anomalous algebraic decay, the second (after an honest retraction of the first) predicted standard exponential decay via a memory kernel but without systematic derivation. Neither was correct, but both came tantalisingly close.
- **Strogatz–Mirollo (1991).** Formulated the continuum-limit PDE cleanly and linearised it about the uniform incoherent state $\rho_0 = 1/(2\pi)$. The resulting linear operator has a purely imaginary continuous spectrum and an isolated discrete eigenvalue that crosses into the right half plane exactly at $K = K_c$. Surprising upshot: **the incoherent state is never linearly stable for $K < K_c$** — only neutrally stable — yet numerics show $r(t)$ decays exponentially.
- **Strogatz–Mirollo–Matthews (1992).** Resolved the apparent paradox: the observed exponential decay is [[landau-damping]], the same mechanism Landau identified for the Vlasov equation in 1946. The decay rate is given by the analytic continuation of the discrete eigenvalue formula into the left half plane and is not a spectral eigenvalue of the original operator at all. For the Lorentzian, the explicit decay rate is $\lambda = K/2 - \gamma$.
- **Crawford (1994, 1995).** Imported center-manifold reduction and equivariant bifurcation theory from the Vlasov-equation stability literature and produced the first rigorous weakly-nonlinear stability analysis of the partially-synchronized branch near onset, in the presence of weak noise. He also showed that the square-root scaling $r \sim \sqrt{K - K_c}$ is **nongeneric** — for general periodic coupling functions with a nonzero second harmonic, Daido's $\beta = 1$ scaling holds instead, and the amplitude equations themselves are singular. The pure Kuramoto case is the accident of a missing $f_2$.

## Open questions

The 1975 derivation, and the modern self-consistency extension to general symmetric unimodal $g$, rest on ansatz-level reasoning about the relevant steady states. Rigorous versions remain only partially available:

- [[kuramoto-stability-problem]] — is the partially-synchronized branch linearly stable along its entire length, and globally nonlinearly attracting? Crawford resolved the near-onset case with noise; the rest is open.
- [[kuramoto-finite-n-convergence]] — does the finite-$N$ Kuramoto ODE system converge rigorously to the continuum-limit PDE as $N \to \infty$? Raised by Kopell in 1986; no rigorous convergence results as of the most recent source in this wiki.

Both are open problems with direct cross-links to plasma-physics analogues through [[landau-damping]] and [[kinetic-formulation]].
