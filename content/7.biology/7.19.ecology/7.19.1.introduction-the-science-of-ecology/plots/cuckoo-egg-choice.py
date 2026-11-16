# Nest-choice experiment with common cuckoos (Cuculus canorus) parasitizing Daurian redstarts
# (Phoenicurus auroreus). Each active redstart nest (centre) was flanked at 0.5 m by two unattended
# nest boxes holding a blue or a pink model clutch. Bars: number of cuckoo eggs laid in each box,
# read from Fig. 2 of Zhang et al. (2023) Proc. R. Soc. B 290: 20222094.
# A: host clutch blue (4 / 9 / 0 eggs in the blue box / host nest / pink box);
# B: host clutch pink (7 / 1 / 1).
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyBboxPatch
import wikibio as bio

P = bio.P
BLUE, PINK = P.fill("dna"), P.fill("petal")

panels = [
    ("A  Host clutch blue", [("blue", "empty box"), ("blue", "host nest"), ("pink", "empty box")], [4, 9, 0]),
    ("B  Host clutch pink", [("blue", "empty box"), ("pink", "host nest"), ("pink", "empty box")], [7, 1, 1]),
]

fig, axs = plt.subplots(1, 2, figsize=(9.0, 4.0), sharey=True)
for ax, (title, boxes, counts) in zip(axs, panels):
    xs = [0, 1, 2]
    for x, (col, kind), n in zip(xs, boxes, counts):
        c = BLUE if col == "blue" else PINK
        e = P.edge("dna") if col == "blue" else P.edge("petal")
        if n > 0:
            ax.bar(x, n, width=0.55, color=c, edgecolor=e, lw=1.0)
        ax.text(x, n + 0.25, str(n), ha="center", fontsize=9, color=P.ink())
        # nest box with clutch below the axis
        ax.add_patch(FancyBboxPatch((x - 0.3, -2.9), 0.6, 1.6, boxstyle="round,pad=0.02",
                                    facecolor=P.light("animal"), edgecolor=P.edge("animal"), lw=1.0,
                                    clip_on=False))
        for k, dx in enumerate((-0.15, 0.0, 0.15)):
            ax.add_patch(Ellipse((x + dx, -2.2 + 0.18 * (k % 2)), 0.11, 0.42, facecolor=c, edgecolor=e,
                                 lw=0.7, clip_on=False))
        ax.text(x, -3.25, kind, ha="center", va="top", fontsize=8, color=P.ink())
    ax.annotate("", xy=(0.3, -0.75), xytext=(0.7, -0.75), arrowprops=dict(arrowstyle="<->", color=P.muted()),
                annotation_clip=False)
    ax.annotate("", xy=(1.3, -0.75), xytext=(1.7, -0.75), arrowprops=dict(arrowstyle="<->", color=P.muted()),
                annotation_clip=False)
    ax.text(0.5, -0.65, "0.5 m", ha="center", va="bottom", fontsize=7, color=P.muted())
    ax.text(1.5, -0.65, "0.5 m", ha="center", va="bottom", fontsize=7, color=P.muted())
    ax.set_xlim(-0.6, 2.6)
    ax.set_ylim(0, 10.5)
    ax.set_xticks([])
    ax.set_title(title, loc="left", fontsize=10, fontweight="bold", color=P.ink())
    for s in ("top", "right", "bottom"):
        ax.spines[s].set_visible(False)
axs[0].set_ylabel("Cuckoo eggs laid")
fig.subplots_adjust(left=0.08, right=0.98, top=0.9, bottom=0.3, wspace=0.12)
