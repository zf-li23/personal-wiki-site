"""Urban ecosystems: diversity along an urbanization gradient and flood hydrographs (Section 54.4).

A, B: schematic model (not data) of the patterns summarized by McKinney (2002, 2008).
Urbanization index u from 0 (wildland) to 1 (urban core). Plants: native richness 100 (1 - u)^0.7,
introduced (non-native) richness 150 u (1 - u)^0.6, total = sum (peaks at intermediate,
suburban urbanization). Birds: richness 60 (1 - 0.75 u^1.5); total abundance and the share of
urban exploiters (synanthropic species) 0.1 + 0.85 u^2.
C: runoff from 10 mm of rain falling in 2 hours on a 50 km^2 catchment, routed through a Nash
cascade of n = 3 linear reservoirs with storage constant k (unit hydrograph
u(t) = t^(n-1) e^(-t/k) / (k^n Gamma(n)); peak proportional to 1/k, Proposition 54.4.1):
natural channel k = 6 h, runoff coefficient 0.3; channelized (Manning n from 0.035 to 0.013, flow
velocity x 2.7, k = 2.2 h); channelized with paved catchment (runoff coefficient 0.7).
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma

import wikibio as bio
from wikibio import charts as C

P = bio.P
FS = bio.core.FONT

fig, axes = plt.subplots(1, 3, figsize=(13, 3.9))
u = np.linspace(0, 1, 300)

ax = axes[0]
nat = 100 * (1 - u) ** 0.7
exo = 150 * u * (1 - u) ** 0.6
ax.plot(u, nat, color=C.line("plant"), lw=2, label="native plants")
ax.plot(u, exo, color=C.line("rna"), lw=2, label="introduced plants")
ax.plot(u, nat + exo, color=P.ink(), lw=2.2, label="total")
ax.set_xlim(0, 1)
ax.set_ylim(0, 140)
ax.set_xticks([0, 0.5, 1], ["wildland", "suburban", "urban core"])
C.style_axes(ax, "urbanization", "species richness (schematic)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "A  Plants: a suburban peak")

ax = axes[1]
ax.plot(u, 60 * (1 - 0.75 * u ** 1.5), color=C.line("dna"), lw=2, label="bird species richness")
ax2 = ax.twinx()
ax2.plot(u, 100 * (0.1 + 0.85 * u ** 2), color=C.line("negative"), lw=2, ls=(0, (4, 2)))
ax.plot([], [], color=C.line("negative"), lw=2, ls=(0, (4, 2)), label="urban exploiters (% of birds)")
ax.set_xlim(0, 1)
ax.set_ylim(0, 70)
ax2.set_ylim(0, 100)
ax.set_xticks([0, 0.5, 1], ["wildland", "suburban", "urban core"])
C.style_axes(ax, "urbanization", "species richness (schematic)")
C.style_axes(ax2, None, "share of individuals (%)")
ax2.spines["right"].set_visible(True)
ax2.spines["right"].set_color(P.muted())
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="lower left")
C.title(ax, "B  Birds: fewer species, more of a few")

ax = axes[2]
dt = 0.05
t = np.arange(0, 48, dt)
rain = np.where(t < 2, 10 / 2, 0.0)  # mm per hour
area = 50e6  # m^2


def hydrograph(k, coef, n=3):
    uh = t ** (n - 1) * np.exp(-t / k) / (k ** n * gamma(n))
    q = np.convolve(rain * coef, uh)[: len(t)] * dt  # mm per hour of runoff
    return q * 1e-3 * area / 3600  # m^3 per second


for k, coef, col, lab in ((6.0, 0.3, C.line("plant"), "natural channel"),
                          (2.2, 0.3, C.line("dna"), "channelized"),
                          (2.2, 0.7, C.line("negative"), "channelized + paved catchment")):
    q = hydrograph(k, coef)
    ax.plot(t, q, color=col, lw=2, label=f"{lab} (peak {q.max():.0f} m³/s)")
ax.set_xlim(0, 36)
ax.set_ylim(0, None)
C.style_axes(ax, "time since rain began (h)", "discharge at the outlet (m³/s)")
ax.legend(frameon=False, fontsize=FS["tiny"], labelcolor=P.ink(), loc="upper right")
C.title(ax, "C  Faster channels, higher peaks downstream")
fig.tight_layout()
