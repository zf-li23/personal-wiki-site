# Three estimates behind the physicists' picture of the gene (1935-1944).
# A: target theory. If one ionization inside a sensitive volume (the target) suffices to cause a mutation, the
#    number of hits is Poisson with mean sigma*D, and the mutated fraction is 1 - exp(-sigma D): linear at low dose,
#    with no threshold. A target that needs two hits gives 1 - exp(-x)(1 + x), quadratic at low dose.
#    Dose in units of 1/sigma.
# B: thermal stability (Schroedinger's table): a configuration separated from its neighbours by a barrier W
#    survives on average tau = tau0 exp(W / kBT), tau0 = 1e-14 s; W/kBT = 30, 50, 60 give 0.1 s, 16 months and
#    about 30 000 years.
# C: the sqrt(N) rule: a system of N independent particles fluctuates by about 1/sqrt(N); for a gene of about
#    1000 atoms treated as a little gas this is 3 %, far larger than observed mutation rates (about 1e-5 to 1e-8
#    per gene per generation), so the order of the gene cannot be statistical.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(13.0, 3.7))

ax = axs[0]
x = np.linspace(0, 4, 300)
ax.plot(x, 1 - np.exp(-x), color=charts.line("dna"), lw=1.9, label="one hit: 1 − e^(−σD)")
ax.plot(x, 1 - np.exp(-x) * (1 + x), color=charts.line("negative"), lw=1.6, ls=(0, (5, 2.5)),
        label="two hits")
ax.plot(x[x < 0.8], x[x < 0.8], color=P.muted(), lw=0.9, ls=":")
ax.text(0.62, 0.42, "slope σ", fontsize=7, color=P.muted())
ax.set_xlim(0, 4)
ax.set_ylim(0, 1.02)
ax.legend(fontsize=7, frameon=False, loc="lower right")
charts.style_axes(ax, "dose σD", "fraction mutated")
ax.set_title("A   Target theory", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
w = np.linspace(20, 70, 300)
tau = 1e-14 * np.exp(w)
ax.semilogy(w, tau, color=charts.line("protein"), lw=1.9)
marks = [(30, "0.1 s"), (50, "16 months"), (60, "30 000 yr")]
for ww, txt in marks:
    tt = 1e-14 * np.exp(ww)
    ax.plot([ww], [tt], "o", color=charts.line("protein"), ms=5)
    ax.text(ww - 1.0, tt * 4, txt, fontsize=7, color=P.ink(), ha="right")
for yy, txt in ((1, "1 s"), (3.156e7, "1 yr"), (3.156e7 * 1e6, "1 Myr")):
    ax.axhline(yy, color=P.muted(), lw=0.6, ls=":")
    ax.text(70.5, yy, txt, fontsize=6.5, color=P.muted(), va="center")
ax.set_xlim(20, 70)
charts.style_axes(ax, "barrier W / kBT  (1 eV ≈ 39 kBT at 300 K)", "mean lifetime τ / s")
ax.set_title("B   Thermal stability", loc="left", fontsize=9, color=P.ink())

ax = axs[2]
n = np.logspace(0, 24, 200)
ax.loglog(n, 1 / np.sqrt(n), color=charts.line("neutral"), lw=1.9)
ax.plot([1e3], [1e3 ** -0.5], "o", color=charts.line("negative"), ms=5)
ax.text(2e3, 5e-2, "gene of ~1000 atoms:\n3 % fluctuation", fontsize=7, color=P.ink())
ax.axhspan(1e-8, 1e-5, color=P.fill("positive"), alpha=0.3, lw=0)
ax.text(2e12, 2e-7, "observed mutation\nrates per gene", fontsize=7, color=P.ink())
ax.set_xlim(1, 1e24)
ax.set_ylim(1e-12, 2)
ax.set_xticks([1, 1e6, 1e12, 1e18, 1e24])
charts.style_axes(ax, "number of particles N", "relative fluctuation 1/√N")
ax.set_title("C   The √N rule", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
