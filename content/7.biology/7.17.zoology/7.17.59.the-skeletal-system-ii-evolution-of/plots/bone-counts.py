# Number of bones in the adult skull (with the lower jaw) in the vertebrate classes, as ranges given in
# comparative anatomy textbooks (Kardong 2019; Yang & Cheng, Comparative Anatomy of Vertebrates, 2nd ed.),
# log axis, in phylogenetic order. Orders of magnitude only: counts depend on how paired, fused and
# juvenile elements are counted.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(20, 8)
groups = [("Teleosts", 100, 180), ("Early tetrapods", 50, 90), ("Living reptiles", 50, 90),
          ("Living amphibians", 30, 50), ("Mammals (dog, rabbit)", 30, 35), ("Humans", 22, 22)]
p = quant.Plot(ax, (6.5, 1.3, 12.5, 6.0), xlim=(15, 250), ylim=(0, len(groups)), xlog=True,
               xlabel="number of bones in the skull (log scale)", xticks=[20, 50, 100, 200], yticks=[])
for i, (name, lo, hi) in enumerate(groups):
    y = len(groups) - i - 0.5
    if hi > lo:
        p.band(np.array([lo, hi]), np.array([y - 0.28] * 2), np.array([y + 0.28] * 2), "bone", alpha=1.0)
    p.points([np.sqrt(lo * hi)], [y], "ink", r=0.09)
    p.text(13.0, y, name, ha="right")
    p.text(hi * 1.08, y, f"{lo}-{hi}" if hi > lo else f"{lo}", ha="left")
