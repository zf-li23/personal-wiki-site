"""QTL mapping in a simulated backcross (F1 x parent, 200 individuals, seed 3): markers every 10 cM on a
100 cM chromosome, one QTL at 47 cM whose heterozygote raises the trait by 0.6 phenotypic SD units.
A: LOD profile of Haley-Knott interval mapping (line) and single-marker LOD scores (dots); the peak lies close
to the true QTL (triangle), the shaded band is the 1.5-LOD support interval, dashed the genome-wide 5 %
threshold from 200 permutations of the trait. B: the null distribution of the maximum LOD over the
chromosome obtained by permutation, with its 95 % quantile."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, gwas

P = bio.P
FT = bio.core.FONT
m = gwas.backcross_scan(200, qtl=47.0, effect=0.6, n_perm=200, rng=np.random.default_rng(3))
fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9), gridspec_kw={"width_ratios": [1.8, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.15, top=0.88, wspace=0.25)
peak, (lo, hi) = gwas.lod_profile(axs[0], m["x"], m["lod"], threshold=m["threshold"], markers=m["markers"], qtl=47.0,
                                  marker_lod=m["marker_lod"])
axs[0].text(99, m["threshold"] + 0.08, f"5% threshold {m['threshold']:.2f}", ha="right", va="bottom",
            fontsize=FT["tiny"], color=P.muted())
axs[0].text(hi + 1.5, m["lod"].max() * 0.85, f"peak {peak:.0f} cM\nsupport {lo:.0f}-{hi:.0f} cM", fontsize=FT["tiny"],
            color=P.ink())
charts.title(axs[0], "A  Interval mapping, true QTL at 47 cM")
b = axs[1]
b.hist(m["perm_max"], bins=20, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.6)
b.axvline(m["threshold"], color=charts.line("negative"), lw=1.2, ls="--")
b.axvline(m["lod"].max(), color=charts.line("dna"), lw=1.6)
b.text(m["lod"].max(), b.get_ylim()[1] * 0.9, " observed\n maximum", fontsize=FT["tiny"], color=charts.line("dna"), va="top")
charts.style_axes(b, "maximum LOD under permutation", "count")
charts.title(b, "B  Permutation threshold")
