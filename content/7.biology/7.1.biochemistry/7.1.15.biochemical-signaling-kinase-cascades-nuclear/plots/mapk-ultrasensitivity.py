"""Ultrasensitivity in a three-tier MAP kinase cascade (after Huang and Ferrell, 1996), at steady state.

Each kinase is activated by the active kinase of the tier above and inactivated by a phosphatase, both
with Michaelis-Menten kinetics (Km = 1 in units of the total concentration of the substrate kinase;
substrates of the same enzyme compete for it). Tier 1 (MAPKKK) is modified once by the input E; tiers 2
(MAPKK) and 3 (MAPK) need two phosphorylations, added and removed one at a time (distributively). The
active form of each tier is the enzyme of the next, scaled so that it spans the input range of that tier.
A: fraction active at each tier against the input. The apparent Hill coefficient,
nH = ln 81 / ln(E90/E10), grows from tier to tier (about 1.3, 2.4 and 4.6; Huang and Ferrell computed
1.0, 1.7 and 4.9 with their parameters, and Ferrell measured about 5 for MAPK in Xenopus oocyte extracts).
B: the sources of steepness in one tier: a single modification is graded (nH about 1.3 here); a
distributive double modification gives a sigmoid response even with little saturation (Km = 10, nH about 1.4);
competition and saturation (Km = 1) make it steeper (nH about 1.9).
"""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P


def single(u, K=1.0):
    return brentq(lambda x: u * (1 - x) / (K + 1 - x) - x / (K + x), 0.0, 1.0)


def double(u, K=1.0):
    def g(r):
        m0 = 1 / (1 + r + r * r)
        m1, m2 = r * m0, r * r * m0
        return r - u * (1 + (m1 + m2) / K) / (1 + (m0 + m1) / K)
    r = brentq(g, 1e-14, 1e14)
    return r * r / (1 + r + r * r)


grid = np.logspace(-3, 3, 2000)
ec = np.interp(0.5, [double(u) for u in grid], grid)
c = 4 * ec


def tier1(E):
    return single(E)


def tier2(E):
    return double(c * tier1(E))


def tier3(E):
    return double(c * tier2(E))


def hill_n(f, xs):
    y = np.array([f(x) for x in xs])
    y = (y - y.min()) / (y.max() - y.min())
    return np.log(81) / np.log(np.interp(0.9, y, xs) / np.interp(0.1, y, xs))


E = np.logspace(-3.5, 2, 600)
fig, ax = bio.canvas(20.0, 7.8)
bio.panel(ax, "A", (0.1, 7.7))
pa = charts.axes_at(ax, (1.6, 1.4, 7.6, 5.6))
for f, tok, name in ((tier1, "highlight", "MAPKKK*"), (tier2, "protein", "MAPKK-PP"), (tier3, "positive", "MAPK-PP")):
    y = np.array([f(e) for e in E])
    n = hill_n(f, E)
    pa.semilogx(E, y / y.max(), color=charts.line(tok), lw=2.0, label=f"{name}  (nH ≈ {n:.1f})")
pa.set_xlim(E[0], E[-1])
pa.set_ylim(0, 1.05)
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pa, "input stimulus E (relative)", "fraction active (normalized)")
charts.title(pa, "Steepness grows down the cascade")

bio.panel(ax, "B", (10.6, 7.7))
pb = charts.axes_at(ax, (12.2, 1.4, 7.2, 5.6))
u = np.logspace(-2.5, 2.5, 600)
for f, tok, name in ((lambda x: single(x), "highlight", "single site"), (lambda x: double(x, K=10.0), "channel", r"two sites, $K_\mathrm{m}$ = 10"),
                     (lambda x: double(x, K=1.0), "protein", r"two sites, $K_\mathrm{m}$ = 1")):
    y = np.array([f(x) for x in u])
    n = hill_n(f, u)
    pb.semilogx(u, y, color=charts.line(tok), lw=2.0, label=f"{name}  (nH ≈ {n:.1f})")
pb.set_xlim(u[0], u[-1])
pb.set_ylim(0, 1.05)
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(pb, "kinase / phosphatase activity ratio", "fraction fully modified")
charts.title(pb, "One tier: multisite modification")
