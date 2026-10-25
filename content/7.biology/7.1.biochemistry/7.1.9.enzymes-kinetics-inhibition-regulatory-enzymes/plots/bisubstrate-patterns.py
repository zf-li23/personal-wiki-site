"""Steady-state kinetics of bisubstrate reactions A + B -> P + Q in double-reciprocal form:
1/v against 1/[A] at several fixed concentrations of B.

Sequential (ternary-complex) mechanism: v = V[A][B] / (K_iA K_B + K_B [A] + K_A [B] + [A][B]);
the slope depends on [B], so the lines intersect (here to the left of the 1/v axis).
Ping-pong (double-displacement) mechanism: v = V[A][B] / (K_B [A] + K_A [B] + [A][B]);
the slope K_A/V does not depend on [B], so the lines are parallel.
Parameters (concentrations in mM): V = 1, K_A = 1, K_B = 0.5, K_iA = 2."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
V, KA, KB, KIA = 1.0, 1.0, 0.5, 2.0
Bs = (0.25, 0.5, 1.0, 4.0)
toks = ("negative", "drug", "enzyme", "channel")


def seq(x, B):  # x = 1/[A]
    return (KA + KIA * KB / B) / V * x + (1 + KB / B) / V


def pp(x, B):
    return KA / V * x + (1 + KB / B) / V


fig, ax = bio.canvas(20.0, 8.0)
for k, (letter, name, f, x0) in enumerate((("A", "Sequential: lines intersect", seq, 1.3),
                                           ("B", "Ping-pong: lines parallel", pp, 11.8))):
    bio.panel(ax, letter, (x0 - 1.2, 7.9))
    a = charts.axes_at(ax, (x0, 1.0, 7.8, 6.0))
    x = np.linspace(-1.2, 4, 100)
    for B, tok in zip(Bs, toks):
        a.plot(x, f(x, B), color=charts.line(tok), lw=1.8, label=f"[B] = {B:g} mM")
    a.axhline(0, color=P.muted(), lw=0.6)
    a.axvline(0, color=P.muted(), lw=0.6)
    a.set_xlim(-1.2, 4)
    a.set_ylim(-1, 14 if k == 0 else 8)
    a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
    charts.style_axes(a, "1/[A] / mM$^{-1}$", "1/$v_0$ (relative)")
    charts.title(a, name)
