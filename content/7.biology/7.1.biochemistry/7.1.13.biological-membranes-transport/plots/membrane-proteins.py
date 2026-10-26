"""How proteins associate with the lipid bilayer (fluid mosaic model).

From left to right: a bitopic integral protein with one transmembrane helix and an extracellular
glycosylated domain (glycophorin); a polytopic protein with seven transmembrane helices
(bacteriorhodopsin, the GPCRs); a beta-barrel protein (porin) of the outer membranes of bacteria,
mitochondria and chloroplasts; a monotopic protein inserted into one leaflet only
(prostaglandin H2 synthase); a peripheral protein bound by electrostatic interactions and hydrogen
bonds to head groups and to an integral protein; and lipid-anchored proteins: a GPI-anchored
protein on the outer face, an N-myristoylated and S-palmitoylated protein and a prenylated
(farnesylated) protein on the inner face. Glycans (green) are always on the extracellular side.
"""

import numpy as np
from matplotlib.patches import FancyBboxPatch, Polygon
import wikibio as bio
from wikibio import cellbio as CB

P = bio.P
fig, ax = bio.canvas(24.0, 8.6)
y = 4.3
MH = CB.MH
CB.sides(ax, (0.2, 23.8), y, height=(3.9, 3.9), top=None, bottom=None)
bio.label(ax, (0.45, 2.5), "Cytosol", size="small", bold=True, ha="left", color=P.muted())
bio.label(ax, (0.45, 7.45), "Extracellular", size="small", bold=True, ha="left", color=P.muted())
bio.bilayer(ax, [(0.2, y), (23.8, y)])
LW = bio.core.LINE


def helix(x, tok, y0=y - MH - 0.12, y1=y + MH + 0.12, w=0.26, angle=0.0):
    ax.add_patch(FancyBboxPatch((x - w / 2, y0), w, y1 - y0, boxstyle=f"round,pad=0,rounding_size={w * 0.45}",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=LW * 0.8, zorder=12))


def glycan(base, n=4, direction=1, dx=0.0):
    pts = [np.asarray(base, float) + np.array([dx * k, 0.24 * k * direction]) for k in range(1, n + 1)]
    xs = [base[0]] + [p[0] for p in pts]
    ys = [base[1]] + [p[1] for p in pts]
    ax.plot(xs, ys, color=P.edge("carbohydrate"), lw=0.9, zorder=13)
    for p in pts:
        bio.molecule(ax, p, token="carbohydrate", r=0.1, zorder=14)
    # a branch at the second residue
    q = pts[1]
    r = q + np.array([0.24, 0.18 * direction])
    ax.plot([q[0], r[0]], [q[1], r[1]], color=P.edge("carbohydrate"), lw=0.9, zorder=13)
    bio.molecule(ax, r, token="carbohydrate", r=0.1, zorder=14)


def chain(a, b, tok="lipid", wave=True):
    """An acyl or prenyl chain inserted into the bilayer from a to b (zigzag)."""
    a, b = np.asarray(a, float), np.asarray(b, float)
    t = np.linspace(0, 1, 11)
    pts = a + (b - a) * t[:, None]
    d = (b - a) / np.linalg.norm(b - a)
    n = np.array([-d[1], d[0]])
    pts = pts + n * 0.05 * np.where(np.arange(11) % 2, 1, -1)[:, None]
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok), lw=1.6, zorder=13, solid_joinstyle="round")


def title(x, text, ytext=0.55):
    bio.label(ax, (x, ytext), text, size="small", bold=True)


# 1. bitopic glycoprotein
x = 1.9
helix(x, "receptor")
bio.protein(ax, (x, y + MH + 0.85), 1.1, 0.95, "receptor", wobble=0.07)
bio.protein(ax, (x, y - MH - 0.6), 0.7, 0.55, "receptor", wobble=0.07)
glycan((x - 0.2, y + MH + 1.3), n=3)
glycan((x + 0.3, y + MH + 1.25), n=3)
title(x, "bitopic")
bio.label(ax, (x, 0.2), "(glycophorin)", size="tiny", color=P.muted())

# 2. polytopic, seven helices
x = 5.2
for i in range(7):
    helix(x + (i - 3) * 0.34, "protein")
for i in range(6):
    x0, x1 = x + (i - 3) * 0.34, x + (i - 2) * 0.34
    yy = y + (MH + 0.12) * (1 if i % 2 else -1)
    t = np.linspace(0, np.pi, 20)
    ax.plot(np.linspace(x0, x1, 20), yy + np.sign(yy - y) * 0.16 * np.sin(t), color=P.edge("protein"), lw=LW, zorder=11)
title(x, "polytopic (7 TM)")
bio.label(ax, (x, 0.2), "(bacteriorhodopsin, GPCRs)", size="tiny", color=P.muted())

