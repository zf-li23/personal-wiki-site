# Virion architecture: the four structural classes.
# A helical rod (tobacco mosaic virus, drawn as a stack of capsomere discs around a helical RNA);
# B icosahedral shells with triangulation numbers T = 1, 3 and 4, built as geodesic arrangements of
#   capsomeres (12 pentamers at the icosahedral vertices, 10(T-1) hexamers at face centres or edge
#   midpoints) and projected orthographically, with 60T subunits in all;
# C a complex virion (phage T4: prolate head, contractile tail, baseplate and fibres);
# D an enveloped virion (influenza A: lipid bilayer with haemagglutinin and neuraminidase spikes,
#   M2 channels, an M1 layer and eight helical ribonucleoprotein segments).
# Sizes in nanometres are given for each; the drawings are not to a common scale.
import itertools
import math

import numpy as np
from matplotlib.patches import Circle, PathPatch, Polygon
from matplotlib.path import Path

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(34, 11.2)
INK, MUT = P.ink(), P.muted()


def title(x, y, t, sub):
    bio.label(ax, (x, y), t, size="title", bold=True, ha="left")
    bio.label(ax, (x, y - 0.62), sub, size="small", ha="left", color=MUT)


# ---------------------------------------------------------------- A: helical, TMV
bio.panel(ax, "A", (0.2, 10.9))
title(0.9, 10.7, "Helical", "tobacco mosaic virus, 300 × 18 nm")
x0, xc, y0 = 1.0, 7.4, 6.3
half = 1.35
n = 26
step = (xc - x0) / n
for i in range(n + 1):
    x = x0 + i * step
    cut = i > n - 9  # the last turns are cut away to show the RNA and the hollow core
    col = P.fill("protein")
    ec = P.edge("protein")
    if not cut:
        ax.add_patch(Polygon([(x, y0 - half), (x + step * 0.92, y0 - half), (x + step * 0.92, y0 + half), (x, y0 + half)],
                             closed=True, facecolor=col, edgecolor=ec, lw=0.7, zorder=5))
    else:
        for sgn in (1, -1):
            ax.add_patch(Polygon([(x, y0 + sgn * 0.42), (x + step * 0.92, y0 + sgn * 0.42),
                                  (x + step * 0.92, y0 + sgn * half), (x, y0 + sgn * half)],
                                 closed=True, facecolor=col, edgecolor=ec, lw=0.7, zorder=5))
# hollow core and the RNA helix in the cut-away part
xs = np.linspace(x0 + (n - 8.5) * step, xc, 240)
ax.plot(xs, y0 + 0.30 * np.sin(2 * np.pi * (xs - xs[0]) / (2.1 * step)), color=P.edge("rna") if not P.is_dark() else P.fill("rna"),
        lw=2.0, zorder=7, solid_capstyle="round")
bio.callout(ax, (x0 + 6 * step, y0 + 1.0), (2.2, 9.2), "capsomere: 2130 identical subunits,\n16⅓ per turn")
bio.callout(ax, (xc - 1.0, y0 + 0.3), (3.0, 3.9), "(+) RNA, 6395 nt, three per subunit")
bio.callout(ax, (xc - 0.2, y0), (5.3, 2.9), "hollow 4 nm core")
bio.label(ax, (4.2, 8.2), "length set by the genome", size="small", color=MUT)
bio.scale_bar(ax, (1.0, 1.9), (300 / 300) * 6.4, "300 nm")

# ---------------------------------------------------------------- B: icosahedral shells
bio.panel(ax, "B", (8.9, 10.9))
title(9.6, 10.7, "Icosahedral", "60T subunits: 12 pentamers + 10(T − 1) hexamers")

PHI = (1 + 5 ** 0.5) / 2
_v = []
for a, b in itertools.product((-1, 1), (-PHI, PHI)):
    _v += [(0, a, b), (a, b, 0), (b, 0, a)]
V = np.array(_v, float)
V /= np.linalg.norm(V[0])
FACES = [f for f in itertools.combinations(range(12), 3)
         if all(abs(np.linalg.norm(V[i] - V[j]) - np.linalg.norm(V[0] - V[1])) < 1e-6 for i, j in itertools.combinations(f, 2))]
EDGES = sorted({tuple(sorted(e)) for f in FACES for e in itertools.combinations(f, 2)})


