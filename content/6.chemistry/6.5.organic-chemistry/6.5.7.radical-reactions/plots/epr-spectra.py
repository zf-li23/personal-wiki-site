"""Simulated X-band EPR spectra, drawn as first derivatives of the absorption as spectrometers
record them. Left: one line (absorption and its derivative). Middle: the methyl radical, whose
unpaired electron couples to three equivalent protons (a = 2.30 mT) giving a 1:3:3:1 quartet.
Right: a nitroxide (TEMPO-like), coupling to one 14N nucleus (I = 1, a = 1.6 mT) giving a
1:1:1 triplet."""

import numpy as np
import matplotlib.pyplot as plt
from math import comb

B0 = 339.0  # mT, centre of the spectrum at about 9.5 GHz for g = 2.00
B = np.linspace(B0 - 6, B0 + 6, 3000)
w = 0.25  # Lorentzian half-width, mT


def absorption(centres, weights):
    y = np.zeros_like(B)
    for c, a in zip(centres, weights):
        y += a * w**2 / ((B - c) ** 2 + w**2)
    return y


def derivative(y):
    return np.gradient(y, B)


fig, axes = plt.subplots(1, 3, figsize=(10, 3.2))
single = absorption([B0], [1.0])
axes[0].plot(B, single / single.max(), color="0.55", lw=1.4, label="absorption")
d = derivative(single)
axes[0].plot(B, d / np.abs(d).max(), color="C0", lw=1.6, label="first derivative")
axes[0].legend(fontsize=8, frameon=False, loc="lower left")
axes[0].set_title("one line", fontsize=11)
axes[0].set_xlim(B0 - 2.5, B0 + 2.5)

a_h = 2.30
lines = [B0 + (k - 1.5) * a_h for k in range(4)]
y = derivative(absorption(lines, [comb(3, k) for k in range(4)]))
axes[1].plot(B, y / np.abs(y).max(), color="C0", lw=1.4)
for c, k in zip(lines, range(4)):
    axes[1].text(c, 1.08, str(comb(3, k)), ha="center", fontsize=9)
axes[1].annotate("", xy=(lines[1], -1.1), xytext=(lines[0], -1.1), arrowprops=dict(arrowstyle="<->", lw=1))
axes[1].text((lines[0] + lines[1]) / 2, -1.3, "$a$(H) = 2.30 mT", ha="center", fontsize=9)
axes[1].set_title(r"$\bullet$CH$_3$: 1:3:3:1", fontsize=11)

a_n = 1.6
lines = [B0 - a_n, B0, B0 + a_n]
y = derivative(absorption(lines, [1, 1, 1]))
axes[2].plot(B, y / np.abs(y).max(), color="C0", lw=1.4)
axes[2].set_title(r"nitroxide R$_2$N$-$O$\bullet$: 1:1:1", fontsize=11)

for ax in axes:
    ax.set_xlabel(r"$B$ / mT")
    ax.set_yticks([])
    ax.set_ylim(-1.5, 1.3)
fig.tight_layout()
