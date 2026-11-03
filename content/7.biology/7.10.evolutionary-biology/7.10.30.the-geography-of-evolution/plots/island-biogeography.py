"""The equilibrium theory of island biogeography (Section 30.7.2). A: the immigration rate falls and the
extinction rate rises with the number S of species on the island, I(S) = I0 (1 - S/P) and
E(S) = E0 S/P, with a mainland pool of P = 100 species; near islands receive more immigrants
(I0 = 6 vs 2 species per year) and small islands lose species faster (E0 = 6 vs 2 per year). The
equilibria S* = P I0/(I0 + E0) (dots) are highest for near, large islands. B: recolonization of a
defaunated island, dS/dt = I(S) - E(S), approaches S* exponentially at the rate (I0 + E0)/P; the
time to reach it does not depend on how many species the island held before. C: the species-area
relationship S = c A^z with z = 0.25 on logarithmic axes."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
P = 100.0
S = np.linspace(0, P, 200)
fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.3), gridspec_kw={"width_ratios": [1.2, 1, 0.9]})
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.18, top=0.86, wspace=0.34)
a, b, c = axes
for I0, lab, ls in ((6, "near", "-"), (2, "far", "--")):
    a.plot(S, I0 * (1 - S / P), color=P_.edge("dna"), lw=1.8, ls=ls)
    a.text(1, I0 * 0.98, f"immigration, {lab}", fontsize=FT["tiny"], color=P_.edge("dna"), va="bottom")
for E0, lab, ls in ((6, "small", "-"), (2, "large", "--")):
    a.plot(S, E0 * S / P, color=P_.edge("negative"), lw=1.8, ls=ls)
    a.text(99, E0 * 0.99, f"extinction, {lab}", fontsize=FT["tiny"], color=P_.edge("negative"), ha="right", va="bottom")
for I0 in (6, 2):
    for E0 in (6, 2):
        s = P * I0 / (I0 + E0)
        a.plot([s], [E0 * s / P], "o", ms=5, color=P_.ink())
        a.plot([s, s], [0, E0 * s / P], color=P_.muted(), lw=0.6, ls=":")
charts.style_axes(a, "species on island, S", "rate (species per year)")
charts.title(a, "A  Immigration and extinction")
t = np.linspace(0, 80, 400)
for I0, E0, tok, lab in ((6, 2, "plant", "near, large"), (6, 6, "rna", "near, small"), (2, 2, "dna", "far, large"), (2, 6, "neutral", "far, small")):
    sstar = P * I0 / (I0 + E0)
    k = (I0 + E0) / P
    b.plot(t, sstar * (1 - np.exp(-k * t)), color=P_.edge(tok), lw=1.8, label=lab)
charts.style_axes(b, "years after defaunation", "species, S(t)")
charts.title(b, "B  Recolonization")
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="lower right")
A = np.logspace(0, 5, 50)
c.loglog(A, 10 * A ** 0.25, color=P_.edge("plant"), lw=2)
c.text(3, 60, r"$S = cA^{z}$, $z = 0.25$", fontsize=FT["small"], color=P_.ink())
charts.style_axes(c, r"island area, $A$ (km$^2$)", "species, S")
charts.title(c, "C  Species and area")
