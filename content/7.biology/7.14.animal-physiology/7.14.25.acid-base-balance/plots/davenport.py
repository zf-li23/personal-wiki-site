# Davenport diagram: plasma [HCO3-] against pH, with PCO2 isobars and the four primary disturbances.
# Isobars from the Henderson-Hasselbalch equation: [HCO3-] = 0.03 PCO2 10^(pH - 6.1) (mM, mmHg).
# Blood buffer line through the normal point N (pH 7.40, 24 mM, 40 mmHg): slope -28 mM per pH unit
# (non-bicarbonate buffers of whole blood, mostly hemoglobin). A pure respiratory change moves along the
# buffer line; adding or removing non-volatile acid at constant PCO2 moves along an isobar.
# Compensation targets (clinical rules of thumb): chronic respiratory acidosis PCO2 60 mmHg, HCO3- rises
# 3.5 mM per 10 mmHg; chronic respiratory alkalosis PCO2 25 mmHg, HCO3- falls 5 mM per 10 mmHg; metabolic
# acidosis HCO3- 12 mM, PCO2 = 1.5 HCO3- + 8 (Winter); metabolic alkalosis HCO3- 36 mM, PCO2 rises
# 0.7 mmHg per mM.
import matplotlib.pyplot as plt
import numpy as np


def hco3(ph, p):
    return 0.03 * p * 10 ** (ph - 6.1)


def ph_of(h, p):
    return 6.1 + np.log10(h / (0.03 * p))


def buffer_point(p, ph0=7.40, h0=24.0, beta=28.0):
    # intersection of the buffer line h = h0 - beta (ph - ph0) with the isobar p
    phs = np.linspace(6.8, 8.0, 20001)
    d = hco3(phs, p) - (h0 - beta * (phs - ph0))
    i = np.argmin(np.abs(d))
    return phs[i], hco3(phs[i], p)


fig, ax = plt.subplots(figsize=(7.2, 5.0))
ph = np.linspace(6.9, 7.8, 300)
for p in (20, 25, 30, 40, 50, 60, 80):
    ax.plot(ph, hco3(ph, p), color="#9e9e9e", lw=0.9 if p != 40 else 1.6)
    x = 7.78 if hco3(7.78, p) < 50 else ph_of(49, p)
    ax.text(x, min(hco3(x, p), 49), f"{p}", fontsize=8, color="#7a7a7a", ha="left", va="bottom")
ax.text(6.92, 42.5, "grey curves: PCO$_2$ isobars (mmHg)", fontsize=8, color="#7a7a7a", va="top")
bl = np.linspace(7.1, 7.7, 10)
ax.plot(bl, 24 - 28 * (bl - 7.4), color="#7a4fb3", lw=1.2, ls="--")
ax.text(7.12, 24 - 28 * (7.12 - 7.4) + 0.8, "buffer line", fontsize=8.5, color="#7a4fb3")

N = (7.40, 24.0)
ax.plot(*N, "o", color="black", ms=6, zorder=5)
ax.text(7.41, 22.6, "N", fontsize=10, fontweight="bold")


def path(points, color, label, pos):
    xs, ys = zip(*points)
    ax.annotate("", xy=points[1], xytext=points[0],
                arrowprops=dict(arrowstyle="-|>", color=color, lw=2))
    ax.annotate("", xy=points[2], xytext=points[1],
                arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6, ls="--"))
    ax.text(*pos, label, color=color, fontsize=8.5, ha="center")


# respiratory acidosis
a1 = buffer_point(60)
a2 = (ph_of(24 + 7, 60), 24 + 7)
path([N, a1, a2], "#c0392b", "respiratory\nacidosis", (7.37, 32.0))
# respiratory alkalosis
b1 = buffer_point(25)
b2 = (ph_of(24 - 7.5, 25), 24 - 7.5)
path([N, b1, b2], "#2f6fb5", "respiratory\nalkalosis", (7.66, 12.0))
# metabolic acidosis
m1 = (ph_of(12, 40), 12)
pc = 1.5 * 12 + 8
m2 = (ph_of(12, pc), 12)
path([N, m1, m2], "#e08a3c", "metabolic\nacidosis", (7.08, 9.2))
# metabolic alkalosis
k1 = (ph_of(36, 40), 36)
pk = 40 + 0.7 * 12
k2 = (ph_of(36, pk), 36)
path([N, k1, k2], "#3c9a5f", "metabolic\nalkalosis", (7.62, 37.0))

ax.text(6.92, 47, "solid: primary change\ndashed: compensation", fontsize=8, va="top")
ax.set_xlim(6.9, 7.85)
ax.set_ylim(0, 52)
ax.set_xlabel("Plasma pH")
ax.set_ylabel("Plasma [HCO$_3^-$] (mmol/L)")
sec = ax.secondary_xaxis("top", functions=(lambda x: 10 ** (9 - x), lambda h: 9 - np.log10(np.maximum(h, 1e-6))))
sec.set_xticks([120, 80, 60, 40, 30, 20])
sec.set_xlabel("[H$^+$] (nmol/L)")
ax.spines["right"].set_visible(False)
fig.tight_layout()
