# Compound leaves, leaf arrangement and phyllotaxis, generated from rules (wikibio.botany). (A) Compound
# leaves: the blade is divided into leaflets, each on a petiolule; a pinnate leaf has leaflets along a
# rachis, with (imparipinnate) or without (paripinnate) a terminal leaflet; a bipinnate leaf bears pinnae on
# the rachis, each with pinnules on its rachilla; palmately compound (digitate) leaflets spread from the
# petiole tip; a trifoliolate leaf has three leaflets (here pinnately trifoliolate, the terminal leaflet
# stalked, with stipules). A leaflet has no axillary bud; a leaf has one in its axil. (B) Arrangement of
# leaves at the nodes: alternate (one per node; distichous: successive leaves 180 degrees apart), spiral
# (one per node, about 137.5 degrees apart), opposite (two per node), decussate (opposite pairs at right
# angles to the pairs above and below) and whorled (three or more per node). Leaves behind the stem are
# drawn faded. (C) Spiral phyllotaxis seen from above the shoot apex (Vogel's model, primordium n at angle
# n x 137.5 degrees, radius proportional to the square root of n; 1 = youngest): successive primordia are
# separated by the golden angle 360(1 - 1/phi) = 137.5 degrees, and the primordia line up along two
# families of contact spirals (parastichies), 8 running one way and 13 the other: consecutive Fibonacci
# numbers.
import wikibio as bio
from wikibio import botany as B
from wikibio.quant import line_color

P = bio.P
fig, ax = bio.canvas(30.0, 19.0)

# ---- A: compound leaves -------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 18.8))
bio.label(ax, (0.85, 18.77), "Compound leaves", size="title", ha="left", va="top")
X = [2.6, 8.0, 13.6, 19.4, 25.3]
kinds = [("paripinnate", "Paripinnate"), ("imparipinnate", "Imparipinnate"), ("bipinnate", "Bipinnate"),
         ("palmate", "Palmately compound"), ("trifoliate", "Trifoliolate")]
anc = {}
for x, (k, name) in zip(X, kinds):
    anc[k] = B.compound_leaf(ax, (x, 10.6), 6.4 if k != "palmate" else 6.0, kind=k, leaflets=4 if k != "palmate" else 5,
                             pinnae=3, stipules=(k == "trifoliate"),
                             leaflet=dict(shape="oblanceolate", width=0.62, base_type="attenuate") if k == "palmate" else None)
    bio.label(ax, (x, 10.2), name, size="normal")
a = anc["imparipinnate"]
bio.callout(ax, a["terminal"], (X[1] + 2.3, 17.9), "Terminal leaflet")
bio.callout(ax, a["leaflets"][5]["blade"], (X[1] + 2.4, 15.0), "Leaflet")
bio.callout(ax, a["rachis"], (X[1] + 1.5, 12.4), "Rachis")
bio.callout(ax, a["petiole"], (X[1] + 1.3, 11.2), "Petiole")
p = anc["paripinnate"]
bio.callout(ax, p["petiolule"], (X[0] - 0.9, 12.4), "Petiolule")
bp = anc["bipinnate"]
bio.callout(ax, bp["pinna"], (X[2] + 2.9, 12.6), "Pinna")
bio.callout(ax, bp["pinnule"], (X[2] + 2.9, 11.6), "Pinnule")
bio.callout(ax, bp["rachilla"], (X[2] - 3.0, 13.6), "Rachilla")
t = anc["trifoliate"]
bio.callout(ax, t["stipule"], (X[4] + 1.8, 11.2), "Stipules")

# ---- B: arrangement ----------------------------------------------------------------------------------------------
bio.panel(ax, "B", (0.2, 9.0))
bio.label(ax, (0.85, 8.97), "Leaf arrangement", size="title", ha="left", va="top")
arr = [("alternate", "Alternate (distichous)"), ("spiral", "Spiral"), ("opposite", "Opposite"), ("decussate", "Decussate"),
       ("whorled", "Whorled")]
for i, (k, name) in enumerate(arr):
    x = 3.4 + i * 3.4
    s = B.shoot(ax, (x, 1.0), 6.6, arrangement=k, nodes=4 if k != "spiral" else 6, leaf_length=1.7)
    bio.label(ax, (x, 0.55), name, size="small")
    if k == "alternate":
        bio.callout(ax, s["node"], (x - 1.9, 3.7), "Node", size="tiny")
        bio.callout(ax, s["internode"], (x - 1.9, 4.6), "Internode", size="tiny")
        bio.callout(ax, s["apical_bud"], (x + 1.3, 7.95), "Terminal bud", size="tiny")
        if s.get("axillary_bud") is not None:
            bio.callout(ax, s["axillary_bud"], (x - 1.9, 6.4), "Axillary bud", size="tiny")

# ---- C: phyllotaxis -------------------------------------------------------------------------------------------------
bio.panel(ax, "C", (20.3, 9.0))
bio.label(ax, (20.95, 8.97), "Spiral phyllotaxis (apex view)", size="title", ha="left", va="top")
c = (26.5, 4.3)
ph = B.phyllotaxis(ax, c, 3.2, n=72, numbers=8, parastichies=(8, 13), tokens=("dna", "rna"))
bio.callout(ax, ph["arc"], (22.8, 7.4), "137.5° (golden angle)")
bio.callout(ax, ph["primordia"][0], (22.8, 6.5), "Youngest primordium (1)")
for k, (tkn, text) in enumerate((("dna", "8 parastichies (n to n + 8)"), ("rna", "13 parastichies (n to n + 13)"))):
    y = 1.3 - k * 0.5
    ax.plot([20.4, 21.0], [y, y], color=line_color(tkn), lw=1.6)
    bio.label(ax, (21.1, y), text, size="tiny", ha="left")
