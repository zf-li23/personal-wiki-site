"""A half-centre oscillator and an intersegmental travelling wave (Matsuoka rate model).

Each half-centre is a rate unit with slow adaptation (a stand-in for the ionic mechanisms of
the tadpole CPG); left and right inhibit each other reciprocally (crossed glycinergic inhibition).
A: alternation of the left and right half-centres of one segment under tonic excitation.
B: twelve segments, each a half-centre pair, coupled to their neighbours by weak excitation
of the same side; the intrinsic frequency declines from head to tail (adaptation time constant
50 -> 62 ms), so rostral segments lead and each burst is followed by the next segment's
burst: a head-to-tail wave with a nearly constant phase lag.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
dt = 0.1  # ms
T = 600
t = np.arange(0, T, dt)
tau, tauA, beta, w = 6.0, 60.0, 2.5, 2.5


def simulate(nseg, drive, coup=0.3, tA=None):
    tA = np.full(nseg, tauA) if tA is None else tA
    x = np.zeros((nseg, 2)); v = np.zeros((nseg, 2))
    x[:, 0] = 0.1
    Y = np.zeros((len(t), nseg, 2))
    for k in range(len(t)):
        y = np.maximum(x, 0)
        inh = w * y[:, ::-1]
        nb = np.zeros_like(y)
        nb[1:] += coup * y[:-1]
        nb[:-1] += coup * y[1:]
        dx = (-x - beta * v - inh + drive[:, None] + nb) / tau
        dv = (-v + y) / tA[:, None]
        x += dt * dx; v += dt * dv
        Y[k] = y
    return Y


Y1 = simulate(1, np.array([1.0]))
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4.0), gridspec_kw={"width_ratios": [1, 1.3]})
a.plot(t, Y1[:, 0, 0] + 0.6, color=P.edge("dna"), lw=1.6, label="left half-centre")
a.plot(t, Y1[:, 0, 1], color=P.edge("rna"), lw=1.6, label="right half-centre")
a.set_xlim(200, 600)
a.set_yticks([])
a.set_xlabel("Time / ms")
a.legend(frameon=False, fontsize=8, loc="upper right", bbox_to_anchor=(1, 1.12), ncol=2)
a.set_title("A", loc="left", fontweight="bold")
nseg = 12
drive = np.full(nseg, 1.0)
Y = simulate(nseg, drive, tA=np.linspace(50.0, 62.0, nseg))
for s in range(nseg):
    on = Y[:, s, 0] > 0.25 * Y[:, s, 0].max()
    b.fill_between(t, s - 0.4, s + 0.4, where=on, color=P.fill("dna"), lw=0)
    onr = Y[:, s, 1] > 0.25 * Y[:, s, 1].max()
    b.fill_between(t, s - 0.4, s + 0.4, where=onr, color=P.fill("rna"), lw=0, alpha=0.55)
b.set_xlim(300, 600)
b.set_ylim(nseg - 0.5, -0.5)
b.set_yticks([0, nseg - 1]); b.set_yticklabels(["head", "tail"])
b.set_ylabel("Segment")
b.set_xlabel("Time / ms")
b.text(302, -0.9, "blue: left bursts; orange: right bursts", fontsize=7.5, color=P.muted(), va="bottom")
b.set_title("B", loc="left", fontweight="bold", pad=14)
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
