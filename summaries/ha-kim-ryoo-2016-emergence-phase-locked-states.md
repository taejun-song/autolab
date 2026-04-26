---
type: source-summary
title: "Ha, Kim, Ryoo (2016) — Emergence of Phase-Locked States for the Kuramoto Model in a Large Coupling Regime"
created: 2026-04-14
updated: 2026-04-14
sources: []
tags: [dynamical-systems, synchronization, statistical-physics, mathematical-biology]
aliases: ["Ha-Kim-Ryoo 2016", "HKR 2016", "emergence of phase-locked states for Kuramoto", "Kuramoto generic initial data theorem"]
source_file: "../raw/papers/CMS-2016-0014-0004-a010 (2).pdf"
source_kind: pdf
source_date: 2015-09-05
---

# Ha, Kim, Ryoo (2016) — Emergence of Phase-Locked States for the Kuramoto Model in a Large Coupling Regime

A 19-page paper by Seung-Yeal Ha, Hwa Kil Kim, and Sang Woo Ryoo proving the complete-synchronization theorem for the finite-dimensional Kuramoto model from generic initial configurations — configurations that need not lie in a half-circle — in the large-coupling regime. This is the primary source for the theorem that [[ha-ko-park-zhang-2016-collective-synchronization]] cites as Theorem 4.2.

## Bibliographic details

- **Authors:** Seung-Yeal Ha (Seoul National University + Korea Institute for Advanced Study), Hwa Kil Kim (Seoul National University), Sang Woo Ryoo (Seoul National University).
- **Venue:** *Communications in Mathematical Sciences* **14** (2016), no. 4, 1073–1091. Published by International Press. Communicated by Shi Jin.
- **Submission timeline:** Received April 23, 2015; accepted (in revised form) September 5, 2015. Used `source_date: 2015-09-05` as the acceptance date — the most specific moment the manuscript content was frozen.
- **Length:** 19 pages (pages 1073–1091 of the CMS issue).
- **Pages read:** all 19, in two chunks (1–10, 11–19).
- **MSC:** 15B48, 92D25.

## What the paper does

The paper proves the following theorem about the finite-dimensional [[kuramoto-model]]:

**Theorem 1.1.** Suppose the initial configuration $\Theta^0$ and natural frequencies $\Omega_i$ satisfy $\sum_j \Omega_j = 0$, $\theta_{j0} \in [-\pi, \pi)$, $r_0 = |N^{-1}\sum_j e^{i\theta_{j0}}| > 0$, $\theta_{j0} \neq \theta_{k0}$ for $j \neq k$, and $\max_j |\Omega_j| < \infty$. Then there exists $K_\infty > 0$ such that for $K \geq K_\infty$ the solution $\Theta(t)$ converges in $\ell^\infty$ to a phase-locked state $\Theta^\infty$.

Prior complete-synchronization results (Choi–Ha–Jung–Kim 2012, Ha–Kim–Park 2015, Dörfler–Bullo 2011, Chopra–Spong 2009) all restricted the initial configuration to $D(\Theta^0) < \pi + \varepsilon$ with $\varepsilon \ll 1$ — i.e. essentially the half-circle confined case. This paper removes that restriction entirely, allowing initial configurations scattered anywhere on the unit circle, at the cost of driving $K$ sufficiently large. The only exclusion is the measure-zero set $r_0 = 0$ (which contains splay states and other balanced configurations).

## Three-ingredient proof strategy

The paper's §4.2 structures the proof into three combined ingredients, with a scaling reduction $\tau = Kt$, $\tilde{\Omega}_j = \Omega_j/K$ to reduce large-$K$ to unit-coupling with small frequencies.

**Ingredient 1 — Bipolar dichotomy for identical oscillators (§3).** For identical oscillators ($\Omega_j \equiv 0$) with $r_0 > 0$ and distinct initial phases, the asymptotic state is either complete phase synchronization or a bipolar configuration in which some oscillators collapse onto one phase and others onto the antipodal phase (Dong–Xue 2013, Ha–Kim–Park 2015, their Proposition 3.2). Ha–Kim–Ryoo refines this:

- **Lemma 3.3**: The "bipolar set" $\mathcal{I}_b = \{j : \lim |\theta_j - \phi| = \pi\}$ has at most one element. The proof shows that if two oscillators were heading toward the antipode, their difference would grow exponentially and contradict the finite phase-diameter assumption.
- **Lemma 3.4**: The "synchronous set" $\mathcal{I}_s$ (consequently with at least $N - 1$ elements) contracts to phase synchronization exponentially: $D(\Theta_s(t)) \leq e^{-K\lambda(t - T_2)}D(\Theta_s(T_2))$ for an explicit $\lambda = ((N-1)(1-\delta) - 1)/N > 0$ when $N \geq 3$.

**Ingredient 2 — Finite-time continuity between identical and non-identical systems (Lemma 4.2).** Let $\Theta^I$ and $\Theta^{NI}$ be solutions of the identical and non-identical Kuramoto systems with the same initial data. A Gronwall estimate gives

$$||\Theta^{NI}(t) - \Theta^I(t)||_\infty \;\leq\; \frac{||\Omega||_\infty}{2K}\left(e^{2Kt} - 1\right), \qquad t > 0.$$

This blows up exponentially in $t$, but on a fixed window $[0, T]$ and for sufficiently small $||\Omega||_\infty$, the non-identical solution stays arbitrarily close to its identical counterpart — enough time for the bipolar dichotomy from Ingredient 1 to drive the non-identical system into a configuration where $N - 1$ oscillators lie in a small arc.

