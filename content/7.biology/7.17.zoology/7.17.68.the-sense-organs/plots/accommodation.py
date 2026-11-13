# Modes of accommodation, schematic horizontal sections of the eye (light from the left). Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(25, 6.8)
MV = P.edge("muscle")


def eye(cx, cy, title, lens=(0.0, 0.55, 0.55), cornea=0.3):
    bio.label(ax, (cx, cy + 2.6), title, size="small")
    bio.shape(ax, vs.oval((cx + 0.2, cy), 1.9, 1.9), token="nucleus", zorder=2)           # globe (vitreous)
    th = np.linspace(-1.3, 1.3, 40)
    ax.plot(cx + 0.2 + 1.9 * np.cos(th), cy + 1.9 * np.sin(th), color=P.edge("blood"), lw=3.0, zorder=3)  # retina
    th2 = np.linspace(np.pi - 0.75, np.pi + 0.75, 30)
    ax.plot(cx - 1.55 - cornea + 1.9 * (np.cos(th2) + 1) * 0.35, cy + 1.25 * np.sin(th2) / np.sin(0.75),
            color=P.edge("extracellular"), lw=2.0, zorder=4)
    dx, rx, ry = lens
    bio.shape(ax, vs.oval((cx - 0.9 + dx, cy), rx, ry), token="lipid", zorder=5, lw=0.9)
    return cx - 0.9 + dx


def arrow(a, b):
    bio.arrow(ax, a, b, kind="process", color=MV, lw=1.8, head=0.18)


x = 2.4; y = 3.2
lx = eye(x, y, "A  Teleost", lens=(0.0, 0.62, 0.62))
ax.plot([lx + 0.3, x + 1.4], [y - 0.5, y - 1.5], color=MV, lw=1.6, zorder=6)
arrow((lx + 0.7, y + 0.9), (lx + 1.4, y + 0.9))
bio.label(ax, (x, y - 2.4), "retractor lentis pulls lens back (far)", size="tiny")
x = 7.4
lx = eye(x, y, "B  Shark, frog", lens=(0.0, 0.55, 0.55))
ax.plot([lx - 0.2, x - 1.4], [y - 0.4, y - 1.2], color=MV, lw=1.6, zorder=6)
arrow((lx - 0.3, y + 0.9), (lx - 1.0, y + 0.9))
bio.label(ax, (x, y - 2.4), "protractor lentis pulls lens forward (near)", size="tiny")
x = 12.4
lx = eye(x, y, "C  Snake", lens=(0.0, 0.55, 0.55))
for s in (1, -1):
    arrow((x + 0.9, y + s * 1.0), (x + 0.3, y + s * 0.4))
arrow((lx - 0.3, y + 0.95), (lx - 1.0, y + 0.95))
bio.label(ax, (x, y - 2.4), "vitreous pressure pushes lens forward", size="tiny")
x = 17.4
lx = eye(x, y, "D  Bird, lizard", lens=(0.0, 0.45, 0.7), cornea=0.45)
for s in (1, -1):
    bio.shape(ax, vs.oval((lx, y + s * 0.95), 0.32, 0.17), token="muscle", zorder=6, lw=0.7)
    arrow((lx, y + s * 1.45), (lx, y + s * 1.05))
    ax.plot([x - 1.2, x - 0.6], [y + s * 1.6, y + s * 1.85], color=vs.edge("scleral_ossicle") if False else P.edge("bone"),
            lw=4, zorder=6)
bio.label(ax, (x, y - 2.4), "ciliary muscle squeezes soft lens", size="tiny")
x = 22.4
lx = eye(x, y, "E  Mammal", lens=(0.0, 0.4, 0.75))
for s in (1, -1):
    ax.plot([lx, lx], [y + s * 0.75, y + s * 1.5], color=P.muted(), lw=1.0, zorder=6)
    bio.shape(ax, vs.oval((lx, y + s * 1.6), 0.28, 0.14), token="muscle", zorder=6, lw=0.7)
bio.label(ax, (x, y - 2.4), "ciliary muscle relaxes zonule; lens rounds", size="tiny")
