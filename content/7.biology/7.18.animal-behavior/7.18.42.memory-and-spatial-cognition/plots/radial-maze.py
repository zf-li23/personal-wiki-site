# Working memory in the eight-arm radial maze (Olton and Samuelson 1976). A: the maze seen from above; each
# arm is baited once, and the rat has already emptied the arms marked as visited. B: the distribution of the
# number of different arms entered in the first eight choices for a rat choosing arms at random (with
# replacement, exact distribution computed by dynamic programming; mean 5.25) compared with trained rats,
# which typically enter 7 to 8 different arms. C: interruption experiment in a 12-arm maze (Cook, Brown and
# Riley 1985). The rat is removed after its k-th choice and returned after a delay; the predicted memory load
# during the delay, and hence errors after it, rises with k if the rat remembers the arms visited
# (retrospective coding), falls with k if it remembers the arms still to visit (prospective coding), and peaks
# at k = 6 if it switches from one code to the other halfway, the pattern observed.
import numpy as np

import wikibio as bio
import wikibehav as wb
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(28.0, 9.4)
bio.panel(ax, "A", (0.2, 9.2))
wb.radial_maze(ax, (4.2, 4.6), arm=3.0, n=8, width=0.6, baited=(0, 1, 3, 4, 6), visited=(2, 5, 7))
bio.label(ax, (4.2, 0.4), "3 arms visited, 5 still baited", size="tiny", color=P.muted())

# exact distribution of distinct arms in 8 random choices
dist = np.zeros(9)
dist[0] = 1.0
for _ in range(8):
    new = np.zeros(9)
    for k in range(9):
        if dist[k] == 0:
            continue
        new[k] += dist[k] * k / 8
        if k < 8:
            new[k + 1] += dist[k] * (8 - k) / 8
    dist = new
mean = float(np.dot(np.arange(9), dist))
pb = quant.Plot(ax, (10.6, 1.8, 7.2, 6.4), (2.5, 8.5), (0, 0.7), xlabel="Different arms in first 8 choices",
                ylabel="Probability", xticks=[3, 4, 5, 6, 7, 8], yticks=[0, 0.2, 0.4, 0.6])
bio.panel(ax, "B", (8.8, 9.2))
for kk in range(3, 9):
    pb.bars([kk - 0.38, kk - 0.02], [dist[kk]], "neutral")
trained = {6: 0.05, 7: 0.3, 8: 0.65}
for kk, v in trained.items():
    pb.bars([kk + 0.02, kk + 0.38], [v], "dna")
pb.legend([(f"random choice (mean {mean:.2f})", "neutral", "-"), ("trained rats (typical)", "dna", "-")], at=(11.2, 7.9))

pc = quant.Plot(ax, (20.4, 1.8, 7.0, 6.4), (0, 12), (0, 1.1), xlabel="Interruption after choice k",
                ylabel="Predicted memory load (relative)", xticks=[2, 4, 6, 8, 10], yticks=[0, 0.5, 1])
bio.panel(ax, "C", (18.6, 9.2))
kk = np.arange(1, 12)
pc.line(kk, kk / 11, "rna", lw=1.6, dashed=True, text="retrospective", at=0.95, dx=-0.1, dy=0.22, ha="right")
pc.line(kk, (12 - kk) / 11, "protein", lw=1.6, dashed=True, text="prospective", at=0.05, dx=0.1, dy=0.22)
pc.line(kk, np.minimum(kk, 12 - kk) / 6, "dna", lw=2.2, text="switching at half", at=0.5, dy=0.2, ha="center")
pc.points(kk, np.minimum(kk, 12 - kk) / 6, "dna", r=0.09)
