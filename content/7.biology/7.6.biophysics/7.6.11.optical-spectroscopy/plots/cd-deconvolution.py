# Secondary structure from far-UV CD by linear decomposition (synthetic data).
# A: model basis spectra of alpha helix, beta sheet and disordered chain built from Gaussian bands at the
#    literature positions (helix +192, -208, -222 nm; sheet +196, -217 nm; disordered -198, +218 nm),
#    in mean residue ellipticity.
# B: a "measured" spectrum of a protein with 35 % helix, 25 % sheet and 40 % disorder, with noise that
#    grows below 200 nm, and its non-negative least-squares fit with the fractions constrained to sum to one.
# C: fitted fractions with data down to 185 nm and with data only from 205 nm (as in a buffer that absorbs
#    strongly), each from 300 noisy replicates (mean and standard deviation): the helix content is robust,
#    sheet and disorder become poorly determined once the 190-200 nm region is lost.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import nnls

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
lam = np.arange(185, 251, 1.0)


def g(c, w, a):
    return a * np.exp(-((lam - c) ** 2) / (2 * w**2))


helix = g(192, 6, 72000) + g(208, 5.5, -33000) + g(222, 7.5, -35000)
sheet = g(196, 6.5, 30000) + g(217, 8, -19000)
coil = g(198, 6, -40000) + g(218, 6, 3500)
B = np.vstack([helix, sheet, coil]).T
names = ("helix", "sheet", "disordered")
toks = ("rna", "dna", "neutral")
ftrue = np.array([0.35, 0.25, 0.40])
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2))
ax = axs[0]
for k in range(3):
    ax.plot(lam, B[:, k] / 1e3, color=charts.line(toks[k]), lw=1.8, label=names[k])
ax.axhline(0, color=P.muted(), lw=0.6)
ax.legend(fontsize=8, frameon=False)
charts.style_axes(ax, "wavelength / nm", "[θ] / (10³ deg cm² dmol⁻¹)")
charts.title(ax, "A   Basis spectra")


def noisy():
    sd = 600 + 2500 * np.exp(-(lam - 185) / 6)
    return B @ ftrue + rng.normal(0, sd)


def fit(y, mask):
    # NNLS with a heavily weighted row that enforces sum(f) = 1
    A = np.vstack([B[mask] / 1e4, 50 * np.ones(3)])
    b = np.concatenate([y[mask] / 1e4, [50.0]])
    return nnls(A, b)[0]


y = noisy()
full = lam >= 185
f = fit(y, full)
ax = axs[1]
ax.plot(lam, y / 1e3, "o", ms=2.5, color=P.muted(), label="data")
ax.plot(lam, B @ f / 1e3, color=charts.line("positive"), lw=1.8, label="fit")
ax.plot(lam, (y - B @ f) / 1e3 - 25, color=charts.line("negative"), lw=0.9, label="residual (offset)")
ax.axhline(-25, color=P.muted(), lw=0.5)
ax.legend(fontsize=8, frameon=False, loc="upper right")
ax.text(206, 5, "fit: " + ", ".join(f"{n} {v:.2f}" for n, v in zip(names, f)), fontsize=7.5, color=P.ink())
charts.style_axes(ax, "wavelength / nm", "[θ] / (10³ deg cm² dmol⁻¹)")
charts.title(ax, "B   Constrained least squares")

ax = axs[2]
res = {}
for label, mask in (("185-250 nm", lam >= 185), ("205-250 nm", lam >= 205)):
    res[label] = np.array([fit(noisy(), mask) for _ in range(300)])
x = np.arange(3)
ax.bar(x - 0.27, ftrue, 0.26, color=P.fill("neutral"), edgecolor=P.edge("neutral"), label="true")
for k, (label, tok) in enumerate(zip(res, ("positive", "negative"))):
    m, s = res[label].mean(0), res[label].std(0)
    ax.bar(x + k * 0.27, m, 0.26, yerr=s, color=P.fill(tok), edgecolor=P.edge(tok), capsize=3,
           error_kw=dict(ecolor=P.ink(), lw=0.8), label=label)
ax.set_xticks(x, names)
ax.set_ylim(0, 0.8)
ax.legend(fontsize=8, frameon=False)
charts.style_axes(ax, None, "fraction")
charts.title(ax, "C   The far-UV end carries the β information")
fig.tight_layout()
