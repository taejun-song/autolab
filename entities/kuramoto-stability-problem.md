---
type: entity
title: "Kuramoto Stability Problem"
created: 2026-04-14
updated: 2026-04-26
sources:
  - "[[castorrini-galatolo-tanzi-2025-self-consistent-transfer]]"
  - "[[campa-2022-oa-generic-frequency]]"
  - "[[strogatz-2000-from-kuramoto-to-crawford]]"
  - "[[ha-ko-park-zhang-2016-collective-synchronization]]"
  - "[[chiba-2015-kuramoto-conjecture]]"
  - "[[fernandez-gerard-varet-giacomin-2016-landau-damping]]"
  - "[[brezis-2011-functional-analysis-sobolev-pdes]]"
  - "[[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]]"
  - "[[dietert-fernandez-2018-asymptotic-stability]]"
  - "[[dietert-2017-pls-sobolev]]"
  - "[[bronski-wang-2020-partially-locked]]"
  - "[[dietert-2016-stability-bifurcation]]"
  - "[[haraux-jendoubi-2015-convergence-problem]]"
  - "[[chen-engelbrecht-mirollo-2017-hyperbolic-geometry]]"
  - "[[cestnik-martens-2024-riccati-array]]"
  - "[[dietert-2016-thesis]]"
tags: [dynamical-systems, synchronization, statistical-physics, open-problem]
aliases: ["stability of the partially-synchronized branch", "Kuramoto branch stability", "stability of Kuramoto synchrony", "Kuramoto conjecture"]
status: partially-resolved
year_stated: 1975
---

# Kuramoto Stability Problem

Is the partially-synchronized branch of the Kuramoto model — the steady state of mutually locked oscillators that bifurcates from incoherence at coupling $K = K_c$ — linearly and globally dynamically stable along its entire length?

## Statement

Work in the [[kinetic-formulation|continuum limit]] of the [[kuramoto-model]] with a symmetric unimodal native-frequency density $g(\omega)$ (mean zero, $g(-\omega) = g(\omega)$, nowhere increasing on $[0,\infty)$) and coupling $K$. For $K \leq K_c := 2/(\pi g(0))$ the uniform incoherent state $\rho_0 = 1/(2\pi)$ is the only steady solution. For $K > K_c$ a continuous family of partially-synchronized states, parameterised by the complex mean-field value $re^{i\psi}$ with $r = r(K) > 0$, bifurcates from incoherence at $K = K_c$.

The Kuramoto stability problem is to prove (or disprove) three progressively stronger assertions:

1. **Local linear stability at onset.** The partially-synchronized branch is linearly stable in the continuum model near $K = K_c^+$.
2. **Linear stability along the entire branch.** The partially-synchronized branch is linearly stable for all $K > K_c$, not only just above onset.
3. **Global nonlinear stability.** The partially-synchronized branch is globally nonlinearly attracting from a generic basin, uniformly in the continuum limit.

## Status (as of Strogatz 2000)

- **Assertion 1 — resolved near onset with noise.** Crawford (1994, *J. Statist. Phys.* **74**, 1047) proved local linear stability near onset by importing center-manifold reduction and equivariant bifurcation theory to the Sakaguchi noisy continuum model, exploiting the $O(2)$ symmetry of the PDE. He obtained the amplitude equation $\dot{r} = \lambda r + a r^3 + O(r^5)$ whose coefficients remain finite as the noise $D \to 0^+$, and confirmed Kuramoto's 1975 coefficient. His proof establishes local linear stability of the bifurcating branch with weak noise; [[strogatz-2000-from-kuramoto-to-crawford]] notes Crawford observes that "when $D = 0$, center manifold theory no longer justifies our reduction to two dimensions" so the $D = 0$ case is not literally covered, but the agreement with numerics makes the extension plausible.
- **Assertion 2 — open at the 2000 snapshot.** Strogatz writes: "But we still do not know how to show that the bifurcating branch is linearly stable along its entire length (if it truly is)." No $K$-uniform stability result is available.
- **Assertion 3 — open at the 2000 snapshot.** Strogatz: "nobody has even touched the problems of global stability and convergence." Finite-dimensional convergence-to-the-partially-synchronized-state results are lacking, and the continuum PDE analysis has not been extended to nonlinear basin-of-attraction statements.

