# Translocation of DNA through a solid-state nanopore (simulation and model).
# Pore: diameter 4 nm, membrane 10 nm, 1 M KCl (sigma = 11 S/m): open conductance from channel plus access
# resistance, G = sigma (4L/(pi d^2) + 1/d)^-1 = 10.5 nS (a model of an ideal cylinder).
# Molecules: 5 kbp dsDNA (diameter 2.2 nm), blockade from the excluded cross-section, Delta G / G ~ (2.2/4)^2 in
# the channel part. Capture rate R = pi c d^2 mu V / (4 L) (diffusion-limited capture radius, independent of D)
# for c = 1 nM and mu = 3.2e-8 m^2/(V s). Dwell times: first passage of drift-diffusion over the contour
# length, an inverse Gaussian with Peclet number 20 and mean 0.5 ms at 300 mV, mean scaling as 1/V.
# A: current trace at 300 mV and 10 nM DNA with Poisson-distributed events and noise (10 us samples).
# B: event scatter plot (blockade depth against dwell time) at 200 and 400 mV.
# C: capture rate against voltage (linear) and dwell-time histogram at 300 mV with the inverse-Gaussian density.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
sig, d, L = 11.0, 4e-9, 10e-9
G0 = sig / (4 * L / (np.pi * d**2) + 1 / d)
dG = G0 * (4 * L / (np.pi * d**2)) / (4 * L / (np.pi * d**2) + 1 / d) * (2.2 / 4.0) ** 2
mu, c = 3.2e-8, 1e-9 * 6.022e23 * 1e3   # 1 nM in m^-3
Pe = 20.0


def rate(V):
    return np.pi * c * d**2 * mu * V / (4 * L)


def dwell(V, n):
    m = 0.5e-3 * 0.3 / V
    lam = m * Pe / 2
    return rng.wald(m, lam, n)


fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.2), gridspec_kw={"width_ratios": [1.5, 1, 1]})
V = 0.3
dt, T = 1e-5, 0.5
t = np.arange(0, T, dt)
I0 = G0 * V
nev = rng.poisson(10 * rate(V) * T)   # 10 nM DNA
starts = np.sort(rng.uniform(0, T, nev))
cur = np.full(t.size, I0)
for s0, w in zip(starts, dwell(V, nev)):
    a, b = int(s0 / dt), int((s0 + max(w, dt)) / dt)
    cur[a:b] -= dG * V * rng.uniform(0.9, 1.1)
cur += rng.normal(0, 0.04 * I0 * 0.25, t.size)
ax = axs[0]
ax.plot(t, cur * 1e9, color=charts.line("dna"), lw=0.5)
ax.text(0.02, I0 * 1e9 * 1.05, f"open pore: G = {G0 * 1e9:.1f} nS, I = {I0 * 1e9:.2f} nA", fontsize=8, color=P.ink())
ax.set_ylim(I0 * 1e9 * 0.55, I0 * 1e9 * 1.12)
charts.style_axes(ax, "time / s", "current / nA")
charts.title(ax, f"A   300 mV, 10 nM DNA ({rate(V):.1f} events per s per nM)")
ax.set_xlim(0, T)
ax = axs[1]
for Vv, tok in ((0.2, "dna2"), (0.4, "rna")):
    w = dwell(Vv, 300)
    depth = dG / G0 * rng.normal(1, 0.06, 300)
    ax.plot(w * 1e3, depth, "o", ms=2.5, color=charts.line(tok), alpha=0.8, label=f"{int(Vv * 1e3)} mV")
ax.set_ylim(0, 0.4)
ax.legend(fontsize=8, frameon=False)
charts.style_axes(ax, "dwell time / ms", "ΔI / I0")
charts.title(ax, "B   Event scatter plot")
ax = axs[2]
w = dwell(0.3, 3000)
ax.hist(w * 1e3, bins=60, range=(0, 1.5), density=True, color=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.3)
x = np.linspace(1e-3, 1.5, 300) * 1e-3
m = 0.5e-3
lam = m * Pe / 2
f = np.sqrt(lam / (2 * np.pi * x**3)) * np.exp(-lam * (x - m) ** 2 / (2 * m**2 * x))
ax.plot(x * 1e3, f * 1e-3, color=charts.line("negative"), lw=1.5, label="inverse Gaussian")
ax.legend(fontsize=7.5, frameon=False)
charts.style_axes(ax, "dwell time / ms", "density / ms⁻¹")
charts.title(ax, "C   First-passage dwell times")
ins = ax.inset_axes([0.55, 0.45, 0.4, 0.3])
Vs = np.linspace(0.1, 0.5, 5)
ins.plot(Vs * 1e3, rate(Vs), "o-", ms=3, color=charts.line("dna"), lw=1)
ins.set_xlabel("V / mV", fontsize=6.5)
ins.set_ylabel("R / s⁻¹", fontsize=6.5)
ins.tick_params(labelsize=6)
fig.tight_layout()
