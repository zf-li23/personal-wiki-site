# Seeds and germination. A: eudicot seed (common bean, Phaseolus vulgaris) opened between its two
# cotyledons: the seed coat (testa) with the hilum (scar of the funiculus) and micropyle, the large
# cotyledons that store the food (no endosperm left at maturity), and the embryo axis: radicle,
# hypocotyl and plumule (epicotyl with the first foliage leaves). B: monocot grain (maize, Zea mays), a
# caryopsis in longitudinal section: pericarp fused with the seed coat, starchy endosperm under the
# aleurone layer, and the embryo with a single cotyledon, the scutellum (absorbs the endosperm), the
# coleoptile sheathing the plumule and the coleorhiza sheathing the radicle. C: epigeal germination
# (bean): the hypocotyl elongates as a hook, lifts the cotyledons above ground and straightens. D: hypogeal
# germination (pea, Pisum sativum): the cotyledons stay in the soil; the epicotyl forms the hook.
import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(31.0, 15.4)

bio.panel(ax, "A", (0.2, 15.2))
bio.label(ax, (4.8, 14.6), "Eudicot seed (bean)", size="normal", bold=True)
a = PM.seed(ax, (4.8, 11.2), 4.6, kind="eudicot")
PM.callouts(ax, [(a["seed_coat"], "Seed coat (testa)", "right"), (a["cotyledon"], "Cotyledon", "left"),
                 (a["plumule"], "Plumule", "right"), (a["hypocotyl"], "Hypocotyl", "right"),
                 (a["radicle"], "Radicle", "left"), (a["hilum"], "Hilum", "right"), (a["micropyle"], "Micropyle", "left")],
            left=1.6, right=7.9, gap=0.5)

bio.panel(ax, "B", (0.2, 7.6))
bio.label(ax, (4.8, 7.0), "Monocot grain (maize)", size="normal", bold=True)
b = PM.seed(ax, (4.6, 3.6), 5.4, kind="monocot")
PM.callouts(ax, [(b["pericarp"], "Pericarp + seed coat", "right"), (b["aleurone"], "Aleurone layer", "right"),
                 (b["endosperm"], "Endosperm", "right"), (b["scutellum"], "Scutellum (cotyledon)", "right"),
                 (b["coleoptile"], "Coleoptile", "left"), (b["plumule"], "Plumule", "left"),
                 (b["radicle"], "Radicle", "left"), (b["coleorhiza"], "Coleorhiza", "left")],
            left=1.9, right=7.7, gap=0.5)

for row, (kind, panel, text, y) in enumerate((("epigeal", "C", "Epigeal germination (bean)", 10.2),
                                               ("hypogeal", "D", "Hypogeal germination (pea)", 2.6))):
    bio.panel(ax, panel, (11.0, y + 5.0))
    bio.label(ax, (20.5, y + 4.4), text, size="normal", bold=True)
    anchors = []
    for k, st in enumerate((1, 2, 3)):
        x = 14.0 + 5.4 * k
        anchors.append(PM.germination(ax, (x, y), 4.6, kind=kind, stage=st))
        if k < 2:
            bio.arrow(ax, (x + 1.95, y + 1.6), (x + 3.2, y + 1.6), kind="process", color=P.muted())
    s1, s2, s3 = anchors
    lx = 14.0 + 5.4 * 2 + 2.4
    if kind == "epigeal":
        bio.callout(ax, s1["radicle"], (12.0, y - 2.0), "Radicle", size="small")
        bio.callout(ax, s2["hypocotyl"], (17.2, y + 3.5), "Hypocotyl hook", size="small")
        PM.callouts(ax, [(s3["leaves"], "First leaves", "right"), (s3["epicotyl"], "Epicotyl", "right"),
                         (s3["cotyledons"], "Cotyledons", "right"), (s3["hypocotyl"], "Hypocotyl", "right"),
                         (s3["root"], "Primary root", "right")], right=lx, gap=0.5)
    else:
        bio.callout(ax, s1["radicle"], (12.0, y - 2.0), "Radicle", size="small")
        bio.callout(ax, s2["epicotyl"], (17.4, y + 3.2), "Epicotyl hook", size="small")
        PM.callouts(ax, [(s3["leaves"], "First leaves", "right"), (s3["epicotyl"], "Epicotyl", "right"),
                         (s3["seed"], "Cotyledons (in seed)", "right"), (s3["root"], "Primary root", "right")], right=lx, gap=0.5)
    bio.label(ax, (14.0 + 5.4 * 2 + 2.3, y + 0.15), "soil surface", size="tiny", color=P.muted(), ha="left")