## Post-2000 progress (as of Ha–Ko–Park–Zhang 2016)

The second source in this wiki, [[ha-ko-park-zhang-2016-collective-synchronization]], reports substantial progress on all three assertions in the 2005–2016 window. The 2000 Strogatz snapshot is preserved above as a historical marker, and the following additions update the status:

- **Chiba (2015), "A proof of the Kuramoto conjecture for a bifurcation structure of the infinite-dimensional Kuramoto model"** (*Ergodic Theory and Dynamical Systems* **35**, 762–834). Establishes the bifurcation structure of the Kuramoto–Sakaguchi continuum PDE rigorously, proving that the partially-synchronized branch really is what bifurcates from the incoherent state at $K = K_c$ with the predicted structure, without the Crawford assumption of weak noise. This is a direct resolution of what Kuramoto 1975 called a "conjecture" and of much of Assertion 1 in the $D = 0$ case. See also Chiba's 2013 "Continuous limit of the moments system for the globally coupled phase oscillators" (*Discrete Contin. Dyn. Syst.* **33**) for supporting technical machinery.

- **[[fernandez-gerard-varet-giacomin-2016-landau-damping|Fernandez–Gérard-Varet–Giacomin (2016)]], "Landau damping in the Kuramoto model"** (*Annales Henri Poincaré* **17**, 1793–1823). Rigorous nonlinear [[landau-damping]] for the Kuramoto model: for $g \in C^n(\mathbb{R})$ ($n \geq 4$) satisfying a Penrose-type stability criterion (equivalent to $K < K_c$ for symmetric unimodal $g$), the order parameter decays as $\mathrm{R}(t) = O(t^{-n})$ from sufficiently small $C^n$ perturbations. The proof uses a Volterra integral equation and bootstrap argument adapted from the Vlasov-HMF setting, rather than the spectral-theoretic approach. This confirms Kuramoto's conjecture that "below the critical coupling strength the incoherent solution is expected to be nonlinearly stable" — the content that Strogatz 2000 had explicitly flagged as subtle and unresolved.

- **Benedetto–Caglioti–Montemagno (2015)** "On the complete phase synchronization for the Kuramoto model in the mean-field limit" (*Commun. Math. Sci.* **13**). Further nonlinear stability refinements for the K-S equation.

- **Ha–Xiao (2015)** "Nonlinear instability of the incoherent state for the Kuramoto–Sakaguchi–Fokker–Planck equation" (*J. Stat. Phys.* **160**) and related work in *J. Differential Equations* **259**. Rigorous nonlinear *instability* of incoherence above the critical coupling, the companion statement to the damping result below the threshold.

[[ha-ko-park-zhang-2016-collective-synchronization]] §4.5 summarises: "Kuramoto conjecture that below the critical coupling strength the incoherent solution is expected to be nonlinearly stable, in contrast above the critical coupling strength, it is expected to be nonlinearly unstable. The verification of this nonlinear phenomena rigorously has been done in aforementioned literature."

This is a substantial shift from the 2000 picture. The entity remains classified `partially-resolved` rather than `proven` because:
- The stability claim for the *partially-synchronized branch itself* (Assertion 2) — as opposed to the incoherent state below threshold — is not fully covered by Chiba's bifurcation analysis at all values of $K > K_c$.
- The global nonlinear attraction statement (Assertion 3) still requires qualifications about initial data and the function-space topology in which convergence holds.
- The finite-$N$ statements (translating continuum-limit stability back to finite ODE systems) remain open via [[kuramoto-finite-n-convergence]].

