# Morales & Poyato (2019/2023) — On the Trend to Global Equilibrium for Kuramoto Oscillators

Source: arXiv:1908.07657. Published in Ann. Inst. H. Poincare Anal. Non Lineaire 40(3), 631-716, 2023.

## Main Results

Studies convergence to stable equilibrium for the Kuramoto-Sakaguchi equation in the LARGE coupling strength regime (K >> K_c).

### Key ingredients:
1. Entropy production estimate using Otto's Riemannian formalism on probability measures
2. Quantitative instability of equilibria with antipodal oscillators
3. Generalized local log-Sobolev and Talagrand inequalities
4. Coupled differential inequalities (Desvillettes-Villani methods)

### Distance metric:
Fibered transportation distance (since K-S equation lacks Wasserstein gradient flow structure).

### Relevance to r-stays-positive:
The paper works in the LARGE coupling regime. For large K, the order parameter r(t) is automatically bounded below because the coupling is strong enough to keep oscillators synchronized. The difficulty is at K slightly above K_c where the synchronization is marginal.

The entropy methods here may be adaptable: if V(t) = int (alpha - alpha*)^2 g dw is an entropy-like functional, the entropy production d/dt V controls convergence. The key question is whether the entropy production has a spectral gap (positive lower bound proportional to V) — this is the "body pair coercivity" in the Lean formalization.

## Connection to r-stays-positive gap

For the r-stays-positive problem at K close to K_c:
- Large coupling results don't directly apply
- But the entropy production framework suggests:
  If V'(t) <= -c(K)*V(t) + perturbation, then V(t) -> 0 exponentially
  This gives r(t) -> r* (not just r stays positive)
- The perturbation comes from the tail (high-frequency oscillators)
- For the body (bounded gamma), the spectral gap c(K) > 0 exists

The paper's innovation is quantitative convergence RATES, which could help with the passage-to-limit strategy (Strategy E in continuum-stability-debate).
