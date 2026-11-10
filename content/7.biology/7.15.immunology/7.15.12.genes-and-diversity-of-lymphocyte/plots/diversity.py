# Counting the repertoire (Eqs. 12.1-12.3 of the page).
# A: theoretical number of receptors against the junctional variants j per junction (log-log); BCR (heavy x light) and TCR.
# B: expected number of identical pairs among N cells drawn uniformly from M possible receptors (birthday estimate N^2/(2M)).
# C: somatic hypermutation: mean number of point mutations in a V region against the number of cell divisions.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
# functional segment numbers (approximate, human)
VH, DH, JH = 40, 23, 6
VK, JK, VL, JL = 35, 5, 30, 4
VA, JA, VB, DB, JB = 45, 50, 48, 2, 13
bcr = VH * DH * JH * (VK * JK + VL * JL)
tcr = (VA * JA) * (VB * DB * JB)

fig, ax = bio.canvas(23.0, 7.2)
bio.panel(ax, "A", (0.1, 7.05))
bio.label(ax, (3.9, 6.9), "Receptor repertoire size", size="title", bold=True)
pa = quant.Plot(ax, (1.7, 1.2, 5.6, 4.8), xlim=(1, 1000), ylim=(1e5, 1e18), xlog=True, ylog=True,
                xlabel="variants per junction $j$", ylabel="possible receptors", ylabel_offset=1.3,
                xticks=[(1, "1"), (10, "10"), (100, "$10^{2}$"), (1000, "$10^{3}$")],
                yticks=[(1e6, "$10^{6}$"), (1e9, "$10^{9}$"), (1e12, "$10^{12}$"), (1e15, "$10^{15}$"), (1e18, "$10^{18}$")])
j = np.logspace(0, 3, 100)
pa.line(j, bcr * j ** 3, "negative", lw=1.8)
pa.line(j, tcr * j ** 3, "channel", lw=1.8)
pa.legend([("antibody (H × L)", "negative", "-"), ("TCR αβ", "channel", "-")], (pa.X(1.5), pa.Y(1e17)), step=0.4)
pa.hline(1e11, dashed=True, text="$10^{11}$", side="left")
j11 = (1e11 / bcr) ** (1 / 3)
pa.points([j11], [1e11], "negative", r=0.09)

bio.panel(ax, "B", (8.0, 7.05))
bio.label(ax, (11.8, 6.9), "Identical receptors by chance", size="title", bold=True)
pb = quant.Plot(ax, (9.4, 1.2, 5.4, 4.8), xlim=(1e3, 1e11), ylim=(1e-3, 1e9), xlog=True, ylog=True,
                xlabel="cells sampled $N$", ylabel="expected identical pairs", ylabel_offset=1.2,
                xticks=[(1e3, "$10^{3}$"), (1e5, "$10^{5}$"), (1e7, "$10^{7}$"), (1e9, "$10^{9}$"), (1e11, "$10^{11}$")],
                yticks=[(1e-3, "$10^{-3}$"), (1, "1"), (1e3, "$10^{3}$"), (1e6, "$10^{6}$"), (1e9, "$10^{9}$")])
N = np.logspace(3, 11, 100)
for M, tok, txt in ((bcr, "enzyme", "$M = 1.6\\times10^{6}$"), (1e11, "channel", "$M = 10^{11}$"), (1e13, "negative", "$M = 10^{13}$")):
    pb.line(N, N ** 2 / (2 * M), tok, lw=1.8)
pb.legend([("$M = 1.6\\times10^{6}$ (combinatorial only)", "enzyme", "-"), ("$M = 10^{11}$", "channel", "-"), ("$M = 10^{13}$", "negative", "-")],
          (pb.X(2e3), pb.Y(2e8)), step=0.4)

bio.panel(ax, "C", (15.6, 7.05))
bio.label(ax, (19.6, 6.9), "Somatic hypermutation", size="title", bold=True)
pc = quant.Plot(ax, (17.0, 1.2, 5.2, 4.8), xlim=(0, 40), ylim=(0, 15), xlabel="cell divisions $n$",
                ylabel="mutations per V region", ylabel_offset=0.9, xticks=[0, 10, 20, 30, 40], yticks=[0, 5, 10, 15])
n = np.linspace(0, 40, 100)
L = 350
for mu, tok in ((1e-3, "negative"), (5e-4, "enzyme"), (2e-4, "channel")):
    pc.line(n, mu * L * n, tok, lw=1.8)
pc.legend([("$\\mu = 10^{-3}$", "negative", "-"), ("$5\\times10^{-4}$", "enzyme", "-"), ("$2\\times10^{-4}$", "channel", "-")],
          (pc.X(2), pc.Y(14)), step=0.4)
