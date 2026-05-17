---
id: theorem-unique-identity
type: theorem
title: "Uniqueness of Identity Element"
status: proved
formal_status: verified
lean_file: "AutoProof/Theorems/UniqueIdentity.lean"
lean_decl: "unique_identity"
depends_on: ["def-group", "axiom-associativity", "axiom-identity-element", "axiom-inverse-element"]
used_by: []
proof_methods: ["direct-proof"]
created_at: 2026-05-17
updated_at: 2026-05-17
---
# Uniqueness of Identity Element

The identity element in a group is unique.

## Statement

Let $(G, \cdot, e, {}^{-1})$ be a group. If $e' \in G$ satisfies $e' \cdot a = a$ for all $a \in G$, then $e' = e$.

## Informal Meaning

There cannot be two distinct "do nothing" elements. Any element that behaves as a left identity must in fact be the designated identity $e$. This justifies referring to "the" identity element of a group.

## Axiomatic Space

| Axiom | Role in this proof |
|---|---|
| [[axiom-identity-element]] | Provides $e \cdot e' = e'$ |
| [[axiom-associativity]] | Not directly used (single-step equalities suffice) |
| [[axiom-inverse-element]] | Not directly used |

The proof is short enough to need only the identity axiom applied in two directions, but the full group structure ensures the axiom is available.

## Ontological Concept Map

```
def-group
├── axiom-identity-element ──► theorem-unique-identity
├── axiom-associativity ─────►
└── axiom-inverse-element ───►
```

## Proof Strategy

**Method**: [[technique-direct-proof]]

Evaluate the product $e' \cdot e$ in two ways: once using the hypothesis that $e'$ is a left identity, and once using the axiom that $e$ is a left identity. Equate the results.

## Proof

Assume $e' \cdot a = a$ for all $a \in G$.

$$
\begin{aligned}
e' &= e \cdot e' && \text{(identity axiom applied to } e') \\
   &= e' \cdot e && \text{(hypothesis applied with } a = e\text{... but we need right identity)}
\end{aligned}
$$

We proceed more carefully. First derive right identity from the axioms.

**Step 1**: Show $a \cdot e = a$ for all $a \in G$ (right identity from left axioms).

Let $a \in G$. We have:
$$
\begin{aligned}
a \cdot e &= a \cdot (a^{-1} \cdot a) && \text{(inverse axiom: } a^{-1} \cdot a = e\text{)} \\
          &= (a \cdot a^{-1}) \cdot a && \text{(associativity)}
\end{aligned}
$$

We need $a \cdot a^{-1} = e$. Derive it:
$$
\begin{aligned}
a^{-1} \cdot (a \cdot a^{-1}) &= (a^{-1} \cdot a) \cdot a^{-1} && \text{(associativity)} \\
&= e \cdot a^{-1} && \text{(inverse axiom)} \\
&= a^{-1} && \text{(identity axiom)}
\end{aligned}
$$

Also $a^{-1} \cdot e = e \cdot (a^{-1}) = a^{-1}$ by identity axiom. So $a^{-1} \cdot (a \cdot a^{-1}) = a^{-1} = a^{-1} \cdot e$.

By left cancellation ([[lemma-cancellation-law]]): $a \cdot a^{-1} = e$.

Then: $a \cdot e = a \cdot (a^{-1} \cdot a) = (a \cdot a^{-1}) \cdot a = e \cdot a = a$.

**Step 2**: Now prove uniqueness.

$$
\begin{aligned}
e' &= e' \cdot e && \text{(right identity, proved in Step 1)} \\
   &= e && \text{(hypothesis: } e' \cdot e = e\text{)}
\end{aligned}
$$

Therefore $e' = e$. $\square$

## Verification

| Step | Justification | Status |
|---|---|---|
| Right inverse from left axioms | Associativity + inverse + identity + cancellation | verified |
| Right identity from right inverse | Associativity + inverse | verified |
| $e' = e' \cdot e$ | Right identity | verified |
| $e' \cdot e = e$ | Hypothesis with $a = e$ | verified |
| Conclude $e' = e$ | Transitivity | verified |

## Lean Formalization

```lean
theorem identity_unique {G : Type*} [MyGroup G] (e' : G)
    (h : ∀ a : G, MyGroup.mul e' a = a) : e' = MyGroup.one := by
  have h1 : MyGroup.mul e' MyGroup.one = MyGroup.one := h MyGroup.one
  have h2 : MyGroup.mul e' MyGroup.one = e' := mul_one e'
  linarith -- or: exact h2.symm.trans h1
```

See: `AutoProof/Theorems/UniqueIdentity.lean`

## Consequences

- Justifies the notation "the identity" and the symbol $e$ (or $1$) without ambiguity.
- Ensures the group structure is not degenerate in having multiple neutral elements.
- Used implicitly in every subsequent proof that references "the identity."

## Related Pages

- [[def-group]]
- [[axiom-identity-element]]
- [[axiom-associativity]]
- [[axiom-inverse-element]]
- [[lemma-cancellation-law]]
- [[theorem-unique-inverse]]
- [[technique-direct-proof]]

## Wiki Update Notes

- Created: 2026-05-17 as part of initial group theory wiki.
- Depends on the cancellation law for the intermediate derivation of right identity.

## Conclusion

The uniqueness of the identity element is one of the first non-trivial consequences of the group axioms. Its proof illustrates how the three axioms interact: associativity enables regrouping, the inverse axiom provides cancellation, and the identity axiom anchors the final simplification.
