"""Newman projections behind the two exceptions of section 4.2.4. Left and middle: 1,2-difluoroethane.
In the gauche conformer each C-F bond is antiperiplanar to a C-H bond on the other carbon (two
sigma(C-H) -> sigma*(C-F) donations, highlighted); in the anti conformer C-F is anti to C-F and C-H
to C-H, which are poorer donor-acceptor pairs. Right: gauche ethane-1,2-diol, where the two OH groups
are close enough for an intramolecular O-H...O hydrogen bond (dotted)."""

import numpy as np
import matplotlib.pyplot as plt

C1, C2 = "#2563eb", "#d97706"
ink = plt.rcParams["text.color"]


def newman(ax, x0, front, back, title):
    """front/back: lists of (angle in degrees, label, highlight colour or None)."""
    ax.add_patch(plt.Circle((x0, 0), 1, fill=None, color=ink, lw=1.4))
    for ang, name, hl in front:
        t = np.radians(ang)
        ax.plot([x0, x0 + 1.6 * np.cos(t)], [0, 1.6 * np.sin(t)], color=hl or ink, lw=2.4 if hl else 1.4)
        ax.text(x0 + 2.0 * np.cos(t), 2.0 * np.sin(t), name, ha="center", va="center", fontsize=11, color=hl or ink)
    for ang, name, hl in back:
        t = np.radians(ang)
        ax.plot([x0 + np.cos(t), x0 + 1.6 * np.cos(t)], [np.sin(t), 1.6 * np.sin(t)], color=hl or ink, lw=2.4 if hl else 1.4)
        ax.text(x0 + 2.0 * np.cos(t), 2.0 * np.sin(t), name, ha="center", va="center", fontsize=11, color=hl or ink)
    ax.text(x0, -2.8, title, ha="center", fontsize=10)


fig, ax = plt.subplots(figsize=(11, 4.0))
# gauche F/F: front F at 90, back F at 150 (60 degrees apart); highlight the two C-H/C-F anti pairs
newman(ax, 0, [(90, "F", C1), (210, "H", None), (330, "H", C2)],
       [(30, "H", None), (150, "F", C2), (270, "H", C1)], "gauche: two $\\sigma_{\\mathrm{CH}}\\to\\sigma^*_{\\mathrm{CF}}$ (more stable)")
newman(ax, 6, [(90, "F", None), (210, "H", None), (330, "H", None)],
       [(30, "H", None), (150, "H", None), (270, "F", None)], "anti: F anti to F, H anti to H")
newman(ax, 12, [(90, "OH", None), (210, "H", None), (330, "H", None)],
       [(30, "H", None), (150, "OH", None), (270, "H", None)], "gauche ethane-1,2-diol")
# hydrogen bond between the two OH groups (front OH at 90, rear OH at 150)
a = np.array([12 - 0.3, 1.9])
b = np.array([12 - 1.4, 1.3])
ax.plot(*zip(a, b), color=ink, lw=1.4, ls=(0, (1, 2.5)))
ax.text(3.0, 2.6, "1,2-difluoroethane", ha="center", fontsize=10, color="0.45")
ax.set_aspect("equal")
ax.set_xlim(-2.8, 14.8)
ax.set_ylim(-3.2, 2.9)
ax.axis("off")
