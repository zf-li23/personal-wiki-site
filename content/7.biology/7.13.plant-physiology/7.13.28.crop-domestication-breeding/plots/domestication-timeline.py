# Approximate dates of domestication of some major crops in the independent centres of origin
# (thousands of years before present). Each bar spans the period from the earliest evidence of
# cultivation of the wild plant to the appearance of the domesticated form; values are rounded
# summaries of archaeobotanical syntheses (e.g. Larson et al. 2014, PNAS 111: 6139) and are
# uncertain by about 1000 years.
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

centres = [
    ("Southwest Asia\n(Fertile Crescent)", "protein",
     [("emmer & einkorn wheat", 11.5, 10.0), ("barley", 11.5, 10.0), ("lentil, pea", 11.0, 9.5)]),
    ("China: Yellow River", "highlight",
     [("broomcorn millet", 10.0, 8.0), ("foxtail millet", 10.0, 7.5), ("soybean", 9.0, 5.0)]),
    ("China: Yangtze", "enzyme", [("rice (japonica)", 10.0, 6.5)]),
    ("Mesoamerica", "plant", [("squash", 10.0, 9.0), ("maize", 9.0, 7.0), ("common bean", 8.0, 6.0)]),
    ("South America\n(Andes, Amazonia)", "petal", [("potato", 9.0, 7.0), ("cassava", 9.0, 7.0)]),
    ("New Guinea", "channel", [("taro, banana", 10.0, 7.0)]),
    ("Africa (Sahel)", "drug", [("sorghum", 6.0, 4.5), ("pearl millet", 5.5, 4.5), ("African rice", 3.5, 2.0)]),
]

fig, ax = plt.subplots(figsize=(10, 5.6))
y = 0
ticks, names = [], []
for centre, token, crops in centres:
    top = y
    for crop, start, end in crops:
        ax.barh(y, start - end, left=end, height=0.62, color=bio.P.fill(token), edgecolor=bio.P.edge(token), lw=1)
        ax.text(end - 0.15, y, crop, fontsize=8, va="center", ha="left", color=bio.P.ink())
        y -= 1
    ticks.append((top + y + 1) / 2)
    names.append(centre)
    ax.axhline(y + 0.5, color=bio.P.light("neutral"), lw=0.8)
    y -= 0.4
ax.set_yticks(ticks)
ax.set_yticklabels(names, fontsize=8.5)
ax.set_xlim(12, 0)
ax.set_ylim(y + 0.6, 0.7)
charts.style_axes(ax, "Thousand years before present", None)
ax.tick_params(axis="y", length=0)
ax.spines["left"].set_visible(False)
fig.tight_layout()
