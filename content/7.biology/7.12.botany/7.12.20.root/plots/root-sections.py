# Primary structure of roots in transverse section (maturation zone), built cell by cell. (A) Eudicot
# root (e.g. Ranunculus): epidermis with root hairs, wide cortex, endodermis with Casparian strips (red),
# pericycle, tetrarch xylem star with exarch protoxylem at the arm tips, phloem strands between the arms,
# no pith. (B) Monocot root (e.g. Zea, Iris): exodermis, polyarch stele with protoxylem poles
# alternating with phloem, large metaxylem vessels and a central pith.
import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(29.4, 12.6)
RR = 4.4
CC, CD = (6.0, 6.0), (20.0, 6.0)
bio.panel(ax, "A", (0.2, 12.4))
bio.label(ax, (0.85, 12.37), "Eudicot root", size="title", ha="left", va="top")
c = B.root_section(ax, CC, RR, kind="eudicot")
bio.panel(ax, "B", (14.6, 12.4))
bio.label(ax, (15.25, 12.37), "Monocot root", size="title", ha="left", va="top")
d = B.root_section(ax, CD, RR, kind="monocot")


def labels(an, items, x, y0, dy=0.85):
    pts = [(name, an[key]) for key, name in items if an.get(key) is not None]
    pts.sort(key=lambda t: (-round(float(t[1][1]), 1), -float(t[1][0])))
    for k, (name, p) in enumerate(pts):
        bio.callout(ax, p, (x, y0 - k * dy), name)


labels(c, [("root_hair", "Root hair"), ("epidermis", "Epidermis"), ("cortex", "Cortex"), ("endodermis", "Endodermis"),
           ("casparian", "Casparian strip"), ("pericycle", "Pericycle"), ("phloem", "Primary phloem"),
           ("protoxylem", "Protoxylem (exarch)"), ("metaxylem", "Metaxylem")], 11.4, 11.0)
labels(d, [("epidermis", "Epidermis"), ("exodermis", "Exodermis"), ("cortex", "Cortex"), ("endodermis", "Endodermis"),
           ("pericycle", "Pericycle"), ("phloem", "Primary phloem"), ("protoxylem", "Protoxylem"),
           ("metaxylem", "Metaxylem vessel"), ("pith", "Pith")], 25.4, 11.0)
