"""Membranes of primary (A) and secondary (B) plastids (schematic, after Barton et al. 2007, Fig. 8.11):
two cyanobacterial membranes; periplastid space with nucleomorph; alga plasma membrane (lost in euglenids
and dinoflagellates); host food-vacuole membrane; host nucleus."""
from matplotlib.patches import Ellipse
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24, 10)


def ring(c, w, h, tok, lw=2.2, fill=None, ls="-"):
    ax.add_patch(Ellipse(c, w, h, facecolor=P.light(fill) if fill else "none", edgecolor=P.edge(tok), lw=lw,
                         ls=ls, zorder=5))


bio.panel(ax, "A", (0.3, 9.7))
bio.label(ax, (5.0, 9.3), "primary plastid (2 membranes)", size="small", bold=True)
c = (5.0, 5.2)
ax.add_patch(Ellipse(c, 6.4, 4.4, facecolor=P.light("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=1.0, zorder=2))
ring(c, 4.0, 2.4, "chloroplast", fill="chloroplast")
ring(c, 3.6, 2.0, "chloroplast")
for k in range(3):
    ax.plot([c[0] - 1.1, c[0] + 1.1], [c[1] - 0.4 + 0.4 * k] * 2, color=P.edge("thylakoid"), lw=2.0, zorder=6)
bio.callout(ax, (c[0] + 1.95, c[1] + 0.3), (8.6, 7.6), "cyanobacterial outer\nand inner membranes", size="tiny")
bio.label(ax, (c[0], c[1] - 3.0), "host cytoplasm", size="tiny", color=P.muted())

bio.panel(ax, "B", (11.0, 9.7))
bio.label(ax, (17.0, 9.3), "secondary plastid (4 membranes)", size="small", bold=True)
c = (17.5, 5.0)
ax.add_patch(Ellipse((16.8, 5.0), 11.6, 7.4, facecolor=P.light("cytoplasm"), edgecolor=P.edge("cytoplasm"), lw=1.0,
                     zorder=1))
bio.nucleus(ax, (12.6, 5.0), 0.9)
bio.label(ax, (12.6, 3.7), "host nucleus", size="tiny", color=P.muted())
ring(c, 7.0, 4.6, "vacuole", lw=2.0)
ring(c, 6.4, 4.0, "lipid_head", lw=2.0, ls=(0, (4, 2)))
ax.add_patch(Ellipse(c, 6.1, 3.7, facecolor=P.light("vesicle"), edgecolor="none", zorder=3))
ring((18.4, 5.0), 3.6, 2.4, "chloroplast", fill="chloroplast")
ring((18.4, 5.0), 3.2, 2.0, "chloroplast")
for k in range(3):
    ax.plot([17.4, 19.4], [4.6 + 0.4 * k] * 2, color=P.edge("thylakoid"), lw=2.0, zorder=6)
ax.add_patch(Ellipse((15.6, 5.0), 0.9, 0.7, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.8, zorder=7))
bio.callout(ax, (15.6, 5.3), (14.8, 8.4), "nucleomorph (in cryptophytes,\nchlorarachniophytes)", size="tiny")
bio.callout(ax, (19.8, 6.6), (21.8, 8.5), "4: host food-vacuole membrane", size="tiny")
bio.callout(ax, (20.5, 5.9), (22.0, 7.6), "3: alga plasma membrane\n(lost in euglenids, dinoflagellates)", size="tiny")
bio.callout(ax, (20.15, 5.3), (22.0, 6.2), "1, 2: cyanobacterial membranes", size="tiny")
bio.callout(ax, (16.6, 4.0), (16.0, 1.0), "periplastid space (former alga cytoplasm)", size="tiny")
