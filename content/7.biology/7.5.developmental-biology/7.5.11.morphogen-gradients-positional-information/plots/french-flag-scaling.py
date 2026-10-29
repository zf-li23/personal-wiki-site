"""The French flag problem: does the pattern scale with the size of the tissue?

Two lines of cells, of length L = 1 and L = 1.6, read two thresholds of a morphogen (T1 = 2/3, T2 = 1/3 of the
source level). Left: Wolpert's original source-sink model, with the concentration held at C0 at one end and at 0
at the other: the steady profile is linear, C = C0 (1 - x / L), and the boundaries sit at L/3 and 2L/3 for every L,
so the flag scales. Right: a synthesis-diffusion-degradation gradient with a fixed decay length (lambda = 0.4 in
units of the smaller tissue) is exponential, C = C0 exp(-x / lambda): the boundaries sit at fixed absolute distances
lambda ln(C0 / T) from the source, so the larger tissue gets the same blue and white bands and a much wider red one.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import development as D
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(24.0, 11.0)
T = (2 / 3, 1 / 3)
tok = ["na", "neutral", "negative"]
lam = 0.4
Ls = (1.0, 1.6)
styles = ({"ls": "-"}, {"ls": (0, (4, 3))})


def fates_of(c):
    return [0 if v > T[0] else 1 if v > T[1] else 2 for v in c]


for col, (title, model) in enumerate((("Source and sink: linear gradient", "lin"),
                                      ("Source and degradation: exponential gradient", "exp"))):
    X0 = 1.6 + col * 12.0
    W = 9.6
    pax = C.axes_at(ax, (X0, 5.2, W, 4.2))
    for L, st in zip(Ls, styles):
        x = np.linspace(0, L, 300)
        c = 1 - x / L if model == "lin" else np.exp(-x / lam)
        pax.plot(x, c, color=Q.line_color("protein") if L == 1 else P.muted(), lw=1.8, **st, label=f"L = {L:g}")
    for t, name in zip(T, ("$T_1$", "$T_2$")):
        pax.axhline(t, color=P.edge("highlight"), lw=0.9, ls=(0, (2, 2)))
        pax.text(1.62, t, name, color=P.edge("highlight"), fontsize=bio.core.FONT["small"], va="center")
    pax.set_xlim(0, 1.6)
    pax.set_ylim(0, 1.05)
    C.style_axes(pax, "position x (source at x = 0)", "C / $C_0$")
    pax.legend(loc="upper right", frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink())
    bio.label(ax, (X0, 10.3), title, size="normal", bold=True, ha="left")
    # rows of cells, drawn to the same x scale as the axes
    for k, (L, yy) in enumerate(zip(Ls, (3.2, 1.6))):
        n = int(round(12 * L))
        xc = (np.arange(n) + 0.5) / n * L
        c = 1 - xc / L if model == "lin" else np.exp(-xc / lam)
        D.cell_row(ax, X0, X0 + W * L / 1.6, yy, fates_of(c), tok, h=0.9, dashed=(k == 1))
        bio.label(ax, (X0 - 0.2, yy), f"L = {L:g}", size="tiny", ha="right")
    note = ("boundaries at L/3 and 2L/3: the flag scales" if model == "lin"
            else "boundaries at λ ln(C₀/T): fixed distances from the source")
    bio.label(ax, (X0 + W / 2, 0.55), note, size="small", color=P.muted())
