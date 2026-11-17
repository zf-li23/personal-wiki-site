"""Raunkiaer life-form spectra: percentage of species in each life form.

Data (Raunkiaer's classic spectra as compiled in Chinese textbooks, after Qu Zhongxiang et al. 1983):
normal spectrum (about 1000 species drawn at random from world floras) 46, 9, 26, 6, 13; Seychelles
(humid tropics) 61, 6, 12, 5, 16; Italy (Mediterranean) 12, 6, 29, 11, 42; Libyan desert 12, 21, 20, 5, 42;
Denmark (cool temperate) 7, 3, 50, 22, 18; Spitsbergen (Arctic) 1, 22, 60, 15, 2, for phanerophytes (Ph),
chamaephytes (Ch), hemicryptophytes (H), cryptophytes (Cr) and therophytes (Th).
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
regions = ["Normal\nspectrum", "Seychelles\n(tropical)", "Italy\n(Mediterranean)", "Libyan\ndesert",
           "Denmark\n(temperate)", "Spitsbergen\n(Arctic)"]
data = np.array([[46, 9, 26, 6, 13], [61, 6, 12, 5, 16], [12, 6, 29, 11, 42], [12, 21, 20, 5, 42],
                 [7, 3, 50, 22, 18], [1, 22, 60, 15, 2]])
forms = ["phanerophytes", "chamaephytes", "hemicryptophytes", "cryptophytes", "therophytes"]
toks = ["plant", "highlight", "dna", "animal", "negative"]

fig, ax = bio.canvas(26.0, 10.5)
pa = C.axes_at(ax, (2.2, 2.2, 22.5, 7.0))
w = 0.15
x = np.arange(len(regions))
for j in range(5):
    pa.bar(x + (j - 2) * w, data[:, j], width=w * 0.92, color=P.fill(toks[j]), edgecolor=P.edge(toks[j]), lw=0.6,
           label=forms[j])
pa.set_xticks(x, regions, fontsize=FS["tiny"])
pa.set_ylim(0, 70)
C.style_axes(pa, None, "percentage of species")
pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), ncol=5, loc="upper center", bbox_to_anchor=(0.5, 1.12))
