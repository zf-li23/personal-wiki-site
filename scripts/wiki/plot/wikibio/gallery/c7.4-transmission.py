# Sample of the transmission module: crossovers among four chromatids, a three-point testcross,
# linkage maps, ordered and unordered asci, and a circular Hfr map
import numpy as np

import wikibio as bio
from wikibio import transmission as T

fig, ax = bio.canvas(30, 15)
P = bio.P

# A: one crossover between chromatids 2 and 3 and its four products
bio.panel(ax, "A", (0.2, 14.8))
loci = [(0.3, ("A", "a")), (0.8, ("B", "b"))]
pr = T.four_chromatids(ax, 0.8, 5.3, 12.4, crossovers=[(0.55, 1, 2)], loci=loci)
bio.arrow(ax, (5.7, 12.4), (6.6, 12.4))
T.chromatid_set(ax, 7.0, 11.5, 12.4, pr, loci_f=[0.3, 0.8], tags=["P", "R", "R", "P"])

# B: three-point testcross classes
bio.panel(ax, "B", (14.6, 14.8))
par = (("v", "cv", "ct+"), ("v+", "cv+", "ct"))
cls = [(("v", "cv", "ct+"), 580), (("v+", "cv+", "ct"), 592), (("v", "cv+", "ct"), 45), (("v+", "cv", "ct+"), 40),
       (("v", "cv", "ct"), 89), (("v+", "cv+", "ct+"), 94), (("v", "cv+", "ct+"), 3), (("v+", "cv", "ct"), 5)]
T.three_point(ax, (15.2, 13.6), par, [0.15, 0.55, 0.9], cls, width=4.4, row=0.62)

# C: linkage maps compared
bio.panel(ax, "C", (0.2, 8.0))
m1 = T.linkage_map(ax, 2.0, 6.9, [("y", 0), ("w", 1.0), ("v", 30.7), ("m", 33.7), ("r", 57.6)], scale=0.095,
                   name="1913", side="right")
m2 = T.linkage_map(ax, 6.0, 6.9, [("y", 0), ("w", 1.5), ("v", 33.0), ("m", 36.1), ("r", 54.5)], scale=0.095,
                   name="Modern", side="left")
T.link_maps(ax, m1, m2)

# D: ordered asci (MI and MII patterns) and unordered tetrads
bio.panel(ax, "D", (9.0, 8.0))
W, K = "bone", "ink"
for k, sp in enumerate([[W] * 4 + [K] * 4, [W, W, K, K, W, W, K, K], [W, W, K, K, K, K, W, W]]):
    T.ascus(ax, (10.0 + 1.1 * k, 4.6), sp)
for k, g in enumerate([["AB", "AB", "ab", "ab"], ["Ab", "Ab", "aB", "aB"], ["AB", "Ab", "aB", "ab"]]):
    T.tetrad(ax, (14.6 + 1.9 * k, 4.6), g)
    bio.label(ax, (14.6 + 1.9 * k, 3.2), ["PD", "NPD", "T"][k], size="small")

# E: Hfr map
bio.panel(ax, "E", (20.8, 8.0))
T.hfr_map(ax, (25.2, 4.2), 2.6, markers=[(0, "thr"), (2, "leu"), (8, "azi"), (9, "ton"), (17, "lac"), (21, "gal"),
                                           (73, "str"), (61, "mal")],
          hfrs=[(97, 1, "HfrH"), (31, -1, "Hfr 2"), (65, 1, "Hfr 3")])
