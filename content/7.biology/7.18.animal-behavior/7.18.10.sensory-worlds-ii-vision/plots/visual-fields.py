# Horizontal visual fields seen from above (approximate values, eyes at rest; Hughes 1977, Martin 1984,
# Wynne and Udell 2020). Binocular field (seen by both eyes), monocular fields and the blind sector.
# Human 200 deg total / 120 deg binocular; tawny owl 201 / 48; pigeon 340 / 35;
# rabbit 360 / 24 in front and about 9 deg of overlap behind the head.
import numpy as np
from matplotlib.patches import Wedge, Circle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 8.2)
SPECIES = [("Human", "phylopic/human", 200, 120, 0, "Predator / omnivore"),
           ("Tawny owl", "phylopic/owl", 201, 48, 0, "Nocturnal predator"),
           ("Pigeon", "phylopic/pigeon", 340, 35, 0, "Ground-feeding prey"),
           ("Rabbit", "phylopic/rabbit", 360, 24, 9, "Grazing prey")]
R = 2.3
for k, (name, icon, total, bino, rear, eco) in enumerate(SPECIES):
    cx, cy = 3.0 + 6.0 * k, 4.3
    front = 90.0                       # straight ahead points up
    half = total / 2
    # monocular field (both sides together), binocular in front, blind sector behind
    ax.add_patch(Wedge((cx, cy), R, front - half, front + half, facecolor=P.fill("channel"),
                       edgecolor=P.edge("channel"), lw=0.8, zorder=3))
    ax.add_patch(Wedge((cx, cy), R, front - bino / 2, front + bino / 2, facecolor=P.fill("highlight"),
                       edgecolor=P.edge("highlight"), lw=0.8, zorder=4))
    if total < 360:
        ax.add_patch(Wedge((cx, cy), R, front + half, front + 360 - half, facecolor=P.fill("neutral"),
                           edgecolor=P.edge("neutral"), lw=0.8, zorder=3))
    if rear:
        ax.add_patch(Wedge((cx, cy), R, 270 - rear / 2, 270 + rear / 2, facecolor=P.fill("highlight"),
                           edgecolor=P.edge("highlight"), lw=0.8, zorder=4))
    ax.add_patch(Circle((cx, cy), 0.42, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.9, zorder=6))
    ax.plot([cx, cx], [cy + 0.42, cy + 0.62], color=P.edge("animal"), lw=1.4, zorder=6)
    bio.label(ax, (cx, cy + R + 0.45), f"{name}", size="small", bold=True)
    bio.label(ax, (cx, 1.25), f"total {total}°, binocular {bino}°" + (f" (+{rear}° behind)" if rear else ""),
              size="tiny")
    bio.label(ax, (cx, 0.75), eco, size="tiny", color=P.muted())
    bio.icon(ax, icon, at=(cx + 2.2, cy + R + 0.2), height=0.8, color="animal")

y = 7.85
for i, (tok, txt) in enumerate((("highlight", "binocular"), ("channel", "monocular"), ("neutral", "blind"))):
    x = 7.0 + 3.6 * i
    ax.add_patch(Wedge((x, y - 0.1), 0.3, 60, 120, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8))
    bio.label(ax, (x + 0.45, y), txt, size="tiny", ha="left")
bio.label(ax, (1.0, y), "Ahead is up", size="tiny", ha="left", color=P.muted())
