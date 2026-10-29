"""Closure of the mammalian neural tube and the defects that follow when it fails (schematic, dorsal view,
anterior up). (A) Closure starts at the hindbrain-cervical boundary (closure 1; about day 22 in humans) and
zips in both directions; further initiation sites at the forebrain-midbrain boundary (closure 2) and at the rostral
end of the forebrain (closure 3) close the head, leaving the hindbrain and anterior neuropores (closed about day 25)
and the posterior neuropore (about day 26-28). The sites were mapped in the mouse; their number in humans is debated.
(B) Where the tube stays open: failure of closure 1 leaves the tube open from the midbrain to the low spine
(craniorachischisis); failure in the head gives anencephaly; failure of the posterior neuropore gives open spina
bifida (myelomeningocele). Encephalocele and closed spina bifida are skin-covered defects of later development."""
import numpy as np
import wikibio as bio
from wikibio import neurodev as N

fig, ax = bio.canvas(20, 11.2)
P = bio.P
ne, ep = N.TISSUE["neural"], N.TISSUE["epidermis"]
cx = 4.0
y = np.linspace(0.8, 10.2, 200)
# half-width of the neural plate/tube along the body axis: broad head folds, narrow spinal region
hw = 0.42 + 1.25 * np.exp(-((y - 8.7) / 1.25) ** 2) + 0.15 * np.exp(-((y - 1.3) / 0.6) ** 2)
outline = np.vstack([np.c_[cx + hw, y], np.c_[cx - hw, y][::-1]])
bio.shape(ax, np.vstack([np.c_[cx + hw + 0.55, y], np.c_[cx - hw - 0.55, y][::-1]]), ep, lw=1.0, zorder=3)
bio.shape(ax, outline, ne, lw=1.1, zorder=4)
# open segments (neuropores) and closed seams between them
for y0, y1 in ((9.2, 9.85), (7.45, 8.6), (0.85, 2.0)):
    yy = np.linspace(y0, y1, 30)
    w = 0.2 * np.sin(np.pi * (yy - y0) / (y1 - y0))
    bio.shape(ax, np.vstack([np.c_[cx + w, yy], np.c_[cx - w, yy][::-1]]), "extracellular", lw=0.8, zorder=6)
for y0, y1 in ((2.0, 7.45), (8.6, 9.2), (9.85, 10.15)):
    ax.plot([cx, cx], [y0, y1], color=P.edge(ne), lw=2.6, zorder=6)
from matplotlib.patches import Circle
for yc, name in ((6.95, "1"), (8.9, "2"), (10.05, "3")):
    ax.add_patch(Circle((cx, yc), 0.24, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=1.0, zorder=8))
    bio.label(ax, (cx, yc), name, size="small", bold=True, color=P.on_fill(), zorder=9)
# zipping directions from each initiation site
for a, b in (((cx + 0.75, 6.7), (cx + 0.75, 2.6)), ((cx + 0.75, 7.15), (cx + 0.75, 7.75)), ((cx - 1.85, 8.75), (cx - 1.85, 8.05)),
             ((cx - 1.85, 9.05), (cx - 1.85, 9.45)), ((cx + 1.2, 10.0), (cx + 1.2, 9.6))):
    bio.arrow(ax, a, b, kind="process", head=0.15, lw=1.1)
bio.callout(ax, (cx + 0.12, 9.5), (cx + 2.4, 10.75), "Anterior neuropore (~day 25)")
bio.callout(ax, (cx + 0.12, 8.0), (cx + 2.4, 8.4), "Hindbrain neuropore")
bio.callout(ax, (cx + 0.12, 1.4), (cx + 2.4, 0.7), "Posterior neuropore (~day 26-28)")
bio.callout(ax, (cx + 0.24, 6.95), (cx + 2.4, 6.2), "Closure 1 (~day 22)")
bio.label(ax, (cx + 2.5, 5.65), "hindbrain-cervical boundary", size="tiny", ha="left", color=P.muted())
bio.callout(ax, (cx - 0.42, 4.5), (cx - 2.0, 4.5), "Spinal cord")
bio.label(ax, (cx - 2.1, 10.55), "head folds", size="tiny", color=P.muted())
bio.panel(ax, "A", (0.3, 10.9))

# (B) extent of the open tube in each defect along the same axis
bio.panel(ax, "B", (11.6, 11.1))
x0 = 13.2
regions = [(9.6, 10.2, "Forebrain"), (8.0, 9.6, "Mid-, hindbrain"), (2.0, 8.0, "Spinal cord"), (0.8, 2.0, "Lumbosacral")]
for y0, y1, name in regions:
    ax.plot([x0 - 0.15, x0 + 7.0], [y0, y0], color=P.muted(), lw=0.5, ls=":", zorder=2)
    bio.label(ax, (x0 - 0.25, (y0 + y1) / 2), name, size="tiny", ha="right", color=P.muted())
defects = [("Anencephaly", 8.0, 10.2, "negative"), ("Craniorachischisis", 1.5, 9.0, "negative"),
           ("Open spina bifida", 0.8, 2.4, "negative"), ("Encephalocele", 9.0, 9.5, "neutral"),
           ("Closed spina bifida", 0.9, 1.7, "neutral")]
for k, (name, y0, y1, tok) in enumerate(defects):
    xb = x0 + 0.5 + k * 1.4
    bio.box(ax, (xb, (y0 + y1) / 2), 0.45, y1 - y0, token=tok, radius=0.12)
    yl = (y0 + y1) / 2 if y1 - y0 > 2.5 else (y1 + 0.2 if y1 < 5 else y0 - 0.2)
    bio.label(ax, (xb + 0.42, yl), name, size="tiny", rotation=90, ha="center", va="center" if y1 - y0 > 2.5 else ("bottom" if y1 < 5 else "top"))
bio.label(ax, (x0 + 2.6, 10.3), "open (failed closure)", size="tiny", color=P.edge("negative"))
bio.label(ax, (x0 + 5.8, 10.3), "skin-covered (later defect)", size="tiny", color=P.muted())
