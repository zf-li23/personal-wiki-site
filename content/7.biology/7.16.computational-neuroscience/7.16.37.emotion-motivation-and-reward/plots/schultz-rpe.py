"""Schematic of the responses of midbrain dopamine neurons in the experiments of Schultz and colleagues (1997).

Peri-stimulus time histograms (simulated Poisson spike counts, 20 trials, 20 ms bins) for three conditions:
reward without prediction; reward predicted by a conditioned stimulus (CS) 1 s earlier; CS followed by omission.
Baseline 4 Hz; phasic burst to 25 Hz for 150 ms (latency 80 ms); pause to 0 Hz for 200 ms at the time of
the omitted reward. Schematic of the published data shapes, not data.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
dt, n_trials = 0.02, 20
t = np.arange(-0.5, 2.0, dt)


def rate(events):
    r = np.full_like(t, 4.0)
    for t0, kind in events:
        if kind == "burst":
            r[(t >= t0 + 0.08) & (t < t0 + 0.23)] = 25.0
        else:
            r[(t >= t0 + 0.05) & (t < t0 + 0.25)] = 0.0
    return r


cases = [("No prediction, reward occurs", [(1.0, "burst")], [], [1.0]),
         ("Reward predicted by CS, reward occurs", [(0.0, "burst")], [0.0], [1.0]),
         ("Reward predicted by CS, no reward", [(0.0, "burst"), (1.0, "pause")], [0.0], [])]
fig, axs = plt.subplots(3, 1, figsize=(7.5, 5.6), sharex=True)
for ax, (title, ev, cs, rw) in zip(axs, cases):
    r = rate(ev)
    counts = rng.poisson(r * dt, size=(n_trials, len(t))).sum(axis=0) / (n_trials * dt)
    ax.bar(t, counts, width=dt, align="edge", color=P.fill("neuron"), edgecolor=P.edge("neuron"), lw=0.3)
    for c in cs:
        ax.axvline(c, color=P.edge("dna"), lw=1.2, ls="--")
        ax.text(c + 0.02, 38, "CS", color=P.edge("dna"), fontsize=8.5)
    for x in rw:
        ax.axvline(x, color=P.edge("positive"), lw=1.2, ls="--")
        ax.text(x + 0.02, 38, "reward", color=P.edge("positive"), fontsize=8.5)
    if not rw and cs:
        ax.text(1.02, 38, "(no reward)", color=P.muted(), fontsize=8.5)
    ax.set_ylim(0, 44)
    ax.set_ylabel("Rate / Hz")
    ax.set_title(title, loc="left", fontsize=9.5)
axs[-1].set_xlabel("Time / s")
fig.tight_layout()
