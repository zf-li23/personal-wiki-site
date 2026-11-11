"""A one-dimensional continuous attractor network (CANN) on a ring.

Model (Wu, Amari and colleagues; Formula 44.2.1), discretized on N = 256 neurons with preferred
stimuli x_i in [-pi, pi):
  tau du_i/dt = -u_i + sum_j J_ij r_j + I_i(t),   r_i = u_i^2 / (1 + k sum_j u_j^2),
  J_ij = exp(-d(x_i, x_j)^2 / (2 a^2)) / (sqrt(2 pi) a),  d = distance on the ring,
with tau = 1 (time unit), a = 0.3, k = 1 (the density rho dx = 1 is absorbed in J and k).
Input I = alpha exp(-d(x, z(t))^2 / (4 a^2)).
A: space-time plot of r: a stimulus at x = 0 (alpha = 0.5) is on for 0 < t < 50 and then
   removed: the bump persists; from t = 150 a weak stimulus (alpha = 0.1) appears at x = -1.5
   and moves at speed 0.01 per time unit; the bump jumps to it and tracks it (dashed line).
B: the stationary bump after the input is removed (dots) and the theoretical profile
   r0 exp(-x^2 / (2 a^2)) with the analytical amplitude (line; Eq. (44.3)).
C: path integration: adding an asymmetric component -gamma * dJ/dx to the weights (a rotation
   signal of strength gamma) makes the bump move without input at a speed proportional to
   gamma.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
N, tau, a, k, dt = 256, 1.0, 0.3, 1.0, 0.1
x = -np.pi + 2 * np.pi * np.arange(N) / N
D = np.angle(np.exp(1j * (x[:, None] - x[None, :])))
J = np.exp(-(D**2) / (2 * a**2)) / (np.sqrt(2 * np.pi) * a)
dJ = -D / a**2 * J  # derivative of the kernel with respect to x_i - x_j


def ring(z):
    return np.angle(np.exp(1j * (x - z)))


def center(u):
    return np.angle(np.sum(np.maximum(u, 0) * np.exp(1j * x)))


def rate(u):
    u2 = np.maximum(u, 0) ** 2
    return u2 / (1 + k * u2.sum())


def run(T, stim, W=J, u=None):
    n = int(T / dt)
    u = np.zeros(N) if u is None else u
    R = np.empty((n, N))
    for s in range(n):
        t = s * dt
        I = stim(t)
        u = u + dt / tau * (-u + W @ rate(u) + I)
        R[s] = rate(u)
    return u, R


def stim_A(t):
    if t < 50:
        return 0.5 * np.exp(-ring(0.0) ** 2 / (4 * a**2))
    if t >= 150:
        z = -1.5 + 0.01 * (t - 150)
        return 0.1 * np.exp(-ring(z) ** 2 / (4 * a**2))
    return 0.0


u, R = run(450, stim_A)
fig, axs = plt.subplots(1, 3, figsize=(13, 3.9), gridspec_kw=dict(width_ratios=[1.6, 1, 1]))
ax = axs[0]
T = np.arange(R.shape[0]) * dt
ax.imshow(R[::10].T, aspect="auto", origin="lower", extent=(0, 450, -np.pi, np.pi), cmap="viridis")
tt = np.linspace(150, 450, 50)
ax.plot(tt, np.angle(np.exp(1j * (-1.5 + 0.01 * (tt - 150)))), ls="--", color="white", lw=1.2)
ax.axvline(50, color="white", lw=0.8, ls=":")
ax.text(5, 2.6, "cue on", color="white", fontsize=8)
ax.text(60, 2.6, "cue off: bump persists", color="white", fontsize=8)
ax.text(160, -2.9, "moving cue: tracking", color="white", fontsize=8)
ax.set_xlabel("Time / $\\tau$")
ax.set_ylabel("Preferred stimulus x / rad")
ax.set_title("A  Persistence and tracking", loc="left", fontsize=10)

# stationary bump at t = 140 (no input)
_, R2 = run(140, lambda t: 0.5 * np.exp(-ring(0.0) ** 2 / (4 * a**2)) if t < 50 else 0.0)
dx = 2 * np.pi / N
# Eq. (44.3) in the discrete normalization: u = U0 exp(-x^2/4a^2), r = r0 exp(-x^2/2a^2),
# with c = sqrt(2 pi) a / dx, U0 = [1 + sqrt(1 - 8 k c dx^2)] / (2 sqrt(2) k c dx), r0 = sqrt(2) dx U0
c = np.sqrt(2 * np.pi) * a / dx
U0 = (1 + np.sqrt(1 - 8 * k * c * dx**2)) / (2 * np.sqrt(2) * k * c * dx)
r0 = np.sqrt(2) * dx * U0
ax = axs[1]
ax.plot(x, R2[-1], "o", ms=3, color=P.edge("dna"), label="Simulation")
ax.plot(x, r0 * np.exp(-(x**2) / (2 * a**2)), color=P.edge("negative"), lw=1.8, label="Theory")
ax.set_xlim(-1.5, 1.5)
ax.set_xlabel("x / rad")
ax.set_ylabel("Rate r (a.u.)")
ax.set_title("B  Stationary bump", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)

ax = axs[2]
gams = np.linspace(-0.004, 0.004, 9)
speeds = []
u0 = run(60, lambda t: 0.5 * np.exp(-ring(0.0) ** 2 / (4 * a**2)) if t < 50 else 0.0)[0]
for g in gams:
    W = J - g * dJ
    uu, RR = run(100, lambda t: 0.0, W=W, u=u0.copy())
    zs = np.unwrap([center(r) for r in RR[::10]])
    speeds.append((zs[-1] - zs[len(zs) // 2]) / (50.0))
ax.plot(gams, speeds, "o-", color=P.edge("dna"), lw=1.8)
ax.axhline(0, color=P.muted(), lw=0.8)
ax.set_xlabel("Rotation signal $\\gamma$")
ax.set_ylabel("Bump speed / (rad per $\\tau$)")
ax.set_title("C  Path integration", loc="left", fontsize=10)
for a_ in axs[1:]:
    a_.grid(True, alpha=0.3)
fig.tight_layout()
