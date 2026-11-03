"""The distribution of fitness effects of new deleterious mutations (Definition 4.4.1), modeled as a
gamma distribution of the selection coefficient |s| with shape 0.2 and mean 0.04, chosen so that about
12 percent of mutations have |s| > 0.1 (illustrative values; shapes of about 0.2 have been estimated for
nonsynonymous mutations in humans). A: the distribution of log10 |s|: a few mutations are strongly
deleterious, most are mildly deleterious or nearly neutral. B: the fraction of mutations that behave
as effectively neutral, |4 N_e s| < 1, as a function of the effective population size: the same
mutations are mostly neutral in a small population and mostly selected in a large one."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
shape = 0.2
scale = 0.04 / shape
g = stats.gamma(shape, scale=scale)
fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.4))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.17, top=0.86, wspace=0.3)
x = np.linspace(-9, 0.3, 400)
s = 10.0 ** x
dens = g.pdf(s) * s * np.log(10)
a.fill_between(x, dens, color=P.fill("negative"), edgecolor=P.edge("negative"), lw=1.0)
a.axvline(-1, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
a.text(-0.9, dens.max() * 0.9, f"$|s| > 0.1$:\n{g.sf(0.1):.0%}", fontsize=FT["tiny"], color=P.ink(), va="top")
a.set_xlim(-9, 0.3)
a.set_ylim(0, None)
charts.style_axes(a, r"$\log_{10}|s|$", "density")
charts.title(a, "A  Effects of new deleterious mutations")
Ne = np.logspace(2, 7, 200)
b.semilogx(Ne, g.cdf(1 / (4 * Ne)), color=charts.line("dna"), lw=1.8)
for n0, txt in ((1e4, "humans,\n$N_{\\mathrm{e}} \\approx 10^4$"), (1e6, "$D.\\ melanogaster$,\n$N_{\\mathrm{e}} \\approx 10^6$")):
    f = g.cdf(1 / (4 * n0))
    b.plot([n0], [f], "o", color=P.edge("rna"), ms=5)
    b.text(n0 * 1.3, f + 0.03, f"{txt}: {f:.0%}", fontsize=FT["tiny"], color=P.ink())
b.set_ylim(0, 0.6)
charts.style_axes(b, r"effective population size $N_{\mathrm{e}}$", r"fraction with $|4N_{\mathrm{e}}s| < 1$")
charts.title(b, "B  Effectively neutral fraction")
