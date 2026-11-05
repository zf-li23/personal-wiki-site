"""Sporophytes of a liverwort, a moss and a hornwort (schematic longitudinal sections, not to scale).
A: Marchantia: foot, short seta, capsule with a one-layered wall, spores and elaters, no columella; the
calyptra, pseudoperianth and involucre are gametophyte tissue. B: Funaria: foot, long seta, capsule with
operculum, peristome and annulus, urn with a central columella and the spore sac around it, apophysis
with stomata; calyptra on top. C: hornwort: foot in the thallus, no seta, a long capsule growing from a
basal meristem, central columella, spores and multicellular pseudoelaters, stomata, splitting into two
valves from the top."""
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 16)
GAM = "plant"      # gametophyte tissue
SPO = "animal"     # sporophyte wall
SPORE = "lipid"


def ell(c, rx, ry, a0=0, a1=360, n=60):
    t = np.radians(np.linspace(a0, a1, n))
    return np.c_[c[0] + rx * np.cos(t), c[1] + ry * np.sin(t)]


def dots(x0, x1, y0, y1, n, seed):
    rng = np.random.default_rng(seed)
    for _ in range(n):
        bio.shape(ax, ell((rng.uniform(x0, x1), rng.uniform(y0, y1)), 0.07, 0.07), token=SPORE, lw=0.3, zorder=9)


def elaters(x0, x1, y0, y1, n, seed, multi=False):
    rng = np.random.default_rng(seed)
    for _ in range(n):
        x, y = rng.uniform(x0, x1), rng.uniform(y0, y1)
        a = rng.uniform(0, np.pi)
        t = np.linspace(-0.3, 0.3, 20)
        ax.plot(x + t * np.cos(a), y + t * np.sin(a) + 0.04 * np.sin(t * 40), color=P.edge(SPO), lw=0.8, zorder=9)
        if multi:
            for s in (-0.1, 0.1):
                ax.plot([x + s * np.cos(a) - 0.04 * np.sin(a)] * 2, [y + s * np.sin(a) - 0.06, y + s * np.sin(a) + 0.06],
                        color=P.edge(SPO), lw=0.6, zorder=9)


def head(x, t, sub):
    bio.label(ax, (x, 15.4), t, size="normal", bold=True)
    bio.label(ax, (x, 14.8), sub, size="small", color=P.muted(), italic=True)


# ---------------- A: Marchantia (hanging under the receptacle) ----------------
bio.panel(ax, "A", (0.2, 15.8))
head(4.6, "Liverwort", "Marchantia")
xa = 4.6
bio.shape(ax, [[1.0, 13.4], [8.2, 13.4], [8.2, 12.6], [1.0, 12.6]], token=GAM, lw=1.0, zorder=3)
bio.label(ax, (2.0, 13.0), "receptacle (n)", size="tiny", color=P.on_fill())
bio.shape(ax, ell((xa, 12.4), 0.5, 0.45), token="receptor", lw=0.9, zorder=6)  # foot
bio.shape(ax, [[xa - 0.22, 12.1], [xa + 0.22, 12.1], [xa + 0.22, 10.9], [xa - 0.22, 10.9]], token="receptor", lw=0.9, zorder=6)
bio.shape(ax, ell((xa, 9.5), 1.9, 1.75, 0, 360), token=GAM, lw=0.9, zorder=3)  # pseudoperianth
bio.shape(ax, ell((xa, 9.4), 1.55, 1.5), token="bone", lw=0.9, zorder=4)    # calyptra
bio.shape(ax, ell((xa, 9.4), 1.25, 1.25), token=SPO, lw=1.0, zorder=5)
bio.shape(ax, ell((xa, 9.4), 1.12, 1.12), token="cytoplasm", lw=0.5, zorder=6)
dots(xa - 0.8, xa + 0.8, 8.7, 10.1, 40, 1)
elaters(xa - 0.8, xa + 0.8, 8.7, 10.1, 9, 2)
bio.callout(ax, (xa + 0.45, 12.4), (7.6, 11.9), "Foot", size="small")
bio.callout(ax, (xa + 0.22, 11.4), (7.6, 11.2), "Short seta", size="small")
bio.callout(ax, (xa + 1.85, 9.9), (7.6, 10.4), "Pseudoperianth (n)", size="small")
bio.callout(ax, (xa + 1.45, 8.9), (7.6, 8.4), "Calyptra (n)", size="small")
bio.callout(ax, (xa + 0.3, 9.6), (7.6, 7.4), "Spores and elaters", size="small")
bio.callout(ax, (xa - 1.25, 9.0), (1.0, 6.8), "Capsule wall:\none cell layer", size="small")
bio.label(ax, (xa, 6.0), "no columella, no stomata;\nseta elongates after the\ncapsule matures", size="small", color=P.muted())

