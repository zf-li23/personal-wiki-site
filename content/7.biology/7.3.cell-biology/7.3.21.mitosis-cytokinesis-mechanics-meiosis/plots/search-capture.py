"""Search and capture: how fast can dynamic microtubules find kinetochores? (model after Holy and Leibler 1994,
Wollman et al. 2005).

Each spindle pole keeps n = 250 microtubules; a microtubule grows in a random direction at v_g = 0.2 um/s
until it undergoes catastrophe (rate f, no rescue), shrinks back at v_s = 0.3 um/s and is renucleated in a new
direction. A kinetochore of capture radius a at distance d is hit by one growth phase with probability
p = (a / 2d)^2 exp(-f d / v_g): the solid-angle fraction of the target times the probability of growing that
far. One cycle lasts (1/f)(1 + v_g/v_s), so the capture rate of one kinetochore is
    lambda(f, d) = n f / (1 + v_g/v_s) * (a / 2d)^2 * exp(-f d / v_g),
which is maximal at f* = v_g / d (Holy and Leibler).
(A) lambda as a function of f for kinetochores at 4, 7 and 10 um (a = 0.25 um); circles mark f* = v_g/d.
(B) Fraction of the 92 kinetochores of a human cell captured over time (each at a distance drawn uniformly
from 4 to 10 um, f = 0.03 per s; capture times exponential with rate lambda; mean of 200 simulated cells):
unbiased search; with a RanGTP zone of radius 3 um around the chromosomes in which catastrophes are
suppressed (the exponential factor becomes exp(-f (d - 3 um) / v_g)); and with the zone plus the expanded
fibrous corona of unattached kinetochores (a = 0.6 um). The shaded band marks the 10-20 minutes that
prometaphase takes in human cells; dashed lines are the median time to capture the last kinetochore.
"""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(0)

N_MT, VG, VS = 250, 0.2, 0.3


def rate(f, d, a=0.25, zone=0.0):
    reach = np.maximum(d - zone, 0.0)
    return N_MT * f / (1 + VG / VS) * (a / (2 * d)) ** 2 * np.exp(-f * reach / VG)


fig, ax = bio.canvas(24.0, 9.0)
bio.panel(ax, "A", (0.2, 8.8))
a1 = charts.axes_at(ax, (1.8, 1.5, 8.6, 6.6))
f = np.logspace(-3, 0, 400)
for d, tok in ((4, "positive"), (7, "channel"), (10, "negative")):
    lam = rate(f, d) * 60  # per minute
    a1.plot(f, lam, color=charts.line(tok), lw=1.8, label=f"d = {d} µm")
    fs = VG / d
    a1.plot([fs], [rate(fs, d) * 60], "o", ms=5, mfc="none", mec=charts.line(tok))
a1.set_xscale("log")
a1.set_yscale("log")
a1.set_ylim(1e-4, 1)
a1.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
a1.text(0.0012, 2.0e-4, "circles: optimum f* = v_g / d", fontsize=FT["tiny"], color=P.muted())
charts.style_axes(a1, "catastrophe frequency f / s⁻¹", "capture rate per kinetochore / min⁻¹")

bio.panel(ax, "B", (12.0, 8.8))
b = charts.axes_at(ax, (13.6, 1.5, 9.8, 6.6))
b.axvspan(10, 20, color=P.fill("highlight"), alpha=0.35, lw=0)
b.text(15, 1.03, "prometaphase", ha="center", fontsize=FT["tiny"], color=P.muted())
t = np.linspace(0, 240, 1200)
F = 0.03
cases = [("unbiased search", dict(a=0.25, zone=0.0), "negative"),
         ("RanGTP zone (3 µm)", dict(a=0.25, zone=3.0), "channel"),
         ("zone + expanded corona", dict(a=0.6, zone=3.0), "positive")]
for name, kw, tok in cases:
    curves, last = [], []
    for _ in range(200):
        d = rng.uniform(4, 10, 92)
        tc = rng.exponential(1 / (rate(F, d, **kw) * 60))
        curves.append([(tc <= x).mean() for x in t[::10]])
        last.append(tc.max())
    b.plot(t[::10], np.mean(curves, axis=0), color=charts.line(tok), lw=1.8, label=name)
    m = np.median(last)
    if m < 240:
        b.axvline(m, color=charts.line(tok), ls="--", lw=0.8)
b.set_xlim(0, 240)
b.set_ylim(0, 1.08)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(b, "time after nuclear envelope breakdown / min", "fraction of kinetochores captured")
