# From ovipositor to sting (schematic, not to scale). The hymenopteran ovipositor is built from the
# appendages of abdominal segments 8 and 9: the first valvifers (A8) carry the first valvulae, which become
# the paired lancets; the second valvifers (A9) carry the second valvulae, fused into a single dorsal stylet,
# and the third valvulae, which form the sheaths. (A) A parasitoid wasp: the shaft is exserted and the egg
# passes down it. (B) A stinging wasp or bee: the same parts are withdrawn into a sting chamber, the egg
# leaves at the base, and the canal between stylet and lancets carries venom from the venom gland and its
# reservoir; Dufour's gland opens nearby. (C) Cross-section of the shaft: the lancets slide on rails of the
# stylet (tongue-and-groove joints) around a central canal.
import numpy as np
from matplotlib.patches import Ellipse, Polygon, Circle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27, 12.5)

C = {"v1": "enzyme", "v2": "protein", "v3": "channel", "vf1": "drug", "vf2": "antibody"}


def poly(pts, tok, z=6, lw=0.9):
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=lw, zorder=z,
                         joinstyle="round"))


def abdomen(x0, y0, w, h, nseg=6):
    """Outline of the posterior abdomen (segments 3 to 7) ending at x0 + w."""
    for i in range(nseg):
        xa = x0 + i * w / nseg
        xb = x0 + (i + 1) * w / nseg
        ha = h * (1 - 0.12 * i)
        hb = h * (1 - 0.12 * (i + 1))
        poly([(xa, y0 - ha / 2), (xb, y0 - hb / 2), (xb, y0 + hb / 2), (xa, y0 + ha / 2)], "bone", z=4)
    return x0 + w, h * (1 - 0.12 * nseg)


# ---------------- (A) parasitoid ovipositor
bio.panel(ax, "A", (0.2, 12.2))
bio.label(ax, (5.6, 12.0), "Parasitoid wasp: exserted ovipositor", size="normal", bold=True)
xe, he = abdomen(0.6, 8.4, 5.0, 2.6)
# valvifers at the tip
poly([(xe - 0.2, 8.4 - 0.55), (xe + 0.9, 8.0), (xe + 0.9, 8.35), (xe - 0.2, 8.4 + 0.1)], C["vf1"], z=7)
poly([(xe - 0.1, 8.4 + 0.1), (xe + 1.0, 8.45), (xe + 1.0, 8.8), (xe - 0.1, 8.4 + 0.55)], C["vf2"], z=7)
# shaft: lancets + stylet, and sheaths drawn alongside
L = 6.0
ax.plot([xe + 0.9, xe + 0.9 + L], [8.3, 7.3], color=P.edge(C["v1"]), lw=3.2, zorder=6, solid_capstyle="round")
ax.plot([xe + 0.9, xe + 0.9 + L], [8.42, 7.42], color=P.edge(C["v2"]), lw=2.2, zorder=7, solid_capstyle="round")
ax.plot([xe + 1.0, xe + 0.6 + L * 0.9], [8.75, 7.95], color=P.edge(C["v3"]), lw=2.6, zorder=6, solid_capstyle="round")
# egg moving down the shaft
ax.add_patch(Ellipse((xe + 3.6, 7.93), 0.55, 0.22, angle=-9.5, facecolor=P.fill("highlight"),
                     edgecolor=P.edge("highlight"), lw=0.8, zorder=9))
bio.callout(ax, (xe + 0.35, 8.1), (4.2, 6.4), "1st valvifer (A8)", size="small")
bio.callout(ax, (xe + 0.45, 8.6), (3.8, 10.9), "2nd valvifer (A9)", size="small")
bio.callout(ax, (xe + 4.6, 7.62), (11.0, 6.3), "lancets (1st valvulae) +\nstylet (2nd valvulae)", size="small")
bio.callout(ax, (xe + 4.0, 8.12), (10.8, 10.4), "sheaths (3rd valvulae)", size="small")
bio.callout(ax, (xe + 3.6, 7.93), (8.2, 10.9), "egg passes down the shaft", size="small")

# ---------------- (B) aculeate sting
bio.panel(ax, "B", (0.2, 5.2))
bio.label(ax, (6.2, 5.0), "Stinging wasp or bee: sting withdrawn", size="normal", bold=True)
xe2, he2 = abdomen(0.6, 1.9, 5.0, 2.6)
# sting chamber inside the tip
ax.add_patch(Ellipse((xe2 - 0.6, 1.8), 1.6, 0.75, facecolor=P.light("bone"), edgecolor=P.edge("bone"), lw=0.8,
                     zorder=5, ls=(0, (2, 1.5))))
