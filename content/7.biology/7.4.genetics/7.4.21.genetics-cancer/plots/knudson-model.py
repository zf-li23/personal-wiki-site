"""Knudson's two-hit model in quantitative form, Eqs. (21.1) and (21.2): N = 1.5e5 retinoblasts at risk and
mu = 4e-6 inactivations per allele per year. A: the fraction of children still free of tumors against age.
B: the number of tumors per carrier at age five. C: penetrance against age for carriers and non-carriers."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
N, mu = 1.5e5, 4e-6
t = np.linspace(0.05, 6, 300)
m1, m2 = N * mu * t, N * (mu * t) ** 2

fig, axs = plt.subplots(1, 3, figsize=(13.2, 3.9))
fig.subplots_adjust(left=0.06, right=0.985, bottom=0.17, top=0.87, wspace=0.33)

a = axs[0]
A = N * mu          # per year; the two forms are scaled to the same risk at age 6 to compare their shapes
a.semilogy(t, np.exp(-A * t), color=charts.line("receptor"), lw=2, label="one hit needed: straight line in $t$")
a.semilogy(t, np.exp(-A * t**2 / 6), color=charts.line("dna"), lw=2, label="two hits needed: straight line in $t^2$")
a.set_ylim(2e-2, 1.3)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(a, "age / years", "fraction still free of tumors")
charts.title(a, "A  Shape of onset (scaled to equal risk)")

b = axs[1]
k = np.arange(0, 9)
pmf = stats.poisson.pmf(k, N * mu * 5)
b.bar(k, pmf, width=0.65, color=P.fill("receptor"), edgecolor=charts.line("receptor"), lw=0.9)
b.text(4.6, 0.21, "mean 3 tumors\nper carrier at age 5", fontsize=FT["tiny"], color=P.muted())
uni = (1 - np.exp(-1.5)) ** 2
b.text(4.6, 0.135, f"unaffected {np.exp(-3):.0%}\nbilateral {uni:.0%} of carriers", fontsize=FT["tiny"],
       color=P.muted())
b.set_xticks(k)
charts.style_axes(b, "number of tumors", "probability")
charts.title(b, "B  Tumors per carrier (Poisson)")

c = axs[2]
c.plot(t, 1 - np.exp(-m1), color=charts.line("receptor"), lw=2, label="carrier (left axis)")
c.axhline(0.9, color=P.muted(), lw=0.8, ls=":")
c.text(0.1, 0.92, "90 % penetrance observed", fontsize=FT["tiny"], color=P.muted())
c.set_ylim(0, 1.05)
charts.style_axes(c, "age / years", "penetrance, carrier")
c2 = c.twinx()
c2.plot(t, 1 - np.exp(-m2), color=charts.line("dna"), lw=2, ls="--")
c2.set_ylabel("penetrance, non-carrier", fontsize=FT["small"], color=charts.line("dna"))
c2.tick_params(axis="y", labelsize=FT["small"], colors=charts.line("dna"))
for sp in ("top",):
    c2.spines[sp].set_visible(False)
c2.spines["right"].set_color(P.muted())
charts.title(c, "C  Penetrance (note the two scales)")
