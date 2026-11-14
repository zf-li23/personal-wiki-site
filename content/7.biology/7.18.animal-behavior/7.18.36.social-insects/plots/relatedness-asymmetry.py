"""Relatedness asymmetries in hymenopteran colonies and the conflicts they predict, against the number k of males with
which the queen mated (equal paternity).

A: sex allocation. A worker is related to her sisters by r_s = 1/4 + 1/(2k) and to her brothers by r_b = 1/4. Her
favored investment in females is r_s / (r_s + r_b) (Trivers and Hare 1976): 3/4 with single mating, falling toward
1/2 (the queen's optimum) as k increases. Split sex ratios: when colonies differ in k, workers in colonies with a
singly mated queen should rear mostly females and those with a multiply mated queen mostly males.
B: male production. A worker is related to her own sons by 1/2, to the queen's sons (brothers) by 1/4 and to the sons
of other workers (nephews) by r_s / 2 on average. Nephews are worth more than brothers only when k < 2; with more
matings, workers gain by destroying each other's eggs (worker policing; Ratnieks 1988). Honeybee queens mate with
about 12 males on average.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
k = np.linspace(1, 20, 400)
rs = 0.25 + 0.5 / k
fig, ax = bio.canvas(30.0, 10.0)

pa = Ch.axes_at(ax, (2.6, 1.8, 11.0, 7.2))
pa.plot(k, rs / (rs + 0.25), color=Ch.line("rna"), lw=1.7)
pa.axhline(0.5, color=Ch.line("dna"), lw=1.4, ls=(0, (4, 2)))
pa.text(19.8, 0.485, "queen's optimum 1:1", fontsize=FS["tiny"], color=Ch.line("dna"), ha="right", va="top")
pa.text(3.0, 0.70, "workers' optimum", fontsize=FS["tiny"], color=Ch.line("rna"))
pa.set_xlim(1, 20)
pa.set_ylim(0.4, 0.8)
pa.set_xticks([1, 2, 5, 10, 15, 20])
Ch.style_axes(pa, "number of males mated by the queen, k", "favored investment in females")
bio.panel(ax, "A", (0.3, 9.8))

pb = Ch.axes_at(ax, (18.2, 1.8, 10.8, 7.2))
pb.plot(k, rs / 2, color=Ch.line("rna"), lw=1.7)
pb.axhline(0.25, color=Ch.line("dna"), lw=1.6)
pb.axhline(0.5, color=Ch.line("protein"), lw=1.2, ls=(0, (4, 2)))
pb.plot([2], [0.25], "o", ms=5, color=P.ink())
pb.annotate("k = 2", (2, 0.25), (3.6, 0.33), fontsize=FS["tiny"], color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.7))
pb.text(19.8, 0.26, "brothers (queen's sons)", fontsize=FS["tiny"], color=Ch.line("dna"), ha="right", va="bottom")
pb.text(19.8, 0.155, "nephews (other workers' sons)", fontsize=FS["tiny"], color=Ch.line("rna"), ha="right")
pb.text(19.8, 0.51, "own sons", fontsize=FS["tiny"], color=Ch.line("protein"), ha="right", va="bottom")
pb.axvspan(2, 20, color=P.mix(P.fill("highlight"), P.surface(), 0.75), lw=0, zorder=0)
pb.text(11, 0.42, "policing favored", fontsize=FS["small"], color=P.ink(), ha="center")
pb.plot([12], [rs[np.argmin(np.abs(k - 12))] / 2], "s", ms=5, color=Ch.line("rna"))
pb.text(12, 0.10, "honeybee", fontsize=FS["tiny"], color=Ch.line("rna"), ha="center")
pb.set_xlim(1, 20)
pb.set_ylim(0, 0.6)
pb.set_xticks([1, 2, 5, 10, 15, 20])
Ch.style_axes(pb, "number of males mated by the queen, k", "relatedness of a worker")
bio.panel(ax, "B", (15.8, 9.8))
