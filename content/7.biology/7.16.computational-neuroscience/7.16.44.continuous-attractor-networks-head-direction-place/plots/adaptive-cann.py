"""Dynamical regimes of a continuous attractor network with spike-frequency adaptation (A-CANN).

Model (Mi, Fung, Wong and Wu, 2014; Formula 44.6.1), N = 256 neurons on a ring [-pi, pi):
  tau du_i/dt   = -u_i + sum_j J_ij r_j - v_i + I_i(t),   r_i = u_i^2 / (1 + k sum_j u_j^2),
  tau_v dv_i/dt = -v_i + m u_i,
J_ij Gaussian with width a = 0.3 (normalized as in cann-bump.py), k = 1, tau = 1, tau_v = 50.
Input: I = alpha exp(-d(x, z(t))^2 / (4 a^2)), z(t) = v_ext t.
Rows (space-time plots of the rate r; dashed line: stimulus position):
A: traveling wave: m = 0.9, alpha = 0.03, stimulus at x = 0 only for t < 30: the bump moves on
   its own at constant speed (intrinsic mobility, m > tau / tau_v).
B: oscillatory tracking: m = 0.334, alpha = 0.2, v_ext = 0.0012: the bump oscillates around
   the slowly moving stimulus, sweeping ahead and back.
C: smooth tracking: m = 0.05, alpha = 0.2, v_ext = 0.004: the bump follows the stimulus.
Right column: displacement of the bump center from the stimulus, z_bump - z(t).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
N, tau, tauv, a, k, dt = 256, 1.0, 50.0, 0.3, 1.0, 0.1
x = -np.pi + 2 * np.pi * np.arange(N) / N
D = np.angle(np.exp(1j * (x[:, None] - x[None, :])))
J = np.exp(-(D**2) / (2 * a**2)) / (np.sqrt(2 * np.pi) * a)


def simulate(m, alpha, vext, T, stim_off=None):
    u = np.zeros(N)
    v = np.zeros(N)
    n = int(T / dt)
    R = np.empty((n // 10, N))
    zb, zs = [], []
    for s in range(n):
        t = s * dt
        z = vext * t
        I = alpha * np.exp(-np.angle(np.exp(1j * (x - z))) ** 2 / (4 * a**2))
        if stim_off is not None and t > stim_off:
            I = 0.0
        u2 = np.maximum(u, 0) ** 2
        r = u2 / (1 + k * u2.sum())
        du = (-u + J @ r - v + I) / tau
        dv = (-v + m * u) / tauv
        u = u + dt * du
        v = v + dt * dv
        if s % 10 == 0:
            R[s // 10] = r
            zb.append(np.angle(np.sum(r * np.exp(1j * x))))
            zs.append(z)
    return R, np.array(zb), np.array(zs)


cases = [
    ("A  Traveling wave", 0.9, 0.03, 0.0, 600.0, 30.0),
    ("B  Oscillatory tracking", 0.334, 0.2, 0.0012, 1400.0, None),
    ("C  Smooth tracking", 0.05, 0.2, 0.004, 1400.0, None),
]
fig, axs = plt.subplots(3, 2, figsize=(12, 8.4), gridspec_kw=dict(width_ratios=[2.2, 1]))
for row, (ttl, m, alpha, vext, T, off) in enumerate(cases):
    R, zb, zs = simulate(m, alpha, vext, T, off)
    t = np.arange(R.shape[0]) * dt * 10
    ax = axs[row, 0]
    ax.imshow(R.T, aspect="auto", origin="lower", extent=(0, T, -np.pi, np.pi), cmap="viridis")
    if off is None:
        ax.plot(t, np.angle(np.exp(1j * zs)), ".", ms=0.6, color="white")
    ax.set_ylabel("x / rad")
    ax.set_title(f"{ttl}  (m = {m}, $\\alpha$ = {alpha})", loc="left", fontsize=10)
    ax2 = axs[row, 1]
    if off is None:
        disp = np.angle(np.exp(1j * (zb - zs)))
        ax2.plot(t, disp, color=P.edge("dna"), lw=1.2)
        ax2.axhline(0, color=P.muted(), lw=0.8)
        ax2.set_ylabel("$z_{\\mathrm{bump}} - z$ / rad")
    else:
        ax2.plot(t, np.unwrap(zb), color=P.edge("dna"), lw=1.5)
        ax2.set_ylabel("Bump position (unwrapped) / rad")
    ax2.grid(True, alpha=0.3)
axs[2, 0].set_xlabel("Time / $\\tau$")
axs[2, 1].set_xlabel("Time / $\\tau$")
fig.tight_layout()
