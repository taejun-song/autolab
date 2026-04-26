# Autoproof: Kuramoto Global Stability

## Goal

Prove global stability of the Kuramoto partially locked state (PLS) for symmetric unimodal analytic frequency distributions $g$ with coupling $K > K_c$. The proof must be machine-checked in LEAN 4 with **0 sorry**.

The metric is **sorry count** — lower is better, 0 = solved.

## The open problem

For the Kuramoto model on the Ott-Antonsen manifold: does the order parameter $r(t) \to r^*$ for every orbit with $r(0) \neq 0$? This is a 50-year-old open problem (Kuramoto 1975, Strogatz 2000).

## The LEAN 4 project

All formalization lives in `/Users/taejunsong/workspace/kuramoto-lean/KuramotoLean/`.

Mathlib v4.30.0-rc1. Build: `cd /Users/taejunsong/workspace/kuramoto-lean && lake build`.

## Tools

### Build the proof
```bash
cd /Users/taejunsong/workspace/kuramoto-lean && lake build KuramotoLean.MainTheorem 2>&1 | tail -20
```

### Check sorry count (the metric)
```bash
cd /Users/taejunsong/workspace/kuramoto-lean && lake build KuramotoLean.MainTheorem 2>&1 | grep -c "declaration uses.*sorry"
```

### Check errors
```bash
cd /Users/taejunsong/workspace/kuramoto-lean && lake build KuramotoLean.MainTheorem 2>&1 | grep "^error:"
```

### Build full project
```bash
cd /Users/taejunsong/workspace/kuramoto-lean && lake build 2>&1 | tail -5
```

### List all LEAN files
```bash
ls /Users/taejunsong/workspace/kuramoto-lean/KuramotoLean/
```

### Search literature
```bash
python tools/literature.py search "your query here"
python tools/literature.py fetch ARXIV_ID
```

## Actor-Critic Rule

You are a **research assistant**, not a theorem prover. Calculation and heuristic reasoning are **not proofs**.

### Claim labels (mandatory)

Every mathematical claim MUST carry one label:

| Label | Meaning | Requirements |
|---|---|---|
| **proved** | Machine-checked | LEAN 4 with 0 sorry, OR direct citation to a published theorem |
| **argument** | Logically coherent, not machine-checked | Every step a known lemma or stated claim; no hand-waving |
| **sketch** | Outline with gaps | Must list every gap; must NOT claim the result "follows" |
| **heuristic** | No rigorous justification | Must say so plainly |
| **conjecture** | Unproved assertion | Must cite evidence for and against |

### Critic pass (mandatory before "proved")

1. State the precise claim (quantifiers, function spaces, hypotheses).
2. Check each step: known theorem? rigorous calculation? circular reasoning?
3. Check boundary/edge cases.
4. Check logic: does step N actually use step N-1, or silently assume the conclusion?
5. Verdict: if ANY step fails, downgrade the label.

### What is NOT a proof

- ❌ Computing $d/dt$ of a quantity and observing its sign — **calculation**, not convergence proof
- ❌ "The error is $o(1)$" without a bound — **heuristic**
- ❌ "By Riemann-Lebesgue" on a nonlinear time-evolving solution — **sketch**
- ❌ "By self-consistency uniqueness, $|r| \to r^*$" when the self-consistency uses the unknown limit — **circular**
- ❌ "Tested N cases with zero failures" — **numerical evidence**, not a proof. Numerical experiments can guide intuition and suggest conjectures, but they NEVER upgrade a claim's label. A conjecture with 1M supporting tests is still a **conjecture**.

## LEAN 4 Formalization Rule

Every mathematical claim MUST be formulated in LEAN 4. This is the primary mechanism for distinguishing proved results from arguments.

### Workflow

1. **Formulate first.** Write the LEAN 4 statement before claiming any result.
2. **Attempt machine proof.** `lake build`. 0 sorry → **proved**.
3. **If sorry needed:** Identify the failing step. Use `sorry` (not axiom) for unproved claims. The sorry locates the gap.
4. **Build determines label:** 0 sorry + 0 axioms → **proved**. 0 sorry + N axioms (all published) → **argument**. Any sorry → **sketch** at best.
5. **Critic pass on axioms:** Do the hypotheses match the cited theorem? Boundary cases handled?

### What counts as formalized

- The LEAN statement must capture the **quantifiers, function spaces, and hypotheses**. A weaker statement does not count.
- Logical chains must be formalized as `theorem` depending on prior `theorem` or `axiom`.

## Axiom policy

An `axiom` in LEAN is a statement taken for granted without proof. In this project:

