---
id: axiom-inverse-element
type: axiom
title: "Inverse Element"
status: accepted
formal_status: verified
lean_file: "AutoProof/Definitions/Group.lean"
lean_decl: "mul_left_inv"
depends_on: ["def-group"]
used_by: ["theorem-unique-inverse", "lemma-cancellation-law"]
created_at: 2026-05-17
updated_at: 2026-05-17
---
# Inverse Element

The inverse axiom guarantees that every element has a left inverse under the group operation.

## Statement

For every $a \in G$, there exists $a^{-1} \in G$ such that:
$$a^{-1} \cdot a = e$$

## Informal Meaning

Every operation can be undone. Given any element $a$, its inverse $a^{-1}$ "cancels" it, returning the system to the identity state. This reversibility is what distinguishes groups from monoids.

## Role in Group Theory

The inverse axiom enables:
- Solving equations: $a \cdot x = b$ has the unique solution $x = a^{-1} \cdot b$
- The cancellation law: if $a \cdot b = a \cdot c$ then $b = c$
- Definition of quotients and cosets

## Note on Left vs Right Inverse

We state the left inverse axiom ($a^{-1} \cdot a = e$). The right inverse property ($a \cdot a^{-1} = e$) is derivable from the left inverse, left identity, and associativity. See [[theorem-unique-inverse]] for the uniqueness proof.

## Lean Formalization

```lean
class MyGroup (G : Type*) where
  ...
  inv_mul : ∀ a : G, mul (inv a) a = one
```

## Related Pages

- [[def-group]]
- [[axiom-identity-element]]
- [[theorem-unique-inverse]]
- [[lemma-cancellation-law]]
