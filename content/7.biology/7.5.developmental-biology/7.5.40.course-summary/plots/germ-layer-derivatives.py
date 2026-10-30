"""The derivatives of the three germ layers and of the germ line, as a tree.

The epiblast gives the three germ layers at gastrulation (7.5.9) and the primordial germ cells
(7.5.27). Each germ layer is subdivided into the regions of the following chapters, and each leaf
names the main tissues formed, with the chapter in which their development is described.
Colours: ectoderm blue, mesoderm red, endoderm yellow (zoology.GERM); neural crest, neural tube,
notochord and intermediate mesoderm use the tokens of the neurodev and mesoderm modules.
"""

import wikibio as bio
from wikibio import mesoderm as M
from wikibio import neurodev as N
from wikibio.zoology import GERM

P = bio.P

tree = [
    ("Ectoderm", GERM["ectoderm"], [
        ("Surface ectoderm", GERM["ectoderm"], ["epidermis, hair, glands, tooth enamel (22)",
                                                "placodes: lens, inner ear, olfactory epithelium (22)"]),
        ("Neural crest", N.TISSUE["crest"], ["sensory and autonomic ganglia, Schwann cells (20)",
                                              "melanocytes; enteric neurons (20)",
                                              "facial skeleton, odontoblasts; outflow septum (20, 28)"]),
        ("Neural tube", N.TISSUE["neural"], ["brain and spinal cord (18, 19)", "retina (22)"]),
    ]),
    ("Mesoderm", GERM["mesoderm"], [
        ("Axial", N.TISSUE["notochord"], ["notochord, prechordal plate (16, 17)"]),
        ("Paraxial", M.TISSUE["paraxial"], ["sclerotome: vertebrae, ribs (23, 24)",
                                            "myotome, dermomyotome: muscle, dermis (23, 24)",
                                            "syndetome: tendons (23)"]),
        ("Intermediate", M.TISSUE["intermediate"], ["kidneys and ureters (25)", "gonads, genital ducts (26)"]),
        ("Lateral plate", GERM["mesoderm"], ["heart (28)", "blood vessels and blood (29)",
                                             "limb skeleton and connective tissue (31, 32)",
                                             "gut wall: smooth muscle, mesentery (30)"]),
    ]),
    ("Endoderm", GERM["endoderm"], [
        ("Foregut", GERM["endoderm"], ["pharyngeal pouches: thymus, parathyroids; thyroid (30)",
                                       "trachea and lungs (30)", "stomach, liver, pancreas (30)"]),
        ("Midgut, hindgut", GERM["endoderm"], ["intestinal epithelium (30)"]),
    ]),
    ("Germ line", "neutral", [
        ("PGCs", "neutral", ["eggs and sperm (27)"]),
    ]),
]

STEP = 0.72
n_leaves = sum(len(leaves) for _, _, subs in tree for _, _, leaves in subs)
gap = 0.45
H = n_leaves * STEP + gap * (len(tree) - 1) + 1.2
fig, ax = bio.canvas(24, H)

X_ROOT, X_LAYER, X_SUB, X_LEAF = 1.6, 5.4, 10.0, 13.1
y = H - 0.8
layer_pos = []
for name, tok, subs in tree:
    sub_pos = []
    for sname, stok, leaves in subs:
        ys = []
        for leaf in leaves:
            ax.plot([X_LEAF - 0.55, X_LEAF - 0.2], [y, y], color=P.muted(), lw=0.8)
            ax.plot([X_LEAF - 0.05], [y], "o", ms=4.5, color=P.fill(stok), mec=P.edge(stok), mew=0.8)
            bio.label(ax, (X_LEAF + 0.2, y), leaf, size="small", ha="left")
            ys.append(y)
            y -= STEP
        yc = (ys[0] + ys[-1]) / 2
        ax.plot([X_LEAF - 0.55, X_LEAF - 0.55], [ys[0], ys[-1]], color=P.muted(), lw=0.8)
        ax.plot([X_SUB + 1.3, X_LEAF - 0.55], [yc, yc], color=P.muted(), lw=0.8)
        bio.box(ax, (X_SUB, yc), 2.6, 0.55, stok, sname, size="small")
        sub_pos.append(yc)
    yl = (sub_pos[0] + sub_pos[-1]) / 2
    xm = X_SUB - 1.75
    ax.plot([xm, xm], [sub_pos[0], sub_pos[-1]], color=P.muted(), lw=0.9)
    for ys_ in sub_pos:
        ax.plot([xm, X_SUB - 1.3], [ys_, ys_], color=P.muted(), lw=0.9)
    ax.plot([X_LAYER + 1.2, xm], [yl, yl], color=P.muted(), lw=0.9)
    bio.box(ax, (X_LAYER, yl), 2.4, 0.7, tok, name, size="normal")
    layer_pos.append(yl)
    y -= gap

yr = (layer_pos[0] + layer_pos[-1]) / 2
xm = X_LAYER - 1.75
ax.plot([xm, xm], [layer_pos[0], layer_pos[-1]], color=P.muted(), lw=1.0)
for yl in layer_pos:
    ax.plot([xm, X_LAYER - 1.2], [yl, yl], color=P.muted(), lw=1.0)
ax.plot([X_ROOT + 1.0, xm], [yr, yr], color=P.muted(), lw=1.0)
bio.box(ax, (X_ROOT, yr), 2.0, 0.8, "positive", "Epiblast", size="normal")
bio.label(ax, (X_ROOT, yr - 0.85), "gastrulation (9)", size="tiny", color=P.muted())
bio.label(ax, (X_ROOT, yr - 1.25), "PGC induction (27)", size="tiny", color=P.muted())
bio.label(ax, (X_LEAF + 0.2, 0.35), "Numbers: chapters of this course (7.5.n)", size="tiny", color=P.muted(), ha="left")
