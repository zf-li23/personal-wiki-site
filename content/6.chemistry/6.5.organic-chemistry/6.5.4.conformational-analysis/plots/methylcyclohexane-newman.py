"""Newman projections of methylcyclohexane viewed along C1-C2. Equatorial CH3 is anti to C3 of the
ring; axial CH3 is gauche to C3 (like gauche butane), and the same holds along C1-C6: two gauche
butane interactions, i.e. the two 1,3-diaxial CH3/H contacts."""

import numpy as np
import matplotlib.pyplot as plt

ME, RING = "#dc2626", "#2563eb"


def newman(ax, x0, front, back, title):
    ink = plt.rcParams["text.color"]
    ax.add_patch(plt.Circle((x0, 0), 1, fill=False, color=ink, lw=1.4))
    for ang, name in front:
        t = np.radians(ang)
        ax.plot([x0, x0 + 1.6 * np.cos(t)], [0, 1.6 * np.sin(t)], color=ink, lw=1.4)
        col = ME if "CH" in name else RING if "C6" in name else ink
        ax.text(x0 + 2.05 * np.cos(t), 2.05 * np.sin(t), name, ha="center", va="center", fontsize=10, color=col)
    for ang, name in back:
        t = np.radians(ang)
        ax.plot([x0 + np.cos(t), x0 + 1.6 * np.cos(t)], [np.sin(t), 1.6 * np.sin(t)], color=ink, lw=1.4)
        col = RING if "C3" in name else ink
        ax.text(x0 + 2.05 * np.cos(t), 2.05 * np.sin(t), name, ha="center", va="center", fontsize=10, color=col)
    ax.text(x0, -2.75, title, ha="center", fontsize=10)


back = [(30, "C3"), (150, "H"), (270, "H")]
fig, ax = plt.subplots(figsize=(9, 3.9))
newman(ax, 0, [(90, "H"), (-30, "C6"), (210, "CH$_3$")], back, "equatorial CH$_3$: anti to C3")
newman(ax, 6, [(90, "CH$_3$"), (-30, "C6"), (210, "H")], back, "axial CH$_3$: gauche to C3")
ax.text(3, 2.6, "front carbon C1, rear carbon C2", ha="center", fontsize=9, color="0.45")
ax.set_aspect("equal")
ax.set_xlim(-3, 9)
ax.set_ylim(-3.1, 2.9)
ax.axis("off")
