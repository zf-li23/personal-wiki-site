# Transposon sequencing (Tn-seq): simulated data, to show how a library of transposon mutants measures the
# fitness contribution of every gene. A mariner transposon inserting at TA dinucleotides is modelled on a
# 30 kb stretch of a genome with ten genes: insertions are placed at random TA sites (density 1 per 40 bp),
# then the library is grown for 15 generations; the abundance of a mutant changes as 2^(15 w) with its
# relative fitness w (w = 1 neutral, w = 0 essential gene, 0 < w < 1 fitness cost in the condition tested).
# Reads are drawn as a multinomial sample of 300 000 reads from the final abundances.
# A: read counts at insertion sites along the segment; essential genes are empty, genes with a cost are
#    depleted. B: fitness estimated per gene from the log ratio of final to initial reads, against the true
#    value used in the simulation.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
L, GEN, READS = 30000, 15, 300000
# gene start, end, true relative fitness, name
GENES = [(600, 3300, 1.0, "g1"), (3600, 6000, 0.0, "g2 (essential)"), (6400, 8800, 1.0, "g3"),
         (9200, 12000, 0.55, "g4 (cost)"), (12400, 15000, 1.0, "g5"), (15400, 18200, 0.0, "g6 (essential)"),
         (18600, 21000, 1.0, "g7"), (21400, 23800, 0.8, "g8 (cost)"), (24200, 26800, 1.0, "g9"), (27200, 29600, 1.0, "g10")]

sites = np.sort(rng.choice(np.arange(50, L - 50), size=L // 40, replace=False))
w = np.ones(sites.size)
for a, b, wf, _ in GENES:
    inside = (sites >= a) & (sites < b)
    # insertions in the last 10 % of a gene often leave it functional: treat them as neutral
    tail = sites >= b - 0.1 * (b - a)
    w[inside & ~tail] = wf
n0 = rng.poisson(40, sites.size).astype(float) + 1
nt = n0 * 2.0 ** (GEN * w)
reads = rng.multinomial(READS, nt / nt.sum()).astype(float)
reads0 = rng.multinomial(READS, n0 / n0.sum()).astype(float)

fig = plt.figure(figsize=(12.5, 4.6))
gs = fig.add_gridspec(1, 2, width_ratios=[1.75, 1.0], wspace=0.3)

ax = fig.add_subplot(gs[0, 0])
ymax = reads.max()
ax.vlines(sites / 1000, 0, reads, color=P.edge("dna"), lw=0.8)
for a, b, wf, name in GENES:
    tok = "negative" if wf == 0 else "highlight" if wf < 1 else "positive"
    ax.add_patch(plt.Rectangle((a / 1000, -0.17 * ymax), (b - a) / 1000, 0.1 * ymax, facecolor=P.fill(tok),
                               edgecolor=P.edge(tok), lw=0.7, clip_on=False))
    ax.text((a + b) / 2000, -0.12 * ymax, name.split(" ")[0], ha="center", va="center", fontsize=6.4, color=P.on_fill())
ax.set_xlim(0, L / 1000)
ax.set_ylim(0, ymax * 1.05)
ax.spines["bottom"].set_position(("data", 0))
charts.style_axes(ax, "position / kb", "reads at insertion site")
ax.xaxis.labelpad = 44
for tok, text in (("positive", "no cost"), ("highlight", "fitness cost"), ("negative", "essential")):
    ax.add_patch(plt.Rectangle((0, 0), 0, 0, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, label=text))
ax.legend(fontsize=6.6, frameon=False, ncol=3, loc="upper right", bbox_to_anchor=(1.0, -0.22))
charts.title(ax, "A   Tn-seq read counts after 15 generations (simulated)")

ax = fig.add_subplot(gs[0, 1])
est, true, names = [], [], []
for a, b, wf, name in GENES:
    inside = (sites >= a) & (sites < b - 0.1 * (b - a))
    f1, f0 = reads[inside].sum(), reads0[inside].sum()
    est.append(np.log2(max(f1, 0.5) / max(f0, 0.5)) / GEN + 1.0)
    true.append(wf)
    names.append(name.split(" ")[0])
ax.plot([-0.05, 1.15], [-0.05, 1.15], color=P.muted(), lw=0.8, ls=":")
for t, e, n in zip(true, est, names):
    tok = "negative" if t == 0 else "highlight" if t < 1 else "positive"
    ax.plot([t], [e], "o", ms=6, color=P.fill(tok), markeredgecolor=P.edge(tok))
    if t < 1:
        ax.annotate(n, (t, e), (t + 0.09, e - 0.04), fontsize=6.4, color=P.ink())
ax.annotate("genes with no cost", (1.0, np.mean([e for t, e in zip(true, est) if t == 1])), (0.62, 1.1),
            fontsize=6.4, color=P.ink(), arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.6))
ax.set_xlim(-0.12, 1.2)
ax.set_ylim(-0.12, 1.2)
charts.style_axes(ax, "fitness used in the simulation", "fitness estimated from reads")
charts.title(ax, "B   Estimated fitness per gene")
