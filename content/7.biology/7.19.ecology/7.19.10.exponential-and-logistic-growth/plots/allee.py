"""Allee effects (Section 10.3.2), dimensionless: x = N/K, tau = r t, a = A/K.

Model dx/dtau = x (1 - x)(x - a): strong Allee effect for 0 < a < 1, weak for -1 < a < 0; the logistic is
dx/dtau = x (1 - x). Per capita growth g(x) = (1 - x)(x - a).
A: per capita growth rate for the logistic, a weak (a = -0.5)
and a strong (a = 0.25) Allee effect. B: solutions of the strong case from x0 = 0.05 ... 0.6.
C: bifurcation diagram with an added per capita mortality m: dx/dtau = x [g(x) - m]; equilibria satisfy
g(x) = m, giving x = [(1 + a) +- sqrt((1 - a)^2 - 4 m)] / 2; solid = stable, dashed = unstable;
x = 0 is stable for all m in the strong case, for m > 0.5 in the weak case and for m > 1 in the logistic.
Logistic: the positive equilibrium 1 - m meets 0 at m = 1 (transcritical). Strong (a = 0.25): saddle-node at
m_c = (1 - a)^2/4 = 0.1406. Weak (a = -0.5): transcritical at m = -a = 0.5, saddle-node at m_c = 0.5625.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
cs, cw, cl = C.line("negative"), C.line("rna"), C.line("dna")

fig, axes = plt.subplots(1, 3, figsize=(12.8, 3.9))
ax = axes[0]
x = np.linspace(0, 1.1, 300)
ax.plot(x, 1 - x, color=cl, lw=2, label="logistic, 1 − x")
ax.plot(x, (1 - x) * (x + 0.5), color=cw, lw=2, label="weak Allee, a = −0.5")
ax.plot(x, (1 - x) * (x - 0.25), color=cs, lw=2, label="strong Allee, a = 0.25")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.plot([0.25], [0], "o", ms=6, mfc=P.surface(), mec=cs)
ax.text(0.27, -0.06, "threshold a", fontsize=FS["tiny"], color=cs)
ax.set_ylim(-0.32, 1.05)
C.style_axes(ax, "x = N / K", "per capita growth rate")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "A  Per capita growth")

ax = axes[1]
a = 0.25
for x0 in (0.05, 0.12, 0.2, 0.24, 0.26, 0.3, 0.4, 0.6):
    s = solve_ivp(lambda t, y: y * (1 - y) * (y - a), (0, 40), [x0], max_step=0.1)
    ax.plot(s.t, s.y[0], color=cs if x0 > a else P.muted(), lw=1.5)
ax.axhline(a, color=cs, lw=0.8, ls=(0, (3, 2)))
ax.text(40, a + 0.02, "threshold", fontsize=FS["tiny"], color=cs, ha="right")
ax.set_ylim(0, 1.05)
ax.set_xlim(0, 40)
C.style_axes(ax, "τ = rt", "x = N / K")
C.title(ax, "B  Strong Allee effect: bistability")

ax = axes[2]
m = np.linspace(0, 1.05, 600)
ax.plot(m, np.clip(1 - m, 0, None), color=cl, lw=2, label="logistic")
ax.plot(m[m > 1], 0 * m[m > 1], color=cl, lw=2)
ax.plot(m[m < 1], 0 * m[m < 1], color=cl, lw=1.2, ls=(0, (3, 2)))
for a, col, name in ((-0.5, cw, "weak"), (0.25, cs, "strong")):
    mc = (1 - a) ** 2 / 4
    mm = np.linspace(0, mc, 400)
    disc = np.sqrt(np.clip((1 - a) ** 2 - 4 * mm, 0, None))
    up, lo = ((1 + a) + disc) / 2, ((1 + a) - disc) / 2
    ax.plot(mm, up, color=col, lw=2, label=f"{name} Allee (a = {a:g})")
    keep = lo > 0
    ax.plot(mm[keep], lo[keep], color=col, lw=1.4, ls=(0, (3, 2)))
    ax.plot([mc], [(1 + a) / 2], "o", color=col, ms=5)
    ax.annotate("", ((mc + 0.02), 0.03), (mc, (1 + a) / 2 - 0.04),
                arrowprops=dict(arrowstyle="-|>", color=col, lw=0.9, ls="--"))
ax.plot(m[m >= 0.5], 0 * m[m >= 0.5], color=cw, lw=2)
ax.plot(m, 0 * m, color=cs, lw=1.2)
ax.text(0.155, 0.6, "saddle-node:\ncollapse", fontsize=FS["tiny"], color=cs)
ax.set_xlim(0, 1.05)
ax.set_ylim(-0.04, 1.05)
C.style_axes(ax, "added mortality m (units of r)", "equilibrium x*")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "C  Bifurcation diagram")
fig.tight_layout()
