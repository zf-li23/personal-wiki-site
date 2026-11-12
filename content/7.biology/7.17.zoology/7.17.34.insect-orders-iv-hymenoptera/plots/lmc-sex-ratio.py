# Local mate competition (Hamilton 1967): when n foundresses lay eggs in a patch and their offspring mate
# there before the daughters disperse, sons compete with brothers for mates, and the evolutionarily
# stable proportion of sons falls below 1/2. For diploids x* = (n - 1) / (2n) (Hamilton 1967); for
# haplodiploids, in which a mother is more related to daughters, x* = (n - 1)(2n - 1) / (n (4n - 1))
# (Hamilton 1979; Taylor and Bulmer 1980). Curves are theory, not data.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(16, 9.5)
a = charts.axes_at(ax, (1.8, 1.4, 13.4, 7.4))
n = np.arange(1, 21)
nn = np.linspace(1, 20, 400)
dip = (nn - 1) / (2 * nn)
hap = (nn - 1) * (2 * nn - 1) / (nn * (4 * nn - 1))
a.plot(nn, dip, color=P.edge("negative"), lw=2, label="diploid: (n - 1) / 2n")
a.plot(nn, hap, color=P.edge("positive"), lw=2, label="haplodiploid: (n - 1)(2n - 1) / n(4n - 1)")
a.plot(n, (n - 1) * (2 * n - 1) / (n * (4 * n - 1)), "o", color=P.edge("positive"), ms=3.5)
a.axhline(0.5, color=P.muted(), lw=0.8, ls="--")
a.text(19.8, 0.51, "Fisherian 1:1", ha="right", va="bottom", fontsize=7, color=P.muted())
a.set_xlim(0.5, 20.5)
a.set_ylim(0, 0.56)
a.set_xlabel("Number of foundresses laying eggs in a patch, n")
a.set_ylabel("Stable proportion of sons, x*")
a.legend(fontsize=7, frameon=False, loc="lower right")
a.annotate("one foundress: just enough sons\nto mate with all sisters", xy=(1, 0.0), xytext=(2.5, 0.12), fontsize=7,
           color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
