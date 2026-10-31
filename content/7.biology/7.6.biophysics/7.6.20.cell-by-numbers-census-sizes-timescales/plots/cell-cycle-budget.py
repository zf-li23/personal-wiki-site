"""The material budget of one E. coli cell cycle and the machines that pay it.

Doubling time tau = 3000 s (minimal medium with glucose, 37 C). A: average rates needed to double the
cell's content in tau, from the census (counts from Neidhardt 1990): carbon atoms (about 1e10 per cell,
supplied as glucose, 6 C each), water (2.3e10), amino acids into protein (2.4e6 proteins of about 300
residues), phospholipids (2.2e7), base pairs of DNA (4.6e6) and nucleotides into stable RNA (rRNA of
1.9e4 ribosomes at 4566 nt each plus 2e5 tRNAs of 76 nt). B: number of machines working at their
measured speeds needed to sustain these rates (bars), compared with the number present (diamonds):
replication forks at 1000 bp/s, ribosomes at 15 amino acids per second and RNA polymerases on rRNA
and tRNA genes at 60 nt/s; the census and the speeds are consistent."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
tau = 3000.0
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
rows = [
    ("water molecules", 2.3e10 / tau, "neutral"),
    ("carbon atoms", 1e10 / tau, "metabolite"),
    ("glucose molecules", 1e10 / 6 / tau, "carbohydrate"),
    ("amino acids into protein", 2.4e6 * 300 / tau, "protein"),
    ("nucleotides into stable RNA", (1.9e4 * 4566 + 2e5 * 76) / tau, "rrna"),
    ("phospholipids", 2.2e7 / tau, "lipid_head"),
    ("base pairs of DNA", 4.6e6 / tau, "dna"),
]
fig, axs = plt.subplots(1, 2, figsize=(10.4, 3.6), gridspec_kw={"width_ratios": [1.3, 1]})
fig.subplots_adjust(wspace=0.7, left=0.17, right=0.97, bottom=0.17, top=0.88)
ax = axs[0]
ys = np.arange(len(rows))[::-1]
for y, (name, r, tok) in zip(ys, rows):
    ax.barh(y, r, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
    e = int(np.floor(np.log10(r)))
    ax.text(r * 1.4, y, f"{r / 10 ** e:.1f} × 10" + str(e).translate(SUP), va="center",
            fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_yticks(ys)
ax.set_yticklabels([r[0] for r in rows], fontsize=bio.core.FONT["tiny"])
ax.set_xscale("log")
ax.set_xlim(1e2, 1e9)
charts.style_axes(ax, "rate needed / s⁻¹")
charts.title(ax, "A  Rates to double in 3000 s")

ax = axs[1]
need = [
    ("replication forks", 4.6e6 / tau / 1000, 2, "dna"),
    ("RNA polymerases on\nrRNA and tRNA genes", (1.9e4 * 4566 + 2e5 * 76) / tau / 60, 1000, "mrna"),
    ("ribosomes", 2.4e6 * 300 / tau / 15, 1.9e4, "rrna"),
]
ys = np.arange(len(need))[::-1]
for y, (name, n, have, tok) in zip(ys, need):
    ax.barh(y, n, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8)
    ax.plot(have, y, "D", mfc="none", mec=P.ink(), ms=7, mew=1.2)
ax.plot([], [], "D", mfc="none", mec=P.ink(), ms=6, ls="none", label="present in the cell")
ax.set_yticks(ys)
ax.set_yticklabels([n[0] for n in need], fontsize=bio.core.FONT["tiny"])
ax.set_xscale("log")
ax.set_xlim(0.5, 1e5)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "number of machines")
charts.title(ax, "B  Machines needed")
