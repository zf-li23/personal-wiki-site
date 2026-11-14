"""Continuous, instantaneous and one-zero recording of a simulated behavioral state (feeding bouts).

Bouts: exponential durations, mean 20 s; gaps: exponential, mean 40 s; true proportion of time = 1/3.
B: mean estimate over 400 sessions of 600 s for sample intervals of 5-120 s.
"""

import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT
rng = np.random.default_rng(4)
L = 600.0


def session(rng):
    t, on, bouts = 0.0, rng.random() < 1 / 3, []
    while t < L:
        d = rng.exponential(20.0 if on else 40.0)
        if on:
            bouts.append((t, min(t + d, L)))
        t += d
        on = not on
    return bouts


def state_at(bouts, x):
    return any(a <= x < b for a, b in bouts)


def occurred(bouts, a, b):
    return any(s < b and e > a for s, e in bouts)


fig, ax = bio.canvas(30.0, 10.0)
bouts = session(rng)
pa = C.axes_at(ax, (2.6, 1.6, 13.0, 6.8))
feed = C.line("positive")
for a, b in bouts:
    pa.fill_between([a, b], 2.6, 3.0, color=feed, lw=0)
dt = 30.0
pts = np.arange(dt, L + 0.1, dt)
for x in pts:
    on = state_at(bouts, x - 1e-9)
    pa.plot([x], [1.6], "o", ms=5, color=feed if on else P.muted(), mfc=feed if on else "none")
for k in range(int(L / dt)):
    a, b = k * dt, (k + 1) * dt
    if occurred(bouts, a, b):
        pa.fill_between([a + 1, b - 1], 0.4, 0.8, color=feed, alpha=0.55, lw=0)
    else:
        pa.plot([a + 1, b - 1, b - 1, a + 1, a + 1], [0.4, 0.4, 0.8, 0.8, 0.4], color=P.muted(), lw=0.5)
true = sum(b - a for a, b in bouts) / L
inst = np.mean([state_at(bouts, x - 1e-9) for x in pts])
oz = np.mean([occurred(bouts, k * dt, (k + 1) * dt) for k in range(int(L / dt))])
pa.set_yticks([0.6, 1.6, 2.8])
pa.set_yticklabels([f"one-zero ({oz:.2f})", f"instantaneous ({inst:.2f})", f"continuous ({true:.2f})"])
pa.set_xlim(0, L)
pa.set_ylim(0, 3.5)
pa.spines["left"].set_visible(False)
pa.tick_params(axis="y", length=0)
C.style_axes(pa, "time / s", None)
bio.panel(ax, "A", (0.3, 9.7))

intervals = np.array([5, 10, 15, 20, 30, 45, 60, 90, 120], float)
sessions = [session(rng) for _ in range(400)]
e_inst, e_oz, e_true = [], [], np.mean([sum(b - a for a, b in s) / L for s in sessions])
for dt in intervals:
    ps = np.arange(dt, L + 0.1, dt)
    e_inst.append(np.mean([np.mean([state_at(s, x - 1e-9) for x in ps]) for s in sessions]))
    n = int(L / dt)
    e_oz.append(np.mean([np.mean([occurred(s, k * dt, (k + 1) * dt) for k in range(n)]) for s in sessions]))
pb = C.axes_at(ax, (19.8, 1.6, 9.4, 6.8))
pb.axhline(e_true, color=P.muted(), lw=0.9, ls=(0, (3, 2)))
pb.plot(intervals, e_inst, "o-", color=C.line("dna"), lw=1.7, ms=4)
pb.plot(intervals, e_oz, "s-", color=C.line("negative"), lw=1.7, ms=4)
pb.text(118, e_true - 0.03, "true proportion", color=P.muted(), fontsize=FS["tiny"], ha="right", va="top")
pb.text(118, e_inst[-1] + 0.03, "instantaneous", color=C.line("dna"), fontsize=FS["tiny"], ha="right", va="bottom")
pb.text(118, e_oz[-1] - 0.04, "one-zero", color=C.line("negative"), fontsize=FS["tiny"], ha="right", va="top")
pb.set_xlim(0, 125)
pb.set_ylim(0, 1)
C.style_axes(pb, "sample interval / s", "estimated proportion of time feeding")
bio.panel(ax, "B", (17.8, 9.7))
