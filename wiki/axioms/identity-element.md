---
id: axiom-identity-element
type: axiom
title: "Identity Element"
status: accepted
formal_status: verified
lean_file: "AutoProof/Definitions/Group.lean"
lean_decl: "mul_left_id"
depends_on: ["def-group"]
used_by: ["theorem-unique-identity", "lemma-cancellation-law"]
created_at: 2026-05-17
updated_at: 2026-05-17
---
# Identity Element

The identity axiom asserts the existence of a neutral element under the group operation.

## Statement

There exists $e \in G$ such that for all $a \in G$:
$$e \cdot a = a$$

## Informal Meaning

The identity element acts as a "do nothing" operation. Composing any element with the identity leaves it unchanged. This provides a baseline from which inverses are defined: the inverse of $a$ is the element that, combined with $a$, yields the identity.

## Role in Group Theory

The identity element:
- Anchors the inverse axiom ($a^{-1} \cdot a = e$)
- Serves as the empty product (the result of composing zero elements)
- Is the unique fixed point of the map $x \mapsto e \cdot x$

## Note on Left vs Right Identity

We state the left identity axiom ($e \cdot a = a$). The right identity ($a \cdot e = a$) is derivable from the left identity together with the inverse axiom and associativity. See [[theorem-unique-identity]] for the proof that the identity is unique.

## Lean Formalization

```lean
class MyGroup (G : Type*) where
  ...
  one_mul : ∀ a : G, mul one a = a
```

## Related Pages

- [[def-group]]
- [[axiom-inverse-element]]
- [[theorem-unique-identity]]
- [[lemma-cancellation-law]]
