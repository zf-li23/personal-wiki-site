# Primary stems in transverse section, built cell by cell (wikibio.botany). (A) Eudicot stem (e.g.
# Helianthus): epidermis, collenchyma, cortex, a ring of open collateral bundles (sclerenchyma cap, phloem
# outside, fascicular cambium, xylem inside with protoxylem towards the pith: endarch), pith rays and pith.
# (B) Monocot stem (e.g. Zea): sclerenchymatous hypodermis, ground tissue with scattered closed bundles,
# each in a sclerenchyma sheath with phloem outwards, two large metaxylem vessels, protoxylem and a
# protoxylem lacuna.
import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(29.4, 12.6)
R = 4.6
CA, CB = (6.0, 6.0), (20.0, 6.0)
bio.panel(ax, "A", (0.2, 12.4))
bio.label(ax, (0.85, 12.37), "Eudicot stem", size="title", ha="left", va="top")
a = B.stem_section(ax, CA, R, kind="eudicot")
bio.panel(ax, "B", (14.6, 12.4))
bio.label(ax, (15.25, 12.37), "Monocot stem", size="title", ha="left", va="top")
b = B.stem_section(ax, CB, R, kind="monocot")


def labels(an, items, x, y0, dy=0.85):
    pts = [(name, an[key]) for key, name in items if an.get(key) is not None]
    pts.sort(key=lambda t: (-round(float(t[1][1]), 1), -float(t[1][0])))
    for k, (name, p) in enumerate(pts):
        bio.callout(ax, p, (x, y0 - k * dy), name)


labels(a, [("epidermis", "Epidermis"), ("collenchyma", "Collenchyma"), ("cortex", "Cortex"), ("cap", "Sclerenchyma cap"),
           ("phloem", "Primary phloem"), ("cambium", "Fascicular cambium"), ("xylem", "Metaxylem"),
           ("protoxylem", "Protoxylem (endarch)"), ("pith_ray", "Pith ray"), ("pith", "Pith")], 11.4, 11.4)
labels(b, [("epidermis", "Epidermis"), ("hypodermis", "Sclerenchyma (hypodermis)"), ("sheath", "Bundle sheath"),
           ("phloem", "Phloem"), ("metaxylem", "Metaxylem vessel"), ("protoxylem", "Protoxylem"), ("lacuna", "Protoxylem lacuna"),
           ("ground", "Ground tissue")], 25.4, 11.4)
