# Sink-to-source transition of a eudicot leaf (schematic data following the typical pattern: export starts
# at about 25 % of final area and the transition is complete at 40-50 %). Import and export are given per
# leaf, relative to the maximum import; the net carbon balance is export - import. The inset sketches a
# leaf in transition: the tip already exports, the base still imports.
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon


def sig(x, x0, w):
    return 1 / (1 + np.exp(-(x - x0) / w))


area = np.linspace(0, 100, 400)
imp = (1 - sig(area, 30, 4.5)) * (0.25 + 0.75 * sig(area, 6, 3))
exp_ = 1.6 * sig(area, 36, 5) * (area / 100) ** 0.5
net = exp_ - imp
fig, ax = plt.subplots(figsize=(8.4, 4.4))
ax.axvspan(25, 47, color="0.55", alpha=0.13, lw=0)
ax.text(36, 1.47, "transition", ha="center", fontsize=9, color="0.35")
ax.plot(area, imp, color="#d9822b", lw=2.3, label="import")
ax.plot(area, exp_, color="#3a8a3a", lw=2.3, label="export")
ax.plot(area, net, color="#2f6fb5", lw=1.8, ls="--", label="net balance (export − import)")
ax.axhline(0, color="0.5", lw=0.7)
ax.set_xlabel("Leaf area / % of final area")
ax.set_ylabel("Assimilate flux (relative)")
ax.set_xlim(0, 100)
ax.set_ylim(-1.1, 1.6)
ax.legend(frameon=False, fontsize=9, loc="upper left")
ax.spines[["top", "right"]].set_visible(False)

ins = fig.add_axes([0.66, 0.13, 0.14, 0.22])
th = np.linspace(0, np.pi, 60)
xs = np.concatenate([0.5 * np.sin(th) ** 1.2, -0.5 * np.sin(th[::-1]) ** 1.2])
ys = np.concatenate([np.cos(th) * -1 + 1, np.cos(th[::-1]) * -1 + 1])
leaf = np.column_stack([xs, ys])
top = leaf[leaf[:, 1] >= 1.1]
bot = leaf[leaf[:, 1] <= 1.1]
ins.add_patch(Polygon(leaf[leaf[:, 1] >= 1.0], closed=True, facecolor="#3a8a3a", alpha=0.75, edgecolor="none"))
ins.add_patch(Polygon(leaf[leaf[:, 1] <= 1.0], closed=True, facecolor="#d9822b", alpha=0.75, edgecolor="none"))
ins.plot(leaf[:, 0], leaf[:, 1], color="0.3", lw=1)
ins.plot([0, 0], [-0.4, 2], color="0.3", lw=1)
ins.text(0.62, 1.6, "tip: source", fontsize=7)
ins.text(0.62, 0.35, "base: sink", fontsize=7)
ins.set_xlim(-0.7, 1.9)
ins.set_ylim(-0.5, 2.1)
ins.axis("off")
