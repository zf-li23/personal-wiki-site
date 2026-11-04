# Two AB toxins and their intracellular routes: diphtheria toxin (endosome) and cholera toxin (retrograde to the ER).
from matplotlib.patches import Circle, Rectangle

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(19.0, 9.2)


def cell_frame(x0, w, letter, title, subtitle):
    bio.panel(ax, letter, (x0, 8.95))
    bio.label(ax, (x0 + w / 2, 8.95), title, size="title", bold=True)
    bio.label(ax, (x0 + w / 2, 8.5), subtitle, size="tiny", color=P.muted())
    ax.add_patch(Rectangle((x0, 0.5), w, 7.1, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=1))
    bio.bilayer(ax, [(x0, 7.6), (x0 + w, 7.6)], zorder=4)


def toxin(center, label_a):
    """An AB toxin: a dark A moiety on a pentameric B ring."""
    x, y = center
    for k in range(5):
        ax.add_patch(Circle((x - 0.56 + k * 0.28, y), 0.14, facecolor=P.fill("enzyme"),
                            edgecolor=P.edge("enzyme"), lw=0.8, zorder=12))
    bio.protein(ax, (x, y + 0.42), 0.6, 0.38, "drug", text=label_a, size="tiny")


# ================================================================ A: diphtheria toxin
X, W = 0.4, 8.8
cell_frame(X, W, "A", "Diphtheria toxin", "low pH in the endosome drives translocation")

toxin((X + 1.6, 8.05), "A")
bio.receptor(ax, X + 1.6, 7.6, kind="rtk", token="receptor", text=None)

bio.vesicle(ax, (X + 1.6, 6.1), 0.75)
toxin((X + 1.6, 6.0), "A")
bio.arrow(ax, (X + 1.6, 7.25), (X + 1.6, 6.95), kind="process")
bio.label(ax, (X + 2.6, 6.7), "receptor proHB-EGF;\nclathrin-mediated endocytosis", size="tiny", ha="left", color=P.muted())
bio.label(ax, (X + 2.6, 5.9), "the endosome acidifies to pH ≈ 5;\nthe T domain inserts and threads\nthe A chain into the cytosol",
          size="tiny", ha="left", color=P.muted())

bio.arrow(ax, (X + 1.2, 5.4), (X + 1.0, 4.4), kind="process")
bio.protein(ax, (X + 1.0, 4.1), 0.7, 0.45, "drug", text="A", size="tiny")

bio.box(ax, (X + 3.6, 4.1), 2.3, 0.9, token="protein", radius=0.15)
bio.label(ax, (X + 3.6, 4.1), "EF-2", size="small", bold=True, color=P.on_fill())
bio.arrow(ax, (X + 1.4, 4.1), (X + 2.4, 4.1), kind="catalysis")
bio.label(ax, (X + 1.9, 5.05), "ADP-ribosylation\nof diphthamide", size="tiny", color=P.muted())
bio.molecule(ax, (X + 2.0, 3.3), token="atp", text="NAD⁺", r=0.3, size="tiny")

bio.arrow(ax, (X + 4.8, 4.1), (X + 5.8, 4.1), kind="inhibition")
bio.box(ax, (X + 7.1, 4.1), 2.6, 0.9, token="negative", radius=0.15)
bio.label(ax, (X + 7.1, 4.1), "translation stops", size="small", bold=True, color=P.on_fill())
bio.structures.ribosome(ax, (X + 7.1, 2.6), 0.55)
bio.label(ax, (X + 7.1, 1.85), "the cell dies; pharyngeal\npseudomembrane, damage\nto heart and nerves",
          size="tiny", color=P.muted())
bio.label(ax, (X + W / 2, 0.75), "one molecule in the cytosol is enough", size="tiny", color=P.muted())

# ================================================================ B: cholera toxin
X, W = 9.8, 8.8
cell_frame(X, W, "B", "Cholera toxin", "backwards through Golgi and ER, then ERAD")

toxin((X + 1.5, 8.05), "A")
ax.add_patch(Circle((X + 1.5, 7.62), 0.17, facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"),
                    lw=0.9, zorder=11))

bio.vesicle(ax, (X + 1.5, 6.5), 0.55)
bio.arrow(ax, (X + 1.5, 7.3), (X + 1.5, 7.1), kind="process")
bio.golgi(ax, (X + 1.5, 5.3), 2.0)
bio.arrow(ax, (X + 1.5, 6.0), (X + 1.5, 5.85), kind="process")
bio.er(ax, (X + 1.6, 3.8), 2.4, 1.0)
bio.arrow(ax, (X + 1.5, 4.65), (X + 1.5, 4.35), kind="process")
bio.label(ax, (X + 3.0, 5.4), "receptor: ganglioside GM1;\nretrograde transport", size="tiny", ha="left", color=P.muted())
bio.label(ax, (X + 3.0, 3.8), "the A1 chain is unfolded and\nexported by the ERAD machinery", size="tiny",
          ha="left", color=P.muted())

bio.protein(ax, (X + 1.2, 2.7), 0.7, 0.45, "drug", text="A1", size="tiny")
bio.arrow(ax, (X + 1.4, 3.2), (X + 1.3, 3.0), kind="process")
bio.box(ax, (X + 3.5, 2.7), 2.2, 0.9, token="protein", radius=0.15)
bio.label(ax, (X + 3.5, 2.7), "$G_\\mathrm{s}\\alpha$", size="small", bold=True, color=P.on_fill())
bio.arrow(ax, (X + 1.6, 2.7), (X + 2.4, 2.7), kind="catalysis")
bio.label(ax, (X + 2.2, 2.05), "ADP-ribosylation:\nno GTPase activity", size="tiny", color=P.muted())

bio.arrow(ax, (X + 4.6, 2.7), (X + 5.4, 2.7), kind="activation")
bio.box(ax, (X + 6.9, 2.7), 2.8, 0.9, token="enzyme", radius=0.15)
bio.label(ax, (X + 6.9, 2.7), "adenylate cyclase on", size="tiny", bold=True, color=P.on_fill())
bio.arrow(ax, (X + 6.9, 2.2), (X + 6.9, 1.8), kind="process")
bio.label(ax, (X + 6.9, 1.45), "cAMP high → CFTR opens", size="tiny")
bio.arrow(ax, (X + 6.9, 1.2), (X + 6.9, 0.95), kind="process")
bio.label(ax, (X + 6.9, 0.72), "Cl⁻ and water into the lumen", size="tiny")
bio.label(ax, (X + 2.4, 0.95), "the epithelium stays intact, and\nNa⁺–glucose uptake still works:\noral rehydration cures",
          size="tiny", color=P.muted())
