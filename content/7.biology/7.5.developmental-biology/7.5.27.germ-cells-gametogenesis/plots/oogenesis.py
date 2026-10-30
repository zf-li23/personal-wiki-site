"""Oogenesis and folliculogenesis in the human ovary. Top: an oogonium divides mitotically in the fetal ovary,
enters meiosis and arrests as a primary oocyte in diplotene of prophase I (dictyate), for up to five decades;
at each ovulation one oocyte completes meiosis I, extruding the first polar body, and arrests again in
metaphase II; meiosis II is completed only at fertilization, with the second polar body. Bottom: the follicle
that houses the oocyte grows from a primordial follicle (a flat layer of pregranulosa cells) through primary
(one cuboidal granulosa layer, zona pellucida) and secondary follicles (several layers, theca) to the antral
(Graafian) follicle, whose oocyte sits in the cumulus beside a fluid-filled antrum. Growth to the preantral
stage takes months and does not need gonadotropins; the antral stages depend on FSH, and the LH surge
triggers meiotic resumption and ovulation."""
import wikibio as bio
from wikibio import organogenesis as O

P = bio.P
fig, ax = bio.canvas(24, 12)
g = O.germ_lineage(ax, (2.0, 9.0), "egg", step=5.0, r=0.5)
arrows = [("gonium", "primary", "fetal ovary:\nmitosis, then meiosis"), ("primary", "secondary", "LH surge:\nmeiosis I completed"),
          ("secondary", "egg", "fertilization:\nmeiosis II completed")]
for a_, b_, txt in arrows:
    xa, xb = g[a_][0], g[b_][0]
    bio.arrow(ax, (xa + 1.2, 9.0), (xb - 1.2, 9.0), kind="process")
    bio.label(ax, ((xa + xb) / 2, 10.0), txt, size="tiny", color=P.muted())
for key, txt in (("gonium", "oogonium\n2n, 2c"), ("primary", "primary oocyte\narrested in prophase I\n(dictyate), 2n, 4c"),
                 ("secondary", "secondary oocyte\narrested in metaphase II\n1n, 2c + polar body 1"), ("egg", "egg\n(+ polar body 2)")):
    bio.label(ax, (g[key][0], 7.0), txt, size="tiny")
xs = (2.4, 7.4, 12.6, 19.0)
for k, (st, r, txt) in enumerate((("primordial", 1.6, "primordial\n(about 0.03 mm)"), ("primary", 1.6, "primary"),
                                  ("secondary", 1.8, "secondary (preantral)\nabout 0.2 mm"), ("antral", 2.6, "antral (Graafian)\nup to about 20 mm"))):
    f = O.follicle(ax, (xs[k], 3.2), r, st)
    bio.label(ax, (xs[k], 0.4), txt, size="tiny")
    if st == "antral":
        bio.callout(ax, f["antrum"], (22.8, 5.6), "Antrum")
        bio.callout(ax, f["cumulus"], (15.6, 5.8), "Cumulus")
        bio.callout(ax, f["theca"], (22.8, 1.4), "Theca")
    if st == "secondary":
        bio.callout(ax, f["zona"], (10.2, 5.8), "Zona pellucida")
        bio.callout(ax, f["granulosa"], (15.0, 1.2), "Granulosa")
rad = (0.65, 0.9, 1.5, 2.55)
for a_, b_ in ((0, 1), (1, 2), (2, 3)):
    bio.arrow(ax, (xs[a_] + rad[a_] + 0.3, 3.2), (xs[b_] - rad[b_] - 0.3, 3.2), kind="process", color=P.muted())
