"""Extinction in the Galton-Watson process with f(x) = q + p x^2 (Theorem 36.4.3).

A stem cell with a fixed cycle either divides into two stem cells (probability p) or into two differentiated
cells (q = 1 - p). P0(t), the probability that the clone is extinct by generation t, obeys P0(t + 1) = f(P0(t)),
P0(0) = 0. A-C: cobweb diagrams for p = 0.4 (subcritical, m = 2p = 0.8), p = 0.5 (critical) and p = 0.6
(supercritical): the iteration climbs the staircase to the smallest fixed point of f in [0, 1], which is 1 when
m <= 1 and q/p = 2/3 when m > 1. D: P0(t) for the three cases; at criticality it approaches 1 slowly,
1 - P0(t) ~ 2 / t.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
FS = bio.core.FONT
fig, ax = bio.canvas(32.0, 9.0)
cases = ((0.4, "protein", "p = 0.4, m = 0.8"), (0.5, "enzyme", "p = 0.5, m = 1"), (0.6, "negative", "p = 0.6, m = 1.2"))
x = np.linspace(0, 1, 200)
for i, (p, tok, lab) in enumerate(cases):
    q = 1 - p
    f = lambda z: q + p * z * z
    pa = C.axes_at(ax, (1.8 + 7.4 * i, 1.6, 5.6, 5.6))
    pa.plot(x, f(x), color=Q.line_color(tok), lw=1.6)
    pa.plot(x, x, color=P.muted(), lw=0.8)
    z, xs, ys = 0.0, [0.0], [0.0]
    for _ in range(12):
        nz = f(z)
        xs += [z, nz]
        ys += [nz, nz]
        z = nz
    pa.plot(xs, ys, color=P.ink(), lw=0.7)
    fp = min(1.0, q / p)
    pa.plot([fp], [fp], "o", ms=4, color=Q.line_color(tok))
    pa.set_xlim(0, 1)
    pa.set_ylim(0, 1)
    pa.set_aspect("equal")
    C.style_axes(pa, "P0(t)", "P0(t + 1)" if i == 0 else None)
    bio.panel(ax, "ABC"[i], (0.4 + 7.4 * i, 8.8))
    bio.label(ax, (1.8 + 7.4 * i, 8.5), lab, size="small", bold=True, ha="left")

pd = C.axes_at(ax, (24.4, 1.6, 6.8, 5.6))
T = np.arange(0, 41)
for p, tok, lab in cases:
    q = 1 - p
    v = [0.0]
    for _ in T[1:]:
        v.append(q + p * v[-1] ** 2)
    pd.plot(T, v, color=Q.line_color(tok), lw=1.6, label=lab.split(",")[1].strip())
pd.plot(T[2:], 1 - 2 / T[2:], color=P.muted(), lw=0.8, ls=(0, (3, 2)), label="1 - 2/t")
pd.set_ylim(0, 1.02)
C.style_axes(pd, "generation t", "P(extinct by t)")
pd.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower right")
bio.panel(ax, "D", (23.0, 8.8))
bio.label(ax, (24.4, 8.5), "Approach to extinction", size="small", bold=True, ha="left")
