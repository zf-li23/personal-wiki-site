# Daily course of stomatal aperture and of the guard-cell potassium and sucrose contents in intact
# broad-bean leaves, sketched after the pattern reported by Talbott & Zeiger (1998). Values are
# relative (0-1); smooth logistic pieces reproduce the timing: K+ rises with the morning opening and
# falls after midday while the aperture is still wide; sucrose accumulates slowly and becomes the main
# osmoticum in the afternoon; closure at dusk parallels the sucrose decline.
import matplotlib.pyplot as plt
import numpy as np


def sig(t, t0, w):
    return 1 / (1 + np.exp(-(t - t0) / w))


t = np.linspace(5, 23, 600)
aperture = 0.95 * sig(t, 8.4, 0.7) * (1 - sig(t, 18.6, 0.7)) + 0.05 + 0.05 * np.exp(-((t - 14) / 2.5) ** 2)
aperture = aperture / aperture.max()
k = 0.08 + 0.9 * sig(t, 8.2, 0.6) * (1 - sig(t, 13.4, 0.9))
suc = 0.1 + 0.85 * sig(t, 11.8, 1.3) * (1 - sig(t, 19.0, 0.8))

fig, ax = plt.subplots(figsize=(8.6, 4.6))
ax.axvspan(7.2, 13.4, ymin=0, ymax=0.06, color="#d98c3a", alpha=0.55, lw=0)
ax.axvspan(13.4, 19.5, ymin=0, ymax=0.06, color="#4f8fc0", alpha=0.55, lw=0)
ax.text(10.3, 0.075, "K+ phase", ha="center", va="center", fontsize=9)
ax.text(16.45, 0.075, "sucrose phase", ha="center", va="center", fontsize=9)
ax.plot(t, aperture, color="#3a9a4a", lw=2.6, label="Stomatal aperture")
ax.plot(t, k, color="#d98c3a", lw=2.0, label="Guard-cell K+")
ax.plot(t, suc, color="#4f8fc0", lw=2.0, ls="--", label="Guard-cell sucrose")
ax.axvspan(5, 6.2, color="0.5", alpha=0.18, lw=0)
ax.axvspan(20.2, 23, color="0.5", alpha=0.18, lw=0)
ax.text(5.6, 0.5, "night", rotation=90, va="center", ha="center", fontsize=8, color="0.45")
ax.text(21.6, 0.5, "night", rotation=90, va="center", ha="center", fontsize=8, color="0.45")
ax.set_xlim(5, 23)
ax.set_ylim(0, 1.08)
ax.set_xticks([6, 9, 12, 15, 18, 21])
ax.set_xticklabels(["06:00", "09:00", "12:00", "15:00", "18:00", "21:00"])
ax.set_xlabel("Time of day")
ax.set_ylabel("Relative value")
ax.legend(frameon=False, fontsize=9, loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.12))
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
