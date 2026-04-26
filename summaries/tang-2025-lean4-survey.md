---
type: source-summary
title: "Tang (2025) — A Comprehensive Survey of the Lean 4 Theorem Prover"
created: 2026-04-16
updated: 2026-04-16
sources: []
tags: [formal-verification, theorem-prover, reference-tool]
aliases: ["Lean 4 survey", "Tang 2025", "LEAN 4"]
source_file: "../raw/papers/2501.18639.pdf"
source_kind: pdf
source_date: 2025-01-28
---

# Tang (2025) — A Comprehensive Survey of the Lean 4 Theorem Prover

A 46-page survey of Lean 4's architecture, type system, proof tactics, mathematical libraries, and applications, ingested here as the **formal verification** component of the attack on the Kuramoto open problems: once a candidate Lyapunov kernel is identified (by hand or by computational search), Lean 4 formally verifies the decrease property.

## Bibliographic details

- **Author:** Xichen Tang.
- **Venue:** arXiv preprint arXiv:2501.18639v1 (January 28, 2025). Subject areas: cs.LO (Logic in Computer Science), cs.PL (Programming Languages).
- **Length:** 46 pages.
- **Pages read:** pp 1–10 (intro, set theory, tactics, structures, advanced tactics, best practices), pp 26–35 (mathematical foundations, proof automation, real analysis, advanced verification, performance optimization, type theory). Approximately 20 of 46 pages — focused on the sections most relevant to the Kuramoto pipeline.
- **Not read:** pp 11–25 (axioms and computation details, full real-number construction, pattern matching mechanics), pp 36–46 (Mathlib advanced structures, perfectoid spaces, homotopy type theory integration, educational applications, future research directions, comprehensive conclusion). These are either too low-level (language internals) or too specialized (algebraic geometry, HoTT) for the present concordance.
- **Original URL:** https://arxiv.org/abs/2501.18639

## How Lean 4 fits the Kuramoto attack pipeline

The computational attack pipeline for [[kuramoto-stability-problem]] has three stages:

1. **Hypothesis generation** — the [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] synthesis page identifies the candidate Lyapunov kernel $\mathcal{H}(\alpha; \alpha^*_K)$ as the target object.
2. **Candidate identification** — by manual mathematical analysis, numerical experimentation, or computational search.
3. **Formal verification** — **Lean 4** (this source) is the theorem prover that would take a promising candidate kernel and produce a machine-checked proof that the time derivative is strictly negative along the [[ott-antonsen-ansatz]] flow for all valid inputs.

Lean 4's role is the final verification step that elevates a numerical or heuristic observation to a machine-checked mathematical theorem.

## What Lean 4 is

