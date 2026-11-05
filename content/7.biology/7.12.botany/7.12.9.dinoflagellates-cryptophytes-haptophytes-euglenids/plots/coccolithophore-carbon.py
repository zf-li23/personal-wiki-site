"""Coccolithophores and the two carbon pumps (schematic). Left: a coccolithophore cell covered by coccoliths; a
new coccolith forms in a Golgi-derived coccolith vesicle and is secreted to the surface. Right: in surface water
photosynthesis fixes CO2 as organic carbon (organic carbon pump) while calcification combines Ca2+ and HCO3- into
CaCO3 and releases CO2 (carbonate pump); dead cells and coccoliths sink in faecal pellets and aggregates, and
part is buried as chalk."""
import numpy as np
from matplotlib.patches import Circle, Ellipse, Rectangle
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30, 13)
C = "highlight"

# cell
c = np.array([6.0, 6.8])
ax.add_patch(Circle(c, 3.3, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.3, zorder=3))
for a in np.linspace(0, 2 * np.pi, 16, endpoint=False):
    p = c + 3.75 * np.array([np.cos(a), np.sin(a)])
    ax.add_patch(Ellipse(p, 1.5, 0.75, angle=np.degrees(a) + 90, facecolor=P.light("bone"), edgecolor=P.edge("bone"), lw=1.0, zorder=4))
    ax.add_patch(Ellipse(p, 0.7, 0.3, angle=np.degrees(a) + 90, facecolor="none", edgecolor=P.edge("bone"), lw=0.8, zorder=5))
bio.chloroplast(ax, (c[0] - 1.3, c[1] - 1.2), 2.4, 1.0, angle=20)
bio.chloroplast(ax, (c[0] + 1.4, c[1] - 1.3), 2.4, 1.0, angle=-25)
bio.nucleus(ax, (c[0], c[1] + 1.4), 0.9)
bio.golgi(ax, (c[0] + 1.6, c[1] + 0.9), 1.4)
ax.add_patch(Ellipse((c[0] + 2.0, c[1] + 2.0), 1.0, 0.5, angle=30, facecolor=P.fill("vesicle"), edgecolor=P.edge("vesicle"), lw=1.0, zorder=9))
ax.add_patch(Ellipse((c[0] + 2.0, c[1] + 2.0), 0.6, 0.25, angle=30, facecolor=P.light("bone"), edgecolor=P.edge("bone"), lw=0.8, zorder=10))
bio.callout(ax, (c[0] + 2.0, c[1] + 2.0), (11.0, 11.8), "coccolith vesicle", size="tiny")
bio.callout(ax, tuple(c + 3.75 * np.array([np.cos(0.4), np.sin(0.4)])), (11.0, 9.8), "coccolith (calcite)", size="tiny")
bio.callout(ax, (c[0] - 1.3, c[1] - 1.2), (1.0, 1.4), "plastid", size="tiny")
bio.callout(ax, (c[0], c[1] + 1.4), (1.0, 12.0), "nucleus", size="tiny")

# right: ocean column
x0, x1 = 14.0, 29.6
ax.add_patch(Rectangle((x0, 9.6), x1 - x0, 0.15, facecolor=P.edge("dna"), edgecolor="none"))
bio.label(ax, (x0 + 0.2, 12.4), "atmosphere", size="tiny", ha="left", color=P.muted())
bio.label(ax, (x0 + 0.2, 9.2), "surface ocean", size="tiny", ha="left", color=P.muted())
ax.add_patch(Rectangle((x0, 0.4), x1 - x0, 1.2, facecolor=P.light("bone"), edgecolor=P.edge("bone"), lw=0.8))
bio.label(ax, ((x0 + x1) / 2, 1.0), "sediment: chalk (coccolith ooze)", size="tiny")
# CO2 exchange
bio.arrow(ax, (17.0, 11.8), (17.0, 9.9), kind="process", head=0.16)
bio.label(ax, (17.0, 12.3), r"CO$_2$", size="small")
# organic pump
bio.box(ax, (18.0, 7.6), 6.6, 1.5, token="plant", text=r"Photosynthesis" "\n" r"CO$_2$ + H$_2$O $\rightarrow$ (CH$_2$O) + O$_2$", size="tiny")
bio.box(ax, (25.6, 7.6), 6.8, 1.5, token=C, text=r"Calcification" "\n" r"Ca$^{2+}$ + 2 HCO$_3^-$ $\rightarrow$ CaCO$_3$ + CO$_2$ + H$_2$O", size="tiny")
bio.arrow(ax, (25.6, 8.4), (25.6, 9.9), kind="process", head=0.16, dashed=True)
bio.label(ax, (27.4, 9.0), r"CO$_2$ released", size="tiny")
bio.label(ax, (18.0, 5.6), "organic carbon pump", size="small", bold=True, color=P.edge("plant"))
bio.label(ax, (25.6, 5.6), "carbonate pump", size="small", bold=True, color=P.edge(C))
for xs in (18.0, 25.6):
    bio.arrow(ax, (xs, 5.0), (xs, 2.0), kind="process", head=0.2)
bio.label(ax, (21.8, 3.6), "sinking cells, faecal pellets\nand aggregates (ballast)", size="tiny", color=P.muted())
