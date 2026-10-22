"""Radius-ratio rule: critical geometries for coordination numbers 6 and 8, and AX compounds placed by r+/r-."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig = plt.figure(figsize=(12, 4.4))
gs = fig.add_gridspec(1, 3, width_ratios=[1, 1.1, 1.6])

# CN 6: the plane through the cation and four of its six anions (a square).
ax = fig.add_subplot(gs[0])
rm = 1.0
rp = (np.sqrt(2) - 1) * rm
for x, y in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
    ax.add_patch(Circle((x * rm, y * rm), rm, facecolor="C2", alpha=0.35, edgecolor="C2", lw=1.2))
ax.add_patch(Circle((0, 0), rp, facecolor="C1", alpha=0.8, edgecolor="C1"))
ax.plot([-1, 1], [-1, -1], color="0.4", lw=0.9)
ax.plot([-1, 1], [-1, 1], color="0.4", lw=0.9, ls="--")
ax.text(0, -1.18, r"$2r_-$", ha="center", va="top", fontsize=10)
ax.text(0.55, 0.3, r"$2(r_+ + r_-)$", fontsize=10, rotation=45, ha="center")
ax.set_title("CN 6, critical contact\n" + r"$r_+/r_- = \sqrt{2}-1 = 0.414$", fontsize=10.5)

# CN 8: the diagonal plane of the cube (a rectangle a x a*sqrt(2)).
ax2 = fig.add_subplot(gs[1])
a = 2 * rm
rp8 = (np.sqrt(3) - 1) * rm
w = a * np.sqrt(2)
for x, y in [(-w / 2, -a / 2), (w / 2, -a / 2), (w / 2, a / 2), (-w / 2, a / 2)]:
    ax2.add_patch(Circle((x, y), rm, facecolor="C2", alpha=0.35, edgecolor="C2", lw=1.2))
ax2.add_patch(Circle((0, 0), rp8, facecolor="C1", alpha=0.8, edgecolor="C1"))
ax2.plot([-w / 2, -w / 2], [-a / 2, a / 2], color="0.4", lw=0.9)
ax2.plot([-w / 2, w / 2], [-a / 2, a / 2], color="0.4", lw=0.9, ls="--")
ax2.text(-w / 2 - 0.12, 0, r"$a = 2r_-$", ha="right", va="center", fontsize=10)
ax2.text(0.35, 0.55, r"$\sqrt{3}\,a = 2(r_+ + r_-)$", fontsize=10, ha="center")
ax2.set_title("CN 8, diagonal plane of the cube\n" + r"$r_+/r_- = \sqrt{3}-1 = 0.732$", fontsize=10.5)

for axx, lim in ((ax, 2.1), (ax2, 2.6)):
    axx.set_aspect("equal")
    axx.set_xlim(-lim, lim)
    axx.set_ylim(-2.1, 2.1)
    axx.axis("off")

# AX compounds by radius ratio (Shannon radii, cation radius for its actual coordination number).
ax3 = fig.add_subplot(gs[2])
data = [  # name, r+/r-, observed CN
    ("BeO", 27 / 140, 4), ("ZnS", 60 / 184, 4), ("CuCl", 60 / 181, 4), ("AgI", 100 / 220, 4),
    ("MgO", 72 / 140, 6), ("NaCl", 102 / 181, 6), ("AgCl", 115 / 181, 6), ("KCl", 138 / 181, 6),
    ("RbCl", 152 / 181, 6), ("CsCl", 174 / 181, 8), ("CsI", 174 / 220, 8),
]
bands = [(0.225, 0.414, 4, "C0"), (0.414, 0.732, 6, "C2"), (0.732, 1.0, 8, "C1")]
for lo, hi, cn, col in bands:
    ax3.axvspan(lo, hi, color=col, alpha=0.12)
    ax3.text((lo + hi) / 2, 9.1, f"predicted CN {cn}", ha="center", fontsize=9)
offsets = {"ZnS": 0.35, "CuCl": -0.45, "AgI": 0.35, "NaCl": 0.35, "AgCl": -0.45, "MgO": -0.45, "CsI": -0.45}
for name, q, cn in data:
    ok = any(lo <= q < hi and c == cn for lo, hi, c, _ in bands)
    ax3.plot(q, cn, "o" if ok else "X", color="C0" if ok else "C3", ms=8)
    ax3.text(q, cn + offsets.get(name, 0.35), name, ha="center", fontsize=8.5)
ax3.set_xlim(0.15, 1.02)
ax3.set_ylim(3, 9.6)
ax3.set_yticks([4, 6, 8])
ax3.set_xlabel(r"$r_+/r_-$")
ax3.set_ylabel("observed coordination number")
ax3.set_title("AX compounds: circles agree with the rule, crosses do not", fontsize=10.5)
fig.tight_layout()
