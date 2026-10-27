"""Two circuits that adapt perfectly to a sustained stimulus.

A: incoherent feed-forward loop. The stimulus S activates the output R directly and, more slowly, an
inhibitor Y of R: dY/dt = (S - Y)/tau_Y, dR/dt = (S/Y - R)/tau_R, with tau_Y = 10 and tau_R = 1
(arbitrary time units). At steady state Y = S, so R returns to 1 whatever S is; after each step the
transient depends only on the fold change of S (here 2, 4 and 8 in successive steps of 2-fold), not
on its absolute level (fold-change detection).
B: integral feedback. R is made in proportion to S and removed by Z; Z integrates the deviation of R
from a set point R0: dR/dt = S - Z R, dZ/dt = k (R - R0), with k = 0.2 and R0 = 1. The steady state
R = R0 holds for every S; steps of S from 1 to 2 to 4 give damped excursions that return exactly to
the set point (the logic of bacterial chemotaxis, where methylation of the receptors is the integrator).
The dashed curves show a non-adapting response R = S for comparison.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts, network

P = bio.P
FS = bio.core.FONT["tiny"]

fig, ax = bio.canvas(20.0, 10.6)


def step(t, levels, times):
    v = levels[0]
    for lv, tm in zip(levels[1:], times):
        if t >= tm:
            v = lv
    return v


# A: incoherent feed-forward loop
bio.panel(ax, "A", (0.1, 10.5))
d = network.Diagram(ax)
d.activity("S", (2.3, 9.0), "S", token="drug")
d.activity("Y", (4.6, 9.0), "Y (slow)", token="negative")
d.activity("R", (3.45, 7.5), "R", token="highlight")
d.connect("S", "Y", "positive")
d.connect("S", "R", "positive")
d.connect("Y", "R", "negative")
bio.label(ax, (6.6, 8.5), "incoherent\nfeed-forward loop", size="small", ha="left", color=P.ink())

pa = charts.axes_at(ax, (1.5, 1.2, 7.6, 5.0))
lv, tm = [1, 2, 4, 8], [20, 60, 100]
t = np.linspace(0, 140, 4000)
sol = solve_ivp(lambda tt, y: [(step(tt, lv, tm) - y[0]) / 10, (step(tt, lv, tm) / y[0] - y[1]) / 1.0],
                (0, 140), [1, 1], t_eval=t, max_step=0.05)
S = np.array([step(x, lv, tm) for x in t])
pa.plot(t, S / 4, color=P.muted(), lw=1.0, ls=(0, (4, 2)), label="stimulus S (÷4)")
pa.plot(t, sol.y[1], color=charts.line("highlight"), lw=2.0, label="output R")
pa.plot(t, sol.y[0] / 4, color=charts.line("negative"), lw=1.3, label="inhibitor Y (÷4)")
pa.set_xlim(0, 140)
pa.set_ylim(0, 2.3)
pa.legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="upper left", ncol=3)
charts.style_axes(pa, "time", "level")
charts.title(pa, "Equal fold changes give equal responses")

# B: integral feedback
bio.panel(ax, "B", (10.3, 10.5))
e = network.Diagram(ax)
e.activity("S2", (12.4, 9.0), "S", token="drug")
e.activity("R2", (14.8, 9.0), "R", token="highlight")
e.activity("Z", (14.8, 7.5), "Z = ∫(R − R₀) dt", token="negative")
e.connect("S2", "R2", "positive")
e.connect("R2", "Z", "positive", start=(14.35, 8.68), end=(14.35, 7.86))
e.connect("Z", "R2", "negative", start=(15.25, 7.86), end=(15.25, 8.64))
bio.label(ax, (17.0, 8.5), "integral\nfeedback", size="small", ha="left", color=P.ink())

pb = charts.axes_at(ax, (11.7, 1.2, 7.7, 5.0))
lv2, tm2 = [1, 2, 4], [20, 70]
t2 = np.linspace(0, 140, 4000)
sol2 = solve_ivp(lambda tt, y: [step(tt, lv2, tm2) - y[1] * y[0], 0.2 * (y[0] - 1.0)], (0, 140), [1, 1],
                 t_eval=t2, max_step=0.05)
S2 = np.array([step(x, lv2, tm2) for x in t2])
pb.plot(t2, S2, color=P.muted(), lw=1.0, ls=(0, (4, 2)), label="non-adapting (R = S)")
pb.plot(t2, sol2.y[0], color=charts.line("highlight"), lw=2.0, label="output R")
pb.plot(t2, sol2.y[1], color=charts.line("negative"), lw=1.3, label="integrator Z")
pb.axhline(1.0, color=P.muted(), lw=0.6)
pb.text(139, 1.06, "set point R₀", fontsize=FS, color=P.muted(), ha="right")
pb.set_xlim(0, 140)
pb.set_ylim(0, 4.6)
pb.legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="upper left", ncol=3)
charts.style_axes(pb, "time", "level")
charts.title(pb, "Return to the set point for every stimulus")
