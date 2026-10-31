# Forster resonance energy transfer as a spectroscopic ruler.
# A: transfer efficiency E = 1 / (1 + (R/R0)^6) for R0 = 2.5 (Trp-dansyl-like), 5.4 (Cy3-Cy5) and 7 nm;
#    the shaded band 0.5 R0 - 1.5 R0 of the Cy3-Cy5 pair is the useful range.
# B: spectral overlap: normalized donor emission F_D, acceptor absorption eps_A (model Cy3/Cy5 shapes) and the
#    integrand F_D eps_A lambda^4 of the overlap integral J.
# C: distribution of the orientation factor kappa^2 = (cos theta_T - 3 cos theta_D cos theta_A)^2 for randomly
#    oriented but static dipoles (Monte Carlo, 2e5 pairs): mean 2/3, range 0-4, median about 0.48.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2))
ax = axs[0]
R = np.linspace(0, 14, 400)
for R0, tok in ((2.5, "protein"), (5.4, "dna"), (7.0, "rna")):
    ax.plot(R, 1 / (1 + (R / R0) ** 6), color=charts.line(tok), lw=1.8, label=f"R0 = {R0} nm")
ax.axvspan(0.5 * 5.4, 1.5 * 5.4, color=P.light("dna"), alpha=0.5, lw=0)
ax.axhline(0.5, color=P.muted(), lw=0.6, ls=":")
ax.legend(fontsize=8, frameon=False)
charts.style_axes(ax, "donor-acceptor distance R / nm", "transfer efficiency E")
charts.title(ax, "A   E = 1 / (1 + (R/R0)⁶)")

ax = axs[1]
lam = np.linspace(500, 720, 600)


FD = np.exp(-((1e7 / lam - 1e7 / 565) / 700) ** 2) + 0.35 * np.exp(-((1e7 / lam - (1e7 / 565 - 1200)) / 800) ** 2)
FD /= np.trapezoid(FD, lam)
eA = 250000 * (np.exp(-((1e7 / lam - 1e7 / 649) / 600) ** 2) + 0.4 * np.exp(-((1e7 / lam - (1e7 / 649 + 1200)) / 800) ** 2))
integ = FD * eA * lam**4
ax.plot(lam, FD / FD.max(), color=charts.line("positive"), lw=1.8, label="donor emission F_D")
ax.plot(lam, eA / eA.max(), color=charts.line("negative"), lw=1.8, label="acceptor absorption ε_A")
ax.fill_between(lam, integ / integ.max(), color=P.light("highlight"), alpha=0.9, lw=0, label="F_D ε_A λ⁴")
J = np.trapezoid(integ, lam)
ax.text(505, 0.55, f"J = {J:.1e}\nM⁻¹ cm⁻¹ nm⁴", fontsize=8, color=P.ink(), va="top")
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "wavelength / nm", "normalized")
charts.title(ax, "B   Spectral overlap")

ax = axs[2]
n = 200000


def unit(n):
    v = rng.normal(size=(n, 3))
    return v / np.linalg.norm(v, axis=1, keepdims=True)


d, a = unit(n), unit(n)
rhat = np.array([0, 0, 1.0])
k2 = (np.sum(d * a, 1) - 3 * (d @ rhat) * (a @ rhat)) ** 2
ax.hist(k2, bins=80, range=(0, 4), density=True, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.3)
ax.axvline(2 / 3, color=charts.line("negative"), lw=1.2)
ax.text(0.75, 1.6, f"mean = {k2.mean():.3f}\nmedian = {np.median(k2):.2f}", fontsize=8, color=P.ink())
ax.set_yscale("log")
charts.style_axes(ax, "κ²", "probability density")
charts.title(ax, "C   κ² for static random dipoles")
fig.tight_layout()
