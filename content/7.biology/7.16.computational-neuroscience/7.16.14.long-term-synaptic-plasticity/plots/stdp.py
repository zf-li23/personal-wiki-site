"""Spike-timing-dependent plasticity: the window and the trace implementation.

Pair-based rule with exponential window, dt = t_post - t_pre:
  DW = A_+ exp(-dt / tau_+)   for dt > 0 (pre before post: potentiation),
  DW = -A_- exp(dt / tau_-)   for dt < 0 (post before pre: depression),
with tau_+ = 16.8 ms and tau_- = 33.7 ms (fits to hippocampal culture data), A_+ = 1 and
A_- = 0.55 (arbitrary units; A_- tau_- slightly exceeds A_+ tau_+).
A: the window (line) and the weight change of single pre-post pairings computed with the trace
   algorithm (dots): the two agree for isolated pairs.
B: the trace algorithm for one pre-post pair (pre at 20 ms, post at 30 ms): a presynaptic trace x
   (decay tau_+) is read out at the postsynaptic spike (potentiation), a postsynaptic trace y
   (decay tau_-) is read out at the presynaptic spike (depression); lower trace: weight.
C: the same for a post-pre pair (post at 20 ms, pre at 30 ms).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
tp, tm, Ap, Am = 16.8, 33.7, 1.0, 0.55


def window(d):
    d = np.asarray(d, float)
    return np.where(d >= 0, Ap * np.exp(-np.abs(d) / tp), -Am * np.exp(-np.abs(d) / tm))


def pair_traces(tpre, tpost, T=140.0, dt=0.1):
    t = np.arange(0, T, dt)
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    w = np.zeros_like(t)
    xv = yv = wv = 0.0
    for k, tt in enumerate(t):
        xv *= np.exp(-dt / tp)
        yv *= np.exp(-dt / tm)
        if abs(tt - tpre) < dt / 2:
            wv -= Am * yv
            xv += 1.0
        if abs(tt - tpost) < dt / 2:
            wv += Ap * xv
            yv += 1.0
        x[k], y[k], w[k] = xv, yv, wv
    return t, x, y, w


fig = plt.figure(figsize=(13, 4.2))
gs = fig.add_gridspec(2, 3, width_ratios=[1.15, 1, 1])
ax = fig.add_subplot(gs[:, 0])
d = np.linspace(-100, 100, 600)
ax.plot(d, window(d), color=P.edge("protein"), lw=2.2)
dd = np.arange(-80, 81, 10)
dd = dd[dd != 0]
sim = []
for dl in dd:
    t, x, y, w = pair_traces(150.0, 150.0 + dl, T=400.0)
    sim.append(w[-1])
ax.plot(dd, sim, "o", ms=5, color=P.edge("negative"), label="trace algorithm")
ax.axhline(0, color=P.muted(), lw=0.8)
ax.axvline(0, color=P.muted(), lw=0.8)
ax.set_xlabel("$t_{\\mathrm{post}} - t_{\\mathrm{pre}}$ / ms")
ax.set_ylabel("Weight change per pairing")
ax.set_title("A  STDP window", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.grid(True, alpha=0.3)
for col, (tpre, tpost, ttl) in enumerate(((20.0, 30.0, "B  Pre before post"), (30.0, 20.0, "C  Post before pre"))):
    t, x, y, w = pair_traces(tpre, tpost)
    a1 = fig.add_subplot(gs[0, 1 + col])
    a1.plot(t, x, color=P.edge("dna"), lw=1.6, label="pre trace $x$")
    a1.plot(t, y, color=P.edge("negative"), lw=1.6, label="post trace $y$")
    a1.axvline(tpre, color=P.edge("dna"), lw=0.8, ls=":")
    a1.axvline(tpost, color=P.edge("negative"), lw=0.8, ls=":")
    a1.set_ylim(0, 1.5)
    a1.tick_params(labelbottom=False)
    a1.set_title(ttl, loc="left", fontsize=10)
    a1.legend(frameon=False, fontsize=7.5, loc="upper right")
    a2 = fig.add_subplot(gs[1, 1 + col], sharex=a1)
    a2.plot(t, w, color=P.edge("positive") if w[-1] > 0 else P.edge("negative"), lw=2.0)
    a2.axhline(0, color=P.muted(), lw=0.6)
    a2.set_ylim(-0.8, 1.0)
    a2.set_xlabel("Time / ms")
    a2.set_ylabel("$\\Delta w$")
    for a in (a1, a2):
        a.grid(True, alpha=0.3)
fig.tight_layout()
