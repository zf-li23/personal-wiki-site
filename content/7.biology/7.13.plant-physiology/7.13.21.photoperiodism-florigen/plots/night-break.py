# Night-break experiments (schematic). Left: 24 h light-dark cycles with a critical night length of
# about 9 h for an SDP and the same for an LDP; a short flash of red light (R) in the middle of a long
# night prevents flowering of the SDP and promotes flowering of the LDP; far-red (FR) given right after
# R reverses the effect, and the last flash decides. Right: effectiveness of a 1 h red night break given
# at different times of a 16 h night (illustrative curve, after classic Xanthium data): a night break
# is most effective near the middle of the night.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

rows = [
    ("16 h light", 16, [], "no", "yes"),
    ("8 h light", 8, [], "yes", "no"),
    ("8 h light + R", 8, ["R"], "no", "yes"),
    ("8 h light + R, FR", 8, ["R", "FR"], "yes", "no"),
    ("8 h light + R, FR, R", 8, ["R", "FR", "R"], "no", "yes"),
]
col = {"R": "#d93a2b", "FR": "#a0466e"}

fig, (ax, bx) = plt.subplots(1, 2, figsize=(11, 4.2), gridspec_kw={"width_ratios": [1.9, 1]})
for i, (name, light, flashes, sdp, ldp) in enumerate(rows):
    y = len(rows) - 1 - i
    ax.add_patch(Rectangle((0, y + 0.2), light, 0.6, facecolor="#f2c94c", edgecolor="0.3", lw=0.8))
    ax.add_patch(Rectangle((light, y + 0.2), 24 - light, 0.6, facecolor="0.25", edgecolor="0.3", lw=0.8))
    mid = light + (24 - light) / 2
    for k, f in enumerate(flashes):
        x = mid - 0.45 * (len(flashes) - 1) + 0.9 * k
        ax.add_patch(Rectangle((x - 0.3, y + 0.12), 0.6, 0.76, facecolor=col[f], edgecolor="none"))
        ax.text(x, y + 0.98, f, ha="center", va="bottom", fontsize=7, color=col[f])
    ax.text(-0.5, y + 0.5, name, ha="right", va="center", fontsize=8.5)
    for xx, res in ((27.8, sdp), (33.6, ldp)):
        ax.text(xx, y + 0.5, "flowers" if res == "yes" else "vegetative", ha="center", va="center", fontsize=8.5,
                color="#2e8b57" if res == "yes" else "0.45", weight="bold" if res == "yes" else "normal")
ax.text(27.8, len(rows) + 0.15, "SDP", ha="center", fontsize=9, weight="bold")
ax.text(33.6, len(rows) + 0.15, "LDP", ha="center", fontsize=9, weight="bold")
ax.set_xlim(-10, 36.5)
ax.set_ylim(-0.3, len(rows) + 0.6)
ax.set_xticks([0, 6, 12, 18, 24])
ax.set_xlabel("Time from dawn / h")
ax.set_yticks([])
for s in ("top", "right", "left"):
    ax.spines[s].set_visible(False)
ax.spines["bottom"].set_bounds(0, 24)

t = np.linspace(0, 16, 400)
eff = 100 * np.exp(-((t - 8) / 2.6) ** 2)
bx.plot(t, eff, color="#d93a2b", lw=2.2)
bx.fill_between(t, eff, color="#d93a2b", alpha=0.12, lw=0)
bx.set_xlim(0, 16)
bx.set_ylim(0, 110)
bx.set_xticks([0, 4, 8, 12, 16])
bx.set_xlabel("Time of night break after dusk / h")
bx.set_ylabel("Inhibition of SDP flowering / %")
bx.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
