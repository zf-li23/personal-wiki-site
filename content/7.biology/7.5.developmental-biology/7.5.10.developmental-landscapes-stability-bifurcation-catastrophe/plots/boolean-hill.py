"""A three-gene loop at two resolutions: Boolean network and Hill-function ODEs.

Logic: a inhibits b, b activates c, c inhibits a (a positive feedback loop, two negative links).
A: synchronous Boolean dynamics a' = not c, b' = not a, c' = b on the 8 states (a b c): two fixed
points, 011 and 100, and two 3-cycles. B: the continuous version
da/dt = F-(c) - a, db/dt = F-(a) - b, dc/dt = F+(b) - c with F+(x) = x^n / (theta^n + x^n),
F-(x) = theta^n / (theta^n + x^n), n = 4, theta = 0.5, from 12 random initial states: every
trajectory goes to one of two stable steady states, close to the Boolean fixed points; the
3-cycles of the synchronous Boolean map have no counterpart (they are artefacts of updating all
genes at once; with asynchronous updating they disappear too).
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts, quant

P = bio.P
fig, ax = bio.canvas(30.0, 11.0)
bio.panel(ax, "A", (0.1, 10.9))


def step(s):
    a, b, c = s
    return (1 - c, 1 - a, b)


pos = {(0, 1, 1): (2.2, 8.6), (1, 0, 0): (2.2, 3.0),
       (0, 0, 0): (6.2, 9.2), (1, 1, 0): (9.6, 9.2), (1, 0, 1): (7.9, 6.6),
       (0, 0, 1): (6.2, 4.2), (0, 1, 0): (9.6, 4.2), (1, 1, 1): (7.9, 1.6)}
for s, xy in pos.items():
    fixed = step(s) == s
    bio.box(ax, xy, 1.5, 0.8, "positive" if fixed else "neutral", text="".join(map(str, s)), size="small")
for s, xy in pos.items():
    t = step(s)
    if t == s:
        ax.annotate("", xy=(xy[0] + 0.5, xy[1] + 0.42), xytext=(xy[0] - 0.5, xy[1] + 0.42),
                    arrowprops=dict(arrowstyle="->", color=P.ink(), lw=1.0, connectionstyle="arc3,rad=-1.2"))
    else:
        bio.arrow(ax, xy, pos[t], kind="process", shrink=0.75)
bio.label(ax, (2.2, 6.0), "fixed points", size="tiny", color=P.muted())
bio.label(ax, (8.0, 10.4), "3-cycles", size="tiny", color=P.muted())
bio.label(ax, (5.9, 0.4), "states (a b c);  a′ = not c,  b′ = not a,  c′ = b", size="tiny")

bio.panel(ax, "B", (13.0, 10.9))
pb = charts.axes_at(ax, (15.0, 2.0, 6.0, 7.6))
pc = charts.axes_at(ax, (23.4, 2.0, 6.0, 7.6))
n, th = 4, 0.5
Fp = lambda x: x ** n / (th ** n + x ** n)
Fm = lambda x: th ** n / (th ** n + x ** n)


def rhs(t, y):
    a, b, c = y
    return [Fm(c) - a, Fm(a) - b, Fp(b) - c]


rng = np.random.default_rng(4)
for k in range(12):
    y0 = rng.random(3)
    sol = solve_ivp(rhs, (0, 12), y0, t_eval=np.linspace(0, 12, 300))
    end = sol.y[:, -1]
    tok = "mesoderm" if end[0] > 0.5 else "ectoderm"
    pb.plot(sol.t, sol.y[0], color=quant.line_color(tok), lw=1.0, alpha=0.9)
    pc.plot(sol.y[0], sol.y[2], color=quant.line_color(tok), lw=1.0, alpha=0.9)
    pc.plot(end[0], end[2], "o", color=quant.line_color(tok), ms=5)
pb.set_xlim(0, 12)
pb.set_ylim(0, 1.05)
charts.style_axes(pb, "time t", "a")
charts.title(pb, "Time courses of a")
pc.set_xlim(0, 1.05)
pc.set_ylim(0, 1.05)
charts.style_axes(pc, "a", "c")
charts.title(pc, "Two attractors: (1,0,0) and (0,1,1)")
