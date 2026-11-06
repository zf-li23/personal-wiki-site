# Effects of the nine classes of plant hormones on major processes (a summary).
# +1 promotes, -1 inhibits, 0 little / variable, 2 = depends on concentration or species (shown as "±").
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

hormones = ["Auxin", "GA", "Cytokinin", "ABA", "Ethylene", "BR", "JA", "SA", "SL"]
rows = [
    ("Stem / hypocotyl elongation", [2, 1, 0, -1, -1, 1, -1, 0, 0]),
    ("Root elongation", [2, 1, -1, 2, -1, 2, -1, 0, 0]),
    ("Lateral / adventitious roots", [1, -1, -1, -1, 1, 1, 0, 0, -1]),
    ("Cell division", [1, 1, 1, -1, 0, 1, -1, 0, 0]),
    ("Shoot branching (bud outgrowth)", [-1, 0, 1, -1, 0, 1, 0, 0, -1]),
    ("Vascular / xylem differentiation", [1, 1, 1, 0, 0, 1, 0, 0, 1]),
    ("Seed dormancy", [0, -1, -1, 1, -1, -1, 0, 0, 0]),
    ("Germination", [0, 1, 1, -1, 1, 1, -1, 0, 0]),
    ("Flowering (bolting, LD rosettes)", [0, 1, 0, -1, 2, 1, 0, 0, 0]),
    ("Fruit set / parthenocarpy", [1, 1, 1, 0, 0, 1, 0, 0, 0]),
    ("Fruit ripening (climacteric)", [0, -1, -1, 1, 1, 0, 1, 0, 0]),
    ("Leaf senescence", [-1, -1, -1, 1, 1, 0, 1, 1, 1]),
    ("Abscission", [-1, 0, -1, 1, 1, 0, 1, 0, 0]),
    ("Stomatal opening", [0, 0, 1, -1, 0, 0, -1, -1, 0]),
    ("Defence: biotrophic pathogens", [0, 0, 0, -1, 0, 0, -1, 1, 0]),
    ("Defence: herbivores, necrotrophs", [0, 0, 0, 0, 1, 0, 1, -1, 0]),
    ("Abiotic stress tolerance", [0, 0, 0, 1, 0, 1, 0, 0, 0]),
    ("Arbuscular mycorrhiza", [0, -1, 0, 0, -1, 0, 0, 0, 1]),
]
M = np.array([r[1] for r in rows], float)
col = np.where(M == 2, 3, M + 1)     # 0 inhibit, 1 neutral, 2 promote, 3 depends
cmap = ListedColormap(["#d9706b", "#eceff3", "#6fb26a", "#e3c35c"])

fig, ax = plt.subplots(figsize=(8.6, 8.4))
ax.imshow(col, cmap=cmap, vmin=-0.5, vmax=3.5, aspect="auto")
sym = {-1: "−", 0: "", 1: "+", 2: "±"}
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        ax.text(j, i, sym[int(M[i, j])], ha="center", va="center", fontsize=11, color="#2b2f36")
ax.set_xticks(range(len(hormones)), hormones, rotation=40, ha="right")
ax.set_yticks(range(len(rows)), [r[0] for r in rows])
ax.set_xticks(np.arange(-0.5, len(hormones)), minor=True)
ax.set_yticks(np.arange(-0.5, len(rows)), minor=True)
ax.grid(which="minor", color="white", lw=1.5)
ax.tick_params(which="minor", length=0)
ax.tick_params(length=0)
for s in ax.spines.values():
    s.set_visible(False)
ax.xaxis.tick_top()
ax.set_xticklabels(hormones, rotation=40, ha="left")
fig.tight_layout()
