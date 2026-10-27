"""A caspase switch: variable delay, then all-or-none activation (minimal model with the topology of
Eissing et al. 2004 and the single-cell observations of Goldstein et al. 2000 and Albeck et al. 2008).

Variables are fractions of the active forms: x = active initiator caspase (caspase-8 or -9), y = active
executioner caspase-3, z = free XIAP (relative to its resting level). A death stimulus u activates the
initiator; executioner caspase feeds back on the initiator; XIAP inhibits the executioner and is itself
destroyed when it binds active caspase:
    dx/dt = (u + a y)(1 - x) - d x
    dy/dt = b x (1 - y) - (c z + d) y
    dz/dt = p - (q + e y) z
a = b = 1, c = 32, d = 0.1, p = q = 0.02, e = 4 (per minute).
(A) Caspase-3 activity after constant stimuli of different strengths: below a threshold u* the cell stays
alive; above it activity stays near zero for a delay that lengthens as u approaches u*, then rises to the
"on" state in a few minutes. (B) Delay before activation versus stimulus; it diverges at u* (the slow
passage near the vanishing steady state). The "on" state persists when u is removed (irreversibility).
(C) 400 cells with lognormally distributed stimulus (median 0.008, sd of log 0.7): each dot is a cell;
times to activation are spread over hours, while the 10-90 % rise time of each cell is a few minutes.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
a, b, c, d, p, q, e = 1.0, 1.0, 32.0, 0.1, 0.02, 0.02, 4.0
T = 1500.0


def rhs(t, Y, u):
    x, y, z = Y
    return [(u + a * y) * (1 - x) - d * x, b * x * (1 - y) - (c * z + d) * y, p - (q + e * y) * z]


def run(u, T=T, n=6001):
    s = solve_ivp(rhs, (0, T), [0.0, 0.0, 1.0], args=(u,), method="LSODA", rtol=1e-7, atol=1e-10, dense_output=True)
    t = np.linspace(0, T, n)
    return t, s.sol(t)[1]


def timing(u):
    t, y = run(u, n=15001)
    if y[-1] < 0.3:
        return np.nan, np.nan
    m = y[-1]
    t10, t50, t90 = (t[np.argmax(y > f * m)] for f in (0.1, 0.5, 0.9))
    return t50, t90 - t10


fig, ax = bio.canvas(27.0, 9.0)
bio.panel(ax, "A", (0.2, 8.8))
A = charts.axes_at(ax, (1.8, 1.5, 7.6, 6.6))
for u, tok in ((0.003, "neutral"), (0.0045, "enzyme"), (0.007, "channel"), (0.02, "drug"), (0.1, "negative")):
    t, y = run(u)
    A.plot(t / 60, y, color=charts.line(tok), lw=1.7, label=f"u = {u:g}")
A.set_xlim(0, 10)
A.set_ylim(-0.02, 0.85)
A.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(A, "time after stimulus / h", "active caspase-3 (fraction)")

bio.panel(ax, "B", (10.6, 8.8))
B = charts.axes_at(ax, (12.2, 1.5, 5.6, 6.6))
us = np.geomspace(0.0036, 0.3, 30)
dl = np.array([timing(u)[0] for u in us])
B.plot(us, dl / 60, "o-", color=charts.line("negative"), ms=3, lw=1.4)
lo = 0.0034
B.axvline(lo, color=P.muted(), ls="--", lw=0.8)
B.text(lo * 1.1, 11.0, "threshold u*", fontsize=FT["tiny"], color=P.muted())
B.set_xscale("log")
B.set_ylim(0, 12.5)
charts.style_axes(B, "stimulus u", "delay to half-maximal activity / h")

bio.panel(ax, "C", (19.4, 8.8))
C = charts.axes_at(ax, (21.0, 1.5, 5.6, 6.6))
rng = np.random.default_rng(0)
cells = np.exp(np.log(0.008) + 0.7 * rng.standard_normal(400))
res = np.array([timing(u) for u in cells])
ok = ~np.isnan(res[:, 0])
C.scatter(res[ok, 0] / 60, res[ok, 1], s=7, color=charts.line("negative"), alpha=0.7, lw=0)
C.set_xlim(0, 12)
C.set_ylim(0, 30)
C.text(0.97, 0.9, f"{(~ok).sum()} of 400 cells stay alive", transform=C.transAxes, ha="right",
       fontsize=FT["tiny"], color=P.muted())
charts.style_axes(C, "time to activation / h", "10–90 % rise time / min")
