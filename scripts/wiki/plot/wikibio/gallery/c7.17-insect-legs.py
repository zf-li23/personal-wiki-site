# Insect leg types: one segmented ground plan (coxa, trochanter, femur, tibia, tarsus with 1-5
# tarsomeres, pretarsal claws) modified for different functions (wikibio.zoomorph.leg). Top: the insect in
# lateral view with the specialized pair coloured; bottom: that leg enlarged, segments coloured as in the
# key. Cursorial (running) legs are slender and similar (cockroach); saltatorial hind legs have an
# enlarged femur housing the jumping muscle, with its herringbone pattern, and a long spiny tibia
# (grasshopper, 3 tarsomeres); raptorial forelegs have an elongate coxa, and spiny femur and tibia that
# close like a jack-knife (mantis); fossorial forelegs are broad, the tibia bearing strong dactyls
# (mole cricket); natatorial hind legs are flattened and fringed with long setae, beating as oars
# (diving beetle). Proportions are schematic.
import wikibio as bio
from wikibio import zoomorph as zm

P = bio.P
fig, ax = bio.canvas(28, 13.4)
COLS = [
    ("cursorial", "Cursorial", "running", "Cockroach (Blattodea)", "Blattodea", dict(antenna=("setaceous", 0.55)), "mid", 4.2),
    ("saltatorial", "Saltatorial", "jumping", "Grasshopper (Caelifera)", "Orthoptera", dict(), "hind", 4.6),
    ("raptorial", "Raptorial", "grasping prey", "Mantis (Mantodea)", "Mantodea", dict(), "fore", 4.4),
    ("fossorial", "Fossorial", "digging", "Mole cricket (Gryllotalpidae)", "Orthoptera",
     dict(legs=("fossorial", "cursorial", "cursorial"), leg_len=(0.45, 0.4, 0.45), antenna=("setaceous", 0.25), pro=(0.2, 0.2, "plain"),
          fore=("orthoptera_fore", 0.3, 10), cerci=0.12, abd=(0.5, 0.17, "oval", 9)), "fore", 4.0),
    ("natatorial", "Natatorial", "swimming", "Diving beetle (Dytiscidae)", "Coleoptera",
     dict(legs=("cursorial", "cursorial", "natatorial"), leg_len=(0.32, 0.36, 0.75), abd=(0.6, 0.4, "oval", 6), clearance=0.05),
     "hind", 3.6),
]
CW = 5.6
for i, (kind, title, func, ex, order, over, pair, size) in enumerate(COLS):
    x = CW * i + CW / 2
    bio.label(ax, (x, 13.0), title, size="title", bold=True)
    bio.label(ax, (x, 12.45), f"{func}; e.g. {ex}", size="tiny", color=P.muted())
    zm.insect(ax, (x - 0.1, 10.2), size, order, view="lateral", highlight=(pair,), **over)
    # the enlarged leg
    L = {"cursorial": 5.2, "saltatorial": 5.6, "raptorial": 6.6, "fossorial": 4.2, "natatorial": 5.0}[kind]
    base = {"cursorial": (x - 1.8, 7.0), "saltatorial": (x + 0.2, 6.6), "raptorial": (x - 1.5, 5.0), "fossorial": (x - 1.8, 5.8),
            "natatorial": (x - 2.3, 6.0)}[kind]
    a = zm.leg(ax, base, kind, L)
    if i == 0:
        bio.callout(ax, a["coxa"], (x + 1.2, 7.4), "Coxa", size="tiny")
        bio.callout(ax, a["trochanter"], (x + 1.2, 6.9), "Trochanter", size="tiny")
        bio.callout(ax, a["femur"], (x + 1.2, 6.2), "Femur", size="tiny")
        bio.callout(ax, a["tibia"], (x + 1.2, 4.6), "Tibia", size="tiny")
        bio.callout(ax, a["tarsus"], (x + 1.2, 3.0), "Tarsus (5 tarsomeres)", size="tiny")
        bio.callout(ax, a["claws"], (x + 0.4, 1.9), "Claws (pretarsus)", size="tiny")
    elif kind == "saltatorial":
        bio.callout(ax, a["femur"], (x + 1.0, 2.6), "Enlarged femur", size="tiny")
        bio.callout(ax, a["tibia"], (x - 1.4, 2.0), "Spiny tibia", size="tiny")
    elif kind == "raptorial":
        bio.callout(ax, a["coxa"], (x + 0.9, 2.2), "Elongate coxa", size="tiny")
        bio.callout(ax, a["femur"], (x + 1.6, 7.2), "Spiny femur", size="tiny")
        bio.callout(ax, a["tibia"], (x + 1.6, 4.4), "Tibia folds on femur", size="tiny")
    elif kind == "fossorial":
        bio.callout(ax, a["dactyls"], (x + 0.6, 2.4), "Tibial dactyls", size="tiny")
        bio.callout(ax, a["femur"], (x + 1.0, 7.4), "Broad femur", size="tiny")
    elif kind == "natatorial":
        bio.callout(ax, a["tarsus"], (x + 0.8, 3.6), "Flattened tarsus,\nfringe of setae", size="tiny")
        bio.callout(ax, a["coxa"], (x - 1.0, 7.4), "Large fixed coxa", size="tiny")

# key
x0 = 7.2
for k, part in enumerate(("coxa", "trochanter", "femur", "tibia", "tarsus")):
    x = x0 + k * 3.0
    tok = zm.LEG[part]
    bio.shape(ax, [(x - 0.17, 0.43), (x + 0.17, 0.43), (x + 0.17, 0.77), (x - 0.17, 0.77)], tok, lw=0.8, zorder=20)
    bio.label(ax, (x + 0.35, 0.6), part.capitalize(), size="small", ha="left")
for c in range(1, 5):
    ax.plot([c * CW, c * CW], [1.2, 13.2], color=P.muted(), lw=0.4, alpha=0.5)
