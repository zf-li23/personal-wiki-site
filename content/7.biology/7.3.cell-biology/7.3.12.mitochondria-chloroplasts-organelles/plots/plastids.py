"""Plastid types, their interconversions and plastid division (schematic, not to scale).
(A) All plastids of a plant develop from proplastids of meristems. In light, proplastids become chloroplasts;
in darkness, etioplasts with a paracrystalline prolamellar body, which turn into chloroplasts within hours of
illumination. Proplastids also become amyloplasts (starch storage, gravity sensing in root caps), elaioplasts
(lipid storage) and other leucoplasts. Chloroplasts become chromoplasts (carotenoid-rich) when fruits ripen
and gerontoplasts in senescent leaves; several conversions are reversible (dashed).
(B) Division of a chloroplast: a ring of FtsZ1/FtsZ2 assembles inside, on the stromal side of the inner
envelope, and is linked across the envelope (ARC6, PDV1/2) to an outer ring of the dynamin-related protein
ARC5 (DRP5B) and the polyglucan outer plastid-dividing (PD) ring on the cytosolic side."""

import numpy as np

import wikibio as bio

P = bio.P
FT = bio.core.FONT
fig, ax = bio.canvas(23.0, 10.0, scale=0.42)


def ellipse(c, rx, ry, n=100):
    a = np.linspace(0, 2 * np.pi, n)
    return np.c_[c[0] + rx * np.cos(a), c[1] + ry * np.sin(a)]


def envelope(c, rx, ry, token, fill=None):
    bio.shape(ax, ellipse(c, rx, ry), token, lw=1.1, zorder=6)
    bio.shape(ax, ellipse(c, rx - 0.09, ry - 0.09), fill or token, lw=0.6, zorder=7)


def proplastid(c):
    envelope(c, 0.55, 0.4, "plant", fill="cytoplasm")
    for dx in (-0.15, 0.12):
        ax.plot([c[0] + dx - 0.15, c[0] + dx + 0.15], [c[1] + 0.05 * np.sign(dx), c[1] + 0.05 * np.sign(dx)],
                color=P.edge("thylakoid"), lw=0.9, zorder=8)


def etioplast(c):
    envelope(c, 0.95, 0.6, "lipid", fill="cytoplasm")
    for i in range(4):
        for j in range(4):
            ax.plot([c[0] - 0.3 + 0.2 * i], [c[1] - 0.3 + 0.2 * j], "o", color=P.edge("lipid"), ms=2.4, zorder=9)
    for i in range(4):
        ax.plot([c[0] - 0.3, c[0] + 0.3], [c[1] - 0.3 + 0.2 * i] * 2, color=P.edge("lipid"), lw=0.5, zorder=8)
        ax.plot([c[0] - 0.3 + 0.2 * i] * 2, [c[1] - 0.3, c[1] + 0.3], color=P.edge("lipid"), lw=0.5, zorder=8)
    for s in (-1, 1):
        ax.plot([c[0] + s * 0.38, c[0] + s * 0.75], [c[1], c[1]], color=P.edge("thylakoid"), lw=0.9, zorder=8)


def amyloplast(c):
    envelope(c, 0.9, 0.7, "carbohydrate", fill="cytoplasm")
    for (dx, dy, r) in ((-0.3, 0.15, 0.26), (0.28, 0.2, 0.22), (0.0, -0.25, 0.25)):
        bio.shape(ax, ellipse((c[0] + dx, c[1] + dy), r, r * 0.85), "carbohydrate", lw=0.7, zorder=8)


def chromoplast(c):
    envelope(c, 0.95, 0.6, "drug", fill="cytoplasm")
    rng = np.random.default_rng(4)
    for _ in range(12):
        p = (c[0] + rng.uniform(-0.6, 0.6), c[1] + rng.uniform(-0.3, 0.3))
        ax.add_patch(bio.core.Circle(p, 0.07, facecolor=P.fill("drug"), edgecolor=P.edge("drug"), lw=0.4, zorder=8))
    ax.plot([c[0] - 0.45, c[0] + 0.1], [c[1] - 0.15, c[1] + 0.25], color=P.edge("drug"), lw=2.2, zorder=8)


def elaioplast(c):
    envelope(c, 0.75, 0.55, "lipid", fill="cytoplasm")
    rng = np.random.default_rng(7)
    for _ in range(6):
        p = (c[0] + rng.uniform(-0.35, 0.35), c[1] + rng.uniform(-0.2, 0.2))
        ax.add_patch(bio.core.Circle(p, 0.13, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.5, zorder=8))


def gerontoplast(c):
    envelope(c, 0.85, 0.55, "neutral", fill="cytoplasm")
    for dx in (-0.25, 0.25):
        ax.plot([c[0] + dx - 0.2, c[0] + dx + 0.2], [c[1] + 0.1, c[1] + 0.1], color=P.edge("thylakoid"), lw=0.8, zorder=8)
    for p in ((c[0] - 0.3, c[1] - 0.2), (c[0] + 0.1, c[1] - 0.22), (c[0] + 0.4, c[1] - 0.1)):
        ax.add_patch(bio.core.Circle(p, 0.09, facecolor=P.fill("lipid"), edgecolor=P.edge("lipid"), lw=0.4, zorder=8))


