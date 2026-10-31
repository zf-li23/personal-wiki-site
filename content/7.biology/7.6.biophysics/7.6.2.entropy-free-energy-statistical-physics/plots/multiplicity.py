# Sharpening of the most probable macrostate. N distinguishable molecules in a box, each independently in the
# left or right half; the macrostate is the number N1 on the left, with multiplicity Omega(N1) = C(N, N1).
# A: Omega(N1) / Omega(N/2) against the scaled deviation (N1 - N/2)/(N/2) for N = 10, 100 and 10^4 (exact binomial
#    coefficients via log-gamma); the width shrinks as 1/sqrt(N).
# B: the exact ln Omega(N/2) (points) against N ln 2 (dashed) and Stirling's estimate with the square-root
#    correction, N ln 2 - (1/2) ln(pi N / 2) (line); the relative difference between ln Omega(N/2) and the
#    logarithm of the total number of microstates, N ln 2, vanishes as (ln N)/N.
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gammaln

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 2, figsize=(11.0, 3.8), gridspec_kw={"width_ratios": [1.35, 1.0]})

ax = axs[0]
for N, tok in ((10, "neutral"), (100, "dna"), (10000, "negative")):
    n1 = np.arange(0, N + 1)
    lnw = gammaln(N + 1) - gammaln(n1 + 1) - gammaln(N - n1 + 1)
    r = np.exp(lnw - lnw.max())
    xx = (n1 - N / 2) / (N / 2)
    if N <= 100:
        ax.plot(xx, r, "o-", color=charts.line(tok), ms=3 if N == 100 else 4.5, lw=1.2, label=f"N = {N}")
    else:
        ax.plot(xx, r, "-", color=charts.line(tok), lw=1.8, label=f"N = {N:,}".replace(",", " "))
ax.set_xlim(-1, 1)
ax.set_ylim(0, 1.05)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "(N₁ − N/2) / (N/2)", "Ω(N₁) / Ω(N/2)")
ax.set_title("A   Multiplicity of the macrostates", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
Ns = np.unique(np.logspace(0.5, 4, 25).astype(int) // 2 * 2)
exact = gammaln(Ns + 1) - 2 * gammaln(Ns / 2 + 1)
ax.plot(Ns, exact / (Ns * np.log(2)), "o", color=charts.line("dna"), ms=4, label="exact ln Ω(N/2)")
nn = np.logspace(0.5, 4, 200)
ax.plot(nn, (nn * np.log(2) - 0.5 * np.log(np.pi * nn / 2)) / (nn * np.log(2)), color=charts.line("protein"),
        lw=1.6, label="N ln 2 − ½ ln(πN/2)")
ax.axhline(1, color=P.muted(), lw=0.9, ls=(0, (4, 3)), label="N ln 2")
ax.set_xscale("log")
ax.set_ylim(0.5, 1.05)
ax.legend(fontsize=7.5, frameon=False, loc="lower right")
charts.style_axes(ax, "N", "ln Ω(N/2) / (N ln 2)")
ax.set_title("B   Stirling's approximation", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
