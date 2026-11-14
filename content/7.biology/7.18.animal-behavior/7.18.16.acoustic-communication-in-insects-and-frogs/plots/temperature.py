"""Temperature coupling in the field cricket Gryllus firmus (after Pires and Hoy 1992).

A: syllable rate of male calling songs rises with temperature; points are the model songs used in
the experiments (15 C: 14.3 Hz; 21 C: 20.0 Hz; 30 C: 25.0 Hz, from field recordings), with a linear
fit and the implied Q10. B: schematic of the result of the single-stimulus experiments: at each
test temperature, females walked most strongly toward the model song recorded at that temperature
(diagonal); scores are illustrative.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
T = np.array([15.0, 21.0, 30.0])
rate = np.array([14.3, 20.0, 25.0])
fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.8))
fit = np.polyfit(T, rate, 1)
TT = np.linspace(12, 32, 50)
a.plot(TT, np.polyval(fit, TT), color=P.edge("dna"), lw=1.5, label=f"male song: {fit[0]:.2f} Hz per °C")
a.plot(T, rate, "o", color=P.edge("dna"), ms=7)
a.plot(T, rate, "x", color=P.edge("negative"), ms=11, mew=2, label="song preferred by females at T")
q10 = (25.0 / 14.3) ** (10 / 15)
a.text(13, 26, f"Q10 ≈ {q10:.1f} (15 → 30 °C)", fontsize=8, color=P.ink())
a.set_xlabel("Temperature / °C")
a.set_ylabel("Syllable rate / Hz")
a.legend(frameon=False, fontsize=7.5, loc="lower right")
a.set_title("A", loc="left", fontweight="bold")
score = np.array([[1.0, 0.45, 0.1], [0.4, 1.0, 0.45], [0.15, 0.5, 1.0]])
im = b.imshow(score, cmap="Blues", vmin=0, vmax=1.1, origin="lower")
for i in range(3):
    for j in range(3):
        b.text(j, i, "strong" if i == j else ("weak" if score[i, j] < 0.3 else "moderate"),
               ha="center", va="center", fontsize=8, color=P.surface() if score[i, j] > 0.6 else P.ink())
b.set_xticks(range(3)); b.set_xticklabels(["15 °C song", "21 °C song", "30 °C song"], fontsize=8)
b.set_yticks(range(3)); b.set_yticklabels(["female at 15 °C", "female at 21 °C", "female at 30 °C"], fontsize=8)
b.set_title("B  Phonotaxis (schematic)", loc="left", fontweight="bold")
for s in ("top", "right"):
    a.spines[s].set_visible(False)
fig.tight_layout()
