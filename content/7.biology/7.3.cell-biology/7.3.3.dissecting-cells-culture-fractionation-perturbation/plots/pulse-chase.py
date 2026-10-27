# A compartment model of the Jamieson-Palade pulse-chase experiment in pancreatic acinar cells.
# Labeled protein moves through a chain of compartments with first-order exit rates:
#     dA_1/dt = p(t) - k_1 A_1,   dA_i/dt = k_{i-1} A_{i-1} - k_i A_i,
# where p(t) is the incorporation of [3H]leucine during a 3-min pulse (then a chase with unlabeled leucine).
# Compartments: rough ER -> Golgi (peripheral vesicles and stacks) -> condensing vacuoles -> zymogen
# granules -> secreted (lumen). Illustrative rates (per min): k_ER = 0.12, k_Golgi = 0.10, k_CV = 0.03,
# k_ZG = 0.004, chosen to reproduce the reported timing (label mostly over rough ER at the end of the pulse,
# over the Golgi at about 7-17 min, over condensing vacuoles at about 37 min and over zymogen granules by
# about 2 h). Mean residence time in compartment i is 1/k_i. Points: grain fractions read at the classic
# sampling times (3, 7, 37, 117 min) from the model, as autoradiographs would sample it.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
k = np.array([0.12, 0.10, 0.03, 0.004])
names = ["rough ER", "Golgi", "condensing vacuoles", "zymogen granules", "secreted"]
toks = ["er", "golgi", "protein", "negative", "neutral"]
dt = 0.05
t = np.arange(0, 180 + dt, dt)
A = np.zeros((len(t), 5))
for i in range(len(t) - 1):
    p = 1.0 / 3.0 if t[i] < 3 else 0.0
    a = A[i]
    da = np.empty(5)
    da[0] = p - k[0] * a[0]
    for j in range(1, 4):
        da[j] = k[j - 1] * a[j - 1] - k[j] * a[j]
    da[4] = k[3] * a[3]
    A[i + 1] = a + dt * da
frac = A / np.maximum(A.sum(axis=1, keepdims=True), 1e-12)

fig, ax = plt.subplots(figsize=(8.0, 3.9))
ax.axvspan(0, 3, color=P.fill("positive"), alpha=0.35, lw=0)
ax.text(1.5, 1.02, "pulse", fontsize=7, color=P.ink(), ha="center", va="bottom")
for j in range(5):
    ax.plot(t, frac[:, j], color=charts.line(toks[j]), lw=1.8, label=names[j])
for ts in (3, 7, 37, 117):
    i = int(round(ts / dt))
    ax.axvline(ts, color=P.muted(), lw=0.5, ls=":")
    for j in range(5):
        ax.plot([ts], [frac[i, j]], "o", ms=3.5, color=charts.line(toks[j]))
ax.set_xlim(0, 180)
ax.set_ylim(0, 1.08)
ax.legend(fontsize=7, frameon=False, loc="center right")
charts.style_axes(ax, "time after start of pulse / min", "fraction of label")
fig.tight_layout()
