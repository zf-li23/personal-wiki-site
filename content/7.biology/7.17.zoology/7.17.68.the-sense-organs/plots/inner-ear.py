# Membranous labyrinths of six vertebrates, schematic lateral views of the left ear (anterior to the left).
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(25, 7.8)
C = {"canal": "channel", "utricle": "positive", "saccule": "highlight", "lagena": "drug", "papilla": "receptor"}


def loop(c, r, a0, a1, tok="canal", w=2.8):
    th = np.radians(np.linspace(a0, a1, 50))
    x, y = c[0] + r * np.cos(th), c[1] + r * np.sin(th)
    ax.plot(x, y, color=P.edge(C[tok]), lw=w + 1.4, zorder=4, solid_capstyle="round")
    ax.plot(x, y, color=P.fill(C[tok]), lw=w, zorder=4.1, solid_capstyle="round")
    return x, y


def sac(c, rx, ry, tok, text=None):
    bio.shape(ax, vs.oval(c, rx, ry), token=C[tok], zorder=5, lw=0.8)


def ampulla(p):
    bio.shape(ax, vs.oval(p, 0.17, 0.17), token=C["canal"], zorder=6, lw=0.7)


def panel(x, title, canals, lagena=False, papilla=None, cochlea=None):
    bio.label(ax, (x + 1.7, 7.4), title, size="small")
    sac((x + 1.7, 4.4), 0.9, 0.42, "utricle")
    if canals >= 1:
        loop((x + 1.0, 5.4), 0.85, 20, 200); ampulla((x + 0.2, 5.2))
    if canals >= 2:
        loop((x + 2.4, 5.4), 0.85, -20, 160); ampulla((x + 3.2, 5.1))
    if canals >= 3:
        loop((x + 1.7, 4.6), 1.35, 150, 210); ampulla((x + 0.4, 4.3))
    sac((x + 1.7, 3.2), 0.6, 0.55, "saccule")
    if lagena:
        sac((x + 2.3, 2.3), 0.33, 0.3, "lagena")
    if papilla:
        for p in papilla:
            sac(p, 0.18, 0.18, "papilla")
    if cochlea == "straight":
        ax.plot([x + 1.6, x + 1.9], [2.7, 1.2], color=P.edge(C["papilla"]), lw=6, zorder=4, solid_capstyle="round")
        ax.plot([x + 1.6, x + 1.9], [2.7, 1.2], color=P.fill(C["papilla"]), lw=4.4, zorder=4.1, solid_capstyle="round")
        sac((x + 1.95, 1.05), 0.25, 0.22, "lagena")
    if cochlea == "coiled":
        th = np.linspace(0, 5 * np.pi, 200)
        r = 0.9 * np.exp(-0.13 * th)
        xs, ys = x + 1.7 + r * np.cos(th), 1.6 + r * np.sin(th) * 0.8
        ax.plot(xs, ys, color=P.edge(C["papilla"]), lw=5, zorder=4, solid_capstyle="round")
        ax.plot(xs, ys, color=P.fill(C["papilla"]), lw=3.4, zorder=4.1, solid_capstyle="round")


panel(0.4, "A  Hagfish", 1)
panel(4.5, "B  Lamprey", 2)
panel(8.6, "C  Teleost", 3, lagena=True)
panel(12.7, "D  Frog", 3, lagena=True, papilla=[(12.7 + 2.5, 3.6), (12.7 + 1.0, 2.6)])
panel(16.8, "E  Bird", 3, cochlea="straight")
panel(20.9, "F  Mammal", 3, cochlea="coiled")
lx = 1.0
for k, t in (("canal", "semicircular canal, ampulla"), ("utricle", "utricle"), ("saccule", "saccule"),
             ("lagena", "lagena"), ("papilla", "auditory papillae, cochlear duct")):
    bio.shape(ax, np.array([(lx, 0.15), (lx + 0.4, 0.15), (lx + 0.4, 0.45), (lx, 0.45)]), token=C[k], lw=0.6)
    bio.label(ax, (lx + 0.55, 0.3), t, size="tiny", ha="left")
    lx += 4.8