def shell(cx, cy, T, r=1.6, label=""):
    """Capsomere positions of a T = 1, 3 or 4 shell, drawn in orthographic projection."""
    pent = [(v, True) for v in V]
    hexa = []
    if T == 3:
        hexa = [(V[list(f)].mean(axis=0), False) for f in FACES]
    elif T == 4:
        hexa = [((V[i] + V[j]) / 2, False) for i, j in EDGES]
    pts = pent + hexa
    th = math.radians(20)
    R = np.array([[math.cos(th), 0, math.sin(th)], [0, 1, 0], [-math.sin(th), 0, math.cos(th)]])
    R2 = np.array([[1, 0, 0], [0, math.cos(th), -math.sin(th)], [0, math.sin(th), math.cos(th)]])
    ax.add_patch(Circle((cx, cy), r * 1.02, facecolor=P.mix(P.light("virus"), P.surface(), 0.55),
                        edgecolor=P.mix(P.edge("virus"), P.surface(), 0.6), lw=0.6, zorder=4))
    out = []
    for p, is_pent in pts:
        q = R2 @ (R @ (p / np.linalg.norm(p)))
        out.append((q[2], q[0] * r + cx, q[1] * r + cy, is_pent))
    for z, x, y, is_pent in sorted(out):
        depth = 0.45 + 0.55 * (z + 1) / 2
        tok = "channel" if is_pent else "virus"
        rad = r * 0.19 * (0.78 + 0.22 * depth)
        ax.add_patch(Circle((x, y), rad, facecolor=P.mix(P.fill(tok), P.light("virus"), 1 - depth),
                            edgecolor=P.edge(tok), lw=0.6 * depth + 0.2, zorder=5 + z))
    bio.label(ax, (cx, cy - r - 0.65), f"$T$ = {T}", size="normal")
    bio.label(ax, (cx, cy - r - 1.25), f"{10 * T + 2} capsomeres\n{60 * T} subunits", size="tiny", color=MUT)
    bio.label(ax, (cx, cy - r - 2.25), label, size="tiny", color=MUT)


shell(11.3, 7.0, 1, label="φX174\n(ssDNA phage)")
shell(15.1, 7.0, 3, label="poliovirus\n(pseudo-$T$ = 3)")
shell(18.9, 7.0, 4, label="hepatitis B\ncapsid")
bio.label(ax, (11.3, 2.0), "pentamers at the twelve\nfivefold vertices (blue)", size="tiny", color=MUT)
bio.label(ax, (17.0, 2.0), "hexamers between them; larger shells (herpesvirus $T$ = 16, adenovirus $T$ = 25,\n"
                           "$Mimivirus$ $T$ near 1000) need a scaffold, a portal vertex and a maturation step",
          size="tiny", color=MUT)

# ---------------------------------------------------------------- C: complex, phage T4
bio.panel(ax, "C", (21.0, 10.9))
title(21.7, 10.7, "Complex", "phage T4: head 85 × 115 nm")
hx, hy = 23.6, 7.6
head = np.array([[-1.0, -1.35], [-1.0, 0.75], [0, 1.5], [1.0, 0.75], [1.0, -1.35], [0, -2.0]])
ax.add_patch(Polygon(head + [hx, hy], closed=True, facecolor=P.fill("virus"), edgecolor=P.edge("virus"), lw=1.1, zorder=6))
for yy in (-0.7, 0.0, 0.7):  # facets
    ax.plot([hx - 1.0, hx + 1.0], [hy + yy, hy + yy], color=P.edge("virus"), lw=0.4, zorder=7)
ax.plot([hx, hx], [hy - 2.0, hy + 1.5], color=P.edge("virus"), lw=0.4, zorder=7)
ax.add_patch(Polygon([[hx - 0.42, hy - 2.05], [hx + 0.42, hy - 2.05], [hx + 0.42, hy - 2.35], [hx - 0.42, hy - 2.35]],
                     closed=True, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.8, zorder=7))
for yy in np.arange(hy - 2.45, hy - 4.55, -0.26):  # sheath rings around the tube
    ax.add_patch(Polygon([[hx - 0.40, yy], [hx + 0.40, yy], [hx + 0.40, yy - 0.2], [hx - 0.40, yy - 0.2]], closed=True,
                         facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.5, zorder=6))
ax.plot([hx, hx], [hy - 2.4, hy - 4.9], color=P.edge("neutral"), lw=1.6, zorder=5)
ax.add_patch(Polygon([[hx - 0.75, hy - 4.75], [hx + 0.75, hy - 4.75], [hx + 0.5, hy - 5.1], [hx - 0.5, hy - 5.1]],
                     closed=True, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.9, zorder=7))
