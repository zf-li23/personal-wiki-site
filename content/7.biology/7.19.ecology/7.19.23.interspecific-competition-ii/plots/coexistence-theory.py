"""Modern coexistence theory: niche and fitness differences, and the storage effect.

A: two competitors with Lotka-Volterra per capita coefficients a_ij coexist if and only if
rho < k1/k2 < 1/rho, where rho = sqrt(a12 a21 / (a11 a22)) is the niche overlap and
k1/k2 = sqrt(a22 a21 / (a11 a12)) the fitness ratio (Chesson 2000). Shaded: coexistence; outside,
the species with the higher fitness wins (or, with rho > 1, priority decides). B, C: the lottery model
of Chesson and Warner (1981), simulated: two species occupy all sites; each year a fraction delta of adults
dies and the vacant sites are won in proportion to B_i N_i, where the per capita recruitment B_i has
ln B_i = mu_i + sigma Z_i(t) with independent standard normal Z (sigma = 1.2, mu_1 - mu_2 = -0.1, seed 1).
B: long-lived adults (delta = 0.1) store the gains of good years and both species persist. C: no
adult survival (delta = 1): the species with the higher mean ln B (species 2) excludes species 1.
D: long-run growth rate of species 1 when rare, E ln(1 - delta + delta B1/B2) (Monte Carlo, 2 x 10^5
draws): positive when fluctuations are large and adults long-lived, so the storage effect overcomes a
mean disadvantage.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(33.0, 22.0)
c1, c2 = Q.line_color("dna"), Q.line_color("rna")

pa = C.axes_at(ax, (2.4, 12.2, 11.5, 8.0))
o = np.linspace(0, 1, 300)
rho = 1 - o
pa.fill_between(o, rho, 1 / rho.clip(1e-3), color=P.mix(P.fill("positive"), P.surface(), 0.5), lw=0)
pa.plot(o, rho, color=P.ink(), lw=1.0)
pa.plot(o, 1 / rho.clip(1e-3), color=P.ink(), lw=1.0)
pa.axhline(1, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pa.set_yscale("log")
pa.set_xlim(0, 0.95)
pa.set_ylim(0.1, 10)
pa.text(0.62, 1.15, "coexistence", fontsize=FS["small"], color=P.ink())
pa.text(0.08, 4.0, "species 1 wins", fontsize=FS["small"], color=c1)
pa.text(0.08, 0.2, "species 2 wins", fontsize=FS["small"], color=c2)
pa.annotate("", xy=(0.5, 1.6), xytext=(0.1, 1.6), arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.0))
pa.text(0.3, 1.75, "stabilizing", fontsize=FS["tiny"], color=P.ink(), ha="center")
pa.annotate("", xy=(0.35, 1.1), xytext=(0.35, 3.0), arrowprops=dict(arrowstyle="-|>", color=P.ink(), lw=1.0))
pa.text(0.37, 2.2, "equalizing", fontsize=FS["tiny"], color=P.ink())
C.style_axes(pa, r"niche difference $1 - \rho$", r"fitness ratio $\kappa_1/\kappa_2$ (log scale)")
bio.panel(ax, "A", (0.4, 21.6))
bio.label(ax, (2.4, 21.2), "Niche and fitness differences", size="small", bold=True, ha="left")


def lottery(delta, years=400, sigma=1.2, dmu=-0.1, seed=1):
    rng = np.random.default_rng(seed)
    n1 = 0.5
    out = [n1]
    for _ in range(years):
        b1 = np.exp(dmu + sigma * rng.standard_normal())
        b2 = np.exp(sigma * rng.standard_normal())
        n2 = 1 - n1
        n1 = (1 - delta) * n1 + delta * b1 * n1 / (b1 * n1 + b2 * n2)
        out.append(n1)
    return np.array(out)


for k, (delta, tag, name, rect) in enumerate([
        (0.1, "B", r"Long-lived adults: storage ($\delta$ = 0.1)", (18.9, 12.2, 12.5, 8.0)),
        (1.0, "C", r"Annual life cycle: no storage ($\delta$ = 1)", (2.4, 1.8, 11.5, 8.0))]):
    p = C.axes_at(ax, rect)
    n1 = lottery(delta)
    t = np.arange(len(n1))
    p.plot(t, n1, color=c1, lw=1.0, label="species 1")
    p.plot(t, 1 - n1, color=c2, lw=1.0, label="species 2")
    p.set_xlim(0, 400)
    p.set_ylim(0, 1)
    C.style_axes(p, "years", "fraction of sites")
    p.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right", ncol=2)
    bio.panel(ax, tag, (rect[0] - 2.0, rect[1] + 9.4))
    bio.label(ax, (rect[0], rect[1] + 9.0), name, size="small", bold=True, ha="left")

pd = C.axes_at(ax, (18.9, 1.8, 12.5, 8.0))
rng = np.random.default_rng(2)
z = rng.standard_normal((2, 200000))
sig = np.linspace(0, 2.0, 41)
for delta, tok in [(0.05, "dna"), (0.2, "positive"), (0.5, "protein"), (1.0, "rna")]:
    rbar = [np.mean(np.log(1 - delta + delta * np.exp(-0.1 + s * (z[0] - z[1])))) for s in sig]
    pd.plot(sig, rbar, color=Q.line_color(tok), lw=1.6, label=rf"$\delta$ = {delta}")
pd.axhline(0, color=P.muted(), lw=0.8)
pd.set_xlim(0, 2)
C.style_axes(pd, r"environmental variability $\sigma$", "growth rate when rare (per year)")
pd.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "D", (16.9, 11.2))
bio.label(ax, (18.9, 10.8), "Invasion growth rate of species 1", size="small", bold=True, ha="left")
