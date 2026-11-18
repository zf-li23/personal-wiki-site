"""Species-area relationships from sampling and from the equilibrium theory.

A: passive sampling (Coleman 1981). A mainland community of 400 species whose abundances n_i are
lognormal (ln n_i normal, mean 6, sd 2); a plot that covers a fraction a of the region contains species i
with probability 1 - (1 - a)^{n_i}, so E[S(a)] = sum_i [1 - (1 - a)^{n_i}] (line, log-log axes). The local
slope z = d ln S/d ln a (right axis, dashed) is not constant: near 1 for tiny plots (almost every individual
added is a new species), 0.2-0.5 at intermediate scales, and 0 once the whole region is sampled. B: simulated archipelagos under the
MacArthur-Wilson model with area- and distance-dependent rates, S* = P/(1 + (e/i) A^(-x) exp(d/d0)),
P = 200, e/i = 10, x = 0.5, d0 = 100 km; 30 islands per archipelago at 10 km (near) or 300 km (far), areas
log-uniform from 1 to 10^4 km^2, observed counts Poisson around S*. Lines: least-squares fits of
log10 S = log10 c + z log10 A, with fitted z. C: the local slope of the model, z = x (1 - S*/P): remote
islands, being further from saturation, have steeper curves; all are curved on log-log axes.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(4)

fig, ax = bio.canvas(31.0, 10.0)

n_i = np.exp(rng.normal(6, 2, 400)).astype(int) + 1
a = np.logspace(-7, 0, 300)
S = np.array([(1 - (1 - aa) ** n_i).sum() for aa in a])
pa = C.axes_at(ax, (2.2, 1.6, 7.0, 6.8))
pa.loglog(a, S, color=Q.line_color("dna"), lw=1.8, label="expected richness S(a)")
pa.set_xlim(a[0], 1)
pa.set_ylim(0.5, 600)
C.style_axes(pa, "fraction of the region sampled a", "species S")
pa2 = pa.twinx()
z = np.gradient(np.log(S), np.log(a))
pa2.semilogx(a, z, color=Q.line_color("negative"), lw=1.3, ls=(0, (4, 2)))
pa2.set_ylim(0, 1)
C.style_axes(pa2, None, "local slope z")
pa2.spines["right"].set_visible(True)
pa.plot([], [], color=Q.line_color("negative"), lw=1.3, ls=(0, (4, 2)), label="z = d ln S / d ln a (right axis)")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "A", (0.4, 9.6))
bio.label(ax, (2.2, 9.2), "Passive sampling (random placement)", size="small", bold=True, ha="left")

Pp, ei, x, d0 = 200, 10.0, 0.5, 100.0


def Sstar(A, d):
    return Pp / (1 + ei * A ** (-x) * np.exp(d / d0))


pb = C.axes_at(ax, (12.4, 1.6, 7.0, 6.8))
for d, tok, lab in ((10, "plant", "near (10 km)"), (300, "enzyme", "far (300 km)")):
    A = 10 ** rng.uniform(0, 4, 30)
    obs = rng.poisson(Sstar(A, d))
    keep = obs > 0
    zfit, lc = np.polyfit(np.log10(A[keep]), np.log10(obs[keep]), 1)
    c = Q.line_color(tok)
    pb.loglog(A[keep], obs[keep], "o", ms=3.5, color=c, label=f"{lab}: z = {zfit:.2f}")
    AA = np.logspace(0, 4, 50)
    pb.loglog(AA, 10 ** lc * AA ** zfit, color=c, lw=1.4)
pb.set_xlim(1, 1e4)
pb.set_ylim(0.7, 300)
C.style_axes(pb, "island area A (km²)", "species S")
pb.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "B", (10.9, 9.6))
bio.label(ax, (12.4, 9.2), "Two simulated archipelagos", size="small", bold=True, ha="left")

pc = C.axes_at(ax, (22.6, 1.6, 7.0, 6.8))
AA = np.logspace(-1, 6, 300)
for d, tok, lab in ((10, "plant", "near (10 km)"), (100, "protein", "100 km"), (300, "enzyme", "far (300 km)")):
    s = Sstar(AA, d)
    pc.semilogx(AA, x * (1 - s / Pp), color=Q.line_color(tok), lw=1.6, label=lab)
pc.axhline(x, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pc.text(1.5e5, x + 0.012, "x (extinction–area exponent)", fontsize=FS["tiny"], color=P.muted(), ha="right")
pc.set_xlim(AA[0], AA[-1])
pc.set_ylim(0, 0.56)
C.style_axes(pc, "island area A (km²)", "local slope z = x (1 − S*/P)")
pc.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "C", (21.1, 9.6))
bio.label(ax, (22.6, 9.2), "Isolation steepens the curve", size="small", bold=True, ha="left")
