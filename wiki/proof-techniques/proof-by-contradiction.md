---
id: technique-contradiction
type: proof-technique
title: "Proof by Contradiction"
status: active
depends_on: []
used_by: []
created_at: 2026-05-17
updated_at: 2026-05-17
---
# Proof by Contradiction

A proof by contradiction (reductio ad absurdum) establishes a statement by showing that its negation leads to a logical impossibility.

## Description

To prove a statement $P$, assume $\neg P$ and derive a contradiction (a statement of the form $Q \land \neg Q$). Since the logical system is consistent, the assumption $\neg P$ must be false, so $P$ holds.

For implications $P \implies Q$: assume $P$ and $\neg Q$, then derive a contradiction.

## When to Use

- The conclusion is an existence or uniqueness statement where direct construction is unclear.
- The negation of the conclusion provides strong structural information to exploit.
- Inequality or non-membership statements where assuming equality/membership leads to contradictions.
- The statement involves "there is no" or "it is impossible that."

## Structure

1. **State what is to be proved**: $P$.
2. **Assume the negation**: Suppose $\neg P$.
3. **Derive consequences**: Using $\neg P$ together with known facts, deduce further statements.
4. **Reach a contradiction**: Arrive at $Q \land \neg Q$ for some proposition $Q$.
5. **Conclude**: Therefore $\neg P$ is false, so $P$ holds. $\square$

## Example

**Claim**: $\sqrt{2}$ is irrational.

**Proof by contradiction**:
1. Suppose $\sqrt{2}$ is rational, i.e., $\sqrt{2} = p/q$ with $\gcd(p,q) = 1$.
2. Then $2q^2 = p^2$, so $p^2$ is even, hence $p$ is even: $p = 2k$.
3. Then $2q^2 = 4k^2$, so $q^2 = 2k^2$, hence $q$ is even.
4. But then $\gcd(p,q) \geq 2$, contradicting $\gcd(p,q) = 1$. $\square$

## Advantages

- Powerful for impossibility and uniqueness results.
- The negation often provides extra hypotheses to work with.
- Natural for non-constructive existence proofs (assume no witness exists, derive contradiction).

## Limitations

- Non-constructive: does not produce a witness or explicit computation.
- Can obscure the "real reason" a theorem is true.
- Harder to formalize in constructive/intuitionistic logic (where excluded middle is not assumed).
- In Lean 4 and similar proof assistants, requires `Classical.byContradiction` or the `omega`/`decide` tactics.

## Lean Encoding

```lean
theorem example_by_contradiction (P : Prop) (h : ¬P → False) : P :=
  Classical.byContradiction (fun hnp => h hnp)
```

## Comparison with Other Techniques

| Technique | Assumes | Derives |
|---|---|---|
| Direct proof | $P$ | $Q$ |
| Contrapositive | $\neg Q$ | $\neg P$ |
| Contradiction | $P \land \neg Q$ (or $\neg P$) | $\bot$ (a contradiction) |

## Related Pages

- [[technique-direct-proof]]
