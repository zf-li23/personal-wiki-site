"""Leaf blade terms, generated from rules (wikibio.botany): (A) overall shape of simple blades;
(B) apex types; (C) base types; (D) margins, from entire to deeply divided. Petiole at the bottom.
"""

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(27.0, 24.6)

SHAPES = ["linear", "lanceolate", "oblanceolate", "elliptic", "oblong", "ovate", "obovate", "orbicular", "spatulate",
          "cordate", "reniform", "sagittate", "hastate", "deltoid", "rhombic", "flabellate", "palmately lobed"]
VEIN = {"linear": "parallel", "flabellate": "dichotomous", "palmately lobed": "palmate", "reniform": "palmate",
        "orbicular": "palmate"}
SIZE = {"reniform": 1.55, "orbicular": 2.0, "palmately lobed": 2.1, "flabellate": 1.55, "deltoid": 2.1, "sagittate": 2.2}

bio.panel(ax, "A", (0.2, 24.4))
bio.label(ax, (0.85, 24.37), "Blade shape", size="title", ha="left", va="top")
for i, s in enumerate(SHAPES):
    x = 1.5 + (i % 9) * 2.95
    y = 20.8 - (i // 9) * 4.0
    B.leaf(ax, (x, y - 0.1), SIZE.get(s, 2.5), 90, shape=s,
           petiole=0.35 if s not in ("sagittate", "hastate") else 0.9, venation=VEIN.get(s, "pinnate"), secondaries=5)
    bio.label(ax, (x, y - 0.5), s.capitalize(), size="small")

bio.panel(ax, "B", (0.2, 15.6))
bio.label(ax, (0.85, 15.57), "Apex", size="title", ha="left", va="top")
APICES = ["acuminate", "acute", "obtuse", "rounded", "truncate", "retuse", "emarginate", "mucronate", "cuspidate", "aristate"]
for i, a in enumerate(APICES):
    x = 1.4 + i * 2.6
    B.leaf(ax, (x, 11.95), 2.6, 90, shape="oblong", width=1.15, apex=a, base_type="rounded", petiole=0.0,
           venation="pinnate", secondaries=5)
    bio.label(ax, (x, 11.6), a.capitalize(), size="small")

bio.panel(ax, "C", (0.2, 10.7))
bio.label(ax, (0.85, 10.67), "Base", size="title", ha="left", va="top")
BASES = ["attenuate", "cuneate", "obtuse", "rounded", "truncate", "cordate", "oblique", "sagittate", "hastate"]
for i, b in enumerate(BASES):
    x = 1.6 + i * 2.85
    B.leaf(ax, (x, 6.75), 2.3, 90, shape="ovate" if b in ("cordate", "sagittate", "hastate") else "oblong", width=1.25,
           apex="acute", base_type=b, petiole=0.35 if b not in ("sagittate", "hastate") else 0.75, venation="pinnate",
           secondaries=4)
    bio.label(ax, (x, 6.4), b.capitalize(), size="small")

bio.panel(ax, "D", (0.2, 5.6))
bio.label(ax, (0.85, 5.57), "Margin", size="title", ha="left", va="top")
MARGINS = ["entire", "sinuate", "crenate", "dentate", "serrate", "serrulate", "doubly serrate", "spinose", "lobed",
           "pinnatifid", "pinnatisect"]
for i, m in enumerate(MARGINS):
    x = 1.3 + i * 2.4
    B.leaf(ax, (x, 1.1), 2.9, 90, shape="obovate" if m == "lobed" else "elliptic",
           width=1.3 if m not in ("pinnatifid", "pinnatisect") else 1.6, margin=m, petiole=0.3, venation="pinnate",
           secondaries=5, apex="acute" if m != "lobed" else "obtuse")
    bio.label(ax, (x, 0.75), {"pinnatifid": "Pinnatifid\n(parted)", "pinnatisect": "Pinnatisect\n(divided)"}.get(m, m.capitalize()),
              size="small", va="top")