# ---------------- B: Funaria ----------------
bio.panel(ax, "B", (10.2, 15.8))
head(15.0, "Moss", "Funaria")
xb = 14.4
bio.shape(ax, [[11.8, 1.2], [16.6, 1.2], [16.6, 2.6], [11.8, 2.6]], token=GAM, lw=1.0, zorder=3)
bio.label(ax, (12.8, 1.9), "gametophyte (n)", size="tiny", color=P.on_fill())
bio.shape(ax, ell((xb, 2.3), 0.25, 0.6), token="receptor", lw=0.8, zorder=5)
t = np.linspace(0, 1, 40)
sx = xb + 0.0 * t + 0.8 * t ** 3
sy = 2.8 + t * 7.0
ax.plot(sx, sy, color=P.edge("receptor"), lw=3.4, zorder=5)
ax.plot(sx, sy, color=P.fill("receptor"), lw=2.0, zorder=5.1)
# capsule (tilted) drawn upright for clarity
cx, cy = xb + 0.8, 11.6
bio.shape(ax, [[cx - 0.5, cy - 1.8], [cx + 0.5, cy - 1.8], [cx + 0.85, cy - 1.0], [cx - 0.85, cy - 1.0]], token="chloroplast",
          lw=0.9, zorder=6)  # apophysis
bio.shape(ax, ell((cx, cy), 1.1, 1.2), token=SPO, lw=1.0, zorder=6)  # urn wall
bio.shape(ax, ell((cx, cy), 0.85, 0.95), token=SPORE, lw=0.6, zorder=7)  # spore sac
bio.shape(ax, ell((cx, cy - 0.05), 0.3, 0.8), token="bone", lw=0.6, zorder=8)  # columella
dots(cx - 0.75, cx - 0.35, cy - 0.6, cy + 0.6, 12, 3)
dots(cx + 0.35, cx + 0.75, cy - 0.6, cy + 0.6, 12, 4)
bio.shape(ax, ell((cx, cy + 1.25), 0.85, 0.45, 0, 180).tolist() + [[cx - 0.85, cy + 1.25]], token="bone", lw=0.9, zorder=9)  # operculum
for k in range(7):
    xx = cx - 0.6 + k * 0.2
    ax.plot([xx, xx + 0.05], [cy + 0.95, cy + 1.3], color=P.edge("antibody"), lw=1.4, zorder=10)  # peristome
bio.shape(ax, [[cx - 0.4, cy + 1.6], [cx + 0.4, cy + 1.6], [cx + 1.1, cy + 0.3], [cx + 1.0, cy + 1.9], [cx, cy + 2.6],
               [cx - 0.5, cy + 2.0]], token=GAM, lw=0.9, zorder=4)  # calyptra (behind)
for sx_ in (cx - 0.35, cx + 0.35):
    bio.shape(ax, ell((sx_, cy - 1.6), 0.08, 0.05), token="neutral", lw=0.5, zorder=8)
