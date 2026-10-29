"""Juxtacrine lateral inhibition along a row of cells (Collier model, Definition 24.3.3 of 7.3.24).

For cell i: dN_i/dt = f(<D>_i) - N_i, dD_i/dt = g(N_i) - D_i, f(x) = x^2 / (a + x^2), g(x) = 1 / (1 + b x^2),
a = 0.01, on a ring of 30 cells, from the uniform state with 1 % noise. A: with contact only between immediate
neighbours (<D>_i = mean of the two neighbours) the row resolves into alternating high- and low-Delta cells
(red: high Delta, the cells that adopt the inhibiting fate; b = 100). If each cell also signals to the next-but-one
cells, as through long basal protrusions (weights 1 for neighbours at distance 1 and 2), high-Delta cells end up
further apart. B: amplitude of the final pattern (max D - min D) against the feedback strength b with nearest-
neighbour contact; the dashed line marks the linear threshold of the alternating mode, f'(D*) |g'(N*)| = 1.
"""

import numpy as np
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts as C
from wikibio import development as Dv
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
A_ = 0.01
n = 30


def simulate(b, offsets, T=200.0, dt=0.02, seed=3):
    f = lambda x: x * x / (A_ + x * x)
    g = lambda x: 1 / (1 + b * x * x)
    Ds = brentq(lambda d: d - g(f(d)), 1e-9, 1.0)
    rng = np.random.default_rng(seed)
    D = Ds * (1 + 0.01 * rng.standard_normal(n))
    N = f(D)
    for _ in range(int(T / dt)):
        Dm = np.mean([np.roll(D, s) for s in offsets], axis=0)
        N, D = N + dt * (f(Dm) - N), D + dt * (g(N) - D)
    return D, Ds


def threshold():
    def gain(b):
        f = lambda x: x * x / (A_ + x * x)
        g = lambda x: 1 / (1 + b * x * x)
        Ds = brentq(lambda d: d - g(f(d)), 1e-9, 1.0)
        Ns = f(Ds)
        fp = 2 * A_ * Ds / (A_ + Ds * Ds) ** 2
        gp = 2 * b * Ns / (1 + b * Ns * Ns) ** 2
        return fp * gp - 1
    return brentq(gain, 0.5, 200)


fig, ax = bio.canvas(26.0, 9.6)
toks = ["neutral", "negative"]
for row, (offs, name, y) in enumerate((((-1, 1), "contact with neighbours", 7.0),
                                      ((-2, -1, 1, 2), "contact up to two cells away", 4.6))):
    D, _ = simulate(100.0, offs)
    fates = [1 if d > 0.5 * (D.max() + D.min()) else 0 for d in D]
    Dv.cell_row(ax, 1.0, 13.0, y, fates, toks, h=1.0)
    bio.label(ax, (1.0, y + 0.9), name, size="small", ha="left")
bio.label(ax, (1.0, 2.9), "red: high Delta (inhibiting fate)   grey: low Delta (inhibited)", size="tiny", ha="left", color=P.muted())
bio.panel(ax, "A", (0.3, 9.0))
bio.label(ax, (1.0, 9.0), "Spacing set by the range of contact", size="small", bold=True, ha="left")

bs = np.logspace(0, 2.3, 16)
amp = [np.ptp(simulate(b, (-1, 1), T=400.0)[0]) for b in bs]
bt = threshold()
pb = C.axes_at(ax, (16.6, 1.6, 8.6, 6.2))
pb.semilogx(bs, amp, "o-", color=Q.line_color("protein"), lw=1.4, ms=4)
pb.axvline(bt, color=P.edge("highlight"), lw=0.9, ls=(0, (2, 2)))
pb.text(bt * 1.08, 0.3 * max(amp), f"threshold b = {bt:.1f}", color=P.edge("highlight"), fontsize=FS["tiny"])
C.style_axes(pb, "feedback strength b (log scale)", "pattern amplitude")
bio.panel(ax, "B", (15.3, 9.0))
bio.label(ax, (16.6, 9.0), "Onset of the alternating pattern", size="small", bold=True, ha="left")
