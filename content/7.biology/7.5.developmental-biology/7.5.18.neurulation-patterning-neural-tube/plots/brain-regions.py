"""Anterior-posterior regions of the vertebrate neural tube (schematic, anterior left). (A) The three primary
vesicles (prosencephalon, mesencephalon, rhombencephalon) subdivide into five secondary vesicles; the
telencephalon forms the cerebral hemispheres, the diencephalon the thalamus, hypothalamus and the optic vesicles,
the metencephalon the cerebellum and pons, the myelencephalon the medulla. (B) Expression map of the
midbrain-hindbrain region: the Otx2/Gbx2 border positions the isthmic organizer, which expresses Fgf8 (and Wnt1
just anterior to it) and maintains Engrailed across the boundary; the hindbrain is segmented into rhombomeres
r1-r7, with Krox20 (Egr2) in r3 and r5 and nested anterior limits of Hox paralogue groups 1-4 at rhombomere
boundaries (group 1 at r3/r4, group 2 at r1/r2, group 3 at r4/r5, group 4 at r6/r7)."""
import numpy as np
import wikibio as bio

fig, ax = bio.canvas(24, 11.5)
P = bio.P
bio.panel(ax, "A", (0.2, 11.4))


def tube(y, segs, h=0.9):
    for x0, x1, tok, name, sub in segs:
        bio.box(ax, ((x0 + x1) / 2, y), x1 - x0 - 0.08, h, token=tok, radius=0.3)
        bio.label(ax, ((x0 + x1) / 2, y), name, size="small", color=P.on_fill())
        if sub:
            bio.label(ax, ((x0 + x1) / 2, y - h / 2 - 0.3), sub, size="tiny", color=P.muted())


prim = [(1.0, 5.0, "receptor", "Prosencephalon", "forebrain"), (5.0, 7.5, "antibody", "Mesencephalon", "midbrain"),
        (7.5, 12.2, "enzyme", "Rhombencephalon", "hindbrain"), (12.2, 15.5, "channel", "Spinal cord", "")]
sec = [(1.0, 3.0, "receptor", "Telencephalon", "cerebrum"), (3.0, 5.0, "drug", "Diencephalon", "thalamus, retina"),
       (5.0, 7.5, "antibody", "Mesencephalon", "tectum, tegmentum"), (7.5, 9.6, "enzyme", "Metencephalon", "cerebellum, pons"),
       (9.6, 12.2, "carbohydrate", "Myelencephalon", "medulla"), (12.2, 15.5, "channel", "Spinal cord", "")]
tube(10.1, prim)
tube(8.0, sec)
bio.label(ax, (16.6, 10.1), "3-vesicle stage", size="small", ha="left")
bio.label(ax, (16.6, 8.0), "5-vesicle stage", size="small", ha="left")
for x in (3.0, 4.0, 6.25, 8.55, 10.9):
    bio.arrow(ax, (x, 9.15), (x, 8.55), kind="process", head=0.12, lw=0.9)

# (B) expression map
bio.panel(ax, "B", (0.2, 6.3))
cols = [("Fore", 0.6, 2.6), ("Mid", 2.6, 5.0), ("r1", 5.0, 6.6), ("r2", 6.6, 7.8), ("r3", 7.8, 9.0), ("r4", 9.0, 10.2),
        ("r5", 10.2, 11.4), ("r6", 11.4, 12.6), ("r7", 12.6, 13.8), ("SC", 13.8, 15.5)]
x_of = {n: (a, b) for n, a, b in cols}
ytop = 5.7
for n, a, b in cols:
    ax.plot([a, a], [0.4, ytop], color=P.muted(), lw=0.5, ls=":", zorder=2)
    bio.label(ax, ((a + b) / 2, ytop + 0.25), n, size="tiny")
ax.plot([5.0, 5.0], [0.4, ytop], color=P.edge("negative"), lw=1.2, zorder=3)
bio.label(ax, (5.0, 0.15), "isthmus (MHB)", size="tiny", color=P.edge("negative"))
rows = [("Otx2", [("Fore", "Mid")], "receptor"), ("Gbx2", [("r1", "SC")], "enzyme"), ("Wnt1", [("Mid", "Mid")], "antibody"),
        ("Fgf8", [("r1", "r1")], "negative"), ("En1/2", [("Mid", "r1")], "k"), ("Krox20", [("r3", "r3"), ("r5", "r5")], "drug"),
        ("Hox1", [("r4", "SC")], "dna"), ("Hox2", [("r2", "SC")], "dna"), ("Hox3", [("r5", "SC")], "dna"), ("Hox4", [("r7", "SC")], "dna")]
for k, (gene, spans, tok) in enumerate(rows):
    y = ytop - 0.45 - k * 0.5
    bio.label(ax, (0.45, y), gene, size="tiny", italic=True, ha="right")
    for s0, s1 in spans:
        a, b = x_of[s0][0], x_of[s1][1]
        if gene == "Wnt1":
            a = b - 0.5
        if gene == "Fgf8":
            b = a + 0.5
        if gene == "En1/2":
            a, b = 3.6, 6.2
        bio.box(ax, ((a + b) / 2, y), b - a - 0.06, 0.32, token=tok, radius=0.1)

# rhombomere lineage restriction and crest streams (side note)
bio.label(ax, (16.2, 5.3), "Rhombomeres", size="small", bold=True, ha="left")
notes = ["cells mix within a rhombomere,", "not across its boundaries (Eph/ephrin);",
         "even rhombomeres (r2, r4, r6) feed", "neural crest streams into pharyngeal", "arches 1, 2 and 3; r3 and r5 are",
         "largely crest-free", "", "Isthmic organizer", "graft into the diencephalon: ectopic", "midbrain and cerebellum; an Fgf8 bead", "mimics the graft"]
for k, t in enumerate(notes):
    bold = t == "Isthmic organizer"
    bio.label(ax, (16.2, 4.75 - k * 0.42), t, size="small" if bold else "tiny", ha="left", bold=bold,
              color=P.ink() if bold else P.muted())
