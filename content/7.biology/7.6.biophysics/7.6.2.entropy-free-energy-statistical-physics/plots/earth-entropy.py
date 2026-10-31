# The entropy budget of the Earth, treating the incoming sunlight as black-body radiation at the temperature of
# the solar surface (5772 K) and the outgoing radiation as black-body radiation at the effective emission
# temperature of the Earth (255 K). In steady state the energy flows are equal.
# A: distribution of the radiated power over wavelength, d(power)/d(ln lambda), normalized to the same total
#    power for both spectra (logarithmic wavelength axis); the peaks are near 0.6 um and 13 um in this
#    representation.
# B: per joule of energy, the entropy carried ((4/3)/T for black-body radiation) and, in brackets, the number of
#    photons (mean photon energy 2.70 kBT): the Earth returns about 23 times as many photons as it receives, and
#    exports about 23 times the entropy it imports. Absorbed sunlight is dilute (not black-body at 5772 K at
#    the distance of the Earth), which raises its entropy somewhat; the order of magnitude is unchanged.
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
h, c, kB = 6.62607015e-34, 2.99792458e8, 1.380649e-23
Ts, Te = 5772.0, 255.0

fig, axs = plt.subplots(1, 2, figsize=(11.5, 3.8), gridspec_kw={"width_ratios": [1.3, 1.0]})
ax = axs[0]
lam = np.logspace(-7.3, -3.7, 600)


def per_lnlam(T):
    x = np.minimum(h * c / (lam * kB * T), 600.0)
    # lambda * B_lambda normalized by sigma T^4 / pi: (15/pi^4) x^4 / (e^x - 1)
    return 15 / np.pi ** 4 * x ** 4 / np.expm1(x)


ax.fill_between(lam * 1e6, per_lnlam(Ts), color=P.fill("highlight"), alpha=0.6, lw=0)
ax.plot(lam * 1e6, per_lnlam(Ts), color=charts.line("highlight"), lw=1.6, label="sunlight in (5772 K)")
ax.fill_between(lam * 1e6, per_lnlam(Te), color=P.fill("negative"), alpha=0.35, lw=0)
ax.plot(lam * 1e6, per_lnlam(Te), color=charts.line("negative"), lw=1.6, label="infrared out (255 K)")
ax.axvspan(0.4, 0.7, color=P.fill("positive"), alpha=0.18, lw=0)
ax.text(0.42, 0.78, "visible", fontsize=7, color=P.ink())
ax.set_xscale("log")
ax.set_xlim(0.05, 200)
ax.set_ylim(0, 0.85)
ax.legend(fontsize=7, frameon=False, loc="upper right")
charts.style_axes(ax, "wavelength λ / µm", "fraction of power per unit ln λ")
ax.set_title("A   Same energy in and out", loc="left", fontsize=9, color=P.ink())

ax = axs[1]
n_in, n_out = 1 / (2.701 * kB * Ts), 1 / (2.701 * kB * Te)
s_in, s_out = 4 / 3 / Ts, 4 / 3 / Te
ax.bar([0, 1], [s_in * 1e3, s_out * 1e3], width=0.55, color=[P.fill("highlight"), P.fill("negative")],
       edgecolor=[P.edge("highlight"), P.edge("negative")])
ax.text(0, s_in * 1e3 + 0.12, f"{s_in * 1e3:.2f}\n(4.6 × 10¹⁸ photons)", ha="center",
        fontsize=7, color=P.ink())
ax.text(1, s_out * 1e3 + 0.12, f"{s_out * 1e3:.2f}\n(1.1 × 10²⁰ photons)", ha="center",
        fontsize=7, color=P.ink())
ax.set_xticks([0, 1])
ax.set_xticklabels(["sunlight in", "infrared out"])
ax.set_ylim(0, 6.6)
charts.style_axes(ax, None, "entropy carried per joule / (mJ K⁻¹)")
ax.set_title(f"B   Entropy exported: × {s_out / s_in:.0f}", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
