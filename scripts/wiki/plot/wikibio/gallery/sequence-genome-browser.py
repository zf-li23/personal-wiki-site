# A genome-browser view of a synthetic locus: gene models, RNA-seq coverage before and after induction,
# ChIP-seq of H3K4me3 (active promoters) and of a transcription factor, with called peaks. The data are
# deterministic simulations (numpy seed), not measurements.
import numpy as np

import wikibio as bio
from wikibio import sequence

P = bio.P
start, end = 1_200_000, 1_218_000
fig, ax = bio.canvas(19, 10.2)
gb = sequence.Browser(ax, (start, end), 3.4, 18.7, chrom="chr5")

rng = np.random.default_rng(7)
pos = np.arange(start, end, 20) + 10
exons_a = [(1_206_000, 1_206_420), (1_208_100, 1_208_260), (1_209_400, 1_209_610), (1_211_300, 1_211_450), (1_213_200, 1_214_300)]
cds_a = (1_206_250, 1_213_700)
exons_b = [(1_200_400, 1_201_300), (1_202_200, 1_202_380), (1_203_300, 1_203_700)]  # minus strand, TSS at 1,203,700


def smooth(v, k):
    w = np.exp(-0.5 * (np.arange(-3 * k, 3 * k + 1) / k) ** 2)
    return np.convolve(v, w / w.sum(), mode="same")


def coverage(exons, level):
    inside = np.zeros(len(pos))
    for s, e in exons:
        inside[(pos >= s) & (pos < e)] = 1
    mean = level * inside * (0.75 + 0.25 * np.linspace(0, 1, len(pos))) + 0.02 * level
    return smooth(rng.gamma(4, mean / 4), 2)


def chip(centres, width, height, background=1.0):
    mu = background + sum(h * np.exp(-0.5 * ((pos - c) / w) ** 2) for c, w, h in zip(centres, width, height))
    return smooth(rng.poisson(mu).astype(float), 3)


rna_ctrl = coverage(exons_a, 12) + coverage(exons_b, 30)
rna_ind = coverage(exons_a, 95) + coverage(exons_b, 30)
# H3K4me3 flanks the nucleosome-depleted region at each TSS (two humps)
k4 = chip([1_205_700, 1_206_500, 1_203_950, 1_203_300], [350, 450, 350, 400], [26, 34, 20, 24], background=1.5)
tf = chip([1_205_850, 1_203_800, 1_202_050], [90, 90, 110], [60, 30, 22], background=1.2)

y_axis, y_gene, y_r1, y_r2, y_k4, y_tf, y_pk = 9.4, 8.2, 6.4, 4.7, 3.0, 1.35, 0.55
gb.highlight(1_201_850, 1_202_250, 0.25, 9.0)
gb.axis(y_axis)
gb.gene(y_gene, exons_a, strand="+", name="geneA", cds=cds_a)
gb.gene(y_gene, exons_b, strand="-", name="geneB", cds=(1_200_900, 1_203_500))
gb.track_label(y_gene, "Genes")
top = sequence.nice_ceil(max(rna_ctrl.max(), rna_ind.max()))  # the same scale for both conditions
gb.signal(y_r1, 1.2, rna_ctrl, pos, token="rna", label="RNA-seq, control", ymax=top)
gb.signal(y_r2, 1.2, rna_ind, pos, token="rna", label="RNA-seq, induced", ymax=top)
gb.signal(y_k4, 1.2, k4, pos, token="chromatin", label="H3K4me3 ChIP")
gb.signal(y_tf, 1.2, tf, pos, token="enzyme", label="TF ChIP")
# peaks: contiguous runs of the TF signal above a threshold
above = tf > 12
edges = np.flatnonzero(np.diff(np.r_[0, above.astype(int), 0]))
peaks = [(pos[a], pos[b - 1]) for a, b in zip(edges[::2], edges[1::2])]
gb.peaks(y_pk, peaks, token="enzyme", label="TF peaks")
bio.label(ax, (gb.x(1_202_050), 9.0), "enhancer", size="tiny", color=P.muted(), va="bottom")
