# Major veins of a shark, a frog and a mammal, schematic ventral views (anterior up). Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(24, 12.2)
TOK = {"caval": "dna", "portal": "plant", "renal": "lipid_head", "abdominal": "rrna", "pulmonary": "negative"}


def vein(pts, kind, lw=3.2, dashed=False):
    p = np.asarray(pts, float)
    ls = (0, (3, 2)) if dashed else "-"
    ax.plot(p[:, 0], p[:, 1], color=P.edge(TOK[kind]), lw=lw + 1.2, zorder=5, solid_capstyle="round", ls=ls)
    ax.plot(p[:, 0], p[:, 1], color=P.fill(TOK[kind]), lw=lw, zorder=5.1, solid_capstyle="round", ls=ls)


def organ(c, rx, ry, tok, text=None):
    bio.shape(ax, vs.oval(c, rx, ry), token=tok, zorder=3, lw=0.8)
    if text:
        bio.label(ax, c, text, size="tiny", color=P.on_fill())


def heart(c):
    bio.shape(ax, vs.oval(c, 0.55, 0.4), token="blood", zorder=6, lw=0.8)


# A shark
x = 4.0
bio.label(ax, (x, 11.8), "A  Shark", size="small")
heart((x, 9.6))
organ((x, 7.4), 1.1, 0.7, "mitochondrion", "liver")
for s in (-1, 1):
    organ((x + s * 0.8, 4.0), 0.3, 2.0, "lysosome")
    vein([(x + s * 1.6, 11.2), (x + s * 1.6, 9.6), (x + s * 0.4, 9.6)], "caval")      # anterior cardinal, common cardinal
    vein([(x + s * 0.8, 6.2), (x + s * 1.3, 8.5), (x + s * 1.6, 9.6)], "caval")       # posterior cardinal
    vein([(x + s * 0.6, 1.3), (x + s * 0.8, 2.2), (x + s * 0.8, 5.8)], "renal", lw=2.4)
    vein([(x + s * 2.0, 2.2), (x + s * 2.2, 6.0), (x + s * 2.2, 9.0), (x + s * 1.6, 9.5)], "abdominal", lw=2.2)
vein([(x, 0.6), (x, 1.3), (x - 0.6, 1.3)], "renal", lw=2.4)
vein([(x, 1.3), (x + 0.6, 1.3)], "renal", lw=2.4)
vein([(x + 0.3, 3.0), (x + 0.2, 6.8)], "portal", lw=2.6)
vein([(x, 8.0), (x, 9.25)], "caval", lw=2.4)
for p, q, s in [((x - 1.6, 10.6), (x - 3.2, 11.0), "anterior cardinal"), ((x - 1.1, 8.2), (x - 3.4, 8.0), "posterior cardinal"),
                ((x - 0.9, 9.6), (x - 3.4, 9.4), "common cardinal"), ((x + 0.25, 4.5), (x + 3.0, 4.4), "hepatic portal"),
                ((x - 0.8, 3.0), (x - 3.4, 2.8), "renal portal"), ((x + 2.2, 7.0), (x + 3.0, 6.3), "lateral abdominal"),
                ((x, 0.8), (x + 1.8, 0.4), "caudal vein")]:
    bio.callout(ax, p, q, s, size="tiny")

# B frog
x = 12.0
bio.label(ax, (x, 11.8), "B  Frog", size="small")
heart((x, 9.6))
organ((x, 7.4), 1.1, 0.7, "mitochondrion", "liver")
for s in (-1, 1):
    organ((x + s * 0.7, 4.2), 0.35, 1.1, "lysosome")
    organ((x + s * 1.5, 9.4), 0.4, 0.75, "er")
    vein([(x + s * 1.7, 11.2), (x + s * 1.2, 10.0), (x + s * 0.4, 9.7)], "caval")      # anterior vena cava
    vein([(x + s * 1.3, 9.2), (x + s * 0.3, 9.45)], "pulmonary", lw=2.0)
    vein([(x + s * 1.2, 0.8), (x + s * 1.0, 3.0), (x + s * 0.85, 3.4)], "renal", lw=2.4)
    vein([(x + s * 1.0, 1.8), (x + s * 0.2, 2.6)], "abdominal", lw=2.0)
