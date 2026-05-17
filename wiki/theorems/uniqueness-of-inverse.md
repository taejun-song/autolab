---
id: theorem-unique-inverse
type: theorem
title: "Uniqueness of Inverse"
status: proved
formal_status: verified
lean_file: "AutoProof/Theorems/UniqueInverse.lean"
lean_decl: "unique_inverse"
depends_on: ["def-group", "axiom-associativity", "axiom-identity-element", "axiom-inverse-element", "lemma-cancellation-law"]
used_by: []
proof_methods: ["direct-proof"]
created_at: 2026-05-17
updated_at: 2026-05-17
---
# Uniqueness of Inverse

Every element in a group has exactly one inverse.

## Statement

Let $(G, \cdot, e, {}^{-1})$ be a group. For all $a \in G$, if $b \in G$ satisfies $b \cdot a = e$, then $b = a^{-1}$.

## Informal Meaning

There is only one way to "undo" any given element. If some element $b$ cancels $a$ from the left, then $b$ must be the designated inverse $a^{-1}$. This justifies the notation $a^{-1}$ as a well-defined function of $a$.

## Axiomatic Space

| Axiom/Lemma | Role in this proof |
|---|---|
| [[axiom-inverse-element]] | Provides $a^{-1} \cdot a = e$ |
| [[lemma-cancellation-law]] | From $b \cdot a = a^{-1} \cdot a$, conclude $b = a^{-1}$ (right cancellation variant) |
| [[axiom-associativity]] | Used within the cancellation law |
| [[axiom-identity-element]] | Used within the cancellation law |

## Ontological Concept Map

```
def-group
├── axiom-associativity ─────┐
├── axiom-identity-element ──┼──► lemma-cancellation-law ──┐
├── axiom-inverse-element ───┘                             ├──► theorem-unique-inverse
└── axiom-inverse-element ─────────────────────────────────┘
```

## Proof Strategy

**Method**: [[technique-direct-proof]]

Show that $b \cdot a = e = a^{-1} \cdot a$, then apply right cancellation (which follows from left cancellation in the full group) to conclude $b = a^{-1}$.

## Proof

Assume $b \cdot a = e$.

By the inverse axiom: $a^{-1} \cdot a = e$.

Therefore:
$$b \cdot a = e = a^{-1} \cdot a$$

So $b \cdot a = a^{-1} \cdot a$.

We need right cancellation: if $x \cdot a = y \cdot a$ then $x = y$. This follows by a symmetric argument to [[lemma-cancellation-law]] (multiply on the right by $a^{-1}$, using right inverse which was established in the uniqueness-of-identity proof).

Applying right cancellation:
$$b = a^{-1} \quad \square$$

**Detailed right cancellation derivation** (for completeness):

$$
\begin{aligned}
b \cdot a &= a^{-1} \cdot a && \text{(established above)} \\
(b \cdot a) \cdot a^{-1} &= (a^{-1} \cdot a) \cdot a^{-1} && \text{(right-multiply by } a^{-1}\text{)} \\
b \cdot (a \cdot a^{-1}) &= a^{-1} \cdot (a \cdot a^{-1}) && \text{(associativity)} \\
b \cdot e &= a^{-1} \cdot e && \text{(right inverse: } a \cdot a^{-1} = e\text{)} \\
b &= a^{-1} && \text{(right identity)} \quad \square
\end{aligned}
$$

## Verification

| Step | Justification | Status |
|---|---|---|
| $b \cdot a = e$ | Hypothesis | verified |
| $a^{-1} \cdot a = e$ | [[axiom-inverse-element]] | verified |
| Equate: $b \cdot a = a^{-1} \cdot a$ | Transitivity of equality | verified |
| Right-multiply by $a^{-1}$ | Congruence | verified |
| Associativity regrouping | [[axiom-associativity]] | verified |
| $a \cdot a^{-1} = e$ | Derived right inverse | verified |
| $x \cdot e = x$ | Derived right identity | verified |
| Conclude $b = a^{-1}$ | Simplification | verified |

## Lean Formalization

```lean
theorem inverse_unique {G : Type*} [MyGroup G] (a b : G)
    (h : MyGroup.mul b a = MyGroup.one) : b = MyGroup.inv a := by
  have h1 : MyGroup.mul (MyGroup.inv a) a = MyGroup.one := MyGroup.inv_mul a
  have h2 : MyGroup.mul b a = MyGroup.mul (MyGroup.inv a) a := by rw [h, h1]
  exact right_cancel a b (MyGroup.inv a) h2
```

See: `AutoProof/Theorems/UniqueInverse.lean`

## Consequences

- Justifies writing $a^{-1}$ as "the" inverse rather than "an" inverse.
- Enables the involution property: $(a^{-1})^{-1} = a$ (since $a \cdot a^{-1} = e$ means $a$ is an inverse of $a^{-1}$, and by uniqueness it must be the inverse).
- Foundation for well-defined quotient operations in more advanced algebra.

## Related Pages

- [[def-group]]
- [[axiom-associativity]]
- [[axiom-identity-element]]
- [[axiom-inverse-element]]
- [[lemma-cancellation-law]]
- [[theorem-unique-identity]]
- [[technique-direct-proof]]

## Wiki Update Notes

- Created: 2026-05-17 as part of initial group theory wiki.
- Uses right cancellation, which is the symmetric form of [[lemma-cancellation-law]].

## Conclusion

The uniqueness of inverses completes the basic structural theorems of group theory. Together with [[theorem-unique-identity]], it establishes that the group axioms determine a rigid algebraic structure where identity and inverses are unambiguous. The proof demonstrates the interplay between the cancellation law and the inverse axiom.
