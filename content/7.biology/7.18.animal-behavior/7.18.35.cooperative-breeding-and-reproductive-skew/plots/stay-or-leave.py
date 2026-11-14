"""The decision to disperse or to stay and help (illustrative model), and Reyer's pied kingfisher data.

A: a young bird can disperse, survive the journey with probability 0.7, and find a territory with probability v,
on which it raises W = 2 offspring; or stay, help its parents raise B = 0.8 extra siblings (indirect fitness rB)
and inherit the natal territory with probability 0.15 (direct fitness 0.15 W). Inclusive fitness of the two options
against v, for full siblings (r = 1/2) and half siblings (r = 1/4). Staying is favored when vacancies are scarce
(habitat saturation), and the switch point moves to scarcer vacancies when the young would be helping half siblings.
B: inclusive fitness of three tactics of year-old male pied kingfishers over two years (Reyer 1984): primary helpers
(which help their parents) gain indirect fitness in the first year (1.8 extra young x r = 0.32) but survive less
well into the second; secondary helpers (which help unrelated pairs) gain only direct fitness in the second year,
often by pairing with the female they helped; delayers neither help nor breed in the first year.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)

pa = Ch.axes_at(ax, (2.4, 1.8, 11.0, 7.2))
v = np.linspace(0, 1, 200)
W, sd, B, h = 2.0, 0.7, 0.8, 0.15
pa.plot(v, sd * v * W, color=Ch.line("rna"), lw=1.8)
pa.text(0.98, sd * W - 0.05, "disperse", fontsize=FS["small"], color=Ch.line("rna"), ha="right", va="top")
for r, tok, ls in ((0.5, "dna", "-"), (0.25, "dna", (0, (4, 2)))):
    stay = r * B + h * W
    pa.axhline(stay, color=Ch.line(tok), lw=1.6, ls=ls)
    vs = stay / (sd * W)
    pa.plot([vs], [stay], "o", ms=4.5, color=Ch.line(tok))
    pa.text(0.02, stay + 0.03, f"stay and help, r = {r:g}", fontsize=FS["tiny"], color=Ch.line(tok), va="bottom")
pa.set_xlim(0, 1)
pa.set_ylim(0, 1.5)
Ch.style_axes(pa, "probability of finding a territory, v", "inclusive fitness")
bio.panel(ax, "A", (0.3, 9.8))

pb = Ch.axes_at(ax, (18.2, 1.8, 10.8, 7.2))
names = ["primary\nhelper", "secondary\nhelper", "delayer"]
y1 = np.array([0.58, 0.0, 0.0])
y2 = np.array([0.41, 0.84, 0.29])
x = np.arange(3)
pb.bar(x, y1, 0.55, color=P.fill("positive"), edgecolor=P.edge("positive"), lw=0.8)
pb.bar(x, y2, 0.55, bottom=y1, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8)
for xi, t in zip(x, y1 + y2):
    pb.text(xi, t + 0.03, f"{t:.2f}", ha="center", fontsize=FS["tiny"], color=P.ink())
pb.set_xticks(x)
pb.set_xticklabels(names, fontsize=FS["tiny"])
pb.set_ylim(0, 1.2)
pb.text(2.4, 1.12, "indirect, year 1", fontsize=FS["tiny"], color=Ch.line("positive"), ha="right")
pb.text(2.4, 1.03, "direct, year 2", fontsize=FS["tiny"], color=Ch.line("dna"), ha="right")
Ch.style_axes(pb, None, "fitness (offspring equivalents)")
bio.panel(ax, "B", (15.8, 9.8))
