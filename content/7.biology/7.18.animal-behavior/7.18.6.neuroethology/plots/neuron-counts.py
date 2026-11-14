"""Approximate numbers of neurons in nervous systems used in neuroethology (published counts).

Filled bars: a complete connectome of the whole nervous system or brain has been published
(C. elegans, White et al. 1986; adult Drosophila central brain, FlyWire 2024).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
data = [
    ("Crab stomatogastric ganglion", 30, False),
    ("C. elegans (hermaphrodite)", 302, True),
    ("Aplysia (CNS)", 2e4, False),
    ("Zebrafish larva (brain)", 1e5, False),
    ("Drosophila (central brain)", 1.4e5, True),
    ("Honey bee (brain)", 1e6, False),
    ("Mouse (brain)", 7e7, False),
    ("Octopus (whole animal)", 5e8, False),
    ("Common raven (brain)", 2.2e9, False),
    ("Rhesus macaque (brain)", 6.4e9, False),
    ("Human (brain)", 8.6e10, False),
]
italic = {"C. elegans": "C. elegans", "Aplysia": "Aplysia", "Drosophila": "Drosophila"}
fig, ax = plt.subplots(figsize=(8.5, 4.6))
y = np.arange(len(data))[::-1]
for yi, (name, n, conn) in zip(y, data):
    ax.barh(yi, n, left=1, color=P.fill("neuron") if conn else "none", edgecolor=P.edge("neuron"), lw=1.2, height=0.62)
    e = int(np.floor(np.log10(n)))
    m = n / 10 ** e
    txt = f"{int(n)}" if n < 1e4 else (f"$10^{{{e}}}$" if abs(m - 1) < 0.05 else f"${m:.2g}\\times 10^{{{e}}}$")
    ax.text(n * 1.4, yi, txt, va="center", fontsize=8, color=P.muted())
ax.set_xscale("log")
ax.set_xlim(1, 1e12)
ax.set_yticks(y)
labels = []
for name, _, _ in data:
    for k in italic:
        if name.startswith(k):
            name = "$\\it{" + k.replace(" ", "\\ ") + "}$" + name[len(k):]
    labels.append(name)
ax.set_yticklabels(labels, fontsize=8.5)
ax.set_xlabel("Number of neurons")
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
ax.bar(0, 0, color=P.fill("neuron"), edgecolor=P.edge("neuron"), label="complete connectome published")
ax.bar(0, 0, color="none", edgecolor=P.edge("neuron"), label="no complete connectome")
ax.legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
