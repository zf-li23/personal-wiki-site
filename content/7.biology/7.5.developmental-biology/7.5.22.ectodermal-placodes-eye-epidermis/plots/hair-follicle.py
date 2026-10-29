"""The hair follicle and its cycle (schematic sections). (A) A growing (anagen) follicle: an epithelial tube
continuous with the epidermis, with the sebaceous gland and, below it, the bulge, where the attachment of the
arrector pili muscle marks the niche of the follicle stem cells. At the base, the matrix of rapidly dividing
transit-amplifying cells surrounds the dermal papilla, a condensate of dermal cells derived from the dermal
condensate of the embryo, and produces the hair shaft and inner root sheath. (B) The cycle: in catagen the lower
follicle regresses by apoptosis and the dermal papilla is drawn up to the bulge; in telogen (rest) the papilla lies
beside the bulge and the secondary hair germ; signals from the papilla (Wnt activation, relief of BMP inhibition)
activate the hair germ and then the bulge stem cells to start a new anagen."""
import numpy as np
import wikibio as bio
from wikibio import neurodev as N
from matplotlib.patches import Circle, Ellipse, Rectangle

fig, ax = bio.canvas(22, 10.8)
P = bio.P
ep = N.TISSUE["epidermis"]


def follicle(ax, x, top, depth, w=0.55, papilla=True, gland=True, shaft=True, scale=1.0, zorder=5):
    """An epithelial follicle hanging from the epidermis at x, reaching down to top - depth."""
    yb = top - depth
    body = np.array([(x - w, top), (x + w, top), (x + w, yb + 0.8 * scale), (x + 0.9 * scale, yb + 0.3 * scale),
                     (x + 0.7 * scale, yb - 0.4 * scale), (x - 0.7 * scale, yb - 0.4 * scale), (x - 0.9 * scale, yb + 0.3 * scale),
                     (x - w, yb + 0.8 * scale)])
    bio.shape(ax, bio.smooth_closed(body, n=160), ep, lw=1.0, zorder=zorder)
    a = {}
    if shaft:
        ax.add_patch(Rectangle((x - 0.15, yb), 0.3, depth + 1.2, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.8, zorder=zorder + 2))
    if papilla:
        ax.add_patch(Ellipse((x, yb - 0.05 * scale), 0.9 * scale, 0.7 * scale, facecolor=P.fill("mesoderm"), edgecolor=P.edge("mesoderm"),
                             lw=0.9, zorder=zorder + 3))
        a["papilla"] = (x, yb - 0.05 * scale)
        a["matrix"] = (x + 0.75 * scale, yb + 0.3 * scale)
    if gland:
        bio.shape(ax, bio.blob((x - w - 0.55, top - 1.1), 0.6, 0.45, wobble=0.06, seed=2, k=8), "lipid", lw=0.9, zorder=zorder + 1)
        a["gland"] = (x - w - 0.55, top - 1.1)
    a["bulge"] = (x + w, top - 2.2)
    return a


bio.panel(ax, "A", (0.2, 10.7))
top = 8.6
ax.add_patch(Rectangle((0.6, top), 8.6, 0.6, facecolor=P.fill(ep), edgecolor=P.edge(ep), lw=1.0))
ax.add_patch(Rectangle((0.6, 0.6), 8.6, top - 0.6, facecolor=P.light("mesoderm"), edgecolor="none", zorder=0))
a = follicle(ax, 4.6, top, 6.4)
ax.plot([a["bulge"][0], a["bulge"][0] + 2.3], [a["bulge"][1], a["bulge"][1] - 1.3], color=P.edge("muscle"), lw=3.0, zorder=4)
ax.add_patch(Ellipse(a["bulge"], 0.5, 0.9, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.9, zorder=8))
bio.callout(ax, a["bulge"], (7.6, 8.0), "bulge (stem cells)")
bio.callout(ax, a["gland"], (1.0, 7.0), "sebaceous gland")
bio.callout(ax, a["papilla"], (1.0, 1.6), "dermal papilla")
bio.callout(ax, a["matrix"], (7.6, 1.6), "matrix")
bio.callout(ax, (4.6, 5.0), (1.0, 4.6), "hair shaft")
bio.callout(ax, (a["bulge"][0] + 1.8, a["bulge"][1] - 1.03), (7.6, 5.4), "arrector pili")
bio.label(ax, (2.2, 9.6), "epidermis", size="small")
bio.label(ax, (8.8, 0.9), "dermis", size="tiny", color=P.muted(), ha="right")

bio.panel(ax, "B", (10.6, 10.7))
stages = [("anagen", 13.0, 6.4, 1.0), ("catagen", 16.5, 3.8, 0.85), ("telogen", 20.0, 2.0, 0.75)]
for name, x, depth, sc in stages:
    ax.add_patch(Rectangle((x - 1.4, top), 2.8, 0.45, facecolor=P.fill(ep), edgecolor=P.edge(ep), lw=0.9))
    b = follicle(ax, x, top, depth, w=0.42, scale=sc)
    ax.add_patch(Ellipse(b["bulge"], 0.4, 0.7, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=8))
    bio.label(ax, (x, top + 1.5), name, size="small", bold=True)
bio.arrow(ax, (14.2, 3.0), (15.3, 3.0), kind="process", head=0.15, lw=1.0)
bio.arrow(ax, (17.7, 3.0), (18.8, 3.0), kind="process", head=0.15, lw=1.0)
bio.label(ax, (16.5, 1.4), "lower follicle regresses by apoptosis", size="tiny", color=P.muted())
bio.label(ax, (20.0, 4.6), "then new anagen:", size="tiny", color=P.muted())
bio.label(ax, (20.0, 4.2), "Wnt on, BMP off", size="tiny", color=P.muted())
