import wikibio as bio

fig, ax = bio.canvas(14, 5)
bio.icon(ax, "servier/mitochondrion", at=(2, 2.6), height=2.2)
bio.mitochondrion(ax, (5.4, 2.6), 3.0, 1.2, angle=10)
bio.icon(ax, "servier/heart", at=(9, 2.6), height=3.2)
bio.icon(ax, "phylopic/mouse", at=(12.3, 2.6), height=1.6, color="animal")
bio.reaction(ax, (1, 0.6), (5, 0.6), side=("ATP", "ADP"))
bio.lysosome(ax, (7, 0.7), 0.35)
for i, k in enumerate(["ca", "na", "k", "cl"]):
    bio.ion(ax, (8.5 + 1.1 * i, 0.7), k)
