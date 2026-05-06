# Wiki Index

_Last regenerated: 2026-05-06 (ContinuumSolvedTailBodyV2, exp 265)_

## Recently Updated

- [[continuum-stability-debate]] — ContinuumSolvedTailBodyV2.lean (exp 265): `kuramoto_solved_continuum'` — DEFINITIVE tail-body theorem for standard continuum Kuramoto on R. RESOLVES ALL 3 REVIEWER PROBLEMS: (1) no uniform persistence (body persistence only on {γ≤M}), (2) no bounded γ (body bounded by M per truncation), (3) no c_min (body coercivity K·δ(M)·ds(M)). Takes body exp decay per M as SINGLE convergence hypothesis. Tail vanishing automatic. `body_exp_of_bounded_gamma` subsumption. 0 sorry, 0 axioms. ALL g ∈ L¹(R).
- [[continuum-stability-debate]] — KuramotoStandardContinuum.lean (exp 264): `kuramoto_solved_continuum` — DEFINITIVE theorem for standard continuum Kuramoto on ℝ. γ=|ω| unbounded, no uniform persistence, no bounded γ, no c_min. Body exp decay per truncation M. Tail-body split: integral_add_compl + Cauchy-Schwarz. Subsumption `_of_bounded`. 0 sorry, 0 axioms. ALL g ∈ L¹(ℝ).
- [[continuum-stability-debate]] — ContinuumSolvedPhysical.lean (exp 263): `kuramoto_solved_continuum'` — CLEAN theorem for standard continuum model. Resolves PROBLEMS 1-3 (no uniform persistence, no bounded γ, no c_min). Body exp decay per M. 0 sorry, 0 axioms. ALL g ∈ L¹(R).
- [[continuum-stability-debate]] — ContinuumStandardModel.lean (exp 262): `kuramoto_continuum_standard_model` — clean definitive theorem for standard continuum Kuramoto (γ unbounded). No uniform persistence, no bounded γ, no c_min. Body exp decay per M + tail vanishing. Subsumption `_of_bounded`. 0 sorry, 0 axioms. ALL g ∈ L¹(R).
- [[continuum-stability-debate]] — ContinuumKuramotoSolvedDefinitive.lean (exp 261): `kuramoto_solved_continuum_definitive` — ISS absorbing-ball theorem for standard continuum model. Takes C(M)+μ(tail)→0 (combined vanishing). Also `_gronwall` (body Gronwall → absorbing), `_exp` (body exp decay), `bounded_gamma_implies_continuum` (subsumption). 0 sorry, 0 axioms. Covers Gaussian, Student-t ν>2, compact support.
- [[continuum-stability-debate]] — Fix `kuramoto_solved_continuum` (exp 260): NEW definitive theorem for ALL g ∈ L¹(R) including Lorentzian. No γ integrability, no bounded γ, no uniform persistence, no c_min. Takes body exp decay per truncation M + tail vanishing from probability measure. `kuramoto_solved_of_bounded` proves `kuramoto_solved` is special case. 0 sorry, 0 axioms.
- [[continuum-stability-debate]] — ContinuumSolvedActual.lean: `kuramoto_actual_continuum` (0 sorry, 0 axioms) — Clean theorem for ACTUAL standard continuum model. γ=|ω| unbounded, locked+drifting oscillators. Tail-body split: body exp decay per M + tail vanishing. No bounded γ, no uniform persistence, no c_min. Also ISS version `kuramoto_actual_continuum_iss` with C(M)+μ(tail)→0.
- [[continuum-stability-debate]] — ContinuumKuramotoSolved.lean: `kuramoto_continuum_solved` (0 sorry, 0 axioms) — DEFINITIVE standard continuum theorem. Body Gronwall + C(M)→0 + tail vanishing from probability measure. No bounded γ, no uniform persistence, no c_min. `kuramoto_continuum_solved_of_bounded` proves `kuramoto_solved` is special case. ALL g ∈ L¹(R).
- [[continuum-stability-debate]] — GeneralGMainTheorem.lean: `kuramoto_solved_full_continuum` (0 sorry, 0 axioms) — DEFINITIVE standard continuum theorem with self-contained tail-body split proof. Takes ODE + body exp decay per M. No bounded γ, no uniform persistence, no c_min. `kuramoto_solved_full_continuum_of_bounded` proves `kuramoto_solved` is special case. ALL g ∈ L¹(R).
- [[continuum-stability-debate]] — GeneralGMainTheorem.lean: `kuramoto_solved_v2` (0 sorry, 0 axioms) — Direct analogue of `kuramoto_solved` fixed for standard continuum model. Three FALSE hypotheses REMOVED (bounded γ, uniform persistence, c_min), REPLACED by body exp decay per truncation M. `kuramoto_solved_v2_of_bounded` shows `kuramoto_solved` is special case. ALL g ∈ L¹(R).
- [[continuum-stability-debate]] — GeneralGMainTheorem.lean: `kuramoto_continuum_from_body_drop` (0 sorry, 0 axioms) — CLEANEST standard continuum theorem. Takes body Lyapunov drop per M (Tendsto form). Tail vanishing from probability measure. ε/2 argument via integral_add_compl. Also `body_drop_of_exp_decay` + `kuramoto_continuum_from_body_exp_decay`. No bounded γ, no uniform persistence, no c_min. ALL g ∈ L¹(R).
- [[continuum-stability-debate]] — ContinuumDerivedGronwall.lean (0 sorry, 0 axioms): `kuramoto_solved_continuum_v2` — NEW theorem with derived body Gronwall. Takes body derivative bound dV_body/dt ≤ -rate·V_body + forcing per M. DERIVES body Gronwall via new `gronwall_with_forcing` lemma (Gronwall comparison with forcing term). No bounded γ, no uniform persistence, no c_min. Combined vanishing forcing/rate + μ(tail) → 0.
- [[continuum-stability-debate]] — ContinuumSolvedWired.lean (0 sorry, 0 axioms): `kuramoto_continuum_wired` — SINGLE wired continuum theorem. Derives body persistence from ODE comparison, wires into parameterized body drop, calls kuramoto_continuum_real. Uses hγ_pos (0 < γ, Ω excludes ω=0 WLOG). No moment condition. Codex reviewed: "measure-theoretically fine."
- [[continuum-stability-debate]] — KuramotoSolvedContinuumNew.lean (0 sorry, 0 axioms): `kuramoto_solved_continuum` — DEFINITIVE tail-body split theorem for standard continuum model. Takes body absorbing ball + combined vanishing C(M)+μ(tail)→0. No bounded γ, no uniform persistence, no c_min. Also `kuramoto_solved_continuum_gronwall` (body Gronwall → absorbing ball).
- [[continuum-stability-debate]] — ContinuumSolvedReal.lean (0 sorry, 0 axioms): `kuramoto_continuum_real` — NO MOMENT CONDITION continuum theorem. Tail vanishing derived from probability measure (not γ integrability). Applies to ALL g ∈ L¹ including Lorentzian. Strictly generalizes kuramoto_solved_continuum.
- [[continuum-stability-debate]] — KuramotoSolvedContinuum.lean (0 sorry, 0 axioms): `kuramoto_solved_continuum` — DEFINITIVE continuum theorem. Resolves all three reviewer problems: (1) body persistence not uniform, (2) γ integrable not bounded, (3) rate from body pair coercivity not c_min. Covers Gaussian, Student-t ν>2, compact support.
- [[continuum-stability-debate]] — ContinuumSolvedFinal.lean (0 sorry, 0 axioms): `kuramoto_standard_continuum` — standard continuum convergence with body pair coercive bound. Key new ingredient: ∫∫ pair ≥ 2·δ·ds·μ(body)·V_body via set integral monotonicity. Integrable γ, body persistence, no bounded γ_max. Covers Gaussian, Student-t ν>2, compact support.
- [[continuum-stability-debate]] — ContinuumSolvedComplete.lean (0 sorry, 0 axioms): `kuramoto_continuum_stability` — definitive end-to-end theorem for standard continuum model (γ=|ω| unbounded). Resolves all three reviewer problems: (1) body persistence not uniform, (2) γ bounded per-body, (3) rate from coercivity not c_min. Covers Gaussian, Student-t ν>3, compact support.
- [[continuum-stability-debate]] — ContinuumSolvedFromODE.lean (0 sorry, 0 axioms): `kuramoto_solved_continuum_from_ode` — correct continuum theorem deriving body persistence from ODE comparison. Resolves all three problems (uniform persistence, bounded γ, c_min). Body persistence via bodyEquilibrium(M,K,r_min). Applies to Gaussian, Student-t ν>2, compact support.
- [[continuum-stability-debate]] — ContinuumSolvedDefinitive.lean (0 sorry, 0 axioms): `kuramoto_standard_continuum` — definitive theorem for standard continuum model. Body Gronwall + combined vanishing C(M)+μ(tail)→0. Subsumes `kuramoto_solved`. Applies to Gaussian, Student-t ν>2, compact support.
- [[continuum-stability-debate]] — KuramotoContinuumTheorem.lean (0 sorry, 0 axioms): `kuramoto_continuum_theorem` — clean end-to-end theorem for standard continuum model. Direct ε/2 tail-body split. Takes V antitone + tail vanishing + body convergence per M. Resolves all three reviewer problems. Minimal hypotheses.
- [[continuum-stability-debate]] — BodyPersistenceFromODE.lean (0 sorry, 0 axioms): `body_persistence_lower_bound` — α(t) ≥ min(α(0), β*) on body {γ≤M} when r≥r_min. Proves body persistence from ODE comparison principle. Also: 2 integrability sorries filled in KuramotoSolvedContinuum.lean.
- [[continuum-stability-debate]] — ContinuumStandardFull.lean (0 sorry, 0 axioms): `kuramoto_continuum_standard_full` — definitive standard continuum theorem via body drop + EventualTAC. Takes V antitone + body drop + tail vanishing. Resolves all three reviewer problems. Covers ALL g ∈ L¹ (including Lorentzian path via monotone limit).
- [[continuum-stability-debate]] — KuramotoSolvedContinuumClean.lean (0 sorry, 0 axioms): Three clean theorems for standard continuum model. `kuramoto_solved_continuum_tailbody` resolves all three reviewer problems via tail-body ISS split. Covers Gaussian, Student-t ν>2, compact support.
- [[continuum-stability-debate]] — KuramotoSolvedContinuum.lean: `leibniz_oa_integrable_gamma` (0 sorry) — Leibniz with ω-dependent dominator 2γ(ω)+K. Resolves bounded-γ obstruction for standard continuum model. Main theorem `kuramoto_solved_integrable_gamma` handles Gaussian/Student-t/compact g.
- [[continuum-stability-debate]] — BodyLaSalleConvergence.lean (0 sorry): V→0 via MVT on each body truncation. Alternative proof path: body LaSalle + tail vanishing. Same BodyODEData hypotheses.
- [[continuum-stability-debate]] — ContinuumSolvedDerived.lean (0 sorry): derived continuum theorem with generalized Leibniz (dominator 2γ+K integrable). Resolves all three reviewer problems for ∫|ω|g < ∞.
- [[continuum-stability-debate]] — ContinuumBodyLeibniz.lean (0 sorry): FTC body Leibniz → monotone limit → V→0 for ALL g ∈ L¹. Gap: HasDerivAt V_body (Leibniz rule).
- [[continuum-stability-debate]] — ContinuumSolvedRealLine.lean (0 sorry): definitive continuum theorem for standard model on R. Resolves all three reviewer problems: no bounded γ, no uniform persistence, no c_min.
- [[continuum-stability-debate]] — BodyLeibnizInstantiation.lean (0 sorry): body Leibniz identity → MonotoneLeibniz → V→0. Single gap: Leibniz integral rule for OA on bounded body.
- [[continuum-stability-debate]] — SummabilityLaSalle.lean (0 sorry): V→0 via ∫|V'|<∞ summability route. Body drop → V_body summable → V→0.
- [[continuum-stability-debate]] — ContinuumSolvedGeneral.lean (0 sorry): definitive continuum theorem resolving all three reviewer problems. No bounded γ, no uniform persistence, no c_min.
- [[continuum-stability-debate]] — BarbalatLeibnizBridge.lean (0 sorry): V→0 proved for g with finite first moment (∫|ω|g < ∞). Extends bounded-γ theorem to Gaussian/compact support.
- [[continuum-stability-debate]] — ContinuumTailBodyConvergence.lean (0 sorry): corrected ISS convergence with general absorbing radius C(M). Fixes unsatisfiable C ≤ μ(tail) in prior theorems.
- [[lean-proof-status]] — Machine-checked proof status: 145 files, 0 sorry, 0 axioms. New: `tail_body_iss_convergence`.
- [[h-approx-equivalence]] — h_approx ↔ V→0 equivalence proved in Lean. The tail-body hypothesis is exactly L² Lyapunov convergence.
- [[kuramoto-stability-problem]] — Is the partially-synchronized branch of the Kuramoto model linearly and globally dynamically stable along its entire length?
- [[kuramoto-stability-state-of-the-art]] — A cross-source synthesis of the current state of the 50-year-old problem of global nonlinear stability of the partially locked state (PLS) of the Kuramoto model.
- [[subproblem-decomposition]] — Breaking the open problem into concrete, individually attackable subproblems.
- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — A research hypothesis for a partial resolution of the Kuramoto stability problem by extending the Lipton-Mirollo-Strogatz hyperbolic Lyapunov construction to the Ott-Antonsen manifold.
- [[research-program]] — A concrete sequence of progressively harder problems, where each level builds on the previous and the final level IS the open problem.
- [[cooperative-oa-global-stability]] — A focused synthesis assembling the ingredients for Approach 22 (rational approximation + cooperativity) — the most promising attack on full-range global stability of the Kuramoto PLS.
- [[ott-antonsen-ansatz]] — The Ott-Antonsen ansatz is an exact dimension reduction of the Kuramoto-Sakaguchi equation in which a two-parameter family of densities parameterised by a complex function collapses the nonlinear integro-differential PDE to a closed ODE.
- [[kuehn-landi-2025-oa-unstable-manifold]] — Proves that the OA manifold of the mean-field limit is the direct dynamical analogue of the unstable manifold of the homogeneous steady state in the continuum limit.
- [[banaji-angeli-2009-monotone-first-integral]] — Proves every bounded orbit converges for strongly monotone semiflows with a $K$-increasing conserved first integral, with unique equilibrium per level set.
- [[cestnik-martens-2024-riccati-array]] — Exact dimensionality reduction for arbitrary arrays of globally coupled complex-valued Riccati equations, generalizing Watanabe-Strogatz (1993) to complex amplitudes.

