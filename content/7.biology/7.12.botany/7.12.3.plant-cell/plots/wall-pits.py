"""Layers of the cell wall and the types of pits (schematic, not to scale).
A: a fibre-like cell with a secondary wall, in transverse section: middle lamella shared with the
neighbours, primary wall, the three layers S1, S2 (thickest) and S3 of the secondary wall, and the lumen
left by the dead protoplast. B: a primary pit field: a thin region of the primary wall crossed by
plasmodesmata. C to G: pit pairs in section between two cells with secondary walls; the pit membrane is the
two primary walls plus the middle lamella. C: simple pit pair (a canal of even width). D: bordered pit pair:
the secondary wall arches over the pit chamber and leaves a narrow aperture. E: half-bordered pit pair
(tracheid next to a parenchyma cell). F: bordered pit pair of a conifer tracheid with a torus (a thickened,
impermeable centre of the pit membrane) on a porous margo. G: aspirated pit: a pressure difference pushes
the membrane aside and the torus seals the aperture of the side with the lower pressure. H: face views:
a simple pit is one circle, a bordered pit two concentric circles (aperture inside the border), a bordered
pit with a torus three.
"""

import numpy as np
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch, Polygon, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 12.6)
ML, PW, SW = "lipid", "cell_wall", "plant"


def rect(x0, y0, x1, y1, tk, z=3, lw=0.6):
    ax.add_patch(Polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], closed=True, facecolor=P.fill(tk), edgecolor=P.edge(tk), lw=lw, zorder=z))


def rrect(c, w, h, tk, r=0.3, z=3, lw=0.8):
    ax.add_patch(FancyBboxPatch((c[0] - w / 2, c[1] - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                facecolor=P.fill(tk), edgecolor=P.edge(tk), lw=lw, zorder=z))


# --- A: wall layers in transverse section
bio.panel(ax, "A", (0.1, 12.5))
c = (3.6, 6.9)
rrect(c, 6.6, 7.4, ML, r=0.9, z=1)
rrect(c, 6.3, 7.1, PW, r=0.8, z=2)
rrect(c, 5.9, 6.7, "ovule", r=0.7, z=3)      # S1
rrect(c, 5.6, 6.4, SW, r=0.6, z=4)           # S2
rrect(c, 3.6, 4.4, "bone", r=0.45, z=5)      # S3
rrect(c, 3.3, 4.1, "extracellular", r=0.4, z=6)  # lumen
# S2 microfibrils at a steep angle, S1 and S3 nearly transverse (hatching)
for x in np.linspace(c[0] - 2.4, c[0] + 2.4, 13):
    ax.plot([x - 0.15, x + 0.15], [c[1] + 3.05, c[1] + 2.25], color=P.edge(SW), lw=0.5, zorder=4.5)
bio.label(ax, (c[0], c[1]), "Lumen", size="small", color=P.muted())
items = [((c[0] + 3.28, c[1] + 2.0), "Middle lamella"), ((c[0] + 3.08, c[1] + 1.2), "Primary wall"),
         ((c[0] + 2.88, c[1] + 0.4), "S1"), ((c[0] + 2.3, c[1] - 0.4), "S2"), ((c[0] + 1.72, c[1] - 1.2), "S3")]
for p, t in items:
    bio.callout(ax, p, (8.0, p[1]), t, size="tiny")
bio.label(ax, (8.95, c[1] - 0.4), "secondary wall", size="tiny", color=P.muted(), ha="left")
ax.plot([8.75, 8.75], [c[1] - 1.35, c[1] + 0.55], color=P.muted(), lw=0.7, zorder=19)

# --- B: primary pit field with plasmodesmata
bio.panel(ax, "B", (0.1, 2.9))
y = 1.3
ax.add_patch(Polygon([(0.6, y - 0.45), (2.6, y - 0.45), (3.2, y - 0.14), (4.6, y - 0.14), (5.2, y - 0.45), (7.2, y - 0.45),
                      (7.2, y + 0.45), (5.2, y + 0.45), (4.6, y + 0.14), (3.2, y + 0.14), (2.6, y + 0.45), (0.6, y + 0.45)],
                     closed=True, facecolor=P.fill(PW), edgecolor=P.edge(PW), lw=0.8, zorder=3))
ax.plot([0.6, 7.2], [y, y], color=P.edge(ML), lw=0.8, zorder=4)
for x in np.linspace(3.35, 4.45, 5):
    ax.plot([x, x], [y - 0.32, y + 0.32], color=P.edge("membrane"), lw=1.0, zorder=5)
bio.callout(ax, (3.9, y + 0.2), (5.9, 2.6), "Primary pit field", size="tiny")
bio.callout(ax, (4.45, y - 0.25), (6.6, 0.25), "Plasmodesmata", size="tiny")


# --- C to G: pit pairs in section
def pit_pair(x, y0, y1, left="simple", right="simple", torus=None, title=""):
    ym = (y0 + y1) / 2
    # pit membrane: two primary walls and the middle lamella, continuous
    off = 0.0
    if torus == "aspirated":
        off = -0.42
    t = np.linspace(y0, y1, 80)
    bulge = off * np.exp(-((t - ym) / 0.55) ** 2)
    for sgn, w in ((-1, 0.17), (1, 0.17)):
        xs = x + bulge + sgn * np.linspace(0, 0, 80)
    ax.fill_betweenx(t, x + bulge - 0.17, x + bulge + 0.17, color=P.fill(PW), lw=0, zorder=3)
    ax.plot(x + bulge - 0.17, t, color=P.edge(PW), lw=0.6, zorder=3.2)
    ax.plot(x + bulge + 0.17, t, color=P.edge(PW), lw=0.6, zorder=3.2)
    ax.plot(x + bulge, t, color=P.edge(ML), lw=0.8, zorder=3.3)
    if torus:
        tx = x + (off if torus == "aspirated" else 0)
        ax.add_patch(Ellipse((tx, ym), 0.36, 0.8, facecolor=P.fill(PW), edgecolor=P.edge(PW), lw=0.9, zorder=3.5))
        ax.add_patch(Ellipse((tx, ym), 0.18, 0.6, facecolor=P.edge(PW), edgecolor="none", zorder=3.6))
    for side, kind in ((-1, left), (1, right)):
        x_in = x + side * 0.17          # surface of the primary wall
        x_out = x + side * 1.0          # lumen surface of the secondary wall
        if kind == "none":
            continue
        if kind == "simple":
            a = 0.32
            for s in (-1, 1):
                ya, yb = (ym + a, y1) if s > 0 else (y0, ym - a)
                ax.add_patch(Polygon([(x_in, ya), (x_out, ya), (x_out, yb), (x_in, yb)], closed=True,
                                     facecolor=P.fill(SW), edgecolor=P.edge(SW), lw=0.6, zorder=4))
        else:  # bordered: chamber half-height b at the membrane, aperture half-height a at the lumen
            b, a = 0.95, 0.2
            for s in (-1, 1):
                if s > 0:
                    pts = [(x_in, y1), (x_in, ym + b), (x_in + side * 0.25, ym + b * 0.82), (x_out - side * 0.12, ym + a + 0.12),
                           (x_out, ym + a), (x_out, y1)]
                else:
                    pts = [(x_in, y0), (x_in, ym - b), (x_in + side * 0.25, ym - b * 0.82), (x_out - side * 0.12, ym - a - 0.12),
                           (x_out, ym - a), (x_out, y0)]
                ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(SW), edgecolor=P.edge(SW), lw=0.6, zorder=4))
    bio.label(ax, (x, y1 + 0.45), title, size="tiny")


