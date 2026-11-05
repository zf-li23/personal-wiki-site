"""Transverse sections of a C3 dorsiventral eudicot leaf (A) and a C4 grass leaf with Kranz anatomy (B),
built cell by cell (wikibio.botany); labels on the right, in the vertical order of their anchors.
"""

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(25.0, 13.6)
W, H = 17.0, 4.2

bio.panel(ax, "A", (0.2, 13.4))
bio.label(ax, (0.85, 13.37), "C3 leaf (dorsiventral eudicot)", size="title", ha="left", va="top")
a = B.leaf_anatomy(ax, (0.6, 7.7, W, H), kind="C3", veins=2)
bio.panel(ax, "B", (0.2, 6.5))
bio.label(ax, (0.85, 6.47), "C4 leaf (Kranz anatomy, grass)", size="title", ha="left", va="top")
b = B.leaf_anatomy(ax, (0.6, 0.7, W, H), kind="C4")
X = W + 1.6


def labels(an, items, y0, y1):
    pts = [(name, an[key]) for key, name in items if an.get(key) is not None]
    pts.sort(key=lambda t: (-round(float(t[1][1]), 1), -float(t[1][0])))
    for k, (name, p) in enumerate(pts):
        y = y0 - k * (y0 - y1) / max(1, len(pts) - 1)
        bio.callout(ax, p, (X, y), name)


labels(a, [("cuticle", "Cuticle"), ("upper_epidermis", "Upper epidermis"), ("palisade", "Palisade mesophyll"),
           ("xylem", "Xylem"), ("sheath", "Bundle sheath"), ("phloem", "Phloem"), ("spongy", "Spongy mesophyll"),
           ("air_space", "Substomatal chamber"), ("guard_cell", "Guard cell"), ("lower_epidermis", "Lower epidermis")],
       12.6, 7.4)
labels(b, [("bulliform", "Bulliform cells"), ("upper_epidermis", "Upper epidermis"), ("mesophyll", "Radial mesophyll"),
           ("sheath", "Kranz bundle sheath"), ("xylem", "Xylem"), ("phloem", "Phloem"), ("guard_cell", "Stoma"),
           ("lower_epidermis", "Lower epidermis")], 5.6, 0.6)