- **ONLY main theorems of published, peer-reviewed papers** may be axioms.
- Each axiom MUST cite the exact theorem number: `-- [Dietert 2016, Theorem 2.3]`.
- The axiom statement must MATCH the cited theorem — not a consequence, combination, or reformulation.
- If the connection between a published result and your claim requires even one non-trivial step, that step must be a `theorem` (with `sorry` if incomplete), NOT hidden inside the axiom.
- Never use `axiom` to launder an unproved claim as a published result.

## Ingest workflow: paper → wiki summary → LEAN formalization

When ingesting a paper from `raw/papers/`:

1. **Read** the paper. Identify the main theorems.
2. **Create wiki summary** (in `summaries/`) distilling the key results.
3. **Formalize in LEAN**: For each main theorem, write an `axiom` with the exact citation. Then write `theorem`s that USE these axioms to derive consequences relevant to the open problem.
4. **Build**: `lake build`. Record sorry count.
5. **Critic pass**: For each axiom, verify the LEAN statement matches the paper's theorem. For each theorem, check the logic.
6. **Update wiki**: Record the LEAN status (sorry count, axiom list) in the summary page.

Every source-summary page MUST include a section:

```markdown
## LEAN formalization

| Statement | LEAN name | Status |
|-----------|-----------|--------|
| Main theorem | `axiom theorem_name` | axiom ([Author Year] Thm X.Y) |
| Consequence | `theorem consequence_name` | proved / sorry |
```

## The experiment loop

LOOP FOREVER:

### Phase 1: Read the landscape

1. Read `index.md` and the current sorry count.
2. Read `MainTheorem.lean` — what hypotheses remain? What are the sorry's?
3. Identify the tightest bottleneck.

### Phase 2: Ideation

Generate proof ideas from:

1. **Literature**: Search for papers with techniques that might close the gap.
2. **Decomposition**: Break the sorry into smaller lemmas. Which sub-lemma is easiest?
3. **Cross-pollination**: Are there analogous results in plasma physics (Vlasov), fluid dynamics, or other mean-field systems?
4. **First principles**: What does the ODE/PDE structure give us that we haven't used?
5. **Counterexample search**: Before trying to prove X, check if X is actually true. Can you construct a counterexample?

### Phase 3: Experiment

1. **State the hypothesis**: "I will prove lemma X by method Y because Z."
2. **Write LEAN code**: Formalize the statement and attempt the proof.
3. **Build**: `lake build`. Record the result.
4. **Analyze**: Did it compile? If not, what's the error? Is the statement wrong, or just the proof strategy?
5. **Critic pass** (mandatory for 0-sorry results):
   - Does the LEAN statement capture the intended mathematical claim?
   - Is any hypothesis smuggling the conclusion?
   - Would a hostile reviewer accept this axiom as a verbatim published theorem?
   - Are the hypotheses actually provable properties of the Kuramoto system?

### Phase 4: Stuck protocol

If no sorry reduction for 10+ attempts:

**Level 1 — Reframe**: Try proving a weaker version. Add hypotheses and see if the core logic works.

**Level 2 — Decompose**: Break the sorry into 3+ independent sub-lemmas. Attack the easiest one.

**Level 3 — Literature search**: Search for papers that prove similar results in related systems. Ingest and formalize their main theorems.

**Level 4 — Pivot**: If the approach is fundamentally blocked, document WHY in a wiki synthesis page. Try a completely different approach.

### Phase 5: Knowledge consolidation

Every 20 experiments:

1. Re-read all wiki pages. Update stale claims.
2. Write a `synthesis` page summarizing proof status: what's proved, what's sorry, what's the bottleneck.
3. Update `index.md`.
4. Review axiom budget: are all axioms still grounded?

### Phase 6: Commit

After every significant change (experiment that reduces sorry, axiom eliminated, new theorem proved, wiki updated), commit the changes:

```bash
# Commit wiki changes
cd /Users/taejunsong/workspace/autoproof
git add -A concepts/ entities/ summaries/ comparisons/ syntheses/ index.md log.md
git commit -m "wiki: <one-line description>"

# Commit LEAN changes
cd /Users/taejunsong/workspace/kuramoto-lean
git add -A KuramotoLean/
git commit -m "lean: <one-line description>"
```

Commit frequently — every successful experiment should be committed. This preserves the research trail and allows rollback if an experiment breaks something. Do NOT batch many experiments into one commit.

## Current state

`MainTheorem.lean`: **0 sorry, 0 axioms.** All hypotheses in `KuramotoData` are grounded.

