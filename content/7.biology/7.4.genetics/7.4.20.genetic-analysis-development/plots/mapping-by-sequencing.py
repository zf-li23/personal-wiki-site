"""Mapping by sequencing (simulation). Mutant F2 individuals from a cross to a polymorphic strain are
pooled and sequenced; the plot shows, at each marker, the fraction of reads carrying the allele of the
mutant parent. The expectation is 1 - r(d) with the Haldane mapping function, peaking at the mutation."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts
from wikibio import transmission as T

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
pos = np.linspace(0, 80, 81)          # cM along the chromosome
mut = 46.0                            # position of the causative mutation
d = np.abs(pos - mut) / 100.0
f = 1 - T.haldane(d)                  # expected frequency of the mutant parent's allele

fig, ax = plt.subplots(figsize=(9.4, 4.0))
fig.subplots_adjust(left=0.09, right=0.98, bottom=0.15, top=0.9)
ax.plot(pos, f, color=P.muted(), lw=1.6, label=r"expectation $1 - r(d)$")
depth = 300
for n, tok, ms in ((20, "dna", 5), (200, "receptor", 4)):
    # each mutant individual contributes two chromosomes; reads sample the pooled alleles
    k = rng.binomial(2 * n, f) / (2 * n)
    obs = rng.binomial(depth, k) / depth
    ax.plot(pos, obs, "o", color=charts.line(tok), ms=ms, alpha=0.85, label=f"pool of {n} mutants")
ax.axvline(mut, color=charts.line("positive"), lw=1.0, ls="--")
ax.text(mut + 1.2, 0.52, "mutation", fontsize=FT["small"], color=charts.line("positive"))
ax.axhline(0.5, color=P.muted(), lw=0.7, ls=":")
ax.set_ylim(0.44, 1.08)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "position along the chromosome / cM", "fraction of reads from the mutant parent")
