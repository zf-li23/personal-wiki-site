"""For a fixed epsilon, sin x admits one delta everywhere, while 1/x needs ever smaller delta near 0."""

import numpy as np
import matplotlib.pyplot as plt

eps = 0.5
fig, axes = plt.subplots(1, 2, figsize=(11, 4.2))

ax = axes[0]
x = np.linspace(0, 2 * np.pi, 400)
ax.plot(x, np.sin(x), color="C0", lw=2, label="$\\sin x$")
delta = eps  # |sin u - sin v| <= |u - v|
for x0 in (0.3, 1.6, 3.1, 4.7):
    ax.add_patch(plt.Rectangle((x0 - delta / 2, np.sin(x0) - eps / 2), delta, eps,
                               fill=True, alpha=0.25, color="C1"))
ax.set_title(f"$\\sin x$: one width $\\delta = {delta}$ works everywhere ($\\varepsilon = {eps}$)", fontsize=10)
ax.legend(loc="upper right", fontsize=9)

ax = axes[1]
x = np.linspace(0.12, 3.6, 400)
ax.plot(x, 1 / x, color="C0", lw=2, label="$1/x$")
# largest window [x0 - d/2, x0 + d/2] on which 1/x varies by less than eps
for x0 in (0.35, 0.6, 1.1, 2.2):
    # solve 1/(x0 - d/2) - 1/(x0 + d/2) = eps for d
    d = 2 * (np.sqrt(1 + eps ** 2 * x0 ** 2) - 1) / eps
    top, bottom = 1 / (x0 - d / 2), 1 / (x0 + d / 2)
    ax.add_patch(plt.Rectangle((x0 - d / 2, bottom), d, top - bottom, alpha=0.3, color="C1"))
    ax.annotate(f"$\\delta \\approx {d:.2f}$", (x0, top), xytext=(4, 6),
                textcoords="offset points", fontsize=9)
ax.set_ylim(0, 6)
ax.set_title(f"$1/x$ on $(0, +\\infty)$: the admissible $\\delta$ shrinks to 0 ($\\varepsilon = {eps}$)", fontsize=10)
ax.legend(loc="upper right", fontsize=9)

for ax in axes:
    ax.axhline(0, color="0.8", lw=0.8)
fig.tight_layout()
