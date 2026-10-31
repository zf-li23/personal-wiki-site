"""The genetic toggle switch in dimensionless form, du/dt = -u + alpha/(1 + v^n),
dv/dt = -v + alpha/(1 + u^n), with n = 2. A, B: nullclines (du/dt = 0 blue, dv/dt = 0 red), the
flow field and trajectories for alpha = 1 (one stable state with u = v) and alpha = 3 (two stable
states, one with u high and one with v high, separated by an unstable saddle on the diagonal; the
diagonal is the separatrix). C: fixed points against alpha: the symmetric state loses stability at
alpha = 2 in a pitchfork bifurcation, where the two asymmetric states appear; with unequal
promoters (alpha_v = 0.8 alpha_u, thin lines) the pitchfork unfolds into a saddle-node bifurcation."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts

P = bio.P
n = 2


def field(u, v, a, av=None):
    av = a if av is None else av
    return -u + a / (1 + v ** n), -v + av / (1 + u ** n)


def fixed_points(a, av=None):
    av = a if av is None else av
    u = np.linspace(0, a + 1e-9, 200001)
    v = av / (1 + u ** n)
    g = -u + a / (1 + v ** n)
    idx = np.where(np.sign(g[1:]) != np.sign(g[:-1]))[0]
    out = []
    for i in idx:
        uu = u[i] - g[i] * (u[i + 1] - u[i]) / (g[i + 1] - g[i])
        vv = av / (1 + uu ** n)
        J = np.array([[-1, -a * n * vv ** (n - 1) / (1 + vv ** n) ** 2],
                      [-av * n * uu ** (n - 1) / (1 + uu ** n) ** 2, -1]])
        out.append((uu, vv, np.all(np.linalg.eigvals(J).real < 0)))
    return out


fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.4))
fig.subplots_adjust(wspace=0.32, left=0.06, right=0.98, bottom=0.16, top=0.88)
for ax, a, lab in ((axs[0], 1.0, "A"), (axs[1], 3.0, "B")):
    L = 3.4
    g = np.linspace(0, L, 15)
    U, V = np.meshgrid(g, g)
    du, dv = field(U, V, a)
    ax.quiver(U, V, du, dv, color=P.muted(), angles="xy", width=0.004, headwidth=3.5, scale=25)
    s = np.linspace(0, L, 300)
    ax.plot(a / (1 + s ** n), s, color=charts.line("dna"), lw=1.6, label="du/dt = 0")
    ax.plot(s, a / (1 + s ** n), color=charts.line("blood"), lw=1.6, label="dv/dt = 0")
    for u0, v0 in ((0.2, 3.2), (3.2, 0.3), (0.1, 0.4), (2.8, 3.2), (1.5, 1.6), (0.4, 0.1)):
        sol = solve_ivp(lambda t, y: field(y[0], y[1], a), (0, 15), [u0, v0], max_step=0.05)
        ax.plot(sol.y[0], sol.y[1], color=charts.line("protein"), lw=0.8)
    for uu, vv, st in fixed_points(a):
        ax.plot(uu, vv, "o", ms=6, mfc=P.ink() if st else P.surface(), mec=P.ink(), zorder=5)
    ax.set_xlim(0, L)
    ax.set_ylim(0, L)
    ax.set_aspect("equal")
    if lab == "A":
        ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
    charts.style_axes(ax, "repressor 1, u", "repressor 2, v")
    charts.title(ax, f"{lab}  α = {a:g}")

ax = axs[2]
As = np.linspace(0.3, 5, 300)
for av_ratio, lw, ms in ((1.0, 1.6, 1.8), (0.8, 0.8, 0.8)):
    for a in As:
        for uu, vv, st in fixed_points(a, av_ratio * a):
            ax.plot(a, uu, ".", ms=ms, color=charts.line("protein") if st else P.muted())
ax.axvline(2, color=P.muted(), lw=0.6, ls=":")
ax.text(2.05, 4.3, "α = 2", fontsize=bio.core.FONT["tiny"], color=P.ink())
charts.style_axes(ax, "α", "u at fixed points")
charts.title(ax, "C  Pitchfork bifurcation")
