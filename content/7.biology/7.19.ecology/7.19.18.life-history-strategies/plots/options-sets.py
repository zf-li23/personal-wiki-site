"""Options sets and fitness contours (Sibly and Calow 1983).

An established individual divides its resources between present reproduction b (offspring this season)
and residual reproductive value: its survival s to the next season times the value of a survivor.
Fitness is lambda = b + V s, so fitness contours are straight lines of slope -1/V in the (b, s) plane.
A high cost-of-reproduction habitat (high CR: survivors are valuable, V = 4) has shallow contours, a low
CR habitat (V = 1) steep ones.
A: a convex-outward options set, s = sqrt(1 - (b/B)^2) with B = 4:
the optimum moves from low to high reproductive allocation as CR falls.
B: a concave-outward options set (s = (1 - sqrt(b/B))^2): the optimum is at an extreme, either no
reproduction or all-out (semelparous) reproduction.
C: fitness along each boundary as a function of the reproductive allocation b/B; points: optima.
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(30.0, 10.0)
B = 4.0
b = np.linspace(0, B, 400)
convex = np.sqrt(1 - (b / B) ** 2)
concave = (1 - np.sqrt(b / B)) ** 2
habitats = [(5.0, "dna", "high CR (V = 5)"), (1.0, "negative", "low CR (V = 1)")]


def panel(rect, s, name, letter, lx):
    pa = C.axes_at(ax, rect)
    pa.fill_between(b, 0, s, color=P.fill("neutral"), alpha=0.35, lw=0)
    pa.plot(b, s, color=P.ink(), lw=1.6)
    for V, tok, lab in habitats:
        lam = b + V * s
        k = int(np.argmax(lam))
        for level in (lam[k] - 1.2, lam[k] - 0.6, lam[k]):
            pa.plot(b, (level - b) / V, color=Q.line_color(tok), lw=0.9 if level < lam[k] else 1.4,
                    ls=(0, (4, 2)) if level < lam[k] else "-")
        pa.plot(b[k], s[k], "o", ms=6, color=Q.line_color(tok), label=lab)
    pa.set_xlim(0, B)
    pa.set_ylim(0, 1.15)
    C.style_axes(pa, "present reproduction b", "survival to next season s")
    pa.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
    bio.panel(ax, letter, (lx - 1.5, 9.6))
    bio.label(ax, (lx, 9.2), name, size="small", bold=True, ha="left")


panel((2.0, 1.6, 7.0, 6.8), convex, "Convex-outward options set", "A", 2.0)
panel((12.0, 1.6, 7.0, 6.8), concave, "Concave-outward options set", "B", 12.0)

pc = C.axes_at(ax, (22.5, 1.6, 7.0, 6.8))
for s, ls, nm in [(convex, "-", "convex"), (concave, (0, (4, 2)), "concave")]:
    for V, tok, lab in habitats:
        lam = b + V * s
        pc.plot(b / B, lam, color=Q.line_color(tok), lw=1.4, ls=ls, label=f"{nm}, V = {V:g}")
        k = int(np.argmax(lam))
        pc.plot(b[k] / B, lam[k], "o", ms=4.5, color=Q.line_color(tok))
pc.set_xlim(0, 1)
pc.set_ylim(0, 7)
C.style_axes(pc, "reproductive allocation b / B", "fitness lambda = b + V s")
pc.legend(frameon=False, fontsize=FS["tiny"] - 1, labelcolor=P.ink(), loc="upper left")
bio.panel(ax, "C", (21.0, 9.6))
bio.label(ax, (22.5, 9.2), "Fitness along the trade-off", size="small", bold=True, ha="left")
