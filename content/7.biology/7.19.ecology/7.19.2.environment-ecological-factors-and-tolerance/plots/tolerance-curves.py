# Tolerance curves (schematic models).
# A: Shelford's law of tolerance. Performance along an environmental gradient, modeled as a Gaussian
#    P(x) = exp(-(x - 50)^2 / (2 * 15^2)); zones: optimum (P > 0.8), physiological stress, intolerance
#    (P < 0.05, beyond the limits of tolerance). Survival (S), growth (G) and reproduction (R) are possible
#    over successively narrower ranges (thresholds 0.05, 0.4, 0.75 of the same curve).
# B: Generalist-specialist trade-off: three Gaussian tolerance curves with the same area,
#    P(x) = (c / sigma) exp(-(x - mu)^2 / (2 sigma^2)), sigma = 6 (stenotopic), 12 and 24 (eurytopic),
#    so that the peak height is inversely proportional to the breadth.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
x = np.linspace(0, 100, 1001)

fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.2))

p = np.exp(-(x - 50) ** 2 / (2 * 15 ** 2))
lo_limit = 50 - 15 * np.sqrt(-2 * np.log(0.05))
opt = 15 * np.sqrt(-2 * np.log(0.8))
a.axvspan(0, lo_limit, color=P.light("negative"), lw=0)
a.axvspan(100 - lo_limit, 100, color=P.light("negative"), lw=0)
a.axvspan(50 - opt, 50 + opt, color=P.light("positive"), lw=0)
a.plot(x, p, color=P.ink(), lw=2)
a.text(1, 1.08, "intolerance", ha="left", fontsize=8, color=P.edge("negative"))
a.text(99, 1.08, "intolerance", ha="right", fontsize=8, color=P.edge("negative"))
a.text(50, 1.08, "optimum", ha="center", fontsize=8, color=P.edge("positive"))
a.text(31, 1.08, "stress", ha="center", fontsize=8, color=P.muted())
a.text(69, 1.08, "stress", ha="center", fontsize=8, color=P.muted())
for thr, name, y in ((0.05, "S", -0.08), (0.4, "G", -0.16), (0.75, "R", -0.24)):
    half = 15 * np.sqrt(-2 * np.log(thr))
    a.plot([50 - half, 50 + half], [y, y], color=P.edge("dna"), lw=2.5, solid_capstyle="butt")
    a.text(50 + half + 1.5, y, name, va="center", fontsize=8, color=P.edge("dna"))
a.annotate("", xy=(lo_limit, 0.55), xytext=(100 - lo_limit, 0.55),
           arrowprops=dict(arrowstyle="<->", color=P.muted(), lw=0.9))
a.text(50, 0.58, "ecological amplitude", ha="center", fontsize=8, color=P.muted())
a.text(lo_limit, -0.36, "lower limit", ha="center", fontsize=7.5, color=P.muted())
a.text(100 - lo_limit, -0.36, "upper limit", ha="center", fontsize=7.5, color=P.muted())
a.set_xlim(0, 100)
a.set_ylim(-0.42, 1.18)
a.set_yticks([0, 0.5, 1])
a.set_xticks([])
a.set_xlabel("Environmental factor (e.g. temperature)")
a.set_ylabel("Performance (relative)")
a.set_title("A", loc="left", fontweight="bold")

for sig, tok, name in ((6, "negative", "stenotopic, sigma = 6"), (12, "atp", "sigma = 12"),
                       (24, "dna", "eurytopic, sigma = 24")):
    b.plot(x, (6 / sig) * np.exp(-(x - 50) ** 2 / (2 * sig ** 2)), color=P.edge(tok), lw=2, label=name)
b.set_xlim(0, 100)
b.set_ylim(0, 1.1)
b.set_xticks([])
b.set_yticks([0, 0.5, 1])
b.set_xlabel("Environmental factor")
b.set_ylabel("Performance (equal area)")
b.legend(frameon=False, fontsize=8, loc="upper right")
b.set_title("B", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
