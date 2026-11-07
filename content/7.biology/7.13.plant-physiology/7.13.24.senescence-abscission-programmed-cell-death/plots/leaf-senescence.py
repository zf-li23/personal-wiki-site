# Time course of leaf senescence (illustrative logistic curves, after typical data for annual crops).
# Each variable declines as y = y_end + (1 - y_end) / (1 + exp((t - t50) / s)) from its value in the
# mature leaf (1). Net photosynthesis falls first (t50 = 28 d), soluble protein and Rubisco next
# (t50 = 33 d), chlorophyll later (t50 = 38 d); leaf nitrogen falls to about half of its mature value
# because about 50 % of the nitrogen is resorbed (remobilized) to young leaves and seeds.
# Grey band: onset of visible yellowing (chlorophyll below 70 %).
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 60, 600)


def decline(t50, s, y_end):
    return y_end + (1 - y_end) / (1 + np.exp((t - t50) / s))


curves = [
    ("net photosynthesis", decline(28, 3.5, 0.0), "#3a9a5b", "-"),
    ("soluble protein (Rubisco)", decline(33, 3.5, 0.08), "#9c6bc4", "-"),
    ("chlorophyll", decline(38, 3.0, 0.05), "#2e8b57", "--"),
    ("leaf nitrogen", decline(36, 4.0, 0.5), "#2f6fb5", "-"),
]
fig, ax = plt.subplots(figsize=(8.2, 4.3))
chl = curves[2][1]
k = np.argmax(chl < 0.7)
ax.axvspan(t[k], 60, color="#e0b04a", alpha=0.15, lw=0)
ax.text(t[k] + 0.5, 1.07, "visible yellowing", fontsize=8, color="#9a7000")
for lab, y, col, ls in curves:
    ax.plot(t, 100 * y, color=col, lw=2.2, ls=ls, label=lab)
ax.annotate("resorbed N ≈ 50 %", (55, 52), (44, 75), fontsize=8, arrowprops=dict(arrowstyle="-", color="0.5", lw=0.7))
ax.set_xlabel("Days after full leaf expansion / d")
ax.set_ylabel("Per cent of mature-leaf value")
ax.set_xlim(0, 60)
ax.set_ylim(0, 112)
ax.legend(frameon=False, fontsize=8, loc="lower left")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
