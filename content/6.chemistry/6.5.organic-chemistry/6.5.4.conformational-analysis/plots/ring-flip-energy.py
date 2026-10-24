"""Energy profile of the cyclohexane ring flip: chair -> half-chair (transition state) -> twist-boat
(intermediate) -> boat (transition state between twist-boats) -> twist-boat -> half-chair -> chair.
Relative energies (kJ/mol): chair 0, half-chair 45, twist-boat 23, boat 29."""

import numpy as np
import matplotlib.pyplot as plt

xs = [0, 1, 2, 3, 4, 5, 6]
es = [0, 45, 23, 29, 23, 45, 0]
names = ["chair", "half-chair", "twist-boat", "boat", "twist-boat", "half-chair", "chair (flipped)"]

fig, ax = plt.subplots(figsize=(8.5, 4.2))
for i in range(len(xs) - 1):
    t = np.linspace(0, 1, 60)
    s = (1 - np.cos(np.pi * t)) / 2  # smooth step: flat at both stationary points
    ax.plot(xs[i] + t, es[i] + (es[i + 1] - es[i]) * s, color="C0", lw=2)
for x, e, name in zip(xs, es, names):
    ax.text(x, e + 2.5, f"{name}\n{e}", ha="center", va="bottom", fontsize=9)
ax.annotate("", xy=(0.3, 45), xytext=(0.3, 0), arrowprops=dict(arrowstyle="<->", color="0.5"))
ax.text(0.38, 20, r"$\Delta G^{\ddagger} \approx 45$", fontsize=9, color="0.4")
ax.set_xlim(-0.5, 6.5)
ax.set_ylim(-5, 60)
ax.set_xticks([])
ax.set_xlabel("reaction coordinate of the ring flip")
ax.set_ylabel(r"$E/(\mathrm{kJ\,mol^{-1}})$")
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
fig.tight_layout()
