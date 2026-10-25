"""The concerted (MWC) model for a tetramer. A: states (squares T, circles R; filled dots = bound
ligand); all subunits switch together, L = [T0]/[R0], ligand binds R with dissociation constant K_R
and T with K_T = K_R/c. B: saturation theta (solid) and fraction of molecules in the R state (dashed)
against alpha = [L]/K_R for c = 0.01 and several L. C: Hill coefficient at half-saturation against L;
it is largest when L c^2 = 1, i.e. at L = 1e4 here."""

import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
c = 0.01


def theta(a, L):
    return (a * (1 + a) ** 3 + L * c * a * (1 + c * a) ** 3) / ((1 + a) ** 4 + L * (1 + c * a) ** 4)


def rfrac(a, L):
    return (1 + a) ** 4 / ((1 + a) ** 4 + L * (1 + c * a) ** 4)


def hill(L):
    a50 = brentq(lambda a: theta(a, L) - 0.5, 1e-8, 1e8)
    lg = lambda y: np.log(y / (1 - y))
    h = 1e-5
    return (lg(theta(a50 * (1 + h), L)) - lg(theta(a50 * (1 - h), L))) / (2 * h)


fig, ax = bio.canvas(22.0, 8.0)

# A: schematic
bio.panel(ax, "A", (0.1, 7.9))
bio.label(ax, (3.6, 7.45), "Concerted transition", size="small", bold=True)


def tetramer(x, y, kind, n):
    tok = "neutral" if kind == "T" else "positive"
    for k, (dx, dy) in enumerate(((-0.22, 0.22), (0.22, 0.22), (-0.22, -0.22), (0.22, -0.22))):
        if kind == "T":
            ax.add_patch(FancyBboxPatch((x + dx - 0.17, y + dy - 0.17), 0.34, 0.34, boxstyle="round,pad=0,rounding_size=0.04",
                                        facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=10))
        else:
            ax.add_patch(Circle((x + dx, y + dy), 0.19, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=10))
        if k < n:
            ax.add_patch(Circle((x + dx, y + dy), 0.07, color=P.edge("blood"), zorder=11))


for n in range(5):
    x = 0.9 + n * 1.45
    tetramer(x, 5.8, "R", n)
    tetramer(x, 3.3, "T", n)
    bio.label(ax, (x, 4.55), "⇅", size="small", color=P.muted())
    if n < 4:
        bio.label(ax, (x + 0.72, 5.8), "⇄", size="small", color=P.muted())
        bio.label(ax, (x + 0.72, 3.3), "⇄", size="small", color=P.muted())
bio.label(ax, (0.9, 6.65), "R₀", size="tiny")
bio.label(ax, (0.9, 2.45), "T₀", size="tiny")
bio.label(ax, (3.8, 1.75), r"binding to R: $K_\mathrm{R}$; to T: $K_\mathrm{T} = K_\mathrm{R}/c$", size="tiny")
bio.label(ax, (3.8, 1.25), r"$\mathrm{R}_n \rightleftharpoons \mathrm{T}_n$: equilibrium constant $Lc^n$", size="tiny")
bio.label(ax, (3.8, 0.65), r"$Z = (1+\alpha)^4 + L(1+c\alpha)^4,\ \alpha = [\mathrm{L}]/K_\mathrm{R}$", size="tiny", color=P.edge("protein"))

# B: curves
bio.panel(ax, "B", (7.8, 7.9))
pb = charts.axes_at(ax, (9.0, 1.3, 5.6, 5.8))
a = np.logspace(-2, 4, 500)
for L, tok in ((1.0, "neutral"), (1e2, "enzyme"), (1e4, "blood"), (1e6, "protein")):
    pb.plot(a, theta(a, L), color=charts.line(tok), lw=1.7, label=rf"$L = 10^{{{int(np.log10(L))}}}$" if L > 1 else r"$L = 1$")
    pb.plot(a, rfrac(a, L), color=charts.line(tok), lw=0.9, ls="--")
pb.set_xscale("log")
pb.set_ylim(0, 1.03)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
pb.text(600, 0.4, "dashed:\nfraction of\nmolecules\nin R state", fontsize=bio.core.FONT["tiny"], color=P.ink(), ha="center")
charts.style_axes(pb, r"$\alpha = [\mathrm{L}]/K_\mathrm{R}$", r"$\theta$ (solid)")
charts.title(pb, "Saturation, c = 0.01")

# C: Hill coefficient
bio.panel(ax, "C", (15.3, 7.9))
pc = charts.axes_at(ax, (16.5, 1.3, 5.0, 5.8))
Ls = np.logspace(-1, 9, 200)
for cc_, tok in ((0.01, "blood"), (0.1, "enzyme")):
    c = cc_
    pc.plot(Ls, [hill(L) for L in Ls], color=charts.line(tok), lw=1.7, label=f"c = {cc_}")
c = 0.01
pc.axhline(4, color=P.muted(), lw=0.6, ls=":")
pc.text(2e5, 3.82, "limit n = 4", fontsize=bio.core.FONT["tiny"], color=P.ink())
pc.axvline(1e4, color=P.muted(), lw=0.6, ls=":")
pc.set_xscale("log")
pc.set_ylim(0.9, 4.2)
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(pc, "L", r"$n_\mathrm{H}$ at half-saturation")
charts.title(pc, r"Cooperativity peaks at $Lc^2 = 1$")
