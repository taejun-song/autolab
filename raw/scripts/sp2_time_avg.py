"""
Time-averaged contraction: does the EFFECTIVE adiabatic constant C_A^eff
(accounting for the low-pass filtering of the Riccati) fall below 1-F'?

For each omega: the Riccati at contraction rate lambda(omega) acts as a
low-pass filter with cutoff lambda. The oscillatory part of dot_r at
frequency omega_osc is attenuated by factor lambda/sqrt(lambda^2+omega_osc^2).

Estimate omega_osc from the autocorrelation of |r(t)|, then compute C_A^eff.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.signal import welch

def gaussian_g(omega):
    return np.exp(-omega**2 / 2) / np.sqrt(2 * np.pi)

def find_r_star(K, omega_grid, g_vals, d_omega):
    r = 0.5
    for _ in range(500):
        u = omega_grid / (K * r + 1e-15)
        locked = np.abs(u) <= 1
        beta = np.zeros_like(u, dtype=complex)
        beta[locked] = -1j * u[locked] + np.sqrt(1 - u[locked]**2 + 0j)
        beta[~locked] = -1j * u[~locked] + 1j * u[~locked] * np.sqrt(1 - u[~locked]**(-2) + 0j)
        r_new = np.real(np.sum(beta * g_vals * d_omega))
        if abs(r_new - r) < 1e-14:
            break
        r = 0.5 * r + 0.5 * r_new
    return r

def oa_rhs(t, alpha_flat, omega_grid, g_vals, d_omega, K):
    N = len(omega_grid)
    alpha = alpha_flat[:N] + 1j * alpha_flat[N:]
    r = np.sum(alpha * g_vals * d_omega)
    dadt = -1j * omega_grid * alpha + (K / 2) * (np.conj(r) - r * alpha**2)
    return np.concatenate([np.real(dadt), np.imag(dadt)])

def enforce_symmetry(alpha, omega_grid):
    N = len(omega_grid)
    result = alpha.copy()
    for i in range(N // 2):
        j = N - 1 - i
        avg = (alpha[i] + np.conj(alpha[j])) / 2
        result[i] = avg
        result[j] = np.conj(avg)
    return result

def compute_contraction_rate(omega, K, r):
    u = abs(omega) / (K * r + 1e-15)
    if u < 1:
        return K * np.sqrt(max(r**2 - omega**2 / K**2, 0))
    else:
        return K**2 * r**2 / (2 * omega**2 + 1e-15)

def run_test(K_over_Kc, T=300.0, seed=42):
    n_omega = 400
    omega_max = 8.0
    rng = np.random.default_rng(seed)
    omega_grid = np.linspace(-omega_max, omega_max, n_omega)
    d_omega = omega_grid[1] - omega_grid[0]
    g_vals = gaussian_g(omega_grid)
    K_c = 2 / (np.pi * gaussian_g(0))
    K = K_over_Kc * K_c
    r_star = find_r_star(K, omega_grid, g_vals, d_omega)

    rho0 = rng.uniform(0.1, 0.9, n_omega)
    phi0 = rng.uniform(-np.pi, np.pi, n_omega)
    alpha0 = rho0 * np.exp(1j * phi0 * 0.5)
    alpha0 = enforce_symmetry(alpha0, omega_grid)
    y0 = np.concatenate([np.real(alpha0), np.imag(alpha0)])

    t_eval = np.linspace(0, T, int(T * 20))
    sol = solve_ivp(oa_rhs, [0, T], y0, t_eval=t_eval, method='RK45',
                    args=(omega_grid, g_vals, d_omega, K),
                    rtol=1e-10, atol=1e-12, max_step=0.05)

    rs = np.array([np.real(np.sum((sol.y[:n_omega, i] + 1j * sol.y[n_omega:, i]) * g_vals * d_omega))
                    for i in range(len(sol.t))])

    # Estimate oscillation frequency from PSD of |r - mean(r)| in last half
    half = len(rs) // 2
    rs_last = rs[half:]
    dt = sol.t[1] - sol.t[0]
    freqs, psd = welch(rs_last - np.mean(rs_last), fs=1/dt, nperseg=min(256, len(rs_last)//2))
    peak_idx = np.argmax(psd[1:]) + 1
    omega_osc = 2 * np.pi * freqs[peak_idx]

    # Compute F'(r*) and instantaneous C_A
    dr = 1e-7
    def F(r):
        u = omega_grid / (K * r + 1e-15)
        locked = np.abs(u) <= 1
        beta = np.zeros_like(u, dtype=complex)
        beta[locked] = -1j * u[locked] + np.sqrt(1 - u[locked]**2 + 0j)
        beta[~locked] = -1j * u[~locked] + 1j * u[~locked] * np.sqrt(1 - u[~locked]**(-2) + 0j)
        return np.real(np.sum(beta * g_vals * d_omega))
    F_prime = (F(r_star + dr) - F(r_star - dr)) / (2 * dr)

    C_A_inst = 0.0
    C_A_avg = 0.0
    for i, omega in enumerate(omega_grid):
        lam = compute_contraction_rate(omega, K, r_star)
        if lam < 1e-10:
            continue
        u1 = omega / (K * (r_star + dr))
        u2 = omega / (K * (r_star - dr))
        def beta_val(u):
            if abs(u) <= 1:
                return -1j * u + np.sqrt(1 - u**2 + 0j)
            else:
                return -1j * u + 1j * u * np.sqrt(1 - u**(-2) + 0j)
        d_alpha = abs(beta_val(u1) - beta_val(u2)) / (2 * dr)
        C_A_inst += g_vals[i] * d_alpha / lam * d_omega
        attenuation = lam / np.sqrt(lam**2 + omega_osc**2)
        C_A_avg += g_vals[i] * d_alpha / lam * attenuation * d_omega

    margin_inst = (1 - F_prime) - C_A_inst
    margin_avg = (1 - F_prime) - C_A_avg

    print(f"K/Kc={K_over_Kc:.2f}: r*={r_star:.4f}, ω_osc={omega_osc:.3f}, "
          f"1-F'={1-F_prime:.4f}, "
          f"C_A={C_A_inst:.4f} (margin {margin_inst:+.4f}), "
          f"C_A^eff={C_A_avg:.4f} (margin {margin_avg:+.4f}) "
          f"{'✓' if margin_avg > 0 else '✗'}")

if __name__ == '__main__':
    print("=" * 90)
    print("Time-averaged contraction: C_A^eff vs 1-F'(r*)")
    print("=" * 90)
    for K_ratio in [1.05, 1.1, 1.2, 1.3, 1.5, 2.0, 3.0]:
        run_test(K_ratio, T=300.0)
