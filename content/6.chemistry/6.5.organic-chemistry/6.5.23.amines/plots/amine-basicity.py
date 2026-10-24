"""pKa of the conjugate acids of common nitrogen bases in water at 25 C (the unified table of 6.5.3,
CRC values; DMAP from the same table). Bars are grouped by the kind of nitrogen: amidine/guanidine,
alkylamines, sp2 nitrogen and arylamines, and amides."""

import matplotlib.pyplot as plt

DATA = [
    ("guanidine", 13.6, 0),
    ("pyrrolidine", 11.27, 1),
    ("piperidine", 11.12, 1),
    ("triethylamine", 10.75, 1),
    ("dimethylamine", 10.73, 1),
    ("methylamine", 10.66, 1),
    ("trimethylamine", 9.80, 1),
    ("DMAP", 9.6, 2),
    ("ammonia", 9.25, 1),
    ("imidazole", 6.99, 2),
    ("pyridine", 5.23, 2),
    ("aniline", 4.60, 2),
    ("4-nitroaniline", 1.0, 2),
    ("acetamide (O)", -0.5, 3),
]
GROUPS = ["amidine / guanidine", "alkylamines", "sp$^2$ N, arylamines", "amides"]
COLORS = ["C3", "C0", "C2", "C1"]

fig, ax = plt.subplots(figsize=(6.4, 4.6))
names = [d[0] for d in DATA][::-1]
values = [d[1] for d in DATA][::-1]
groups = [d[2] for d in DATA][::-1]
ax.barh(range(len(DATA)), values, color=[COLORS[g] for g in groups], height=0.7)
for i, v in enumerate(values):
    ax.text(v + (0.15 if v >= 0 else -0.15), i, f"{v:g}", va="center", ha="left" if v >= 0 else "right", fontsize=8)
ax.set_yticks(range(len(DATA)), names)
ax.axvline(0, color="black", lw=0.8)
ax.set_xlim(-2, 15)
ax.set_xlabel(r"p$K_\mathrm{a}$ of the conjugate acid (water, 25 $^\circ$C)")
handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in COLORS]
ax.legend(handles, GROUPS, loc="lower right", fontsize=8, frameon=False)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
