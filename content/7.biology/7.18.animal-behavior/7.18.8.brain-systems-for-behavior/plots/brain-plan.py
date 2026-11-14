"""Schematic lateral views of vertebrate brains with homologous divisions in the same color
(anterior to the left; sizes schematic, not to scale)."""
from matplotlib.patches import Ellipse

import wikibio as bio

P = bio.P
regions = [("olfactory bulb", "rna"), ("telencephalon", "receptor"), ("diencephalon", "highlight"),
           ("optic tectum / midbrain", "dna"), ("cerebellum", "positive"), ("medulla", "metabolite")]
col = dict(regions)
# per class: list of (region, x, y, w, h) in a 6 x 3 panel
brains = {
    "Fish": [("olfactory bulb", 0.6, 1.4, 0.8, 0.5), ("telencephalon", 1.6, 1.5, 1.1, 0.9), ("diencephalon", 2.5, 1.0, 0.7, 0.6),
             ("optic tectum / midbrain", 3.0, 1.75, 1.4, 1.1), ("cerebellum", 4.1, 1.7, 1.2, 1.0), ("medulla", 5.0, 1.15, 1.6, 0.6)],
    "Frog": [("olfactory bulb", 0.6, 1.4, 0.8, 0.5), ("telencephalon", 1.8, 1.5, 1.6, 0.9), ("diencephalon", 2.8, 1.1, 0.7, 0.6),
             ("optic tectum / midbrain", 3.3, 1.7, 1.0, 0.9), ("cerebellum", 4.05, 1.6, 0.5, 0.6), ("medulla", 4.9, 1.2, 1.6, 0.6)],
    "Lizard": [("olfactory bulb", 0.5, 1.4, 0.8, 0.45), ("telencephalon", 1.9, 1.6, 2.0, 1.2), ("diencephalon", 3.0, 1.0, 0.7, 0.6),
               ("optic tectum / midbrain", 3.5, 1.75, 1.0, 0.9), ("cerebellum", 4.25, 1.7, 0.6, 0.7), ("medulla", 5.0, 1.15, 1.5, 0.6)],
    "Bird": [("olfactory bulb", 0.45, 1.5, 0.45, 0.3), ("telencephalon", 1.9, 1.75, 2.6, 1.9), ("diencephalon", 2.9, 0.85, 0.7, 0.5),
             ("optic tectum / midbrain", 3.2, 0.95, 1.2, 0.95), ("cerebellum", 4.05, 1.9, 1.2, 1.3), ("medulla", 4.9, 1.05, 1.4, 0.55)],
    "Mammal": [("olfactory bulb", 0.4, 1.3, 0.6, 0.4), ("telencephalon", 2.3, 1.85, 3.6, 2.1), ("diencephalon", 2.9, 1.0, 0.7, 0.5),
               ("optic tectum / midbrain", 3.6, 1.05, 0.7, 0.5), ("cerebellum", 4.5, 1.15, 1.3, 1.1), ("medulla", 5.3, 0.75, 1.2, 0.5)],
}
fig, ax = bio.canvas(34, 7.2)
for i, (name, parts) in enumerate(brains.items()):
    x0 = 0.5 + i * 6.7
    order = sorted(parts, key=lambda r: 0 if r[0] in ("medulla", "diencephalon") else 1)
    for reg, x, y, w, h in order:
        ax.add_patch(Ellipse((x0 + x, 2.2 + y), w, h, facecolor=P.fill(col[reg]), edgecolor=P.edge(col[reg]), lw=1.0,
                             zorder=5 if reg in ("medulla", "diencephalon") else 6))
    bio.label(ax, (x0 + 3.0, 5.6), name, size="normal")
for j, (reg, tok) in enumerate(regions):
    x = 1.0 + j * 5.5
    bio.box(ax, (x, 0.9), 0.6, 0.45, tok)
    bio.label(ax, (x + 0.45, 0.9), reg, size="small", ha="left")
ax.set_ylim(0.3, 6.3)
