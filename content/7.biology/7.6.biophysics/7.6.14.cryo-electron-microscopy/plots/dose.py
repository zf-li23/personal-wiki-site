# Radiation damage limits the electron exposure, and does so first at high resolution.
# A: critical exposure N_e(k) = 0.245 k^-1.665 + 2.81 electrons per square angstrom (Grant and
#    Grigorieff 2015, 300 kV, rotavirus capsid), the exposure after which the amplitude of the signal at
#    spatial frequency k has fallen to exp(-1/2) of its initial value.
# B: the fraction of the amplitude remaining, exp(-N / (2 N_e)), against accumulated exposure N for
#    10, 5, 3 and 2 A.
# C: signal-to-noise ratio of an image summed over an exposure N without weighting, relative to its
#    optimum: SNR^2 is proportional to [2 N_e (1 - exp(-N / 2 N_e))]^2 / N (signal summed over the movie,
#    shot noise growing as N). The optimum lies at N = 2.5 N_e (marked); exposure-dependent weighting of
#    the movie frames removes the penalty for longer exposures at low resolution.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P


def Ne(k):
    return 0.245 * k**-1.665 + 2.81


fig, axs = plt.subplots(1, 3, figsize=(13.5, 3.9))
ax = axs[0]
k = np.linspace(0.02, 0.55, 300)
ax.plot(k, Ne(k), color=charts.line("protein"), lw=1.8)
for d in (10, 5, 3, 2):
    ax.plot(1 / d, Ne(1 / d), "o", color=charts.line("highlight"), ms=5)
    ax.annotate(f"{d} Å: {Ne(1 / d):.1f}", (1 / d, Ne(1 / d)), xytext=(5, 5), textcoords="offset points",
                fontsize=7, color=P.ink())
ax.set_ylim(0, 40)
charts.style_axes(ax, "spatial frequency k / Å⁻¹", "Nₑ / (e⁻ Å⁻²)")
charts.title(ax, "A   Critical exposure")

ax = axs[1]
N = np.linspace(0, 80, 400)
for d, tok in ((10, "dna"), (5, "positive"), (3, "highlight"), (2, "negative")):
    ax.plot(N, np.exp(-N / (2 * Ne(1 / d))), color=charts.line(tok), lw=1.6, label=f"{d} Å")
ax.legend(fontsize=7.5, frameon=False, title="feature size", title_fontsize=7.5)
charts.style_axes(ax, "accumulated exposure N / (e⁻ Å⁻²)", "signal amplitude remaining")
charts.title(ax, "B   Fading of the signal")

ax = axs[2]
x = np.linspace(0.05, 8, 400)
snr = (1 - np.exp(-x / 2)) / np.sqrt(x)
xopt = x[np.argmax(snr)]
ax.plot(x, snr / snr.max(), color=charts.line("protein"), lw=1.8)
ax.axvline(xopt, color=P.muted(), lw=0.7, ls=":")
ax.text(xopt + 0.15, 0.3, f"optimum N = {xopt:.2f} Nₑ", fontsize=7.5, color=P.ink())
ax.set_ylim(0, 1.05)
charts.style_axes(ax, "exposure N / Nₑ", "relative SNR (unweighted sum)")
charts.title(ax, "C   Optimal exposure")
fig.tight_layout()
