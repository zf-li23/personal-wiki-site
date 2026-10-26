# What ribosome profiling reads out: a simulated mRNA (simulation, not data).
# Model: a 5' leader of 120 nt with a 10-codon uORF, a coding sequence of 300 codons and a 3' UTR. At low ribosome
# density (no queuing), the number of ribosomes at a codon is proportional to the flux J times the mean dwell
# time at that codon. Dwell times: 1/k per codon with k drawn from a distribution (codon-specific decoding
# rates, mean 6 codons/s), a 10-fold slower Pro-Pro-Pro motif at codon 180 (relieved by eIF5A), a 3-fold
# longer dwell at the start codon (initiation-to-elongation transition) and at the stop codon (termination).
# Footprint 5' ends are mapped to the P-site codon with 75 % of reads in frame 0 and 12.5 % in each other frame,
# and counts are Poisson.
# A: footprints along the mRNA (elongating ribosomes, cycloheximide-style snapshot); the uORF is translated, the
#    reading frame shows as 3-nt periodicity (inset) and the stall as a peak.
# B: with harringtonine or lactimidomycin, which stop ribosomes at initiation, only start codons remain:
#    the uORF AUG and the main AUG.
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(3)
L5, uorf, ncod, L3 = 120, (30, 10), 300, 150
nt = L5 + 3 * ncod + L3
dwell = np.zeros(nt // 3 + 1)
cds0 = L5 // 3
k = rng.gamma(4.0, 6.0 / 4.0, size=ncod)
dwell[cds0:cds0 + ncod] = 1 / k
dwell[cds0] *= 3
dwell[cds0 + ncod - 1] *= 3
dwell[cds0 + 180:cds0 + 183] *= 10
u0 = uorf[0] // 3
dwell[u0:u0 + uorf[1]] = 0.25 / rng.gamma(4.0, 6.0 / 4.0, size=uorf[1])
J = 2500.0
counts = np.zeros(nt)
for c in range(len(dwell)):
    lam = J * dwell[c]
    if lam <= 0:
        continue
    for f, w in ((0, 0.75), (1, 0.125), (2, 0.125)):
        pos = 3 * c + f
        if pos < nt:
            counts[pos] += rng.poisson(lam * w)

fig, axs = plt.subplots(2, 1, figsize=(12.6, 4.8), sharex=True, gridspec_kw={"height_ratios": [1.7, 1]})
ax = axs[0]
ax.bar(np.arange(nt), counts, width=1.0, color=charts.line("rrna"))
ax.set_ylim(0, counts.max() * 1.15)
ax.axvspan(L5, L5 + 3 * ncod, color=P.fill("positive"), alpha=0.15, lw=0)
ax.axvspan(uorf[0], uorf[0] + 3 * uorf[1], color=P.fill("highlight"), alpha=0.3, lw=0)
ax.text(uorf[0], counts.max() * 1.05, "uORF", fontsize=7, color=P.ink())
ax.text(L5 + 5, counts.max() * 1.05, "coding sequence", fontsize=7, color=P.ink())
ax.annotate("Pro-Pro-Pro stall", xy=(L5 + 3 * 180, counts[L5 + 540:L5 + 549].max()), xytext=(L5 + 3 * 120, counts.max() * 0.8),
            fontsize=7, color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
ax.annotate("start", xy=(L5, counts[L5]), xytext=(L5 - 60, counts.max() * 0.6), fontsize=7, color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
ax.annotate("stop", xy=(L5 + 3 * ncod - 3, counts[L5 + 3 * ncod - 3]), xytext=(L5 + 3 * ncod + 20, counts.max() * 0.6),
            fontsize=7, color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
charts.style_axes(ax, None, "footprints")
ax.set_title("A   Elongating ribosomes (simulated)", loc="left", fontsize=9, color=P.ink())
ins = ax.inset_axes([0.76, 0.5, 0.14, 0.38])
ins.set_facecolor("none")
frame = np.array([counts[L5 + f:L5 + 3 * ncod:3].sum() for f in range(3)])
ins.bar([0, 1, 2], frame / frame.sum(), color=[charts.line("rrna"), P.fill("neutral"), P.fill("neutral")])
ins.set_ylim(0, 1)
ins.set_xticks([0, 1, 2])
ins.set_xticklabels(["0", "+1", "+2"])
charts.style_axes(ins, "frame", None)
ins.tick_params(labelsize=6)

ax = axs[1]
start = np.zeros(nt)
start[uorf[0]] = rng.poisson(300)
start[L5] = rng.poisson(900)
start[uorf[0] + 1] = rng.poisson(30)
start[L5 + 1] = rng.poisson(90)
ax.bar(np.arange(nt), start, width=2.0, color=charts.line("positive"))
charts.style_axes(ax, "position on mRNA / nt", "footprints")
ax.set_title("B   Initiating ribosomes (harringtonine)", loc="left", fontsize=9, color=P.ink())
ax.set_xlim(0, nt)
fig.tight_layout()
