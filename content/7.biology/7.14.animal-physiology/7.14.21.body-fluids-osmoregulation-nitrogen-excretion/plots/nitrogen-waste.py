# The three nitrogenous wastes compared (order-of-magnitude values).
# A: water needed to excrete 1 g of nitrogen (Schmidt-Nielsen's estimates: ammonia 300-500 mL, urea about
#    50 mL, uric acid about 10 mL or less, excreted as a paste or solid).
# B: ATP equivalents per nitrogen atom: ammonia 0; urea 2 (urea cycle, 4 high-energy phosphate bonds per urea);
#    uric acid about 2 (estimate: de novo purine synthesis about 6 ATP equivalents per IMP plus glutamine
#    synthesis for 2 of its 4 nitrogens), and carbon atoms lost per nitrogen (0, 0.5, 1.25).
# C: highest concentration tolerated or reached in body fluids: ammonia about 0.05 mM in mammalian blood
#    (toxic above about 1 mM); urea about 350-400 mM in elasmobranch plasma; uric acid saturates near 0.4 mM.
import matplotlib.pyplot as plt
import numpy as np

names = ["Ammonia", "Urea", "Uric acid"]
cols = ["#2f6fb5", "#3c9a5f", "#c77c1e"]
x = np.arange(3)

fig, axs = plt.subplots(1, 3, figsize=(11, 3.9))
ax = axs[0]
water = np.array([400, 50, 10])
lo = np.array([300, 40, 1])
hi = np.array([500, 60, 10])
ax.bar(x, water, color=cols, width=0.6)
ax.errorbar(x, water, yerr=[water - lo, hi - water], fmt="none", ecolor="black", capsize=4, lw=1)
ax.set_yscale("log")
ax.set_ylim(0.5, 2000)
ax.set_ylabel("Water per g N excreted (mL)")
ax.set_title("A  Water cost", loc="left", fontsize=11, fontweight="bold")

ax = axs[1]
atp = np.array([0, 2.0, 2.0])
carbon = np.array([0, 0.5, 1.25])
w = 0.36
ax.bar(x - w / 2, atp, width=w, color=cols, label="ATP equivalents per N")
ax.bar(x + w / 2, carbon, width=w, color=cols, alpha=0.45, hatch="//", label="C atoms lost per N")
ax.errorbar([2 - w / 2], [2.0], yerr=[[0.3], [0.5]], fmt="none", ecolor="black", capsize=4, lw=1)
ax.set_ylim(0, 3)
ax.set_ylabel("Per nitrogen atom")
ax.set_title("B  Energy and carbon cost", loc="left", fontsize=11, fontweight="bold")
ax.legend(frameon=False, fontsize=8, loc="upper left")

ax = axs[2]
conc = np.array([0.05, 400, 0.4])
ax.bar(x, conc, color=cols, width=0.6)
ax.set_yscale("log")
ax.set_ylim(0.01, 3000)
ax.axhline(1.0, color="#c0392b", lw=0.9, ls="--")
ax.text(-0.35, 1.25, "ammonia toxic", fontsize=8, color="#c0392b")
ax.text(2, 0.55, "saturates", fontsize=8, ha="center")
ax.set_ylabel("Concentration in body fluids (mM)")
ax.set_title("C  Toxicity and solubility", loc="left", fontsize=11, fontweight="bold")

for ax in axs:
    ax.set_xticks(x)
    ax.set_xticklabels(names)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
