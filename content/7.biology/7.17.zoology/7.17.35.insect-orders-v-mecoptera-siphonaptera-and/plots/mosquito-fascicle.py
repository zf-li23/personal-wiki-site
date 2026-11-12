# The proboscis of a female mosquito in cross-section (schematic, after the standard descriptions of
# Culicidae mouthparts). Six stylets form the fascicle that enters the skin: the labrum (folded into the food
# canal), two mandibles, two maxillae (laciniae, toothed at the tip, which cut and anchor) and the
# hypopharynx (with the salivary canal). The labium is a grooved sheath that encloses the fascicle and bends
# back as the stylets penetrate; it does not enter the wound. Colours follow the mouthpart homology used
# throughout the course: labrum yellow, mandibles orange, maxillae blue, labium green.
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon
import wikibio as bio
from wikibio import zoomorph as zm

P = bio.P
fig, ax = bio.canvas(22, 11)
M = zm.MOUTH


def ring(c, r_out, r_in, t0, t1, tok, z=6):
    th = np.linspace(t0, t1, 80)
    pts = [(c[0] + r_out * np.cos(t), c[1] + r_out * np.sin(t)) for t in th]
    pts += [(c[0] + r_in * np.cos(t), c[1] + r_in * np.sin(t)) for t in th[::-1]]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=z))


c = (8.0, 5.4)
# labium sheath: open dorsally (top)
ring(c, 4.2, 3.6, np.deg2rad(115), np.deg2rad(425), M["labium"], z=4)
# labrum: an inverted gutter forming the food canal
ring((c[0], c[1] + 1.2), 1.45, 0.95, np.deg2rad(-75), np.deg2rad(255), M["labrum"], z=7)
food = (c[0], c[1] + 1.2)
ax.add_patch(Circle(food, 0.9, facecolor=P.light("blood"), edgecolor=P.edge("blood"), lw=0.7, zorder=6))
# mandibles (thin blades) and maxillae (larger, toothed tips)
for sgn in (-1, 1):
    ax.add_patch(Ellipse((c[0] + sgn * 2.15, c[1] + 0.9), 0.55, 1.6, angle=sgn * 20, facecolor=P.fill(M["mandible"]),
                         edgecolor=P.edge(M["mandible"]), lw=0.8, zorder=7))
    ax.add_patch(Ellipse((c[0] + sgn * 1.75, c[1] - 1.5), 1.35, 1.0, angle=-sgn * 25, facecolor=P.fill(M["maxilla"]),
                         edgecolor=P.edge(M["maxilla"]), lw=0.8, zorder=7))
# hypopharynx with salivary canal
ax.add_patch(Ellipse((c[0], c[1] - 0.75), 1.4, 0.7, facecolor=P.fill(M["hypopharynx"]), edgecolor=P.edge(M["hypopharynx"]),
                     lw=0.8, zorder=7))
ax.add_patch(Circle((c[0], c[1] - 0.75), 0.16, facecolor=P.light("highlight"), edgecolor=P.edge("highlight"), lw=0.6, zorder=8))
bio.callout(ax, (c[0], c[1] + 2.42), (14.2, 10.2), "Labrum (rolled into the food canal)", size="small")
bio.callout(ax, food, (14.2, 8.9), "Food canal: blood drawn up by the cibarial\nand pharyngeal pumps", size="small")
bio.callout(ax, (c[0] + 2.2, c[1] + 0.9), (14.2, 7.4), "Mandible (thin blade)", size="small")
bio.callout(ax, (c[0] + 1.85, c[1] - 1.5), (14.2, 5.9), "Maxilla (lacinia, toothed tip:\ncuts and anchors)", size="small")
bio.callout(ax, (c[0], c[1] - 0.75), (14.2, 4.2), "Hypopharynx with salivary canal:\nanticoagulants, vasodilators", size="small")
bio.callout(ax, (c[0] + 3.0, c[1] - 2.8), (14.2, 2.6), "Labium: grooved sheath, bends back;\ntip (labella) guides the stylets", size="small")
bio.label(ax, (c[0], 0.4), "Fascicle of six stylets inside the labial sheath (cross-section)", size="small", bold=True)
bio.label(ax, (21.8, 0.1), "Schematic; not to scale", size="tiny", color=P.muted(), ha="right")
