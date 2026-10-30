"""Organ size by negative feedback versus an intrinsic program (Section 34.5; a minimal model).

Feedback ("chalone") model: the organ of mass M secretes an inhibitor I into a well-mixed circulation, dI/dt = p M - k I,
and grows as dM/dt = g M (1 - I / I*) (atrophy when I > I*), with g = 0.3, p = k = 0.5, I* = 1, so the set point is
M* = k I* / p = 1. Intrinsic model: the organ grows at the same rate until an internal clock stops it when it has reached the same size (t = 13), with
no feedback. A: removal of two thirds of the organ at t = 20 (as in partial hepatectomy): the feedback organ
regrows to its set point, the intrinsic one stays small. B: grafting an extra organ of mass 0.5 at t = 20: with
feedback the total mass returns to M* (both organs shrink); without, the total stays larger.
"""

import numpy as np
from scipy.integrate import solve_ivp
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
g, p, k, Is = 0.3, 0.5, 0.5, 1.0


def fb(t, y):
    M, I = y
    return [g * M * (1 - I / Is), p * M - k * I]


def run_fb(event):
    s1 = solve_ivp(fb, (0, 20), [0.02, 0.0], max_step=0.05, dense_output=True)
    M, I = s1.y[:, -1]
    M = event(M)
    s2 = solve_ivp(fb, (20, 60), [M, I], max_step=0.05, dense_output=True)
    return np.concatenate([s1.t, s2.t]), np.concatenate([s1.y[0], s2.y[0]])


def run_int(event, tstop=np.log(50) / 0.3):
    t = np.linspace(0, 60, 1200)
    M = 0.02 * np.exp(g * np.minimum(t, tstop))
    M = np.where(t >= 20, event(M[np.searchsorted(t, 20) - 1]) + 0 * M, M)
    return t, M


fig, ax = bio.canvas(26.0, 9.5)
for j, (title, ev) in enumerate((("Removal of two thirds", lambda M: M / 3), ("Graft of an extra organ (total mass)", lambda M: M + 0.5))):
    pa = C.axes_at(ax, (1.8 + 13.2 * j, 1.5, 9.4, 6.6))
    t1, M1 = run_fb(ev)
    t2, M2 = run_int(ev)
    pa.plot(t1, M1, color=Q.line_color("positive"), lw=1.8, label="feedback (chalone)")
    pa.plot(t2, M2, color=Q.line_color("drug"), lw=1.6, ls=(0, (5, 2)), label="intrinsic program")
    pa.axvline(20, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
    pa.axhline(1.0, color=P.muted(), lw=0.6)
    pa.set_xlim(0, 60)
    pa.set_ylim(0, 1.7)
    C.style_axes(pa, "time", "organ mass / set point")
    pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper right")
    bio.panel(ax, "AB"[j], (0.3 + 13.2 * j, 9.3))
    bio.label(ax, (1.8 + 13.2 * j, 9.1), title, size="small", bold=True, ha="left", va="top")
