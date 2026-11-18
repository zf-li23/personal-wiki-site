"""MacArthur's (1972) model of species richness on a one-dimensional resource axis.

Each species uses a stretch of the resource axis (utilization curves drawn as Gaussians with width
proportional to the niche breadth n); adjacent species overlap by o. The axis has length R. Panels, from
top: a reference community; a longer axis (larger R); narrower niches (smaller n); greater overlap
(larger o); an unsaturated community in which part of the axis is unused. With the axis fully packed, the
number of species is S = (R - o)/(n - o) (written on each row).
"""

import numpy as np

import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT

rows = [
    ("reference", 10.0, 2.0, 0.5, None),
    ("larger range of resources R", 14.0, 2.0, 0.5, None),
    ("more specialized species (smaller n)", 10.0, 1.4, 0.35, None),
    ("more overlap (larger o)", 10.0, 2.0, 1.0, None),
    ("unsaturated (part of R unused)", 10.0, 2.0, 0.5, (6.0, 10.0)),
]
toks = ["dna", "enzyme", "protein", "negative", "plant", "highlight", "rna"]

fig, ax = bio.canvas(24.0, 16.0)
x = np.linspace(-0.5, 15, 1500)
for r, (title, R, n, o, gap) in enumerate(rows):
    y0 = 13.2 - r * 3.0
    pa = C.axes_at(ax, (2.0, y0, 18.0, 2.2))
    step = n - o
    S = int(round((R - o) / step))
    for i in range(S):
        lo = i * step
        mid = lo + n / 2
        if gap and gap[0] <= mid <= gap[1]:
            continue
        sd = n / 4
        pa.fill_between(x, np.exp(-0.5 * ((x - mid) / sd) ** 2), color=Q.line_color(toks[i % len(toks)]), alpha=0.35, lw=0)
        pa.plot(x, np.exp(-0.5 * ((x - mid) / sd) ** 2), color=Q.line_color(toks[i % len(toks)]), lw=1.0)
    pa.plot([0, R], [-0.12, -0.12], color=P.ink(), lw=2.2, solid_capstyle="butt")
    if gap:
        pa.plot([gap[0], gap[1]], [-0.12, -0.12], color=P.muted(), lw=2.2, solid_capstyle="butt")
    pa.set_xlim(-0.5, 15)
    pa.set_ylim(-0.25, 1.1)
    pa.set_yticks([])
    pa.set_xticks([] if r < len(rows) - 1 else [0, 5, 10, 15])
    C.style_axes(pa, "resource axis (e.g. prey size)" if r == len(rows) - 1 else None, None)
    pa.spines["left"].set_visible(False)
    shown = S if not gap else sum(1 for i in range(S) if not (gap[0] <= i * step + n / 2 <= gap[1]))
    bio.label(ax, (2.0, y0 + 2.5), f"{title}:  R = {R:g}, n = {n:g}, o = {o:g},  S = {shown}", size="small", ha="left")
