"""Altitudinal zonation of the fauna on the slopes of the Hengduan Mountains (schematic).

Belts and elevations are approximate and vary with latitude and slope; each animal is placed in the belt
where it is most typical, not at the limits of its range. Palearctic elements dominate the upper belts,
Oriental elements the valleys, and the two interdigitate along the north-south valleys.
"""

import numpy as np
import wikibio as bio
from wikibio import charts
from matplotlib.patches import Polygon

P = bio.P

fig, ax = bio.canvas(20, 12)
a = charts.axes_at(ax, (3.2, 1.0, 8.8, 10.2))

BELTS = [  # (lower, upper elevation in m, token, belt, fauna class)
    (1000, 2000, "positive", "Subtropical evergreen broadleaf forest\nand dry valleys", "Oriental"),
    (2000, 2800, "lipid", "Mixed broadleaf-conifer forest", "mixed"),
    (2800, 3800, "plant", "Subalpine conifer forest\n(fir, spruce; bamboo understory)", "mixed"),
    (3800, 4600, "metabolite", "Alpine shrub and meadow", "Palearctic"),
    (4600, 5400, "neutral", "Scree, cold desert, snow", "Palearctic"),
]
x = np.linspace(0, 10, 400)
profile = 1000 + 4300 * np.exp(-((x - 5.0) / 2.4) ** 2) + 120 * np.sin(3.1 * x)
for lo, hi, tok, name, cls in BELTS:
    top = np.minimum(profile, hi)
    m = profile > lo
    a.fill_between(x[m], lo, top[m], color=P.fill(tok), lw=0)
a.plot(x, profile, color=P.ink(), lw=1.4)
a.set_xlim(0, 10)
a.set_ylim(800, 5600)
a.set_xticks([])
charts.style_axes(a, None, "elevation / m")
a.spines["bottom"].set_visible(False)

# belt labels at the right
for lo, hi, tok, name, cls in BELTS:
    yc = 1.0 + 10.2 * (((lo + hi) / 2) - 800) / 4800
    ax.add_patch(Polygon([(12.4, yc - 0.55), (12.8, yc - 0.55), (12.8, yc + 0.55), (12.4, yc + 0.55)],
                         closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8))
    bio.label(ax, (13.0, yc + 0.25), name.split("\n")[0], size="tiny", ha="left", bold=True)
    rest = name.split("\n")[1:]
    if rest:
        bio.label(ax, (13.0, yc - 0.05), rest[0], size="tiny", ha="left", color=P.muted())

ANIMALS = {  # belt index: typical animals
    0: "rhesus macaque, bamboo rats, sunbirds, Oriental frogs",
    1: "golden pheasant, Temminck's tragopan, red panda",
    2: "giant panda, golden snub-nosed monkey, takin",
    3: "blood pheasant, Chinese monal, white-lipped deer",
    4: "Himalayan marmot, pikas, Tibetan snowcock",
}
for i, (lo, hi, tok, name, cls) in enumerate(BELTS):
    yc = 1.0 + 10.2 * (((lo + hi) / 2) - 800) / 4800
    bio.label(ax, (13.0, yc - 0.4 if len(name.split("\n")) > 1 else yc - 0.15), ANIMALS[i], size="tiny",
              ha="left", italic=False, color=P.ink())

# Palearctic / Oriental arrow
bio.arrow(ax, (0.5, 4.0), (0.5, 10.6), kind="process", color=P.edge("metabolite"))
bio.arrow(ax, (0.9, 8.0), (0.9, 1.4), kind="process", color=P.edge("plant"))
bio.label(ax, (0.25, 7.6), "Palearctic elements", size="tiny", rotation=90, color=P.edge("metabolite"))
bio.label(ax, (1.2, 4.6), "Oriental elements", size="tiny", rotation=90, color=P.edge("plant"))
bio.label(ax, (19.8, 0.4), "Schematic; elevations approximate", size="tiny", ha="right", color=P.muted())
