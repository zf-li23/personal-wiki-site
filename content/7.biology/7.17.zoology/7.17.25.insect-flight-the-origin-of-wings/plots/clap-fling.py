# The clap-and-fling (Weis-Fogh mechanism), schematic: wing sections (chords) seen from the side, leading
# edge marked by a dot, at the top of the stroke. 1-2 clap: the wings approach dorsally, the leading edges
# meet first and the closing gap pushes air out backwards (jet), adding thrust. 3-4 fling: the wings
# rotate apart about their trailing edges; air rushes into the opening gap, and each wing starts the
# downstroke with a bound circulation already established (circular arrows, opposite in sign), so lift
# develops at once without waiting for the slow build-up of circulation (Wagner effect). The
# circulations of the two wings cancel, so Kelvin's theorem is not violated. Used by small insects
# (Encarsia, thrips) and, partially, by butterflies and Drosophila in tethered flight.
import numpy as np
import wikibio as bio
from matplotlib.patches import FancyArrowPatch, Arc

P = bio.P
fig, ax = bio.canvas(26, 8.6)
pos = [(3.0, "1  Clap begins"), (9.5, "2  Clap: air expelled"), (16.0, "3  Fling: wings open"), (22.5, "4  Downstroke with circulation")]
cfg = [  # (angle of each chord from vertical, gap at trailing edge)
    dict(le=(0.45, 6.6), te=(1.0, 3.4)),
    dict(le=(0.06, 6.6), te=(0.06, 3.4)),
    dict(le=(1.1, 6.4), te=(0.06, 3.4)),
    dict(le=(2.3, 5.6), te=(1.2, 3.0)),
]
for (x, title), c in zip(pos, cfg):
    bio.label(ax, (x, 8.2), title, size="small", bold=True)
    for s in (-1, 1):
        le = (x + s * c["le"][0], c["le"][1])
        te = (x + s * c["te"][0], c["te"][1])
        ax.plot([le[0], te[0]], [le[1], te[1]], color=P.edge("er"), lw=4, solid_capstyle="round", zorder=5)
        ax.add_patch(__import__("matplotlib").patches.Circle(le, 0.16, color=P.ink(), zorder=6))
    if title.startswith("2"):
        bio.arrow(ax, (x, 3.2), (x, 1.4), kind="process", color=P.edge("channel"))
        bio.label(ax, (x + 0.3, 2.2), "jet", size="tiny", ha="left")
    if title.startswith("3"):
        for s in (-1, 1):
            bio.arrow(ax, (x + s * 2.2, 7.4), (x + s * 0.5, 6.0), kind="process", color=P.edge("channel"))
        bio.label(ax, (x, 7.5), "inflow", size="tiny")
    if title.startswith("4") or title.startswith("3"):
        r = 0.75 if title.startswith("4") else 0.55
        for s in (-1, 1):
            cx = x + s * (c["le"][0] + c["te"][0]) / 2
            cy = (c["le"][1] + c["te"][1]) / 2 + 0.1
            ax.add_patch(Arc((cx, cy), 2 * r + 0.9, 2 * r + 0.9, theta1=30, theta2=320, color=P.edge("negative"), lw=1.4, zorder=7))
            ang = np.deg2rad(320 if s > 0 else 30)
            bio.label(ax, (cx + s * 1.3, cy - 1.3), "+Γ" if s < 0 else "−Γ", size="small", color=P.edge("negative"))
bio.label(ax, (13.0, 0.5), "dot: leading edge; sections viewed along the wing span; schematic", size="tiny", color=P.muted())
