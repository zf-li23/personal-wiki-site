"""Reaction coordinate diagrams (schematic Gibbs energies in kJ/mol).

A: uncatalyzed S -> P against the enzyme-catalyzed path E + S -> ES -> EP -> E + P. The enzyme
lowers the activation Gibbs energy but leaves the overall standard reaction Gibbs energy unchanged.
B: the "stickase" thought experiment. An enzyme complementary to the substrate binds S tightly
(deep ES trough) and raises the barrier measured from ES; an enzyme complementary to the
transition state binds S weakly and releases most of its binding energy only at the transition
state, which lowers the barrier."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P


def profile(points, n=120):
    """Smooth curve through (x, G) extrema: cosine interpolation, zero slope at every point."""
    xs, ys = [], []
    for (x0, g0), (x1, g1) in zip(points[:-1], points[1:]):
        t = np.linspace(0, 1, n)
        xs.append(x0 + (x1 - x0) * t)
        ys.append(g0 + (g1 - g0) * (1 - np.cos(np.pi * t)) / 2)
    return np.concatenate(xs), np.concatenate(ys)


def level(a, x, g, text, dx=0.0, dy=4.0, ha="center"):
    a.text(x + dx, g + dy, text, fontsize=bio.core.FONT["tiny"], color=P.ink(), ha=ha, va="bottom")


def gap(a, x, g0, g1, text, side=1, color=None):
    color = color or P.ink()
    a.annotate("", (x, g1), (x, g0), arrowprops=dict(arrowstyle="<->", color=color, lw=0.9, shrinkA=0, shrinkB=0))
    a.text(x + 0.12 * side, (g0 + g1) / 2, text, fontsize=bio.core.FONT["tiny"], color=color,
           ha="left" if side > 0 else "right", va="center")


fig, ax = bio.canvas(22.0, 8.6)
unc = charts.line("neutral")
cat = charts.line("enzyme")
bad = charts.line("negative")

# --- A ---------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.5))
a = charts.axes_at(ax, (1.2, 0.9, 8.8, 6.8))
xu, gu = profile([(0, 0), (5, 85), (10, -20)])
xc, gc = profile([(0, 0), (1.6, 22), (3.0, -12), (5, 38), (7.0, -28), (8.4, 6), (10, -20)])
a.plot(xu, gu, color=unc, lw=1.8, ls=(0, (5, 3)), label="uncatalyzed")
a.plot(xc, gc, color=cat, lw=2.0, label="enzyme-catalyzed")
for g in (0, -20):
    a.axhline(g, color=P.muted(), lw=0.6, ls=":")
level(a, 0.2, 0, "S", dy=3, ha="left")
level(a, 9.8, -20, "P", dy=3, ha="right")
level(a, 5.0, 85, r"S$^{\ddagger}$", dy=2)
level(a, 3.0, -12, "ES", dy=-10)
level(a, 5.2, 38, r"ES$^{\ddagger}$", dy=2, ha="left")
level(a, 7.0, -28, "EP", dy=-10)
gap(a, 4.3, 0, 85, r"$\Delta^{\ddagger}G_{\mathrm{uncat}}$", side=-1, color=unc)
gap(a, 5.6, -12, 38, r"$\Delta^{\ddagger}G_{\mathrm{cat}}$", color=cat)
gap(a, 9.3, 0, -20, r"$\Delta_{\mathrm{r}}G'^{\circ}$", side=-1)
a.set_xlim(0, 10)
a.set_ylim(-45, 100)
a.set_xticks([])
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "Reaction coordinate", "Gibbs energy $G$ / (kJ mol$^{-1}$)")
charts.title(a, "Enzymes lower the barrier, not $\\Delta_{\\mathrm{r}}G'^{\\circ}$")

# --- B ---------------------------------------------------------------------------------------
bio.panel(ax, "B", (11.2, 8.5))
b = charts.axes_at(ax, (12.4, 0.9, 9.2, 6.8))
xu, gu = profile([(0, 0), (5, 85), (10, -20)])
xs, gs = profile([(0, 0), (1.6, 10), (3.0, -40), (5, 70), (7.0, -45), (8.4, 6), (10, -20)])
xt, gt = profile([(0, 0), (1.6, 10), (3.0, -10), (5, 30), (7.0, -30), (8.4, 6), (10, -20)])
b.plot(xu, gu, color=unc, lw=1.8, ls=(0, (5, 3)), label="no enzyme")
b.plot(xs, gs, color=bad, lw=1.8, label="complementary to S")
b.plot(xt, gt, color=cat, lw=2.0, label=r"complementary to S$^{\ddagger}$")
level(b, 3.0, -40, "ES (too stable)", dy=-11)
level(b, 3.25, -10, "ES", dy=-9, ha="left")
gap(b, 3.0, -40, 70, "barrier from ES:\n110 kJ/mol", side=-1, color=bad)
gap(b, 5.0, 85, 30, "", color=cat)
b.text(5.15, 93, r"$\Delta G_{\mathrm{B}}$ realized in ES$^{\ddagger}$", fontsize=bio.core.FONT["tiny"], color=cat)
b.set_xlim(0, 10)
b.set_ylim(-60, 105)
b.set_xticks([])
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "Reaction coordinate", None)
charts.title(b, "Binding energy must be released at the transition state")
