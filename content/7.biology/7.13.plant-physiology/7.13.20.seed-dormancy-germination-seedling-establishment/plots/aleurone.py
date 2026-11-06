# Mobilization of starch in a germinating cereal grain (schematic, after Taiz et al. 6e, Figs 18.9 and
# 18.11; Gubler et al. 1995). (A) The grain: gibberellin (GA1) made by the embryo diffuses through the
# scutellum and starchy endosperm to the living aleurone layer; aleurone cells secrete alpha-amylase and other
# hydrolases into the dead starchy endosperm; the sugars released are absorbed by the scutellum and fed to
# the embryo. (B) An aleurone cell: GA binds the receptor GID1, the GA-GID1-DELLA complex is ubiquitinated by
# SCF(SLY1/GID2) and DELLA is degraded by the 26S proteasome; GA-MYB is expressed (about 1 h) and binds the
# GARE (TAACAAA) of the alpha-amylase promoter (mRNA rises after about 3 h); alpha-amylase is made on the rough
# ER and secreted via the Golgi, a step that needs Ca2+-calmodulin. ABA represses GA-MYB.
import numpy as np
import wikibio as bio
from matplotlib.patches import Circle, Ellipse, FancyBboxPatch

P = bio.P
fig, ax = bio.canvas(18, 9)
bio.panel(ax, "A", (0.1, 8.9))
# grain outline
g = bio.blob((4.3, 4.4), 3.7, 2.4, wobble=0.03, seed=4)
bio.shape(ax, g, token="cell_wall", lw=1.4, zorder=2)  # testa-pericarp
inner = bio.blob((4.3, 4.4), 3.45, 2.17, wobble=0.03, seed=4)
bio.shape(ax, inner, token="protein", lw=1.0, zorder=3)  # aleurone
end = bio.blob((4.6, 4.4), 3.0, 1.85, wobble=0.03, seed=4)
bio.shape(ax, end, token="carbohydrate", lw=1.0, zorder=4)  # starchy endosperm
rng = np.random.default_rng(1)
for _ in range(60):
    x, y = rng.uniform(2.3, 7.2), rng.uniform(3.0, 5.8)
    if ((x - 4.6) / 2.8) ** 2 + ((y - 4.4) / 1.7) ** 2 < 1 and x > 2.3:
        ax.add_patch(Circle((x, y), 0.09, facecolor=P.edge("carbohydrate"), edgecolor="none", zorder=5))
ax.add_patch(Ellipse((1.25, 4.4), 1.7, 2.6, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.1, zorder=6))
ax.add_patch(Ellipse((2.0, 4.4), 0.45, 2.3, facecolor=P.fill("sepal"), edgecolor=P.edge("sepal"), lw=1.0, zorder=7))
red = P.edge("negative")
bio.arrow(ax, (2.3, 5.2), (4.3, 6.35), kind="process", color=P.edge("drug"), lw=1.8, bend=-0.2)
bio.label(ax, (3.0, 6.25), "GA", size="small", color=P.edge("drug"), bold=True)
bio.arrow(ax, (5.4, 6.45), (5.6, 5.4), kind="process", color=red, lw=1.8)
bio.label(ax, (6.5, 5.95), "α-amylase", size="tiny", color=red)
bio.arrow(ax, (4.0, 3.6), (2.3, 3.8), kind="process", color=P.edge("plant"), lw=1.8, bend=0.15)
bio.label(ax, (3.2, 3.3), "sugars", size="tiny", color=P.edge("plant"))
bio.callout(ax, (1.0, 4.4), (0.4, 1.3), "Embryo", size="tiny")
bio.callout(ax, (2.0, 3.6), (1.9, 0.6), "Scutellum", size="tiny")
bio.callout(ax, (5.5, 4.4), (6.0, 1.0), "Starchy endosperm (dead)", size="tiny")
bio.callout(ax, (6.8, 6.1), (7.0, 7.8), "Aleurone layer (living)", size="tiny")
bio.callout(ax, (7.95, 4.4), (8.3, 2.0), "Testa–pericarp", size="tiny")

bio.panel(ax, "B", (9.0, 8.9))
ax.add_patch(FancyBboxPatch((9.4, 0.6), 8.3, 7.6, boxstyle="round,pad=0,rounding_size=0.4",
                            facecolor=P.fill("cytoplasm"), edgecolor=P.edge("cell_wall"), lw=2.4, zorder=2))
bio.nucleus(ax, (12.0, 5.7), 1.6, pores=10, nucleolus=False, chromatin=False, zorder=3)
bio.protein(ax, (10.6, 7.6), 0.9, 0.5, "metabolite", text="GA₁")
bio.protein(ax, (11.4, 6.6), 0.95, 0.55, "receptor", text="GID1")
bio.protein(ax, (12.6, 6.6), 0.95, 0.55, "negative", text="DELLA")
bio.label(ax, (12.0, 7.35), "SCF(SLY1)", size="tiny")
bio.protein(ax, (13.9, 7.6), 1.0, 0.55, "neutral", text="26S")
bio.arrow(ax, (13.1, 6.85), (13.6, 7.3), kind="process", lw=1.2)
bio.dna(ax, (10.8, 5.0), (13.3, 5.0), style="duplex")
bio.label(ax, (11.4, 4.6), "GA-MYB gene", size="tiny", italic=True)
bio.dna(ax, (10.8, 4.0), (13.3, 4.0), style="duplex")
bio.label(ax, (12.2, 3.6), "GARE · α-amylase gene", size="tiny")
bio.protein(ax, (14.6, 5.0), 1.3, 0.55, "protein", text="GA-MYB")
bio.arrow(ax, (12.6, 6.3), (12.2, 5.25), kind="inhibition", lw=1.2)
bio.arrow(ax, (13.4, 5.0), (13.9, 5.0), kind="process", lw=1.2)
bio.arrow(ax, (14.4, 4.7), (13.2, 4.2), kind="activation", lw=1.2)
bio.er(ax, (14.6, 2.7), 1.8, 0.9, sheets=3)
bio.golgi(ax, (16.4, 3.4), 1.0, cisternae=4)
bio.arrow(ax, (13.4, 3.8), (13.9, 3.0), kind="process", lw=1.2)
bio.arrow(ax, (15.5, 2.8), (15.9, 3.2), kind="process", lw=1.2)
bio.vesicle(ax, (16.9, 1.6), 0.25, cargo="enzyme")
bio.arrow(ax, (16.6, 3.0), (16.9, 1.9), kind="process", lw=1.2)
bio.arrow(ax, (17.2, 1.4), (18.1, 1.0), kind="process", color=red, lw=1.6)
bio.label(ax, (16.2, 0.95), "Ca²⁺–calmodulin", size="tiny")
bio.protein(ax, (16.0, 7.0), 0.9, 0.5, "drug", text="ABA")
bio.arrow(ax, (15.9, 6.7), (14.9, 5.3), kind="inhibition", lw=1.2)
bio.label(ax, (17.4, 5.1), "~1 h", size="tiny", color=P.muted())
bio.label(ax, (11.0, 3.2), "mRNA ~3 h", size="tiny", color=P.muted())
bio.label(ax, (13.5, 8.55), "Aleurone cell", size="small", bold=True)
