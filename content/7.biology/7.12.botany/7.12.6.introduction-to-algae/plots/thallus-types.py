"""Main types of algal thallus, roughly in order of complexity (schematic, not to scale). Top row:
motile unicell (Chlamydomonas type: two flagella, cup-shaped chloroplast, eyespot), non-motile unicell,
coenobium with a fixed number of cells in a common envelope (Pandorina type) and palmelloid colony with
cells scattered in mucilage (Microcystis type). Bottom row: uniseriate filament, branched heterotrichous
filament (prostrate and erect parts), siphonous coenocyte without cross walls (Vaucheria type), sheet one
or two cells thick (Ulva, Porphyra type) and parenchymatous thallus with holdfast, stipe and blade (kelp)."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Rectangle, Wedge, PathPatch
from matplotlib.path import Path
import wikibio as bio

P = bio.P
rng = np.random.default_rng(1)
fig, ax = bio.canvas(32, 15)
G = "chloroplast"


def cap(x, y, t):
    bio.label(ax, (x, y), t, size="small", bold=True)


def cellc(c, r, tok=G, z=5):
    ax.add_patch(Circle(c, r, facecolor=P.light(tok), edgecolor=P.edge(tok), lw=1.1, zorder=z))


def wave(p0, ang, L, amp=0.08):
    t = np.linspace(0, 1, 80)
    a = np.radians(ang)
    u, n = np.array([np.cos(a), np.sin(a)]), np.array([-np.sin(a), np.cos(a)])
    pts = p0 + np.outer(t * L, u) + np.outer(amp * np.sin(2 * np.pi * 2 * t) * np.minimum(1, 4 * t), n)
    ax.plot(pts[:, 0], pts[:, 1], color=P.ink(), lw=1.2, zorder=8)


# --- top row
y = 11.0
# motile unicell
ax.add_patch(Ellipse((3.5, y), 1.8, 2.4, facecolor=P.fill("cytoplasm"), edgecolor=P.edge(G), lw=1.3, zorder=4))
ax.add_patch(Wedge((3.5, y + 0.25), 0.95, 200, 340, width=0.4, facecolor=P.fill(G), edgecolor=P.edge(G), lw=0.8, zorder=5))
ax.add_patch(Circle((3.5, y - 0.6), 0.22, facecolor=P.fill("ovule"), edgecolor=P.edge(G), lw=0.8, zorder=6))
ax.add_patch(Circle((2.75, y + 0.45), 0.12, color=P.edge("negative"), zorder=7))
wave(np.array([3.35, y + 1.18]), 120, 1.6)
wave(np.array([3.65, y + 1.18]), 60, 1.6)
cap(3.5, y - 2.0, "Motile unicell")
# non-motile unicell
cellc((8.5, y), 1.0)
ax.add_patch(Wedge((8.5, y), 0.8, 120, 300, width=0.35, facecolor=P.fill(G), edgecolor=P.edge(G), lw=0.8, zorder=6))
cap(8.5, y - 2.0, "Non-motile unicell")
# coenobium
ax.add_patch(Circle((14.0, y), 1.45, facecolor=P.fill("extracellular"), edgecolor=P.muted(), lw=1.0, zorder=3))
for k in range(8):
    a = 2 * np.pi * k / 8
    cellc((14.0 + 0.85 * np.cos(a), y + 0.85 * np.sin(a)), 0.42)
for k in range(4):
    a = 2 * np.pi * k / 4 + 0.4
    cellc((14.0 + 0.3 * np.cos(a), y + 0.3 * np.sin(a)), 0.3, z=6)
cap(14.0, y - 2.0, "Coenobium (fixed colony)")
# palmelloid colony
t = np.linspace(0, 2 * np.pi, 60)
rr = 1.5 + 0.25 * np.sin(3 * t) + 0.15 * np.cos(5 * t)
ax.fill(19.8 + 1.2 * rr * np.cos(t), y + 0.8 * rr * np.sin(t), facecolor=P.fill("extracellular"), edgecolor=P.muted(), lw=1.0, zorder=3)
for _ in range(70):
    r, a = 1.3 * np.sqrt(rng.random()), 2 * np.pi * rng.random()
    cellc((19.8 + 1.25 * r * np.cos(a), y + 0.8 * r * np.sin(a)), 0.12, tok="bacterium")
cap(19.8, y - 2.0, "Palmelloid colony")
bio.label(ax, (26.5, y + 0.6), "unicells and colonies", size="normal", color=P.muted())
bio.label(ax, (26.5, y - 0.1), "(green algae, cyanobacteria,\nchrysophytes, dinoflagellates, ...)", size="tiny", color=P.muted())

# --- bottom row
y = 3.6
# uniseriate filament
for k in range(7):
    ax.add_patch(Rectangle((0.8 + 0.6 * k, y + 0.8), 0.6, 0.45, facecolor=P.light(G), edgecolor=P.edge(G), lw=1.0, zorder=5))
    ax.add_patch(Rectangle((0.8 + 0.6 * k + 0.08, y + 0.88), 0.44, 0.29, facecolor=P.fill(G), edgecolor="none", zorder=6))
cap(2.9, y - 2.0, "Filament")
# heterotrichous
for k in range(9):
    ax.add_patch(Rectangle((5.8 + 0.5 * k, y - 0.9), 0.5, 0.35, facecolor=P.light(G), edgecolor=P.edge(G), lw=0.9, zorder=5))
for x0, n in ((6.3, 6), (7.8, 8), (9.3, 5)):
    for k in range(n):
        ax.add_patch(Rectangle((x0, y - 0.55 + 0.45 * k), 0.32, 0.45, facecolor=P.light(G), edgecolor=P.edge(G), lw=0.9, zorder=5))
    for k in range(3):
        ax.add_patch(Rectangle((x0 + 0.32 + 0.38 * k, y - 0.55 + 0.45 * (n - 2) + 0.15 * k), 0.38, 0.28,
                               facecolor=P.light(G), edgecolor=P.edge(G), lw=0.9, zorder=5))
bio.label(ax, (10.6, y - 0.75), "prostrate", size="tiny", ha="left", color=P.muted())
bio.label(ax, (10.0, y + 2.6), "erect", size="tiny", ha="left", color=P.muted())
cap(8.0, y - 2.0, "Heterotrichous filament")
# siphonous
path = np.array([[12.8, y - 0.8], [13.4, y + 0.2], [13.6, y + 1.6], [14.4, y + 2.6]])
for seg in ([[12.8, y - 0.8], [13.5, y + 0.6], [13.6, y + 2.4]], [[13.5, y + 0.6], [14.6, y + 1.4], [15.6, y + 2.2]]):
    seg = np.array(seg)
    ax.plot(seg[:, 0], seg[:, 1], color=P.edge(G), lw=11, solid_capstyle="round", solid_joinstyle="round", zorder=4)
    ax.plot(seg[:, 0], seg[:, 1], color=P.light(G), lw=8.5, solid_capstyle="round", solid_joinstyle="round", zorder=5)
    for f in np.linspace(0.05, 0.95, 9):
        i = int(f * (len(seg) - 1))
        q = seg[i] + (seg[min(i + 1, len(seg) - 1)] - seg[i]) * ((f * (len(seg) - 1)) % 1)
        ax.add_patch(Circle(q + rng.normal(0, 0.04, 2), 0.06, color=P.edge("nucleus"), zorder=6))
cap(14.2, y - 2.0, "Siphonous coenocyte")
bio.label(ax, (14.2, y - 1.3), "many nuclei, no cross walls", size="tiny", color=P.muted())
# sheet
t = np.linspace(0, 2 * np.pi, 80)
sx = 19.6 + 1.7 * np.cos(t) * (1 + 0.12 * np.sin(4 * t))
sy = y + 0.9 + 2.0 * np.sin(t) * (1 + 0.08 * np.cos(3 * t))
ax.fill(sx, sy, facecolor=P.light(G), edgecolor=P.edge(G), lw=1.2, zorder=4)
for xx in np.arange(18.2, 21.2, 0.35):
    for yy in np.arange(y - 0.9, y + 2.8, 0.35):
        if ((xx - 19.6) / 1.6) ** 2 + ((yy - y - 0.9) / 1.85) ** 2 < 0.62:
            ax.add_patch(Rectangle((xx, yy), 0.3, 0.3, facecolor=P.fill(G), edgecolor="none", zorder=5))
cap(19.6, y - 2.0, "Sheet (1-2 cells thick)")
# kelp (drawn natively: holdfast, stipe, blade)
BR = "plant"
kx = 26.5
for a in (-60, -35, -15, 15, 35, 60):
    r = np.radians(a - 90)
    ax.plot([kx, kx + 0.9 * np.cos(r)], [y - 0.6, y - 0.6 + 0.6 * np.sin(r)], color=P.edge(BR), lw=2.2, solid_capstyle="round", zorder=5)
ax.add_patch(Rectangle((kx - 0.12, y - 0.6), 0.24, 1.3, facecolor=P.fill(BR), edgecolor=P.edge(BR), lw=1.0, zorder=5))
t = np.linspace(0, 1, 60)
w = 0.75 * np.sin(np.pi * t) ** 0.6
bx = np.r_[kx + w, (kx - w)[::-1]]
by = np.r_[y + 0.7 + 3.4 * t, (y + 0.7 + 3.4 * t)[::-1]]
ax.fill(bx, by, facecolor=P.light(BR), edgecolor=P.edge(BR), lw=1.2, zorder=4)
bio.callout(ax, (kx + 0.5, y + 2.6), (28.4, y + 2.6), "blade")
bio.callout(ax, (kx + 0.1, y + 0.2), (28.4, y + 0.2), "stipe")
bio.callout(ax, (kx + 0.6, y - 0.95), (28.4, y - 0.95), "holdfast")
cap(26.5, y - 2.0, "Parenchymatous thallus")
