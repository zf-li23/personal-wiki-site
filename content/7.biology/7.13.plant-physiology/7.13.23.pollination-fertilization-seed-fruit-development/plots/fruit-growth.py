# Growth curves of fruits (illustrative parameters).
# Single sigmoid (apple, tomato): W = Wmax / (1 + exp(-k (t - tm))), Wmax = 180 g, k = 0.065 /d, tm = 70 d.
# Double sigmoid (peach, cherry, grape): sum of two logistic phases,
#   W = W1 / (1 + exp(-k1 (t - t1))) + W2 / (1 + exp(-k2 (t - t2))),
#   W1 = 50 g, k1 = 0.15 /d, t1 = 25 d; W2 = 110 g, k2 = 0.16 /d, t2 = 95 d.
# Stage I: cell division and early expansion; stage II: slow growth of the pericarp while the
# endocarp (stone) lignifies and the embryo grows; stage III: final swell by cell expansion.
# Top: fresh mass; bottom: absolute growth rate dW/dt.
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 140, 700)


def logistic(t, W, k, tm):
    return W / (1 + np.exp(-k * (t - tm)))


single = logistic(t, 180, 0.065, 70)
double = logistic(t, 50, 0.15, 25) + logistic(t, 110, 0.16, 95)

fig, (ax, bx) = plt.subplots(2, 1, figsize=(7.8, 5.6), sharex=True, gridspec_kw={"height_ratios": [1.4, 1]})
ax.plot(t, single, color="#3a9a5b", lw=2.2, label="single sigmoid (apple)")
ax.plot(t, double, color="#d93a6b", lw=2.2, label="double sigmoid (peach)")
for x0, x1, lab in ((0, 45, "I"), (45, 80, "II"), (80, 140, "III")):
    ax.axvspan(x0, x1, color="#d93a6b", alpha=0.05 if lab != "II" else 0.13, lw=0)
    ax.text((x0 + x1) / 2, 188, lab, ha="center", fontsize=10, color="#a32a52")
ax.set_ylabel("Fresh mass / g")
ax.set_ylim(0, 200)
ax.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(0.0, 0.9))
bx.plot(t, np.gradient(single, t), color="#3a9a5b", lw=2.2)
bx.plot(t, np.gradient(double, t), color="#d93a6b", lw=2.2)
bx.set_xlabel("Days after full bloom / d")
bx.set_ylabel("Growth rate / (g d⁻¹)")
bx.set_xlim(0, 140)
bx.set_ylim(0, 5)
for a, letter in zip((ax, bx), "AB"):
    a.spines[["top", "right"]].set_visible(False)
    a.text(-0.1, 1.0, letter, transform=a.transAxes, fontsize=12, weight="bold")
fig.tight_layout()
