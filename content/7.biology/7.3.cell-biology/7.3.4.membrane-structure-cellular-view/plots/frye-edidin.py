"""The Frye-Edidin experiment (1970) and a diffusion model of it.

A: schematic. A mouse cell (surface antigens green) and a human cell (red) are fused by Sendai virus;
immediately after fusion the labels occupy opposite halves of the heterokaryon, after 40 min at 37 C
they are intermixed.
B: diffusion on a sphere of radius R = 7.5 um from a hemispherical start. With x = cos(theta), the
concentration is c(x, t) = sum_l a_l P_l(x) exp(-l(l+1) D t / R^2), a_l = (2l+1)/2 int_0^1 P_l dx.
Plotted: the fraction of label still in the original hemisphere, for three values of D.
C: percentage of cells scored as mixed (less than 60 % of the label in one half) when D varies from
cell to cell (log-normal, sd of ln D = 0.6), median D = 0.03 um^2/s (37 C) and 0.003 um^2/s (cold).
"""

import numpy as np
from numpy.polynomial import legendre as L
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 7.6)
R = 7.5
LMAX = 41


def coeffs():
    a = np.zeros(LMAX + 1)
    for l in range(LMAX + 1):
        c = np.zeros(l + 1)
        c[l] = 1
        integ = L.legint(c, lbnd=0)
        a[l] = (2 * l + 1) / 2 * (L.legval(1, integ) - L.legval(0, integ))
    return a


A = coeffs()
HALF = np.zeros(LMAX + 1)  # integral of P_l over (0, 1)
for l in range(LMAX + 1):
    c = np.zeros(l + 1)
    c[l] = 1
    integ = L.legint(c, lbnd=0)
    HALF[l] = L.legval(1, integ) - L.legval(0, integ)
LL = np.arange(LMAX + 1) * (np.arange(LMAX + 1) + 1)


def frac(t, D):
    return np.array([(A * HALF * np.exp(-LL * D * ti / R**2)).sum() for ti in np.atleast_1d(t)])


# ---- A: schematic
bio.panel(ax, "A", (0.1, 7.4))


def cellcircle(c, r, left, right, mixed=False, seed=1):
    o = bio.blob(c, r, r * 0.92, wobble=0.04, seed=seed, k=9)
    bio.membrane(ax, o, inside="cytoplasm")
    rng = np.random.default_rng(seed)
    th = np.linspace(0, 2 * np.pi, 34, endpoint=False)
    for i, t in enumerate(th):
        p = (c[0] + r * 1.0 * np.cos(t), c[1] + r * 0.92 * np.sin(t))
        if mixed:
            tok = "positive" if i % 2 else "negative"
        else:
            tok = left if np.cos(t) < 0 else right
        if tok:
            bio.molecule(ax, p, token=tok, r=0.11, zorder=12)


cellcircle((1.4, 4.6), 0.95, "positive", "positive", seed=2)
cellcircle((3.6, 4.6), 0.95, "negative", "negative", seed=3)
bio.label(ax, (1.4, 3.15), "mouse", size="small")
bio.label(ax, (3.6, 3.15), "human", size="small")
bio.arrow(ax, (2.5, 3.0), (2.5, 2.35), kind="process")
bio.label(ax, (2.75, 2.7), "fusion", size="tiny", ha="left", color=P.muted())
cellcircle((1.4, 1.2), 0.95, "positive", "negative", seed=4)
bio.label(ax, (1.4, 0.05), "0 min", size="small")
bio.arrow(ax, (2.55, 1.2), (3.0, 1.2), kind="process")
cellcircle((4.1, 1.2), 0.95, None, None, mixed=True, seed=5)
bio.label(ax, (4.1, 0.05), "40 min, 37 °C", size="small")

# ---- B: model
bio.panel(ax, "B", (6.2, 7.4))
pb = charts.axes_at(ax, (7.8, 1.3, 6.6, 5.4))
t = np.linspace(0, 90 * 60, 400)
for D, tok in ((0.01, "dna"), (0.03, "protein"), (0.1, "negative")):
    pb.plot(t / 60, frac(t, D), color=charts.line(tok), lw=1.8, label=f"D = {D} µm² s⁻¹")
pb.axhline(0.5, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pb.axhline(0.6, color=P.muted(), lw=0.5, ls=(0, (1, 2)))
pb.text(88, 0.61, "threshold 0.6", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="right", va="bottom")
pb.set_xlim(0, 90)
pb.set_ylim(0.45, 1.02)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(pb, "time after fusion / min", "fraction in original half")
charts.title(pb, "Diffusion on a sphere, R = 7.5 µm")

# ---- C: population
bio.panel(ax, "C", (15.6, 7.4))
pc = charts.axes_at(ax, (17.2, 1.3, 6.4, 5.4))
rng = np.random.default_rng(0)
tt = np.linspace(0, 90 * 60, 181)
for Dm, tok, name in ((0.03, "protein", "37 °C (median D = 0.03)"), (0.003, "dna", "cold (median D = 0.003)")):
    Ds = Dm * np.exp(0.6 * rng.standard_normal(300))
    # time at which each cell first holds less than 60 % of the label in the original half
    g = np.geomspace(1, 400 * 60, 300)
    crossing = []
    for D in Ds:
        fv = frac(g, D)
        idx = np.argmax(fv < 0.6)
        crossing.append(g[idx] if fv[idx] < 0.6 else np.inf)
    crossing = np.array(crossing)
    pct = [(crossing <= ti).mean() * 100 for ti in tt]
    pc.plot(tt / 60, pct, color=charts.line(tok), lw=1.8, label=name)
pc.set_xlim(0, 90)
pc.set_ylim(0, 102)
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(pc, "time after fusion / min", "mixed heterokaryons / %")
charts.title(pc, "Scored population (model)")
