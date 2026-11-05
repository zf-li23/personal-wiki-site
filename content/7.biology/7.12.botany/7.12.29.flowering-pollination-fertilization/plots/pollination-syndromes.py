# Pollination syndromes (after Faegri and van der Pijl), drawn as a chart. Each row is a pollinator group;
# columns give the typical flower colour, scent, time of anthesis, flower shape and reward. Silhouettes:
# PhyloPic (bee, moth, beetle, bat). The syndromes are tendencies: many flowers are visited by several
# kinds of animals.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 15.2)
cols = [0.6, 6.0, 10.2, 14.6, 18.4, 25.4]
heads = ["Pollinator", "Colour", "Scent", "Anthesis", "Flower", "Reward"]
for x, h in zip(cols, heads):
    bio.label(ax, (x, 14.6), h, size="normal", bold=True, ha="left")
ax.plot([0.4, 29.6], [14.15, 14.15], color=P.muted(), lw=0.8)
COL = {"red": "negative", "yellow": "atp", "blue": "dna", "purple": "nucleus", "white": "neutral", "green": "plant",
       "brown": "animal", "pink": "petal", "orange": "mitochondrion"}
rows = [
    ("Bee", "phylopic/honey-bee", ["blue", "purple", "yellow"], "fresh, sweet", "day", "zygomorphic, landing platform,\nnectar guides (UV)", "nectar, pollen"),
    ("Butterfly", None, ["red", "orange", "pink"], "weak", "day", "upright, narrow tube or spur,\nlanding platform", "nectar"),
    ("Hawkmoth", "phylopic/moth", ["white"], "strong, sweet,\nat night", "dusk, night", "long narrow tube or spur,\nno landing platform", "nectar"),
    ("Beetle", "phylopic/beetle", ["white", "green"], "strong, fruity\nor fermenting", "day or night", "large, open bowl,\nprotected ovules", "pollen, floral tissue"),
    ("Carrion fly", None, ["brown", "purple"], "putrid", "day or night", "often a trap or a deep tube", "none (deceit)"),
    ("Bird", None, ["red", "orange"], "none", "day", "tubular or pendent, sturdy,\nexserted stamens and stigma", "copious dilute nectar"),
    ("Bat", "phylopic/bat", ["white", "green"], "strong, musty", "night", "large, robust, pendent or\non the trunk, many stamens", "much nectar, pollen"),
    ("Wind", None, ["green"], "none", "often before leaves", "perianth reduced, catkins,\nfeathery stigmas", "none"),
]
y = 13.2
for name, icon, colours, scent, time, shape, reward in rows:
    if icon == "phylopic/honey-bee":
        bio.icon(ax, "phylopic/honey-bee", at=(4.6, y), height=1.05, color="neutral")
    elif icon == "phylopic/moth":
        bio.icon(ax, "phylopic/moth", at=(4.6, y), height=1.05, color="neutral")
    elif icon == "phylopic/beetle":
        bio.icon(ax, "phylopic/beetle", at=(4.6, y), height=1.05, color="neutral")
    elif icon == "phylopic/bat":
        bio.icon(ax, "phylopic/bat", at=(4.6, y), height=0.9, color="neutral")
    bio.label(ax, (cols[0], y), name, size="normal", ha="left")
    for k, c in enumerate(colours):
        bio.box(ax, (cols[1] + 0.35 + 0.85 * k, y), 0.6, 0.6, token=COL[c], radius=0.12)
    bio.label(ax, (cols[2], y), scent, size="small", ha="left")
    bio.label(ax, (cols[3], y), time, size="small", ha="left")
    bio.label(ax, (cols[4], y), shape, size="small", ha="left")
    bio.label(ax, (cols[5], y), reward, size="small", ha="left")
    ax.plot([0.4, 29.6], [y - 0.8, y - 0.8], color=P.light("neutral"), lw=0.6)
    y -= 1.62
