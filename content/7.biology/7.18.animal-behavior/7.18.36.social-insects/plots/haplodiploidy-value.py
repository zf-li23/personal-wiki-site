"""Does haplodiploidy make helping easier? The Trivers-Hare argument with reproductive values.

A worker can raise siblings (sisters r = 3/4, brothers r = 1/4, for a singly mated queen) or her own offspring
(r = 1/2 to each sex). When the population contains a fraction z of females among reproductives, a male is worth
z/(1 - z) females in reproductive value. The genetic value of raising a brood with a fraction q of females is
q (1) r_f + (1 - q) (z / (1 - z)) r_m, and helping pays if B/C exceeds the ratio of the values of offspring and
siblings.
Curves: (1) siblings and offspring both at the population sex ratio (q = z): the critical B/C is exactly 1, as for
diploids (Trivers and Hare 1976; Craig 1979). (2) Split sex ratios: the worker's nest raises 3:1 females (q = 3/4)
while the population ratio is z, and a solitary female would also produce q = 3/4. (3) A solitary female instead
produces the sex ratio that maximizes her own value (only sons when z > 1/2), while the worker raises siblings at
the population ratio: haplodiploidy then hinders helping (B/C = 2 at z = 3/4).
"""

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT
z = np.linspace(0.5, 0.85, 200)
vm = z / (1 - z)


def val(q, rf, rm):
    return q * rf + (1 - q) * vm * rm


fig, ax = bio.canvas(20.0, 10.0)
pa = Ch.axes_at(ax, (2.6, 1.8, 13.4, 7.4))
c1 = val(z, 0.5, 0.5) / val(z, 0.75, 0.25)
c2 = val(0.75, 0.5, 0.5) / val(0.75, 0.75, 0.25)
best = np.maximum(val(1.0, 0.5, 0.5), val(0.0, 0.5, 0.5))
c3 = best / val(z, 0.75, 0.25)
for c, tok, lab, y in ((c1, "neutral", "siblings and offspring at the population sex ratio", 1.04),
                       (c2, "positive", "split sex ratio: 3:1 in the nest", None),
                       (c3, "negative", "solitary female makes the best sex ratio for herself", None)):
    pa.plot(z, c, color=Ch.line(tok) if tok != "neutral" else P.ink(), lw=1.7)
pa.text(0.505, 0.9, "siblings and offspring at the population ratio: B/C > 1", fontsize=FS["tiny"], color=P.ink())
pa.text(0.62, c2[np.argmin(np.abs(z - 0.62))] - 0.13, "split sex ratio (3:1 in the worker's nest)", fontsize=FS["tiny"],
        color=Ch.line("positive"))
pa.text(0.66, c3[np.argmin(np.abs(z - 0.66))] + 0.08, "solitary female makes her best sex ratio", fontsize=FS["tiny"],
        color=Ch.line("negative"), rotation=0)
pa.axvline(0.75, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
pa.text(0.752, 2.7, "z = 3/4", fontsize=FS["tiny"], color=P.muted())
pa.set_xlim(0.5, 0.85)
pa.set_ylim(0, 3.0)
Ch.style_axes(pa, "proportion of females among reproductives in the population, z", "critical B/C for helping")
