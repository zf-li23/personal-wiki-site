"""Temperature correction in the metabolic theory of ecology (simulated data).

Simulated resting metabolic rates of 160 ectotherms: mass M log-uniform over 1 mg to 10 kg, body temperature drawn
from 5, 15, 25 or 35 C, B = b0 M^(3/4) exp(-E / (k T)) with E = 0.65 eV, k = 8.617e-5 eV/K and lognormal scatter
(SD 0.35 in natural log units). b0 is chosen so that a 1 kg animal at 20 C has B = 0.14 W.
A: raw data, log B against log M, colored by temperature. B: temperature-corrected rates B exp(E/(kT)) collapse onto
one line of slope 3/4. C: mass-corrected rates B M^(-3/4) against 1/(kT): an Arrhenius plot with slope -E.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
k = 8.617e-5
E = 0.65
n = 160
M = 10 ** rng.uniform(-6, 1, n)
Tc = rng.choice([5.0, 15.0, 25.0, 35.0], n)
T = Tc + 273.15
b0 = 0.14 / np.exp(-E / (k * 293.15))
B = b0 * M ** 0.75 * np.exp(-E / (k * T)) * np.exp(rng.normal(0, 0.35, n))
cols = {5.0: "dna", 15.0: "plant", 25.0: "highlight", 35.0: "negative"}

fig, axes = plt.subplots(1, 3, figsize=(14.0, 4.3))
ax, bx, cx = axes
for t, tok in cols.items():
    s = Tc == t
    ax.scatter(M[s], B[s], s=14, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, label=f"{t:.0f} $^\\circ$C")
    bx.scatter(M[s], B[s] * np.exp(E / (k * T[s])), s=14, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.6)
    cx.scatter(1 / (k * T[s]), np.log(B[s] * M[s] ** -0.75), s=14, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.6)
for a in (ax, bx):
    a.set_xscale("log")
    a.set_yscale("log")
    a.set_xlabel("body mass $M$ / kg")
ax.set_ylabel("metabolic rate $B$ / W")
ax.legend(frameon=False, fontsize=8, title="body temperature", title_fontsize=8, loc="upper left")
ax.set_title("A  Raw rates", loc="left", fontsize=10)

x = np.log(M)
y = np.log(B * np.exp(E / (k * T)))
slope, icpt = np.polyfit(x, y, 1)
mm = np.logspace(-6, 1, 20)
bx.plot(mm, np.exp(icpt) * mm ** slope, color=P.ink(), lw=1.5)
bx.text(1e-5, np.exp(icpt) * 3e-1 ** 0 * 1e-2 * 30, f"OLS slope {slope:.2f}", fontsize=8.5, color=P.ink())
bx.set_ylabel("temperature-corrected rate $B\\,\\mathrm{e}^{E/(k_{\\mathrm{B}}T)}$")
bx.set_title("B  Correcting for temperature", loc="left", fontsize=10)

xx = 1 / (k * T)
yy = np.log(B * M ** -0.75)
s2, i2 = np.polyfit(xx, yy, 1)
xl = np.linspace(xx.min(), xx.max(), 10)
cx.plot(xl, i2 + s2 * xl, color=P.ink(), lw=1.5)
cx.text(xx.mean(), (i2 + s2 * xx.mean()) + 1.2, f"slope $-E$ = {s2:.2f} eV", fontsize=8.5, color=P.ink())
cx.set_xlabel("$1/(k_{\\mathrm{B}}T)$ / eV$^{-1}$")
cx.set_ylabel("$\\ln(B\\,M^{-3/4})$")
cx.set_title("C  Arrhenius plot of mass-corrected rates", loc="left", fontsize=10)
for a in axes:
    for s in ("top", "right"):
        a.spines[s].set_visible(False)
fig.tight_layout()
