# Cell-cycle analysis by flow cytometry: histograms of DNA content (fluorescence of a stoichiometric DNA
# dye such as propidium iodide) for 20,000 simulated cells. G1 cells have 2C, G2 and M cells 4C, S-phase cells
# a content between, distributed uniformly in this simple model (constant replication rate); each cell's
# signal is blurred by a 4% coefficient of variation.
# A: asynchronous culture, 55% G1, 30% S, 15% G2/M. B: the same culture after a mitotic block (nocodazole),
# which accumulates cells with 4C DNA: 15% G1, 20% S, 65% G2/M. Shaded: the contributions of each phase.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(5)
cv, N = 0.04, 20000


def population(fg1, fs, fg2):
    n1, ns = int(N * fg1), int(N * fs)
    n2 = N - n1 - ns
    dna = [np.full(n1, 2.0), rng.uniform(2.0, 4.0, ns), np.full(n2, 4.0)]
    return [d * (1 + cv * rng.normal(size=d.size)) for d in dna]


edges = np.linspace(1.0, 5.0, 161)
fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.6), sharey=True)
for ax, (f, title) in zip(axs, (((0.55, 0.30, 0.15), "A   Asynchronous culture"),
                                ((0.15, 0.20, 0.65), "B   After a mitotic block"))):
    parts = population(*f)
    bottom = np.zeros(len(edges) - 1)
    for d, txt, tok in zip(parts, ("G1 (2C)", "S", "G2/M (4C)"), ("dna", "positive", "negative")):
        h, _ = np.histogram(d, edges)
        ax.bar(edges[:-1], h, width=np.diff(edges), bottom=bottom, align="edge", color=P.fill(tok), edgecolor="none",
               label=f"{txt}: {d.size / N:.0%}")
        bottom += h
    ax.step(edges[:-1], bottom, where="post", color=P.ink(), lw=0.8)
    ax.set_xlim(1, 5)
    ax.set_xticks([2, 3, 4])
    ax.set_xticklabels(["2C", "3C", "4C"])
    ax.legend(fontsize=7, frameon=False, loc="upper right")
    charts.style_axes(ax, "DNA content (fluorescence)", "cells per bin" if ax is axs[0] else None)
    ax.set_title(title, loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
