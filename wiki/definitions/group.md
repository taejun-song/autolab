---
id: def-group
type: definition
title: "Group"
status: accepted
formal_status: verified
lean_file: "AutoProof/Definitions/Group.lean"
lean_decl: "MyGroup"
depends_on: []
used_by: ["theorem-unique-identity", "theorem-unique-inverse", "lemma-cancellation-law"]
created_at: 2026-05-17
updated_at: 2026-05-17
---
# Group

A group is an algebraic structure consisting of a set equipped with a binary operation satisfying associativity, identity, and inverse axioms.

## Formal Definition

A **group** is a tuple $(G, \cdot, e, {}^{-1})$ where:
- $G$ is a nonempty set
- $\cdot : G \times G \to G$ is a binary operation (closure)
- $e \in G$ is the identity element
- ${}^{-1} : G \to G$ is the inverse map

subject to the axioms below.

## Axioms

| Axiom | Statement | ID |
|---|---|---|
| Associativity | $\forall a, b, c \in G,\ (a \cdot b) \cdot c = a \cdot (b \cdot c)$ | [[axiom-associativity]] |
| Identity | $\forall a \in G,\ e \cdot a = a$ | [[axiom-identity-element]] |
| Inverse | $\forall a \in G,\ a^{-1} \cdot a = e$ | [[axiom-inverse-element]] |

## Informal Meaning

A group captures the notion of symmetry and reversible composition. Every operation can be undone (inverse exists), combining operations in sequence is well-defined regardless of grouping (associativity), and there is a "do nothing" operation (identity).

## Examples

1. **Integers under addition** $(\mathbb{Z}, +, 0, -)$: addition is associative, $0$ is the identity, and $-n$ is the inverse of $n$.
2. **Nonzero reals under multiplication** $(\mathbb{R}^*, \times, 1, {}^{-1})$: multiplication is associative, $1$ is the identity, and $1/x$ is the inverse of $x$.
3. **Symmetric group** $S_n$: permutations of $n$ elements under composition.

## Related Pages

- [[axiom-associativity]]
- [[axiom-identity-element]]
- [[axiom-inverse-element]]
- [[theorem-unique-identity]]
- [[theorem-unique-inverse]]
- [[lemma-cancellation-law]]
