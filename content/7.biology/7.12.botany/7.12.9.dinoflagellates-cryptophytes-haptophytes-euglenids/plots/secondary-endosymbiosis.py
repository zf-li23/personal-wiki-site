"""Four outcomes of secondary endosymbiosis (schematic). In each cell the host nucleus is blue; the remains of
the engulfed alga are green (green-algal origin) or red (red-algal origin). A: cryptophytes (red) and B:
chlorarachniophytes (green): four envelope membranes, with the relic nucleus of the engulfed alga (nucleomorph,
purple) between the second and third. C: heterokonts and haptophytes (red): four membranes, the outermost
continuous with the host nuclear envelope, nucleomorph lost. D: euglenids (green) and peridinin dinoflagellates
(red): the plasma membrane of the engulfed alga also lost, three membranes remain."""
import numpy as np
from matplotlib.patches import Ellipse, Circle, FancyBboxPatch
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(32, 11)


def rbox(c, w, h, edge, fill="none", lw=1.6, z=5, r=0.6):
    ax.add_patch(FancyBboxPatch((c[0] - w / 2, c[1] - h / 2), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                facecolor=fill, edgecolor=edge, lw=lw, zorder=z))


panels = [("A", "Cryptophytes", "red", 4, True, False), ("B", "Chlorarachniophytes", "green", 4, True, False),
          ("C", "Heterokonts, haptophytes", "red", 4, False, True), ("D", "Euglenids, dinoflagellates", "both", 3, False, False)]
for i, (L, title, origin, nmem, nm, cer) in enumerate(panels):
    x = 4.0 + 8.0 * i
    bio.panel(ax, L, (x - 3.8, 10.8))
    bio.label(ax, (x, 10.3), title, size="small", bold=True)
    ax.add_patch(Ellipse((x, 5.0), 7.0, 8.2, facecolor=P.fill("cytoplasm"), edgecolor=P.edge("membrane"), lw=1.3, zorder=2))
    # host nucleus
    ax.add_patch(Circle((x - 1.6, 2.4), 0.95, facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=1.2, zorder=4))
    pc = np.array([x + 0.4, 6.0])
    tok = {"red": "negative", "green": "plant", "both": "plant"}[origin]
    # inner plastid (two cyanobacterial membranes)
    rbox(pc, 2.0, 1.5, P.edge("chloroplast"), fill=P.light("chloroplast"), z=7, r=0.5)
    rbox(pc, 2.3, 1.8, P.edge("chloroplast"), z=7, r=0.6)
    for yy in (-0.3, 0.0, 0.3):
        ax.plot([pc[0] - 0.7, pc[0] + 0.7], [pc[1] + yy, pc[1] + yy], color=P.edge("thylakoid"), lw=1.0, zorder=8)
    if nmem == 4:
        # periplastid space bounded by algal plasma membrane
        rbox(pc + np.array([0.2, 0]), 3.6, 2.9, P.edge(tok), fill=P.light(tok), z=6, r=0.8)
        rbox(pc + np.array([0.2, 0]), 4.1, 3.4, P.edge("dna"), z=6, r=0.9)
    else:
        rbox(pc, 2.8, 2.3, P.edge("dna"), z=6, r=0.7)
    if nm:
        ax.add_patch(Circle(pc + np.array([1.55, 0.6]), 0.3, facecolor=P.fill("nucleus"), edgecolor=P.edge("nucleus"), lw=1.0, zorder=8))
        bio.callout(ax, tuple(pc + np.array([1.55, 0.6])), (x + 2.6, 9.0), "nucleomorph", size="tiny")
    if cer:
        ax.plot([x - 1.0, x - 1.4], [4.4, 3.3], color=P.edge("dna"), lw=1.6, zorder=6)
        bio.label(ax, (x - 2.0, 4.4), "outer membrane\njoins nuclear\nenvelope", size="tiny", ha="center", color=P.muted())
    bio.label(ax, (x, 0.5), f"{nmem} membranes", size="small", color=P.muted())
    bio.label(ax, (x + 1.2, 1.9), {"red": "red-algal plastid", "green": "green-algal plastid", "both": "green or red origin"}[origin],
              size="tiny", color=P.muted())
