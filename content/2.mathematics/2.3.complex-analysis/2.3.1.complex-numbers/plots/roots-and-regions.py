"""Fourth roots of -16 and three typical point sets: a disc, an annulus, a slit plane."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 4, figsize=(15, 4))
t = np.linspace(0, 2 * np.pi, 400)

# Fourth roots of -16: 2 exp(i (pi/4 + k pi/2))
ax = axes[0]
ax.plot(2 * np.cos(t), 2 * np.sin(t), color="0.6", lw=1, ls="--")
roots = 2 * np.exp(1j * (np.pi / 4 + np.arange(4) * np.pi / 2))
ax.fill(roots.real, roots.imag, color="C0", alpha=0.15)
for k, w in enumerate(roots):
    ax.plot([0, w.real], [0, w.imag], color="C0", lw=1)
    ax.plot(w.real, w.imag, "o", color="C0")
    ax.text(1.18 * w.real, 1.18 * w.imag, f"w{k}", ha="center", va="center")
ax.set_title("z^4 = -16: a square on |z| = 2")

# Disc: simply connected
ax = axes[1]
ax.fill(np.cos(t), np.sin(t), color="C2", alpha=0.3, lw=0)
ax.plot(np.cos(t), np.sin(t), color="C2", ls="--", lw=1.2)
ax.set_title("disc |z| < 1: simply connected")

# Annulus: not simply connected
ax = axes[2]
ax.fill(np.r_[2 * np.cos(t), np.cos(t[::-1])], np.r_[2 * np.sin(t), np.sin(t[::-1])], color="C3", alpha=0.3, lw=0)
ax.plot(2 * np.cos(t), 2 * np.sin(t), color="C3", ls="--", lw=1.2)
ax.plot(np.cos(t), np.sin(t), color="C3", ls="--", lw=1.2)
ax.plot(1.5 * np.cos(t), 1.5 * np.sin(t), color="C1", lw=1.6)
ax.text(0, 0, "loop |z| = 1.5\ncannot shrink", ha="center", va="center", color="C1", fontsize=9)
ax.set_title("annulus 1 < |z| < 2: not simply connected")

# Slit plane: simply connected
ax = axes[3]
ax.fill([-2.2, 2.2, 2.2, -2.2], [-2.2, -2.2, 2.2, 2.2], color="C4", alpha=0.25, lw=0)
ax.plot([-2.2, 0], [0, 0], color="C4", lw=3)
ax.plot(0, 0, "o", color="C4", mfc="none", ms=8)
ax.text(-1.1, 0.18, "removed", ha="center", fontsize=9)
ax.set_title("plane minus (-inf, 0]: simply connected")

for ax in axes:
    ax.axhline(0, color="0.7", lw=0.6)
    ax.axvline(0, color="0.7", lw=0.6)
    ax.set_aspect("equal")
    ax.set_xlim(-2.3, 2.3)
    ax.set_ylim(-2.3, 2.3)
    ax.set_xlabel("Re z")
axes[0].set_ylabel("Im z")
fig.tight_layout()