## Concepts

- [[kinetic-formulation]] — The kinetic formulation describes a population of interacting particles or oscillators in the thermodynamic limit $N \to \infty$ by a density evolving under a continuity equation whose velocity field is sourced by a self-consistent mean field.
- [[landau-damping]] — Landau damping is the exponential decay of macroscopic perturbations in a system whose linearization has a neutrally stable continuous spectrum on the imaginary axis, produced not by true eigenmodes but by phase mixing of a continuum of neutral modes.
- [[mean-field-coupling]] — Mean-field coupling is the modelling ansatz in which every pair of units in a population interacts with the same strength scaled as $1/N$, so that each unit effectively sees a global average rather than individual neighbours.
- [[order-parameter]] — An order parameter is a scalar (or low-dimensional) quantity whose value distinguishes the phases of a many-body system and serves as the dependent variable in a phase-transition description.
- [[ott-antonsen-ansatz]] — The Ott-Antonsen ansatz is an exact dimension reduction of the Kuramoto-Sakaguchi equation in which a two-parameter family of densities parameterised by a complex function collapses the nonlinear integro-differential PDE to a closed ODE.
- [[phase-locked-state]] — A phase-locked state of a coupled-oscillator ensemble is a configuration in which every pairwise phase difference is constant in time, so the whole population rotates rigidly while its shape in phase space is frozen.
- [[synchronization]] — Synchronization is the spontaneous emergence of collective rhythmic order in a population of self-sustained oscillators with differing native frequencies, arising as a phase transition once pairwise coupling exceeds a threshold.

