# Ecological pyramids from a model food chain (Proposition 43.4.1).
# Production: NPP 1000 kJ m^-2 yr^-1, transfer efficiencies 13%, 10%, 10%.
# Biomass B = P / (P/B) with turnover ratios 300, 20, 2, 0.5 per year (energy -> biomass at 20 kJ/g).
# Numbers (forest, per hectare, illustrative): 400 trees, 1e6 herbivorous insects, 5e4 predatory arthropods, 4 birds.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import ecology

P = bio.P
fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.4))
names = ["Producers", "Herbivores", "Carnivores", "Top carnivores"]
toks = ["plant", "antibody", "rna", "negative"]
prod = [1000.0]
for te in (0.13, 0.10, 0.10):
    prod.append(prod[-1] * te)
turn = [300, 20, 2, 0.5]
biom = [p / t / 20 for p, t in zip(prod, turn)]  # g dry mass m^-2
nums = [400, 1e6, 5e4, 4]
specs = [
    ("A  Production (kJ m⁻² yr⁻¹)", prod, "linear", "{:,.4g}"),
    ("B  Biomass (g m⁻²), log width", biom, "log", "{:.2g}"),
    ("C  Numbers (per ha, forest), log width", nums, "log", "{:,.0f}"),
]
labels_c = ["Trees", "Herbivorous insects", "Predatory arthropods", "Insectivorous birds"]
for k, (ax, (title, vals, scale, fmt)) in enumerate(zip(axes, specs)):
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5.2)
    ax.axis("off")
    levels = []
    for i in range(4):
        levels.append(dict(text=(labels_c if k == 2 else names)[i], value=vals[i], token=toks[i]))
    ecology.pyramid(ax, (4.6, 0.4), levels, width=7.4, height=1.05, scale=scale, value_fmt=fmt,
                    label_inside=False, size="small")
    ax.set_title(title, loc="left", fontweight="bold", fontsize=10)
fig.tight_layout()
