"""Birth times on a 24-hour clock, and how the Kolmogorov statistic depends on the origin."""

import numpy as np
import matplotlib.pyplot as plt

hours = np.array([1, 3, 4 + 20 / 60, 5, 5 + 40 / 60, 6 + 20 / 60, 6 + 40 / 60, 7,
                  9 + 40 / 60, 11, 12, 17 + 20 / 60])
n = len(hours)
k = np.arange(1, n + 1)


def one_sided(origin):
    u = np.sort(((hours - origin) % 24) / 24)
    return np.max(k / n - u), np.max(u - (k - 1) / n)


fig = plt.figure(figsize=(10, 4.4))
ax1 = fig.add_subplot(1, 2, 1, projection="polar")
theta = hours / 24 * 2 * np.pi
ax1.set_theta_zero_location("N")
ax1.set_theta_direction(-1)
ax1.scatter(theta, np.ones(n), s=50, color="C0", zorder=3)
ax1.set_ylim(0, 1.2)
ax1.set_yticks([])
ax1.set_xticks(np.arange(0, 24, 3) / 24 * 2 * np.pi)
ax1.set_xticklabels([f"{h}:00" for h in range(0, 24, 3)])
ax1.set_title("12 home births on a 24-hour clock")

ax2 = fig.add_subplot(1, 2, 2)
origins = np.linspace(0, 24, 961)
vals = np.array([one_sided(o) for o in origins])
ax2.plot(origins, vals[:, 0], color="C0", lw=1.2, label="D+ (empirical above uniform)")
ax2.plot(origins, vals[:, 1], color="C2", lw=1.2, label="D- (uniform above empirical)")
ax2.plot(origins, vals.max(axis=1), color="C3", lw=2.2, label="Kolmogorov D = max(D+, D-)")
ax2.plot(origins, vals.sum(axis=1), color="C1", lw=2.2, ls="--", label="Kuiper V = D+ + D-")
ax2.set_xlabel("origin of the clock (hour)")
ax2.set_ylabel("statistic")
ax2.set_xticks(range(0, 25, 3))
ax2.set_title("Only V is invariant under rotation")
ax2.legend(frameon=False, fontsize=8, loc="upper right")
ax2.set_ylim(0, 0.75)
ax2.grid(alpha=0.3)
fig.tight_layout()
