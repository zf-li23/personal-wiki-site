# Genetic control of floral symmetry in Antirrhinum (floral diagrams, adaxial side up). A: wild type,
# zygomorphic: two adaxial petals form the upper lip, three abaxial ones the lower lip, the adaxial median
# (fifth) stamen is a staminode; CYC and DICH are expressed in the adaxial domain (shaded). B: cyc dich
# double mutant: actinomorphic, all petals abaxial-like, five fertile stamens. C: Linaria peloric epimutant:
# Lcyc silenced by methylation, actinomorphic, all five petals spurred.
import numpy as np
import wikibio as bio
from matplotlib.patches import Wedge
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(33, 12)
R = 3.0
XS = [5.2, 16.5, 27.8]
Y = 6.4


def head(i, letter, title, sub):
    bio.panel(ax, letter, (XS[i] - 4.6, 11.8))
    bio.label(ax, (XS[i], 11.4), title, size="title")
    bio.label(ax, (XS[i], 1.1), sub, size="small")


head(0, "A", "Wild type", r"$\it{CYC}$, $\it{DICH}$ on: zygomorphic")
ax.add_patch(Wedge((XS[0], Y), R * 1.25, 90 - 72, 90 + 72, facecolor=P.light("highlight"), edgecolor="none", zorder=1))
plant.floral_diagram(ax, (XS[0], Y), R, [
    dict(organ="sepal", n=5, r=1.0, width=30),
    dict(organ="petal", n=5, r=0.82, width=38, connate=True,
         members=[dict(scale=0.85), dict(scale=0.85), dict(scale=1.15), dict(scale=1.15), dict(scale=1.15)], phase=-36),
    dict(organ="stamen", n=5, r=0.56, phase=0, members=[dict(token="atp", scale=0.35), {}, {}, {}, {}]),
    dict(organ="gynoecium", n=2, placentation="axile", ovules=3, size=0.28)], symmetry="bilateral")
bio.label(ax, (XS[0] + 3.6, Y + 3.3), "adaxial domain", size="small")
bio.callout(ax, (XS[0], Y + 0.56 * R), (XS[0] - 3.0, Y + 4.0), "Staminode", size="small")

head(1, "B", r"$\it{cyc\ dich}$ double mutant", "all petals abaxial-like: actinomorphic")
plant.floral_diagram(ax, (XS[1], Y), R, [
    dict(organ="sepal", n=5, r=1.0, width=30),
    dict(organ="petal", n=5, r=0.82, width=38, connate=True, phase=-36, members=[dict(scale=1.15)] * 5),
    dict(organ="stamen", n=5, r=0.56, phase=0),
    dict(organ="gynoecium", n=2, placentation="axile", ovules=3, size=0.28)], symmetry="radial")

head(2, "C", r"$\it{Linaria}$ peloria", r"$\it{Lcyc}$ methylated: five spurs")
d = plant.floral_diagram(ax, (XS[2], Y), R, [
    dict(organ="sepal", n=5, r=1.0, width=30),
    dict(organ="petal", n=5, r=0.82, width=38, connate=True, phase=-36, members=[dict(scale=1.15)] * 5),
    dict(organ="stamen", n=5, r=0.56, phase=0),
    dict(organ="gynoecium", n=2, placentation="axile", ovules=3, size=0.28)], symmetry="radial")
for k in range(5):
    a = np.radians(90 - (-36 + 72 * k))
    u = np.array([np.cos(a), np.sin(a)])
    p = np.array([XS[2], Y]) + 0.82 * R * u
    q = np.array([XS[2], Y]) + 1.28 * R * u
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge("petal"), lw=3.0, solid_capstyle="round", zorder=2)
bio.callout(ax, np.array([XS[2], Y]) + 1.25 * R * np.array([np.cos(np.radians(126)), np.sin(np.radians(126))]),
            (XS[2] - 4.3, Y + 4.2), "Spur", size="small")
