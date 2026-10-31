# Molecular dynamics of a two-dimensional Lennard-Jones fluid (reduced units: epsilon = sigma = m = 1).
# 64 particles at number density 0.6 in a periodic square box, potential truncated and shifted at
# r_c = 2.5. Initial positions on a lattice, velocities drawn for temperature 1.0.
# A: positions at the end of a run and the trajectories of four particles over the last 1000 steps.
# B: deviation of the total energy per particle from its initial value (log scale) over a time of 20 of the velocity Verlet integrator with time steps
#    for the velocity Verlet integrator with dt = 0.002, 0.005 and 0.010, and for the explicit Euler method with dt = 0.002: Verlet fluctuates
#    about a constant value (it is symplectic and time-reversible), the error growing as dt^2, while
#    Euler drifts steadily upward.
# C: instantaneous kinetic temperature in the microcanonical run (Verlet, dt = 0.005) and with a Langevin
#    thermostat (friction 1.0, target T = 0.7; BAOAB splitting): the thermostat drives the system to
#    the target and keeps it there with canonical fluctuations.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
N, rho, rc = 64, 0.6, 2.5
L = np.sqrt(N / rho)
shift = 4 * (rc**-12 - rc**-6)


def forces(x):
    d = x[:, None, :] - x[None, :, :]
    d -= L * np.round(d / L)
    r2 = (d**2).sum(-1)
    np.fill_diagonal(r2, np.inf)
    m = r2 < rc**2
    inv6 = np.where(m, 1 / r2**3, 0.0)
    f = np.where(m, 24 * (2 * inv6**2 - inv6) / r2, 0.0)
    F = (f[:, :, None] * d).sum(1)
    U = 0.5 * np.where(m, 4 * (inv6**2 - inv6) - shift, 0.0).sum()
    return F, U


def init(seed):
    rng = np.random.default_rng(seed)
    g = int(np.sqrt(N))
    a = L / g
    x = np.array([[(i + 0.5) * a, (j + 0.5) * a] for i in range(g) for j in range(g)])
    v = rng.normal(0, 1.0, (N, 2))
    v -= v.mean(0)
    v *= np.sqrt(1.0 * 2 * (N - 1) / (v**2).sum())
    return x, v, rng


def run(dt, steps, method="verlet", gamma=0.0, T=1.0, seed=0, keep=False):
    x, v, rng = init(seed)
    F, U = forces(x)
    E, Tk, traj = [], [], []
    c1 = np.exp(-gamma * dt)
    c2 = np.sqrt((1 - c1**2) * T)
    for s in range(steps):
        if method == "euler":
            x = x + dt * v
            v = v + dt * F
            F, U = forces(x % L)
        else:
            v = v + 0.5 * dt * F
            x = x + 0.5 * dt * v
            if gamma > 0:
                v = c1 * v + c2 * rng.standard_normal(v.shape)
            x = x + 0.5 * dt * v
            F, U = forces(x % L)
            v = v + 0.5 * dt * F
        K = 0.5 * (v**2).sum()
        E.append((K + U) / N)
        Tk.append(K / (N - 1))
        if keep and s >= steps - 1000:
            traj.append(x.copy())
    return np.array(E), np.array(Tk), x % L, np.array(traj)


fig, axs = plt.subplots(1, 3, figsize=(14, 4.2), gridspec_kw={"width_ratios": [1, 1.4, 1.4]})
E5, T5, xf, traj = run(0.005, 4000, keep=True)
ax = axs[0]
ax.scatter(xf[:, 0], xf[:, 1], s=55, color=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.7, zorder=3)
for i, tok in zip((5, 20, 37, 50), ("negative", "dna", "positive", "highlight")):
    tr = traj[:, i, :] % L
    jumps = np.where(np.abs(np.diff(tr, axis=0)).max(1) > L / 2)[0] + 1
    for seg in np.split(tr, jumps):
        ax.plot(seg[:, 0], seg[:, 1], color=charts.line(tok), lw=0.9, zorder=2)
ax.set_xlim(0, L)
ax.set_ylim(0, L)
ax.set_aspect("equal")
ax.set_xticks([])
ax.set_yticks([])
charts.style_axes(ax, None, None, box=True)
charts.title(ax, "A   2D Lennard-Jones fluid")

ax = axs[1]
t_max = 20.0
for dt, tok in ((0.002, "positive"), (0.005, "protein"), (0.010, "dna")):
    steps = int(t_max / dt)
    E, _, _, _ = run(dt, steps) if dt != 0.005 else (E5, None, None, None)
    tt = np.arange(1, len(E) + 1) * dt
    ax.semilogy(tt[: int(t_max / dt)], np.abs(E[: int(t_max / dt)] - E[0]) + 1e-7, color=charts.line(tok), lw=1.0,
            label=f"velocity Verlet, dt = {dt}")
Ee, _, _, _ = run(0.002, int(t_max / 0.002), method="euler")
ax.semilogy(np.arange(1, len(Ee) + 1) * 0.002, np.abs(Ee - Ee[0]) + 1e-7, color=charts.line("negative"), lw=1.2,
        label="explicit Euler, dt = 0.002")
ax.set_ylim(1e-6, 1e2)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "time (reduced units)", "|E(t) − E(0)| per particle")
charts.title(ax, "B   Energy conservation")

ax = axs[2]
_, Tl, _, _ = run(0.005, 4000, gamma=1.0, T=0.7)
tt = np.arange(1, 4001) * 0.005
ax.plot(tt, T5, color=charts.line("neutral"), lw=0.9, label="microcanonical (NVE)")
ax.plot(tt, Tl, color=charts.line("dna"), lw=0.9, label="Langevin thermostat, T = 0.7")
ax.axhline(0.7, color=charts.line("dna"), lw=0.7, ls=":")
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "time (reduced units)", "kinetic temperature")
charts.title(ax, "C   Temperature control")
fig.tight_layout()
