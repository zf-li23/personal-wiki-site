"""Reaction potential-energy profiles: (left) one elementary step with and without a catalyst;
(right) a two-step reaction through an intermediate."""

import numpy as np
import matplotlib.pyplot as plt


def profile(x, levels, centers, width=0.09):
    """Smooth curve through alternating minima and maxima at the given abscissae."""
    xs = np.array(centers)
    ys = np.array(levels)
    y = np.interp(x, xs, ys)
    # smooth the piecewise-linear profile with cosine easing between nodes
    out = np.empty_like(x)
    for i in range(len(xs) - 1):
        m = (x >= xs[i]) & (x <= xs[i + 1])
        s = (x[m] - xs[i]) / (xs[i + 1] - xs[i])
        out[m] = ys[i] + (ys[i + 1] - ys[i]) * (1 - np.cos(np.pi * s)) / 2
    out[x < xs[0]] = ys[0]
    out[x > xs[-1]] = ys[-1]
    return out


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.2))
x = np.linspace(0, 1, 500)

y_un = profile(x, [0, 0, 100, -40, -40], [0, 0.15, 0.5, 0.85, 1.0])
y_cat = profile(x, [0, 0, 55, -40, -40], [0, 0.15, 0.5, 0.85, 1.0])
ax1.plot(x, y_un, color="C0", lw=1.8, label="uncatalyzed")
ax1.plot(x, y_cat, color="C2", lw=1.8, ls="--", label="catalyzed")
ax1.annotate("", xy=(0.3, 100), xytext=(0.3, 0), arrowprops=dict(arrowstyle="<->", color="C0"))
ax1.annotate(r"$E_\mathrm{a}$", (0.31, 45), color="C0", fontsize=11)
ax1.annotate("", xy=(0.7, 100), xytext=(0.7, -40), arrowprops=dict(arrowstyle="<->", color="C0"))
ax1.annotate(r"$E_\mathrm{a}'$", (0.71, 30), color="C0", fontsize=11)
ax1.annotate("", xy=(0.93, 0), xytext=(0.93, -40), arrowprops=dict(arrowstyle="<->", color="C3"))
ax1.annotate(r"$\Delta_\mathrm{r}H_\mathrm{m}$", (0.80, -25), color="C3", fontsize=10)
ax1.axhline(0, color="0.6", lw=0.6, ls=":")
ax1.axhline(-40, color="0.6", lw=0.6, ls=":")
ax1.annotate("transition state", (0.5, 104), ha="center", fontsize=9)
ax1.annotate("reactants", (0.02, 6), fontsize=9)
ax1.annotate("products", (0.86, -34), fontsize=9)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_xlabel("reaction coordinate")
ax1.set_ylabel("potential energy")
ax1.set_ylim(-60, 125)
ax1.legend(frameon=False, fontsize=9, loc="upper right")
ax1.set_title("one elementary step", fontsize=10)

y2 = profile(x, [0, 0, 70, 25, 95, -30, -30], [0, 0.08, 0.28, 0.47, 0.68, 0.9, 1.0])
ax2.plot(x, y2, color="C0", lw=1.8)
ax2.plot([0.28, 0.68], [70, 95], "o", color="C3", ms=5)
ax2.plot([0.47], [25], "s", color="C2", ms=5)
ax2.annotate("TS 1", (0.28, 75), ha="center", fontsize=9, color="C3")
ax2.annotate("TS 2 (highest)", (0.68, 100), ha="center", fontsize=9, color="C3")
ax2.annotate("intermediate", (0.47, 14), ha="center", fontsize=9, color="C2")
ax2.annotate("reactants", (0.0, 6), fontsize=9)
ax2.annotate("products", (0.86, -24), fontsize=9)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_xlabel("reaction coordinate")
ax2.set_ylim(-60, 125)
ax2.set_title("two steps: the second is rate-determining", fontsize=10)
fig.tight_layout()
