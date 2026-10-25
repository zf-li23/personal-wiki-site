# Monocots and eudicots compared. Monocots: one cotyledon (in grasses the scutellum), leaves usually with
# parallel venation, vascular bundles scattered through the stem, a fibrous root system of adventitious
# roots (the primary root is short-lived), floral organs usually in threes, pollen with one aperture
# (monosulcate), no true secondary growth. Eudicots: two cotyledons, reticulate venation, bundles in a
# ring (with a cambium), a taproot system, floral organs usually in fours or fives, pollen with three
# apertures (tricolpate, the defining character of the clade). Most are tendencies with exceptions (net
# veins in Arum and Smilax, monocot-like features in some water lilies and other early-diverging lineages,
# which share monosulcate pollen with monocots).
import wikibio as bio
from wikibio import botany as B
from wikibio import plant
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(21.0, 23.6)


def mid(b, dy=0.0):
    return (b[0] + b[2] / 2, b[1] + b[3] / 2 + dy)


def caption(b, text):
    bio.label(ax, (b[0] + b[2] / 2, b[1] + 0.32), text, size="small")


rows = [
    ("Embryo", lambda b: (PM.seed(ax, mid(b, 0.3), 2.4, kind="monocot"), caption(b, "one cotyledon (scutellum)")),
     lambda b: (PM.seed(ax, mid(b, 0.3), 2.6, kind="eudicot"), caption(b, "two cotyledons"))),
    ("Leaf venation", lambda b: (bio.icon(ax, "wikimedia/leaf-monocot", at=mid(b, 0.3), width=6.2), caption(b, "parallel veins")),
     lambda b: (bio.icon(ax, "wikimedia/leaf-eudicot", at=mid(b, 0.3), width=5.0), caption(b, "net (reticulate) veins"))),
    ("Stem", lambda b: (B.stem_section(ax, mid(b, 0.35), 1.25, kind="monocot"), caption(b, "scattered vascular bundles")),
     lambda b: (B.stem_section(ax, mid(b, 0.35), 1.25, kind="eudicot"), caption(b, "bundles in a ring"))),
    ("Root system", lambda b: (bio.icon(ax, "wikimedia/root-systems", at=(b[0] + b[2] / 2 + 0.17 * 3.6, b[1] + 2.05), width=3.6,
                                        hide=["soil", "taproot", "taproot-shoot", "lateral-root"], parts={"fibrous-root": "animal"}),
                               caption(b, "fibrous (adventitious roots)")),
     lambda b: (bio.icon(ax, "wikimedia/root-systems", at=(b[0] + b[2] / 2 - 0.3 * 3.6, b[1] + 2.05), width=3.6,
                         hide=["soil", "shoot", "fibrous-root"], parts={"lateral-root": "animal"}), caption(b, "taproot"))),
    ("Flower", lambda b: (plant.floral_diagram(ax, mid(b, 0.25), 1.05, [
        dict(organ="tepal", n=3, phase=180), dict(organ="tepal", n=3), dict(organ="stamen", n=3), dict(organ="stamen", n=3),
        dict(organ="gynoecium", n=3, placentation="axile")]), caption(b, "parts in threes")),
     lambda b: (plant.floral_diagram(ax, mid(b, 0.25), 1.05, [
         dict(organ="sepal", n=5, phase=0), dict(organ="petal", n=5), dict(organ="stamen", n=5),
         dict(organ="gynoecium", n=5, placentation="axile")]), caption(b, "parts in fours or fives"))),
    ("Pollen", lambda b: (PM.pollen(ax, mid(b, 0.3), 1.6, apertures=1), caption(b, "one aperture (monosulcate)")),
     lambda b: (PM.pollen(ax, mid(b, 0.3), 1.6, apertures=3), caption(b, "three apertures (tricolpate)"))),
]
def cellfn(f):
    return lambda _ax, b: f(b)


cells = [["", "Monocots", "Eudicots"]] + [[name, cellfn(m), cellfn(e)] for name, m, e in rows]
cells.append(["Secondary growth", "absent (no vascular cambium)", "common (woody and herbaceous)"])
PM.table(ax, (0.3, 23.2), col_w=[3.6, 8.4, 8.4], row_h=[0.9] + [3.3] * len(rows) + [0.9], cells=cells, size="small")
bio.icon(ax, "phylopic/wheat", at=(6.6, 22.75), height=0.75, color="plant")
bio.icon(ax, "phylopic/arabidopsis", at=(15.0, 22.75), height=0.75, color="plant")
