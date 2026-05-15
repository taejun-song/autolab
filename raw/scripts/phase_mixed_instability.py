"""
Phase-mixed state instability test for the OA equation.

Key question: Can a state with r ≈ 0 but Ψ > 0 persist under OA dynamics?
If NO (r always grows from such states), then the ω-limit set argument closes.

A "phase-mixed" state has oscillators with |α(ω)| > 0 but phases arranged
so that r = ∫α·g ≈ 0. We test whether the OA coupling destabilizes this.

For K > K_c: the dispersion relation at r=0 has an unstable root λ₀ > 0.
This should cause |r| to grow exponentially from any phase-mixed state.
"""
import numpy as np
from scipy.integrate import solve_ivp

def gaussian_g(omega):
    return np.exp(-omega**2 / 2) / np.sqrt(2 * np.pi)

def create_phase_mixed_state(omega_grid, g_vals, rng, amplitude=0.5):
    n = len(omega_grid)
    rho = amplitude * np.ones(n)
    d_omega = omega_grid[1] - omega_grid[0]
    phi = rng.uniform(-np.pi, np.pi, n)
    alpha = rho * np.exp(1j * phi)
    for _ in range(200):
        r = np.sum(alpha * g_vals * d_omega)
        if abs(r) < 1e-12:
            break
        grad = g_vals * d_omega * np.exp(1j * np.angle(alpha))
        alpha -= (r / np.sum(np.abs(grad)**2)) * np.conj(grad)
        alpha = np.clip(np.abs(alpha), 0.01, 0.99) * np.exp(1j * np.angle(alpha))
    alpha_sym = np.zeros_like(alpha)
    for i in range(n // 2):
        j = n - 1 - i
        avg = (alpha[i] + np.conj(alpha[j])) / 2
        alpha_sym[i] = avg
        alpha_sym[j] = np.conj(avg)
    if n % 2 == 1:
        alpha_sym[n // 2] = np.real(alpha[n // 2])
    return alpha_sym

def oa_rhs(t, y, omega_grid, g_vals, d_omega, K):
    N = len(omega_grid)
    alpha = y[:N] + 1j * y[N:]
    r = np.sum(alpha * g_vals * d_omega)
    dadt = -1j * omega_grid * alpha + (K / 2) * (np.conj(r) - r * alpha**2)
    return np.concatenate([np.real(dadt), np.imag(dadt)])

def compute_psi(alpha, g_vals, d_omega):
    abs2 = np.abs(alpha)**2
    abs2 = np.clip(abs2, 0, 1 - 1e-15)
    return np.sum(g_vals * (-np.log(1 - abs2)) * d_omega)

def run_test(K_over_Kc, amplitude=0.5, T=200.0, seed=42):
    n_omega = 300
    omega_max = 6.0
    omega_grid = np.linspace(-omega_max, omega_max, n_omega)
    d_omega = omega_grid[1] - omega_grid[0]
    g_vals = gaussian_g(omega_grid)
    K_c = 2 / (np.pi * gaussian_g(0))
    K = K_over_Kc * K_c
    rng = np.random.default_rng(seed)
    alpha0 = create_phase_mixed_state(omega_grid, g_vals, rng, amplitude)
    r0 = np.sum(alpha0 * g_vals * d_omega)
    psi0 = compute_psi(alpha0, g_vals, d_omega)
    y0 = np.concatenate([np.real(alpha0), np.imag(alpha0)])
    t_eval = np.linspace(0, T, int(T * 10))
    sol = solve_ivp(oa_rhs, [0, T], y0, t_eval=t_eval, method='RK45',
                    args=(omega_grid, g_vals, d_omega, K),
                    rtol=1e-10, atol=1e-12, max_step=0.1)
    rs = np.array([np.abs(np.sum((sol.y[:n_omega, i] + 1j * sol.y[n_omega:, i])
                                  * g_vals * d_omega))
                   for i in range(len(sol.t))])
    psis = np.array([compute_psi(sol.y[:n_omega, i] + 1j * sol.y[n_omega:, i],
                                  g_vals, d_omega)
                     for i in range(len(sol.t))])
    r_max = np.max(rs)
    r_final = np.mean(rs[-20:])
    psi_final = psis[-1]
    r_grew = r_max > 10 * max(abs(r0), 1e-10)
    print(f"  K/Kc={K_over_Kc:.2f}, amp={amplitude:.2f}: "
          f"|r(0)|={abs(r0):.2e}, Ψ(0)={psi0:.3f}, "
          f"|r|_max={r_max:.4f}, |r|_final={r_final:.4f}, "
          f"Ψ_final={psi_final:.3f}, "
          f"grew={'YES' if r_grew else 'no'}")
    return r_grew, sol.t, rs, psis

def dispersion_analysis(K_over_Kc, alpha_bg, omega_grid, g_vals, d_omega):
    """Compute the growth rate from the linearized dispersion relation at a phase-mixed state."""
    K_c = 2 / (np.pi * gaussian_g(0))
    K = K_over_Kc * K_c
    def disp(lam):
        A = np.sum(g_vals * d_omega / (lam + 1j * omega_grid))
        B = np.sum(g_vals * alpha_bg**2 * d_omega / (lam + 1j * omega_grid))
        return 1 - (K / 2) * (A - B)
    from scipy.optimize import brentq
    try:
        def real_disp(x):
            return np.real(disp(x + 0j))
        lam0 = brentq(real_disp, 0.001, 5.0)
        return lam0
    except ValueError:
        return None

if __name__ == '__main__':
    print("=" * 90)
    print("Phase-mixed state instability test")
    print("=" * 90)
    print("\nTest 1: Various K/Kc, fixed amplitude 0.5")
    for K_ratio in [1.01, 1.05, 1.1, 1.2, 1.5, 2.0, 3.0]:
        run_test(K_ratio, amplitude=0.5, T=300.0)
    print("\nTest 2: Various amplitudes, K/Kc = 1.1")
    for amp in [0.1, 0.3, 0.5, 0.7, 0.9]:
        run_test(1.1, amplitude=amp, T=300.0)
    print("\nTest 3: Multiple seeds at weak coupling K/Kc = 1.01")
    grew_count = 0
    total = 10
    for seed in range(total):
        grew, _, _, _ = run_test(1.01, amplitude=0.5, T=500.0, seed=seed)
        if grew:
            grew_count += 1
    print(f"\n  K/Kc=1.01: {grew_count}/{total} trials showed |r| growth")
    print("\nTest 4: Dispersion relation growth rate at incoherence (α=0)")
    n_omega = 300
    omega_grid = np.linspace(-6, 6, n_omega)
    d_omega = omega_grid[1] - omega_grid[0]
    g_vals = gaussian_g(omega_grid)
    for K_ratio in [1.01, 1.1, 1.5, 2.0]:
        alpha_bg = np.zeros(n_omega)
        lam = dispersion_analysis(K_ratio, alpha_bg, omega_grid, g_vals, d_omega)
        if lam is not None:
            print(f"  K/Kc={K_ratio:.2f}, α≡0: λ₀ = {lam:.4f}")
        else:
            print(f"  K/Kc={K_ratio:.2f}, α≡0: no unstable root found")
