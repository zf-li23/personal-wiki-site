"""Stages in the evolution of a camera eye (Section 32.3.2), each found in living animals (after the
sequence used by Nilsson and Pelger 1994 and Futuyma and Kirkpatrick 2017, Fig. 20.8). Cross sections:
photoreceptor cells (orange) backed by a layer of dark pigment; the cup deepens, giving information on
the direction of light; its aperture narrows to a pinhole, giving a crude image; a lens of graded
refractive index fills the cup and focuses the image, and an iris regulates the aperture. Each step
improves vision, and every stage is useful to its possessor."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import wikibio as bio

P = bio.P
FT = bio.core.FONT
fig, ax = plt.subplots(figsize=(10.8, 2.9))
fig.subplots_adjust(left=0.01, right=0.99, bottom=0.02, top=0.98)
ink, muted = P.ink(), P.muted()
STAGES = [("light-sensitive\npatch", 0.0, 1.0, False, False), ("shallow\ncup", 0.6, 1.0, False, False),
          ("deep cup", 1.3, 1.0, False, False), ("pinhole eye", 1.7, 0.35, False, False),
          ("lens eye", 1.7, 0.45, True, False), ("lens and\niris", 1.7, 0.45, True, True)]
for k, (name, depth, aper, lens, iris) in enumerate(STAGES):
    cx = 1.0 + 2.1 * k
    if depth == 0:
        xs = np.linspace(cx - 0.8, cx + 0.8, 50)
        ax.fill_between(xs, 1.35, 1.55, color=P.fill("rna"), ec=P.edge("rna"), lw=0.8)
        ax.fill_between(xs, 1.15, 1.35, color=P.ink(), lw=0)
    else:
        # cup as part of a circle; angle range set by aperture
        R = 0.85
        half = np.pi * (1 - 0.45 * aper)
        th = np.linspace(np.pi / 2 - half, np.pi / 2 + half, 80) + np.pi
        scale_y = depth / 1.7
        cy = 1.55
        xo, yo = cx + R * np.cos(th), cy + 0.2 + R * scale_y * np.sin(th) * 1.0
        xi, yi = cx + (R - 0.18) * np.cos(th), cy + 0.2 + (R - 0.18) * scale_y * np.sin(th)
        xp, yp = cx + (R + 0.14) * np.cos(th), cy + 0.2 + (R + 0.14) * scale_y * np.sin(th)
        ax.fill(np.r_[xo, xi[::-1]], np.r_[yo, yi[::-1]], color=P.fill("rna"), ec=P.edge("rna"), lw=0.8)
        ax.fill(np.r_[xp, xo[::-1]], np.r_[yp, yo[::-1]], color=P.ink(), lw=0)
        if lens:
            ax.add_patch(Ellipse((cx, cy + 0.2 - 0.25 * scale_y), 0.9, 0.9 * scale_y + 0.15, fc=P.fill("protein"), ec=P.edge("protein"), lw=0.9))
        if iris:
            for sgn in (-1, 1):
                ax.plot([cx + sgn * 0.55, cx + sgn * 0.3], [cy + 0.45, cy + 0.45], color=P.edge("dna"), lw=3.2, solid_capstyle="butt")
    for dx in (-0.35, 0, 0.35):
        ax.annotate("", xy=(cx + dx * 0.6, 1.7), xytext=(cx + dx, 2.55), arrowprops=dict(arrowstyle="-|>", color=P.edge("highlight"), lw=0.9))
    ax.text(cx, 0.35, name, ha="center", va="center", fontsize=FT["small"], color=ink)
    ax.text(cx, -0.2, str(k + 1), ha="center", fontsize=FT["tiny"], color=muted, weight="bold")
    if k < len(STAGES) - 1:
        ax.annotate("", xy=(cx + 1.25, 1.1), xytext=(cx + 0.9, 1.1), arrowprops=dict(arrowstyle="-|>", color=muted, lw=1.0))
ax.text(1.0, 2.75, "light", fontsize=FT["tiny"], color=P.edge("highlight"), ha="center")
ax.set_xlim(-0.1, 12.5)
ax.set_ylim(-0.45, 2.95)
ax.set_aspect("equal")
ax.axis("off")
