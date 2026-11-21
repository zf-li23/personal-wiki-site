"""Two explanations for why insects circle a lamp.

A: light-compass reaction. The insect keeps the light at a fixed angle alpha to its heading.
With the sun (parallel rays) the path is straight; with a lamp a few meters away the bearing
changes as the insect moves, and keeping alpha fixed produces a logarithmic spiral
(alpha < 90 deg: inward, 90 deg: circle, > 90 deg: outward).
B: dorsal light response. The insect turns its back toward the brightest part of the visual
field; near a lamp the back faces the lamp, so the thrust (perpendicular to the back)
is tangential and the insect orbits, or it pitches up and stalls, or flips over when the
lamp is below it (the pattern found in 3-D tracking by Fabian et al. 2024).
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P


def spiral(alpha_deg, start=(-3.0, 0.4), v=0.02, n=4000):
    a = np.radians(alpha_deg)
    p = np.array(start, float)
    out = [p.copy()]
    for _ in range(n):
        to_light = -p / np.linalg.norm(p)
        # rotate the bearing to the light by alpha (light kept on the insect's left)
        c, s = np.cos(-a), np.sin(-a)
        h = np.array([c * to_light[0] - s * to_light[1], s * to_light[0] + c * to_light[1]])
        p = p + v * h
        out.append(p.copy())
        if np.linalg.norm(p) < 0.05 or np.linalg.norm(p) > 4.5:
            break
    return np.array(out)


fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.6))
cols = {60: P.edge("negative"), 85: P.edge("neuron"), 90: P.edge("dna"), 100: P.edge("positive")}
for alpha, col in cols.items():
    tr = spiral(alpha, n=945 if alpha == 90 else 4000)
    a.plot(tr[:, 0], tr[:, 1], color=col, lw=1.6, label=f"α = {alpha}°")
a.plot(0, 0, "*", ms=16, color=P.edge("highlight"))
a.text(0.12, -0.35, "lamp", fontsize=8, color=P.ink())
a.plot(-3.0, 0.4, "o", color=P.ink(), ms=4)
a.text(-3.1, 0.6, "start", fontsize=8, color=P.ink(), ha="right")
# parallel rays: straight path
for yy in (3.7, 3.3):
    a.annotate("", (-4.1, yy), (-2.9, yy), arrowprops=dict(arrowstyle="->", color=P.edge("highlight"), lw=0.8))
a.text(-2.8, 3.5, "sunlight (parallel rays):\nfixed angle = straight path", fontsize=7.5, color=P.muted(), va="center")
a.set_aspect("equal"); a.set_xlim(-4.2, 4.2); a.set_ylim(-4.0, 4.0)
a.set_xticks([]); a.set_yticks([])
a.legend(frameon=False, fontsize=8, loc="upper right")
a.set_title("A  Light-compass reaction near a lamp", loc="left", fontweight="bold", fontsize=10)
for s in ("top", "right", "left", "bottom"):
    a.spines[s].set_visible(False)

# panel B: dorsal light response
b.plot(0, 0, "*", ms=18, color=P.edge("highlight"))
b.add_patch(plt.Circle((0, 0), 1.6, fill=False, ls="--", color=P.muted(), lw=0.8))
for ang in np.radians(np.arange(0, 360, 45)):
    pos = 1.6 * np.array([np.cos(ang), np.sin(ang)])
    back = -pos / 1.6  # dorsal side faces the lamp
    body = np.array([-back[1], back[0]])  # long axis tangential
    e = plt.matplotlib.patches.Ellipse(pos, 0.55, 0.22, angle=np.degrees(np.arctan2(body[1], body[0])),
                                       facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=1)
    b.add_patch(e)
    b.annotate("", pos + 0.45 * back, pos, arrowprops=dict(arrowstyle="->", color=P.edge("rna"), lw=1.1))
    b.annotate("", pos + 0.55 * body, pos + 0.15 * body,
               arrowprops=dict(arrowstyle="-|>", color=P.edge("dna"), lw=1.2))
b.text(0, -2.45, "dorsal side turned to the light (orange); thrust along the body (blue)\n"
       "is tangential, so the insect orbits the lamp", fontsize=7.5, color=P.muted(), ha="center")
b.set_aspect("equal"); b.set_xlim(-2.8, 2.8); b.set_ylim(-2.9, 2.4)
b.set_xticks([]); b.set_yticks([])
for s in ("top", "right", "left", "bottom"):
    b.spines[s].set_visible(False)
b.set_title("B  Dorsal light response near a lamp", loc="left", fontweight="bold", fontsize=10)
fig.tight_layout()
