# Altitudinal zonation on three mountains in China (simplified; approximate boundaries in meters).
# Same vegetation type -> same color across mountains.
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import wikibio as bio

P = bio.P
TYPES = {
    "trop": ("Tropical lowland / seasonal rain forest", "thylakoid"),
    "mrain": ("Montane rain forest", "peroxisome"),
    "evb": ("Evergreen broadleaf forest", "plant"),
    "dec": ("Deciduous broadleaf forest", "golgi"),
    "mix": ("Mixed coniferous-broadleaf forest", "enzyme"),
    "con": ("Subalpine coniferous forest (spruce, fir)", "dna"),
    "krum": ("Birch krummholz", "lipid_tail"),
    "shrub": ("Alpine shrubland and meadow", "rna"),
    "tundra": ("Alpine tundra", "neutral"),
    "sparse": ("Sparse alpine vegetation (scree)", "bone"),
    "snow": ("Permanent snow and ice", "extracellular"),
}
MOUNTAINS = [
    ("Changbai Shan\n42° N, 2691 m",
     [(250, 500, "dec"), (500, 1100, "mix"), (1100, 1800, "con"), (1800, 2100, "krum"), (2100, 2691, "tundra")]),
    ("Yushan\n23.5° N, 3952 m",
     [(0, 600, "trop"), (600, 900, "mrain"), (900, 1800, "evb"), (1800, 3000, "mix"), (3000, 3600, "con"),
      (3600, 3952, "shrub")]),
    ("Namcha Barwa (south slope)\n29.6° N, 7782 m",
     [(600, 1100, "trop"), (1100, 2400, "evb"), (2400, 2800, "mix"), (2800, 3900, "con"), (3900, 4500, "shrub"),
      (4500, 5000, "sparse"), (5000, 7782, "snow")]),
]

fig, ax = plt.subplots(figsize=(10.4, 6.4))
W = 1.0
for i, (name, belts) in enumerate(MOUNTAINS):
    x = i * 2.2
    for lo, hi, key in belts:
        tok = TYPES[key][1]
        ax.add_patch(Rectangle((x, lo), W, hi - lo, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8))
        ax.text(x + W + 0.06, lo, f"{lo:,}", fontsize=7, va="center", ha="left", color=P.muted())
    ax.text(x + W + 0.06, belts[-1][1], f"{belts[-1][1]:,}", fontsize=7, va="center", ha="left", color=P.muted())
    ax.text(x + W / 2, -350, name, ha="center", va="top", fontsize=8.5, color=P.ink())
used = []
for _, belts in MOUNTAINS:
    for _, _, k in belts:
        if k not in used:
            used.append(k)
order = ["trop", "mrain", "evb", "dec", "mix", "con", "krum", "shrub", "tundra", "sparse", "snow"]
for j, k in enumerate([k for k in order if k in used][::-1]):
    name, tok = TYPES[k]
    y = 7600 - j * 560
    ax.add_patch(Rectangle((6.9, y - 180), 0.35, 360, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8))
    ax.text(7.35, y, name, fontsize=8, va="center", ha="left", color=P.ink())
ax.set_xlim(-0.3, 11.2)
ax.set_ylim(-1300, 8000)
ax.set_yticks(range(0, 8001, 1000))
ax.set_ylabel("Elevation / m")
ax.set_xticks([])
for s in ("top", "right", "bottom"):
    ax.spines[s].set_visible(False)
ax.spines["left"].set_bounds(0, 8000)
fig.tight_layout()