## Entities

### Open

- [[kuramoto-finite-n-convergence]] — Does the finite-$N$ Kuramoto oscillator system converge, in a rigorous probabilistic sense, to its continuum limit as $N \to \infty$, and at what rate do the finite-$N$ fluctuations of the order parameter decay?

### Partially-Resolved

- [[kuramoto-stability-problem]] — Is the partially-synchronized branch of the Kuramoto model linearly and globally dynamically stable along its entire length?

### Proven

_(none yet)_

### Disproven

_(none yet)_

### Other

- [[kuramoto-model]] — The Kuramoto model is a system of $N$ mean-field-coupled phase oscillators with distributed native frequencies, introduced by Yoshiki Kuramoto in 1975 as the first exactly-soluble model of synchronization as a phase transition.
- [[kuramoto-on-a-sphere]] — The Kuramoto model on a sphere is the generalization of the classical Kuramoto model to $N$ identical self-propelled particles moving on the unit sphere $S^{d-1}$, with $d \geq 3$, coupled all-to-all through a $d$-dimensional vector order parameter.
- [[kuramoto-sakaguchi-equation]] — The Kuramoto-Sakaguchi equation is the nonlinear integro-differential PDE obtained as the mean-field / kinetic limit $N \to \infty$ of the Kuramoto model.
- [[peskin-model]] — The Peskin model is a pulse-coupled integrate-and-fire model of cardiac pacemaker cells, introduced by Charles S. Peskin in 1975, in which identical oscillators emit instantaneous voltage kicks to their neighbours upon firing and synchronize in finite time.
- [[winfree-model]] — The Winfree model is the first mathematical model of collective synchronization of a population of weakly-coupled biological oscillators, introduced by Arthur Winfree in 1967.

