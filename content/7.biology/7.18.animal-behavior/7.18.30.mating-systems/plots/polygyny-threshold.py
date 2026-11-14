"""The polygyny threshold model (Verner and Willson 1966; Orians 1969) and sequential settlement.

A: the reproductive success of a female increases with the quality of the territory she settles on; settling as
a second female of an already mated male costs her an amount C (shared male help), so her curve lies below
the monogamous curve. A female choosing between an unmated male on a poor territory (quality q_B) and a mated
male on a good territory (q_A) should choose polygyny if q_A - q_B exceeds the polygyny threshold PT.
B: six females arrive in turn and each settles where her expected success is greatest (like an ideal free
distribution), among six territories of different quality; the first female on a territory is assumed not to
suffer from a second. Success as a monogamous (or first) female is 2 + 0.6 q, as a second female 2 + 0.6 q - 1.6.
Numbers are the order of settlement; two males become polygynous, two monogamous and two remain unmated.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.5)

pa = Ch.axes_at(ax, (2.6, 1.8, 10.8, 7.6))
q = np.linspace(0, 10, 100)
mono = 1 + 0.8 * q
second = mono - 2.4
pa.plot(q, mono, color=Ch.line("dna"), lw=1.9)
pa.plot(q, second, color=Ch.line("rna"), lw=1.9)
qB, qA = 3.0, 7.0
yB = 1 + 0.8 * qB
pa.plot([qB], [yB], "o", color=Ch.line("dna"), ms=6)
pa.plot([qA], [1 + 0.8 * qA - 2.4], "o", color=Ch.line("rna"), ms=6)
qT = qB + 2.4 / 0.8
pa.hlines(yB, qB, qT, color=P.muted(), lw=0.8, ls=(0, (3, 2)))
pa.vlines([qB, qT], 0, yB, color=P.muted(), lw=0.8, ls=(0, (1, 2)))
pa.annotate("", (qT, 0.6), (qB, 0.6), arrowprops=dict(arrowstyle="<->", color=P.ink(), lw=0.8))
pa.text((qB + qT) / 2, 0.75, "polygyny threshold PT", fontsize=FS["tiny"], color=P.ink(), ha="center",
        va="bottom")
pa.annotate("", (8.8, 1 + 0.8 * 8.8 - 2.4), (8.8, 1 + 0.8 * 8.8), arrowprops=dict(arrowstyle="<->",
            color=P.muted(), lw=0.8))
pa.text(8.95, 1 + 0.8 * 8.8 - 1.2, "cost of\nsharing C", fontsize=FS["tiny"], color=P.muted(), va="center")
pa.text(0.3, 8.8, "monogamous female (blue), second female (red)", fontsize=FS["tiny"], color=Ch.line("dna"))

pa.text(qB, yB + 0.4, "unmated male,\npoor territory", fontsize=FS["tiny"], color=Ch.line("dna"), ha="center",
        va="bottom")
pa.text(qA + 0.15, 1 + 0.8 * qA - 2.4 - 0.25, "mated male,\ngood territory", fontsize=FS["tiny"],
        color=Ch.line("rna"), va="top")
pa.set_xlim(0, 10)
pa.set_ylim(0, 9.5)
Ch.style_axes(pa, "territory quality", "female reproductive success")
Ch.title(pa, "The polygyny threshold")
bio.panel(ax, "A", (0.3, 10.2))

pb = Ch.axes_at(ax, (17.6, 1.8, 11.6, 7.6))
quality = np.array([10, 8, 6, 4, 2, 1.0])
names = "ABCDEF"
first = 2 + 0.6 * quality
sec = first - 1.6
females = [0] * 6
order = []
for f in range(6):
    best, val = None, -1
    for i in range(6):
        v = first[i] if females[i] == 0 else (sec[i] if females[i] == 1 else -1)
        if v > val:
            best, val = i, v
    order.append((best, females[best], val))
    females[best] += 1
x = np.arange(6)
pb.plot(x, first, "-", color=Ch.line("dna"), lw=1.6)
pb.plot(x, sec, "-", color=Ch.line("rna"), lw=1.6)
for k, (i, rank, v) in enumerate(order):
    tok = "dna" if rank == 0 else "rna"
    pb.plot([i], [v], "o", color=Ch.line(tok), ms=13, mfc=bio.P.surface(), mew=1.5)
    pb.text(i, v, str(k + 1), fontsize=FS["small"], color=P.ink(), ha="center", va="center", weight="bold")
pb.set_xticks(x)
pb.set_xticklabels(names)
pb.text(5.0, first[5] + 0.75, "monogamous or first female", fontsize=FS["tiny"], color=Ch.line("dna"), ha="right",
        va="bottom")
pb.text(5.0, sec[5] - 0.3, "second female", fontsize=FS["tiny"], color=Ch.line("rna"), ha="right", va="top")
pb.set_xlim(-0.5, 5.5)
pb.set_ylim(0, 8.8)
Ch.style_axes(pb, "male territory, best (A) to worst (F)", "female reproductive success")
Ch.title(pb, "Six females settle in turn")
bio.panel(ax, "B", (15.5, 10.2))
