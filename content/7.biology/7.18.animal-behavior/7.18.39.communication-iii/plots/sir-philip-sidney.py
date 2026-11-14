"""Region of honest signaling in the Sir Philip Sidney game (a = 0.6, b = 0.2):
r b <= d <= r a and b - r d <= c <= a - r d (c >= 0)."""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
A, B = 0.6, 0.2
fig, axs = plt.subplots(1, 2, figsize=(10, 3.8), sharey=True)
for ax, r, t in zip(axs, (0.5, 1.0), "AB"):
    d = np.linspace(r * B, r * A, 100)
    lo = np.maximum(B - r * d, 0)
    hi = A - r * d
    ax.fill_between(d, lo, hi, color=P.light("dna"), alpha=0.9, lw=0)
    ax.plot(d, lo, color=P.edge("dna"), lw=1.4)
    ax.plot(d, hi, color=P.edge("dna"), lw=1.4)
    for x in (r * B, r * A):
        ax.axvline(x, color=P.muted(), ls="--", lw=0.9)
    ax.text(r * B, 0.66, " d = rb", fontsize=8, color=P.muted())
    ax.text(r * A, 0.66, " d = ra", fontsize=8, color=P.muted())
    ax.text(np.mean(d), np.mean(hi + lo) / 2, "honest\nsignaling", ha="center", va="center", fontsize=8.5)
    ax.text(r * A + 0.02, (A - r * A) + 0.12, "above: needy beneficiaries\nwould not signal", fontsize=7.5,
            color=P.muted(), va="bottom")
    if lo.max() > 0:
        ax.text(r * A + 0.02, 0.03, "below: non-needy would\nalso signal", fontsize=7.5, color=P.muted())
    ax.set_xlim(0, 0.75); ax.set_ylim(0, 0.72)
    ax.set_xlabel("Donor's cost of giving, d")
    ax.set_title(f"{t}   r = {r:g}", loc="left", fontweight="bold")
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
axs[0].set_ylabel("Cost of the signal, c")
fig.tight_layout()
