"""Types of covering epithelium, classified by the number of cell layers and the shape of the surface cells
(Servier Medical Art icons). Simple epithelia (one layer): squamous (exchange surfaces such as capillary
endothelium and lung alveoli), cuboidal (kidney tubules, glands) and columnar (intestine). Pseudostratified
epithelium is one layer of cells of unequal height whose nuclei lie at different levels (the ciliated lining
of the airways). Stratified squamous epithelium has many layers renewed from the basal layer; in land
vertebrates the outer cells keratinize (skin). Most invertebrates have a simple epidermis that secretes a
cuticle.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(27.0, 7.6)
ITEMS = [
    ("Simple squamous", "servier/epithelium-squamous"),
    ("Simple cuboidal", "servier/epithelium-cuboidal"),
    ("Simple columnar", "servier/epithelium-columnar"),
    ("Pseudostratified", "servier/epithelium-pseudostratified"),
    ("Stratified squamous", "servier/epithelium-stratified-squamous"),
]
X = [2.8 + 5.35 * i for i in range(5)]
bio.icon(ax, "servier/epithelium-squamous", at=(X[0], 3.8), width=4.6)
bio.icon(ax, "servier/epithelium-cuboidal", at=(X[1], 3.8), width=4.6)
bio.icon(ax, "servier/epithelium-columnar", at=(X[2], 3.8), width=4.6)
bio.icon(ax, "servier/epithelium-pseudostratified", at=(X[3], 3.8), width=4.6)
bio.icon(ax, "servier/epithelium-stratified-squamous", at=(X[4], 3.8), width=4.6)
for x, (name, _) in zip(X, ITEMS):
    bio.label(ax, (x, 0.7), name, size="small", bold=True)
ax.plot([0.6, 13.5], [7.0, 7.0], color=P.muted(), lw=0.9)
bio.label(ax, (7.05, 7.35), "Simple: one layer", size="small", color=P.muted())
ax.plot([19.0, 26.5], [7.0, 7.0], color=P.muted(), lw=0.9)
bio.label(ax, (22.7, 7.35), "Pseudostratified and stratified", size="small", color=P.muted())
