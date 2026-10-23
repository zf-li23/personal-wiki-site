"""Four analysts determine Fe in the same reference material (true mass fraction 37.40 %).
Dots are the individual results, bars the means: accuracy is the distance of the mean from
the true value, precision the scatter of the results about their own mean."""

import numpy as np
import matplotlib.pyplot as plt

true = 37.40
results = {
    "A": [37.36, 37.42, 37.38, 37.45],   # accurate and precise
    "B": [37.02, 37.08, 37.05, 36.98],   # precise but biased
    "C": [36.45, 36.92, 37.18, 36.70],   # neither
    "D": [36.80, 37.10, 37.80, 37.95],   # mean close to the truth by chance, poor precision
}
labels = {
    "A": "high accuracy, high precision",
    "B": "low accuracy, high precision",
    "C": "low accuracy, low precision",
    "D": "apparent accuracy, low precision",
}

fig, ax = plt.subplots(figsize=(8, 3.6))
for k, (name, x) in enumerate(results.items()):
    yk = 3 - k
    ax.plot(x, [yk] * len(x), "o", color="C0", ms=6, alpha=0.85)
    m = np.mean(x)
    ax.plot([m, m], [yk - 0.25, yk + 0.25], color="C3", lw=2.2)
    ax.text(38.08, yk, labels[name], va="center", fontsize=9)
ax.axvline(true, color="0.4", ls="--", lw=1.2)
ax.text(true, 3.55, "true value", ha="center", fontsize=9, color="0.4")
ax.set_yticks([3, 2, 1, 0])
ax.set_yticklabels(list(results))
ax.set_ylim(-0.6, 3.8)
ax.set_xlim(36.3, 38.1)
ax.set_xlabel(r"$w$(Fe) / %")
ax.plot([], [], "o", color="C0", label="single result")
ax.plot([], [], color="C3", lw=2.2, label="mean")
ax.legend(frameon=False, fontsize=9, loc="lower left", ncol=2)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.subplots_adjust(left=0.06, right=0.66, bottom=0.17, top=0.95)
