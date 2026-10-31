# The electron as a wave: relativistic wavelength and interaction constant against accelerating voltage.
# A: de Broglie wavelength lambda = h / sqrt(2 m0 e U (1 + e U / (2 m0 c^2))) (solid) and the
#    non-relativistic value h / sqrt(2 m0 e U) (dashed); markers at 80, 120, 200 and 300 kV, the
#    voltages of biological transmission microscopes. Right axis: beta = v / c.
# B: interaction constant sigma = 2 pi m e lambda / h^2 with the relativistic mass m = gamma m0, which
#    converts a projected potential (V nm) into a phase shift (rad); it falls with voltage, so faster
#    electrons are scattered less (thicker specimens are tolerated) but also give less contrast.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
h, m0, e, c = 6.62607015e-34, 9.1093837e-31, 1.602176634e-19, 299792458.0

U = np.logspace(np.log10(10e3), np.log10(3e6), 300)
gamma = 1 + e * U / (m0 * c**2)
lam = h / np.sqrt(2 * m0 * e * U * (1 + e * U / (2 * m0 * c**2)))
lam_nr = h / np.sqrt(2 * m0 * e * U)
beta = np.sqrt(1 - 1 / gamma**2)
sigma = 2 * np.pi * gamma * m0 * e * lam / h**2 * 1e-9     # rad / (V nm)

fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.2))
ax = axs[0]
ax.plot(U / 1e3, lam * 1e12, color=charts.line("protein"), lw=2.0, label="relativistic")
ax.plot(U / 1e3, lam_nr * 1e12, color=charts.line("protein"), lw=1.2, ls="--", label="non-relativistic")
for kv in (80, 120, 200, 300):
    uu = kv * 1e3
    ll = h / np.sqrt(2 * m0 * e * uu * (1 + e * uu / (2 * m0 * c**2))) * 1e12
    ax.plot(kv, ll, "o", color=charts.line("highlight"), ms=5)
    ax.annotate(f"{kv} kV\n{ll:.2f} pm", (kv, ll), xytext=(6, 6), textcoords="offset points",
                fontsize=7, color=P.ink())
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(10, 3000)
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(ax, "accelerating voltage U / kV", "wavelength λ / pm")
charts.title(ax, "A   Electron wavelength")
ax2 = ax.twinx()
ax2.plot(U / 1e3, beta, color=charts.line("neutral"), lw=1.0, ls=":")
ax2.set_ylim(0, 1.05)
ax2.set_ylabel("β = v / c (dotted)", fontsize=8, color=P.muted())
ax2.tick_params(colors=P.muted(), labelcolor=P.muted(), labelsize=7)
for name, sp in ax2.spines.items():
    sp.set_visible(name == "right")
    sp.set_color(P.muted())

ax = axs[1]
ax.plot(U / 1e3, sigma, color=charts.line("dna"), lw=2.0)
for kv in (120, 200, 300):
    i = np.argmin(abs(U - kv * 1e3))
    ax.plot(kv, sigma[i], "o", color=charts.line("highlight"), ms=5)
    ax.annotate(f"{sigma[i] * 1e3:.2f}", (kv, sigma[i]), xytext=(5, 5), textcoords="offset points",
                fontsize=7, color=P.ink())
ax.set_xscale("log")
ax.set_xlim(10, 3000)
ax.set_ylim(0, 0.025)
charts.style_axes(ax, "accelerating voltage U / kV", "σ / (rad V⁻¹ nm⁻¹)")
charts.title(ax, "B   Interaction constant (labels in 10⁻³ rad V⁻¹ nm⁻¹)")
fig.tight_layout()
