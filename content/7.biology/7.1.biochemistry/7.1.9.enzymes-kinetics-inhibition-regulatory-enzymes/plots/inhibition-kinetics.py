"""Reversible inhibition, from the general rate law v = V_max [S] / (alpha K_M + alpha' [S]) with
alpha = 1 + [I]/K_I and alpha' = 1 + [I]/K_I'. Top row: v against [S]; bottom row: double-reciprocal
plots, at [I] = 0, 1, 3 (in units of K_I). Competitive (K_I' infinite): lines meet on the 1/v axis.
Uncompetitive (K_I infinite, K_I' = 1): parallel lines. Mixed (K_I = 1, K_I' = 3, binding to E
preferred): lines meet to the left of the 1/v axis and above the 1/[S] axis, at
1/[S] = -K_I/(K_M K_I'). K_M = 1 and V_max = 1."""

import numpy as np
import wikibio as bio
from wikibio import charts
from wikibio import metabolism as M

P = bio.P
VMAX, KM = 1.0, 1.0
types = [
    ("A", "Competitive", dict(ki=1.0), r"$K_\mathrm{M}$ ↑, $v_{\max}$ unchanged"),
    ("B", "Uncompetitive", dict(kiu=1.0), r"$K_\mathrm{M}$ and $v_{\max}$ ↓ by $\alpha'$"),
    ("C", "Mixed", dict(ki=1.0, kiu=3.0), r"$v_{\max}$ ↓; $K_\mathrm{M}$ ↑ here ($\alpha > \alpha'$)"),
]
levels = [(0.0, "enzyme", "0"), (1.0, "drug", "1"), (3.0, "negative", "3")]

fig, ax = bio.canvas(21.0, 13.0)
S = np.linspace(0, 10, 300)
x = np.linspace(-1.5, 4, 100)
for k, (letter, name, kw, note) in enumerate(types):
    x0 = 1.3 + k * 6.9
    bio.panel(ax, letter, (x0 - 1.1, 12.9))
    top = charts.axes_at(ax, (x0, 7.4, 5.3, 4.6))
    bot = charts.axes_at(ax, (x0, 1.0, 5.3, 4.6))
    for i, tok, lab in levels:
        top.plot(S, M.rate(S, VMAX, KM, i, **kw), color=charts.line(tok), lw=1.8, label=f"[I] = {lab} $K_\\mathrm{{I}}$")
        vm, km = M.apparent(VMAX, KM, i, **kw)
        bot.plot(x, km / vm * x + 1 / vm, color=charts.line(tok), lw=1.8)
    top.set_xlim(0, 10)
    top.set_ylim(0, 1.0)
    top.set_yticks([0, 0.5, 1.0])
    charts.style_axes(top, r"[S] / $K_\mathrm{M}$", r"$v_0/v_{\max}$" if k == 0 else None)
    charts.title(top, name)
    top.text(0.4, 0.88, note, fontsize=bio.core.FONT["tiny"], color=P.ink())
    if k == 0:
        top.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower right")
    bot.axhline(0, color=P.muted(), lw=0.6)
    bot.axvline(0, color=P.muted(), lw=0.6)
    bot.set_xlim(-1.5, 4)
    bot.set_ylim(-1, 12)
    charts.style_axes(bot, r"$K_\mathrm{M}$/[S]", r"$v_{\max}/v_0$" if k == 0 else None)
