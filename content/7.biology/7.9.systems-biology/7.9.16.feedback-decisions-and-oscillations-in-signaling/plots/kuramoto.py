"""Synchronization in the Kuramoto model with Lorentzian natural frequencies.

N = 2000 phase oscillators, d theta_i/dt = omega_i + K r sin(psi - theta_i) (mean-field form), with
omega_i drawn (seed 0) from a Lorentzian of center 0 and half-width gamma = 0.5, so that the
self-consistency theory gives K_c = 2 gamma = 1 and r = sqrt(1 - K_c/K) above it.
Euler integration, step 0.05, 200 time units from random initial phases; r averaged over the last 80.
A: order parameter r against the coupling K: simulation (points) and theory (line); below K_c the
finite population has r of order N^(-1/2).
B: phases (angle) and natural frequencies (radius, ordered) after the run, for K = 0.6 (incoherent) and
K = 2 (a locked cluster with |omega| < K r plus drifting oscillators).
"""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
N, gam = 2000, 0.5
omega = gam * np.tan(np.pi * (rng.random(N) - 0.5))
theta0 = 2 * np.pi * rng.random(N)
dt, T = 0.05, 200.0


def run(K):
    th = theta0.copy()
    rs = []
    for k in range(int(T / dt)):
        z = np.exp(1j * th).mean()
        r, psi = abs(z), np.angle(z)
        th += dt * (omega + K * r * np.sin(psi - th))
        if k * dt > T - 80:
            rs.append(r)
    return np.mean(rs), th


Ks = np.linspace(0, 4, 21)
res = [run(K) for K in Ks]
fig = plt.figure(figsize=(10, 3.6))
ax = fig.add_axes([0.07, 0.16, 0.38, 0.7])
ax.plot(Ks, [r for r, _ in res], "o", color=charts.line("protein"), ms=4, label="simulation, N = 2000")
Kt = np.linspace(1, 4, 200)
ax.plot(Kt, np.sqrt(1 - 1 / Kt), color=P.ink(), lw=1.5, label="theory, r = sqrt(1 - K_c/K)")
ax.plot([0, 1], [0, 0], color=P.ink(), lw=1.5)
ax.axvline(1, color=P.muted(), lw=0.7, ls=":")
ax.text(1.05, 0.9, "K_c = 2 gamma", fontsize=7, color=P.ink())
ax.set_ylim(0, 1)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "coupling K", "order parameter r")
charts.title(ax, "A  A phase transition to synchrony")
order = np.argsort(np.argsort(np.abs(omega)))
rad = 0.3 + 0.7 * order / N
for j, K in enumerate([0.6, 2.0]):
    pa = fig.add_axes([0.52 + 0.24 * j, 0.12, 0.2, 0.68], projection="polar")
    _, th = run(K)
    r = abs(np.exp(1j * th).mean())
    locked = np.abs(omega) < K * r
    pa.scatter(th[~locked] % (2 * np.pi), rad[~locked], s=2, color=P.muted(), alpha=0.6)
    pa.scatter(th[locked] % (2 * np.pi), rad[locked], s=2, color=charts.line("protein"))
    pa.set_xticks([])
    pa.set_yticks([])
    pa.set_facecolor("none")
    pa.spines["polar"].set_color(P.muted())
    pa.set_title(f"K = {K:g}, r = {r:.2f}", fontsize=8, color=P.ink())
fig.text(0.52, 0.92, "B  Phases (angle); |frequency| rank (radius)", fontsize=8, color=P.ink(), weight="bold")
