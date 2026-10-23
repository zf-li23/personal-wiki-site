"""Stability diagram of the Mathieu equation u'' + (a - 2q cos 2x) u = 0 for a linear quadrupole:
an ion passes when both the x motion (a, q) and the y motion (-a, -q) are stable. The first
(overlap) stability region with its apex at q = 0.706, a = 0.237; operating lines a = 2(U/V) q
for two U/V ratios; on a line, ions of larger m/z sit closer to the origin (a and q scale as 1/m)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import mathieu_a, mathieu_b

# Characteristic values: x is stable for a0(q) < a < b1(q); y (a -> -a) for -b1(q) < a < -a0(q).
# For a >= 0 the overlap is bounded by a < -a0(q) and a < b1(q).
q = np.linspace(0.0, 0.908, 600)
upper = np.minimum(-mathieu_a(0, q), mathieu_b(1, q))
upper = np.clip(upper, 0, None)

fig, ax = plt.subplots(figsize=(6.2, 4.2))
ax.fill_between(q, 0, upper, color="C0", alpha=0.35, lw=0)
ax.plot(q, upper, color="C0", lw=1.2)
ax.plot([0.706], [0.237], "o", color="k", ms=4)
ax.annotate("apex (0.706, 0.237)", xy=(0.706, 0.237), xytext=(0.74, 0.27), fontsize=8,
            arrowprops=dict(arrowstyle="-", lw=0.6))
for ratio, color, label in [(0.160, "C3", "high resolution, $U/V = 0.160$"), (0.120, "C1", "low resolution, $U/V = 0.120$")]:
    qq = np.linspace(0, 1.0, 50)
    ax.plot(qq, 2 * ratio * qq, color=color, lw=1.3, label=label)
ax.annotate("", xy=(0.30, 0.07), xytext=(0.55, 0.118), arrowprops=dict(arrowstyle="->", lw=0.8))
ax.text(0.40, 0.065, "larger $m/z$", fontsize=8, rotation=12)
ax.text(0.62, 0.06, "stable\nin x and y", fontsize=8, color="C0", ha="center")
ax.text(0.92, 0.012, r"$q_x = 0.908$", fontsize=8, ha="center")
ax.set_xlim(0, 1.0)
ax.set_ylim(0, 0.3)
ax.set_xlabel(r"$q = 4zeV/(m r_0^2 \Omega^2)$")
ax.set_ylabel(r"$a = 8zeU/(m r_0^2 \Omega^2)$")
ax.legend(fontsize=8, frameon=False, loc="upper left")
fig.tight_layout()
