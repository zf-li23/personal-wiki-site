"""Single-channel kinetics of the scheme C1 <-> C2 <-> O (rates per ms: C1->C2 0.2, C2->C1 1.0,
C2->O 2.0, O->C2 0.5), simulated with the Gillespie algorithm. A: 200 ms of a simulated patch-clamp
record (single-channel current -2 pA when open, Gaussian noise of 0.25 pA rms sampled every 0.05 ms).
B: open dwell times from 20 000 openings, logarithmic bins with square-root ordinate (Sigworth-Sine
display): one exponential with time constant 1/k(O->C2) = 2 ms, one open state. C: closed dwell times:
two exponential components (curve: exact distribution from the closed-state rate matrix), revealing
two closed states: short closures within bursts (C2) and long gaps between bursts (C1)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2), gridspec_kw=dict(width_ratios=[1.6, 1, 1]))
fig.subplots_adjust(wspace=0.35, left=0.06, right=0.98, bottom=0.17, top=0.87)
k12, k21, k2o, ko2 = 0.2, 1.0, 2.0, 0.5
rng = np.random.default_rng(0)
state, t = 2, 0.0
times, states = [0.0], [2]
open_d, closed_d = [], []
cur_closed = 0.0
while len(open_d) < 20000:
    if state == 0:
        dwell = rng.exponential(1 / k12); nxt = 1
    elif state == 1:
        tot = k21 + k2o; dwell = rng.exponential(1 / tot); nxt = 2 if rng.random() < k2o / tot else 0
    else:
        dwell = rng.exponential(1 / ko2); nxt = 1
    if state == 2:
        open_d.append(dwell)
    else:
        cur_closed += dwell
        if nxt == 2:
            closed_d.append(cur_closed); cur_closed = 0.0
    t += dwell; state = nxt
    times.append(t); states.append(state)
times, states = np.array(times), np.array(states)

ax = axs[0]
ts = np.arange(0, 200, 0.05)
idx = np.searchsorted(times, ts, side="right") - 1
i = np.where(states[idx] == 2, -2.0, 0.0) + 0.25 * rng.standard_normal(len(ts))
ax.plot(ts, i, color=charts.line("k"), lw=0.5)
ax.set_ylim(-3.2, 1.0)
ax.text(2, 0.6, "closed", fontsize=FT["tiny"], color=P.ink())
ax.text(2, -2.9, "open", fontsize=FT["tiny"], color=P.ink())
charts.style_axes(ax, "time / ms", "current / pA")
charts.title(ax, "A  Single-channel record")

def sqrt_hist(ax, d, pdf, tok, title):
    bins = np.logspace(-2, 3, 40)
    h, e = np.histogram(d, bins=bins)
    c = np.sqrt(e[:-1] * e[1:])
    ax.step(c, np.sqrt(h), where="mid", color=charts.line(tok), lw=1.2)
    tt = np.logspace(-2, 3, 300)
    # expected counts per log bin: N * f(t) * t * dln t
    dln = np.log(bins[1] / bins[0])
    ax.plot(tt, np.sqrt(len(d) * pdf(tt) * tt * dln), color=P.muted(), lw=1.2)
    ax.set_xscale("log")
    charts.style_axes(ax, "dwell time / ms", r"$\sqrt{\mathrm{events\ per\ bin}}$")
    charts.title(ax, title)

sqrt_hist(axs[1], np.array(open_d), lambda t: ko2 * np.exp(-ko2 * t), "k", "B  Open times")
Q = np.array([[-k12, k12], [k21, -(k21 + k2o)]])
u = np.array([0, k2o])
p0 = np.array([0.0, 1.0])
pdf_c = lambda tt: np.array([p0 @ expm(Q * x) @ u for x in np.atleast_1d(tt)])
sqrt_hist(axs[2], np.array(closed_d), pdf_c, "neutral", "C  Closed times")