vein([(x, 3.2), (x, 6.8)], "caval")              # posterior vena cava (through liver)
vein([(x, 8.0), (x, 9.25)], "caval")
vein([(x, 2.6), (x - 0.15, 5.0), (x - 0.4, 6.8)], "abdominal", lw=2.2)
vein([(x + 0.5, 5.5), (x + 0.35, 6.8)], "portal", lw=2.4)
for p, q, s in [((x + 1.5, 10.6), (x + 2.6, 10.3), "anterior vena cava"), ((x + 1.2, 9.25), (x + 3.0, 8.7), "pulmonary vein"),
                ((x, 5.0), (x + 2.8, 5.6), "posterior vena cava"), ((x - 0.2, 4.4), (x - 3.0, 4.8), "ventral abdominal"),
                ((x - 1.1, 2.2), (x - 3.0, 2.0), "renal portal"), ((x + 0.45, 6.0), (x + 2.8, 6.6), "hepatic portal")]:
    bio.callout(ax, p, q, s, size="tiny")

# C mammal
x = 20.0
bio.label(ax, (x, 11.8), "C  Mammal", size="small")
heart((x, 9.6))
organ((x, 7.4), 1.2, 0.7, "mitochondrion", "liver")
for s in (-1, 1):
    organ((x + s * 0.9, 4.6), 0.35, 0.6, "lysosome")
    organ((x + s * 1.5, 9.4), 0.4, 0.75, "er")
    vein([(x + s * 1.3, 9.2), (x + s * 0.3, 9.45)], "pulmonary", lw=2.0)
    vein([(x + s * 1.2, 1.0), (x + s * 0.2, 2.6)], "caval", lw=2.6)
    vein([(x + s * 0.55, 4.6), (x, 4.6)], "caval", lw=2.0)
vein([(x - 1.7, 11.2), (x - 1.2, 10.0), (x - 0.4, 9.7)], "caval")
vein([(x + 1.7, 11.2), (x + 0.5, 10.6), (x - 1.2, 10.1)], "caval", lw=2.4)
vein([(x, 2.6), (x, 6.6)], "caval")
vein([(x, 8.1), (x, 9.25)], "caval")
vein([(x - 0.5, 5.0), (x - 0.5, 8.8), (x - 0.5, 9.4)], "caval", lw=1.6, dashed=True)
vein([(x + 0.6, 4.0), (x + 0.45, 6.8)], "portal", lw=2.4)
for p, q, s in [((x - 1.5, 10.6), (x - 3.0, 11.2), "right anterior vena cava"), ((x + 0.9, 10.4), (x + 2.6, 11.4), "left brachiocephalic"),
                ((x, 5.6), (x + 2.6, 5.9), "posterior vena cava"), ((x - 0.5, 8.6), (x - 3.0, 8.4), "azygos"),
                ((x + 0.52, 5.2), (x + 2.6, 4.2), "hepatic portal"), ((x + 1.3, 9.25), (x + 2.6, 8.6), "pulmonary vein"),
                ((x - 0.9, 4.6), (x - 3.0, 4.3), "kidney (no renal portal)")]:
    bio.callout(ax, p, q, s, size="tiny")

# legend
lx = 1.0
for k, t in (("caval", "cardinal and caval veins"), ("portal", "hepatic portal"), ("renal", "renal portal"),
             ("abdominal", "abdominal veins"), ("pulmonary", "pulmonary veins")):
    ax.plot([lx, lx + 0.6], [0.25, 0.25], color=P.fill(TOK[k]), lw=4, solid_capstyle="round")
    bio.label(ax, (lx + 0.8, 0.25), t, size="tiny", ha="left")
    lx += 4.6
