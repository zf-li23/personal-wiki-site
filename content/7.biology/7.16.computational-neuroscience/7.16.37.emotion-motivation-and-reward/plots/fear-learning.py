"""Acquisition and extinction of conditioned fear with the Rescorla-Wagner rule.

Associative strength V of a tone (CS): Delta V = alpha beta (lambda - V) per trial,
lambda = 1 when the tone is paired with a shock (US), 0 when the tone is presented alone.
Acquisition: 10 trials, alpha beta = 0.3. Extinction: 20 trials, alpha beta = 0.15.
Freezing (percent of time) = 80 V. The dashed point marks the spontaneous recovery seen
when testing a day after extinction (an observation the rule cannot produce).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
V, hist = 0.0, [0.0]
for _ in range(10):
    V += 0.3 * (1 - V)
    hist.append(V)
for _ in range(20):
    V += 0.15 * (0 - V)
    hist.append(V)
trials = np.arange(len(hist))
fig, ax = plt.subplots(figsize=(7.5, 3.4))
ax.axvspan(0.5, 10.5, color=P.light("negative"), zorder=0)
ax.plot(trials, 80 * np.array(hist), "o-", color=P.edge("dna"), ms=4, lw=1.8, label="Rescorla-Wagner prediction")
ax.plot([33], [80 * 0.35], "s", color=P.edge("negative"), ms=7, label="next-day test (spontaneous recovery)")
ax.plot([30, 33], [80 * hist[-1], 80 * 0.35], ls=":", color=P.edge("negative"), lw=1.2)
ax.text(5.5, 86, "acquisition\n(tone + shock)", ha="center", fontsize=8.5, color=P.muted())
ax.text(20.5, 86, "extinction (tone alone)", ha="center", fontsize=8.5, color=P.muted())
ax.set_xlabel("Trial")
ax.set_ylabel("Freezing to the tone / %")
ax.set_ylim(-3, 100)
ax.set_xlim(-0.5, 34.5)
ax.legend(frameon=False, fontsize=8, loc="center right")
ax.grid(True, alpha=0.3)
fig.tight_layout()
