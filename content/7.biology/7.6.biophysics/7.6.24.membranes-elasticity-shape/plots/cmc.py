"""Self-assembly of amphiphiles. A: mass-action model of micellization with aggregation number
N = 60: the concentration of aggregates is X_N = N (X_1 / X_c)^N X_c (mole fraction units), where
X_c = exp(-Delta mu / kB T) is set by the free-energy gain per molecule on joining an aggregate.
Below the critical micelle concentration X_c almost all molecules are free; above it the free
monomer concentration stays nearly constant and every added molecule joins an aggregate.
B: measured critical micelle concentrations against the number of carbons per chain: single-chain
sodium alkyl sulfates (sodium dodecyl sulfate: 8.2 mM) and two-chain diacylphosphatidylcholines;
each CH2 lowers the CMC about twofold (ionic) to threefold (lipids), and a second chain lowers it by
orders of magnitude: free monomers of membrane phospholipids are at sub-nanomolar concentrations."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(8.8, 3.3))
fig.subplots_adjust(wspace=0.38, left=0.09, right=0.97, bottom=0.17, top=0.87)

ax = axs[0]
N, Xc = 60, 1.0
tot = np.logspace(-1, 1, 300)
X1 = []
for T in tot:
    f = lambda x: x + N * x**N - T  # in units of Xc (X_N counted as molecules in aggregates)
    X1.append(brentq(f, 0, T))
X1 = np.array(X1)
ax.plot(tot, X1, color=charts.line("lipid_head"), lw=1.8, label="free monomers")
ax.plot(tot, tot - X1, color=charts.line("dna"), lw=1.8, label="in micelles")
ax.axvline(1, color=P.muted(), lw=0.7, ls=":")
ax.text(1.1, 4, "CMC", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, "total amphiphile / CMC", "concentration / CMC")
charts.title(ax, "A  A sharp onset (N = 60)")

ax = axs[1]
sulf = {8: 0.13, 10: 3.3e-2, 12: 8.2e-3, 14: 2.1e-3, 16: 5.2e-4}  # M
pc = {6: 1.5e-2, 7: 1.4e-3, 8: 2.7e-4, 10: 5e-6, 12: 9e-8, 14: 6e-9, 16: 4.6e-10}  # M
ax.plot(list(sulf), list(sulf.values()), "o-", color=charts.line("lipid_head"), ms=4, lw=1, label="sodium alkyl sulfates (1 chain)")
ax.plot(list(pc), list(pc.values()), "s-", color=charts.line("dna"), ms=4, lw=1, label="diacyl-PC (2 chains)")
ax.annotate("SDS", (12, 8.2e-3), (12.6, 8e-2), fontsize=bio.core.FONT["tiny"], color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
ax.annotate("DPPC", (16, 4.6e-10), (14.6, 3e-11), fontsize=bio.core.FONT["tiny"], color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
ax.set_yscale("log"); ax.set_ylim(1e-11, 1)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
charts.style_axes(ax, "carbons per chain", "CMC / M")
charts.title(ax, "B  Longer and more chains")
