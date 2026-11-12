# From bilateral larva to pentaradial juvenile in a sea star (schematic): coelomic sacs, the rudiment
# formed by the left hydrocoel and left somatocoel, metamorphosis and the juvenile water vascular system.
import numpy as np
import wikibio as bio
from matplotlib.patches import Polygon, Circle, Ellipse

P = bio.P
fig, ax = bio.canvas(27.0, 9.4)
AX, HY, SO = "drug", "channel", "positive"  # axocoel, hydrocoel, somatocoel


def oval(c, rx, ry, token, z=5, light=False, ls="-", angle=0):
    ax.add_patch(Ellipse(c, 2 * rx, 2 * ry, angle=angle, facecolor=P.light(token) if light else P.fill(token),
                         edgecolor=P.edge(token), lw=0.9, zorder=z, ls=ls))


def body(pts, z=2, ls="-"):
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.light("ectoderm"), edgecolor=P.edge("ectoderm"), lw=1.0,
                         zorder=z, ls=ls))


def lobes(c, r, n=5, k=0.28, start=90, z=6, token=HY, full=True):
    th = np.linspace(0, 2 * np.pi if full else 1.6 * np.pi, 400) + np.radians(start)
    rr = r * (1 + k * np.cos(n * (th - np.radians(start))))
    pts = np.c_[c[0] + rr * np.cos(th), c[1] + rr * np.sin(th)]
    ax.add_patch(Polygon(pts, closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.9, zorder=z))


def gut(x, y0, y1, w=0.22, z=4):
    ax.add_patch(Polygon([(x - w, y0), (x - w, y1), (x + w, y1), (x + w, y0)], closed=True,
                         facecolor=P.fill("endoderm"), edgecolor=P.edge("endoderm"), lw=0.8, zorder=z))


C = bio.callout
# ---------------------------------------------------------------- 1: early bipinnaria (ventral view)
bio.label(ax, (3.4, 9.0), "1  Bipinnaria (dorsal view)", size="normal", bold=True)
th = np.linspace(0, 2 * np.pi, 300)
body(np.c_[3.4 + 2.2 * np.cos(th), 4.6 + 3.2 * np.sin(th)])
gut(3.4, 2.0, 5.2)
oval((3.4, 5.8), 0.9, 0.6, "endoderm", z=4)
for s in (-1, 1):
    oval((3.4 + s * 1.15, 6.6), 0.42, 0.38, AX, light=s > 0)
    oval((3.4 + s * 1.2, 5.4), 0.38, 0.45, HY, light=s > 0)
    oval((3.4 + s * 1.05, 3.6), 0.4, 0.75, SO)
ax.plot([2.25, 2.0, 1.7], [6.9, 7.4, 7.65], color=P.edge(AX), lw=1.0, zorder=6)
bio.label(ax, (2.25, 8.5), "L", size="small", bold=True)
bio.label(ax, (4.55, 8.5), "R", size="small", bold=True)
C(ax, (1.7, 7.65), (0.4, 8.6), "Hydropore")
C(ax, (2.25, 6.6), (0.2, 7.2), "Axocoel")
C(ax, (2.2, 5.4), (0.2, 5.9), "Hydrocoel")
C(ax, (2.35, 3.6), (0.2, 3.0), "Somatocoel")

# ---------------------------------------------------------------- 2: late brachiolaria (left side)
bio.label(ax, (10.0, 9.0), "2  Brachiolaria (left side)", size="normal", bold=True)
body(np.vstack([np.c_[10.0 + 2.1 * np.cos(th), 4.2 + 2.8 * np.sin(th)]]))
for dx, dy in ((-0.9, 7.1), (0.0, 7.4), (0.9, 7.1)):  # brachiolar arms
    body(np.c_[10.0 + dx + 0.28 * np.cos(th), dy + 0.9 + 0.7 * np.sin(th)], z=1.9)
