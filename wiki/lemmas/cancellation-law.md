---
id: lemma-cancellation-law
type: lemma
title: "Left Cancellation Law"
status: proved
formal_status: verified
lean_file: "AutoProof/Lemmas/CancellationLaw.lean"
lean_decl: "left_cancel"
depends_on: ["def-group", "axiom-associativity", "axiom-identity-element", "axiom-inverse-element"]
used_by: ["theorem-unique-identity", "theorem-unique-inverse"]
proof_methods: ["direct-proof"]
created_at: 2026-05-17
updated_at: 2026-05-17
---
# Left Cancellation Law

In any group, left multiplication by a fixed element is injective.

## Statement

Let $(G, \cdot, e, {}^{-1})$ be a group. For all $a, b, c \in G$:
$$a \cdot b = a \cdot c \implies b = c$$

## Informal Meaning

If two products share the same left factor and are equal, then the remaining factors must be equal. This is the group-theoretic analogue of "dividing both sides by $a$."

## Axiomatic Space

This lemma requires the full group structure:
- **Associativity** ([[axiom-associativity]]): to regroup $a^{-1} \cdot (a \cdot b)$ as $(a^{-1} \cdot a) \cdot b$
- **Identity** ([[axiom-identity-element]]): to simplify $e \cdot b = b$
- **Inverse** ([[axiom-inverse-element]]): to obtain $a^{-1} \cdot a = e$

## Ontological Concept Map

```
def-group
├── axiom-associativity ─────┐
├── axiom-identity-element ──┼──► lemma-cancellation-law
└── axiom-inverse-element ───┘
```

## Proof Strategy

**Method**: [[technique-direct-proof]]

Multiply both sides of the hypothesis on the left by $a^{-1}$, then apply associativity, the inverse axiom, and the identity axiom to simplify.

## Proof

Assume $a \cdot b = a \cdot c$. We derive $b = c$:

$$
\begin{aligned}
a \cdot b &= a \cdot c && \text{(hypothesis)} \\
a^{-1} \cdot (a \cdot b) &= a^{-1} \cdot (a \cdot c) && \text{(left-multiply by } a^{-1}\text{)} \\
(a^{-1} \cdot a) \cdot b &= (a^{-1} \cdot a) \cdot c && \text{(associativity)} \\
e \cdot b &= e \cdot c && \text{(inverse axiom)} \\
b &= c && \text{(identity axiom)} \quad \square
\end{aligned}
$$

## Verification

| Step | Justification | Status |
|---|---|---|
| Left-multiply by $a^{-1}$ | Congruence of equality | verified |
| Regroup via associativity | [[axiom-associativity]] | verified |
| Replace $a^{-1} \cdot a$ with $e$ | [[axiom-inverse-element]] | verified |
| Replace $e \cdot x$ with $x$ | [[axiom-identity-element]] | verified |

## Lean Formalization

```lean
theorem left_cancel {G : Type*} [MyGroup G] (a b c : G) 
    (h : MyGroup.mul a b = MyGroup.mul a c) : b = c := by
  have h1 := congr_arg (MyGroup.mul (MyGroup.inv a)) h
  simp [← MyGroup.mul_assoc, MyGroup.inv_mul, MyGroup.one_mul] at h1
  exact h1
```

See: `AutoProof/Lemmas/CancellationLaw.lean`

## Consequences

- Enables [[theorem-unique-identity]]: if $e' \cdot a = a = e \cdot a$, cancel $a$ on the right (or apply left cancellation to the transposed equation).
- Enables [[theorem-unique-inverse]]: if $b \cdot a = e = a^{-1} \cdot a$, use cancellation to conclude $b = a^{-1}$.
- Implies left multiplication $\lambda_a : G \to G$ defined by $\lambda_a(x) = a \cdot x$ is a bijection.

## Related Pages

- [[def-group]]
- [[axiom-associativity]]
- [[axiom-identity-element]]
- [[axiom-inverse-element]]
- [[theorem-unique-identity]]
- [[theorem-unique-inverse]]
- [[technique-direct-proof]]

## Conclusion

The left cancellation law is a foundational lemma that transforms the abstract group axioms into a practical tool for equation solving. It is used pervasively in subsequent proofs, including the uniqueness theorems for identity and inverse elements.
