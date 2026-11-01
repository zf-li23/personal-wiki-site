"""Gene set enrichment analysis of the airway data for the Hallmark set 'TNF-alpha signaling via
NF-kB' (MSigDB, CC BY 4.0). The 18865 tested genes are ranked by the DESeq2 Wald statistic of
dexamethasone against untreated (pydeseq2), from most induced (left) to most repressed. A: the
ranking metric along the list. B: positions of the 176 genes of the set. C: the running sum, which
rises at each member by its |metric| / (sum of |metric| over members) and falls by 1/(N - n) at each
non-member; its maximum deviation from zero is the enrichment score ES, and the members before the
peak form the leading edge (shaded). D: ES of 2000 random gene sets of the same size (histogram)
against the observed ES (line)."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
with open("tnfa_gsea.csv") as f:
    head = f.readline()
    f.readline()
    prof = np.array([float(v) for v in f.readline().split(",")])
    pos, w = [], []
    null = None
    for line in f:
        if line.startswith("null"):
            null = np.array([float(v) for v in line.split(",")[1:]])
        else:
            a, b = line.split(",")
            pos.append(int(a))
            w.append(float(b))
pos, w = np.array(pos), np.array(w)
N = int(head.split("N=")[1].split(";")[0])
n = len(pos)
hit = np.zeros(N)
hit[pos] = w / w.sum()
miss = np.full(N, 1 / (N - n))
miss[pos] = 0
rs = np.cumsum(hit - miss)
j = np.argmax(np.abs(rs))
es = rs[j]

fig = plt.figure(figsize=(11, 4.2))
a = fig.add_axes([0.06, 0.62, 0.58, 0.28])
b = fig.add_axes([0.06, 0.52, 0.58, 0.08])
c = fig.add_axes([0.06, 0.14, 0.58, 0.36])
d = fig.add_axes([0.72, 0.14, 0.26, 0.76])
xs = np.linspace(0, N - 1, prof.size)
a.fill_between(xs, prof, color=P.fill("neutral"), lw=0)
a.plot(xs, prof, color=P.edge("neutral"), lw=0.8)
a.set_xlim(0, N)
a.set_xticks([])
charts.style_axes(a, None, "Wald statistic")
charts.title(a, "A-C  Running sum along the ranked list")
b.vlines(pos, 0, 1, color=charts.line("rna"), lw=0.6)
b.set_xlim(0, N)
b.axis("off")
c.plot(np.arange(N), rs, color=charts.line("dna"), lw=1.5)
c.axhline(0, color=P.muted(), lw=0.7)
c.axvspan(0, j, color=P.fill("highlight"), alpha=0.35, lw=0)
c.plot(j, es, "o", color=charts.line("negative"), ms=4)
c.text(j + 400, es - 0.04, f"ES = {es:.2f} at rank {j + 1}\nleading edge: {np.sum(pos <= j)} genes", fontsize=7.5, color=P.ink(), va="top")
c.set_xlim(0, N)
charts.style_axes(c, "rank in the list (induced to repressed)", "running sum")
d.hist(null, bins=40, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.4)
d.axvline(es, color=charts.line("negative"), lw=1.4)
pval = (1 + np.sum(null >= es)) / (null.size + 1)
nes = es / null[null >= 0].mean()
d.text(0.04, 0.9, f"random sets with ES >= observed: {np.sum(null >= es)}\np = {pval:.4f}, NES = {nes:.2f}", transform=d.transAxes, fontsize=7.5, color=P.ink())
charts.style_axes(d, "ES of random sets", "count")
charts.title(d, "D  Permutation null")