## Comparisons

_(none yet)_

## Syntheses

- [[body-lasalle-gap-analysis]] — V_body antitonicity is the REAL gap (not Leibniz). Leibniz proved; pair bound for body-restricted integral under global self-consistency is open.
- [[lean-proof-status]] — Machine-checked proof status: 0 sorry, 0 axioms across 132 files. h_approx ↔ V→0 equivalence proved. 3480 build jobs.
- [[h-approx-equivalence]] — h_approx ↔ V→0: the tail-body hypothesis is equivalent to L² convergence. Proved in Lean.
- [[continuum-stability-debate]] — Final debate synthesis: standard continuum model remains open; 5 obstructions identified, 4 viable strategies ranked.
- [[continuum-l2-lyapunov]] — V∞ = ∫g|α-α*|²dω is a Lyapunov function for the continuum OA flow. h_approx↔V→0 (tautological); real gap is proving V→0 via LaSalle+precompactness.
- [[cooperative-oa-global-stability]] — A focused synthesis assembling the ingredients for Approach 22 (rational approximation + cooperativity) — the most promising attack on full-range global stability of the Kuramoto PLS.
- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — A research hypothesis for a partial resolution of the Kuramoto stability problem by extending the Lipton-Mirollo-Strogatz hyperbolic Lyapunov construction to the Ott-Antonsen manifold.
- [[kuramoto-stability-state-of-the-art]] — A cross-source synthesis of the current state of the 50-year-old problem of global nonlinear stability of the partially locked state (PLS) of the Kuramoto model.
- [[research-program]] — A concrete sequence of progressively harder problems, where each level builds on the previous and the final level IS the open problem.
- [[subproblem-decomposition]] — Breaking the open problem into concrete, individually attackable subproblems.