Y0, Y1 = 4.4, 9.6
xs = (13.0, 16.3, 19.6, 22.9, 26.2)
specs = (("simple", "simple", None, "C  Simple pit pair"), ("bordered", "bordered", None, "D  Bordered pit pair"),
         ("bordered", "simple", None, "E  Half-bordered pair"), ("bordered", "bordered", "open", "F  With torus (open)"),
         ("bordered", "bordered", "aspirated", "G  Aspirated pit"))
for x, (l, r, t, title) in zip(xs, specs):
    pit_pair(x, Y0, Y1, l, r, t, title)
bio.callout(ax, (13.0, 8.6), (11.0, 11.0), "Pit membrane", size="tiny")
bio.callout(ax, (12.45, 7.0), (11.0, 3.6), "Pit canal", size="tiny")
bio.callout(ax, (16.75, 7.0), (14.8, 11.0), "Pit chamber", size="tiny")
bio.callout(ax, (17.3, 7.1), (18.0, 11.0), "Aperture", size="tiny")
bio.callout(ax, (16.3 + 0.9, 8.2), (17.9, 3.6), "Border (secondary wall)", size="tiny")
bio.callout(ax, (22.9, 7.25), (21.3, 11.0), "Torus", size="tiny")
bio.callout(ax, (22.9, 6.1), (24.4, 3.6), "Margo", size="tiny")
bio.label(ax, (27.6, 7.0), "high", size="tiny", color=P.muted())
bio.label(ax, (24.75, 7.0), "low", size="tiny", color=P.muted())
bio.label(ax, (26.2, 3.9), "pressure", size="tiny", color=P.muted())
bio.label(ax, (12.0, 4.05), "cell 1", size="tiny", color=P.muted())
bio.label(ax, (14.0, 4.05), "cell 2", size="tiny", color=P.muted())

# --- H: face views
bio.panel(ax, "H", (10.4, 2.9))
yf = 1.35
ax.add_patch(Circle((13.0, yf), 0.38, facecolor=P.fill("extracellular"), edgecolor=P.edge(SW), lw=1.0, zorder=4))
for x, rings in ((16.3, (0.75, 0.2)), (22.9, (0.75, 0.42, 0.2))):
    ax.add_patch(Circle((x, yf), rings[0], facecolor=P.fill(SW), edgecolor=P.edge(SW), lw=1.0, zorder=4))
    if len(rings) == 3:
        ax.add_patch(Circle((x, yf), rings[1], facecolor=P.fill(PW), edgecolor=P.edge(PW), lw=0.9, zorder=4.5))
    ax.add_patch(Circle((x, yf), rings[-1], facecolor=P.fill("extracellular"), edgecolor=P.edge(SW), lw=0.9, zorder=5))
bio.label(ax, (13.0, 0.4), "simple pit", size="tiny", color=P.muted())
bio.label(ax, (16.3, 0.25), "bordered pit", size="tiny", color=P.muted())
bio.label(ax, (22.9, 0.25), "bordered pit with torus", size="tiny", color=P.muted())
bio.label(ax, (19.6, 1.35), "face views", size="tiny", color=P.muted())