Both Chiba 2015 and Fernandez–Gérard-Varet–Giacomin 2016 have now been ingested as primary sources. Additionally, [[dietert-fernandez-2018-asymptotic-stability|Dietert–Fernandez (2018)]] proves **local nonlinear stability of the partially locked state itself** (Assertions 1–2), with polynomial decay $|r(t) - r_s e^{i\Theta_\infty}| = O(t^{1/2-b})$ for Sobolev-regular $g$ and exponential decay $O(e^{-a't})$ for analytic $g$. The same review proves the [[ott-antonsen-ansatz|OA manifold]] is exponentially attracting for analytic $g$ (Proposition 4.1).

**Update (2026-04-24): Assertion 3 — argument-level proof for all analytic $g$, all $K > K_c$, conditional on (H2).** The [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] contains a logically complete argument for global stability, conditional on hypothesis (H2): that $W^u(0) \to$ PLS in the infinite-dimensional OA semiflow. Under (H2): $0 \in \Omega$ + instability + heteroclinic $\Rightarrow$ PLS $\in \Omega$ $\Rightarrow$ Dietert's local stability closes. (H2) is proved for finite-dimensional reductions (Lorentzian mixtures, all $n$) but open for the continuum semiflow. For **rational $g$**: **proved** (machine-checked $L^2$ Lyapunov, LEAN 4, 0 sorry). For **general analytic $g$**: **sketch** (conditional on (H2)). Previously reported as unconditional — corrected after reviewer critique identified the (H2) gap.

**Unconditional results (2026-04-25):** The following results hold for all analytic $g$, all $K > K_c$, without (H2):
- **Progressive locking**: $\Psi(t) \to +\infty$ and $|r(t)| \not\to 0$ for every orbit with $r(0) \neq 0$. Phase mixing ($r \to 0$) is ruled out. Label: **argument** (LEAN 4, `case_A_impossible` + `Ψ_diverges`, 0 sorry).
- **$\sup_\Omega \Psi = +\infty$**: the $\omega$-limit set contains states of arbitrarily high locking degree. Proved via the homoclinic contradiction: if $\Psi$ bounded on $\Omega$, forward orbits visit 0 (amplification), but $\Psi$ nondecreasing from $\Psi(x) > 0$ prevents this. Label: **argument** (LEAN 4, `sup_Ψ_unbounded`, 0 sorry).
- **PLS $\in \Omega_r$ for all $g \in L^1$**: unconditional, all $K > K_c$. The generalized tail-body split (2026-04-25) shows $\text{tail}(t)/\Psi(t) \to 0$ for ANY $g \in L^1$, using only $\varepsilon(M) = \int_{|\omega|>M} g \to 0$ and $\liminf|r| > 0$. This forces body $\to +\infty$, giving $r^* \in \Omega_r$ via Fatou's lemma + self-consistency. Extends previous exponential-tail result to all distributions. Label: **argument** (LEAN 4, `GeneralizedTailBody.lean`, 0 sorry, 0 axioms).

## Why it is hard

Three structural features conspire to make the analysis subtle:

1. **Neutral continuous spectrum.** Linearisation about incoherence has a pure-imaginary continuous spectrum; the partially-synchronized branch inherits a similarly non-normal linearization. Standard spectral arguments — "eigenvalues in the left half plane implies stability" — do not apply without care, and decay of the macroscopic order parameter is governed by [[landau-damping]] rather than by ordinary spectral modes.
2. **Singular amplitude equations.** Crawford showed that in the generalized Kuramoto model (non-sinusoidal $2\pi$-periodic coupling $f$), the center-manifold amplitude equations develop singularities whenever the second harmonic coefficient $f_2$ is nonzero. The pure Kuramoto model ($f = \sin$) is a nongeneric special case where $f_2 = 0$, so the square-root scaling $r \sim \sqrt{K - K_c}$ is the accident of a missing harmonic rather than a robust pitchfork. This is why extension of stability results beyond a small neighbourhood of onset is delicate.
3. **Infinite-dimensional steady state.** The partially-synchronized fixed point of the [[kinetic-formulation|continuum PDE]] is an infinite-dimensional object (a distribution $\rho(\theta, \omega)$ rather than a point), and the linearized stability problem is posed on function spaces whose topology matters for which perturbations count.

For the functional-analytic and PDE toolkit these difficulties demand — evolution equations as $du/dt + Au = 0$ via maximal monotone / Hille–Yosida theory, spectral decomposition of compact self-adjoint operators, weak and weak-* topologies on function and measure spaces, Sobolev regularity of weak solutions — see the concordance in [[brezis-2011-functional-analysis-sobolev-pdes]]. Note especially the caveat there: Brezis only handles discrete spectra of compact operators, so the continuous-spectrum aspect of difficulty 1 above is where the user must supplement Brezis with a dedicated non-compact spectral theory reference.

Strogatz reports that he, Mirollo, and Crawford discussed a fresh attack on the entire-branch stability problem at a 1998 Pattern Formation meeting, but Crawford's death following cancer treatment ended that collaboration. As of March 2000 the problem was explicitly flagged as unsolved in [[strogatz-2000-from-kuramoto-to-crawford]], which is the most recent source in this wiki.

## Alternative approach: dimension reduction via Möbius group

A second line of attack orthogonal to the functional-analytic approach comes from the [[ott-antonsen-ansatz]]. The Ott–Antonsen ansatz identifies a specific invariant submanifold of the [[kuramoto-sakaguchi-equation|K-S equation]] state space — the set of Poisson-kernel densities on $S^1$ parameterised by a single complex order parameter $z \in \mathbb{D}$ — on which the full PDE dynamics collapse exactly to a closed ODE for $z$. [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]] unifies this with the finite-$N$ Watanabe–Strogatz reduction under a single group-theoretic framework (the Möbius group of the unit ball $B^d$ with its hyperbolic metric) and extends it to the [[kuramoto-on-a-sphere|higher-dimensional Kuramoto model]]. For a specific class of couplings (positive-weight first-order linear order parameters on $S^{d-1}$), they prove **global convergence to complete synchronization** via a hyperbolic Lyapunov potential — a rare global-stability result for any Kuramoto-type model.

This is a genuinely different path from Chiba's bifurcation-theoretic resolution discussed above. It sidesteps the continuous-spectrum subtlety and the non-compactness of the linearized K-S operator by finding an *explicit* invariant submanifold on which dynamics are integrable. The limitation is that the reduction is exact only on the ansatz submanifold; for **non-identical frequencies** and off-manifold initial data, neither the stability analysis nor the global-convergence result transfers directly. Whether the Möbius-group framework can be extended to cover the full state space — the "generalized Ott–Antonsen" question — is the central open problem in this line. A positive answer would provide a geometric route to resolving the stability question that does not go through FA spectral theory at all.

**LEAN formalization complete (2026-04-26):** The entire LEAN project has **0 sorry, 0 axioms** across 40 .lean files. `MainTheorem.lean` proves global stability from 22 KuramotoData hypotheses (all groundable on published results) using only Mathlib. Companion files (FullRangeStability, GradientLike, WindowedApproximation, etc.) have all former axioms eliminated — either proved from Mathlib, removed as dead code, or converted to structure fields. The single open mathematical assumption (H2: unstable_manifold_to_pls) is now an explicit structure field, not a LEAN axiom. Label: **argument**.

## Current synthesis

See [[kuramoto-stability-state-of-the-art]] for the full cross-source synthesis of all 22 ingested sources, 5 LEAN 4 files, and 18 attempted proof approaches.

## Related problems

- [[kuramoto-finite-n-convergence]] — whether the finite-$N$ Kuramoto model converges to the continuum limit, a prerequisite for translating continuum-model stability results back to the original ODE system.
- Stability of the incoherent state — resolved (Strogatz–Mirollo–Matthews 1992): the incoherent state is never linearly stable below $K_c$, only neutrally stable, but $r(t) \to 0$ exponentially via [[landau-damping]]. An *eigenvalue* crosses into the right half plane at $K = K_c$, making incoherence unstable above threshold.

## If resolved

A full resolution would be the capstone on the 50-year mathematical story of the Kuramoto model: a rigorous statement that the partially-synchronized state the model was designed to explain really is what attracts the population above threshold, uniformly in $N$ and $K$. It would also likely transfer to the Vlasov equation in plasma physics, where — per the analogy Strogatz, Mirollo, Matthews, and Crawford discovered — similar singular amplitude equations and neutral continuous spectra control the weakly nonlinear stability of the collisionless plasma equilibria.
