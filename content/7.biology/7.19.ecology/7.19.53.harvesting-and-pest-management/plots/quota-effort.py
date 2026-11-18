"""Fixed-quota and fixed-effort harvesting of a logistic population (Section 53.1), dimensionless.

x = N/K, tau = r t. Quota: dx/dtau = x(1 - x) - h, h = H/(rK); MSY quota h = 1/4.
Effort: dx/dtau = x(1 - x) - e x, e = qE/r; MSY effort e = 1/2.
A: quota lines against the surplus production curve; B: effort lines; C: equilibria against the
harvest relative to its MSY level (h/0.25 or e/0.5): saddle-node for quota, transcritical for effort;
D: time for a population starting at K to be harvested to extinction when the quota exceeds the MSY,
T = (2/sqrt(eps)) arctan(1/(2 sqrt(eps))), eps = h - 1/4 (Proposition 53.1.3), checked by integration.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
cq, ce, cp = C.line("negative"), C.line("dna"), C.line("plant")

fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.6))
x = np.linspace(0, 1.05, 400)
F = x * (1 - x)


def surplus(ax):
    ax.plot(x, F, color=cp, lw=2.2, label="surplus production x(1 − x)")
    ax.axhline(0, color=P.muted(), lw=0.6)
    ax.set_xlim(0, 1.05)
    ax.set_ylim(-0.02, 0.36)


def stable(ax, xs, ys, col):
    ax.plot(xs, ys, "o", ms=7, color=col, zorder=5)


def unstable(ax, xs, ys, col):
    ax.plot(xs, ys, "o", ms=7, mfc=P.surface(), mec=col, mew=1.6, zorder=5)


# A: quotas
ax = axes[0, 0]
surplus(ax)
for h, ls, lab in ((0.30, "-", "h = 0.30 > MSY"), (0.25, "--", "h = 0.25 = MSY"), (0.15, ":", "h = 0.15")):
    ax.axhline(h, color=cq, lw=1.6, ls=ls)
    ax.text(1.04, h + 0.008, lab, color=cq, fontsize=FS["tiny"], ha="right")
d = np.sqrt(1 - 4 * 0.15)
stable(ax, [(1 + d) / 2], [0.15], cq)
unstable(ax, [(1 - d) / 2], [0.15], cq)
ax.plot([0.5], [0.25], "o", ms=7, color=cq, mfc=P.mix(cq, P.surface(), 0.5), zorder=5)
for x0, x1 in ((0.08, 0.02), (0.5, 0.75), (0.98, 0.84)):
    ax.annotate("", (x1, 0.15 - 0.03), (x0, 0.15 - 0.03),
                arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=1))
C.style_axes(ax, "stock x = N / K", "rate (units of rK)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
C.title(ax, "A  Fixed quota: harvest H independent of N")

# B: efforts
ax = axes[0, 1]
surplus(ax)
for e, ls in ((0.8, "-"), (0.5, "--"), (0.25, ":")):
    ax.plot(x, e * x, color=ce, lw=1.6, ls=ls)
    xs = 1 - e
    stable(ax, [xs], [e * xs], ce)
    xt = min(0.33 / e, 0.98)
    ax.text(xt + 0.02, e * xt - 0.012, f"e = {e:g}", color=ce, fontsize=FS["tiny"], ha="left", va="top")
unstable(ax, [0], [0], ce)
C.style_axes(ax, "stock x = N / K", "rate (units of rK)")
C.title(ax, "B  Fixed effort: harvest qEN proportional to N")

# C: bifurcation diagrams
ax = axes[1, 0]
rel = np.linspace(0, 2.2, 600)
h = 0.25 * rel
ok = h <= 0.25
disc = np.sqrt(1 - 4 * h[ok])
ax.plot(rel[ok], (1 + disc) / 2, color=cq, lw=2.2, label="fixed quota")
ax.plot(rel[ok], (1 - disc) / 2, color=cq, lw=1.4, ls=(0, (3, 2)))
ax.plot([1], [0.5], "o", ms=6, color=cq)
ax.text(1.03, 0.52, "saddle-node:\ncollapse", color=cq, fontsize=FS["tiny"])
e = 0.5 * rel
okk = e < 1
ax.plot(rel[okk], 1 - e[okk], color=ce, lw=2.2, label="fixed effort")
ax.plot(rel[~okk], 0 * rel[~okk], color=ce, lw=2.2)
ax.plot(rel[okk], 0 * rel[okk], color=ce, lw=1.2, ls=(0, (3, 2)))
ax.plot([2], [0], "o", ms=6, color=ce)
ax.text(1.93, 0.05, "transcritical", color=ce, fontsize=FS["tiny"], ha="right")
ax.axvline(1, color=P.muted(), lw=0.6, ls=":")
ax.set_xlim(0, 2.2)
ax.set_ylim(-0.04, 1.05)
C.style_axes(ax, "harvest relative to its MSY level (h / 0.25 or e / 0.5)", "equilibrium stock x*")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "C  Equilibria (solid stable, dashed unstable)")

# D: time to collapse when the quota exceeds the MSY
ax = axes[1, 1]
excess = np.linspace(0.002, 0.6, 400)
eps = 0.25 * excess
T = 2 / np.sqrt(eps) * np.arctan(1 / (2 * np.sqrt(eps)))
ax.plot(100 * excess, T, color=cq, lw=2.2, label="exact time from x = 1 to 0")
ax.plot(100 * excess, np.pi / np.sqrt(eps), color=cq, lw=1, ls=(0, (3, 2)), label="π / √ε (small ε)")
for ex in (0.01, 0.1, 0.4):
    hh = 0.25 * (1 + ex)
    ev = lambda t, y: y[0]
    ev.terminal = True
    s = solve_ivp(lambda t, y: y * (1 - y) - hh, (0, 500), [1.0], events=ev, max_step=0.05)
    ax.plot([100 * ex], [s.t_events[0][0]], "o", ms=5, color=P.ink())
ax.set_yscale("log")
ax.set_xlim(0, 60)
C.style_axes(ax, "quota above MSY (%)", "time to extinction (units of 1/r)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "D  Overestimated MSY quota: a slow, certain decline")
fig.tight_layout()
