"""Transition to chaos in a random rate network (Sompolinsky, Crisanti and Sommers, 1988).

tau dx_i/dt = -x_i + g sum_j J_ij tanh(x_j),  J_ij ~ N(0, 1/N),  N = 400, tau = 10 ms,
Euler step 0.05 tau, random initial condition.
A: activities tanh(x_i) of 5 units for g = 0.8: decay to the silent fixed point.
B: the same for g = 1.5: irregular, self-sustained fluctuations.
C: largest Lyapunov exponent against g (Benettin's method: an infinitesimal perturbation is evolved
   alongside and renormalized every step), with the linear prediction (g - 1)/tau for g < 1.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
N, tau, dt = 400, 10.0, 0.5
J0 = rng.normal(0, 1 / np.sqrt(N), (N, N))
x0 = rng.normal(0, 1, N)


def traj(g, T=400.0):
    x = x0.copy()
    out = []
    for k in range(int(T / dt)):
        out.append(np.tanh(x[:5]))
        x = x + dt / tau * (-x + g * J0 @ np.tanh(x))
    return np.arange(len(out)) * dt, np.array(out)


def lyap(g, T=1500.0, Tt=300.0):
    x = x0.copy()
    v = rng.normal(0, 1, N)
    v /= np.linalg.norm(v)
    s, cnt = 0.0, 0
    for k in range(int(T / dt)):
        th = np.tanh(x)
        Jv = g * J0 @ ((1 - th**2) * v)
        x = x + dt / tau * (-x + g * J0 @ th)
        v = v + dt / tau * (-v + Jv)
        nv = np.linalg.norm(v)
        v /= nv
        if k * dt > Tt:
            s += np.log(nv)
            cnt += 1
    return s / (cnt * dt) * 1000  # per second


fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
cols = [P.edge("dna"), P.edge("negative"), P.edge("positive"), P.edge("rna"), P.edge("protein")]
for ax, g, ttl in ((axs[0], 0.8, "A  $g$ = 0.8: decay"), (axs[1], 1.5, "B  $g$ = 1.5: chaos")):
    t, r = traj(g)
    for k in range(5):
        ax.plot(t, r[:, k], color=cols[k], lw=1.2)
    ax.set_ylim(-1.05, 1.05)
    ax.set_xlabel("Time / ms")
    ax.set_ylabel("Rate $\\tanh(x_i)$")
    ax.set_title(ttl, loc="left", fontsize=10)
ax = axs[2]
gs = np.array([0.5, 0.7, 0.9, 1.0, 1.1, 1.2, 1.4, 1.6, 1.8, 2.0])
ls = np.array([lyap(g) for g in gs])
ax.plot(gs, ls, "o-", color=P.edge("dna"), lw=1.6, ms=4, label="simulation")
gg = np.linspace(0.45, 1.0, 20)
ax.plot(gg, (gg - 1) / tau * 1000, color=P.muted(), ls="--", lw=1.2, label="$(g - 1)/\\tau$")
ax.axhline(0, color=P.ink(), lw=0.8)
ax.axvline(1, color=P.muted(), lw=0.8, ls=":")
ax.set_xlabel("Gain $g$")
ax.set_ylabel("Largest Lyapunov exponent / s$^{-1}$")
ax.set_title("C  Transition at $g$ = 1", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")
for a_ in axs:
    a_.grid(True, alpha=0.3)
fig.tight_layout()
