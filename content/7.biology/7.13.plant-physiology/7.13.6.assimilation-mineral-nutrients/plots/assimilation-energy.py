# Energy cost of nutrient assimilation, in ATP equivalents per atom of N or S incorporated (approximate values
# given in Taiz et al. 2015, chapter 13 introduction and Fig. 13.20): ammonium taken up and fixed by GS-GOGAT
# (about 2, plus uptake); nitrate to glutamine/glutamate (about 12-13: uptake 1, nitrate reductase 3, nitrite
# reductase 7, GS-GOGAT 2); N2 fixation by nodule bacteroids plus assimilation (about 16 per amide N, carbon cost
# to the plant included); sulfate to cysteine (about 14). Right: the corresponding number of electrons, from the
# change of oxidation number (NO3- +5 -> NH4+ -3: 8; N2 0 -> -3: 3 per N plus the obligatory H2; SO4 2- +6 ->
# S2- -2: 8).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
labels = ["NH$_4^+$ → Glu", "NO$_3^-$ → Glu", "N$_2$ → amide N\n(symbiotic)", "SO$_4^{2-}$ → Cys"]
atp = np.array([2, 13, 16, 14])
elec = np.array([2, 10, 4, 8])
toks = ["rna", "dna", "bacterium", "highlight"]
fig, axs = plt.subplots(1, 2, figsize=(11.0, 4.0), gridspec_kw=dict(wspace=0.45, width_ratios=[1.4, 1]))
ax = axs[0]
y = np.arange(len(labels))[::-1]
ax.barh(y, atp, color=[P.fill(t) for t in toks], edgecolor=[charts.line(t) for t in toks])
for yy, v in zip(y, atp):
    ax.text(v + 0.3, yy, f"≈ {v}", va="center", fontsize=8, color=P.ink())
ax.set_yticks(y)
ax.set_yticklabels(labels)
ax.set_xlim(0, 19)
charts.style_axes(ax, "ATP equivalents per N or S atom", None)
charts.title(ax, "A   Energy cost")
ax = axs[1]
ax.barh(y, elec, color=[P.fill(t) for t in toks], edgecolor=[charts.line(t) for t in toks])
for yy, v, t in zip(y, elec, ["GOGAT", "NR 2 + NiR 6 + GOGAT 2", "N$_2$ (6) + H$_2$ (2): 4 per N", "APS red. 2 + SiR 6"]):
    ax.text(v + 0.3, yy, t, va="center", fontsize=6.8, color=P.ink())
ax.set_yticks(y)
ax.set_yticklabels([])
ax.set_xlim(0, 20)
charts.style_axes(ax, "electrons per N or S atom", None)
charts.title(ax, "B   Electrons")