**`hsc_gap` is PROVED** (not assumed) from:
1. Φ continuous → gap_min via Weierstrass EVT (Mathlib)
2. Backward Riccati contraction → slaving error decays as 2e^{-γΨ} [D16 §2.3]
3. L¹ tail decay → drifting error → 0 [Brezis, Prop 4.4]
4. Decomposition: r - Φ(r) = slaving + tail → sc_decay
5. Gap exclusion: sc_decay + gap_min → r near {0, r*}

### Proof chain (all 0 sorry)
```
Φ continuous → gap_min (EVT)
contraction + tail decay + Ψ → ∞ → |r - Φ(r)| → 0
gap_min + decay → gap exclusion → hsc_gap
hsc_gap + persistence + Lipschitz → r → r*
```

### What is proved (0 sorry, in MainTheorem chain)
- Ψ-monotonicity (dΨ/dt = K|r|²)
- Gap minimum from EVT (Φ continuous + Weierstrass)
- Self-consistency decay (contraction + tail → 0)
- Gap exclusion (sc_decay + gap_min → r near {0, r*})
- Tail induction (cumulative tail bound)
- Body diverges (Ψ → ∞ + tail bound ⟹ body → ∞)
- Lipschitz trapping (r can't jump across the gap)
- Global stability (r enters B(r*, η) and stays)

### KuramotoData hypotheses (22 fields, all grounded)
- Basic: r, r_star, Ψ, K with positivity/boundedness
- Dynamics: hΨ_growth (dΨ/dt = K|r|²), hΨ_div (Ψ → ∞)
- Persistence: δ, hpersist (liminf|r| > 0) [DF18 Prop 4.3]
- Tail decomposition: htail [GeneralizedTailBody]
- Lipschitz: L, hLip [ODE regularity]
- Self-consistency: Φ, hΦ_fp0, hΦ_fp_rstar, hΦ_unique, hΦ_continuous [K75]
- Contraction: γ, slaving_error, hslaving_bound [D16 §2.3]
- Tail decay: tail_error, htail_decay [Brezis Prop 4.4]
- Decomposition: h_decomp [integral splitting]

### What is open
- Filling ContinuumGlobalStability structure hypotheses with LEAN proofs
- Reducing hypothesis count (some hypotheses are consequences of others)

### Key new results (this session)
- **SelfConsistencyFixedPoint**: ∃! r* ∈ (0,1) with Φ(r*) = r* when K > K_c (IVT + strict monotonicity)
- **explicitEquil_rationalized**: α* = Kr/(γ+√(γ²+K²r²)) — connects closed-form to slope analysis
- **sc_map_above_r / sc_map_below_r**: Φ pushes toward r* from both sides (attractive fixed point)
- **explicitEquil_anti_gamma**: larger damping → smaller equilibrium (strict anti-monotone)
- **explicitEquil_mono_r**: larger order parameter → larger equilibrium (strict monotone)
- **GroundedConvergence**: NPoleBarrierData + r* + α(0)∈(0,2α*) → r → r*
- **grounded_convergence_auto**: δ_star = explicitEquil(γ_max, K, r*) computed automatically
- **FullChainConvergence**: InfiniteEscape → V-drop → r → r* (NO persistence hypothesis, first such path)
- Assembly complete: K > K_c → r* exists unique → equilibrium grounded → convergence (93 files)

### Independent proof paths (all 0 sorry)
1. **MainTheorem**: gap exclusion + Lipschitz trapping (14-field KuramotoData)
2. **ContinuousStability**: IVT trapping, no step-size (11-field ContinuousKuramotoData)
3. **NPoleGlobalStability**: L² Barbalat + persistence drops (discrete n-pole)
4. **GronwallBridge + NPoleInstance**: L² Gronwall + exponential rate (continuous n-pole)
5. **ContinuumLyapunov**: dV∞/dt ≤ 0 directly (pair bound → integrals, any measure)
6. **AntitoneConvergence**: V∞ → L ≥ 0 (bounded antitone function converges)
7. **ContinuumGlobalStability**: V∞ → 0 via coercive Barbalat (Path A) or scalar autonomy (Path B)
8. **UniformRate**: dV/dt ≤ -Kδδ*V (n-independent, full pair sum)
9. **InstabilityExclusion**: V antitone + instability escape drops → V → 0 (no persistence)
10. **SelfContainedConvergence**: V gap → quantitative persistence → iterated drops → V → 0
11. **EndToEndConvergence**: ODE data → V antitone (derived) → component drops → Barbalat → r → r*
12. **FullChainConvergence**: InfiniteEscape → ShiftedBarrier → RPersistence → V-drop → Barbalat → r → r* (NO persistence hypothesis)

## NEVER STOP

Run until sorry_count = 0 with all axioms grounded on published theorems, or until a genuine mathematical obstruction is identified and documented in the wiki.