## Source Summaries

- [[castorrini-galatolo-tanzi-2025-self-consistent-transfer]] — Proves local exponential convergence to equilibrium for mean-field coupled dynamical systems via spectral analysis of the self-consistent transfer operator differential.
- [[campa-2022-oa-generic-frequency]] — Extends OA dimensional reduction to non-rational $g$ (Gaussian) via rational approximation with Taylor-matching polynomials; numerical only, no rigorous convergence bounds.
- [[kuehn-landi-2025-oa-unstable-manifold]] — Proves that the OA manifold of the mean-field limit is the direct dynamical analogue of the unstable manifold of the homogeneous steady state in the continuum limit.
- [[tang-2025-lean4-survey]] — A 46-page survey of Lean 4's architecture, type system, proof tactics, mathematical libraries, and applications.
- [[pecorella-2024-kuramoto-kolmogorov]] — Studies the Kuramoto model with inertia as a degenerate Kolmogorov-Fokker-Planck equation, proving existence, uniqueness and a priori estimates via Lie group methods.
- [[cestnik-martens-2024-riccati-array]] — Exact dimensionality reduction for arbitrary arrays of globally coupled complex-valued Riccati equations, generalizing Watanabe-Strogatz (1993) to complex amplitudes.
- [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]] — Unifying the Watanabe-Strogatz finite-$N$ reduction and the Ott-Antonsen infinite-$N$ ansatz under a single group-theoretic framework via the Mobius group of the unit ball.
- [[iacobelli-2021-kinetic-wasserstein]] — Introduces anisotropic kinetic Wasserstein distances tailored for Vlasov-type equations, improving classical stability estimates.
- [[bronski-wang-2020-partially-locked]] — Derives analytical criteria for the existence of partially phase-locked states in the finite-$N$ Kuramoto model by constructing nested invariant balls.
- [[dietert-2017-pls-sobolev]] — Extends nonlinear Landau damping from the incoherent state to the PLS under Sobolev regularity, proving local nonlinear stability for $b > 3/2$.
- [[morales-poyato-2019-trend-equilibrium]] — Quantitative convergence rates to the global equilibrium for the K-S equation in a large coupling regime using entropy production methods.
- [[jabin-wang-2019-mean-field-singular]] — Develops relative entropy methods for mean-field limits with singular interaction kernels.
- [[dietert-fernandez-2018-asymptotic-stability]] — The definitive review of rigorous asymptotic stability results for stationary solutions of the continuum Kuramoto PDE, with a crucial original result proving exponential convergence to the OA manifold.
- [[haraux-jendoubi-2015-convergence-problem]] — Comprehensive monograph on the convergence problem: when does a bounded trajectory of an autonomous evolution equation converge to a single equilibrium?
- [[chen-engelbrecht-mirollo-2017-hyperbolic-geometry]] — The $d = 2$ precursor to Lipton-Mirollo-Strogatz (2021): proves that the standard Kuramoto model for identical oscillators on $S^1$ is a gradient flow on the hyperbolic disk.
- [[ha-ko-park-zhang-2016-collective-synchronization]] — A 60-page survey presenting five synchronization models in a unified framework, with rigorous treatment of complete synchronization, phase-locked states, and kinetic limits.
- [[pietras-daffertshofer-2016-oa-parameter-dependent]] — Rigorous proof that the Ott-Antonsen manifold remains asymptotically attractive when oscillator dynamics depend on additional oscillator-specific parameters.
- [[dietert-2016-thesis]] — PhD thesis providing the detailed proofs underlying Dietert (2016) and Dietert (2017), with additional material on exponential norms, strip analyticity, and the $\mathcal{Z}^a$ norm construction.
- [[fernandez-gerard-varet-giacomin-2016-landau-damping]] — The first rigorous proof of nonlinear Landau damping for the Kuramoto model: under a stability criterion equivalent to $K < K_c$, the order parameter decays polynomially.
- [[dietert-2016-stability-bifurcation]] — The foundational paper establishing rigorous stability theory for the Kuramoto model via Fourier-space energy methods, containing the universal energy identity and global stability by energy method.
- [[ha-kim-ryoo-2016-emergence-phase-locked-states]] — Proves the complete-synchronization theorem for the finite-dimensional Kuramoto model from generic initial configurations in the large-coupling regime.
- [[dolbeault-mouhot-schmeiser-2015-hypocoercivity-kinetic]] — Explicit hypocoercivity framework for kinetic equations with microscopic and macroscopic coercivity assumptions, giving exponential convergence with quantitative rates.
- [[chiba-2015-kuramoto-conjecture]] — Resolves the Kuramoto conjecture by developing a spectral theory on a rigged Hilbert space that handles the continuous spectrum of the linearized K-S operator.
- [[faou-rousset-2014-vlasov-hmf]] — Proves nonlinear Landau damping with polynomial rate for the Vlasov-HMF model under Sobolev regularity, using a bootstrap argument on the Volterra equation.
- [[carrillo-2013-wasserstein-kuramoto]] — Proves Wasserstein $p$-distance between measure-valued solutions of the kinetic Kuramoto equation decays exponentially for identical oscillators with initial data in a half-circle.
- [[mouhot-villani-2011-landau-damping]] — Proves nonlinear Landau damping for the Vlasov-Poisson equation in analytic regularity — the landmark result showing convergence to equilibrium without dissipation, purely through phase mixing.
- [[brezis-2011-functional-analysis-sobolev-pdes]] — The Brezis graduate textbook, ingested as a concordance / reference tool for the functional-analytic machinery that the Kuramoto open problems require.
- [[hanche-olsen-holden-2010-kolmogorov-riesz]] — The definitive modern statement of the Frechet-Kolmogorov characterization of precompact sets in $L^p$.
- [[banaji-angeli-2009-monotone-first-integral]] — Proves every bounded orbit converges for strongly monotone semiflows with a $K$-increasing conserved first integral, with unique equilibrium per level set.
- [[villani-2009-hypocoercivity]] — Systematic study of convergence to equilibrium for degenerate diffusive equations via modified Lyapunov functionals combining dissipation and transport.
- [[ott-antonsen-2008-low-dimensional]] — The foundational paper introducing the Ott-Antonsen ansatz: an exact reduction of the infinite-dimensional Kuramoto-Sakaguchi continuum dynamics to a finite set of ODEs.
- [[strogatz-2000-from-kuramoto-to-crawford]] — A 20-page retrospective by Steven Strogatz covering 25 years of mathematical work on the Kuramoto model, from Kuramoto's 1975 self-consistency calculation through the 1990s papers of J. D. Crawford.
- [[kuramoto-1975-self-entrainment]] — Three-page conference contribution in which Yoshiki Kuramoto introduces and exactly solves the mean-field phase-oscillator model that now bears his name.

## Tag Index

- **convergence** (3)
- **cooperative-systems** (2)
- **degenerate-pde** (1)
- **dimension-reduction** (13)
- **dynamical-systems** (41)
- **formal-verification** (2)
- **functional-analysis** (7)
- **group-theory** (5)
- **hypocoercivity** (1)
- **integrability** (1)
- **kinetic-theory** (18)
- **kuramoto** (1)
- **landau-damping** (2)
- **mathematical-biology** (8)
- **mathematical-physics** (1)
- **mean-field** (1)
- **neuroscience** (1)
- **open-problem** (7)
- **optimal-transport** (3)
- **ott-antonsen** (1)
- **pde** (20)
- **plasma-physics** (5)
- **probability** (1)
- **reference-textbook** (1)
- **reference-tool** (1)
- **research-hypothesis** (1)
- **research-plan** (2)
- **riccati-equation** (1)
- **spectral-theory** (2)
- **stability** (1)
- **statistical-physics** (18)
- **synchronization** (38)
- **theorem-prover** (1)
