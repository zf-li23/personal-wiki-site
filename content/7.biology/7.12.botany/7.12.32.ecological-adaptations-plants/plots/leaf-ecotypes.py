"""Transverse sections of leaves from three water regimes, built cell by cell (wikibio.botany).
A xerophyte (Nerium type): thick cuticle, multiple epidermis on both sides, several layers of palisade,
compact spongy tissue, a stomatal crypt with trichomes and stomata at its bottom. B mesophyte: ordinary
dorsiventral C3 leaf. C submerged leaf (Potamogeton type): a few cell layers, thin epidermis with
chloroplasts and no stomata, undifferentiated mesophyll with large air lacunae (aerenchyma), a much
reduced vein.
"""
import numpy as np
from matplotlib.patches import Polygon

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(25.0, 20.4)
X0, W = 0.6, 15.0
LX = W + 1.4


def clip(x0, y0, w, h):
    return Polygon([(x0, y0 - 0.05), (x0 + w, y0 - 0.05), (x0 + w, y0 + h + 0.05), (x0, y0 + h + 0.05)], closed=True,
                   transform=ax.transData, facecolor="none", edgecolor="none")


def labels(items, y0, y1):
    items = sorted(items, key=lambda t: -t[0][1])
    for k, (p, name) in enumerate(items):
        y = y0 - k * (y0 - y1) / max(1, len(items) - 1)
        bio.callout(ax, p, (LX, y), name)


# ---------------------------------------------------------------- A: xerophyte
x0, y0, h = X0, 12.9, 6.0
x1, y1 = x0 + W, y0 + h
S = B.Section(7)
e = 0.32
pad = 1.0
xa, xb = x0 - pad, x1 + pad
crypts = [x0 + 3.2, x0 + 9.0, x0 + 13.6]
cw, cd = 1.5, 1.45  # crypt width and depth

for k in range(3):  # upper multiple epidermis
    S.row(xa, xb, y1 - e * (k + 0.5), e, "epidermis", spacing=e * 1.25, jitter=0.15)
for k in range(2):  # palisade layers
    S.row(xa, xb, y1 - 3 * e - 0.55 - k * 1.05, 1.0, "palisade", spacing=0.34)


def in_crypt(x, y, grow=0.0):
    return any(abs(x - c) < cw / 2 + grow for c in crypts) and y < y0 + cd + grow


for k in range(2):  # lower multiple epidermis, interrupted by the crypts
    for x in np.arange(xa, xb, e * 1.25) + e * 0.4:
        y = y0 + e * (k + 0.5)
        if not in_crypt(x, y, 0.15):
            S.add([x, y], e, "epidermis")
for c in crypts:  # crypt lining: one layer of epidermal cells, guard cells at the bottom, air inside
    for yy in np.arange(y0 + 0.15, y0 + cd, e * 1.1):
        for s in (-1, 1):
            S.add([c + s * (cw / 2 + e * 0.35), yy], e * 0.9, "epidermis")
    for xx in np.arange(c - cw / 2 + 0.25, c + cw / 2 - 0.2, e * 1.2):
        if abs(xx - c) > 0.35:
            S.add([xx, y0 + cd + e * 0.4], e * 0.9, "epidermis")
    S.add([[c - 0.17, y0 + cd + e * 0.35], [c + 0.17, y0 + cd + e * 0.35]], e * 0.75, "guard")
    for xx in np.linspace(c - cw / 2 + 0.2, c + cw / 2 - 0.2, 5):
        for yy in np.linspace(y0 + 0.2, y0 + cd - 0.15, 4):
            S.add([xx, yy], 0.3, "air")
vx, vy = x0 + 6.2, y0 + 2.3
S.ring((vx, vy), 0.75, 0.28, "sheath", spacing=0.27)
S.add([[vx - 0.15, vy + 0.15], [vx + 0.15, vy + 0.15], [vx, vy + 0.35]], 0.2, "xylem")
top_meso = y1 - 3 * e - 2.1


def tissue(pts):
    tags, sizes = [], []
    for x, y in pts:
        dv = np.hypot(x - vx, y - vy)
        if y > top_meso or y < y0 + 2 * e + 0.05 or in_crypt(x, y, 0.3):
            tags.append(None), sizes.append(1)
        elif dv < 0.55:
            tags.append("phloem" if y < vy else "xylem_parenchyma"), sizes.append(0.13)
        elif dv < 0.95:
            tags.append(None), sizes.append(1)
        else:
            tags.append("air" if np.random.random() < 0.04 else "spongy"), sizes.append(0.32)
    return tags, sizes


np.random.seed(2)
S.fill((xa, y0, xb, y1), tissue, 0.12)
S.mirror_line(y1, above=True)
S.mirror_line(y0, above=False)
S.box_ghosts((xa - pad, y0 - h, xb + pad, y1 + h), 1.0)
S.draw(ax, clip=clip(x0, y0, W, h), zorder=5)
ax.plot([x0, x1], [y1, y1], color=P.edge(B.tok("epidermis")), lw=3.2, zorder=7, solid_capstyle="butt")
segs = [x0] + sum([[c - cw / 2 - e * 0.7, c + cw / 2 + e * 0.7] for c in crypts], []) + [x1]
for a, b in zip(segs[::2], segs[1::2]):
    ax.plot([a, b], [y0, y0], color=P.edge(B.tok("epidermis")), lw=3.2, zorder=7, solid_capstyle="butt")
