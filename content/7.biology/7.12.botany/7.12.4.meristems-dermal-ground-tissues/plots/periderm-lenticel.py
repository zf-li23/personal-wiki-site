"""Periderm and a lenticel in transverse section of a young woody stem (schematic, built cell by cell).
Outside in: the remains of the epidermis with its cuticle; cork (phellem), several layers of flat,
suberized dead cells in radial files; the cork cambium (phellogen), one layer of thin-walled dividing
cells; the phelloderm, one or two layers of living cells in the same radial files; and the cortex. On the
right a lenticel: there the phellogen lies deeper and is more active, and produces loosely packed,
rounded complementary cells with large intercellular spaces, which push up and break the epidermis and
let air in.
"""

import math

import numpy as np

import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(22.0, 9.0)
sec = B.Section(seed=11)
XC, HW = 15.2, 2.6           # lenticel centre and half-width
W = 0.55                      # width of a radial file


def depth(x):
    """How far the phellogen dips below its normal level under the lenticel."""
    u = (x - XC) / HW
    return 1.0 * max(0.0, 1 - u * u) ** 1.2


Y_PD, Y_PG, Y_CK = 2.7, 3.35, 3.7
cols = np.arange(0.3, 21.8, W)
for x in cols:
    d = depth(x)
    sec.add([x, Y_PD - 0.3 - d], 0.36, "parenchyma")
    sec.add([x, Y_PD + 0.02 - d], 0.36, "parenchyma")
    sec.add([x, Y_PG - d], 0.32, "phellogen")
    if d < 0.05:
        for k in range(6):
            sec.add([x, Y_CK + k * 0.32], 0.34, "cork")
        sec.add([x, Y_CK + 6 * 0.32 + 0.05], 0.36, "epidermis")
        sec.add([x, Y_CK + 6 * 0.32 + 0.45], 0.36, "ghost")
# complementary cells of the lenticel: loose, rounded, filling the lens above the phellogen
rng = np.random.default_rng(2)
for x in np.arange(XC - HW + 0.25, XC + HW - 0.2, 0.42):
    d = depth(x)
    top = Y_CK + 6 * 0.32 + 0.9 * max(0.0, 1 - ((x - XC) / HW) ** 2) ** 0.7
    y = Y_PG - d + 0.42
    while y < top:
        sec.add([x + rng.uniform(-0.06, 0.06), y], 0.4, "filling")
        y += 0.42
    sec.add([x, y + 0.3], 0.4, "ghost")


def cortex(pts):
    ok = pts[:, 1] < Y_PD - 0.55 - np.array([depth(x) for x in pts[:, 0]])
    return [("cortex" if o else None) for o in ok], np.full(len(pts), 0.75)


sec.fill((0.0, 0.0, 22.0, 2.4), cortex, 0.7)
sec.box_ghosts((0.0, 0.0, 22.0, 6.6), 0.45)
style = {"cork": ("cork", 0.6, 0.04, 0, 0), "phellogen": ("cambium", 0.6, 0.05, 0, 0),
         "filling": ("cork", 0.6, 0.28, 0, 0), "parenchyma": ("parenchyma", 0.5, 0.06, 0, 0.5)}
sec.draw(ax, style=style)
ax.set_xlim(0, 22)
ax.set_ylim(0, 9)
# cuticle over the epidermis remnants, broken above the lenticel
ytop = Y_CK + 6 * 0.32 + 0.25
for xa, xb in ((0.05, XC - HW + 0.35), (XC + HW - 0.35, 21.95)):
    ax.plot([xa, xb], [ytop, ytop], color=P.edge("lipid"), lw=2.0, zorder=8)

bio.callout(ax, (4.0, ytop), (2.0, 8.3), "Cuticle and epidermis (sloughing)", size="small")
bio.callout(ax, (5.2, Y_CK + 0.9), (7.4, 8.3), "Cork (phellem)", size="small")
bio.callout(ax, (6.8, Y_PG), (8.6, 7.4), "Cork cambium (phellogen)", size="small")
bio.callout(ax, (3.5, Y_PD), (0.8, 7.4), "Phelloderm", size="small")
bio.callout(ax, (2.4, 1.0), (0.8, 6.6), "Cortex", size="small")
bio.callout(ax, (XC, Y_CK + 1.6), (19.2, 8.3), "Lenticel: complementary cells", size="small")
bio.callout(ax, (XC + 1.0, Y_PG - depth(XC + 1.0)), (19.4, 7.4), "Lenticel phellogen", size="small")
bio.label(ax, (21.6, 0.35), "outside up", size="tiny", color=P.muted(), ha="right")