oval((10.0, 7.25), 0.45, 0.25, "protein", z=6)  # adhesive disc
oval((9.8, 4.3), 0.9, 0.7, "endoderm", z=4)
lobes((10.0, 4.3), 1.25, start=90, z=5)
oval((10.0, 4.3), 0.95, 0.78, SO, z=4.5)
oval((9.8, 4.3), 0.62, 0.5, "endoderm", z=6)
gut(9.6, 1.8, 3.8, w=0.18)
C(ax, (10.0, 7.25), (13.0, 8.4), "Adhesive disc")
C(ax, (11.2, 4.9), (13.0, 6.6), "Hydrocoel lobes")
C(ax, (10.7, 3.6), (13.0, 2.6), "Rudiment")
C(ax, (9.8, 4.3), (7.6, 1.5), "Stomach")

# ---------------------------------------------------------------- 3: metamorphosis after attachment
bio.label(ax, (16.6, 9.0), "3  Metamorphosis", size="normal", bold=True)
body(np.c_[16.6 + 0.35 * np.cos(th), 6.7 + 1.1 * np.sin(th)], z=2)  # remaining stalk of brachiolar complex
oval((16.6, 7.95), 0.5, 0.22, "protein", z=6)
ax.plot([15.6, 17.6], [8.2, 8.2], color=P.muted(), lw=1.4, zorder=1)
body(np.c_[16.6 + 2.0 * np.cos(th), 4.0 + 2.0 * np.sin(th)], z=1.5, ls="--")
lobes((16.6, 4.0), 1.55, k=0.33, start=90, z=5, token="animal")
lobes((16.6, 4.0), 1.0, k=0.3, start=90, z=6)
ax.add_patch(Circle((16.6, 4.0), 0.4, facecolor=P.fill("endoderm"), edgecolor=P.edge("endoderm"), lw=0.8, zorder=7))
C(ax, (18.35, 5.2), (19.6, 7.3), "Larval body resorbed")
C(ax, (17.7, 3.2), (19.6, 1.6), "Five rays grow out")

# ---------------------------------------------------------------- 4: juvenile (oral view)
bio.label(ax, (23.6, 9.0), "4  Juvenile (oral view)", size="normal", bold=True)
c = np.array([23.6, 4.4])
r = 1.0 + 1.9 * (0.5 + 0.5 * np.cos(5 * (th - np.pi / 2))) ** 2
ax.add_patch(Polygon(np.c_[c[0] + r * np.cos(th), c[1] + r * np.sin(th)], closed=True, facecolor=P.light("animal"),
                     edgecolor=P.edge("animal"), lw=1.0, zorder=2))
ax.add_patch(Circle(c, 0.45, facecolor="none", edgecolor=P.edge(HY), lw=2.4, zorder=6))
for k in range(5):
    a = np.pi / 2 + k * 2 * np.pi / 5
    u = np.array([np.cos(a), np.sin(a)])
    n = np.array([-u[1], u[0]])
    ax.plot(*np.vstack([c + u * 0.45, c + u * 2.55]).T, color=P.edge(HY), lw=1.6, zorder=6)
    for j, s in enumerate((0.9, 1.35, 1.8)):
        for sg in (-1, 1):
            ax.add_patch(Circle(c + u * s + n * sg * 0.2, 0.09, facecolor=P.fill(HY), edgecolor=P.edge(HY), lw=0.6, zorder=7))
C(ax, c + (0.45, 0.0), (26.8, 1.6), "Ring canal")
C(ax, c + np.array([np.cos(np.pi / 2 + 2 * np.pi / 5), np.sin(np.pi / 2 + 2 * np.pi / 5)]) * 2.2, (21.4, 0.9), "Radial canal")
C(ax, c + np.array([0.2, 1.35]), (26.4, 7.8), "Tube feet")
for x in (6.6, 13.4, 20.0):
    bio.arrow(ax, (x - 0.35, 0.6), (x + 0.35, 0.6), kind="process", color=P.muted())