for c in crypts:  # trichomes inside the crypts
    for s in (-1, 1):
        for yy in (y0 + 0.4, y0 + 0.85):
            ax.plot([c + s * cw / 2, c + s * (cw / 2 - 0.5)], [yy, yy - 0.25], color=P.edge(B.tok("epidermis")), lw=1.0, zorder=8)
bio.panel(ax, "A", (0.2, 20.2))
bio.label(ax, (0.85, 20.17), "Xerophyte (Nerium type)", size="title", ha="left", va="top")
labels([((x0 + 12.5, y1), "Thick cuticle"), ((x0 + 12.0, y1 - 0.5), "Multiple epidermis"),
        ((x0 + 12.0, y1 - 1.6), "Palisade, several layers"), ((x0 + 11.0, y0 + 2.4), "Compact spongy tissue"),
        ((vx + 0.75, vy), "Vein"), ((crypts[2] - 0.4, y0 + 0.9), "Trichomes in crypt"),
        ((crypts[2], y0 + cd + 0.1), "Stomata in crypt")], 19.5, 13.1)

# ---------------------------------------------------------------- B: mesophyte
bio.panel(ax, "B", (0.2, 12.1))
bio.label(ax, (0.85, 12.07), "Mesophyte (dorsiventral leaf)", size="title", ha="left", va="top")
m = B.leaf_anatomy(ax, (X0, 6.6, W, 4.2), kind="C3", veins=2)
labels([(m["cuticle"], "Thin cuticle"), (m["upper_epidermis"], "Single epidermis"), (m["palisade"], "Palisade, one layer"),
        (m["spongy"], "Spongy mesophyll"), (m["guard_cell"], "Stoma")], 11.4, 6.7)

# ---------------------------------------------------------------- C: submerged leaf
x0, y0, h = X0, 0.8, 3.4
x1, y1 = x0 + W, y0 + h
S = B.Section(11)
e = 0.42
xa, xb = x0 - 1.0, x1 + 1.0
S.row(xa, xb, y1 - e / 2, e, "epidermis", spacing=e * 1.1)
S.row(xa, xb, y0 + e / 2, e, "epidermis", spacing=e * 1.1)
vx = x0 + 7.5
lac = [x for x in np.arange(xa + 0.6, xb, 1.55) if abs(x - vx) > 1.1]
ym = 0.5 * (y0 + y1)
for x in lac:  # air lacunae separated by one-cell partitions
    for dx in (-0.35, 0.35):
        for yy in np.linspace(y0 + e + 0.55, y1 - e - 0.55, 3):
            S.add([x + dx, yy], 0.45, "air")
for x in np.arange(xa + 0.6 - 0.78, xb, 1.55):
    if abs(x - vx) > 0.8:
        for yy in np.linspace(y0 + e + 0.45, y1 - e - 0.45, 5):
            S.add([x, yy], 0.4, "mesophyll")
for x in np.arange(xa, xb, 0.45):  # a layer of mesophyll along both epidermes
    if abs(x - vx) > 0.9:
        S.add([x, y1 - e - 0.25], 0.4, "mesophyll")
        S.add([x, y0 + e + 0.25], 0.4, "mesophyll")
S.ring((vx, ym), 0.55, 0.3, "sheath", spacing=0.3)
S.add([vx, ym + 0.05], 0.4, "air")
S.add([[vx - 0.22, ym - 0.28], [vx + 0.22, ym - 0.28]], 0.17, "phloem")
for x in (vx - 0.95, vx + 0.95):
    for yy in np.linspace(y0 + e + 0.25, y1 - e - 0.25, 4):
        S.add([x, yy], 0.42, "mesophyll")
S.mirror_line(y1, above=True)
S.mirror_line(y0, above=False)
S.box_ghosts((xa - 1, y0 - h, xb + 1, y1 + h), 1.0)
S.draw(ax, clip=clip(x0, y0, W, h), zorder=5, style={"epidermis": ("cell_wall", 0.7, 0.06, 0, 0.7)})
bio.panel(ax, "C", (0.2, 5.6))
bio.label(ax, (0.85, 5.57), "Submerged leaf (Potamogeton type)", size="title", ha="left", va="top")
labels([((x0 + 12.4, y1 - 0.2), "Epidermis with chloroplasts, no cuticle"), ((lac[-3], ym), "Air lacuna (aerenchyma)"),
        ((lac[-3] + 0.75, ym + 0.4), "Undifferentiated mesophyll"), ((vx + 0.4, ym), "Reduced vein"),
        ((x0 + 13.0, y0 + 0.2), "No stomata")], 5.0, 0.9)
