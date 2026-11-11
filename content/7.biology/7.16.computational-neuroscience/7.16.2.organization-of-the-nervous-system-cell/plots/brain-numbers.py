"""Numbers of nervous systems (orders of magnitude from connectome reconstructions and isotropic
fractionation counts). A: neurons and chemical synapses of whole nervous systems: C. elegans
hermaphrodite (302 neurons, about 7000 synapses), adult Drosophila brain (about 1.4e5 neurons and
5e7 synapses, FlyWire), mouse (7e7 neurons, of order 1e11 synapses) and human (8.6e10 neurons,
of order 1e14 synapses); the dashed lines mark 10, 1000 and 10000 synapses per neuron.
B: distribution of neurons among cerebral cortex, cerebellum and the rest of the brain in mouse and
human (Herculano-Houzel and colleagues): in both, the cerebellum holds most neurons."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, (a1, a2) = plt.subplots(1, 2, figsize=(9.6, 3.6), gridspec_kw=dict(width_ratios=[1.25, 1]))
fig.subplots_adjust(wspace=0.4, left=0.09, right=0.97, bottom=0.17, top=0.88)
data = [("C. elegans", 302, 7.0e3), ("Drosophila", 1.4e5, 5e7), ("mouse", 7.1e7, 1e11), ("human", 8.6e10, 1.5e14)]
nn = np.logspace(2, 11.5, 10)
for k, lab in [(10, "10 per neuron"), (1e3, "10³"), (1e4, "10⁴")]:
    a1.plot(nn, k * nn, color=P.muted(), lw=0.7, ls="--")
    a1.text(nn[-1] / 2, k * nn[-1] / 2 * 1.5, lab, fontsize=FT["tiny"], color=P.muted(), ha="right", va="bottom")
for name, n, s in data:
    a1.plot(n, s, "o", color=charts.line("neuron"), ms=6)
    a1.text(n * 1.6, s / 1.8, name, fontsize=FT["tiny"], color=P.ink(), ha="left", va="top", style="italic" if name in ("C. elegans", "Drosophila") else "normal")
a1.set_xscale("log")
a1.set_yscale("log")
a1.set_xlim(1e2, 3e12)
a1.set_ylim(1e3, 1e16)
charts.style_axes(a1, "neurons", "synapses")
charts.title(a1, "A  Whole nervous systems")

regions = ["cerebral cortex", "cerebellum", "rest of brain"]
toks = ["neuron", "dna", "neutral"]
vals = {"mouse": [13.7e6, 42.4e6, 14.9e6], "human": [16.3e9, 69.0e9, 0.69e9]}
for i, (sp, v) in enumerate(vals.items()):
    frac = np.array(v) / sum(v)
    left = 0
    for f, tok, reg in zip(frac, toks, regions):
        a2.barh(i, f, left=left, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, label=reg if i == 0 else None)
        if f > 0.05:
            a2.text(left + f / 2, i, f"{100 * f:.0f}%", ha="center", va="center", fontsize=FT["tiny"], color=P.on_fill())
        left += f
    a2.text(1.02, i, ("7.1×10⁷" if sp == "mouse" else "8.6×10¹⁰"), fontsize=FT["tiny"], color=P.muted(), va="center")
a2.set_yticks([0, 1])
a2.set_yticklabels(list(vals))
a2.set_xlim(0, 1.32)
a2.set_ylim(-0.6, 2.2)
a2.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left", ncol=3, handlelength=1, columnspacing=0.8)
charts.style_axes(a2, "fraction of neurons")
charts.title(a2, "B  Where the neurons are")
