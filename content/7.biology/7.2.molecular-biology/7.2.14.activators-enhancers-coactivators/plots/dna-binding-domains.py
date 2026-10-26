# A gallery of DNA-binding domains (schematic side views, not to scale). Alpha helices are drawn as cylinders,
# beta strands as flat arrows, zinc ions as small discs; DNA runs horizontally.
# A: three Cys2His2 zinc fingers of Zif268 on 5'-GCG TGG GCG-3' (finger 3 at the 5' end), each a beta hairpin plus
# a recognition helix in the major groove. B: homeodomain, helix 3 in the major groove, N-terminal arm in the minor
# groove at a TAAT core. C: bZIP dimer (GCN4): parallel coiled coil of leucine zippers (leucines every 7 residues)
# continuing into basic regions that grip the DNA. D: bHLH dimer: basic region and helix 1, loop, helix 2; the four
# helices form a bundle; E box CANNTG. E: GAL4 dimer: Zn2Cys6 recognition modules at CGG triplets 11 bp apart,
# joined by linkers to a coiled-coil dimerization helix. F: nuclear receptor DNA-binding domain dimer: two Cys4
# zinc modules per monomer on an inverted repeat (glucocorticoid response element).
import numpy as np
from matplotlib.patches import Circle, Polygon
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(22.5, 15.4)
PT = 0.45 * 72  # points per canvas unit


def cyl(a, b, tok, w=0.36, z=14):
    """An alpha helix drawn as a cylinder from a to b."""
    xs, ys = [a[0], b[0]], [a[1], b[1]]
    ax.plot(xs, ys, color=P.edge(tok), lw=w * PT + 2.2, solid_capstyle="round", zorder=z)
    ax.plot(xs, ys, color=P.fill(tok), lw=w * PT, solid_capstyle="round", zorder=z + 0.1)


