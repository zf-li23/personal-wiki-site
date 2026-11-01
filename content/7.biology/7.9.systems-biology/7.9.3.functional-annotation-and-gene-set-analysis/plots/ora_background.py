"""Two pitfalls of over-representation analysis (simulation). A: the background. A genome of 20000
genes, of which 8000 are expressed in the tissue studied; a 'neural' gene set of 400 genes, 300 of
them expressed. A list of 500 'differentially expressed' genes is drawn at random from the expressed
genes, so it has nothing to do with the set. One-sided hypergeometric p-values over 5000 such lists,
with all genes as background (the set looks enriched in most lists) and with the expressed genes as
background (uniform p-values, as they should be under the null). B: the size of the set. At a fixed
enrichment ratio of 1.5 (observed / expected overlap) and the same 10% of genes selected, the
p-value falls steadily as the set grows: in large, general sets small relative excesses become
'significant'."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
Ng, Ne, S, Se, K = 20000, 8000, 400, 300, 500
# overlap of a random list (drawn from expressed genes) with the set: hypergeometric(Ne, Se, K)
k = stats.hypergeom.rvs(Ne, Se, K, size=5000, random_state=rng)
p_all = stats.hypergeom.sf(k - 1, Ng, S, K)
p_expr = stats.hypergeom.sf(k - 1, Ne, Se, K)

fig, (a, b) = plt.subplots(1, 2, figsize=(9.6, 3.6))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.16, top=0.88, wspace=0.3)
bins = np.linspace(0, 1, 21)
a.hist(p_all, bins, color=P.fill("negative"), alpha=0.7, label=f"all {Ng} genes as background")
a.hist(p_expr, bins, color=P.fill("dna"), alpha=0.7, label=f"{Ne} expressed genes as background")
a.text(0.3, 0.62, f"p < 0.05 in {100 * np.mean(p_all < 0.05):.0f}% of lists\nvs {100 * np.mean(p_expr < 0.05):.1f}%",
       transform=a.transAxes, fontsize=8, color=P.ink())
a.legend(frameon=False, fontsize=7.5, loc="upper right")
charts.style_axes(a, "ORA p-value of the 'neural' set", "number of random lists")
charts.title(a, "A  Background genes matter")

N = 12000
sizes = np.unique(np.logspace(1, 3.3, 30).astype(int))
for frac, tok in [(0.1, "rna")]:
    Kb = int(frac * N)
    ks = np.round(1.5 * sizes * Kb / N).astype(int)
    pv = stats.hypergeom.sf(ks - 1, N, sizes, Kb)
    b.plot(sizes, pv, "o-", ms=3, lw=1.3, color=charts.line(tok))
b.axhline(0.05, color=P.muted(), ls="--", lw=0.8)
b.set_xscale("log")
b.set_yscale("log")
charts.style_axes(b, "genes in the set", "ORA p-value at enrichment ratio 1.5")
charts.title(b, "B  Large sets reach significance easily")