poly([(xe2 - 1.3, 1.55), (xe2 - 0.6, 1.5), (xe2 - 0.6, 1.75), (xe2 - 1.3, 1.85)], C["vf1"], z=7)
poly([(xe2 - 1.35, 1.85), (xe2 - 0.5, 1.8), (xe2 - 0.5, 2.05), (xe2 - 1.35, 2.15)], C["vf2"], z=7)
ax.plot([xe2 - 0.6, xe2 + 0.9], [1.68, 1.5], color=P.edge(C["v1"]), lw=3.0, zorder=6, solid_capstyle="round")
ax.plot([xe2 - 0.6, xe2 + 0.9], [1.8, 1.62], color=P.edge(C["v2"]), lw=2.0, zorder=7, solid_capstyle="round")
# barbs (honey bee workers)
for k in range(5):
    xb = xe2 + 0.25 + 0.13 * k
    ax.plot([xb, xb - 0.08], [1.5 - 0.022 * k, 1.38 - 0.022 * k], color=P.edge(C["v1"]), lw=0.8, zorder=8)
# venom gland, reservoir, Dufour's gland
res = (xe2 - 2.2, 2.25)
ax.add_patch(Ellipse(res, 0.9, 0.55, facecolor=P.fill("negative"), edgecolor=P.edge("negative"), lw=0.8, zorder=7))
ax.plot([res[0] - 0.45, res[0] - 1.6, res[0] - 2.2], [2.3, 2.6, 2.4], color=P.edge("negative"), lw=1.1, zorder=7)
ax.plot([res[0] + 0.45, xe2 - 1.2], [2.2, 1.95], color=P.edge("negative"), lw=1.0, zorder=7)
duf = (xe2 - 1.9, 1.3)
ax.add_patch(Ellipse(duf, 0.75, 0.35, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=7))
bio.callout(ax, (res[0] - 1.6, 2.6), (1.6, 4.1), "venom gland", size="small")
bio.callout(ax, res, (5.2, 4.1), "venom reservoir", size="small")
bio.callout(ax, duf, (3.0, 0.35), "Dufour's gland", size="small")
bio.callout(ax, (xe2 + 0.55, 1.52), (9.6, 0.55), "lancets (barbed in honey bee workers)", size="small")
bio.callout(ax, (xe2 - 0.6, 1.95), (9.0, 3.4), "sting chamber; egg leaves at the base", size="small")

# ---------------- (C) cross-section of the shaft
bio.panel(ax, "C", (17.0, 12.2))
bio.label(ax, (21.8, 12.0), "Cross-section of the shaft", size="normal", bold=True)
cx, cy, R = 21.8, 7.0, 2.6
th = np.linspace(0.08 * np.pi, 0.92 * np.pi, 60)
outer = [(cx + R * np.cos(t), cy + R * np.sin(t)) for t in th]
inner = [(cx + 0.55 * R * np.cos(t), cy + 0.15 * R + 0.5 * R * np.sin(t)) for t in th[::-1]]
poly(outer + inner, C["v2"], z=6)
for sgn in (-1, 1):
    lx = cx + sgn * 1.45
    pts = [(lx - 0.95, cy - 0.15), (lx + 0.95, cy - 0.15), (lx + 0.85, cy - 1.95), (lx - 0.85, cy - 1.95)]
    poly(pts, C["v1"], z=6)
    # rail of the stylet fitting into a groove of the lancet
    ax.add_patch(Circle((lx, cy + 0.02), 0.28, facecolor=P.fill(C["v2"]), edgecolor=P.edge(C["v2"]), lw=0.8, zorder=8))
ax.add_patch(Ellipse((cx, cy + 0.55), 1.7, 1.1, facecolor=P.light("negative"), edgecolor=P.edge("negative"), lw=0.8,
                     zorder=7))
bio.callout(ax, (cx, cy + 2.2), (cx + 1.8, 10.6), "stylet (fused 2nd valvulae)", size="small")
bio.callout(ax, (cx + 1.5, cy - 1.2), (cx + 2.6, 3.6), "lancet (1st valvula)", size="small")
bio.callout(ax, (cx - 1.45, cy + 0.02), (cx - 3.6, 10.2), "rail in groove\n(olistheter)", size="small")
bio.callout(ax, (cx, cy + 0.55), (cx - 3.2, 3.6), "canal: egg or venom", size="small")
for i, (k, t) in enumerate([("vf1", "1st valvifer"), ("vf2", "2nd valvifer"), ("v1", "1st valvulae"),
                            ("v2", "2nd valvulae"), ("v3", "3rd valvulae")]):
    x = 17.4 + (i % 3) * 3.3
    y = 1.4 - (i // 3) * 0.7
    bio.box(ax, (x, y), 0.45, 0.35, token=C[k])
    bio.label(ax, (x + 0.35, y), t, size="tiny", ha="left")
bio.label(ax, (26.8, 0.1), "Schematic; not to scale", size="tiny", color=P.muted(), ha="right")
