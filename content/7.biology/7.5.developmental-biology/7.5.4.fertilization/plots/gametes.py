"""The gametes of sea urchin and mammal.

A: sperm. A mammalian sperm has a flattened head containing the condensed haploid nucleus, covered at the
front by the acrosome (a Golgi-derived secretory vesicle); behind it the midpiece with a helix of
mitochondria around the base of the flagellum, which is driven by dynein on the axoneme. A sea urchin sperm
has a small conical head with a small acrosomal vesicle at its tip and a single mitochondrion.
B: a sea urchin egg at fertilization: meiosis is complete and the haploid female pronucleus is visible; the
cell membrane is covered by the thin vitelline envelope and the jelly coat; about 15 000 cortical granules
lie under the membrane. C: a mammalian egg at ovulation, arrested in metaphase of meiosis II (spindle under
the first polar body), surrounded by the zona pellucida and by cumulus cells embedded in a hyaluronan matrix
(the inner layer is the corona radiata). The cortex over the spindle lacks cortical granules and microvilli.
Not to scale: a sea urchin egg is about 80 um across, a human egg about 120 um, a human sperm about 60 um long.
"""

import wikibio as bio
from wikibio import gametes as gam

P = bio.P
fig, ax = bio.canvas(27, 11.2)

bio.panel(ax, "A", (0.2, 11.0))
bio.label(ax, (4.0, 10.6), "Sperm", size="normal", bold=True)
s1 = gam.sperm(ax, (0.9, 8.6), angle=180, length=6.5, kind="mammal")
bio.callout(ax, s1["acrosome"], (0.9, 9.8), "acrosome", size="small")
bio.callout(ax, s1["nucleus"], (2.4, 9.8), "haploid nucleus", size="small")
bio.callout(ax, s1["midpiece"], (3.4, 7.4), "midpiece (mitochondria)", size="small")
bio.callout(ax, s1["tail"], (6.6, 7.4), "flagellum (axoneme)", size="small")
bio.label(ax, (4.0, 6.8), "mammal", size="small", color=P.muted())
s2 = gam.sperm(ax, (1.3, 4.6), angle=180, length=5.0, kind="urchin")
bio.callout(ax, s2["acrosome"], (0.9, 5.7), "acrosomal vesicle", size="small")
bio.callout(ax, s2["midpiece"], (2.6, 3.5), "one mitochondrion", size="small")
bio.label(ax, (4.0, 2.9), "sea urchin", size="small", color=P.muted())

bio.panel(ax, "B", (8.6, 11.0))
bio.label(ax, (12.4, 10.6), "Sea urchin egg", size="normal", bold=True)
e1 = gam.egg(ax, (12.4, 5.6), 2.3, kind="urchin", jelly=True)
bio.callout(ax, e1["jelly"], (15.6, 9.9), "jelly coat", size="small")
bio.callout(ax, e1["envelope"], (16.1, 8.7), "vitelline envelope", size="small")
bio.callout(ax, e1["granule"], (9.0, 2.0), "cortical granules", size="small")
bio.callout(ax, e1["nucleus"], (9.4, 9.7), "female pronucleus", size="small")
bio.callout(ax, e1["membrane"], (9.0, 8.4), "cell membrane", size="small")

bio.panel(ax, "C", (17.6, 11.0))
bio.label(ax, (22.0, 10.6), "Mammalian egg", size="normal", bold=True)
e2 = gam.egg(ax, (22.0, 5.6), 2.15, kind="mammal", cumulus=True, seed=2)
bio.callout(ax, e2["zona"], (26.2, 9.8), "zona pellucida", size="small")
bio.callout(ax, e2["polar_body"], (19.0, 10.0), "first polar body", size="small")
bio.callout(ax, e2["spindle"], (25.4, 10.3), "meiosis II spindle", size="small")
bio.callout(ax, e2["cumulus"], (26.4, 1.6), "cumulus cells", size="small")
bio.callout(ax, e2["granule"], (18.0, 1.6), "cortical granules", size="small")
bio.callout(ax, e2["space"], (24.3, 0.6), "perivitelline space", size="small")