# 3. beta barrel
x = 8.9
w = 1.5
ax.add_patch(FancyBboxPatch((x - w / 2, y - MH - 0.12), w, 2 * MH + 0.24, boxstyle="round,pad=0,rounding_size=0.18",
                            facecolor=P.fill("channel"), edgecolor=P.edge("channel"), lw=LW, zorder=12))
for k in range(7):
    xx = x - w / 2 + 0.18 + k * (w - 0.36) / 6
    ax.plot([xx - 0.06, xx + 0.06], [y - MH - 0.02, y + MH + 0.02], color=P.edge("channel"), lw=0.9, zorder=12.5)
ax.add_patch(FancyBboxPatch((x - 0.22, y - MH - 0.12), 0.44, 2 * MH + 0.24, boxstyle="round,pad=0,rounding_size=0.1",
                            facecolor=P.fill("extracellular"), edgecolor=P.edge("channel"), lw=0.8, zorder=12.6))
title(x, "β barrel")
bio.label(ax, (x, 0.2), "(porin)", size="tiny", color=P.muted())

# 4. monotopic
x = 12.0
o = np.array([(x - 0.75, y - 0.1), (x + 0.75, y - 0.1), (x + 0.85, y - 0.9), (x + 0.5, y - 1.75), (x - 0.55, y - 1.8),
              (x - 0.9, y - 0.95)])
ax.add_patch(Polygon(bio.core.smooth_closed(o), closed=True, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=LW, zorder=12))
title(x, "monotopic")
bio.label(ax, (x, 0.2), "(PGH₂ synthase)", size="tiny", color=P.muted())

# 5. peripheral protein bound to an integral protein
x = 15.0
helix(x - 0.35, "neutral")
helix(x + 0.35, "neutral")
bio.protein(ax, (x + 0.2, y - MH - 0.62), 1.3, 0.8, "antibody", wobble=0.08, text=None)
title(x, "peripheral")
bio.label(ax, (x, 0.2), "(ionic and H bonds)", size="tiny", color=P.muted())

# 6. GPI anchor (outside)
x = 18.0
bio.protein(ax, (x + 0.1, y + MH + 1.75), 1.1, 0.85, "drug", wobble=0.07)
gp = [(x, y + 0.05), (x, y + MH + 0.25), (x + 0.15, y + MH + 0.55), (x + 0.0, y + MH + 0.85), (x + 0.1, y + MH + 1.3)]
gx, gy = zip(*gp)
ax.plot(gx, gy, color=P.edge("carbohydrate"), lw=1.0, zorder=13)
for p in gp[1:-1]:
    bio.molecule(ax, p, token="carbohydrate", r=0.1, zorder=14)
chain((x - 0.06, y + 0.05), (x - 0.1, y + MH - 0.05), "lipid")
chain((x + 0.06, y + 0.05), (x + 0.1, y + MH - 0.05), "lipid")
title(x, "GPI-anchored")
bio.label(ax, (x, 0.2), "(outer face)", size="tiny", color=P.muted())

# 7. myristoyl + palmitoyl (inside)
x = 20.4
bio.protein(ax, (x, y - MH - 1.0), 1.1, 0.8, "metabolite", wobble=0.07)
chain((x - 0.25, y - MH - 0.62), (x - 0.25, y - 0.05), "lipid")
chain((x + 0.2, y - MH - 0.62), (x + 0.2, y - 0.05), "lipid_head")
bio.callout(ax, (x - 0.25, y - MH - 0.45), (x - 1.0, y - 1.0), "myristoyl", size="tiny")
bio.callout(ax, (x + 0.2, y - MH - 0.45), (x + 0.9, y - 1.95), "palmitoyl", size="tiny")
title(x, "acylated")
bio.label(ax, (x, 0.2), "(inner face)", size="tiny", color=P.muted())

# 8. prenylated (farnesyl)
x = 22.7
bio.protein(ax, (x, y - MH - 0.95), 0.95, 0.75, "positive", wobble=0.07)
chain((x, y - MH - 0.62), (x, y - 0.05), "chloroplast")
bio.callout(ax, (x, y - MH - 0.4), (x + 0.45, y - 2.1), "farnesyl", size="tiny")
title(x, "prenylated")
bio.label(ax, (x, 0.2), "(Ras)", size="tiny", color=P.muted())

# brackets: integral / peripheral / lipid-anchored
for (x0, x1), text, tok in (((0.9, 13.0), "integral (hydrophobic contact with the bilayer core)", "protein"),
                            ((13.8, 16.2), "peripheral", "antibody"),
                            ((16.9, 23.6), "lipid-anchored (amphitropic when reversible)", "drug")):
    yy = 8.25
    ax.plot([x0, x0, x1, x1], [yy - 0.15, yy, yy, yy - 0.15], color=P.edge(tok), lw=1.1, zorder=15)
    bio.label(ax, ((x0 + x1) / 2, yy + 0.22), text, size="tiny", color=P.edge(tok), bold=True)
