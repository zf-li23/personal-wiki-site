# Seed development of a cereal grain (schematic, illustrative curves).
# Top: dry mass (logistic grain filling, W = Wmax / (1 + exp(-k (t - tm)))) and water content (% of
# fresh mass) falling from about 80 % to about 12 % at harvest maturity; the phases are
# histodifferentiation (embryogenesis, cell division), storage-reserve accumulation and maturation
# drying (desiccation). Bottom: sequential peaks of endogenous hormones: cytokinins (around the end of
# fertilization and early endosperm cell division), gibberellins and auxin (rapid filling), and abscisic
# acid (maturation, desiccation tolerance and dormancy).
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 50, 500)
dry = 100 / (1 + np.exp(-0.22 * (t - 22)))
water = 12 + 70 / (1 + np.exp(0.22 * (t - 34)))


def peak(t, c, w):
    return np.exp(-((t - c) / w) ** 2)


fig, (ax, bx) = plt.subplots(2, 1, figsize=(7.8, 5.6), sharex=True)
ax.plot(t, dry, color="#d9822b", lw=2.2, label="dry mass (% of final)")
ax.plot(t, water, color="#2f6fb5", lw=2.2, label="water content (% of fresh mass)")
for x0, x1, lab in ((0, 10, "histodifferentiation"), (10, 34, "reserve accumulation"), (34, 50, "maturation drying")):
    ax.axvline(x1, color="0.75", lw=0.8)
    ax.text((x0 + x1) / 2, 104, lab, ha="center", fontsize=8, color="0.35")
ax.set_ylim(0, 112)
ax.set_ylabel("Per cent")
ax.legend(frameon=False, fontsize=8, loc="center right")
bx.plot(t, peak(t, 6, 3.0), color="#3a9a5b", lw=2.2, label="cytokinins")
bx.plot(t, 0.8 * peak(t, 17, 5.0), color="#9c6bc4", lw=2.2, label="gibberellins")
bx.plot(t, 0.7 * peak(t, 24, 6.0), color="#d93a6b", lw=2.2, ls="--", label="auxin")
bx.plot(t, peak(t, 33, 6.0), color="#2f6fb5", lw=2.2, label="abscisic acid")
for x1 in (10, 34):
    bx.axvline(x1, color="0.75", lw=0.8)
bx.set_ylim(0, 1.15)
bx.set_ylabel("Relative content")
bx.set_xlabel("Days after anthesis / d")
bx.set_xlim(0, 50)
bx.legend(frameon=False, fontsize=8, ncol=2, loc="upper right")
for a, letter in zip((ax, bx), "AB"):
    a.spines[["top", "right"]].set_visible(False)
    a.text(-0.1, 1.0, letter, transform=a.transAxes, fontsize=12, weight="bold")
fig.tight_layout()
