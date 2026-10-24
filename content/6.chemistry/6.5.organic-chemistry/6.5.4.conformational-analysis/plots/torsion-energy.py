"""Torsional potential energy of ethane and butane about the central C-C bond, with Newman
projections of the extreme conformations. Butane: a three-term Fourier series through the
textbook energies (anti 0, gauche 3.8, eclipsed 16, syn 19 kJ/mol); ethane: 12 kJ/mol barrier.
The torsion angle phi is 0 for the syn (fully eclipsed) conformation."""

import numpy as np
import matplotlib.pyplot as plt

ME = "#dc2626"


def newman(ax, cx, cy, w, h, front, back, phi):
    """Newman projection in a small inset centred at data point (cx, cy): front bonds meet at the
    centre, back bonds start at the circle. Labels run clockwise from 12 o'clock; phi rotates the back carbon."""
    ink = plt.rcParams["text.color"]
    sub = ax.inset_axes([cx - w / 2, cy - h / 2, w, h], transform=ax.transData)
    sub.set_xlim(-2.6, 2.6)
    sub.set_ylim(-2.6, 2.6)
    sub.set_aspect("equal")
    sub.axis("off")
    sub.patch.set_alpha(0)
    sub.add_patch(plt.Circle((0, 0), 1, fill=False, color=ink, lw=1.1))
    shift = 16 if phi % 120 == 0 else 0  # eclipsed back bonds drawn slightly offset so they stay visible
    for k, name in enumerate(front):
        t = np.radians(90 - 120 * k)
        sub.plot([0, 1.45 * np.cos(t)], [0, 1.45 * np.sin(t)], color=ink, lw=1.1)
        sub.text(1.85 * np.cos(t), 1.85 * np.sin(t), name, ha="center", va="center", fontsize=7, color=ME if name == "Me" else ink)
    for k, name in enumerate(back):
        t = np.radians(90 - 120 * k - phi - shift)
        sub.plot([np.cos(t), 1.6 * np.cos(t)], [np.sin(t), 1.6 * np.sin(t)], color=ink, lw=1.1)
        sub.text(2.15 * np.cos(t), 2.15 * np.sin(t), name, ha="center", va="center", fontsize=7, color=ME if name == "Me" else ink)


# Butane: V(phi) = a0 + a1 cos phi + a2 cos 2phi + a3 cos 3phi through four reference energies.
ref = {0: 19.0, 60: 3.8, 120: 16.0, 180: 0.0}
A = np.array([[1, np.cos(np.radians(p)), np.cos(np.radians(2 * p)), np.cos(np.radians(3 * p))] for p in ref])
coef = np.linalg.solve(A, np.array(list(ref.values())))
phi = np.linspace(-180, 180, 721)
rad = np.radians(phi)
butane = coef[0] + coef[1] * np.cos(rad) + coef[2] * np.cos(2 * rad) + coef[3] * np.cos(3 * rad)
ethane = 6.0 * (1 + np.cos(3 * rad))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.6), gridspec_kw={"width_ratios": [1, 1.6]})

ax1.plot(phi, ethane, color="C0", lw=2)
ax1.set_xlim(-180, 180)
ax1.set_ylim(-4, 22)
ax1.set_xticks(range(-180, 181, 60))
ax1.set_xlabel(r"H$-$C$-$C$-$H torsion angle $\varphi$ / $^\circ$")
ax1.set_ylabel(r"$E/(\mathrm{kJ\,mol^{-1}})$")
ax1.set_title("ethane", fontsize=11)
ax1.annotate("", xy=(0, 12), xytext=(0, 0), arrowprops=dict(arrowstyle="<->", color="0.5"))
ax1.text(6, 6, "12", fontsize=9, color="0.5")
H3 = ["H", "H", "H"]
newman(ax1, 0, 16.5, 80, 8, H3, H3, 0)
newman(ax1, 60, 4.0, 80, 8, H3, H3, 60)
ax1.text(0, 21.0, "eclipsed", ha="center", fontsize=8)
ax1.text(60, -2.6, "staggered", ha="center", fontsize=8)

ax2.plot(phi, butane, color="C1", lw=2)
ax2.set_xlim(-180, 180)
ax2.set_ylim(-3, 32)
ax2.set_xticks(range(-180, 181, 60))
ax2.set_xlabel(r"C1$-$C2$-$C3$-$C4 torsion angle $\varphi$ / $^\circ$")
ax2.set_title("butane", fontsize=11)
front = ["Me", "H", "H"]
cases = [  # (phi, label, y of drawing, y of label)
    (0, "syn (sp), 19", 25.5, 30.5),
    (60, "gauche (sc), 3.8", 9.5, 14.2),
    (120, "eclipsed (ac), 16", 24.0, 29.0),
    (180, r"anti (ap, $\varphi = 180^\circ$), 0", 24.0, 29.0),
]
for p, label, y, yl in cases:
    newman(ax2, p if p < 180 else -150, y, 70, 9, front, ["Me", "H", "H"], p)
    ax2.text(p if p < 180 else -150, yl, label, ha="center", fontsize=8)
fig.tight_layout()
