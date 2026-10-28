# Mapping complex traits with wikibio.gwas (seeds fixed). A: Manhattan plot of a simulated case-control scan
# (3000 cases, 3000 controls, 10 chromosomes, three causal SNPs with odds ratios 1.25-1.4 and their LD tags).
# B: QQ plot of the same p-values with the 95 % band and lambda_GC. C: r^2 triangle of 36 SNPs from haplotypes
# with two recombination hotspots (top track: physical positions). D: Haley-Knott interval mapping in a
# backcross of 250 individuals (markers every 10 cM, QTL at 47 cM), permutation threshold and 1.5-LOD interval.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts, gwas

fig = plt.figure(figsize=(11.5, 7.2))
gs = fig.add_gridspec(2, 3, width_ratios=[2.2, 1, 1.25], left=0.07, right=0.99, bottom=0.09, top=0.94,
                      wspace=0.32, hspace=0.42)
rng = np.random.default_rng(4)
d = gwas.simulate_case_control(3000, 3000, n_chrom=10, snps_per_chrom=500,
                               causal=[(2, 180, 1.4), (5, 300, 1.3), (8, 90, 1.25)], rng=rng)
a = fig.add_subplot(gs[0, :2])
gwas.manhattan(a, d["chrom"], d["pos"], d["p"], highlight=d["causal"])
charts.title(a, "A  Manhattan plot")
b = fig.add_subplot(gs[0, 2])
gwas.qq(b, d["p"])
charts.title(b, "B  QQ plot")
c = fig.add_subplot(gs[1, 0])
H, pos = gwas.simulate_haplotypes(400, 36, hotspots=[0.36, 0.71], rng=np.random.default_rng(7))
gwas.ld_triangle(c, gwas.ld_r2(H), pos=pos)
charts.title(c, "C  LD blocks between hotspots")
e = fig.add_subplot(gs[1, 1:])
m = gwas.backcross_scan(250, qtl=47.0, effect=0.7, rng=np.random.default_rng(3), n_perm=150)
peak, (lo, hi) = gwas.lod_profile(e, m["x"], m["lod"], threshold=m["threshold"], markers=m["markers"], qtl=47.0,
                                  marker_lod=m["marker_lod"])
e.text(peak + 2, m["lod"].max() * 1.02, f"peak {peak:.0f} cM, 1.5-LOD interval {lo:.0f}-{hi:.0f} cM",
       fontsize=bio.core.FONT["tiny"], color=bio.P.ink(), va="bottom")
e.text(98, m["threshold"] + 0.1, "5% permutation threshold", ha="right", va="bottom",
       fontsize=bio.core.FONT["tiny"], color=bio.P.muted())
charts.title(e, "D  Interval mapping in a backcross")
