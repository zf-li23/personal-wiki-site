"""Stability regions of three modified Nicholson-Bailey models (Section 27.3), computed from the
eigenvalues of the linearized map at the coexistence equilibrium (stable where both lie inside the
unit circle).
A: host density dependence (Beddington, Free and Lawton 1975): H' = H exp[r (1 - H/K) - aP],
P' = c H (1 - exp(-aP)); axes: host growth rate r and depression ratio q = H*/K.
B: mutual interference (Hassell and Varley 1969): searching efficiency a = Q P^(-m); axes: host rate
of increase lam and interference constant m.
C: a refuge protecting a constant proportion beta of hosts: H' = lam H [beta + (1 - beta) exp(-aP)];
coexistence requires beta lam < 1 (hatched above).
"""

import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT


def rho(F, z, eps=1e-6):
    z = np.asarray(z, float)
    J = np.zeros((2, 2))
    for j in range(2):
        dz = np.zeros(2)
        dz[j] = eps * max(1.0, abs(z[j]))
        J[:, j] = (np.array(F(z + dz)) - np.array(F(z - dz))) / (2 * dz[j])
    return np.abs(np.linalg.eigvals(J)).max()


def bed(r, q):
    Ps = r * (1 - q)
    c = Ps / (q * (1 - np.exp(-Ps)))
    return rho(lambda z: [z[0] * np.exp(r * (1 - z[0]) - z[1]), c * z[0] * (1 - np.exp(-z[1]))], [q, Ps])


def hv(lam, m):
    Ps = np.log(lam) ** (1 / (1 - m))
    Hs = lam * Ps / (lam - 1)
    return rho(lambda z: [lam * z[0] * np.exp(-max(z[1], 1e-12) ** (1 - m)),
                          z[0] * (1 - np.exp(-max(z[1], 1e-12) ** (1 - m)))], [Hs, Ps])


def ref(lam, b):
    e = (1 / lam - b) / (1 - b)
    Ps = -np.log(e)
    Hs = Ps / ((1 - b) * (1 - e))
    return rho(lambda z: [lam * z[0] * (b + (1 - b) * np.exp(-z[1])), z[0] * (1 - b) * (1 - np.exp(-z[1]))], [Hs, Ps])


def panel(ax, xs, ys, fun, valid=lambda x, y: True):
    Z = np.full((ys.size, xs.size), np.nan)
    for i, y in enumerate(ys):
        for j, x in enumerate(xs):
            if valid(x, y):
                Z[i, j] = 1.0 if fun(x, y) < 1 else 0.0
    ax.contourf(xs, ys, Z, levels=[-0.5, 0.5, 1.5], colors=[P.light("negative"), P.light("positive")])
    ax.contour(xs, ys, Z, levels=[0.5], colors=[P.ink()], linewidths=0.9)


fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.3))
ax = axes[0]
panel(ax, np.linspace(0.02, 0.98, 80), np.linspace(0.1, 3.5, 70), lambda q, r: bed(r, q))
ax.text(0.2, 2.0, "unstable", fontsize=FS["small"], color=P.on_fill())
ax.text(0.72, 1.0, "stable", fontsize=FS["small"], color=P.on_fill(), ha="center")
C.style_axes(ax, "Host depression q = H*/K", "Host growth rate r")
C.title(ax, "A  Host density dependence")

ax = axes[1]
panel(ax, np.linspace(1.05, 20, 80), np.linspace(0.02, 0.95, 70), lambda L, m: hv(L, m))
ax.text(14, 0.2, "unstable", fontsize=FS["small"], color=P.on_fill(), ha="center")
ax.text(5, 0.8, "stable", fontsize=FS["small"], color=P.on_fill(), ha="center")
C.style_axes(ax, "Host rate of increase λ", "Interference constant m")
C.title(ax, "B  Mutual interference (Hassell–Varley)")

ax = axes[2]
Ls = np.linspace(1.05, 10, 80)
bs = np.linspace(0.005, 0.9, 80)
panel(ax, Ls, bs, lambda L, b: ref(L, b), valid=lambda L, b: b * L < 1)
ax.fill_between(Ls, 1 / Ls, 0.9, color=P.light("neutral"), lw=0)
ax.plot(Ls, 1 / Ls, color=P.ink(), lw=0.9, ls=(0, (3, 2)))
ax.text(6, 0.5, "βλ > 1: hosts escape\ncontrol entirely", fontsize=FS["tiny"], color=P.on_fill(), ha="center")
ax.text(7.5, 0.03, "unstable", fontsize=FS["small"], color=P.on_fill(), ha="center")
ax.set_ylim(0.005, 0.9)
C.style_axes(ax, "Host rate of increase λ", "Proportion in refuge β")
C.title(ax, "C  Proportional refuge")
fig.tight_layout()
