"""Two models of nuclear size (arbitrary units).
(A) Osmotic balance (Proposition 16.7.1, dry-mass volumes neglected): V_n = r V_cell / (1 + r) with r = N_n/N_c.
Control r = 0.087 (nucleus 8 % of the cell; points: cells with 10 % lognormal variation of r); export blocked,
r doubled (dashed); cytoplasmic macromolecules increased 1.5-fold (dotted).
(B) Import-limited growth in egg extract: the import flux of lamin is proportional to the number of pores
(proportional to nuclear surface) times f = a/(K_a + a) / (1 + n/K_n), where a is the importin alpha and n the
NTF2 concentration; with dV/dt proportional to the flux and surface proportional to V^(2/3), the radius grows
linearly, dR/dt = c f. Cross-sectional area pi R^2 is plotted, as measured in extract experiments."""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)

fig, ax = bio.canvas(19.0, 7.4)
bio.panel(ax, "A", (0.1, 7.3))
a = charts.axes_at(ax, (1.9, 1.3, 6.6, 5.6))
V = np.linspace(0, 140, 50)
r0 = 0.087
for r, ls, lab in ((r0, "-", "control"), (2 * r0, "--", "nuclear export blocked"), (r0 / 1.5, ":", "more cytoplasmic macromolecules")):
    a.plot(V, r * V / (1 + r), color=charts.line("nucleus" if ls == "-" else "negative" if ls == "--" else "channel"), lw=1.8, ls=ls,
           label=lab)
Vc = rng.uniform(60, 120, 60)
rr = r0 * np.exp(rng.normal(0, 0.1, 60))
a.plot(Vc, rr * Vc / (1 + rr), "o", color=charts.line("nucleus"), ms=3.5, alpha=0.8)
a.set_xlim(0, 140)
a.set_ylim(0, 22)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, "cell volume", "nuclear volume")

bio.panel(ax, "B", (9.9, 7.3))
b = charts.axes_at(ax, (11.6, 1.3, 6.9, 5.6))
t = np.linspace(0, 90, 200)


def area(alpha, ntf2, R0=1.0, c=0.12, Ka=0.5, Kn=1.0):
    f = alpha / (Ka + alpha) / (1 + ntf2 / Kn)
    R = R0 + c * f * t
    return np.pi * R**2


for (al, nt), tok, ls, lab in (((1.0, 0.5), "positive", "-", r"$\it{X.\ laevis}$ extract"),
                               ((0.4, 1.5), "channel", "-", r"$\it{X.\ tropicalis}$ extract"),
                               ((1.6, 1.5), "channel", "--", r"$\it{X.\ tropicalis}$ + importin α"),
                               ((1.0, 2.0), "positive", "--", r"$\it{X.\ laevis}$ + NTF2")):
    b.plot(t, area(al, nt), color=charts.line(tok), lw=1.8, ls=ls, label=lab)
b.set_xlim(0, 90)
b.set_ylim(0, 70)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "time after nuclear assembly / min", "nuclear cross-sectional area")