for s in (-1, 1):
    ax.plot([hx + s * 0.6, hx + s * 1.55, hx + s * 1.9], [hy - 5.05, hy - 4.5, hy - 5.6], color=P.edge("enzyme"), lw=1.0, zorder=6)
    ax.plot([hx + s * 0.35, hx + s * 0.75], [hy - 5.1, hy - 5.6], color=P.edge("protein"), lw=1.0, zorder=6)
bio.callout(ax, (hx - 0.7, hy + 0.6), (21.4, 9.4), "prolate icosahedral head:\n169 kbp of dsDNA")
bio.callout(ax, (hx + 0.40, hy - 3.2), (25.3, 5.0), "contractile sheath\naround the tail tube")
bio.callout(ax, (hx + 0.5, hy - 4.95), (25.3, 3.4), "baseplate")
bio.callout(ax, (hx + 1.6, hy - 4.6), (25.3, 2.3), "long and short tail fibres")

# ---------------------------------------------------------------- D: enveloped, influenza
bio.panel(ax, "D", (27.4, 10.9))
title(28.0, 10.7, "Enveloped", "influenza A virus, about 100 nm")
cx, cy, r = 30.4, 5.6, 2.5
for a in np.arange(0, 360, 11):  # spikes: HA trimers (triangles) and NA tetramers (mushrooms)
    t = math.radians(a)
    p = np.array([cx + r * math.cos(t), cy + r * math.sin(t)])
    d = np.array([math.cos(t), math.sin(t)])
    n_ = np.array([-d[1], d[0]])
    if a % 44 == 0:
        ax.plot(*np.c_[p, p + 0.55 * d], color=P.edge("enzyme"), lw=1.1, zorder=6)
        ax.add_patch(Circle(p + 0.68 * d, 0.16, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"), lw=0.6, zorder=7))
    else:
        tip = p + 0.6 * d
        ax.add_patch(Polygon([p - 0.12 * n_, p + 0.12 * n_, tip + 0.2 * n_, tip - 0.2 * n_], closed=True,
                             facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.6, zorder=6))
ax.add_patch(Circle((cx, cy), r, facecolor=P.fill("lipid_head"), edgecolor=P.edge("lipid_head"), lw=1.0, zorder=5))
ax.add_patch(Circle((cx, cy), r - 0.30, facecolor=P.fill("extracellular"), edgecolor=P.edge("protein"), lw=1.6, zorder=5))
rng = np.random.default_rng(1)
for k, (dx, dy) in enumerate([(-1.1, 0.9), (-0.2, 1.2), (0.8, 0.8), (-1.3, -0.2), (-0.35, 0.1), (0.75, -0.25),
                              (-0.8, -1.1), (0.35, -1.15)]):  # eight RNP segments of different length
    L = 0.55 + 0.12 * (k % 4)
    t = np.linspace(0, 2 * math.pi * (2 + 0.3 * (k % 3)), 90)
    ax.plot(cx + dx + 0.14 * np.cos(t), cy + dy + np.linspace(-L, L, 90),
            color=P.edge("rna") if not P.is_dark() else P.fill("rna"), lw=1.1, zorder=7)
    ax.add_patch(Circle((cx + dx, cy + dy + L + 0.1), 0.1, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"),
                        lw=0.5, zorder=8))
for a in (28, 150, 255):  # M2 ion channels
    t = math.radians(a)
    ax.add_patch(Circle((cx + r * math.cos(t), cy + r * math.sin(t)), 0.17, facecolor=P.fill("channel"),
                        edgecolor=P.edge("channel"), lw=0.6, zorder=8))
bio.callout(ax, (cx - 1.75, cy - 1.95), (29.3, 1.2), "haemagglutinin (trimer):\nreceptor binding and fusion")
bio.callout(ax, (cx + 1.6, cy + 2.55), (32.6, 9.6), "neuraminidase")
bio.callout(ax, (cx + r * math.cos(math.radians(28)), cy + r * math.sin(math.radians(28))), (33.6, 7.4), "M2 channel")
bio.callout(ax, (cx + 2.3, cy - 1.1), (33.0, 4.0), "host lipid bilayer\nand the M1 layer")
bio.callout(ax, (cx + 0.35, cy - 1.15), (33.4, 2.5), "eight helical RNP segments,\neach with a polymerase")
