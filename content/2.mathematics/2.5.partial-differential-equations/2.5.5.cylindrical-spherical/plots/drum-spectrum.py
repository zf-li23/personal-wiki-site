"""Natural frequencies of a circular membrane compared with those of a string."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import jn_zeros

j01 = jn_zeros(0, 1)[0]
fig, ax = plt.subplots(figsize=(9, 3.4))

# String: omega_n / omega_1 = n
for n in range(1, 7):
    ax.vlines(n, 1.1, 1.9, color="C0", lw=2)
ax.text(0.15, 1.5, "string", va="center", fontsize=10)

# Membrane: omega_mk / omega_01 = j_mk / j_01
for m in range(0, 8):
    for j in jn_zeros(m, 4):
        q = j / j01
        if q <= 6.2:
            ax.vlines(q, 0.1, 0.9, color=f"C{1 + min(m, 5)}", lw=2)
ax.text(0.15, 0.5, "drum", va="center", fontsize=10)
for m in range(0, 6):
    ax.plot([], [], color=f"C{1 + m}", lw=2, label=f"m = {m}" if m < 5 else "m >= 5")

ax.set_xlim(0, 6.3)
ax.set_ylim(0, 2.4)
ax.set_yticks([])
ax.set_xlabel("frequency / fundamental frequency")
ax.set_title("String overtones are integer multiples; drum overtones are not")
ax.legend(loc="upper right", ncol=6, fontsize=8, frameon=False, bbox_to_anchor=(1.0, 1.0))
fig.tight_layout()
