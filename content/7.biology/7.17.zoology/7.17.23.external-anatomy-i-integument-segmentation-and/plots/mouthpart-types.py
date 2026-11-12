# Insect mouthpart types in lateral view (anterior to the right), coloured by homology
# (wikibio.zoomorph.head): labrum (upper lip) yellow, mandibles orange, maxillae blue, labium (lower lip)
# green. The ancestral chewing set (grasshopper) has toothed mandibles, maxillae with 5-segmented palps and
# a labium with 3-segmented palps. In true bugs (Heteroptera) the labium forms a segmented sheath, the
# rostrum, around two pairs of stylets, mandibular (outer) and maxillary (inner, enclosing the food and
# salivary canals); the labium itself does not pierce. In butterflies and moths the mandibles are lost and
# the two maxillary galeae interlock into the coiled proboscis, flanked by upturned labial palps. In
# house flies mandibles and maxillary stylets are absent: the labium forms the haustellum ending in
# spongy labella, whose pseudotracheae draw up liquid food; the maxillary palps remain on the rostrum.
import wikibio as bio
from wikibio import zoomorph as zm

P = bio.P
fig, ax = bio.canvas(28, 12.2)
COLS = [
    ("chewing", "Chewing", "Grasshopper (Orthoptera)", 3.0, 1.75, "filiform"),
    ("piercing-sucking", "Piercing-sucking", "Shield bug (Heteroptera)", 9.4, 1.55, "filiform"),
    ("siphoning", "Siphoning", "Butterfly (Lepidoptera)", 16.4, 1.75, "clavate"),
    ("sponging", "Sponging", "House fly (Diptera)", 22.6, 1.6, "aristate"),
]
Y = 7.0
for kind, title, ex, x, sz, ant in COLS:
    bio.label(ax, (x + 0.9, 11.8), title, size="title", bold=True)
    bio.label(ax, (x + 0.9, 11.25), ex, size="small", color=P.muted())
    a = zm.head(ax, (x, Y), sz, kind, facing="right", antenna_length=0.85 if kind != "sponging" else 0.55)
    R = x + 2.5
    if kind == "chewing":
        bio.callout(ax, a["labrum"], (R, Y - 1.2), "Labrum")
        bio.callout(ax, a["mandible"], (R, Y - 2.0), "Mandible")
        bio.callout(ax, a["maxillary_palp"], (R, Y - 3.1), "Maxillary palp")
        bio.callout(ax, a["maxilla"], (x - 2.2, Y - 3.0), "Maxilla")
        bio.callout(ax, a["labial_palp"], (x - 2.2, Y - 3.7), "Labial palp")
        bio.callout(ax, a["labium"], (x - 2.2, Y - 2.3), "Labium")
    elif kind == "piercing-sucking":
        bio.callout(ax, a["labrum"], (R + 0.3, Y - 0.1), "Labrum")
        bio.callout(ax, a["rostrum"], (R + 0.3, Y - 1.5), "Labium (rostrum,\n4 segments)")
        bio.callout(ax, a["mandible"], (R + 0.3, Y - 3.1), "Mandibular stylets")
        bio.callout(ax, a["maxilla"], (R + 0.3, Y - 3.8), "Maxillary stylets")
    elif kind == "siphoning":
        bio.callout(ax, a["labial_palp"], (R, Y + 0.3), "Labial palp")
        bio.callout(ax, a["proboscis"], (R, Y - 2.2), "Proboscis\n(maxillary galeae)")
        bio.label(ax, (x - 0.4, Y - 4.4), "Mandibles absent", size="small", color=P.muted())
    else:
        bio.callout(ax, a["maxillary_palp"], (R, Y - 0.9), "Maxillary palp")
        bio.callout(ax, a["rostrum"], (R, Y - 1.6), "Rostrum")
        bio.callout(ax, a["labrum"], (R, Y - 2.3), "Labrum")
        bio.callout(ax, a["haustellum"], (R, Y - 3.0), "Haustellum (labium)")
        bio.callout(ax, a["labella"], (R, Y - 3.7), "Labella (pseudotracheae)")
        bio.label(ax, (x - 0.6, Y - 4.4), "Mandibles absent", size="small", color=P.muted())
    bio.callout(ax, a["eye"], (x - 1.9, Y + 2.0), "Compound eye", size="tiny")

# homology key
x0 = 6.5
bio.label(ax, (x0, 1.0), "Homologous parts:", size="small", bold=True, ha="right")
for k, part in enumerate(("labrum", "mandible", "maxilla", "labium")):
    x = x0 + 0.5 + k * 3.4
    tok = zm.MOUTH[part]
    bio.shape(ax, [(x - 0.17, 0.83), (x + 0.17, 0.83), (x + 0.17, 1.17), (x - 0.17, 1.17)], tok, lw=0.8, zorder=20)
    bio.label(ax, (x + 0.35, 1.0), part.capitalize(), size="small", ha="left")
