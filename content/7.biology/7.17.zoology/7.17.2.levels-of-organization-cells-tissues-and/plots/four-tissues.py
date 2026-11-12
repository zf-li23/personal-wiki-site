"""The four basic tissues of animals and their representative cells (Servier Medical Art and DBCLS icons).

Epithelial tissue: cells packed in sheets on a basal lamina, polarized (apical and basal surfaces), here a
simple columnar epithelium with a goblet cell. Connective tissue: few cells in an abundant extracellular
matrix; fibroblasts secrete collagen fibres, adipocytes store fat, and blood is a connective tissue with a
fluid matrix. Muscle tissue: skeletal muscle fibres (multinucleate, striated), cardiomyocytes (branched,
striated, joined by intercalated discs) and smooth muscle cells (spindle-shaped, unstriated). Nervous
tissue: neurons and glial cells, such as the oligodendrocytes that myelinate central axons.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 12.0)
X = [3.2, 9.6, 16.2, 22.6]
for x, t in zip(X, ["Epithelial tissue", "Connective tissue", "Muscle tissue", "Nervous tissue"]):
    bio.label(ax, (x, 11.4), t, size="title", bold=True)
for x in (6.4, 12.9, 19.4):
    ax.plot([x, x], [0.4, 11.0], color=P.muted(), lw=0.6, ls=":")

# epithelial
bio.icon(ax, "servier/epithelium-columnar", at=(X[0], 7.6), width=5.2)
bio.label(ax, (X[0], 5.2), "Simple columnar epithelium", size="small")
bio.icon(ax, "servier/goblet-cell", at=(X[0], 3.0), height=2.6)
bio.label(ax, (X[0], 1.2), "Goblet cell (mucus)", size="small")

# connective
bio.icon(ax, "servier/fibroblast", at=(X[1] - 1.4, 8.6), width=2.6)
bio.label(ax, (X[1] - 1.4, 7.0), "Fibroblast", size="small")
bio.icon(ax, "servier/collagen-fibre", at=(X[1] + 1.6, 8.7), height=3.0)
bio.label(ax, (X[1] + 1.6, 7.0), "Collagen fibre", size="small")
bio.icon(ax, "servier/adipocyte", at=(X[1] - 1.4, 4.2), height=2.4)
bio.label(ax, (X[1] - 1.4, 2.5), "Adipocyte", size="small")
bio.icon(ax, "servier/red-blood-cell", at=(X[1] + 1.6, 4.2), height=1.6)
bio.label(ax, (X[1] + 1.6, 2.5), "Red blood cell", size="small")
bio.label(ax, (X[1], 1.2), "cells in abundant matrix", size="tiny", color=P.muted())

# muscle
bio.icon(ax, "servier/muscle-fibre", at=(X[2], 8.8), width=5.0)
bio.label(ax, (X[2], 7.2), "Skeletal (striated) fibre", size="small")
bio.icon(ax, "servier/cardiomyocyte", at=(X[2] - 1.4, 4.6), width=2.6)
bio.label(ax, (X[2] - 1.4, 2.9), "Cardiomyocyte", size="small")
bio.icon(ax, "servier/smooth-muscle-cell", at=(X[2] + 1.6, 4.6), width=2.8)
bio.label(ax, (X[2] + 1.6, 2.9), "Smooth muscle cell", size="small")
bio.label(ax, (X[2], 1.2), "contractile actin–myosin", size="tiny", color=P.muted())

# nervous
bio.icon(ax, "dbcls/neuron", at=(X[3], 8.2), height=4.0)
bio.label(ax, (X[3], 5.7), "Neuron", size="small")
bio.icon(ax, "dbcls/oligodendrocyte", at=(X[3], 3.6), height=2.6)
bio.label(ax, (X[3], 1.9), "Glial cell (oligodendrocyte)", size="small")
bio.label(ax, (X[3], 1.2), "excitable cells and glia", size="tiny", color=P.muted())
