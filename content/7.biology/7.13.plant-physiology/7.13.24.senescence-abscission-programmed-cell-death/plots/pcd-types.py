# Types of programmed cell death in plants (schematic, three stages each, left to right).
# A: vacuolar cell death, e.g. a xylem tracheary element: the secondary wall is laid down, the central
#    vacuole swells with hydrolases, the tonoplast ruptures and the protoplast is digested (autolysis),
#    leaving a hollow cell with its wall.
# B: hypersensitive response (a necrotic-like death): around a pathogen, a burst of reactive oxygen
#    species, the protoplast shrinks away from the wall and the cell collapses within hours; the
#    vacuole ruptures late.
# C: autophagy in senescing cells: autophagosomes enclose cytoplasm and chloroplast fragments and
#    deliver them to the vacuole, recycling nutrients while the cell is still alive.
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Rectangle

import wikibio as bio

fig, ax = bio.canvas(21, 14.6)
P = bio.P
W, H = 4.4, 2.9


def wall(x, y, thick=False):
    ax.add_patch(FancyBboxPatch((x, y), W, H, boxstyle="round,pad=0,rounding_size=0.25", facecolor="none",
                                edgecolor=P.edge("cell_wall"), lw=3.2 if thick else 1.8, zorder=4))
    if thick:
        for k in range(1, 8):
            xx = x + k * W / 8
            ax.plot([xx, xx], [y + 0.05, y + H - 0.05], color=P.edge("cell_wall"), lw=2.0, zorder=4)


def proto(x, y, shrink=0.0, token="cytoplasm"):
    s = 0.12 + shrink
    ax.add_patch(FancyBboxPatch((x + s, y + s), W - 2 * s, H - 2 * s, boxstyle="round,pad=0,rounding_size=0.2",
                                facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.9, zorder=2))


def vac(x, y, w, h, broken=False):
    ax.add_patch(Ellipse((x, y), w, h, facecolor=P.fill("vacuole"), edgecolor=P.edge("vacuole"), lw=1.0,
                         ls="--" if broken else "-", zorder=3))


def chloro(x, y, s=1.0):
    ax.add_patch(Ellipse((x, y), 0.6 * s, 0.32 * s, facecolor=P.fill("chloroplast"), edgecolor=P.edge("chloroplast"),
                         lw=0.7, zorder=5))


def nuc(x, y, r=0.28, frag=False):
    if frag:
        for dx, dy in ((-0.15, 0), (0.12, 0.1), (0.05, -0.15)):
            ax.add_patch(Circle((x + dx, y + dy), 0.11, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"),
                                lw=0.6, zorder=5))
    else:
        ax.add_patch(Circle((x, y), r, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=0.8, zorder=5))


rows = [("A", "Vacuolar cell death (xylem tracheary element)", 10.6),
        ("B", "Hypersensitive response (necrotic-like)", 6.0),
        ("C", "Autophagy in a senescing cell", 1.4)]
xs = [2.6, 9.2, 15.8]
for letter, title, y in rows:
    bio.panel(ax, letter, (0.2, y + H + 0.9))
    bio.label(ax, (1.0, y + H + 0.62), title, size="normal", ha="left")
    for i in range(2):
        bio.arrow(ax, (xs[i] + W + 0.25, y + H / 2), (xs[i + 1] - 0.25, y + H / 2), kind="process")

# A: tracheary element
y = 10.6
x = xs[0]
proto(x, y)
vac(x + W / 2, y + H / 2, 2.2, 1.4)
nuc(x + 0.8, y + 0.7)
chloro(x + 3.6, y + 2.2)
wall(x, y)
bio.label(ax, (x + W / 2, y - 0.35), "differentiating cell", size="small")
x = xs[1]
proto(x, y)
vac(x + W / 2, y + H / 2, 3.6, 2.3)
nuc(x + 0.6, y + 0.5, r=0.22)
wall(x, y, thick=True)
bio.label(ax, (x + W / 2, y - 0.35), "secondary wall, vacuole swells", size="small")
x = xs[2]
vac(x + W / 2, y + H / 2, 3.9, 2.5, broken=True)
wall(x, y, thick=True)
bio.label(ax, (x + W / 2, y + H / 2), "autolysis", size="small", color=P.muted())
bio.label(ax, (x + W / 2, y - 0.35), "tonoplast ruptures: hollow cell", size="small")

# B: hypersensitive response
y = 6.0
x = xs[0]
proto(x, y)
vac(x + W / 2, y + H / 2, 2.4, 1.5)
nuc(x + 0.8, y + 0.7)
chloro(x + 3.5, y + 2.2)
chloro(x + 3.6, y + 0.6)
wall(x, y)
ax.add_patch(Ellipse((x - 0.35, y + 2.5), 0.7, 0.3, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"),
                     lw=0.8, zorder=6))
bio.label(ax, (x + W / 2, y - 0.35), "pathogen recognized", size="small")
x = xs[1]
proto(x, y, shrink=0.25)
vac(x + W / 2, y + H / 2, 2.0, 1.2)
nuc(x + 0.9, y + 0.8, frag=True)
chloro(x + 3.3, y + 2.0)
for dx, dy in ((0.9, 2.3), (2.2, 2.4), (3.4, 1.0), (1.4, 0.55)):
    bio.label(ax, (x + dx, y + dy), "ROS", size="tiny", bold=True, color=P.edge("negative"))
wall(x, y)
bio.label(ax, (x + W / 2, y - 0.35), "ROS burst, Ca²⁺ influx, shrinkage", size="small")
x = xs[2]
proto(x, y, shrink=0.85, token="negative")
nuc(x + W / 2 - 0.5, y + H / 2, frag=True)
wall(x, y)
bio.label(ax, (x + W / 2, y - 0.35), "collapse within hours", size="small")

# C: autophagy
y = 1.4
for i, x in enumerate(xs):
    proto(x, y)
    vac(x + W / 2 + 0.3, y + H / 2, 2.4 + 0.25 * i, 1.6 + 0.15 * i)
    nuc(x + 0.7, y + 0.7)
    wall(x, y)
x = xs[0]
for dx, dy in ((0.6, 2.3), (3.9, 2.3), (3.9, 0.55), (0.9, 1.7)):
    chloro(x + dx, y + dy)
bio.label(ax, (x + W / 2, y - 0.35), "starvation or senescence", size="small")
x = xs[1]
chloro(x + 0.6, y + 2.3)
ax.add_patch(Circle((x + 3.85, y + 2.25), 0.36, facecolor="none", edgecolor=P.edge("vesicle"), lw=1.4, zorder=6))
chloro(x + 3.85, y + 2.25, s=0.7)
ax.add_patch(Circle((x + 3.95, y + 0.6), 0.3, facecolor="none", edgecolor=P.edge("vesicle"), lw=1.4, zorder=6))
bio.label(ax, (x + W / 2, y - 0.35), "autophagosomes form", size="small")
x = xs[2]
for dx, dy in ((2.1, 1.7), (3.0, 1.3), (2.6, 2.0)):
    ax.add_patch(Circle((x + dx, y + dy), 0.18, facecolor=P.fill("chloroplast"), edgecolor=P.edge("vesicle"),
                        lw=0.8, zorder=6))
bio.label(ax, (x + W / 2, y - 0.35), "digested in the vacuole, recycled", size="small")
