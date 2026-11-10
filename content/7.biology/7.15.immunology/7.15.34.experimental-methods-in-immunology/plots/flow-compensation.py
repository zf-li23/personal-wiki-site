# Spectral spillover and compensation in two-colour flow cytometry (simulated data, seed 0).
# True fluorophore intensities x = (x_FITC, x_PE) of four populations are mixed by the spillover matrix S into the two
# detector readings y = S x + noise, with
#   S = [[1, 0.05], [0.20, 1]]    (y_FITC = x_FITC + 0.05 x_PE,  y_PE = 0.20 x_FITC + x_PE).
# Photon (shot) noise has variance proportional to the detected signal. Compensation applies x_hat = S^-1 y: the
# diagonal FITC-only population is moved back onto the axis, but the noise that spilled into the PE detector is
# subtracted only in mean, not in variance, so the compensated PE readings of FITC-only cells are spread wider
# (spreading error). Axes use a symmetric-log scale because compensated values can be negative.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
S = np.array([[1.0, 0.05], [0.20, 1.0]])
N = 600


def population(mf, mp):
    xf = rng.lognormal(np.log(mf), 0.35, N) if mf else np.abs(rng.normal(0, 40, N))
    xp = rng.lognormal(np.log(mp), 0.35, N) if mp else np.abs(rng.normal(0, 40, N))
    return np.c_[xf, xp]


pops = {"neg": population(0, 0), "F": population(8000, 0), "P": population(0, 6000), "FP": population(8000, 6000)}
Sinv = np.linalg.inv(S)
raw, comp = {}, {}
for k, x in pops.items():
    y = x @ S.T
    y = y + rng.normal(0, 1, y.shape) * np.sqrt(60 * np.abs(y) + 30 ** 2)
    raw[k], comp[k] = y, y @ Sinv.T

cols = {"neg": "neutral", "F": "protein", "P": "negative", "FP": "receptor"}
fig, axs = plt.subplots(1, 3, figsize=(12, 3.6))
for ax, data, ttl in ((axs[0], raw, "A  uncompensated"), (axs[1], comp, "B  compensated")):
    for k, y in data.items():
        ax.plot(y[:, 0], y[:, 1], ".", ms=2.2, color=charts.line(cols[k]), alpha=0.7)
    ax.set_xscale("symlog", linthresh=300, linscale=0.5)
    ax.set_yscale("symlog", linthresh=300, linscale=0.5)
    ax.set_xlim(-300, 1e5)
    ax.set_ylim(-300, 1e5)
    charts.style_axes(ax, "FITC detector", "PE detector")
    ax.set_title(ttl, loc="left", fontsize=8, color=P.ink())
ax = axs[2]
bins = np.linspace(-3000, 4000, 70)
ax.hist(comp["F"][:, 1], bins=bins, histtype="step", color=charts.line("protein"), lw=1.6, label="FITC-only cells")
ax.hist(comp["neg"][:, 1], bins=bins, histtype="step", color=charts.line("neutral"), lw=1.6, label="unstained cells")
ax.legend(frameon=False, fontsize=7, labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "PE reading", "events")
ax.set_title("C  compensated PE reading", loc="left", fontsize=8, color=P.ink())
fig.tight_layout()
