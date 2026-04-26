---
type: concept
title: "Synchronization"
created: 2026-04-14
updated: 2026-04-14
sources:
  - "[[kuramoto-1975-self-entrainment]]"
  - "[[strogatz-2000-from-kuramoto-to-crawford]]"
  - "[[ha-ko-park-zhang-2016-collective-synchronization]]"
tags: [dynamical-systems, synchronization, statistical-physics, mathematical-biology]
aliases: ["self-entrainment", "mutual synchronization", "phase locking", "frequency locking"]
---

# Synchronization

Synchronization is the spontaneous emergence of collective rhythmic order in a population of self-sustained oscillators with differing native frequencies, arising as a phase transition once pairwise coupling exceeds a threshold.

## Setting

The canonical setting is a population of $N$ limit-cycle oscillators, each with its own native frequency $\omega_s$ drawn from a distribution $g(\omega)$, coupled pairwise. Below a critical coupling strength the population remains incoherent — each oscillator runs near its own native frequency. Above the threshold, a macroscopic fraction of the oscillators collapses onto a common rotating frequency, while the rest run at shifted, non-locked frequencies and form a continuous background in the effective-frequency spectrum.

## Why it is a phase transition

The transition is sharp in the thermodynamic limit $N \to \infty$: the [[order-parameter]] — typically the fraction of locked oscillators, or the magnitude of the complex mean field — is identically zero for coupling below threshold and rises continuously from zero above it. The mathematical handle that makes this tractable is [[mean-field-coupling]]: replacing the pairwise sum by a self-consistent mean field so each oscillator sees only an average drive.

[[kuramoto-1975-self-entrainment]] gives the first exactly-soluble instance of this transition in the [[kuramoto-model]], for a Lorentzian native-frequency distribution, with a closed-form threshold and order parameter.

## Historical lineage

- **Huygens (1665).** The first recorded observation: two pendulum clocks mounted on a common beam converge to antiphase lockstep.
- **Wiener (1948).** In *Cybernetics* and *Nonlinear Problems in Random Theory*, Wiener speculates that the α-rhythm of the human EEG reflects a synchronized ensemble of neural oscillators and attempts a Fourier-integral analysis. [[strogatz-2000-from-kuramoto-to-crawford]] reports that Wiener's specific mathematical approach "has turned out to be a dead end," though the underlying picture of collective neural synchronization has proven essentially correct.
- **Winfree (1967).** Proposes synchronization as a phase transition phenomenologically, introduces the crucial two-timescale separation (fast relaxation to limit cycles, slow phase evolution under coupling), and writes the first phase-reduced coupled-oscillator model,
$$
\dot{\theta}_i \;=\; \omega_i + \left(\sum_{j=1}^{N} X(\theta_j)\right) Z(\theta_i),
$$
where $X$ measures each oscillator's influence on the collective rhythm and $Z$ measures sensitivity. Winfree's simulations showed a threshold separating incoherence from synchrony.
- **Kuramoto (1975).** Puts Winfree's intuition on firmer mathematical ground by replacing the pairwise product $X(\theta_j) Z(\theta_i)$ with a pure sinusoidal phase-difference interaction, and solves the resulting model exactly in the Lorentzian case. See [[kuramoto-1975-self-entrainment]] and [[kuramoto-model]]. Kuramoto's own description credits Prigogine's concept of "time order" in nonequilibrium open systems as finding its finest example in this transition phenomenon.
- **Strogatz–Mirollo / Crawford / etc. (1991–1999).** Recast the problem in the [[kinetic-formulation|continuum-limit PDE]] setting, exposed [[landau-damping]] as the relaxation mechanism below threshold, and produced the first rigorous weakly-nonlinear stability results via center-manifold reduction. See [[strogatz-2000-from-kuramoto-to-crawford]].

## Where it appears

[[strogatz-2000-from-kuramoto-to-crawford]] catalogues a striking cross-disciplinary list of systems where synchronization of coupled oscillators is observed and has been modelled with Kuramoto-like equations:

- **Biology.** Networks of pacemaker cells in the heart, circadian pacemaker cells of the mammalian suprachiasmatic nucleus, metabolic synchrony in yeast cell suspensions, congregations of synchronously flashing fireflies, crickets that chirp in unison.
- **Physics and engineering.** Arrays of lasers, arrays of microwave oscillators, superconducting Josephson-junction arrays, power grids.
- **Neuroscience.** Collective rhythms in large neural ensembles giving rise to EEG features such as the α-rhythm — the original motivation Wiener articulated in *Cybernetics*.

In every case the governing mathematics shares the same structure: coupled phase equations with distributed intrinsic frequencies, a coupling-strength control parameter, and a sharp threshold separating incoherence from collective oscillation. This is why the [[kuramoto-model]] — a minimal model that retains exactly this structure — is used as the universal testbed.

## Model taxonomy

[[ha-ko-park-zhang-2016-collective-synchronization]] organises the subject by what flows through the coupling. Restricted to the classical models that this wiki tracks:

| Class | Coupling mechanism | Representative models |
|---|---|---|
| **Pulse-coupled** | Instantaneous threshold-triggered kicks | [[peskin-model]] (cardiac pacemaker cells, integrate-and-fire) |
| **Phase-coupled** | Continuous forcing on a scalar phase | [[winfree-model]], [[kuramoto-model]] |

The phase-coupled models have scalar state $\theta_j \in S^1$. The [[kuramoto-model]] sits at the centre of the classification as the "backbone" — Winfree reduces to Kuramoto in the weak-coupling, close-to-common-frequency regime via averaging over one period. The pulse-coupled Peskin model stands off to one side: it admits a *finite-time* synchronization theorem (Mirollo–Strogatz 1990) with no analogue in any phase-coupled model.

The Ha–Ko–Park–Zhang survey also discusses a third class of *state-coupled* models (Lohe, Schrödinger–Lohe) in which the oscillators carry unitary matrices or wave functions rather than scalar phases, giving a non-abelian generalization of Kuramoto. This wiki scopes out that quantum-synchronization line and keeps the focus on the classical Peskin / Winfree / Kuramoto triple.
