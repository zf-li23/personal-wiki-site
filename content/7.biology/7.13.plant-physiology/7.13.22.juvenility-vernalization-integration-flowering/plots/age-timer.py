# The miR156-SPL age timer (minimal model, illustrative parameters).
# miR156 falls as the plant grows, m(n) = m0 exp(-n / lam) with n the number of leaves produced; sugar
# from the growing shoot represses MIR156 genes, so plants with reduced photosynthesis (e.g. repeated
# defoliation) have a larger lam. SPL protein is repressed by miR156: s = 1 / (1 + m / Km).
# Adult traits (abaxial trichomes in Arabidopsis) appear and the shoot becomes competent to flower
# when s exceeds a threshold (dotted line).
import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0, 20, 400)
m0, Km, thr = 1.0, 0.12, 0.5
fig, ax = plt.subplots(figsize=(7.5, 4.0))
for lam, ls, lab in ((4.0, "-", "normal growth"), (7.0, "--", "low sugar (defoliated)")):
    m = m0 * np.exp(-n / lam)
    s = 1 / (1 + m / Km)
    ax.plot(n, m, color="#d9822b", lw=2, ls=ls)
    ax.plot(n, s, color="#2f6fb5", lw=2, ls=ls)
    k = np.argmax(s > thr)
    ax.plot(n[k], s[k], "o", color="#2f6fb5", ms=6)
    ax.annotate(lab, (n[k], s[k]), (n[k] + 0.6, s[k] - 0.17), fontsize=8,
                arrowprops=dict(arrowstyle="-", color="0.5", lw=0.7))
ax.axhline(thr, color="0.4", lw=0.9, ls=":")
ax.text(19.8, thr + 0.03, "threshold: adult phase", ha="right", fontsize=8, color="0.35")
ax.text(1.0, 0.93, "miR156", color="#b0661c", fontsize=9)
ax.text(15.0, 0.93, "SPL", color="#2f6fb5", fontsize=9)
ax.set_xlabel("Leaves produced")
ax.set_ylabel("Relative level")
ax.set_xlim(0, 20)
ax.set_ylim(0, 1.05)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
