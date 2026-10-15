"""Graphs of the four inverse trigonometric functions with their ranges."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))

x = np.linspace(-1, 1, 400)
ax = axes[0]
ax.plot(x, np.arcsin(x), color="C0", lw=2, label="$\\arcsin x$")
ax.plot(x, np.arccos(x), color="C1", lw=2, label="$\\arccos x$")
for level in (-np.pi / 2, np.pi / 2, np.pi):
    ax.axhline(level, color="0.75", lw=0.8, ls="--")
ax.set_yticks([-np.pi / 2, 0, np.pi / 2, np.pi])
ax.set_yticklabels(["$-\\pi/2$", "0", "$\\pi/2$", "$\\pi$"])
ax.set_xlim(-1.6, 1.6)
ax.set_title("Domain $[-1, 1]$", fontsize=11)
ax.legend(loc="upper center", fontsize=9)

x = np.linspace(-8, 8, 600)
ax = axes[1]
ax.plot(x, np.arctan(x), color="C0", lw=2, label="$\\arctan x$")
ax.plot(x, np.pi / 2 - np.arctan(x), color="C1", lw=2, label="$\\mathrm{arccot}\\, x$")
for level in (-np.pi / 2, np.pi / 2, np.pi):
    ax.axhline(level, color="0.75", lw=0.8, ls="--")
ax.set_yticks([-np.pi / 2, 0, np.pi / 2, np.pi])
ax.set_yticklabels(["$-\\pi/2$", "0", "$\\pi/2$", "$\\pi$"])
ax.set_title("Domain $(-\\infty, +\\infty)$; dashed lines are asymptotes", fontsize=11)
ax.legend(loc="upper right", fontsize=9)

for ax in axes:
    ax.axhline(0, color="0.8", lw=0.8)
    ax.axvline(0, color="0.8", lw=0.8)
    ax.set_ylim(-2, 3.5)
fig.tight_layout()
