"""Four probability sampling designs drawing 12 units from a population of 120 people arranged in four
strata (rows of colour: for example age groups) and twenty clusters (blocks of six: for example households
or villages). Simple random: every set of 12 is equally likely. Systematic: every 10th person on the list
after a random start. Stratified: 3 at random from each stratum. Cluster: all members of 2 randomly chosen
clusters. Schematic; selections drawn with random seed 0.
"""
import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)
rows, cols = 4, 30                     # 4 strata x 30 people; clusters are blocks of 6 within a row
size = 6
idx = np.arange(rows * cols)
strata = ["dna", "rna", "enzyme", "plant"]

simple = set(rng.choice(idx, 12, replace=False))
start = int(rng.integers(0, 10))
systematic = set(range(start, rows * cols, 10))
stratified = set()
for r in range(rows):
    stratified |= set(rng.choice(np.arange(r * cols, (r + 1) * cols), 3, replace=False))
cluster = set()
for c in rng.choice(rows * cols // size, 2, replace=False):
    cluster |= set(range(c * size, c * size + size))

designs = [("A  Simple random", simple), ("B  Systematic (every 10th)", systematic),
           ("C  Stratified (3 per stratum)", stratified), ("D  Cluster (2 whole clusters)", cluster)]
fig, axs = plt.subplots(2, 2, figsize=(10.0, 3.6))
fig.subplots_adjust(left=0.02, right=0.98, bottom=0.03, top=0.90, wspace=0.06, hspace=0.32)
for ax, (name, chosen) in zip(axs.flat, designs):
    for i in idx:
        r, c = divmod(i, cols)
        x, y = c + (c // size) * 0.8, rows - 1 - r
        tok = strata[r]
        if i in chosen:
            ax.add_patch(plt.Circle((x, y), 0.36, facecolor=P.edge(tok), edgecolor=P.ink(), lw=0.8))
        else:
            ax.add_patch(plt.Circle((x, y), 0.30, facecolor=P.light(tok), edgecolor=P.fill(tok), lw=0.5))
    for k in range(1, cols // size):
        ax.axvline(k * (size + 0.8) - 0.9, color=P.muted(), lw=0.6, ls=":")
    ax.set_xlim(-0.8, cols + 0.8 * (cols // size - 1))
    ax.set_ylim(-0.7, rows - 0.3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.text(cols + 0.8 * (cols // size - 1), rows - 0.2, f"n = {len(chosen)}", ha="right", va="bottom", fontsize=FT["tiny"], color=P.muted())
    charts.title(ax, name)
