---
type: source-summary
title: "Strogatz (2000) — From Kuramoto to Crawford: Exploring the Onset of Synchronization in Populations of Coupled Oscillators"
created: 2026-04-14
updated: 2026-04-14
sources: []
tags: [dynamical-systems, synchronization, statistical-physics, plasma-physics, kinetic-theory, mathematical-biology]
aliases: ["Strogatz 2000", "From Kuramoto to Crawford"]
source_file: "../raw/papers/1-s2.0-S0167278900000944-main.pdf"
source_kind: pdf
source_date: 2000-03-01
---

# Strogatz (2000) — From Kuramoto to Crawford: Exploring the Onset of Synchronization in Populations of Coupled Oscillators

A 20-page retrospective by Steven Strogatz covering 25 years of mathematical work on the [[kuramoto-model]], from Kuramoto's 1975 self-consistency calculation through the 1990s papers of J. D. Crawford that imported plasma-physics techniques to resolve the weakly-nonlinear stability problem, narrating both the technical progress and the human story behind it.

## Bibliographic details

- **Author:** Steven H. Strogatz (Center for Applied Mathematics and Department of Theoretical and Applied Mechanics, Cornell University).
- **Venue:** *Physica D* **143** (2000), 1–20. PII: S0167-2789(00)00094-4.
- **Source date:** The paper records that "as of March 2000" no rigorous finite-$N$ convergence results existed, which fixes the manuscript freeze at that month. Used as `source_date: 2000-03-01`.
- **Occasion:** Written as a tribute to J. D. Crawford, who had recently died after treatment for cancer. The closing section recounts Strogatz's last meeting with Crawford in spring 1998 at the IMA Pattern Formation workshop.
- **Pages read:** All 20 (1–20), in three chunks (1–5, 6–13, 14–20).

## What the paper does

The paper is simultaneously an expository introduction to the [[kuramoto-model]], a technical review of the 25-year analysis program, a memorial to Crawford, and an explicit catalogue of what was still unsolved as of 2000. The technical backbone is a linear and weakly nonlinear stability analysis of the continuum Kuramoto model, culminating in the Crawford amplitude equations. The non-technical framing threads a narrative through Kuramoto, Winfree, Wiener, Kopell, Mirollo, Matthews, Rowlands, Sakaguchi, Daido, and Crawford — each contributing a piece to what Strogatz calls "a lovely winding road, with excursions through mathematical biology, statistical physics, kinetic theory, bifurcation theory, and plasma physics."

## Bullet distillation

