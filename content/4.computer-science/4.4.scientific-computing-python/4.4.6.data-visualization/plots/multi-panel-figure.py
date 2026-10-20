"""A three-panel figure built with the object-oriented interface (synthetic data)."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

# Theme-aware categorical colors (validated for both surfaces).
dark = sum(to_rgb(plt.rcParams["figure.facecolor"])) < 1.5
COLORS = ["#3987e5", "#d95926", "#199e70"] if dark else ["#2a78d6", "#eb6834", "#1baf7a"]

rng = np.random.default_rng(0)
strains = ["WT", "mutA", "mutB"]
rates = [0.50, 0.38, 0.28]  # growth rates in 1/h
capacities = [1.25, 0.95, 0.70]  # carrying capacities (OD600)
t = np.arange(0, 25, 1.0)
n_rep = 4


def logistic(t, r, k=1.2, n0=0.04):
    return k / (1 + (k / n0 - 1) * np.exp(-r * t))


# Replicates differ in growth rate; each reading has a small measurement error.
curves = {s: logistic(t[None, :], r * rng.lognormal(0, 0.06, (n_rep, 1)), k)
          * rng.lognormal(0, 0.02, (n_rep, t.size))
          for s, r, k in zip(strains, rates, capacities)}

# Expression z-scores: 12 genes x 6 samples, two clusters of genes respond to treatment.
effect = np.r_[np.full(4, 1.6), np.full(4, -1.4), np.zeros(4)]
expr = rng.normal(0, 0.35, (12, 6))
expr[:, 3:] += effect[:, None]
z = (expr - expr.mean(axis=1, keepdims=True)) / expr.std(axis=1, ddof=1, keepdims=True)

fig = plt.figure(figsize=(10, 3.6), layout="constrained")
ax_a, ax_b, ax_c = fig.subplots(1, 3, width_ratios=[1.3, 1, 1])

# (A) growth curves: mean with a band of +- 1 SD, log y axis
for s, c in zip(strains, COLORS):
    y = curves[s]
    m, sd = y.mean(axis=0), y.std(axis=0, ddof=1)
    ax_a.fill_between(t, m - sd, m + sd, color=c, alpha=0.2, linewidth=0)
    ax_a.plot(t, m, color=c, linewidth=2, label=s)
    ax_a.text(t[-1] + 0.4, m[-1], s, color=c, va="center", fontsize=9)
ax_a.set_yscale("log")
ax_a.set_xlim(0, 27.5)
ax_a.set_xlabel("Time (h)")
ax_a.set_ylabel("OD600")
ax_a.set_title("Growth curves (mean $\\pm$ SD, n = 4)", fontsize=10)

# (B) final OD: every replicate as a point, plus the mean
final = [curves[s][:, t.size // 2] for s in strains]
for i, (vals, c) in enumerate(zip(final, COLORS)):
    jitter = rng.uniform(-0.12, 0.12, vals.size)
    ax_b.scatter(np.full(vals.size, i) + jitter, vals, color=c, s=30, zorder=3)
    ax_b.hlines(vals.mean(), i - 0.25, i + 0.25, color="0.5", linewidth=2)
ax_b.set_xticks(range(3), strains)
ax_b.set_xlim(-0.6, 2.6)
ax_b.set_ylim(0, None)
ax_b.set_ylabel("OD600 at 12 h")
ax_b.set_title("Replicates at 12 h", fontsize=10)

# (C) heatmap with a diverging colormap centred at zero
lim = np.abs(z).max()
im = ax_c.imshow(z, cmap="RdBu_r", vmin=-lim, vmax=lim, aspect="auto")
ax_c.set_xticks(range(6), [f"S{j + 1}" for j in range(6)])
ax_c.set_yticks(range(12), [f"g{i + 1}" for i in range(12)], fontsize=8)
ax_c.axvline(2.5, color="0.5", linewidth=1)
ax_c.set_title("Expression (row z-score)", fontsize=10)
fig.colorbar(im, ax=ax_c, label="z-score", shrink=0.9)

for ax in (ax_a, ax_b):
    ax.spines[["top", "right"]].set_visible(False)
for ax, letter in zip((ax_a, ax_b, ax_c), "ABC"):
    ax.set_title(letter, loc="left", fontweight="bold", fontsize=12)