**Ingredient 3 — Strong-black-hole confinement (Proposition 4.1).** Once $n_0 = N - 1$ oscillators are trapped inside an arc of length $\ell$, the quantitative coupling condition

$$K \;>\; \frac{D(\Omega)}{\frac{n_0}{N}\sin\ell - \frac{2(N - n_0)}{N}\sin\frac{\ell}{2}}$$

guarantees that those oscillators stay confined to the arc for all time, while the lone remaining oscillator's phase is bounded within a $4\pi$-neighbourhood of the arc. This gives uniform boundedness of the phase diameter, which by the Kuramoto gradient-flow dichotomy (Theorem 2.1, due to van Hemmen–Wreszinski 1993) forces convergence to a phase-locked state.

## $N = 2$ base case: the Adler equation

Before the three-ingredient argument, the paper handles the two-oscillator base case independently via the Adler equation $\dot{\theta} = \Omega - K\sin\theta$, with $\theta = \theta_2 - \theta_1$ and $\Omega = \Omega_2 - \Omega_1$. For $K > |\Omega|$, this scalar ODE has a stable equilibrium $\theta_s^1 \in (0, \pi/2)$ and an unstable one $\theta_u^1 \in (\pi/2, \pi)$, and Lemma 2.5 shows every initial datum outside $\{\theta_u^1\}$ (and its $2\pi$-translates) converges to $\theta_s^1$. This is the explicit, fully-solvable instance of the large-coupling dominance picture.

## Why the wiki ingests this primary source

The theorem itself was already present in the wiki via [[ha-ko-park-zhang-2016-collective-synchronization]], which cites this paper (as their reference [40], "to appear") and summarises the result in a single paragraph. Ingesting the primary source adds three things beyond the survey's condensed treatment:

1. **Lemma 4.2's explicit finite-time Gronwall bound.** The survey mentions a "finite-time-interval continuity estimate" as the fourth ingredient of the proof but does not give its form. The primary source states it as $||\Theta^{NI} - \Theta^I||_\infty \leq (||\Omega||_\infty / (2K))(e^{2Kt} - 1)$ — a quantitative bound that makes the "finite time" idea precise. Without it, the survey's narrative is not reproducible.
2. **The Adler-equation base case (Lemma 2.5).** The survey omits the $N = 2$ analysis entirely; the primary source treats it with explicit formulas for the stable equilibrium $\theta_s^1$ and the basin-of-attraction decomposition. This is the simplest instance of the complete-synchronization phenomenon and is missing from any other wiki source.
3. **Explicit $K$-threshold formula in Proposition 4.1.** The quantitative black-hole-confinement threshold $K > D(\Omega) / (\frac{n_0}{N}\sin\ell - \frac{2(N - n_0)}{N}\sin(\ell/2))$ is stated as an inequality in the primary source. The survey paraphrases it as "sufficient coupling" without the formula.

## What the paper does not address

- **Optimal coupling threshold.** The proof gives a threshold $K_\infty$ but no attempt to optimise it. The authors note in §5 that optimisation is deferred to ongoing work ([16] in preparation at the time).
- **Uniqueness of the limit.** Theorem 1.1 is an existence statement. Remark 1.1 explicitly notes that phase-locked states are unique up to phase-shift only in the half-circle regime (Choi–Ha–Jung–Kim 2012, [3]), and in general the counting result of Verwoerd–Mason and Ha–Kim–Ryoo [41] gives up to $2^N$ distinct phase-locked states for large $K$ (see [[phase-locked-state]]).
- **Stability of the limit.** Whether the phase-locked limit $\Theta^\infty$ is linearly or orbitally stable is not addressed. This question is independent and is the subject of Mirollo–Strogatz [21, 22] and related work referenced in [[kuramoto-stability-problem]].
- **Propagation of chaos / $N \to \infty$ limit.** Everything is at fixed finite $N$. The relationship to the [[kuramoto-finite-n-convergence|finite-$N$ convergence problem]] and the [[kuramoto-sakaguchi-equation|Kuramoto–Sakaguchi kinetic equation]] is not treated.

## Notable quotes

> Kuramoto oscillators can be visualized as point rotors moving on the unit circle. In numerical simulations, it has been observed that the relative phase velocities (frequencies) of an ensemble of Kuramoto oscillators tend to zero, regardless of initial configuration, so that the ensemble of rotors behave like a train on the unit circle (the so-called emergence of entrainment). However, such numerical results have not been confirmed in full generality by rigorous mathematical arguments, although there are several partial results available in the literature.
> — §5 Conclusion, motivating the paper.

> In this paper, we have only scratched the surface, basically confirming that the complete synchronization results given by numerical simulations are rigorous in a large coupling regime.
> — §5, the authors' own honest framing.

## Key references cited

Most cited references overlap with those already in the wiki via earlier ingests; the Adler-equation analysis uses Choi–Ha–Jung–Kim [5] for the explicit formulas. Two references worth flagging:

- **[16] Ha, S.-Y., Kim, H. K., Ryoo, S. W.** "Finite collisions and emergence of phase locked states for the Kuramoto model" (in preparation at the time). — Announced follow-up that optimises the coupling threshold and handles "collision" events more carefully. Not yet in the wiki.
- **[17] Ha, S.-Y., Li, Z., and Xue, X.** "Formation of phase-locked states in a population of locally interacting Kuramoto oscillators." *J. Diff. Eqns.* **255** (2013), 3053–3070. — Network / local interaction extension of the complete-synchronization question.
