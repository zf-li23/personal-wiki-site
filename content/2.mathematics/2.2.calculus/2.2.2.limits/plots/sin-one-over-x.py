"""sin(1/x) oscillates without a limit at 0, while x sin(1/x) is squeezed to 0 by -|x| and |x|."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-0.4, 0.4, 20001)
x = x[x != 0]
fig, axes = plt.subplots(1, 2, figsize=(11, 3.9))

ax = axes[0]
ax.plot(x, np.sin(1 / x), color="C0", lw=0.7)
n = np.arange(1, 8)
ax.plot(1 / (2 * n * np.pi), np.zeros_like(n, dtype=float), "o", color="C1", ms=4, label="$x_n = 1/(2n\\pi)$")
ax.plot(1 / (2 * n * np.pi + np.pi / 2), np.ones_like(n, dtype=float), "o", color="C3", ms=4,
        label="$y_n = 1/(2n\\pi + \\pi/2)$")
ax.set_title("$\\sin(1/x)$: two sequences, two different limits", fontsize=11)
ax.set_ylim(-1.3, 1.6)
ax.legend(loc="upper left", fontsize=9)

ax = axes[1]
ax.plot(x, x * np.sin(1 / x), color="C0", lw=0.8, label="$x \\sin(1/x)$")
ax.plot(x, np.abs(x), color="C1", lw=1, ls="--", label="$\\pm |x|$")
ax.plot(x, -np.abs(x), color="C1", lw=1, ls="--")
ax.set_title("$x \\sin(1/x) \\to 0$ by the squeeze theorem", fontsize=11)
ax.set_ylim(-0.45, 0.45)
ax.legend(loc="upper center", fontsize=9)

for ax in axes:
    ax.axhline(0, color="0.8", lw=0.8)
    ax.axvline(0, color="0.8", lw=0.8)
    ax.set_xlabel("$x$")
fig.tight_layout()
