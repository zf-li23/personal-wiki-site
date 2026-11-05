"""Hyphae and hyphal tissues (schematic, not to scale). A: coenocytic and septate hyphae. B: sclerotium in
section (pseudoparenchymatous rind, prosenchymatous medulla). C: ergot sclerotium germinating into stalked
stromata with embedded perithecia. D: rhizomorph tip in longitudinal section. E: haustorium in a host
cell. F: appressorium and penetration peg."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Polygon

import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(30, 15)
rng = np.random.default_rng(4)


def title(x, y, t):
    bio.label(ax, (x, y), t, size="small", bold=True)


# A hyphae
bio.panel(ax, "A", (0.2, 14.8))
t = np.linspace(0, 1, 30)
plant.hypha(ax, np.c_[0.8 + 7 * t, 13.0 + 0.25 * np.sin(5 * t)], width=0.32, septa=None, nuclei=1)
plant.hypha(ax, np.c_[0.8 + 7 * t, 11.5 + 0.25 * np.sin(5 * t)], width=0.32, septa=1.2, nuclei=1)
bio.label(ax, (4.3, 13.75), "Coenocytic (Mucoromycota)", size="small")
bio.label(ax, (4.3, 10.75), "Septate (Ascomycota)", size="small")

# B sclerotium section
bio.panel(ax, "B", (9.8, 14.8))
c = np.array([13.8, 12.0]); R = 2.2
for k in range(170):  # loose medulla hyphae
    a = rng.uniform(0, 2 * np.pi); r = np.sqrt(rng.uniform(0, 1)) * (R - 0.5)
    p = c + r * np.array([np.cos(a), np.sin(a)])
    d = rng.uniform(0, np.pi)
    q = p + 0.35 * np.array([np.cos(d), np.sin(d)])
    ax.plot([p[0], q[0]], [p[1], q[1]], color=P.edge("lipid_tail"), lw=0.9, zorder=5, solid_capstyle="round")
ax.add_patch(Circle(c, R - 0.45, facecolor=P.light("lipid_tail"), edgecolor="none", zorder=4))
for ring, rr in enumerate([R - 0.32, R - 0.12]):
    n = int(2 * np.pi * rr / 0.22)
    for k in range(n):
        a = 2 * np.pi * (k + 0.5 * ring) / n
        ax.add_patch(Circle(c + rr * np.array([np.cos(a), np.sin(a)]), 0.12, facecolor=P.fill("chromatin") if ring else P.fill("bone"),
                            edgecolor=P.edge("chromatin"), lw=0.5, zorder=6))
bio.callout(ax, c + np.array([R - 0.1, 0.6]), (17.6, 13.8), "Rind:\npseudoparenchyma")
bio.callout(ax, c + np.array([0.3, -0.4]), (17.6, 10.6), "Medulla:\nprosenchyma")
bio.label(ax, (13.8, 9.3), "Sclerotium (section)", size="small")

# C ergot with stromata
bio.panel(ax, "C", (20.2, 14.8))
erg = np.array([[22.0, 9.6], [22.4, 9.9], [24.0, 10.4], [24.3, 10.25], [22.6, 9.5]])
bio.shape(ax, bio.smooth_closed(erg, n=80), token="chromatin")
for k, (x0, h) in enumerate([(22.6, 3.2), (23.3, 3.8), (23.9, 3.0)]):
    y0 = 9.75 + 0.25 * (x0 - 22.4)
    ax.plot([x0, x0 + 0.15 * (k - 1)], [y0, y0 + h], color=P.edge("animal"), lw=2.2, zorder=6)
    hc = np.array([x0 + 0.15 * (k - 1), y0 + h + 0.35])
    ax.add_patch(Circle(hc, 0.4, facecolor=P.fill("animal"), edgecolor=P.edge("animal"), lw=0.9, zorder=7))
    for j in range(9):
        a = 2 * np.pi * j / 9
        ax.add_patch(Ellipse(hc + 0.28 * np.array([np.cos(a), np.sin(a)]), 0.12, 0.16, angle=np.degrees(a),
                             facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.4, zorder=8))
bio.callout(ax, (23.3, 13.95), (26.6, 14.3), "Stroma with\nperithecia")
bio.callout(ax, (23.0, 9.8), (26.6, 9.4), "Sclerotium\n(ergot)")
bio.label(ax, (23.2, 8.8), "Claviceps purpurea", size="small", italic=True)

# D rhizomorph
bio.panel(ax, "D", (0.2, 7.6))
x = np.linspace(1.0, 8.0, 50)
top, bot = 4.6 + 0.0 * x, 3.0 + 0.0 * x
tip = [(8.0, 4.6), (8.6, 4.3), (8.75, 3.8), (8.6, 3.3), (8.0, 3.0)]
outline = np.vstack([np.c_[x, top], tip, np.c_[x[::-1], bot[::-1]]])
ax.add_patch(Polygon(outline, closed=True, facecolor=P.fill("chromatin"), edgecolor=P.edge("chromatin"), lw=1.0, zorder=5))
inner = np.vstack([np.c_[x, top - 0.35], [(8.1, 4.1), (8.3, 3.8), (8.1, 3.5)], np.c_[x[::-1], bot[::-1] + 0.35]])
ax.add_patch(Polygon(inner, closed=True, facecolor=P.light("lipid_tail"), edgecolor="none", zorder=6))
for yy in np.linspace(3.5, 4.1, 5):
    ax.plot(x, yy + 0.04 * np.sin(x * 3 + yy * 7), color=P.edge("lipid_tail"), lw=0.7, zorder=7)
ax.add_patch(Ellipse((8.25, 3.8), 0.5, 0.6, facecolor=P.fill("highlight"), edgecolor=P.edge("highlight"), lw=0.7, zorder=8))
bio.callout(ax, (8.3, 3.8), (8.9, 5.6), "Growing point")
bio.callout(ax, (4.0, 4.5), (3.0, 5.6), "Rind")
bio.callout(ax, (3.5, 3.8), (1.6, 2.2), "Medulla")
bio.label(ax, (5.0, 1.2), "Rhizomorph tip (longitudinal section)", size="small")

# E haustorium
bio.panel(ax, "E", (10.2, 7.6))
cell = np.array([[11.0, 1.4], [18.0, 1.4], [18.0, 5.6], [11.0, 5.6]])
ax.add_patch(Polygon(cell, closed=True, facecolor=P.light("plant"), edgecolor=P.edge("cell_wall"), lw=2.4, zorder=4))
plant.hypha(ax, np.array([[11.0, 6.3], [18.0, 6.3]]), width=0.34, septa=1.6, nuclei=1, tip=False)
plant.hypha(ax, np.array([[14.5, 6.2], [14.5, 4.5]]), width=0.12, septa=None, nuclei=0, tip=False)
ax.add_patch(Ellipse((14.5, 3.9), 3.0, 1.9, facecolor=P.light("membrane"), edgecolor=P.edge("membrane"), lw=1.0, ls=(0, (3, 2)), zorder=8))
for dx in (-0.8, -0.3, 0.3, 0.8):
    ax.add_patch(Ellipse((14.5 + dx, 3.75), 0.42, 1.1 - 0.25 * abs(dx), facecolor=P.fill("lipid_tail"), edgecolor=P.edge("lipid_tail"), lw=0.8, zorder=9))
ax.add_patch(Ellipse((14.5, 4.35), 1.6, 0.55, facecolor=P.fill("lipid_tail"), edgecolor=P.edge("lipid_tail"), lw=0.8, zorder=9))
bio.callout(ax, (17.0, 6.3), (19.2, 7.2), "Intercellular hypha")
bio.callout(ax, (14.3, 3.6), (19.2, 3.4), "Haustorium")
bio.callout(ax, (15.95, 4.2), (19.2, 4.8), "Invaginated host\nplasma membrane")
bio.callout(ax, (11.0, 2.5), (19.2, 2.0), "Host cell wall")

# F appressorium
bio.panel(ax, "F", (21.2, 7.6))
ax.add_patch(Polygon(np.array([[21.6, 2.6], [29.6, 2.6], [29.6, 3.2], [21.6, 3.2]]), closed=True, facecolor=P.fill("cell_wall"),
                     edgecolor=P.edge("cell_wall"), lw=0.8, zorder=4))
ax.add_patch(Polygon(np.array([[21.6, 3.2], [29.6, 3.2], [29.6, 3.4], [21.6, 3.4]]), closed=True, facecolor=P.fill("lipid"),
                     edgecolor=P.edge("lipid"), lw=0.6, zorder=4))
ax.add_patch(Ellipse((24.0, 4.8), 1.0, 1.3, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.9, zorder=6))
plant.hypha(ax, np.array([[24.5, 4.8], [26.5, 5.2], [28.0, 5.6]]), width=0.26, septa=None, nuclei=0, tip=False)
ax.add_patch(Ellipse((28.6, 5.8), 1.1, 0.6, angle=20, facecolor=P.fill("ovule"), edgecolor=P.edge("ovule"), lw=0.8, zorder=6))
plant.hypha(ax, np.array([[24.0, 4.2], [24.0, 2.3]]), width=0.1, septa=None, nuclei=0)
plant.hypha(ax, np.array([[24.0, 2.4], [24.8, 1.6]]), width=0.2, septa=None, nuclei=0)
bio.callout(ax, (24.3, 5.2), (21.8, 5.9), "Appressorium\n(melanized,\nhigh turgor)")
bio.callout(ax, (28.7, 5.9), (28.4, 7.0), "Conidium")
bio.callout(ax, (26.2, 5.1), (27.0, 4.2), "Germ tube")
bio.callout(ax, (24.0, 2.9), (21.8, 1.4), "Penetration peg")
bio.callout(ax, (28.0, 3.3), (28.0, 1.4), "Cuticle and wall")