def sheet(a, b, tok, w=0.22, z=14):
    """A beta strand drawn as a flat arrow from a to b."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    d = b - a
    L = np.hypot(*d)
    u = d / L
    n = np.array([-u[1], u[0]])
    hl = min(0.3, 0.45 * L)
    pts = [a + n * w / 2, b - u * hl + n * w / 2, b - u * hl + n * w, b, b - u * hl - n * w, b - u * hl - n * w / 2,
           a - n * w / 2]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=z))


def loop(pts, tok, z=13, dashed=False):
    p = bio.core.polyline(pts, n=80)[0] if len(pts) > 2 else np.asarray(pts)
    ax.plot(p[:, 0], p[:, 1], color=P.edge(tok), lw=1.6, zorder=z, ls=(0, (3, 2)) if dashed else "-",
            solid_capstyle="round")


def zn(c, text=True, z=16):
    ax.add_patch(Circle(c, 0.13, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.9, zorder=z))
    if text:
        bio.label(ax, (c[0] + 0.2, c[1] + 0.02), "Zn", size="tiny", ha="left", zorder=z + 1)


def dna(ox, oy, x0=0.6, x1=6.9, y=1.7):
    bio.dna(ax, (ox + x0, oy + y), (ox + x1, oy + y), style="helix", width=0.8, ends=False, zorder=8)


def title(ox, oy, letter, text):
    bio.panel(ax, letter, (ox + 0.05, oy + 7.3))
    bio.label(ax, (ox + 0.6, oy + 6.95), text, size="small", bold=True, ha="left")


def seq(ox, oy, x, text, y=0.75):
    bio.label(ax, (ox + x, oy + y), text, size="tiny", color=P.muted())


# ---------------- A: zinc fingers
ox, oy = 0.0, 7.7
title(ox, oy, "A", "Cys₂His₂ zinc fingers (Zif268)")
dna(ox, oy)
for k, (x, trip, name) in enumerate([(1.9, "GCG", "F3"), (3.85, "TGG", "F2"), (5.8, "GCG", "F1")]):
    X = ox + x
    sheet((X - 0.75, oy + 3.95), (X - 0.05, oy + 3.55), "receptor")
    sheet((X + 0.0, oy + 3.25), (X - 0.75, oy + 3.6), "receptor")
    cyl((X - 0.55, oy + 2.75), (X + 0.6, oy + 2.05), "receptor")
    zn((X - 0.15, oy + 3.0), text=(k == 0))
    bio.label(ax, (X + 0.35, oy + 3.85), name, size="tiny", bold=True)
    seq(ox, oy, x, trip)
    if k < 2:
        loop([(X + 0.65, oy + 2.0), (X + 1.0, oy + 2.9), (X + 1.15, oy + 3.95)], "receptor")
seq(ox, oy, 0.55, "5′", y=0.75)
seq(ox, oy, 6.95, "3′", y=0.75)
bio.callout(ax, (ox + 2.4, oy + 2.4), (ox + 0.9, oy + 5.4), "recognition helix\n(major groove)", size="tiny")
bio.callout(ax, (ox + 3.45, oy + 3.75), (ox + 4.6, oy + 5.6), "β hairpin", size="tiny")

# ---------------- B: homeodomain
ox, oy = 7.5, 7.7
title(ox, oy, "B", "Homeodomain")
dna(ox, oy)
cyl((ox + 2.0, oy + 2.15), (ox + 5.0, oy + 2.1), "drug")                  # helix 3
cyl((ox + 2.3, oy + 3.65), (ox + 4.7, oy + 3.85), "drug")                 # helix 1
cyl((ox + 4.9, oy + 3.15), (ox + 3.0, oy + 2.95), "drug")                 # helix 2
loop([(ox + 4.7, oy + 3.85), (ox + 5.25, oy + 3.6), (ox + 4.9, oy + 3.15)], "drug")
loop([(ox + 3.0, oy + 2.95), (ox + 2.4, oy + 2.6), (ox + 2.0, oy + 2.15)], "drug")
loop([(ox + 2.3, oy + 3.65), (ox + 1.5, oy + 3.0), (ox + 1.3, oy + 1.65), (ox + 2.2, oy + 1.2)], "drug", z=7, dashed=True)
bio.label(ax, (ox + 3.5, oy + 4.3), "helix 1", size="tiny")
bio.label(ax, (ox + 5.6, oy + 3.0), "helix 2", size="tiny", ha="left")
bio.callout(ax, (ox + 4.4, oy + 2.1), (ox + 5.4, oy + 5.2), "helix 3 (major groove)", size="tiny")
bio.callout(ax, (ox + 1.4, oy + 1.5), (ox + 0.8, oy + 5.2), "N-terminal arm\n(minor groove)", size="tiny")
seq(ox, oy, 3.6, "TAAT")

# ---------------- C: bZIP
ox, oy = 15.0, 7.7
title(ox, oy, "C", "bZIP dimer (GCN4, Fos–Jun)")
dna(ox, oy, y=1.4)
for sgn, tok in ((-1, "receptor"), (1, "antibody")):
    xc = ox + 3.75 + sgn * 0.2
    cyl((xc, oy + 3.35), (xc, oy + 6.2), tok, w=0.34)
    cyl((xc, oy + 3.35), (ox + 3.75 + sgn * 1.25, oy + 1.65), tok, w=0.34)
    for yy in np.arange(3.7, 6.2, 0.55):
        ax.add_patch(Circle((xc - sgn * 0.17, oy + yy), 0.07, color=P.edge("highlight"), zorder=16))
bio.callout(ax, (ox + 3.55, oy + 5.0), (ox + 1.2, oy + 5.6), "leucine zipper\n(coiled coil)", size="tiny")
bio.callout(ax, (ox + 2.75, oy + 2.4), (ox + 0.9, oy + 3.4), "basic region", size="tiny")
bio.label(ax, (ox + 4.4, oy + 5.6), "Leu every\n7 residues", size="tiny", ha="left", color=P.muted())
seq(ox, oy, 3.75, "TGA(C/G)TCA", y=0.45)

# ---------------- D: bHLH
ox, oy = 0.0, 0.0
title(ox, oy, "D", "bHLH dimer (MyoD, Myc–Max)")
dna(ox, oy, y=1.4)
for sgn, tok in ((-1, "enzyme"), (1, "channel")):
    xb = ox + 3.75 + sgn * 1.3
    cyl((xb, oy + 1.65), (ox + 3.75 + sgn * 0.35, oy + 4.3), tok, w=0.34)          # basic region + helix 1
    loop([(ox + 3.75 + sgn * 0.35, oy + 4.3), (ox + 3.75 + sgn * 0.8, oy + 4.25), (ox + 3.75 + sgn * 1.0, oy + 4.7)], tok)
    cyl((ox + 3.75 + sgn * 1.0, oy + 4.7), (ox + 3.75 + sgn * 0.25, oy + 6.1), tok, w=0.34)  # helix 2
bio.callout(ax, (ox + 2.75, oy + 2.4), (ox + 0.8, oy + 3.3), "basic region\n+ helix 1", size="tiny")
bio.callout(ax, (ox + 4.55, oy + 4.3), (ox + 6.0, oy + 5.4), "loop", size="tiny")
bio.callout(ax, (ox + 3.6, oy + 5.5), (ox + 1.4, oy + 6.0), "helix 2", size="tiny")
bio.label(ax, (ox + 5.0, oy + 3.6), "four-helix\nbundle", size="tiny", ha="left", color=P.muted())
seq(ox, oy, 3.75, "E box: CANNTG", y=0.45)

# ---------------- E: GAL4
ox, oy = 7.5, 0.0
title(ox, oy, "E", "GAL4 dimer (Zn₂Cys₆)")
dna(ox, oy, y=1.5)
for sgn, tok in ((-1, "protein"), (1, "metabolite")):
    xm = ox + 3.75 + sgn * 2.3
    cyl((xm - 0.35, oy + 1.95), (xm + 0.35, oy + 1.95), tok, w=0.3)
    zn((xm - 0.15, oy + 2.45), text=(sgn < 0))
    zn((xm + 0.15, oy + 2.45), text=False)
    loop([(xm, oy + 2.6), (xm - sgn * 0.6, oy + 3.4), (ox + 3.75 + sgn * 0.2, oy + 3.8)], tok)
    cyl((ox + 3.75 + sgn * 0.2, oy + 3.8), (ox + 3.75 + sgn * 0.2, oy + 6.1), tok, w=0.32)
bio.callout(ax, (ox + 3.9, oy + 5.2), (ox + 5.2, oy + 5.9), "coiled coil\n(residues 50–94)", size="tiny")
bio.callout(ax, (ox + 1.2, oy + 2.0), (ox + 0.6, oy + 4.6), "recognition module\n(residues 1–40)", size="tiny")
seq(ox, oy, 1.45, "CGG", y=0.55)
seq(ox, oy, 3.75, "N₁₁", y=0.55)
seq(ox, oy, 6.05, "CCG", y=0.55)

# ---------------- F: nuclear receptor
ox, oy = 15.0, 0.0
title(ox, oy, "F", "Nuclear receptor DBD dimer")
dna(ox, oy, y=1.5)
for sgn, tok in ((-1, "lipid"), (1, "rna")):
    xc = ox + 3.75 + sgn * 1.45
    cyl((xc - 0.6, oy + 1.95), (xc + 0.6, oy + 1.95), tok, w=0.32)                 # recognition helix (module I)
    zn((xc - sgn * 0.6, oy + 2.75), text=(sgn < 0))
    cyl((xc - 0.5, oy + 3.5), (xc + 0.5, oy + 3.6), tok, w=0.3)                   # module II helix
    zn((xc + sgn * 0.3, oy + 4.2), text=False)
    loop([(xc + 0.6, oy + 1.95), (xc + 0.75 * sgn, oy + 2.8), (xc + 0.5, oy + 3.6)], tok)
ax.plot([ox + 3.75, ox + 3.75], [oy + 3.1, oy + 4.6], color=P.muted(), lw=0.8, ls=(0, (2, 2)), zorder=15)
bio.label(ax, (ox + 3.75, oy + 4.9), "dimer interface", size="tiny", color=P.muted())
bio.label(ax, (ox + 1.0, oy + 4.6), "two Cys₄\nzinc modules", size="tiny", color=P.muted())
seq(ox, oy, 2.3, "AGAACA →", y=0.55)
seq(ox, oy, 3.75, "nnn", y=0.55)
seq(ox, oy, 5.2, "← TGTTCT", y=0.55)
