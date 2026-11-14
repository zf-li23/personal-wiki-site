"""Host sanctions and the stability of nitrogen fixation (illustrative model, after Kiers and colleagues 2003).

Rhizobia are either fixers, which pay a growth cost c = 0.1, or cheaters. Each nodule is founded by k cells drawn at
random from the soil population (fraction p of fixers). The plant sanctions a nodule in proportion to the fraction
of cheaters in it: the bacteria in the nodule multiply by g = 1 - s (cheater fraction), with sanction strength
s = 0.5. Fixers in a nodule multiply by (1 - c) g, cheaters by g; the released bacteria form the next soil
population.
A: the change in the fraction of fixers per generation against p for nodules founded by one, two or four cells:
with one cell per nodule, sanctions fall entirely on cheaters and fixers win whenever s > c; with mixed nodules,
cheaters share the fixers' rewards, and when the sanction falling on a single cheater, s/k, is smaller than c (here k = 8), cheaters spread.
B: the fraction of fixers over generations, starting at 0.5.
"""

import numpy as np
from math import comb
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
c, s = 0.1, 0.5


def step(p, k):
    out_f = out_c = 0.0
    for j in range(k + 1):  # j fixers among k founders
        pr = comb(k, j) * p ** j * (1 - p) ** (k - j)
        g = 1 - s * (k - j) / k
        out_f += pr * j * (1 - c) * g
        out_c += pr * (k - j) * g
    return out_f / (out_f + out_c)


fig, ax = bio.canvas(30.0, 10.0)
pa = Ch.axes_at(ax, (2.6, 1.8, 11.0, 7.2))
pp = np.linspace(0.001, 0.999, 300)
for k, tok in ((1, "positive"), (3, "protein"), (8, "negative")):
    pa.plot(pp, [step(x, k) - x for x in pp], color=Ch.line(tok), lw=1.6)
    j = 150
    pa.text(pp[j], step(pp[j], k) - pp[j] + (0.004 if k < 8 else -0.014), f"{k} founder{'s' if k > 1 else ''} per nodule",
            fontsize=FS["tiny"], color=Ch.line(tok), ha="center")
pa.axhline(0, color=P.muted(), lw=0.8)
pa.set_xlim(0, 1)
Ch.style_axes(pa, "fraction of fixers p", "change per generation")
bio.panel(ax, "A", (0.3, 9.8))

pb = Ch.axes_at(ax, (18.2, 1.8, 10.8, 7.2))
for k, tok in ((1, "positive"), (3, "protein"), (8, "negative")):
    ps = [0.5]
    for _ in range(80):
        ps.append(step(ps[-1], k))
    pb.plot(ps, color=Ch.line(tok), lw=1.6)
    pb.text(83, ps[-1] + {1: 0.04, 3: -0.03, 8: 0}[k], f"k = {k}", fontsize=FS["tiny"], color=Ch.line(tok), va="center")
    pb.plot([0, 80], [0.5, 0.5], color=P.muted(), lw=0.5, ls=(0, (2, 2))) if k == 1 else None
pb.set_xlim(0, 92)
pb.set_ylim(0, 1.02)
Ch.style_axes(pb, "generations", "fraction of fixers")
bio.panel(ax, "B", (15.8, 9.8))
