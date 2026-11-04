# Operational species boundaries for prokaryotes (simulated genome pairs).
# Each pair of genomes has a genome-wide divergence d (substitutions per site). Genome-wide identity
# (ANI) and 16S rRNA gene identity both follow the Jukes-Cantor relation p = 3/4 (1 - exp(-4 d / 3)),
# the 16S gene evolving at a fraction r of the genome-wide rate (r = 0.25, varying lognormally among
# lineages, sd 0.35 on the log scale) and being only 1500 nt long (binomial sampling of differences).
# Pairs within a species have small d (ANI 96-100 %), pairs from different species of a genus larger d,
# which reproduces the gap in ANI between about 83 and 95 % found in large genome surveys.
# A: ANI against 16S identity, coloured by the true relationship; dashed lines are the 95 % ANI and
#    98.7 % 16S thresholds. Below 98.7 % 16S almost all pairs are different species, above it both occur.
# B: the distribution of ANI over all pairs, with its gap.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)


def identity(d):
    return 100 * (1 - 0.75 * (1 - np.exp(-4 * d / 3)))


n_same, n_diff = 260, 420
d_same = np.minimum(rng.gamma(1.6, 0.011, n_same), 0.048)   # within species: ANI mostly 97-100 %
d_diff = rng.uniform(0.21, 0.36, n_diff)                    # between species of related genera
d_diff = np.concatenate([d_diff, rng.uniform(0.05, 0.14, 25)])  # a few close sister species
d = np.concatenate([d_same, d_diff])
same = np.r_[np.ones(n_same, bool), np.zeros(n_diff + 25, bool)]
r = 0.25 * np.exp(rng.normal(0, 0.35, d.size))
ani = identity(d) + rng.normal(0, 0.15, d.size)
p16 = 1 - identity(r * d) / 100
s16 = 100 * (1 - rng.binomial(1500, np.clip(p16, 0, 1)) / 1500)

fig, axs = plt.subplots(1, 2, figsize=(11.0, 4.3), gridspec_kw=dict(wspace=0.3, width_ratios=[1.25, 1]))

ax = axs[0]
ax.scatter(s16[~same], ani[~same], s=9, color=charts.line("negative"), alpha=0.75, lw=0,
           label="different species")
ax.scatter(s16[same], ani[same], s=9, color=charts.line("dna"), alpha=0.75, lw=0, label="same species")
ax.axhline(95, color=P.ink(), lw=0.9, ls="--")
ax.axvline(98.7, color=P.ink(), lw=0.9, ls="--")
ax.text(91.2, 95.6, "ANI 95 %", fontsize=7, color=P.ink())
ax.text(98.6, 75.6, "16S 98.7 %", fontsize=7, color=P.ink(), ha="right")
ax.text(91.2, 88.0, "below 98.7 %:\ndifferent species", fontsize=6.8, color=P.muted())
ax.set_xlim(91, 100.2)
ax.set_ylim(75, 100.5)
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "16S rRNA gene identity / %", "average nucleotide identity / %")
charts.title(ax, "A   16S identity is necessary, not sufficient")

ax = axs[1]
bins = np.arange(74, 100.6, 0.75)
ax.hist([ani[~same], ani[same]], bins=bins, stacked=True, color=[charts.line("negative"), charts.line("dna")],
        label=["different species", "same species"])
ax.axvspan(83, 95, color=P.fill("neutral"), alpha=0.3, lw=0, zorder=0)
ax.text(89, ax.get_ylim()[1] * 0.85, "few pairs\n(83-95 %)", ha="center", fontsize=7, color=P.ink())
ax.axvline(95, color=P.ink(), lw=0.9, ls="--")
ax.legend(fontsize=7, frameon=False, loc="upper left")
charts.style_axes(ax, "average nucleotide identity / %", "number of genome pairs")
charts.title(ax, "B   A gap in ANI near the species boundary")