- **Kuramoto model setup (§3.1).** Population of $N$ phase oscillators with distributed native frequencies, all-to-all sinusoidal coupling: $\dot{\theta}_i = \omega_i + (K/N)\sum_j \sin(\theta_j - \theta_i)$. Assumes $g(\omega)$ symmetric, unimodal, nowhere increasing on $[0, \infty)$. After shifting to a rotating frame at the mean frequency, $g$ becomes even.
- **Complex mean field (§3.2).** $re^{i\psi} = (1/N)\sum_j e^{i\theta_j}$, interpreted as the centroid of phases on the unit circle. The governing equation rewrites as $\dot{\theta}_i = \omega_i + Kr\sin(\psi - \theta_i)$, exposing the positive-feedback mechanism of synchronization: higher $r$ amplifies effective coupling $Kr$, which recruits more oscillators. See [[order-parameter]] and [[mean-field-coupling]].
- **Numerical picture (§3.3).** For $K < K_c$, $r(t)$ decays to $O(N^{-1/2})$ jitter. For $K > K_c$, $r$ grows exponentially and saturates at $r_\infty(K) < 1$, reflecting nucleation of a locked cluster near the centre of $g(\omega)$. The tails drift. The steady-state $r_\infty$ appears to depend only on $K$, not on initial conditions.
- **Puzzles (§3.4).** Explicit list of open questions that motivate the rest of the paper: formulas for $K_c$ and $r_\infty(K)$, linear and global stability of the zero and bifurcating branches, and $N \to \infty$ convergence theorems.
- **Kuramoto's steady-state analysis (§4).** In a rotating frame where $\psi \equiv 0$, the governing equation becomes $\dot{\theta}_i = \omega_i - Kr\sin\theta_i$. Oscillators with $|\omega_i| \leq Kr$ lock at $\omega_i = Kr\sin\theta_i$; those with $|\omega_i| > Kr$ drift. Self-consistency on $r$ then determines the critical coupling $K_c = 2/(\pi g(0))$ and, near onset, the square-root scaling $r \approx \sqrt{16/(\pi K_c^3)}\sqrt{\mu/(-g''(0))}$ with $\mu = (K-K_c)/K_c$. Supercritical when $g''(0) < 0$ (generic), subcritical otherwise. For the Lorentzian $g(\omega) = \gamma/[\pi(\omega^2 + \gamma^2)]$ the integral is exact: $r = \sqrt{1 - K_c/K}$ for $K \geq K_c$.
- **Two explicit open problems (§5).**
    - **§5.1 Finite-$N$ fluctuations.** Kopell (Berkeley Bowen Lectures, 1986) emphasised that $r(t)$ is not strictly constant for any finite $N$ — at $K = 0$ it is dense in $[0, 1]$ — and asked for a rigorous convergence theorem. Daido and Kuramoto–Nishikawa did heuristic / numerical work supporting $O(N^{-1/2})$ fluctuations away from criticality, but as of March 2000 "there are no rigorous convergence results about the finite-$N$ behavior of the Kuramoto model." See [[kuramoto-finite-n-convergence]].
    - **§5.2 Stability.** Kuramoto in 1975: "Surprisingly enough, this seemingly obvious fact [that weaker coupling makes $r = 0$ stable] seems difficult to prove." Crawford solved local near-onset stability; nobody as of 2000 had handled entire-branch linear stability or global nonlinear stability. See [[kuramoto-stability-problem]].
