---
id: axiom-associativity
type: axiom
title: "Associativity"
status: accepted
formal_status: verified
lean_file: "AutoProof/Definitions/Group.lean"
lean_decl: "mul_assoc"
depends_on: ["def-group"]
used_by: ["theorem-unique-identity", "theorem-unique-inverse", "lemma-cancellation-law"]
created_at: 2026-05-17
updated_at: 2026-05-17
---
# Associativity

The associativity axiom states that the grouping of operations does not affect the result.

## Statement

For all $a, b, c \in G$:
$$(a \cdot b) \cdot c = a \cdot (b \cdot c)$$

## Informal Meaning

When composing three or more elements, parentheses are irrelevant. This allows us to write $a \cdot b \cdot c$ unambiguously. Without associativity, we would need to specify evaluation order, making algebraic manipulation intractable.

## Role in Group Theory

Associativity is the structural backbone of group theory. It enables:
- Chain reasoning: replacing subexpressions freely within longer products
- The cancellation law: multiplying both sides by an inverse requires regrouping
- Well-defined powers $a^n$ without specifying parenthesization

Nearly every group-theoretic proof invokes associativity, often implicitly.

## Lean Formalization

```lean
class MyGroup (G : Type*) where
  mul : G → G → G
  one : G
  inv : G → G
  mul_assoc : ∀ a b c : G, mul (mul a b) c = mul a (mul b c)
```

## Related Pages

- [[def-group]]
- [[lemma-cancellation-law]]
- [[theorem-unique-identity]]
- [[theorem-unique-inverse]]
