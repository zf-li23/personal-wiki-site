"""Fertilization in mammals.

A: the route of sperm in the female tract (schematic): of hundreds of millions of sperm deposited in the
vagina, only hundreds to a few thousand reach the oviduct; uncapacitated sperm bind the epithelium of the isthmus (the sperm
reservoir) and are released as they capacitate and become hyperactivated; guidance by fluid flow
(rheotaxis, long range), by the temperature rise of about 2 C from isthmus to ampulla (thermotaxis) and by
chemoattractants such as progesterone from cumulus cells (chemotaxis, short range). Fertilization occurs in
the ampulla. B: events at the egg: the sperm passes the cumulus (hyaluronidase), most fertilizing sperm have
undergone the acrosome reaction before reaching the zona, binds the N-terminal domain of ZP2, crosses the zona
and fuses side-on, at the equatorial segment, through IZUMO1 on the sperm binding JUNO on the egg membrane
(with CD9 on the egg microvilli). C: blocks to polyspermy: cortical granule exocytosis releases the protease
ovastacin, which cleaves ZP2 so that the zona no longer binds sperm (zona block); JUNO is shed from the egg
membrane within about 40 min (membrane block); a zinc spark accompanies egg activation.
"""


import wikibio as bio
from wikibio import gametes as gam

P = bio.P
fig, ax = bio.canvas(30, 11.6)

# ------------------------------------------------------------- A tract
bio.panel(ax, "A", (0.2, 11.4))
bio.label(ax, (5.6, 11.0), "The route to the egg (schematic)", size="small", bold=True)
segs = [("vagina", 1.6, "~10⁸"), ("cervix", 1.1, ""), ("uterus", 2.0, ""), ("isthmus", 2.1, "~10²–10³"), ("ampulla", 2.6, "~10²")]
x = 0.6
yb = 5.2
for k, (name, w, num) in enumerate(segs):
    tok = "receptor" if name != "isthmus" else "lipid_head"
    bio.box(ax, (x + w / 2, yb), w - 0.08, 0.9 if name not in ("cervix", "isthmus") else 0.55, tok, text=name, size="tiny", radius=0.1)
    if num:
        bio.label(ax, (x + w / 2, yb - 0.85), num, size="tiny", color=P.muted())
    x += w
gam.egg(ax, (x + 0.55, yb), 0.4, kind="mammal", granules=False, polar_bodies=0, spindle=False)
bio.label(ax, (x + 0.55, yb - 0.85), "egg", size="tiny", color=P.muted())
bio.label(ax, (0.6, yb - 1.45), "sperm numbers along the way", size="tiny", ha="left", color=P.muted())
# sperm reservoir and capacitation
bio.label(ax, (6.75, yb - 2.3), "isthmus: sperm bind the epithelium\n(reservoir); released as they\ncapacitate and hyperactivate",
          size="tiny", color=P.edge("lipid_head"))
bio.label(ax, (10.25, yb - 2.3), "ampulla:\nfertilization", size="tiny", color=P.ink())
# guidance ranges, as bars above the segments
for (x0, x1, y, txt, tok) in ((0.6, 9.4, 7.2, "uterine contractions, rheotaxis (against fluid flow)", "dna"),
                              (5.7, 9.4, 8.2, "thermotaxis (ampulla ~2 °C warmer)", "drug"),
                              (8.7, 10.4, 9.2, "chemotaxis (progesterone, cumulus)", "positive")):
    ax.plot([x0, x1], [y, y], color=P.edge(tok), lw=3.0, solid_capstyle="round", zorder=4)
    bio.arrow(ax, (x1 - 0.3, y), (x1 + 0.15, y), kind="process", color=P.edge(tok), head=0.2)
    bio.label(ax, (x0, y + 0.35), txt, size="tiny", ha="left", color=P.edge(tok))

# ------------------------------------------------------------- B at the egg
bio.panel(ax, "B", (13.0, 11.4))
bio.label(ax, (18.6, 11.0), "At the egg", size="small", bold=True)
c = (18.6, 5.6)
e = gam.egg(ax, c, 2.0, kind="mammal", cumulus=True, seed=5)
s1 = gam.sperm(ax, (c[0] - 3.3, c[1] + 2.0), angle=-30, length=2.2, kind="mammal")
s2 = gam.sperm(ax, (c[0] - 2.35, c[1] + 0.2), angle=0, length=2.2, kind="mammal", acrosome="reacted")
s3 = gam.sperm(ax, (c[0] - 1.55, c[1] - 1.3), angle=40, length=2.0, kind="mammal", acrosome="reacted")
bio.label(ax, (14.4, 10.3), "1 hyperactivated sperm passes the cumulus", size="tiny", ha="left")
bio.label(ax, (14.4, 0.9), "2 acrosome-reacted sperm binds ZP2, crosses the zona", size="tiny", ha="left")
bio.label(ax, (14.4, 0.4), "3 fusion at the equatorial segment: IZUMO1–JUNO", size="tiny", ha="left")
bio.callout(ax, e["zona"], (21.6, 10.4), "zona pellucida (ZP1–3; human ZP1–4)", size="tiny")

# ------------------------------------------------------------- C blocks
bio.panel(ax, "C", (23.0, 11.4))
bio.label(ax, (26.4, 11.0), "Blocks to polyspermy", size="small", bold=True)
cc = gam.cortex(ax, (23.4, 5.4, 6.2, 4.6), stage="exocytosis", kind="mammal", granules=5)
bio.label(ax, (26.5, 4.9), "cortical granule exocytosis", size="tiny", color=P.muted())
items = [("ovastacin cleaves ZP2:\nzona no longer binds sperm", "enzyme"), ("JUNO shed from the membrane\n(about 40 min)", "receptor"),
         ("zinc spark; Ca²⁺ oscillations\nactivate the egg", "ca")]
for k, (txt, tok) in enumerate(items):
    y = 3.9 - k * 1.25
    bio.box(ax, (23.8, y), 0.5, 0.5, tok)
    bio.label(ax, (24.25, y), txt, size="tiny", ha="left")
