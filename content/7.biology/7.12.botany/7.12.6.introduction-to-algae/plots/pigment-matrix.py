"""Photosynthetic pigments and storage products of the algal groups (presence matrix).

Dark cell: principal light-harvesting or diagnostic pigment; light cell: present but minor; empty: absent.
Rows are grouped by the pigment combination (chlorophyll a with phycobiliproteins, with chlorophyll b,
with chlorophyll c). The right-hand column gives the main storage product and where it is stored
(P: inside the plastid; C: cytoplasm; V: vacuole). Compiled from Raven 8e Table 15-1, Graham et al.
Algae, and standard phycological sources."""
from matplotlib.patches import Rectangle
import wikibio as bio

P = bio.P
cols = ["Chl a", "Chl b", "Chl c", "Phycobili-\nproteins", "Lutein", "Fuco-\nxanthin", "Peridinin",
        "Allo-\nxanthin", "Diadino-\nxanthin"]
# value per column: 2 major, 1 present, 0 absent
rows = [
    ("Cyanobacteria", [2, 0, 0, 2, 0, 0, 0, 0, 0], "glycogen, cyanophycin (C)", 0),
    ("Glaucophytes", [2, 0, 0, 2, 0, 0, 0, 0, 0], "starch (C)", 0),
    ("Red algae", [2, 0, 0, 2, 1, 0, 0, 0, 0], "floridean starch (C)", 0),
    ("Prochlorophytes", [2, 2, 0, 0, 0, 0, 0, 0, 0], "glycogen (C)", 1),
    ("Green algae", [2, 2, 0, 0, 2, 0, 0, 0, 0], "starch (P)", 1),
    ("Euglenids", [2, 2, 0, 0, 0, 0, 0, 0, 1], "paramylon (C)", 1),
    ("Chlorarachniophytes", [2, 2, 0, 0, 1, 0, 0, 0, 0], "beta-1,3-glucan (C)", 1),
    ("Cryptophytes", [2, 0, 2, 2, 0, 0, 0, 2, 0], "starch (outside plastid)", 2),
    ("Haptophytes", [2, 0, 2, 0, 0, 2, 0, 0, 1], "chrysolaminarin (V)", 2),
    ("Dinoflagellates", [2, 0, 2, 0, 0, 0, 2, 0, 1], "starch (C), oil", 2),
    ("Golden algae", [2, 0, 2, 0, 0, 2, 0, 0, 0], "chrysolaminarin (V), oil", 2),
    ("Yellow-green algae", [2, 0, 1, 0, 0, 0, 0, 0, 2], "chrysolaminarin (V), oil", 2),
    ("Diatoms", [2, 0, 2, 0, 0, 2, 0, 0, 1], "chrysolaminarin (V), oil", 2),
    ("Brown algae", [2, 0, 2, 0, 0, 2, 0, 0, 0], "laminarin (V), mannitol", 2),
]
group_names = ["Chl a + phycobilins", "Chl a + b", "Chl a + c"]
group_tokens = ["negative", "plant", "highlight"]

cw, ch = 1.25, 0.62
x0, y0 = 4.3, 1.0
n = len(rows)
W = x0 + cw * len(cols) + 6.4
H = y0 + ch * n + 1.2
fig, ax = bio.canvas(W, H)
top = y0 + ch * n

for j, c in enumerate(cols):
    bio.label(ax, (x0 + cw * (j + 0.5), top + 0.55), c, size="tiny")
bio.label(ax, (x0 + cw * len(cols) + 0.25, top + 0.55), "Storage product (site)", size="tiny", ha="left")

for i, (name, vals, store, g) in enumerate(rows):
    y = top - ch * (i + 1)
    bio.label(ax, (x0 - 0.2, y + ch / 2), name, size="tiny", ha="right")
    for j, v in enumerate(vals):
        if v == 2:
            fc = P.fill(group_tokens[g])
        elif v == 1:
            fc = P.light(group_tokens[g])
        else:
            fc = "none"
        ax.add_patch(Rectangle((x0 + cw * j + 0.05, y + 0.05), cw - 0.1, ch - 0.1, facecolor=fc,
                               edgecolor=P.muted(), lw=0.4, zorder=5))
    bio.label(ax, (x0 + cw * len(cols) + 0.25, y + ch / 2), store, size="tiny", ha="left")

# group brackets on the left edge
starts = [0, 3, 7]
ends = [3, 7, n]
for g, (a, b) in enumerate(zip(starts, ends)):
    ya, yb = top - ch * a - 0.06, top - ch * b + 0.06
    xb = 0.55
    ax.plot([xb, xb], [yb, ya], color=P.edge(group_tokens[g]), lw=2.4, solid_capstyle="round", zorder=6)
    bio.label(ax, (xb - 0.25, (ya + yb) / 2), group_names[g], size="tiny", rotation=90,
              color=P.edge(group_tokens[g]))

# legend
ly = 0.45
ax.add_patch(Rectangle((x0, ly - 0.18), 0.5, 0.36, facecolor=P.fill("neutral"), edgecolor=P.muted(), lw=0.4))
bio.label(ax, (x0 + 0.65, ly), "principal / diagnostic", size="tiny", ha="left")
ax.add_patch(Rectangle((x0 + 4.0, ly - 0.18), 0.5, 0.36, facecolor=P.light("neutral"), edgecolor=P.muted(), lw=0.4))
bio.label(ax, (x0 + 4.65, ly), "present, minor", size="tiny", ha="left")
bio.label(ax, (x0 + 7.6, ly), "P plastid   C cytoplasm   V vacuole", size="tiny", ha="left", color=P.muted())
