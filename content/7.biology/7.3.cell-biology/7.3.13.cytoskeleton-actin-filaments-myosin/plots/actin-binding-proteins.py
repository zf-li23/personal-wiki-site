"""The main classes of actin-binding proteins (schematic; filaments drawn minus end left, plus end right).

Monomer-binding proteins (thymosin beta4 sequesters ATP-actin; profilin delivers it to plus ends),
nucleators (formin rides on the plus end; the Arp2/3 complex, activated by a nucleation-promoting factor
such as WASP or WAVE at the membrane, branches at 70 degrees and caps the minus end), end-binding proteins
(capping protein on plus ends; tropomodulin on minus ends of tropomyosin-coated filaments), severing and
depolymerizing proteins (cofilin binds ADP-actin, twists and severs old filaments; gelsolin severs when
Ca2+ is high and caps the new plus end) and cross-linkers (fimbrin: tight parallel bundles; alpha-actinin:
loose contractile bundles that admit myosin II; filamin: orthogonal networks; ERM proteins: links to the
plasma membrane).
"""

import math

import numpy as np
from matplotlib.patches import Ellipse

import wikibio as bio
from wikibio import cytoskel as C

P = bio.P
W, H = 6.4, 3.6
fig, ax = bio.canvas(4 * W, 3 * H)
R = 0.085


def cell(i, j):
    return np.array([i * W, (2 - j) * H])


def title(o, text, sub):
    bio.label(ax, o + (0.3, H - 0.35), text, size="small", bold=True, ha="left")
    bio.label(ax, o + (0.3, 0.32), sub, size="tiny", ha="left", color=P.muted())


def monomer(p, state="T"):
    ax.add_patch(Ellipse(p, R * 2.3, R * 1.9, facecolor=C.state_color("actin", state), edgecolor=P.edge("actin"), lw=0.55,
                         zorder=10))


def blobp(p, token, w=0.28, h=0.22, text=None, seed=1):
    bio.protein(ax, p, w, h, token, text=text, size="tiny")


# 1 thymosin
o = cell(0, 0)
title(o, "Thymosin β4", "sequesters ATP-actin: no addition at either end")
for k in range(5):
    p = o + (0.9 + k * 1.1, 1.75 + 0.25 * math.sin(k))
    monomer(p)
    blobp(p + (0.0, 0.22), C.tok("thymosin"), 0.22, 0.14)
# 2 profilin
o = cell(1, 0)
title(o, "Profilin", "binds monomers, delivers them to plus ends")
C.actin_filament(ax, o + (0.4, 1.6), o + (3.8, 1.6), r=R, states="DDPT", ends=False)
for k, x in enumerate((4.6, 5.6)):
    p = o + (x, 1.6 + 0.35 * k)
    monomer(p)
    blobp(p + (0.2, 0.05), C.tok("profilin"), 0.24, 0.2)
bio.arrow(ax, o + (4.45, 1.95), o + (3.95, 1.7), kind="process", head=0.15, lw=0.9)
C.end_label(ax, o + (3.95, 1.25), "+", size="tiny")
# 3 formin
o = cell(2, 0)
title(o, "Formin", "nucleates and rides on the growing plus end")
f = C.actin_filament(ax, o + (0.4, 1.6), o + (4.2, 1.6), r=R, states="DDPTT", ends=False)
blobp(o + (4.45, 1.6), C.tok("formin"), 0.36, 0.5, text=None)
for k, dy in enumerate((0.75, -0.75)):
    pts = np.array([o + (4.5, 1.6 + dy * 0.3), o + (5.0, 1.6 + dy * 0.8), o + (5.6, 1.6 + dy * 0.9)])
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(C.tok("formin")), lw=0.9, zorder=9)
    monomer(pts[-1] + (0.15, 0))
    blobp(pts[-1] + (0.35, 0), C.tok("profilin"), 0.22, 0.18)
