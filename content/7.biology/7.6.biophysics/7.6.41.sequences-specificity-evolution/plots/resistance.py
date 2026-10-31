# The numbers of drug resistance. A: probability that a population of N replicating genomes already
# contains a variant carrying k specific point mutations, 1 - exp(-N mu^k), for HIV (mu = 3e-5 per base
# per replication cycle, k = 1, 2, 3) and for a bacterium with a target-specific resistance mutation
# rate of 1e-8 per cell (k = 1, 2); shaded: the about 1e10 virions produced per day in an untreated
# patient and 1e9-1e11 bacteria in a large infection. B: the mutant selection window. Net growth rate
# lambda(c) = lambda_max / (1 + (c/IC50)^h) - delta against drug concentration for a sensitive strain
# (lambda_max = 1, IC50 = 1) and a resistant mutant with a fitness cost (lambda_max = 0.9, IC50 = 8),
# h = 2, delta = 0.1 per hour: between the concentration where the mutant starts to outgrow the
# sensitive strain and the mutant's own minimal inhibitory concentration, the drug selects resistance.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.0))
ax = axs[0]
N = np.logspace(2, 13, 300)
for mu, kk, tok, lab in ((3e-5, 1, "virus", "HIV, 1 mutation"), (3e-5, 2, "rna", "HIV, 2 mutations"),
                         (3e-5, 3, "negative", "HIV, 3 mutations"), (1e-8, 1, "bacterium", "bacterium, 1 mutation"),
                         (1e-8, 2, "dna", "bacterium, 2 mutations")):
    ax.plot(N, -np.expm1(-N * mu**kk), color=charts.line(tok), lw=1.8, ls="-" if mu > 1e-6 else "--", label=lab)
ax.axvspan(5e9, 2e10, color=P.fill("virus"), alpha=0.3, lw=0)
ax.axvspan(1e9, 1e11, color=P.fill("bacterium"), alpha=0.2, lw=0)
ax.set_xscale("log")
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "population size $N$", "P(resistant variant pre-exists)")
charts.title(ax, "A   Why combination therapy works")

ax = axs[1]
c = np.logspace(-1, 2, 400)
h, delta = 2.0, 0.1
wt = 1.0 / (1 + (c / 1.0) ** h) - delta
mt = 0.9 / (1 + (c / 8.0) ** h) - delta
ax.plot(c, wt, color=charts.line("positive"), lw=2.0, label="sensitive")
ax.plot(c, mt, color=charts.line("negative"), lw=2.0, label="resistant, with cost")
c_lo = c[np.argmax(mt > wt)]
c_hi = c[np.argmax(mt < 0)]
ax.axvspan(c_lo, c_hi, color=P.fill("highlight"), alpha=0.35, lw=0)
ax.text(np.sqrt(c_lo * c_hi), 0.85, "selection\nwindow", ha="center", fontsize=8, color=P.ink())
ax.axhline(0, color=P.muted(), lw=0.7)
ax.set_xscale("log")
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(ax, "drug concentration / IC50 of sensitive strain", "net growth rate / h$^{-1}$")
charts.title(ax, "B   The mutant selection window")
fig.tight_layout()
