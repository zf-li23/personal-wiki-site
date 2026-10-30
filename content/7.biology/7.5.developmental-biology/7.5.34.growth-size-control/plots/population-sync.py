"""Loss of synchrony in a growing cell population (Section 34.3).

Monte Carlo: 4000 cells divide synchronously at t = 0; generation times have mean 1 and a gamma distribution with
coefficient of variation 0.15, shifted so that no cycle is shorter than 0.6. Four rules: fixed cycle (every cycle
= 1); fully inherited cycle (each lineage keeps the cycle time drawn at t = 0); no inheritance (each daughter draws
anew: the renewal process); mixed, daughters keep the mother's cycle with probability beta = 0.7 and draw anew
otherwise. A: log2 of the population against time. B: the deviation of log2 N from its long-time linear trend:
the staircase of the fixed cycle persists; with inherited cycle times the lineages dephase quickly, leaving only a
small residual oscillation at the period of the fastest lineages; without inheritance the oscillation decays
steadily at the rate set by the complex roots of 2 g(p) = 1; partial inheritance damps it sooner.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C
from wikibio import quant as Q

P = bio.P
rng = np.random.default_rng(3)
N0, T = 4000, 8.0
cv, gmin = 0.15, 0.6
shape = ((1 - gmin) / (cv * 1.0)) ** 2
scale = (1 - gmin) / shape


def draw(n):
    return gmin + rng.gamma(shape, scale, n)


def run(rule, beta=0.7):
    births = []                    # times of division events
    t = np.zeros(N0)
    g = np.ones(N0) if rule == "fixed" else draw(N0)
    events = []
    active_t, active_g = t + g, g
    while len(active_t):
        keep = active_t < T
        active_t, active_g = active_t[keep], active_g[keep]
        if not len(active_t):
            break
        events.append(active_t.copy())
        n = len(active_t)
        tt = np.repeat(active_t, 2)
        if rule == "fixed":
            gg = np.ones(2 * n)
        elif rule == "inherited":
            gg = np.repeat(active_g, 2)
        elif rule == "renewal":
            gg = draw(2 * n)
        else:
            gg = np.where(rng.random(2 * n) < beta, np.repeat(active_g, 2), draw(2 * n))
        active_t, active_g = tt + gg, gg
        if len(active_t) > 3e6:
            break
    ev = np.sort(np.concatenate(events)) if events else np.array([])
    ts = np.linspace(0, T, 801)
    N = N0 + np.searchsorted(ev, ts)
    return ts, N


rules = [("fixed", "fixed cycle", "neutral"), ("inherited", "inherited cycle", "protein"),
         ("mixed", "mixed, β = 0.7", "highlight"), ("renewal", "no inheritance", "enzyme")]
fig, ax = bio.canvas(26.0, 9.5)
pa = C.axes_at(ax, (1.8, 1.5, 9.4, 6.6))
pb = C.axes_at(ax, (15.0, 1.5, 9.4, 6.6))
for rule, name, tk in rules:
    ts, N = run(rule)
    y = np.log2(N / N0)
    pa.plot(ts, y, color=Q.line_color(tk), lw=1.5, label=name)
    sel = ts > 3
    c = np.polyfit(ts[sel], y[sel], 1)
    pb.plot(ts, y - np.polyval(c, ts), color=Q.line_color(tk), lw=1.3, label=name)
pa.set_xlim(0, T)
C.style_axes(pa, "t / mean cycle time", "log₂ N(t) / N(0)")
pa.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
pb.set_xlim(0, T)
pb.set_ylim(-0.6, 0.6)
C.style_axes(pb, "t / mean cycle time", "deviation from trend")
bio.panel(ax, "A", (0.3, 9.3))
bio.label(ax, (1.8, 9.1), "Population growth after synchronous division", size="small", bold=True, ha="left", va="top")
bio.panel(ax, "B", (13.5, 9.3))
bio.label(ax, (15.0, 9.1), "Residual synchrony", size="small", bold=True, ha="left", va="top")