bio.panel(ax, "A", (0.1, 9.9))
pos = {"pro": (2.4, 5.0), "chl": (7.2, 7.0), "etio": (4.6, 8.6), "amy": (4.6, 1.7), "ela": (2.0, 2.5),
       "chr": (11.8, 8.4), "ger": (11.8, 5.6)}
proplastid(pos["pro"])
bio.chloroplast(ax, pos["chl"], 2.2, 1.2)
etioplast(pos["etio"])
amyloplast(pos["amy"])
elaioplast(pos["ela"])
chromoplast(pos["chr"])
gerontoplast(pos["ger"])
names = {"pro": ("Proplastid", "meristem", (0, -0.8)), "chl": ("Chloroplast", "photosynthesis", (0, -1.05)),
         "etio": ("Etioplast", "dark-grown seedling", (0, -0.95)), "amy": ("Amyloplast", "starch; statoliths", (0, -1.05)),
         "ela": ("Elaioplast", "lipids", (0, -0.9)), "chr": ("Chromoplast", "carotenoids; fruits, petals", (0, -0.95)),
         "ger": ("Gerontoplast", "senescence", (0, -0.9))}
names["pro"] = ("Proplastid", "meristem", (-0.7, 0.15))
for k, (n, sub, (dx, dy)) in names.items():
    x, y = pos[k]
    ha = "right" if k == "pro" else "center"
    bio.label(ax, (x + dx, y + dy), n, size="small", bold=True, ha=ha)
    bio.label(ax, (x + dx, y + dy - 0.38), sub, size="tiny", color=P.muted(), ha=ha)
A = dict(kind="process", head=0.16)
bio.arrow(ax, (2.95, 5.25), (5.9, 6.65), **A)
bio.label(ax, (4.1, 6.35), "light", size="tiny", color=P.muted())
bio.arrow(ax, (2.6, 5.45), (3.75, 8.2), **A)
bio.label(ax, (2.6, 7.2), "dark", size="tiny", color=P.muted())
bio.arrow(ax, (5.6, 8.4), (6.6, 7.75), **A)
bio.label(ax, (6.6, 8.6), "light (hours)", size="tiny", color=P.muted())
bio.arrow(ax, (2.75, 4.65), (3.9, 2.3), **A)
bio.arrow(ax, (2.25, 4.6), (2.05, 3.15), **A)
bio.arrow(ax, (8.35, 7.4), (10.75, 8.2), **A)
bio.label(ax, (9.5, 8.25), "fruit ripening", size="tiny", color=P.muted())
bio.arrow(ax, (10.85, 8.0), (8.4, 7.2), dashed=True, bend=0.25, color=P.muted(), **A)
bio.arrow(ax, (8.35, 6.6), (10.9, 5.8), **A)
bio.label(ax, (9.6, 5.85), "senescence", size="tiny", color=P.muted())
bio.arrow(ax, (5.4, 2.2), (6.3, 6.45), dashed=True, color=P.muted(), **A)
bio.label(ax, (6.55, 3.8), "greening\nin light", size="tiny", color=P.muted(), ha="left")

# ---- B: division ---------------------------------------------------------------------------------------------
bio.panel(ax, "B", (14.4, 9.9))
cx, cy = 18.6, 5.2
xs = np.linspace(-3.2, 3.2, 200)
half = 1.5 * np.sqrt(np.clip(1 - (xs / 3.2) ** 2, 0, 1)) * (1 - 0.55 * np.exp(-(xs / 0.5) ** 2))
up = np.c_[cx + xs, cy + half]
lo = np.c_[cx + xs[::-1], cy - half[::-1]]
bio.shape(ax, np.vstack([up, lo]), "chloroplast", lw=1.3, zorder=5)
inner = np.vstack([np.c_[cx + xs * 0.95, cy + half * 0.88], np.c_[cx + xs[::-1] * 0.95, cy - half[::-1] * 0.88]])
bio.shape(ax, inner, "chloroplast", lw=0.7, zorder=6)
for s in (-1, 1):
    for k in range(3):
        bio.box(ax, (cx + s * 1.7, cy - 0.45 + 0.45 * k), 1.0, 0.16, "thylakoid", radius=0.06, lw=0.5, zorder=7)
yy = np.linspace(cy - half[100] * 0.85, cy + half[100] * 0.85, 7)
for y in yy:
    ax.add_patch(bio.core.Circle((cx - 0.06, y), 0.06, color=P.edge("positive"), lw=0, zorder=9))
yo = np.linspace(cy - half[100] - 0.18, cy + half[100] + 0.18, 9)
for y in yo:
    ax.add_patch(bio.core.Circle((cx + 0.08, y), 0.07, color=P.edge("negative"), lw=0, zorder=9))
bio.callout(ax, (cx - 0.06, cy + 0.3), (cx - 2.2, 8.4), "FtsZ ring (stroma side)", size="tiny")
bio.callout(ax, (cx + 0.08, cy + half[100] + 0.18), (cx + 1.6, 8.4), "ARC5/DRP5B and outer PD ring (cytosol)", size="tiny")
bio.callout(ax, (cx + 0.0, cy - 0.15), (cx + 1.2, 1.6), "ARC6, PDV1/2 link across the envelope", size="tiny")
bio.callout(ax, (cx - 1.7, cy + 0.45), (cx - 3.3, 1.8), "thylakoids", size="tiny")
bio.label(ax, (cx, 9.5), "Plastid division from inside and outside", size="small", bold=True)
