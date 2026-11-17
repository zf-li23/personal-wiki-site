"""Predator-mediated coexistence of two competing prey (Section 26.3), dimensionless model
u1' = u1 (1 - u1 - a u2 - v), u2' = rho u2 (1 - u2 - b u1 - kappa v), v' = v (-d + e1 u1 + e2 u2),
with a = 0.5, b = 1.5 (prey 1 excludes prey 2 without the predator), rho = 1, e1 = 1, e2 = 0.2:
the predator prefers and profits more from prey 1; kappa = c2/c1 is its relative attack on prey 2.
A: time series for kappa = 0.3 and d = 0.1, 0.35 and 0.8 (predator mortality): prey 1 excluded,
all three coexist, prey 2 excluded. B: outcomes in the (d, kappa) plane from simulations on a coarse
grid (colours), with the invasion boundaries of Proposition 26.3.1: prey 2 invades the prey 1 -
predator system left of the solid line, prey 1 invades the prey 2 - predator system right of the
dashed line; the predator cannot persist on prey 1 for d > e1 (dotted).
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
a, b, rho, e1, e2 = 0.5, 1.5, 1.0, 1.0, 0.2
col1, col2, colv = C.line("dna"), C.line("positive"), C.line("negative")


def rhs(t, z, d, kap):
    u1, u2, v = z
    return [u1 * (1 - u1 - a * u2 - v), rho * u2 * (1 - u2 - b * u1 - kap * v), v * (-d + e1 * u1 + e2 * u2)]


def sim(d, kap, T):
    return solve_ivp(rhs, [0, T], [0.3, 0.3, 0.1], args=(d, kap), method="LSODA", rtol=1e-7, atol=1e-10,
                     dense_output=True)


fig = plt.figure(figsize=(13.5, 5.0))
gs = fig.add_gridspec(3, 2, width_ratios=[1.3, 1])
for i, d in enumerate([0.1, 0.35, 0.8]):
    ax = fig.add_subplot(gs[i, 0])
    s = sim(d, 0.3, 300)
    t = np.linspace(0, 300, 1500)
    u1, u2, v = s.sol(t)
    ax.plot(t, u1, color=col1, lw=1.2, label="prey 1 (superior competitor)")
    ax.plot(t, u2, color=col2, lw=1.2, label="prey 2")
    ax.plot(t, v, color=colv, lw=1.2, label="predator")
    ax.set_ylim(0, 1.8)
    ax.text(298, 1.5, f"d = {d}", ha="right", fontsize=FS["tiny"], color=P.ink())
    C.style_axes(ax, "Time" if i == 2 else None, "Density")
    if i == 0:
        ax.legend(fontsize=FS["tiny"], frameon=False, ncol=3, loc="upper left", bbox_to_anchor=(0, 1.35))
        C.title(ax, "A  Outcome depends on predator mortality (κ = 0.3)")

ax = fig.add_subplot(gs[:, 1])
ds = np.linspace(0.02, 1.2, 30)
ks = np.linspace(0.05, 0.95, 19)
cmap = {0: P.light("neutral"), 1: P.light("dna"), 2: P.light("highlight"), 3: P.light("positive")}
for kap in ks:
    for d in ds:
        y = sim(d, kap, 800).y[:, -1]
        alive = y > 1e-4
        o = 2 if alive.all() else 1 if (alive[0] and alive[2]) else 3 if (alive[1] and alive[2]) else 0
        ax.add_patch(plt.Rectangle((d - 0.0203, kap - 0.025), 0.0407, 0.05, color=cmap[o], lw=0))
kk = np.linspace(0.05, 0.95, 200)
ax.plot(e1 * (1 - kk) / (b - kk), kk, color=P.ink(), lw=1.3)
ax.plot(e2 * (1 - kk) / (1 - a * kk), kk, color=P.ink(), lw=1.3, ls=(0, (4, 2)))
ax.axvline(e1, color=P.ink(), ls=(0, (1, 2)), lw=1.3)
ax.text(0.03, 0.45, "prey 2\n+ predator", fontsize=FS["tiny"], color=P.on_fill())
ax.text(0.27, 0.10, "all three", fontsize=FS["tiny"], color=P.on_fill())
ax.text(0.62, 0.45, "prey 1\n+ predator", fontsize=FS["tiny"], color=P.on_fill())
ax.text(1.03, 0.45, "prey 1\nalone", fontsize=FS["tiny"], color=P.on_fill())
ax.set_xlim(0, 1.2)
ax.set_ylim(0.025, 0.975)
C.style_axes(ax, "Predator mortality d", "Relative attack on prey 2, κ")
C.title(ax, "B  Long-term outcome")
fig.tight_layout()
