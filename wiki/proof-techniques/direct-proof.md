---
id: technique-direct-proof
type: proof-technique
title: "Direct Proof"
status: active
depends_on: []
used_by: ["theorem-unique-identity", "theorem-unique-inverse", "lemma-cancellation-law"]
created_at: 2026-05-17
updated_at: 2026-05-17
---
# Direct Proof

A direct proof establishes a statement by a forward chain of logical deductions from hypotheses and axioms to the conclusion.

## Description

In a direct proof of an implication $P \implies Q$, one assumes $P$ and derives $Q$ through a sequence of justified steps. Each step follows from the hypotheses, previously established facts, definitions, or axioms by a recognized rule of inference.

## When to Use

- The conclusion follows naturally from the hypotheses by algebraic manipulation or logical chaining.
- The statement has the form "if $P$ then $Q$" where $Q$ can be reached by applying known rules to $P$.
- The problem admits a constructive argument (no need to reason about what would happen if the conclusion failed).

## Structure

1. **State the hypothesis**: Assume $P$.
2. **Chain of deductions**: Apply axioms, lemmas, and definitions step by step.
3. **Arrive at conclusion**: The final step yields $Q$.

## Example

**Claim**: In a group, if $a \cdot b = a \cdot c$ then $b = c$ (left cancellation).

**Direct proof**:
1. Assume $a \cdot b = a \cdot c$.
2. Left-multiply both sides by $a^{-1}$.
3. Apply associativity: $(a^{-1} \cdot a) \cdot b = (a^{-1} \cdot a) \cdot c$.
4. Apply inverse axiom: $e \cdot b = e \cdot c$.
5. Apply identity axiom: $b = c$. $\square$

See [[lemma-cancellation-law]] for the full treatment.

## Advantages

- Transparent: every step is explicit and verifiable.
- Constructive: provides a witness or computation path when applicable.
- Mechanizable: direct proofs translate naturally to formal proof assistants (Lean, Coq, Isabelle).

## Limitations

- Not always feasible: some statements are easier to prove by contradiction or contrapositive.
- Can become long if many case splits are needed (though each branch is still "direct").
- Requires insight into which manipulations will lead to the goal.

## Comparison with Other Techniques

| Technique | Assumes | Derives |
|---|---|---|
| Direct proof | $P$ | $Q$ |
| Contrapositive | $\neg Q$ | $\neg P$ |
| Contradiction | $P \land \neg Q$ | a contradiction |

## Related Pages

- [[technique-contradiction]]
- [[lemma-cancellation-law]]
- [[theorem-unique-identity]]
- [[theorem-unique-inverse]]
