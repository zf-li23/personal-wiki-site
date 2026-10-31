# Spectral sensitivity of human photopigments from the Govardovskii et al. (2000) A1 template.
# alpha band: S(x) = 1 / [exp(A(a - x)) + exp(B(b - x)) + exp(C(c - x)) + D], x = lambda_max / lambda,
#   A = 69.7, a = 0.8795 + 0.0459 exp(-(lambda_max - 300)^2 / 11940), B = 28, b = 0.922, C = -14.9,
#   c = 1.104, D = 0.674;
# beta band: 0.26 exp{-[(lambda - lambda_b) / w]^2}, lambda_b = 189 + 0.315 lambda_max,
#   w = -40.5 + 0.195 lambda_max.
# Peaks: S cones 420 nm, rods 498 nm, M cones 530 nm, L cones 560 nm (absorbance of the pigment, without
# the filtering by lens and macular pigment).
# A: the four templates, each normalized to its peak; one template shape fits all pigments when plotted
#    against lambda_max / lambda.
# B: univariance. A single cone type reports only the number of photons it absorbs: 600 nm light is
#    absorbed by an M cone 0.22 times as well as 530 nm light, so 4.5 times more 600 nm photons give the same
#    M-cone signal. Colour is recovered by comparing cones: the ratio L / (L + M) changes monotonically with
#    wavelength across the green-red range, S / (L + M) across the blue.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P


def template(lam, lmax):
    x = lmax / lam
    a = 0.8795 + 0.0459 * np.exp(-((lmax - 300) ** 2) / 11940)
    alpha = 1 / (np.exp(69.7 * (a - x)) + np.exp(28 * (0.922 - x)) + np.exp(-14.9 * (1.104 - x)) + 0.674)
    lb = 189 + 0.315 * lmax
    w = -40.5 + 0.195 * lmax
    s = alpha + 0.26 * np.exp(-(((lam - lb) / w) ** 2))
    return s


lam = np.linspace(380, 720, 500)
pig = [("S cone 420", 420, "dna"), ("rod 498", 498, "neutral"), ("M cone 530", 530, "enzyme"),
       ("L cone 560", 560, "rna")]
fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.0))
ax = axs[0]
for name, lm, tok in pig:
    s = template(lam, lm)
    s = s / s.max()
    ax.plot(lam, s, color=charts.line(tok), lw=1.8, ls="--" if "rod" in name else "-", label=f"{name} nm")
ax.set_xlim(380, 720)
ax.set_ylim(0, 1.08)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "wavelength / nm", "relative absorbance")
charts.title(ax, "A   Photopigment templates")

ax = axs[1]
S = template(lam, 420)
M = template(lam, 530)
L = template(lam, 560)
S, M, L = S / S.max(), M / M.max(), L / L.max()
ax.plot(lam, L / (L + M), color=charts.line("rna"), lw=1.8, label="L / (L + M)")
ax.plot(lam, S / (L + M), color=charts.line("dna"), lw=1.8, label="S / (L + M)")
m600 = np.interp(600, lam, M)
ax.axvline(530, color=P.muted(), lw=0.6, ls=":")
ax.axvline(600, color=P.muted(), lw=0.6, ls=":")
ax.text(603, 3.0, f"M cone absorbs 600 nm\n{m600:.2f}× as well as 530 nm", fontsize=7, color=P.ink())
ax.set_xlim(380, 720)
ax.set_yscale("log")
ax.set_ylim(1e-3, 20)
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(ax, "wavelength / nm", "ratio of cone signals")
charts.title(ax, "B   Colour from comparisons")
fig.tight_layout()
