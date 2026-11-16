# Space-time (Stommel-type) diagram of ecological phenomena. Each ellipse spans the typical spatial
# extent (m) and characteristic time (s) of a process, both on log10 axes; positions are
# order-of-magnitude placements (schematic), in the spirit of Stommel (1963) and Delcourt et al. (1983).
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import wikibio as bio

P = bio.P

# (label, log10 space centre, log10 time centre, width in decades, height in decades, angle, token)
items = [
    ("enzyme kinetics,\nphotosynthesis", -5.0, 0.0, 3.0, 3.2, 20, "enzyme"),
    ("thermoregulation,\nforaging bouts", -0.6, 3.6, 3.0, 2.6, 25, "animal"),
    ("growth and\ndevelopment", -1.0, 6.4, 2.6, 2.4, 20, "plant"),
    ("population\ndynamics", 2.6, 8.0, 4.2, 2.6, 25, "dna"),
    ("dispersal and\nmigration", 4.6, 6.6, 3.4, 2.6, 30, "channel"),
    ("succession", 2.8, 10.0, 3.4, 2.6, 20, "positive"),
    ("nutrient\ncycling", 5.2, 9.0, 4.0, 2.6, 25, "atp"),
    ("biome shifts,\nglacial cycles", 6.4, 11.8, 2.8, 2.2, 15, "metabolite"),
    ("speciation", 5.0, 13.0, 3.4, 2.0, 10, "rna"),
]

fig, ax = plt.subplots(figsize=(8.2, 5.8))
for text, x, y, w, h, ang, tok in items:
    ax.add_patch(Ellipse((x, y), w, h, angle=ang, facecolor=P.light(tok), edgecolor=P.edge(tok), lw=1.2,
                         alpha=0.85))
    ax.text(x, y, text, ha="center", va="center", fontsize=8, color=P.ink())

# disturbance events: short and patchy, placed as points
events = [("treefall gap", 1.5, 5.0), ("wildfire", 5.0, 5.4), ("hurricane", 5.8, 4.9)]
for text, x, y in events:
    ax.plot(x, y, marker="D", ms=5, color=P.edge("negative"))
    ax.text(x + 0.15, y - 0.45, text, fontsize=7.5, color=P.edge("negative"), ha="left")

ax.set_xlim(-7.5, 8)
ax.set_ylim(-2, 15)
xt = [-6, -3, 0, 3, 6]
ax.set_xticks(xt)
ax.set_xticklabels(["1 µm", "1 mm", "1 m", "1 km", "1000 km"])
yticks = [(0, "1 s"), (np.log10(3600), "1 h"), (np.log10(86400), "1 d"), (np.log10(3.156e7), "1 yr"),
          (np.log10(3.156e9), "100 yr"), (np.log10(3.156e11), "10 kyr"), (np.log10(3.156e13), "1 Myr")]
ax.set_yticks([v for v, _ in yticks])
ax.set_yticklabels([t for _, t in yticks])
ax.set_xlabel("Spatial extent (log scale)")
ax.set_ylabel("Characteristic time (log scale)")
ax.plot([-7, 7.5], [-1.0, 14.0], ls=(0, (4, 3)), color=P.muted(), lw=0.8)
ax.text(-4.6, 6.0, "larger processes\nare slower", fontsize=7.5, color=P.muted(), ha="center", rotation=40)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
