"""The barcode gap (simulated distances).

Pairwise distances between COI sequences of 12 species with 10 individuals each. Within a species, two
sequences coalesce at a time T ~ Exponential(mean 0.15 Myr) in the past; sequences of different species
coalesce at their split time, drawn uniformly from 2 to 12 Myr (panel A) or from 0.1 to 3 Myr for a
recently radiated group (panel B). Divergence accumulates at 2 % per Myr between two lineages
(1 % per lineage), and the observed p-distance follows the Jukes-Cantor relation
p = 3/4 (1 - exp(-4/3 x 0.02 T)).
A: within-species (blue) and between-species (red) distances are separated by a gap, and the common
threshold of 2 % assigns specimens correctly. B: in a young radiation the distributions overlap and no
threshold separates the species.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(5)
fig, ax = bio.canvas(21.0, 10.0)


def pdist(T):
    return 0.75 * (1 - np.exp(-4 / 3 * 0.02 * T))


def simulate(lo, hi, nsp=12, nind=10):
    within = pdist(rng.exponential(0.15, nsp * nind * (nind - 1) // 2))
    splits = rng.uniform(lo, hi, nsp * (nsp - 1) // 2)
    between = pdist(np.repeat(splits, nind * nind) + rng.exponential(0.15, splits.size * nind * nind))
    return 100 * within, 100 * between


for k, (lo, hi, title) in enumerate([(2.0, 12, "Old species: a barcode gap"), (0.1, 3, "Young radiation: no gap")]):
    pa = C.axes_at(ax, (2.0 + 10.5 * k, 1.6, 7.5, 6.8))
    w, b = simulate(lo, hi)
    bins = np.linspace(0, 22, 89)
    pa.hist(w, bins=bins, density=True, color=Q.line_color("dna"), alpha=0.55, label="within species")
    pa.hist(b, bins=bins, density=True, color=Q.line_color("negative"), alpha=0.55, label="between species")
    pa.axvline(2.0, color=P.ink(), lw=1.0, ls=(0, (4, 2)))
    pa.text(2.3, pa.get_ylim()[1] * 0.9, "2 % threshold", fontsize=FS["tiny"], color=P.ink())
    pa.set_xlim(0, 22)
    pa.set_yscale("log")
    pa.set_ylim(1e-3, 5)
    C.style_axes(pa, "pairwise COI distance (%)", "density (log scale)")
    pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
    bio.panel(ax, "AB"[k], (0.3 + 10.5 * k, 9.6))
    bio.label(ax, (2.0 + 10.5 * k, 9.2), title, size="small", bold=True, ha="left")
