"""Three quantitative checks of a droplet experiment. A: barcode rank plot (simulated): total UMIs per
barcode against its rank, both on log scales, for 8000 cell-containing droplets (median 4000 UMIs) among
150000 barcodes of empty droplets that carry only ambient RNA; the steep drop (knee) separates cells
(dark) from background (light). B: Poisson loading: when cells occupy droplets at mean lambda per droplet,
the share of cell-containing droplets that hold two or more cells grows with the number of cells
recovered (about 1e5 droplets per channel and a recovery of 60% of loaded cells are assumed). C:
sequencing saturation of one library sequenced on one to four lanes (points: data of Zhang and
colleagues, 2020), with the expected saturation 1 - U(r)/r for U(r) distinct molecules among r reads per
cell, for equal molecule abundances (dashed) and for gamma-distributed abundances (solid, two fitted
parameters: M molecules per cell and shape k)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
fig, axs = plt.subplots(1, 3, figsize=(12.4, 3.6))
fig.subplots_adjust(left=0.06, right=0.99, bottom=0.17, top=0.88, wspace=0.32)

ax = axs[0]
cells = rng.lognormal(np.log(4000), 0.55, 8000)
empty = rng.lognormal(np.log(25), 0.8, 150000)
tot = np.r_[cells, empty]
iscell = np.r_[np.ones(len(cells), bool), np.zeros(len(empty), bool)]
o = np.argsort(-tot)
rank = np.arange(1, len(tot) + 1)
ax.scatter(rank[iscell[o]], tot[o][iscell[o]], s=2, lw=0, color=charts.line("dna"), label="cells", rasterized=True)
ax.scatter(rank[~iscell[o]], tot[o][~iscell[o]], s=2, lw=0, color=P.fill("neutral"), label="empty droplets", rasterized=True)
ax.set_xscale("log"); ax.set_yscale("log")
ax.legend(frameon=False, fontsize=7.5, markerscale=4)
charts.style_axes(ax, "barcode rank", "UMIs per barcode")
charts.title(ax, "A  Barcode rank plot")

ax = axs[1]
rec = np.linspace(500, 20000, 200)
lam = rec / 0.6 / 1e5
mult = (1 - np.exp(-lam) - lam * np.exp(-lam)) / (1 - np.exp(-lam))
ax.plot(rec / 1000, 100 * mult, color=charts.line("rna"), lw=1.6)
for r0 in (1000, 10000):
    l0 = r0 / 0.6 / 1e5
    m0 = (1 - np.exp(-l0) - l0 * np.exp(-l0)) / (1 - np.exp(-l0))
    ax.plot(r0 / 1000, 100 * m0, "o", color=charts.line("rna"), ms=4.5)
    ax.text(r0 / 1000 + 0.6, 100 * m0 - 0.6, f"{r0} cells: {100 * m0:.1f}%", fontsize=7.5, color=P.ink())
charts.style_axes(ax, "cells recovered (thousands)", "droplets with >= 2 cells (%)")
charts.title(ax, "B  Multiplets from Poisson loading")

ax = axs[2]
r = np.array([17959, 35479, 52576, 69880.])
S = np.array([.413, .585, .680, .740])


def sat_u(r, M):
    return 1 - M * (1 - np.exp(-r / M)) / r


def sat_g(r, M, k):
    return 1 - M * (1 - (1 + r / (M * k)) ** (-k)) / r


Mu = optimize.curve_fit(sat_u, r, S, p0=[3e4])[0][0]
(Mg, kg), _ = optimize.curve_fit(sat_g, r, S, p0=[3e4, 1], bounds=([1e3, 0.01], [1e6, 100]))
rr = np.linspace(2000, 250000, 400)
ax.plot(rr / 1000, sat_u(rr, Mu), color=P.muted(), lw=1.1, ls="--", label=f"equal abundance, M = {Mu:,.0f}")
ax.plot(rr / 1000, sat_g(rr, Mg, kg), color=charts.line("dna"), lw=1.6, label=f"gamma, M = {Mg:,.0f}, k = {kg:.2f}")
ax.plot(r / 1000, S, "o", color=charts.line("rna"), ms=5, label="1 to 4 lanes")
ax.axhline(0.9, color=P.muted(), lw=0.6, ls=":")
ax.set_ylim(0, 1)
ax.legend(frameon=False, fontsize=7.2, loc="lower right")
charts.style_axes(ax, "mean reads per cell (thousands)", "sequencing saturation")
charts.title(ax, "C  Sequencing saturation")
print(Mu, Mg, kg)
