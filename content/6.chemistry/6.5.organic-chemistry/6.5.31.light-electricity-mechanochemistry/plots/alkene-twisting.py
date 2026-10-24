"""Schematic potential energy curves of an alkene (stilbene-like) along the twist angle about the
C=C bond. The ground state S0 has minima at 0 deg (Z) and 180 deg (E) and a barrier near 90 deg,
where the pi bond is broken. In the pi,pi* states S1 and T1 the pi bond order is zero, so the
excited molecule relaxes to the twisted geometry near 90 deg (the 'p' or phantom state), which lies
close to the S0 maximum: decay from there gives either isomer."""

import matplotlib.pyplot as plt
import numpy as np

phi = np.linspace(0, 180, 361)
rad = np.radians(phi)
s0 = 125 * np.sin(rad) ** 2 + 18 * (1 + np.cos(rad)) / 2  # Z (0 deg) a little above E (180 deg)
s1 = 400 - 70 * np.sin(rad) ** 2 + 10 * (1 + np.cos(rad)) / 2
t1 = 205 - 70 * np.sin(rad) ** 2 + 8 * (1 + np.cos(rad)) / 2

fig, ax = plt.subplots(figsize=(7.2, 4.8))
ax.plot(phi, s0, color="C0", lw=2, label=r"S$_0$")
ax.plot(phi, t1, color="C1", lw=2, ls="--", label=r"T$_1$ ($\pi,\pi^*$)")
ax.plot(phi, s1, color="C3", lw=2, label=r"S$_1$ ($\pi,\pi^*$)")
arrow = dict(arrowstyle="-|>", lw=1.3)
ax.annotate("", (0, 405), (0, 20), arrowprops=dict(color="C4", **arrow))
ax.annotate("", (180, 395), (180, 2), arrowprops=dict(color="C4", **arrow))
ax.text(4, 260, r"$h\nu$", color="C4")
ax.text(168, 260, r"$h\nu$", color="C4", ha="right")
ax.annotate("", (60, 85), (90, 128), arrowprops=dict(color="0.4", connectionstyle="arc3,rad=0.2", **arrow))
ax.annotate("", (120, 85), (90, 128), arrowprops=dict(color="0.4", connectionstyle="arc3,rad=-0.2", **arrow))
ax.text(90, 305, "twisted (p) state", ha="center", fontsize=9)
ax.text(90, 55, "decay to Z or E", ha="center", fontsize=8, color="0.4")
ax.text(2, -30, "Z", ha="center", fontsize=11)
ax.text(178, -30, "E", ha="center", fontsize=11)
ax.set_xlim(-8, 188)
ax.set_ylim(-50, 440)
ax.set_xticks([0, 45, 90, 135, 180])
ax.set_xlabel("twist angle about C=C / deg")
ax.set_ylabel(r"energy / kJ mol$^{-1}$ (schematic)")
ax.legend(loc="center", fontsize=9, frameon=False, bbox_to_anchor=(0.5, 0.52), ncol=3)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
fig.tight_layout()