- **Kuramoto–Nishikawa attempts (§6).** Two non-rigorous theories aimed at an evolution equation for $r(t)$ — one (1987) predicting anomalously slow $O(1/t)$ decay, one (1989) predicting standard exponential decay via a postulated memory kernel. Both ad hoc; both instructive as failed attempts.
- **Continuum limit (§7).** Strogatz and Mirollo (1991) introduced the [[kinetic-formulation|density PDE]] $\partial_t \rho = -\partial_\theta(\rho v)$ with $v = \omega + Kr\sin(\psi - \theta)$ and $re^{i\psi} = \iint e^{i\theta}\rho g \, \mathrm{d}\omega\,\mathrm{d}\theta$ — a nonlinear integro-differential equation on densities. Sakaguchi (1988) had earlier written its Fokker–Planck version with independent white-noise forcing on phases. This PDE framing is what makes existence, stability, and bifurcation questions systematically tractable.
- **Linear stability of incoherence (§8).** Perturbing $\rho_0 = 1/(2\pi)$ and writing the perturbation in the form $c(t, \omega)e^{i\theta} + \text{c.c.}$ gives a linear operator whose continuous spectrum is pure imaginary and whose discrete spectrum satisfies the dispersion relation $1 = (K/2)\int g(\omega)/(\lambda^2 + \omega^2)\,\mathrm{d}\omega$. Any eigenvalue must satisfy $\lambda \geq 0$: **no negative eigenvalues are possible**. So the incoherent state is either unstable or neutrally stable — never linearly stable. For the Lorentzian, the explicit eigenvalue is $\lambda = K/2 - \gamma$. As $K$ crosses $K_c = 2\gamma$ this eigenvalue emerges from the continuous spectrum at $\lambda = 0$ and moves into the right half plane, giving the bifurcation.
- **Landau damping (§9).** Matthews's numerics showed $r(t)$ decaying exponentially below threshold at rate exactly $|\lambda(K)|$, the analytic continuation of the growth formula into the region where it should not apply. Rowlands, present at Matthews's Warwick lecture, recognised this as [[landau-damping]] from plasma physics (Landau 1946 for the Vlasov equation). The mechanism is a pole of the analytic continuation of the resolvent into the left half plane, not a true eigenvalue. Strogatz, Mirollo, and Matthews (1992) proved it rigorously, finding the exact integral representation $R(t) = (1/(2\pi i))\int_\Gamma (c_0 g)^*(s)/(1 - (K/2)g^*(s))\, e^{st}\,\mathrm{d}s$ and reducing it, for the Lorentzian case, to $R(t) = \exp((K/2 - \gamma)t)$ exactly. For $g$ of compact support, $R(t) \to 0$ but always slower than exponential at long times; for $g$ supported on $\mathbb{R}$ with heavy tails, the asymptotics "can be much wilder."
- **Crawford on the Kuramoto model (§§10–11).** Crawford, an applied mathematician working on the Vlasov plasma equation, had independently developed center-manifold reduction techniques for systems with neutral continuous spectra. After a hamburger-joint lunch with Strogatz at Dynamics Days 1992, Crawford turned his tools on the Kuramoto model. Results:
    1. First systematic weakly-nonlinear stability analysis via center-manifold theory on Sakaguchi's $D > 0$ PDE, exploiting $O(2)$ symmetry.
    2. First rigorous derivation of the amplitude equation $\dot{r} = \lambda r + ar^3 + O(r^5)$, confirming Kuramoto's coefficient.
    3. First proof that the bifurcating branch is locally stable near onset in presence of weak noise.
    4. First use of ideas from Vlasov plasma stability on the Kuramoto model, forging the explicit link.
    5. Discovery that the Kuramoto amplitude equations have *nonsingular* coefficients even as $D \to 0^+$, in striking contrast to the Vlasov case — and an explanation: the Kuramoto model lacks a second-harmonic coupling ($f_2 = 0$ for $f = \sin$), making it a nongeneric fluke.
    6. Study of the singularity structure of amplitude equations in the generalized Kuramoto model with arbitrary $2\pi$-periodic coupling $f$, where Daido had empirically found the non-standard scaling $\|H\| \sim (K - K_c)^\beta$ with $\beta = 1$ rather than the expected $\beta = 1/2$. Crawford derived $|\alpha_\infty| \sim \sqrt{\sigma(\sigma + l^2 D)}$ for the saturated amplitude of mode $e^{il\theta}$, and traced the $\beta = 1$ scaling to the singular limit $D \to 0^+$ in this formula.
- **Epilogue.** Strogatz's last meeting with Crawford was at the IMA Pattern Formation workshop in spring 1998. Over pizza with Mirollo, they discussed a fresh attack on the entire-branch stability problem for the Kuramoto model; Crawford's death ended that plan. "It is still unsolved, 25 years after Kuramoto first posed it, but we thought we had some ideas about how to proceed, and we hoped to collaborate on it after the conference. With Crawford on our team, I bet we could have done it."

## Why this source matters

This review is the definitive mathematical retrospective on the Kuramoto model at the 25-year mark. It does four things no single earlier paper does:

1. **Canonises the modern formulation.** The complex-mean-field form $re^{i\psi}$ and the rewritten governing equation $\dot{\theta}_i = \omega_i + Kr\sin(\psi - \theta_i)$ become the standard notation after this paper, even though they predate it in scattered places.
2. **Establishes the Landau-damping bridge to plasma physics.** Before this review the Kuramoto–Vlasov analogy is folklore among a handful of specialists; after it the analogy is an official part of the subject and the tools from kinetic theory flow freely in both directions.
3. **States the open problems precisely.** The entire-branch stability of the partially-synchronized state and the rigorous finite-$N$ convergence question are explicitly declared unsolved. Later literature cites these as *the* open problems for the Kuramoto model.
4. **Tells the human story.** Strogatz's narrative — Kopell at Berkeley, the Warwick lecture where Rowlands recognised Landau damping, the Dynamics Days lunch with Crawford, the final IMA conversation — gives historical shape to what would otherwise be a collection of citations.

