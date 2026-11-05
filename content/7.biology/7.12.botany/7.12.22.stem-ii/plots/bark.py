# Bark formation. (A) Transverse section of a conifer trunk (template after a Wikimedia Commons diagram):
# secondary xylem with growth rings, vascular cambium, secondary phloem and bark. (B-D) Successive periderms
# in the outer part of a stem (transverse sections, outside at the top): (B) the first periderm forms
# below the epidermis; (C) a second periderm arises deeper, in the secondary phloem, and the tissues
# outside it die; (D) many overlapping, scale-like periderms cut off layers of dead phloem: everything
# outside the innermost periderm is rhytidome (outer bark); the living phloem inside it is the inner bark.
import numpy as np
from matplotlib.patches import Polygon

import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(33.0, 12.0)
bio.panel(ax, "A", (0.2, 11.8))
bio.label(ax, (0.85, 11.77), "Conifer trunk", size="title", ha="left", va="top")
PM.specimen(ax, "wikimedia/trunk-section-conifer", at=(4.6, 5.6), height=9.0,
            labels=[dict(part="bark", text="Bark", side="right"), dict(part="growth-ring", text="Growth rings", side="right")], right=9.6)

W = 5.6
xs = np.linspace(0, W, 120)


def band(x0, ybot, ytop, tok, z=3, dead=False):
    yb = np.broadcast_to(ybot, xs.shape)
    yt = np.broadcast_to(ytop, xs.shape)
    pts = np.vstack([np.c_[x0 + xs, yb], np.c_[x0 + xs, yt][::-1]])
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok) if not dead else P.mix(P.fill(tok), P.fill("animal"), 0.6),
                         edgecolor="none", zorder=z))


def cork(x0, ycurve, z=5):
    pts = np.vstack([np.c_[x0 + xs, ycurve], np.c_[x0 + xs, ycurve + 0.35][::-1]])
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill("cork"), edgecolor=P.edge("cork"), lw=0.8, zorder=z))
    ax.plot(x0 + xs, ycurve, color=P.edge("atp"), lw=1.6, zorder=z + 0.1)  # cork cambium


titles = ["First periderm", "Second periderm", "Rhytidome"]
for k in range(3):
    x0 = 12.4 + k * 7.0
    bio.panel(ax, "BCD"[k], (x0 - 0.4, 11.8))
    bio.label(ax, (x0 + W / 2, 11.3), titles[k], size="normal", bold=True)
    band(x0, 1.0, 2.0, "xylem")                                 # secondary xylem
    ax.plot(x0 + xs, np.full_like(xs, 2.0), color=P.edge("cambium"), lw=2.4, zorder=4)  # vascular cambium
    if k == 0:
        band(x0, 2.0, 5.5, "phloem")
        band(x0, 5.5, 8.4, "cytoplasm")
        band(x0, 8.4, 8.75, "cell_wall")
        cork(x0, np.full_like(xs, 8.0))
    elif k == 1:
        band(x0, 2.0, 5.5, "phloem")
        band(x0, 5.5, 8.4, "cytoplasm", dead=True)
        y2 = 4.0 + 0.6 * np.sin(xs / W * np.pi)
        band(x0, y2 + 0.35, 5.5, "phloem", dead=True, z=3.1)
        cork(x0, np.full_like(xs, 8.0))
        cork(x0, y2)
    else:
        band(x0, 2.0, 6.6, "phloem")
        band(x0, 6.6, 9.2, "phloem", dead=True)
        inner = 3.4 + 0.25 * np.sin(xs * 1.2)
        band(x0, inner + 0.35, 6.6, "phloem", dead=True, z=3.1)
        for c0, w0, h0 in ((1.4, 2.4, 6.2), (3.8, 2.6, 5.4), (2.5, 2.2, 4.4), (0.4, 1.8, 7.6), (4.6, 1.8, 7.2)):
            seg = (xs >= c0 - w0 / 2) & (xs <= c0 + w0 / 2)
            yc = h0 - 0.9 * np.cos((xs[seg] - c0) / (w0 / 2) * np.pi / 2)
            pts = np.vstack([np.c_[x0 + xs[seg], yc], np.c_[x0 + xs[seg], yc + 0.3][::-1]])
            ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill("cork"), edgecolor=P.edge("cork"), lw=0.8, zorder=5))
        cork(x0, inner)
        for yy, txt in ((7.4, "Rhytidome\n(outer bark)"), (2.7, "Inner bark")):
            bio.label(ax, (x0 + W + 0.25, yy), txt, size="small", ha="left")
        ax.plot([x0 + W + 0.15] * 2, [inner[-1] + 0.4, 9.2], color=P.muted(), lw=1.0)
        ax.plot([x0 + W + 0.15] * 2, [2.05, inner[-1]], color=P.muted(), lw=1.0)
    if k == 0:
        bio.callout(ax, (x0 + 0.6, 8.6), (x0 - 0.2, 10.4), "Epidermis", size="small")
        bio.callout(ax, (x0 + 1.6, 8.2), (x0 + 2.0, 10.4), "Periderm", size="small")
        bio.callout(ax, (x0 + 3.5, 7.0), (x0 + 4.4, 10.4), "Cortex", size="small")
        bio.callout(ax, (x0 + 3.0, 3.6), (x0 + 1.6, 0.3), "Secondary phloem", size="small")
        bio.callout(ax, (x0 + 4.6, 2.0), (x0 + 4.8, 0.3), "Vascular cambium", size="small")
    if k == 1:
        bio.callout(ax, (x0 + 2.8, 4.7), (x0 + 1.0, 10.4), "New periderm", size="small")
        bio.callout(ax, (x0 + 4.0, 7.0), (x0 + 4.0, 10.4), "Dead tissues", size="small")
