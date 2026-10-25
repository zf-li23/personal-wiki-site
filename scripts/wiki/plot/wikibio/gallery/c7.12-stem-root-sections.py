# Primary stems and roots of eudicots and monocots in transverse section, built cell by cell
# (wikibio.botany). (A) Eudicot stem (e.g. Helianthus): epidermis, collenchyma, cortical parenchyma and a
# ring of open collateral vascular bundles, each with a sclerenchyma cap, phloem outside, a fascicular
# cambium and xylem inside (protoxylem towards the pith, endarch); pith rays separate the bundles around a
# parenchymatous pith. (B) Monocot stem (e.g. Zea): sclerenchymatous hypodermis and ground tissue with
# scattered closed bundles (no cambium), more numerous and smaller towards the periphery; each bundle sits
# in a sclerenchyma sheath with phloem outwards, two large metaxylem vessels, protoxylem and a protoxylem
# lacuna. (C) Eudicot root (e.g. Ranunculus): epidermis with root hairs, wide cortex, endodermis with
# Casparian strips (red) in its radial walls, pericycle, and a solid stele with a four-armed (tetrarch) xylem
# star, protoxylem at the arm tips (exarch), alternating with phloem strands. (D) Monocot root (e.g. Zea,
# Iris): an exodermis below the epidermis and a polyarch stele: many protoxylem poles alternating with
# phloem, large metaxylem vessels and a central pith.
import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(29.4, 25.0)
R = 4.6
CA, CB = (6.0, 18.6), (20.0, 18.6)
CC, CD = (6.0, 6.0), (20.0, 6.0)
RR = 3.9

bio.panel(ax, "A", (0.2, 24.8))
bio.label(ax, (0.85, 24.77), "Eudicot stem", size="title", ha="left", va="top")
a = B.stem_section(ax, CA, R, kind="eudicot")
bio.panel(ax, "B", (14.6, 24.8))
bio.label(ax, (15.25, 24.77), "Monocot stem", size="title", ha="left", va="top")
b = B.stem_section(ax, CB, R, kind="monocot")
bio.panel(ax, "C", (0.2, 12.0))
bio.label(ax, (0.85, 11.97), "Eudicot root", size="title", ha="left", va="top")
c = B.root_section(ax, CC, RR, kind="eudicot")
bio.panel(ax, "D", (14.6, 12.0))
bio.label(ax, (15.25, 11.97), "Monocot root", size="title", ha="left", va="top")
d = B.root_section(ax, CD, RR, kind="monocot")


def labels(an, items, x, y0, dy=0.85, side="right"):
    pts = [(name, an[key]) for key, name in items if an.get(key) is not None]
    pts.sort(key=lambda t: (-round(float(t[1][1]), 1), -float(t[1][0])))
    for k, (name, p) in enumerate(pts):
        bio.callout(ax, p, (x, y0 - k * dy), name)


labels(a, [("epidermis", "Epidermis"), ("collenchyma", "Collenchyma"), ("cortex", "Cortex"), ("cap", "Sclerenchyma cap"),
           ("phloem", "Phloem"), ("cambium", "Fascicular cambium"), ("xylem", "Xylem (metaxylem)"), ("protoxylem", "Protoxylem"),
           ("pith_ray", "Pith ray"), ("pith", "Pith")], 11.3, 23.2)
labels(b, [("epidermis", "Epidermis"), ("hypodermis", "Sclerenchyma (hypodermis)"), ("sheath", "Bundle sheath"),
           ("phloem", "Phloem"), ("metaxylem", "Metaxylem vessel"), ("protoxylem", "Protoxylem"), ("lacuna", "Protoxylem lacuna"),
           ("ground", "Ground tissue")], 25.2, 23.2)
labels(c, [("root_hair", "Root hair"), ("epidermis", "Epidermis"), ("cortex", "Cortex"), ("endodermis", "Endodermis"),
           ("casparian", "Casparian strip"), ("pericycle", "Pericycle"), ("phloem", "Phloem"), ("protoxylem", "Protoxylem"),
           ("metaxylem", "Metaxylem")], 11.3, 10.6)
labels(d, [("epidermis", "Epidermis"), ("exodermis", "Exodermis"), ("cortex", "Cortex"), ("endodermis", "Endodermis"),
           ("pericycle", "Pericycle"), ("phloem", "Phloem"), ("protoxylem", "Protoxylem"), ("metaxylem", "Metaxylem vessel"),
           ("pith", "Pith")], 25.2, 10.6)
