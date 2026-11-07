# Flowering responses to day length (schematic, illustrative curves).
# Left: qualitative (obligate) responses have a sharp threshold at the critical day length
# (LDP Hyoscyamus niger, about 11.5 h; SDP Xanthium strumarium, about 15.5 h); between 11.5 and 15.5 h
# both flower, so the critical day length of an LDP can be shorter than that of an SDP.
# Right: quantitative (facultative) LDP and SDP, and a day-neutral plant, shown as days to flowering.
import matplotlib.pyplot as plt
import numpy as np

L = np.linspace(4, 24, 600)


def sig(x, x0, s):
    return 1 / (1 + np.exp(-(x - x0) / s))


fig, (ax, bx) = plt.subplots(1, 2, figsize=(10.5, 4.2))
ldp = 100 * sig(L, 11.5, 0.12)
sdp = 100 * (1 - sig(L, 15.5, 0.12)) * sig(L, 5.0, 0.6)
ax.axvspan(11.5, 15.5, color="#9c6bc4", alpha=0.12, lw=0)
ax.plot(L, ldp, color="#2f6fb5", lw=2.2, label="qualitative LDP (Hyoscyamus)")
ax.plot(L, sdp, color="#d9822b", lw=2.2, label="qualitative SDP (Xanthium)")
ax.axvline(11.5, color="#2f6fb5", lw=0.8, ls="--")
ax.axvline(15.5, color="#d9822b", lw=0.8, ls="--")
ax.text(13.5, 50, "both\nflower", ha="center", va="center", fontsize=9, color="#6d3f96")
ax.text(11.4, 104, "11.5 h", ha="right", fontsize=8, color="#2f6fb5")
ax.text(15.6, 104, "15.5 h", ha="left", fontsize=8, color="#b0661c")
ax.set_xlim(4, 24)
ax.set_ylim(0, 112)
ax.set_xlabel("Day length / h")
ax.set_ylabel("Plants flowering / %")
ax.legend(frameon=False, fontsize=8, loc="lower left", bbox_to_anchor=(0.0, 0.12))
ax.spines[["top", "right"]].set_visible(False)

dmin = 30
q_ldp = dmin + 90 * (1 - sig(L, 13, 1.4))
q_sdp = dmin + 90 * sig(L, 13, 1.4)
dnp = dmin + 12 + 0 * L
bx.plot(L, q_ldp, color="#2f6fb5", lw=2.2, label="quantitative LDP")
bx.plot(L, q_sdp, color="#d9822b", lw=2.2, label="quantitative SDP")
bx.plot(L, dnp, color="#3a9a5b", lw=2.2, label="day-neutral")
bx.set_xlim(4, 24)
bx.set_ylim(0, 135)
bx.set_xlabel("Day length / h")
bx.set_ylabel("Days to flowering / d")
bx.legend(frameon=False, fontsize=8, loc="upper center")
bx.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
