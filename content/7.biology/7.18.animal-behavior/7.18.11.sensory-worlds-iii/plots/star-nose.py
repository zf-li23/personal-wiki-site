# The tactile fovea of the star-nosed mole (Condylura cristata). A: the 22 appendages around the nostrils,
# numbered 1-11 on each side; the two ventral appendages 11 lie just above the mouth. B: the share of the
# two appendages 11 in the star: of the appendages (2 of 22), of the Eimer's organs (about 7 %), of the
# afferent nerve fibers (about 11 %) and of the somatosensory cortex representing the star (about 25 %)
# (Catania and Kaas 1995, 1997).
import numpy as np
from matplotlib.patches import Ellipse, Circle
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(21, 9.6)
cx, cy = 4.8, 5.0
# appendage k (1..11) on each side, from dorsal (k=1, top) to ventral (k=11, bottom); 11 is short
for side in (1, -1):
    for k in range(1, 12):
        ang = np.deg2rad(90 - side * (6 + (k - 1) * 16.6))
        length = 2.0 if k < 11 else 1.2
        width = 0.42 if k < 11 else 0.4
        r0 = 1.12 + length / 2
        x, y = cx + r0 * np.cos(ang), cy + r0 * np.sin(ang)
        tok = "receptor" if k == 11 else "animal"
        ax.add_patch(Ellipse((x, y), length, width, angle=np.rad2deg(ang), facecolor=P.fill(tok),
                             edgecolor=P.edge(tok), lw=0.8, zorder=3))
        if side == 1:
            rt = 1.12 + length + 0.32
            bio.label(ax, (cx + rt * np.cos(ang), cy + rt * np.sin(ang)), str(k), size="tiny")
ax.add_patch(Circle((cx, cy), 1.05, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.9, zorder=4))
for dx in (-0.35, 0.35):
    ax.add_patch(Ellipse((cx + dx, cy), 0.35, 0.55, facecolor=P.ink(), zorder=5))
bio.label(ax, (cx, cy - 3.6), "mouth", size="tiny", color=P.muted())
bio.callout(ax, (cx + 0.24, cy - 1.7), (cx + 2.8, cy - 3.6), "appendage 11 (tactile fovea)", size="tiny")
bio.label(ax, (cx, 9.2), "A  The star (front view)", size="small", bold=True)

p = quant.Plot(ax, (12.4, 1.8, 7.6, 6.2), xlim=(0, 4), ylim=(0, 30), ylabel="Share of the two appendages 11 / %",
               xticks=[(0.5, "appendages"), (1.5, "Eimer's\norgans"), (2.5, "afferent\nfibers"), (3.5, "cortex")],
               yticks=[0, 10, 20, 30])
for i, (v, tok) in enumerate(((100 * 2 / 22, "neutral"), (7, "animal"), (11, "highlight"), (25, "receptor"))):
    p.bars([i + 0.15, i + 0.85], [v], tok)
    p.text(i + 0.5, v + 1.4, f"{v:.0f} %")
bio.label(ax, (16.2, 9.2), "B  Magnification of appendage 11", size="small", bold=True)
