# Gametes and fertilization (wikibio.gametes): mammalian and sea urchin sperm, intact and after the
# acrosome reaction; a mammalian egg in metaphase II with zona pellucida, cortical granules, first polar body
# and cumulus; a sea urchin egg with jelly coat and vitelline envelope, and after fertilization with its
# raised fertilization envelope; the cortex before, during and after cortical granule exocytosis; and a
# mammalian zygote at the pronuclear and first-spindle stages.
import wikibio as bio
from wikibio import gametes as gam

fig, ax = bio.canvas(26, 15)
P = bio.P

# sperm
s1 = gam.sperm(ax, (1.0, 13.6), angle=180, length=5.0, kind="mammal")
s2 = gam.sperm(ax, (1.0, 12.0), angle=180, length=5.0, kind="mammal", acrosome="reacted")
s3 = gam.sperm(ax, (7.4, 13.6), angle=180, length=3.6, kind="urchin")
s4 = gam.sperm(ax, (7.9, 12.0), angle=180, length=3.6, kind="urchin", acrosome="reacted")
bio.callout(ax, s1["acrosome"], (1.3, 14.7), "Acrosome")
bio.callout(ax, s1["midpiece"], (3.2, 14.7), "Midpiece")
bio.callout(ax, s2["equatorial"], (1.0, 11.0), "Equatorial segment")
bio.callout(ax, s4["process"], (8.6, 11.0), "Acrosomal process")
bio.label(ax, (3.5, 10.4), "Mammal: intact / reacted", size="small", color=P.muted())
bio.label(ax, (9.3, 10.4), "Sea urchin: intact / reacted", size="small", color=P.muted())

# eggs
e1 = gam.egg(ax, (15.0, 11.6), 1.55, kind="mammal", cumulus=True)
bio.callout(ax, e1["zona"], (18.8, 14.4), "Zona pellucida")
bio.callout(ax, e1["polar_body"], (14.0, 14.9), "First polar body")
bio.callout(ax, e1["granule"], (11.6, 9.4), "Cortical granules")
bio.callout(ax, e1["cumulus"], (18.8, 8.6), "Cumulus cells")
e2 = gam.egg(ax, (22.0, 12.4), 1.2, kind="urchin", jelly=True)
bio.callout(ax, e2["jelly"], (24.6, 14.6), "Jelly coat")
bio.callout(ax, e2["nucleus"], (21.0, 10.9), "Female pronucleus")
e3 = gam.egg(ax, (22.0, 8.6), 1.0, kind="urchin", envelope="fertilization")
bio.callout(ax, e3["envelope"], (24.6, 9.8), "Fertilization envelope")

# cortex
for k, st in enumerate(("before", "exocytosis", "after")):
    c = gam.cortex(ax, (0.6 + k * 5.6, 3.2, 5.0, 3.4), stage=st)
    bio.label(ax, (3.1 + k * 5.6, 2.8), st, size="small", color=P.muted())
    if k == 0:
        bio.callout(ax, c["granule"], (1.2, 2.2), "Cortical granule")
        bio.callout(ax, c["envelope"], (4.8, 7.2), "Vitelline envelope")
    if k == 2:
        bio.callout(ax, c["hyaline"], (12.2, 2.2), "Hyaline layer")
gam.cortex(ax, (17.6, 3.2, 3.0, 3.4), stage="before", kind="mammal", granules=4)
bio.label(ax, (19.1, 2.8), "mammal", size="small", color=P.muted())

# zygotes
z1 = gam.zygote(ax, (22.8, 4.9), 1.0, stage="pronuclei")
bio.callout(ax, z1["male"], (25.4, 2.6), "Male pronucleus")
bio.callout(ax, z1["female"], (21.0, 7.0), "Female pronucleus")
z2 = gam.zygote(ax, (22.8, 1.4), 0.75, stage="spindle", tail=False, zona=False)
