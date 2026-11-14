"""Two-state Markov model of roaming and dwelling in C. elegans (illustrative rates, Example 7.5.1).

Rates are per minute: k_RD = 1 / (mean roaming bout), k_DR = 1 / (mean dwelling bout).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
cases = [("wild type", 1.0, 4.0), ("no serotonin", 1.0, 1.5), ("no PDF", 0.4, 4.0)]


def simulate(mr, md, T, rng):
    t, state, segs = 0.0, 1 if rng.random() < mr / (mr + md) else 0, []
    while t < T:
        dur = rng.exponential(mr if state else md)
        segs.append((t, min(dur, T - t), state))
        t += dur
        state = 1 - state
    return segs


rng = np.random.default_rng(0)
fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.4), gridspec_kw={"width_ratios": [2.3, 1]})
for i, (name, mr, md) in enumerate(cases):
    y = 2 - i
    for t0, d, s in simulate(mr, md, 60, rng):
        a.broken_barh([(t0, d)], (y - 0.32, 0.64), color=P.fill("rna") if s else P.light("neutral"),
                      edgecolor="none")
a.set_yticks([2, 1, 0]); a.set_yticklabels([c[0] for c in cases])
a.set_xlim(0, 60); a.set_xlabel("Time / min")
a.set_title("A", loc="left", fontweight="bold")
a.broken_barh([(40, 3)], (2.55, 0.25), color=P.fill("rna")); a.text(43.5, 2.67, "roaming", va="center", fontsize=8, color=P.ink())
a.broken_barh([(51, 3)], (2.55, 0.25), color=P.light("neutral")); a.text(54.5, 2.67, "dwelling", va="center", fontsize=8, color=P.ink())
a.set_ylim(-0.5, 2.95)
sim, ana = [], []
for name, mr, md in cases:
    segs = simulate(mr, md, 20000, rng)
    sim.append(sum(d for _, d, s in segs if s) / 20000)
    ana.append(mr / (mr + md))
x = np.arange(3)
b.bar(x, sim, color=P.fill("rna"), edgecolor=P.edge("rna"), width=0.6)
b.plot(x, ana, "o", color=P.ink(), ms=5)
b.set_xticks(x); b.set_xticklabels([c[0] for c in cases], fontsize=8)
b.set_ylabel("Fraction of time roaming"); b.set_ylim(0, 0.5)
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
