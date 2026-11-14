"""The hawk-dove-bourgeois game (Maynard Smith 1982) and its replicator dynamics on the strategy simplex.

Each contest has an owner and an intruder, each role taken with probability 1/2. Hawk escalates, Dove displays
and retreats, Bourgeois plays Hawk as owner and Dove as intruder. V = 2, C = 3 (V < C), so the hawk-dove edge
has its mixed equilibrium at p = V/C, but Bourgeois is a strict ESS and attracts every interior trajectory.
"""

import numpy as np
from matplotlib.patches import Circle, Polygon

import wikibio as bio
from wikibio import behaviour as bh
from wikibio import quant

P = bio.P
V, C = 2.0, 3.0
A = np.array([
    [(V - C) / 2, V, (3 * V - C) / 4],
    [0.0, V / 2, V / 4],
    [(V - C) / 4, 3 * V / 4, V / 2],
])
TOK = ["rna", "dna", "protein"]

fig, ax = bio.canvas(30.0, 11.5)

# ---- A: payoff matrix --------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 11.4))
cells = [["$(V-C)/2$", "$V$", "$(3V-C)/4$"],
         ["$0$", "$V/2$", "$V/4$"],
         ["$(V-C)/4$", "$3V/4$", "$V/2$"]]
bh.payoff_matrix(ax, (7.1, 5.6), ["Hawk", "Dove", "Bourg."], cells, w=2.5, h=1.15, tokens=TOK, highlight=(2, 2))
bio.label(ax, (6.2, 2.75), "Bourgeois: Hawk when owner, Dove when intruder", size="tiny", color=P.muted())
bio.label(ax, (6.2, 2.2), "roles equally likely; payoff to the focal (row) player", size="tiny", color=P.muted())
bio.label(ax, (6.2, 1.65), f"$V$ = {V:g}, $C$ = {C:g}:  $E(B,B) > E(H,B)$ and $E(B,B) > E(D,B)$", size="tiny",
          color=P.muted())

# ---- B: replicator dynamics on the simplex ------------------------------------------------------------------
bio.panel(ax, "B", (14.2, 11.4))
vH, vD, vB = np.array([15.8, 1.4]), np.array([27.6, 1.4]), np.array([21.7, 1.4 + 11.8 * np.sqrt(3) / 2 * 0.86])


def to_xy(x):
    x = np.atleast_2d(x)
    return x[:, 0:1] * vH + x[:, 1:2] * vD + x[:, 2:3] * vB


def rhs(_, x):
    f = A @ x
    return x * (f - x @ f)


ax.add_patch(Polygon(
    [vH, vD, vB], closed=True, facecolor=P.mix(P.fill("neutral"), P.surface(), 0.75), edgecolor=P.muted(), lw=0.9,
    zorder=2))
t = np.linspace(0, 400, 8000)
starts = [(0.90, 0.08, 0.02), (0.55, 0.43, 0.02), (0.30, 0.68, 0.02), (0.08, 0.90, 0.02), (0.64, 0.32, 0.04),
          (0.45, 0.25, 0.30), (0.20, 0.45, 0.35), (0.75, 0.05, 0.20), (0.05, 0.60, 0.35), (0.35, 0.10, 0.55)]
for s in starts:
    x = quant.odeint_rk4(rhs, np.array(s, float), t)
    xy = to_xy(x)
    ax.plot(xy[:, 0], xy[:, 1], color=quant.line_color("ink"), lw=1.0, zorder=5, solid_capstyle="round")
    arc = np.r_[0, np.cumsum(np.hypot(*np.diff(xy, axis=0).T))]
    k = int(np.searchsorted(arc, 0.4 * arc[-1]))
    bio.arrow(ax, xy[k - 3], xy[k + 3], kind="process", color=quant.line_color("ink"), lw=0, head=0.28, zorder=6)
# the hawk-dove edge: flow towards p* = V/C, then the neutral line away from it
edge_t = np.linspace(0, 30, 900)
for p0 in (0.02, 0.98):
    x = quant.odeint_rk4(rhs, np.array([p0, 1 - p0, 0.0]), edge_t)
    xy = to_xy(x)
    ax.plot(xy[:, 0], xy[:, 1], color=quant.line_color("rna"), lw=1.8, zorder=6)
pstar = np.array([V / C, 1 - V / C, 0.0])
ps = to_xy(pstar)[0]
ax.add_patch(Circle(ps, 0.22, facecolor=P.surface(), edgecolor=quant.line_color("rna"), lw=1.4, zorder=8))
bio.label(ax, (ps[0], ps[1] - 0.55), "$p^* = V/C$ (hawk-dove mixture)", size="tiny", va="top",
          color=quant.line_color("rna"))
ax.add_patch(Circle(vB, 0.3, facecolor=quant.line_color("protein"), edgecolor=quant.line_color("protein"), lw=1.2,
                    zorder=8))
for v, name, tok, dx, dy, ha in ((vH, "Hawk", "rna", -0.3, -0.3, "right"), (vD, "Dove", "dna", 0.3, -0.3, "left"),
                                 (vB, "Bourgeois (ESS)", "protein", 0.45, 0.25, "left")):
    bio.label(ax, (v[0] + dx, v[1] + dy), name, size="small", bold=True, color=quant.line_color(tok), ha=ha)
bio.label(ax, (15.3, 11.0), "replicator dynamics  $\\dot x_i = x_i\\,[(A\\mathbf{x})_i - "
          "\\mathbf{x}^{T}\\!A\\mathbf{x}]$", size="tiny", color=P.muted(), ha="left")