bio.callout(ax, (cx + 0.6, cy + 2.2), (cx + 2.4, cy + 2.6), "Calyptra (n)", size="small")
bio.callout(ax, (cx + 0.5, cy + 1.45), (cx + 2.4, cy + 1.8), "Operculum", size="small")
bio.callout(ax, (cx + 0.4, cy + 1.15), (cx + 2.4, cy + 1.0), "Peristome teeth", size="small")
bio.callout(ax, (cx + 0.55, cy + 0.2), (cx + 2.4, cy + 0.2), "Spore sac", size="small")
bio.callout(ax, (cx, cy - 0.4), (cx + 2.4, cy - 0.6), "Columella", size="small")
bio.callout(ax, (cx + 0.35, cy - 1.6), (cx + 2.4, cy - 1.6), "Apophysis with stomata", size="small")
bio.callout(ax, (sx[20], sy[20]), (sx[20] + 2.2, sy[20]), "Seta (long, firm)", size="small")
bio.callout(ax, (xb + 0.2, 2.5), (xb + 3.4, 3.4), "Foot", size="small")

# ---------------- C: hornwort ----------------
bio.panel(ax, "C", (21.6, 15.8))
head(25.4, "Hornwort", "Anthoceros")
xc = 25.4
bio.shape(ax, [[22.2, 1.2], [28.6, 1.2], [28.6, 2.8], [22.2, 2.8]], token=GAM, lw=1.0, zorder=3)
bio.label(ax, (23.4, 1.6), "thallus (n)", size="tiny", color=P.on_fill())
bio.shape(ax, ell((xc, 1.9), 0.6, 0.55), token="receptor", lw=0.9, zorder=5)  # foot
bio.shape(ax, [[xc - 0.75, 2.8], [xc - 0.55, 3.8], [xc + 0.55, 3.8], [xc + 0.75, 2.8]], token=GAM, lw=0.9, zorder=4)  # involucre
H0, H1 = 2.5, 13.2
W = 0.55
top = [[xc - W, H0], [xc - W, H1 - 0.6], [xc - 0.25, H1], [xc - 0.05, H1 - 0.8]]
# two valves splitting at the top
bio.shape(ax, [[xc - W, H0], [xc + W, H0], [xc + W, 11.2], [xc + 0.75, H1], [xc + 0.2, 11.6], [xc - 0.2, 11.6], [xc - 0.75, H1],
               [xc - W, 11.2]], token=SPO, lw=1.0, zorder=6)
bio.shape(ax, [[xc - 0.36, 3.2], [xc + 0.36, 3.2], [xc + 0.36, 11.4], [xc - 0.36, 11.4]], token="cytoplasm", lw=0.5, zorder=7)
bio.shape(ax, [[xc - 0.1, 3.2], [xc + 0.1, 3.2], [xc + 0.1, 12.4], [xc - 0.1, 12.4]], token="bone", lw=0.6, zorder=9)  # columella
dots(xc - 0.33, xc - 0.12, 7.0, 11.3, 20, 5)
dots(xc + 0.12, xc + 0.33, 7.0, 11.3, 20, 6)
elaters(xc - 0.3, xc + 0.3, 7.5, 11.0, 6, 7, multi=True)
bio.shape(ax, [[xc - W, 2.9], [xc + W, 2.9], [xc + W, 3.4], [xc - W, 3.4]], token="highlight", lw=0.8, zorder=8)  # meristem
for yy in (5.0, 7.0, 9.0):
    bio.shape(ax, ell((xc + W, yy), 0.08, 0.14), token="neutral", lw=0.5, zorder=8)
bio.callout(ax, (xc + 0.5, 12.4), (xc + 1.8, 13.2), "Dehisces into two valves", size="small")
bio.callout(ax, (xc, 12.0), (xc - 1.8, 13.0), "Columella", size="small")
bio.callout(ax, (xc + 0.25, 9.8), (xc + 1.8, 10.4), "Spores, pseudoelaters", size="small")
bio.callout(ax, (xc + W, 7.0), (xc + 1.8, 7.0), "Stoma", size="small")
bio.callout(ax, (xc - 0.2, 6.0), (xc - 1.8, 6.5), "Immature\nsporogenous tissue", size="small")
bio.callout(ax, (xc + 0.4, 3.15), (xc + 1.8, 4.4), "Basal meristem", size="small")
bio.callout(ax, (xc + 0.5, 1.8), (xc + 1.8, 0.6), "Foot", size="small")
