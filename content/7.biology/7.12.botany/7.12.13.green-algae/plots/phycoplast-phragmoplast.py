"""Cytokinesis in green plants (schematic, telophase; spindle axis vertical, division plane horizontal).
A: phycoplast (Chlorophyceae, Trebouxiophyceae): the spindle collapses, the daughter nuclei lie close
together and a new array of microtubules forms parallel to the division plane; a furrow (or a cell
plate) forms along it. B: Ulvophyceae: closed mitosis with a persistent spindle, nuclei far apart,
cytokinesis by a furrow, no phycoplast. C: phragmoplast (Charophyceae, Coleochaetophyceae,
Zygnematophyceae, land plants): microtubules of the persistent spindle run perpendicular to the plane;
Golgi vesicles carried along them fuse into a cell plate that grows outwards to the parent wall."""
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 12.4)
MT = P.edge("protein")
W, H = 3.6, 4.4  # half width, half height of each cell


def frame(cx, cy, pinch=0.0):
    """Cell outline (wall + cytoplasm); pinch > 0 draws a cleavage furrow at mid-height."""
    t = np.linspace(0, 2 * np.pi, 200)
    x = W * np.cos(t)
    y = H * np.sin(t)
    x = x * (1 - pinch * np.exp(-(y / 0.9) ** 2))
    bio.shape(ax, np.c_[cx + x * 1.05, cy + y * 1.04], token="cell_wall", lw=1.1, zorder=2)
    bio.shape(ax, np.c_[cx + x, cy + y], token="cytoplasm", lw=0.8, zorder=3)


def nuclei(cx, cy, d, r=0.85):
    for s in (1, -1):
        bio.nucleus(ax, (cx, cy + s * d), r, pores=8, chromatin=True)


def head(cx, title, sub, groups):
    bio.label(ax, (cx, 11.75), title, size="normal", bold=True)
    bio.label(ax, (cx, 11.15), sub, size="small", color=P.muted())
    bio.label(ax, (cx, 0.45), groups, size="small", color=P.muted())


CY = 5.6
# A: phycoplast
cx = 5.0
bio.panel(ax, "A", (0.2, 12.2))
head(cx, "Phycoplast", "nuclei close, spindle collapsed", "Chlorophyceae, Trebouxiophyceae")
frame(cx, CY, pinch=0.28)
nuclei(cx, CY, 1.25, r=0.75)
for k in range(-4, 5):
    y = CY + k * 0.06
    ax.plot([cx - 2.5, cx + 2.5], [y, y], color=MT, lw=0.8, zorder=9)
bio.callout(ax, (cx + 1.6, CY), (cx + 0.6, CY - 3.4), "Microtubules parallel\nto the division plane", size="small")
bio.callout(ax, (cx - 2.65, CY), (cx - 3.0, CY + 3.6), "Furrow", size="small")

# B: Ulvophyceae
cx = 15.0
bio.panel(ax, "B", (10.2, 12.2))
head(cx, "Persistent spindle, furrow", "no phycoplast", "Ulvophyceae")
frame(cx, CY, pinch=0.45)
nuclei(cx, CY, 2.7, r=0.75)
for dx in np.linspace(-0.45, 0.45, 5):
    ax.plot([cx + dx * 0.6, cx + dx], [CY + 2.0, CY - 2.0], color=MT, lw=0.8, zorder=9)
bio.callout(ax, (cx + 0.28, CY + 1.0), (cx + 1.8, CY + 1.6), "Spindle", size="small")
bio.callout(ax, (cx - 2.0, CY), (cx - 2.6, CY + 3.0), "Furrow", size="small")

# C: phragmoplast
cx = 25.0
bio.panel(ax, "C", (20.2, 12.2))
head(cx, "Phragmoplast and cell plate", "nuclei far apart, spindle persists", "Streptophytes: advanced charophytes, land plants")
frame(cx, CY)
nuclei(cx, CY, 2.7, r=0.75)
for dx in np.linspace(-1.8, 1.8, 9):
    for s in (1, -1):
        ax.plot([cx + dx, cx + dx], [CY + s * 0.25, CY + s * 1.6], color=MT, lw=0.8, zorder=9)
bio.shape(ax, [[cx - 1.3, CY - 0.09], [cx + 1.3, CY - 0.09], [cx + 1.3, CY + 0.09], [cx - 1.3, CY + 0.09]], token="cell_wall",
          lw=0.8, zorder=10)
for dx in (-2.0, -1.65, 1.65, 2.0, -2.35, 2.35):
    bio.vesicle(ax, (cx + dx, CY), 0.13, token="golgi")
for s in (-1, 1):
    bio.arrow(ax, (cx + s * 2.6, CY + 0.5), (cx + s * 3.4, CY + 0.5), kind="process", head=0.16, color=P.muted())
bio.callout(ax, (cx + 1.8, CY - 1.2), (cx + 0.8, CY - 3.5), "Microtubules perpendicular\nto the division plane", size="small")
bio.callout(ax, (cx - 0.6, CY), (cx - 2.4, CY + 3.6), "Cell plate", size="small")
bio.callout(ax, (cx - 2.35, CY), (cx - 3.2, CY - 2.6), "Golgi vesicles", size="small")