## What the paper does not cover

- **Network topologies.** The review is strictly all-to-all. Chimera states, network extensions, small-world and scale-free Kuramoto models, phase lag (Sakaguchi–Kuramoto), higher-harmonic coupling beyond Daido's framing — essentially any structural generalization of the model is outside the scope.
- **Applications in detail.** The biological / physical examples are listed but not developed. The paper is about the mathematical core, not the modelling.
- **Post-2000 progress.** By construction — it is a March 2000 snapshot. A modern ingest would need to supplement with post-2000 developments on the two open problems.
- **Explicit Vlasov-equation treatment.** Strogatz alludes to the Vlasov connection throughout but does not develop the plasma-physics side; readers are pointed to Crawford's earlier plasma papers for the original techniques.
- **Proofs.** This is a review, not a primary-source technical paper. Lemma-by-lemma stability proofs are cited but not presented.

## Notable quotes

> It is a lovely winding road, with excursions through mathematical biology, statistical physics, kinetic theory, bifurcation theory, and plasma physics.
> — Abstract, characterising the 25-year arc.

> There definitely was a link between Landau damping and the relaxation phenomena we were seeing. It was awe-inspiring: the same mathematics describes the violent world of plasmas and the silent, hypnotic pulsing of fireflies perched along a riverbank.
> — §9.2, on Rowlands's identification of Landau damping in the Kuramoto model at Matthews's Warwick lecture.

> But we still do not know how to show that the bifurcating branch is linearly stable along its entire length (if it truly is), and nobody has even touched the problems of global stability and convergence.
> — §6, on the state of the stability problem. The explicit open-problem statement.

> As of March 2000, there are no rigorous convergence results about the finite-$N$ behavior of the Kuramoto model.
> — §5.1, on the state of the finite-$N$ fluctuation problem.

> It is still unsolved, 25 years after Kuramoto first posed it, but we thought we had some ideas about how to proceed, and we hoped to collaborate on it after the conference. With Crawford on our team, I bet we could have done it.
> — Epilogue, on Crawford's planned but unrealised attack on the stability problem.

## Key references cited (not yet in wiki)

- [1] J. D. Crawford, *J. Statist. Phys.* **74** (1994), 1047 — first Crawford paper on coupled oscillators.
- [2] J. D. Crawford, *Phys. Rev. Lett.* **74** (1995), 4341 — amplitude equations on unstable manifolds.
- [3] J. D. Crawford, K. T. R. Davies, *Physica D* **125** (1999), 1 — rigorous derivation.
- [4] Y. Kuramoto (1975) — already ingested as [[kuramoto-1975-self-entrainment]].
- [5] Y. Kuramoto, *Chemical Oscillations, Waves, and Turbulence*, Springer, 1984 — the book-length extension of the 1975 note.
- [8, 9] Kuramoto–Nishikawa — the two heuristic stability attempts.
- [10] A. T. Winfree, *J. Theor. Biol.* **16** (1967), 15 — the phenomenological precursor.
- [27] N. Wiener, *Cybernetics*, 2nd ed., MIT Press, 1961 — the α-rhythm speculation.
- [34] S. H. Strogatz, R. E. Mirollo, *J. Statist. Phys.* **63** (1991), 613 — the continuum-limit stability paper.
- [35] H. Sakaguchi, *Progr. Theor. Phys.* **79** (1988), 39 — the noisy extension.
- [37] S. H. Strogatz, R. E. Mirollo, P. C. Matthews, *Phys. Rev. Lett.* **68** (1992), 2730 — the Landau-damping resolution.
- [47, 48] J. D. Crawford's earlier Vlasov plasma papers.
- [57–60] H. Daido papers on the order function and nongeneric scaling.

Any of these would be a natural next ingest, especially [34] (Strogatz–Mirollo 1991) and [1] (Crawford 1994).
