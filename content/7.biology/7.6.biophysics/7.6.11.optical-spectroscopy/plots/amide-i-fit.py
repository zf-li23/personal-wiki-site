# Analysis of the amide I band of a protein in D2O (synthetic spectrum).
# Components (position / cm^-1, half width at half height, area fraction): beta sheet 1630 (8, 0.30),
# disordered 1643 (11, 0.20), alpha helix 1652 (10, 0.30), turns 1668 (9, 0.12), antiparallel-sheet
# high-frequency component 1684 (6, 0.08); Lorentz-Gauss (Voigt-like) shapes and 0.3 % noise.
# A: the measured band is a single broad, featureless envelope. B: its negative second derivative, smoothed
# with a Savitzky-Golay filter, resolves the components (narrow bands are enhanced as 1/width^2).
# C: a least-squares fit with five Gaussians started from the second-derivative positions. The fit reproduces
# the envelope within the noise, yet the area fractions (equal absorptivity assumed) differ from the true
# ones: with free widths, a broad component can absorb its neighbours, so band fitting is not unique.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import savgol_filter

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
nu = np.arange(1600, 1711, 0.5)
comp = [(1630, 8, 0.30, "β sheet", "dna"), (1643, 11, 0.20, "disordered", "neutral"),
        (1652, 10, 0.30, "α helix", "rna"), (1668, 9, 0.12, "turns", "protein"),
        (1684, 6, 0.08, "β (high)", "dna2")]


def voigtish(x, c, w):
    L = 1 / (1 + ((x - c) / w) ** 2)
    G = np.exp(-np.log(2) * ((x - c) / w) ** 2)
    v = 0.5 * L + 0.5 * G
    return v / np.trapezoid(v, x)


y = sum(a * voigtish(nu, c, w) for c, w, a, _, _ in comp)
y = y / y.max() + rng.normal(0, 0.003, nu.size)
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2))
axs[0].plot(nu, y, color=charts.line("protein"), lw=1.8)
axs[0].invert_xaxis()
charts.style_axes(axs[0], "wavenumber / cm⁻¹", "absorbance (rel.)")
charts.title(axs[0], "A   Amide I envelope")

d2 = -savgol_filter(y, 17, 3, deriv=2, delta=0.5)
axs[1].plot(nu, d2 / d2.max(), color=charts.line("dna"), lw=1.6)
for c, w, a, n, tok in comp:
    axs[1].axvline(c, color=charts.line(tok), lw=0.8, ls=":")
    axs[1].text(c, 1.06, n, rotation=90, fontsize=7, ha="center", va="bottom", color=P.ink())
axs[1].set_ylim(-0.6, 1.5)
axs[1].invert_xaxis()
charts.style_axes(axs[1], "wavenumber / cm⁻¹", "−d²A/dν̃² (rel.)")
charts.title(axs[1], "B   Second derivative")


def model(x, *p):
    out = np.zeros_like(x)
    for k in range(5):
        a, c, s = p[3 * k:3 * k + 3]
        out += a * np.exp(-((x - c) ** 2) / (2 * s**2))
    return out


p0 = []
for c, w, a, _, _ in comp:
    p0 += [0.5, c, w]
popt, _ = curve_fit(model, nu, y, p0=p0, maxfev=20000)
ax = axs[2]
ax.plot(nu, y, "o", ms=1.8, color=P.muted())
areas = []
for k, (c, w, a, n, tok) in enumerate(comp):
    A_, C_, S_ = popt[3 * k:3 * k + 3]
    comp_y = A_ * np.exp(-((nu - C_) ** 2) / (2 * S_**2))
    areas.append(A_ * abs(S_))
    ax.fill_between(nu, comp_y, color=P.light(tok), alpha=0.9, lw=0)
    ax.plot(nu, comp_y, color=charts.line(tok), lw=1.0)
areas = np.array(areas) / sum(areas)
ax.plot(nu, model(nu, *popt), color=charts.line("positive"), lw=1.5)
txt = "\n".join(f"{n}: {fa:.2f} (true {a:.2f})" for (c, w, a, n, _), fa in zip(comp, areas))
ax.text(1708, 0.95, txt, fontsize=7, va="top", color=P.ink())
ax.invert_xaxis()
charts.style_axes(ax, "wavenumber / cm⁻¹", "absorbance (rel.)")
charts.title(ax, "C   A perfect fit with wrong fractions")
fig.tight_layout()