bio.label(ax, o + (5.0, 2.75), "FH1 + profilin-actin", size="tiny", color=P.muted())
# 4 Arp2/3
o = cell(3, 0)
title(o, "Arp2/3 complex + NPF", "branches at 70°; caps the daughter's minus end")
C._membrane_line(ax, [o + (0.3, 2.75), o + (6.1, 2.75)], zorder=6)
C.branch(ax, o + (0.6, 1.0), o + (5.6, 2.2), at=0.35, length=1.55, side=1, detailed=True, r=R * 0.9)
blobp(o + (3.3, 2.48), C.tok("adaptor"), 0.5, 0.26, text=None)
bio.label(ax, o + (3.7, 2.2), "WASP / WAVE", size="tiny", ha="left")
# 5 capping protein
o = cell(0, 1)
title(o, "Capping protein (CapZ)", "blocks addition and loss at the plus end")
C.actin_filament(ax, o + (0.4, 1.6), o + (5.4, 1.6), r=R, states="DDDDP", ends=False)
C.cap(ax, o + (5.4, 1.6), (1, 0), size=0.16)
C.end_label(ax, o + (5.95, 1.6), "+", size="tiny")
# 6 tropomyosin / tropomodulin
o = cell(1, 1)
title(o, "Tropomyosin, tropomodulin", "stabilize the side and cap the minus end")
fil = C.actin_filament(ax, o + (0.7, 1.6), o + (5.8, 1.6), r=R, states="D", ends=False)
xs = np.linspace(0.75, 5.75, 120)
ax.plot(o[0] + xs, o[1] + 1.6 + 0.09 * np.sin(xs * 2 * math.pi / (13 * R * 1.05)), color=P.edge("lipid"), lw=1.6, zorder=11)
blobp(o + (0.5, 1.6), "metabolite", 0.28, 0.32)
# 7 cofilin
o = cell(2, 1)
title(o, "Cofilin (ADF)", "binds ADP-actin, twists and severs old filaments")
C.actin_filament(ax, o + (0.4, 1.6), o + (2.8, 1.6), r=R, states="D", ends=False)
C.actin_filament(ax, o + (3.2, 1.6), o + (5.8, 1.6), r=R, states="DDPPTT", ends=False)
for x in np.arange(0.6, 2.8, 0.38):
    blobp(o + (x, 1.85), C.tok("cofilin"), 0.18, 0.13)
blobp(o + (3.45, 1.88), C.tok("cofilin"), 0.18, 0.13)
bio.label(ax, o + (3.0, 1.05), "severed", size="tiny", color=P.muted())
# 8 gelsolin
o = cell(3, 1)
title(o, "Gelsolin", "Ca²⁺-activated: severs, then caps the new plus end")
C.actin_filament(ax, o + (0.4, 1.6), o + (2.7, 1.6), r=R, states="D", ends=False)
C.actin_filament(ax, o + (3.4, 1.6), o + (5.8, 1.6), r=R, states="D", ends=False)
blobp(o + (2.95, 1.6), C.tok("gelsolin"), 0.42, 0.48)
bio.ion(ax, o + (2.95, 2.3), "ca", r=0.15)
# 9 fimbrin
o = cell(0, 2)
title(o, "Fimbrin (plastin), villin, fascin", "tight parallel bundle: microvilli, filopodia")
for k in range(4):
    y = 1.15 + k * 0.32
    C.filament(ax, o + (0.5, y), o + (5.6, y), lw=1.8)
for x in np.arange(0.8, 5.5, 0.45):
    ax.plot([o[0] + x] * 2, [o[1] + 1.15, o[1] + 2.11], color=P.edge(C.tok("fascin")), lw=1.0, zorder=9)
# 10 alpha-actinin
o = cell(1, 2)
title(o, "α-Actinin", "loose antiparallel bundle: room for myosin II")
for k, (a, b) in enumerate((((0.5, 1.1), (5.6, 1.1)), ((5.6, 1.85), (0.5, 1.85)), ((0.5, 2.6), (5.6, 2.6)))):
    C.filament(ax, o + a, o + b, lw=1.8)
for x in np.arange(1.0, 5.4, 0.9):
    for y0 in (1.1, 1.85):
        p0, p1 = o + (x, y0 + 0.08), o + (x, y0 + 0.67)
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.edge(C.tok("actinin")), lw=2.4, solid_capstyle="round", zorder=9)
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=P.fill(C.tok("actinin")), lw=1.2, solid_capstyle="round", zorder=9.1)
# 11 filamin
o = cell(2, 2)
title(o, "Filamin", "joins filaments at wide angles: a gel")
c0 = o + (3.1, 1.75)
for ang in (20, 105, 160, 65):
    d = np.array([math.cos(math.radians(ang)), math.sin(math.radians(ang))])
    C.filament(ax, c0 - d * 1.15 + (ang - 90) * 0.004, c0 + d * 1.15, lw=1.6)
for p in (c0 + (0.1, 0.05), c0 + (-0.55, -0.5), c0 + (0.6, 0.55)):
    ax.plot([p[0] - 0.22, p[0], p[0] + 0.22], [p[1] + 0.18, p[1] - 0.1, p[1] + 0.18], color=P.edge(C.tok("filamin")), lw=2.2,
            solid_joinstyle="round", zorder=10)
# 12 ERM
o = cell(3, 2)
title(o, "ERM proteins, spectrin", "link filaments to the plasma membrane")
C._membrane_line(ax, [o + (0.3, 2.5), o + (6.1, 2.5)], zorder=6)
C.filament(ax, o + (0.6, 1.25), o + (5.6, 1.25), lw=1.8)
for x in (1.5, 3.1, 4.7):
    ax.plot([o[0] + x, o[0] + x + 0.15], [o[1] + 1.33, o[1] + 2.4], color=P.edge("enzyme"), lw=1.3, zorder=9)
    blobp(o + (x + 0.08, 1.85), "enzyme", 0.26, 0.2)
    ax.plot([o[0] + x + 0.15] * 2, [o[1] + 2.4, o[1] + 2.75], color=P.edge("receptor"), lw=2.2, zorder=13)
