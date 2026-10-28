"""Mutational processes read from the spectrum of somatic mutations (illustrative values in the proportions
reported for the corresponding reference signatures). A: the six classes of base substitution for four
processes. B: tumor mutational burden by cancer type, on a logarithmic scale."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
classes = ["C>A", "C>G", "C>T", "T>A", "T>C", "T>G"]
procs = [("Ageing (C>T at CpG)", [0.10, 0.06, 0.60, 0.05, 0.14, 0.05], "neutral"),
         ("Tobacco smoke", [0.55, 0.10, 0.17, 0.08, 0.06, 0.04], "metabolite"),
         ("Ultraviolet light", [0.04, 0.04, 0.82, 0.03, 0.04, 0.03], "highlight"),
         ("Mismatch-repair defect", [0.08, 0.04, 0.52, 0.04, 0.26, 0.06], "receptor")]

fig, axs = plt.subplots(1, 2, figsize=(11.0, 4.0), gridspec_kw={"width_ratios": [1.3, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.18, top=0.88, wspace=0.3)

a = axs[0]
x = np.arange(len(classes))
w = 0.2
for k, (name, vals, tok) in enumerate(procs):
    a.bar(x + (k - 1.5) * w, vals, width=w * 0.92, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.7, label=name)
a.set_xticks(x)
a.set_xticklabels(classes, fontsize=FT["small"])
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink())
charts.style_axes(a, "class of base substitution (pyrimidine of the pair)", "fraction of substitutions")
charts.title(a, "A  Signatures of four mutational processes")

b = axs[1]
types = ["pilocytic\nastrocytoma", "acute myeloid\nleukemia", "breast", "colorectal", "lung\n(smokers)",
         "mismatch-repair\ndeficient", "melanoma"]
burden = [0.2, 0.5, 1.2, 3.5, 9.0, 40.0, 60.0]
cols = ["dna" if v < 10 else "positive" for v in burden]
b.barh(np.arange(len(types)), burden, color=[P.fill(c) for c in cols], edgecolor=[P.edge(c) for c in cols], lw=0.8)
b.set_yticks(np.arange(len(types)))
b.set_yticklabels(types, fontsize=FT["tiny"])
b.set_xscale("log")
b.axvline(10, color=P.muted(), lw=0.8, ls="--")
b.text(11, -0.45, "high burden:\nmore neoantigens", fontsize=FT["tiny"], color=P.muted())
charts.style_axes(b, "somatic substitutions per megabase", None)
charts.title(b, "B  Tumor mutational burden")
