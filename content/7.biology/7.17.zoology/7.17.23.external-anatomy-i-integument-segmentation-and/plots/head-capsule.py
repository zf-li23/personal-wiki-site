# A: frontal view of a generalized orthopteroid head (schematic). The inverted-Y epicranial (ecdysial)
# suture divides the vertex from the frons; the frontoclypeal (epistomal) suture separates the frons
# from the clypeus, to which the labrum is hinged; the genae lie below the compound eyes, and the
# subgenal suture runs above the mandibular articulations. Three ocelli: a median ocellus on the frons and
# two lateral ocelli. B: head orientations defined by the direction of the mouthparts relative to the
# body axis: hypognathous (ventral; grasshoppers), prognathous (forward; ground beetles, earwigs, many
# larvae) and opisthognathous (backward; true bugs, cicadas, aphids).
import numpy as np
from matplotlib.patches import Ellipse, Circle
import wikibio as bio
from wikibio.core import smooth_closed

P = bio.P
fig, ax = bio.canvas(26, 12.5)
bio.panel(ax, "A", (0.2, 12.1))
bio.panel(ax, "B", (15.4, 12.1))
cx = 7.0
# capsule outline
cap = smooth_closed([(cx - 3.3, 6.2), (cx - 3.0, 9.2), (cx - 1.6, 11.0), (cx, 11.4), (cx + 1.6, 11.0), (cx + 3.0, 9.2),
                     (cx + 3.3, 6.2), (cx + 2.7, 4.0), (cx + 1.6, 3.2), (cx - 1.6, 3.2), (cx - 2.7, 4.0)])
bio.shape(ax, cap, "animal", lw=1.1, zorder=3)
# compound eyes
for s in (-1, 1):
    ax.add_patch(Ellipse((cx + s * 2.45, 8.1), 1.25, 2.2, angle=s * -12, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.9, zorder=5))
    ax.add_patch(Circle((cx + s * 1.25, 7.7), 0.28, facecolor="none", edgecolor=P.ink(), lw=0.9, zorder=6))  # antennal socket
    ax.plot([cx + s * 1.25, cx + s * 2.0], [7.7, 9.9], color=P.edge("channel"), lw=3.0, zorder=6, solid_capstyle="round")
    ax.add_patch(Circle((cx + s * 0.95, 8.95), 0.14, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.7, zorder=6))
ax.add_patch(Circle((cx, 7.3), 0.15, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.7, zorder=6))
ink = P.ink()
# epicranial suture: stem + arms
ax.plot([cx, cx], [11.35, 9.6], color=ink, lw=1.0, zorder=6)
ax.plot([cx, cx - 0.9, cx - 1.1], [9.6, 8.6, 7.9], color=ink, lw=1.0, zorder=6)
ax.plot([cx, cx + 0.9, cx + 1.1], [9.6, 8.6, 7.9], color=ink, lw=1.0, zorder=6)
# frontoclypeal suture
ax.plot([cx - 1.9, cx + 1.9], [5.3, 5.3], color=ink, lw=1.0, zorder=6)
# subgenal sutures
for s in (-1, 1):
    ax.plot([cx + s * 1.9, cx + s * 2.9], [5.3, 4.6], color=ink, lw=0.8, ls=(0, (3, 2)), zorder=6)
# clypeus and labrum
bio.shape(ax, [(cx - 1.9, 5.3), (cx + 1.9, 5.3), (cx + 1.6, 4.1), (cx - 1.6, 4.1)], "animal", lw=0.9, zorder=4)
lab = smooth_closed([(cx - 1.5, 4.1), (cx + 1.5, 4.1), (cx + 1.3, 3.1), (cx + 0.5, 2.5), (cx - 0.5, 2.5), (cx - 1.3, 3.1)])
bio.shape(ax, lab, "labrum", lw=0.9, zorder=5)
for s in (-1, 1):
    bio.shape(ax, [(cx + s * 1.5, 4.0), (cx + s * 2.3, 3.6), (cx + s * 1.9, 2.2), (cx + s * 0.9, 2.6)], "mandible", lw=0.9, zorder=4)
bio.callout(ax, (cx + 0.3, 10.8), (cx + 4.4, 11.5), "Vertex")
bio.callout(ax, (cx, 10.2), (cx - 4.6, 11.3), "Epicranial suture (stem)")
bio.callout(ax, (cx - 0.95, 8.55), (cx - 5.0, 10.3), "Frontal suture (arm)")
bio.callout(ax, (cx + 0.95, 8.95), (cx + 4.4, 10.4), "Lateral ocellus")
bio.callout(ax, (cx + 2.9, 8.4), (cx + 4.4, 9.3), "Compound eye")
bio.callout(ax, (cx + 1.25, 7.45), (cx + 4.4, 8.2), "Antennal socket")
bio.callout(ax, (cx, 7.15), (cx + 4.4, 7.2), "Median ocellus")
bio.callout(ax, (cx + 0.5, 6.3), (cx + 4.4, 6.2), "Frons")
bio.callout(ax, (cx + 2.6, 5.8), (cx + 4.4, 5.3), "Gena")
bio.callout(ax, (cx + 1.0, 5.3), (cx + 4.4, 4.4), "Frontoclypeal suture")
bio.callout(ax, (cx + 2.5, 4.75), (cx + 4.4, 3.6), "Subgenal suture")
bio.callout(ax, (cx - 0.6, 4.7), (cx - 4.8, 5.2), "Clypeus")
bio.callout(ax, (cx - 0.4, 3.2), (cx - 4.8, 3.6), "Labrum")
bio.callout(ax, (cx - 2.0, 2.8), (cx - 4.8, 2.3), "Mandible")

# B: head orientations
def glyph(x, y, kind, title, ex):
    body = [(x - 3.0, y - 0.45), (x - 0.9, y - 0.45), (x - 0.9, y + 0.45), (x - 3.0, y + 0.45)]
    bio.shape(ax, body, "neutral", lw=0.8, zorder=3)
    ax.add_patch(Ellipse((x, y), 1.8, 1.4, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.9, zorder=4))
    d = {"hypo": (0, -1), "pro": (1, 0), "opistho": (-0.6, -0.8)}[kind]
    d = np.array(d) / np.linalg.norm(d)
    a = np.array([x, y]) + d * 0.7
    bio.arrow(ax, tuple(a), tuple(a + d * 1.2), kind="process", color=P.edge("mandible"))
    ax.plot([x - 3.4, x + 2.3], [y, y], color=P.muted(), lw=0.6, ls=(0, (4, 3)), zorder=2)
    bio.label(ax, (x + 2.6, y + 0.35), title, size="normal", bold=True, ha="left")
    bio.label(ax, (x + 2.6, y - 0.3), ex, size="tiny", ha="left", color=P.muted())
glyph(19.3, 10.0, "hypo", "Hypognathous", "grasshoppers, cockroaches")
glyph(19.3, 6.6, "pro", "Prognathous", "ground beetles, earwigs, larvae")
glyph(19.3, 3.2, "opistho", "Opisthognathous", "true bugs, cicadas, aphids")
bio.label(ax, (20.0, 1.3), "dashed line: body axis; arrow: mouthparts", size="tiny", color=P.muted())