Lean 4 is an **interactive theorem prover and functional programming language** built on dependent type theory (the Calculus of Inductive Constructions). It was developed by Leonardo de Moura (initially at Microsoft Research, now at AWS) and is the successor to Lean 3 (used in the Mathlib project and Kevin Buzzard's formalization work). Key design principles:

- **Propositions as types, proofs as terms.** A mathematical statement is a type; a proof of that statement is a term of that type. The type checker verifies proofs by checking that the term has the claimed type.
- **Dependent types.** Types can depend on values, enabling precise specifications (e.g., "a list of length $n$" rather than just "a list").
- **Metaprogramming.** Users can write custom tactics and automation in Lean itself (not a separate metalanguage), giving full access to the proof state from within the language.
- **Compiled execution.** Lean 4 compiles to C via an intermediate representation, so verified programs can be extracted and run efficiently.

## Concordance — Lean 4 features by Kuramoto-pipeline need

### For formalizing the Lyapunov decrease property

The core verification target is a statement of the form:

> For all $\alpha : \mathbb{R} \to \mathbb{D}$ satisfying the OA ODE and all $K > K_c$, $\frac{d}{dt}\Phi_{\text{OA}}[\alpha(\cdot, t)] < 0$.

To formalize this in Lean 4, one needs:

**Real numbers and inequalities.** Lean 4 constructs $\mathbb{R}$ via Cauchy sequences of rationals, quotient types, and the completeness axiom (least upper bound property). The reals form a `LinearOrderedField` instance, so all ordered-field arithmetic is available. Inequalities ($<$, $\leq$) are `Prop`-valued, and the tactics `linarith` (linear arithmetic) and `norm_num` (numerical normalization) handle routine inequality steps automatically. See §19.3 of the survey (pp 27–28) for the formalization of `Real` as a quotient of `CauchySequence.setoid`.

**Complex numbers.** $\mathbb{C}$ is available in Mathlib as $\mathbb{R} \times \mathbb{R}$ with the standard field structure. The unit disk $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$ can be defined as a subtype `{z : ℂ // Complex.abs z < 1}`.

**Integrals.** The functional $\Phi_{\text{OA}}[\alpha] = \int g(\omega)\,\mathcal{H}(\alpha(\omega); \alpha^*_K(\omega))\,d\omega$ is an integral over $\mathbb{R}$ with respect to the measure $g(\omega)\,d\omega$. Mathlib has the Bochner integral and Lebesgue measure; formalizing this integral is feasible but nontrivial.

**Differentiation.** The time derivative $\frac{d}{dt}\Phi_{\text{OA}}$ requires differentiating under the integral sign with respect to $t$, where $\alpha(\omega, t)$ satisfies an ODE. Lean 4 / Mathlib has `HasDerivAt` and `deriv` for real-valued functions; the chain rule and differentiation under the integral sign are available but the specific form needed (ODE-driven parameter dependence) may require manual setup.

### For proof automation

**Core tactics available (§2 of the survey, pp 5–7):**

- `exact` — supplies an exact proof term
- `rfl` — proves equality by reflexivity
- `apply` — backward reasoning from a hypothesis
- `rw` — rewriting using equations
- `have` — introduces intermediate lemmas
- `ring` — closes goals in commutative rings (e.g., expanding $(a+b)^2 = a^2 + 2ab + b^2$)
- `linarith` — proves linear arithmetic goals (combinations of $\leq$ and $<$ inequalities)
- `simp` — simplification using declared rewriting rules
- `norm_num` — numerical normalization for concrete arithmetic

**For the Kuramoto verification specifically:** the decrease property of $\Phi_{\text{OA}}$ will likely reduce (after symbolic differentiation) to a sign condition on a sum/integral of terms, each of which is a product of real-valued expressions. The `ring` tactic handles algebraic simplification; `linarith` handles the final inequality. The bottleneck is likely the differentiation and integral manipulation, which Mathlib handles but with significant proof-engineering effort.

### For structuring the proof

**Structures and type classes (§3 of the survey, pp 6–7):** Lean 4 uses type classes for algebraic and topological structures. The Kuramoto formalization would use:
- `TopologicalSpace` for the state spaces ($\mathbb{D}$, $\mathbb{R}$, function spaces)
- `MeasureSpace` for the frequency-distribution integral
- `NormedAddCommGroup` and `InnerProductSpace` for the $L^2(g)$ function space
- `LinearOrderedField` for $\mathbb{R}$-valued inequalities

These are all available in Mathlib. The custom structures needed for Kuramoto (e.g., `OttAntonsenState` as a function $\mathbb{R} \to \mathbb{D}$ satisfying certain constraints) would be defined as Lean structures or subtypes.

### For translating candidate kernels into Lean 4

Once a candidate kernel $\mathcal{H}$ is identified (whether by hand or by computational search), it must be translated into a Lean 4 definition for formal verification. Two approaches:

1. **Manual translation.** A human writes the corresponding Lean definition and proof. This is the conservative approach and is guaranteed to work but is slow.
2. **LLM-assisted translation.** An LLM converts a symbolic expression to a Lean 4 `def` and generates a proof skeleton. The skeleton is then completed interactively or via further LLM-assisted tactic application. This is the subject of active research in the LLM-Lean integration community.

## What Lean 4 does not provide (relative to the Kuramoto pipeline)

- **Numerical computation.** Lean 4 is a proof checker, not a numerical solver. Numerical screening of candidate kernels (computing $\frac{d}{dt}\Phi_{\text{OA}}$ along discretized OA trajectories) must happen in a computational environment (Python/NumPy), not in Lean. Lean's role is purely the formal-verification step after a candidate passes numerical screening.
- **ODE solver.** Lean 4 / Mathlib does not have a general ODE existence/uniqueness framework at the level of Brezis Ch 7. Formalizing the OA ODE's existence and the differentiability of its solutions with respect to parameters would be a substantial formalization project in itself. For the pipeline's immediate purposes, the OA ODE can be *assumed* as a hypothesis in the Lean proof, with the existence theory deferred.
- **Measure-theoretic integration in full generality.** Mathlib has the Bochner integral and Lebesgue measure, but the specific integral manipulations needed (differentiation under the integral sign with parameter-dependent bounds, splitting at the locked/drifting boundary $|\omega| = Kr^*$) are not pre-built and would require custom lemma development.
- **Hyperbolic geometry.** The Poincaré disk model, Möbius transformations, and hyperbolic Poisson kernels are not in Mathlib as of the survey date (January 2025). Formalizing the hyperbolic-metric tools from [[lipton-mirollo-strogatz-2021-kuramoto-on-sphere]] would be a separate project.

## Comparison with other provers (from the survey)

The survey compares Lean 4 with Coq, Isabelle/HOL, Agda, and Mizar. For the Kuramoto pipeline, Lean 4's advantages are:

- **Mathlib ecosystem.** The largest unified library of formalized mathematics, with active development in analysis, topology, measure theory, and algebra. Coq has a comparable but more fragmented library landscape.
- **Proof automation.** `simp`, `ring`, `linarith`, `norm_num` cover a wide range of algebraic and arithmetic goals out of the box. Isabelle/HOL has comparably strong automation (`auto`, `simp`, `sledgehammer`); Coq's automation is weaker.
- **Metaprogramming.** Custom tactics can be written in Lean itself, enabling domain-specific automation (e.g., a tactic that handles hyperbolic-metric inequalities). This is a Lean 4 innovation over Lean 3 and most other provers.
- **LLM integration potential.** Lean 4's concrete syntax and the availability of tactic-mode proofs make it a natural target for LLM-generated proof steps. Several research projects (not covered in this survey but known to the community) explore GPT/Claude-assisted Lean proof generation.

## Related pages

- [[hyperbolic-lyapunov-attack-on-kuramoto-stability]] — the synthesis page describing the hypothesis and verification target
- [[kuramoto-stability-problem]] — the open problem the pipeline targets
- [[ott-antonsen-ansatz]] — the mathematical setting for the verification target
- [[brezis-2011-functional-analysis-sobolev-pdes]] — the FA/PDE toolkit whose theorems would need Lean formalization for a complete proof (ODE existence, differentiation under integral sign, Sobolev regularity)
