# Tetrapod lungs in schematic section, ordered by internal subdivision. Not to scale.
import numpy as np
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax = bio.canvas(25.5, 11.0)
AIR, EX, SAC = "extracellular", "blood", "vesicle"


def sac(cx, cy, rx, ry, token=EX):
    v = vs.smooth([(cx - rx, cy), (cx - rx * 0.8, cy + ry * 0.8), (cx, cy + ry), (cx + rx * 0.8, cy + ry * 0.75),
                   (cx + rx, cy - ry * 0.1), (cx + rx * 0.6, cy - ry * 0.9), (cx, cy - ry), (cx - rx * 0.7, cy - ry * 0.85)])
    bio.shape(ax, v, token=token, zorder=3)
    return v


def lumen(cx, cy, rx, ry):
    bio.shape(ax, vs.oval((cx, cy), rx, ry), token=AIR, zorder=4, lw=0.6)


def bronchus(x, y0, y1):
    ax.plot([x, x], [y0, y1], color=P.edge(AIR), lw=5, zorder=6, solid_capstyle="round")
    ax.plot([x, x], [y0, y1], color=P.fill(AIR), lw=3.2, zorder=6.1, solid_capstyle="round")


def title(x, y, s):
    bio.label(ax, (x, y), s, size="small")


# row 1: A salamander, B frog, C lizard
cy = 7.7
title(3.0, 10.55, "A  Salamander")
sac(3.0, cy, 1.5, 2.0); lumen(3.0, cy, 1.38, 1.85); bronchus(3.0, cy + 1.9, cy + 2.6)
title(9.6, 10.55, "B  Frog")
sac(9.6, cy, 1.5, 2.0); lumen(9.6, cy, 1.05, 1.5); bronchus(9.6, cy + 1.6, cy + 2.6)
for a in np.linspace(0, 2 * np.pi, 16, endpoint=False):
    p = (9.6 + 1.05 * np.cos(a), cy + 1.5 * np.sin(a))
    q = (9.6 + 1.45 * np.cos(a), cy + 1.95 * np.sin(a))
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge(EX), lw=0.9, zorder=5)
title(16.2, 10.55, "C  Lizard (single-chambered)")
sac(16.2, cy, 1.5, 2.0); lumen(16.2, cy, 0.6, 1.1); bronchus(16.2, cy + 1.0, cy + 2.6)
for a in np.linspace(0, 2 * np.pi, 28, endpoint=False):
    for r0, r1 in ((0.6, 1.45),):
        p = (16.2 + r0 * np.cos(a) * 1.0, cy + 1.1 * np.sin(a) * 1.0 / 1.0)
        q = (16.2 + 1.45 * np.cos(a), cy + 1.95 * np.sin(a))
        ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge(EX), lw=0.7, zorder=5)
bio.callout(ax, (16.2 + 1.0 * np.cos(0.6), cy + 1.5 * np.sin(0.6)), (19.2, 9.8), "faveoli", size="tiny")
title(22.4, 10.55, "D  Crocodylian (multichambered)")
sac(22.4, cy, 1.6, 2.0)
bronchus(22.4, cy - 1.6, cy + 2.6)
for k, (dx, dy) in enumerate(((-0.8, 1.0), (0.8, 1.0), (-0.85, -0.1), (0.85, -0.1), (-0.7, -1.1), (0.7, -1.1))):
    lumen(22.4 + dx, cy + dy, 0.42, 0.33)
    ax.plot([22.4, 22.4 + dx * 0.55], [cy + dy, cy + dy], color=P.edge(AIR), lw=2.2, zorder=6)
for y in (cy + 1.6, cy + 0.4, cy - 0.6):
    bio.arrow(ax, (22.4 + 1.95, y), (22.4 + 1.95, y - 0.7), kind="process", color=P.edge("dna"), lw=1.1, head=0.14)
bio.label(ax, (24.9, cy - 0.2), "one-way flow", size="tiny", rotation=90, color=P.edge("dna"))

# row 2: E bird, F mammal
cy2 = 2.6
title(6.0, 5.2, "E  Bird: parabronchial lung and air sacs")
lung = np.array([(4.3, cy2 - 0.7), (7.7, cy2 - 0.7), (7.7, cy2 + 0.7), (4.3, cy2 + 0.7)])
bio.shape(ax, lung, token=EX, zorder=4)
for k in range(9):
    y = cy2 - 0.55 + k * 0.137
    ax.plot([4.5, 7.5], [y, y], color=P.fill(AIR), lw=1.6, zorder=5)
bronchus(6.0, cy2 - 1.2, cy2 + 1.3)
for c, r in (((2.6, cy2 + 0.6), 0.75), ((3.0, cy2 - 0.9), 0.65), ((9.2, cy2 + 0.5), 0.75), ((9.6, cy2 - 0.9), 0.95)):
    bio.shape(ax, vs.oval(c, r, r * 0.7), token=SAC, zorder=3, lw=0.8)
bio.label(ax, (2.8, cy2 - 2.0), "cranial air sacs", size="tiny")
bio.label(ax, (9.5, cy2 - 2.2), "caudal air sacs", size="tiny")
bio.callout(ax, (7.0, cy2 + 0.3), (8.6, cy2 + 2.0), "parabronchi", size="tiny")
title(17.5, 5.2, "F  Mammal: bronchial tree and alveoli")


def branch(x, y, ang, ln, depth):
    if depth == 0:
        bio.shape(ax, vs.oval((x, y), 0.17, 0.17), token=EX, zorder=6, lw=0.5)
        return
    x2, y2 = x + ln * np.cos(ang), y + ln * np.sin(ang)
    ax.plot([x, x2], [y, y2], color=P.edge(AIR), lw=0.8 + depth * 0.7, zorder=5, solid_capstyle="round")
    for d in (-0.45, 0.45):
        branch(x2, y2, ang + d, ln * 0.72, depth - 1)


branch(17.0, 4.6, -np.pi / 2, 1.1, 5)
bio.callout(ax, (15.75, 1.75), (13.6, 0.6), "alveoli", size="tiny")
lx = 19.5
for tok, txt in ((AIR, "airway lumen"), (EX, "exchange tissue"), (SAC, "air sacs (no exchange)")):
    pass
for i, (tok, txt) in enumerate(((AIR, "airway lumen"), (EX, "gas-exchange tissue"), (SAC, "air sac (no exchange)"))):
    yy = 3.6 - i * 0.6
    bio.shape(ax, np.array([(21.4, yy), (21.85, yy), (21.85, yy + 0.32), (21.4, yy + 0.32)]), token=tok, lw=0.6)
    bio.label(ax, (22.0, yy + 0.16), txt, size="tiny", ha="left")
