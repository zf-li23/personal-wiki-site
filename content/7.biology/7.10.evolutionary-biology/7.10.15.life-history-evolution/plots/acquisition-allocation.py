"""The Y model of acquisition and allocation (van Noordwijk and de Jong 1986).

Individuals acquire A = exp(N(0, sa)) and allocate x = logistic(N(0, sx)) to reproduction:
reproduction R = A x, survival investment S = A (1 - x). A: sa = 0.5, sx = 0.15. B: sa = 0.05, sx = 0.8.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(1)
fig, ax = bio.canvas(30.0, 10.0)
for k, (sa, sx, title, x0) in enumerate(((0.5, 0.15, "Variation mainly in acquisition", 2.2),
                                          (0.05, 0.8, "Variation mainly in allocation", 17.5))):
    A = np.exp(rng.normal(0, sa, 300))
    x = 1 / (1 + np.exp(-rng.normal(0, sx, 300)))
    R, S = A * x, A * (1 - x)
    r = np.corrcoef(R, S)[0, 1]
    p = C.axes_at(ax, (x0, 1.6, 10.5, 6.8))
    p.scatter(R, S, s=7, color=C.line("dna" if k == 0 else "rna"), alpha=0.7, lw=0)
    p.set_xlim(0, max(R.max(), S.max()) * 1.05)
    p.set_ylim(0, max(R.max(), S.max()) * 1.05)
    C.style_axes(p, "allocation to reproduction  Ax", "allocation to survival  A(1 − x)")
    p.text(0.97, 0.95, f"correlation r = {r:.2f}", transform=p.transAxes, ha="right", va="top",
           fontsize=FS["small"], color=P.ink())
    bio.panel(ax, "AB"[k], (x0 - 2.0, 9.8))
    bio.label(ax, (x0, 9.4), title, size="small", bold=True, ha="left")
