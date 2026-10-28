# Recombination rate along a simulated chromosome and the Marey map of genetic against physical position
import numpy as np
import wikibio as bio
from wikibio import charts

rng = np.random.default_rng(0)
x = np.linspace(0, 100, 5001)  # Mb
cen = 48.0
base = 0.35 + 1.6 * (np.abs(x - cen) / 52) ** 2           # higher toward telomeres
base *= 1 - 0.97 * np.exp(-((x - cen) / 6.0) ** 2)        # suppressed around the centromere
hot = np.zeros_like(x)
for c in rng.uniform(2, 98, 45):
    if abs(c - cen) > 8:
        hot += rng.uniform(4, 14) * np.exp(-((x - c) / 0.12) ** 2)
rate = base + hot
dx = x[1] - x[0]
total = 150.0
rate *= total / (rate.sum() * dx)                          # scale to a 150 cM chromosome
cum = np.cumsum(rate) * dx

fig, ax = bio.canvas(19, 7.8)
a = charts.axes_at(ax, (1.4, 1.2, 7.4, 5.8))
a.plot(x, rate, color=charts.line("dna"), lw=0.9)
a.axvspan(cen - 1.5, cen + 1.5, color=bio.P.fill("neutral"), lw=0)
a.text(cen, rate.max() * 0.9, "centromere", ha="center", fontsize=7.5, color=bio.P.ink())
a.set_xlim(0, 100)
charts.style_axes(a, "physical position / Mb", "recombination rate / (cM/Mb)")
charts.title(a, "A   local rate with hotspots")

b = charts.axes_at(ax, (11.0, 1.2, 7.0, 5.8))
b.plot(x, cum, color=charts.line("receptor"), lw=2)
b.plot([0, 100], [0, total], color=charts.line("neutral"), lw=1, ls="--")
b.axvspan(cen - 1.5, cen + 1.5, color=bio.P.fill("neutral"), lw=0)
b.set_xlim(0, 100)
b.set_ylim(0, total * 1.05)
charts.style_axes(b, "physical position / Mb", "genetic position / cM")
charts.title(b, "B   Marey map")
