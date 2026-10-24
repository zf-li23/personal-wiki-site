"""Why HBr adds to propene with Markovnikov regiochemistry: protonation at C1 gives the secondary
2-propyl cation through a lower transition state (Hammond postulate: the endothermic protonation
step has a late, cation-like transition state) than protonation at C2, which would give the primary
1-propyl cation. Schematic free-energy profile; the energy scale is qualitative."""

import numpy as np
import matplotlib.pyplot as plt


def path(x0, x1, y0, y1):
    x = np.linspace(x0, x1, 60)
    return x, y0 + (y1 - y0) * (1 - np.cos(np.pi * (x - x0) / (x1 - x0))) / 2


fig, ax = plt.subplots(figsize=(6.4, 4.0))
start, prod = 0.0, -8.0
for (ts1, cat, ts2, p), color, lab in (((10, 7, 8, -6), "C3", "via primary cation (minor)"),
                                       ((6.0, 2.5, 3.2, -8.5), "C0", "via secondary cation (major)")):
    segs = [path(0, 1, start, ts1), path(1, 2, ts1, cat), path(2, 2.6, cat, ts2), path(2.6, 3.6, ts2, p)]
    ax.plot(np.concatenate([s[0] for s in segs]), np.concatenate([s[1] for s in segs]), color=color, lw=2, label=lab)
ax.hlines(start, -0.5, 0, color="0.3", lw=2)
ax.text(-0.25, 0.6, "propene\n+ HBr", ha="center", va="bottom", fontsize=9)
ax.text(2.0, 4.4, r"CH$_3$CH$_2$CH$_2^+$", ha="center", fontsize=9, color="C3")
ax.text(2.0, -0.6, r"(CH$_3$)$_2$CH$^+$", ha="center", fontsize=9, color="C0")
ax.text(3.75, -6.0, "1-bromopropane", fontsize=9, va="center", color="C3")
ax.text(3.75, -8.9, "2-bromopropane", fontsize=9, va="center", color="C0")
ax.set_xlim(-0.7, 5.6)
ax.set_ylim(-11, 13)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel("reaction coordinate")
ax.set_ylabel("$G$ (schematic)")
ax.legend(loc="upper right", frameon=False, fontsize=9)
