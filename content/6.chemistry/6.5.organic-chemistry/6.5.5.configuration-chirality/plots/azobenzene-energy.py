"""Schematic energy profile of azobenzene isomerization in the ground state. E (trans) is lower
than Z (cis) by about 50 kJ/mol; the thermal Z -> E barrier is about 95-100 kJ/mol, so the
thermal E -> Z barrier is about 145-150 kJ/mol. Light switches E -> Z (UV, pi-pi*) and Z -> E
(visible, n-pi*)."""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 400)
Ez, ts = 50.0, 147.0
y = np.where(x < 0.5, ts * np.sin(np.pi * x) ** 2, Ez + (ts - Ez) * np.sin(np.pi * x) ** 2)

fig, ax = plt.subplots(figsize=(7.5, 4))
ax.plot(x, y, color="C0", lw=2)
ax.text(0.0, -12, "(E)-azobenzene", ha="center", fontsize=10)
ax.text(1.0, Ez - 12, "(Z)-azobenzene", ha="center", fontsize=10)
ax.annotate("", xy=(0.92, 147), xytext=(0.92, Ez), arrowprops=dict(arrowstyle="<->", color="0.5"))
ax.text(0.95, 95, "about 97", fontsize=9, color="0.4")
ax.annotate("", xy=(1.08, Ez), xytext=(1.08, 0), arrowprops=dict(arrowstyle="<->", color="0.5"))
ax.text(1.1, 22, "about 50", fontsize=9, color="0.4")
ax.plot([1.0, 1.12], [Ez, Ez], color="0.6", lw=0.8)
ax.plot([0.0, 1.12], [0, 0], color="0.6", lw=0.8)
ax.annotate("", xy=(0.95, Ez + 4), xytext=(0.05, 4), arrowprops=dict(arrowstyle="-|>", color="#7c3aed", connectionstyle="arc3,rad=-0.35"))
ax.text(0.35, 60, r"$h\nu$ (UV, about 340 nm)", color="#7c3aed", fontsize=9)
ax.annotate("", xy=(0.06, 8), xytext=(0.94, Ez - 2), arrowprops=dict(arrowstyle="-|>", color="#0891b2", connectionstyle="arc3,rad=-0.3"))
ax.text(0.33, 14, r"$h\nu'$ (visible, about 440 nm) or heat", color="#0891b2", fontsize=9)
ax.set_xlim(-0.2, 1.35)
ax.set_ylim(-22, 165)
ax.set_xticks([])
ax.set_xlabel("C$-$N$=$N$-$C torsion / inversion coordinate")
ax.set_ylabel(r"$E/(\mathrm{kJ\,mol^{-1}})$")
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
fig.tight_layout()
