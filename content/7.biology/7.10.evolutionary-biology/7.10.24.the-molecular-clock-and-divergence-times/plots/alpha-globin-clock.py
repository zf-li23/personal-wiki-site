"""The alpha-globin clock (Example 24.1.1). Percent amino acid differences in alpha-globin among eight
vertebrates (the classic table reproduced in Barton et al. (2007), Fig. 13.26; the shark, carp, dog and
human values also in Futuyma & Kirkpatrick (2017), Fig. 7.17), converted to Poisson distances
K = -ln(1 - p) and plotted against approximate fossil dates of the branch points.
A: comparisons of human with each other species. B: each branch point, averaging all comparisons
that span it (shark against the seven others, carp against the six others, and so on), which uses
every sequence. Lines: least-squares lines through the origin; their slope is 2k."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

species = ["shark", "carp", "newt", "chicken", "echidna", "kangaroo", "dog", "human"]
# Upper triangle of the percent-difference matrix: row i against species i+1, ..., human.
rows = {
    "shark": [59.4, 61.4, 59.7, 60.4, 55.4, 56.8, 53.2],
    "carp": [53.2, 51.4, 53.6, 50.7, 47.9, 48.6],
    "newt": [44.7, 50.4, 47.5, 46.1, 44.0],
    "chicken": [34.0, 29.1, 31.2, 24.8],
    "echidna": [34.8, 29.8, 26.2],
    "kangaroo": [23.4, 19.1],
    "dog": [16.3],
}
# Approximate ages (Mya) of the branch point separating each species from the lineage leading to human.
age = {"shark": 450, "carp": 405, "newt": 350, "chicken": 300, "echidna": 220, "kangaroo": 130, "dog": 80}

t = np.array([age[s] for s in species[:-1]], float)
k_human = np.array([-np.log(1 - rows[s][-1] / 100) for s in species[:-1]])
k_node = np.array([-np.log(1 - np.mean(rows[s]) / 100) for s in species[:-1]])

fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.0), sharey=True)
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.14, top=0.88, wspace=0.08)
panels = [(axes[0], k_human, "A  Human against each species", "dna"),
          (axes[1], k_node, "B  Averaged over each branch point", "rna")]
tt = np.linspace(0, 480, 10)
for ax, k, ttl, tok in panels:
    slope = (t @ k) / (t @ t)
    ax.plot(tt, slope * tt, color=charts.line(tok), lw=1, ls="--", zorder=2)
    ax.scatter(t, k, s=32, color=charts.line(tok), zorder=4)
    for s, ti, ki in zip(species[:-1], t, k):
        dy = -12 if s == "chicken" else 4
        ax.annotate(s, (ti, ki), xytext=(5, dy), textcoords="offset points", fontsize=FT["tiny"], color=P.ink())
    rate = slope / 2 * 1e3
    ax.text(0.04, 0.9, f"$k = {rate:.2f} \\times 10^{{-9}}$ per site per year", transform=ax.transAxes,
            fontsize=FT["tiny"], color=P.ink())
    ax.set_xlim(0, 480)
    ax.set_ylim(0, 1.0)
    charts.style_axes(ax, "age of branch point (Mya)", "Poisson distance $K = -\\ln(1 - p)$" if ax is axes[0] else None)
    charts.title(ax, ttl)
