# Leaf blade morphology, generated from rules (wikibio.botany): (A) overall shapes of simple blades, named
# by the outline as a whole and by where the blade is widest (lanceolate and ovate: below the middle;
# oblanceolate and obovate: above it; elliptic and oblong: at the middle); (B) apex types; (C) base types.
# The apex and base are described independently of the overall shape (terms after Harris & Harris, Plant
# Identification Terminology; Beentje, The Kew Plant Glossary). Petiole at the bottom.
import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(27.0, 19.4)

SHAPES = ["linear", "lanceolate", "oblanceolate", "elliptic", "oblong", "ovate", "obovate", "orbicular", "spatulate",
          "cordate", "reniform", "sagittate", "hastate", "deltoid", "rhombic", "flabellate", "palmately lobed"]
VEIN = {"linear": "parallel", "flabellate": "dichotomous", "palmately lobed": "palmate", "reniform": "palmate",
        "orbicular": "palmate"}
SIZE = {"reniform": 1.55, "orbicular": 2.0, "palmately lobed": 2.1, "flabellate": 1.55, "deltoid": 2.1, "sagittate": 2.2}

bio.panel(ax, "A", (0.2, 19.2))
bio.label(ax, (0.85, 19.17), "Blade shape", size="title", ha="left", va="top")
for i, s in enumerate(SHAPES):
    x = 1.5 + (i % 9) * 2.95
    y = 15.6 - (i // 9) * 4.0
    ln = SIZE.get(s, 2.5)
    B.leaf(ax, (x, y - 0.1), ln, 90, shape=s, petiole=0.35 if s not in ("sagittate", "hastate") else 0.9,
           venation=VEIN.get(s, "pinnate"), secondaries=5)
    bio.label(ax, (x, y - 0.5), s.capitalize(), size="small")

bio.panel(ax, "B", (0.2, 10.4))
bio.label(ax, (0.85, 10.37), "Apex", size="title", ha="left", va="top")
APICES = ["acuminate", "acute", "obtuse", "rounded", "truncate", "retuse", "emarginate", "mucronate", "cuspidate", "aristate"]
for i, a in enumerate(APICES):
    x = 1.4 + i * 2.6
    B.leaf(ax, (x, 6.75), 2.6, 90, shape="oblong", width=1.15, apex=a, base_type="rounded",
           petiole=0.0, venation="pinnate", secondaries=5)
    bio.label(ax, (x, 6.4), a.capitalize(), size="small")

bio.panel(ax, "C", (0.2, 5.5))
bio.label(ax, (0.85, 5.47), "Base", size="title", ha="left", va="top")
BASES = ["attenuate", "cuneate", "obtuse", "rounded", "truncate", "cordate", "oblique", "sagittate", "hastate"]
for i, b in enumerate(BASES):
    x = 1.6 + i * 2.85
    B.leaf(ax, (x, 1.55), 2.3, 90, shape="ovate" if b in ("cordate", "sagittate", "hastate") else "oblong", width=1.25, apex="acute",
           base_type=b, petiole=0.35 if b not in ("sagittate", "hastate") else 0.75, venation="pinnate", secondaries=4)
    bio.label(ax, (x, 1.2 if b != "sagittate" else 1.2), b.capitalize(), size="small")
