# Sunlight as a supply of photons.
# The solar spectrum above the atmosphere is approximated by a black body at 5772 K scaled to the solar
# constant 1361 W m^-2 (the atmosphere removes about a quarter of it, mostly in the infrared; at sea level
# the total is about 1000 W m^-2, the rule of thumb of the text).
# A: spectral irradiance (energy per nm) with the photosynthetically active band 400-700 nm.
# B: the same light counted as photons per nm (n = I lambda / hc); the photon count peaks further to the red
#    than the energy, because red photons carry less energy each. Upper axis of B: photon energy in units of
#    k_B T at 310 K.
# C: photon energy compared with other energies of the cell (k_B T at 310 K, log scale).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
h, c, kB, NA = 6.62607015e-34, 299792458.0, 1.380649e-23, 6.02214076e23
T_sun = 5772.0
lam = np.linspace(200e-9, 2500e-9, 4000)
B = 2 * h * c**2 / lam**5 / np.expm1(h * c / (lam * kB * T_sun))
lam_all = np.linspace(50e-9, 20000e-9, 200000)
B_all = 2 * h * c**2 / lam_all**5 / np.expm1(h * c / (lam_all * kB * T_sun))
scale = 1361.0 / np.trapezoid(B_all, lam_all)
I = B * scale * 1e-9                      # W m^-2 nm^-1
nph = I * lam / (h * c)                   # photons m^-2 s^-1 nm^-1
nm = lam * 1e9
par = (nm >= 400) & (nm <= 700)

fig, axs = plt.subplots(1, 3, figsize=(14.0, 4.0), gridspec_kw=dict(width_ratios=[1, 1, 0.9]))
ax = axs[0]
ax.fill_between(nm[par], I[par], color=P.fill("chloroplast"), alpha=0.4, lw=0)
ax.plot(nm, I, color=charts.line("atp"), lw=1.8)
ax.text(1000, 1.45, "PAR\n400-700 nm\n37 %", ha="center", fontsize=7.5, color=P.ink())
ax.set_xlim(200, 2500)
ax.set_ylim(0, 2.3)
charts.style_axes(ax, "wavelength / nm", "spectral irradiance / (W m⁻² nm⁻¹)")
charts.title(ax, "A   Energy per wavelength (top of atmosphere)")

ax = axs[1]
ax.fill_between(nm[par], nph[par] / 1e18, color=P.fill("chloroplast"), alpha=0.4, lw=0)
ax.plot(nm, nph / 1e18, color=charts.line("dna"), lw=1.8)
ax.set_xlim(200, 2500)
ax.set_ylim(0, None)
charts.style_axes(ax, "wavelength / nm", "photon flux / (10¹⁸ m⁻² s⁻¹ nm⁻¹)")
charts.title(ax, "B   Photons per wavelength")
top = ax.secondary_xaxis("top", functions=(lambda x: h * c / (np.maximum(x, 1) * 1e-9) / (kB * 310),
                                          lambda e: h * c / (np.maximum(e, 1e-3) * kB * 310) * 1e9))
top.set_xticks([100, 60, 40, 30, 20])
top.tick_params(colors=P.muted(), labelcolor=P.ink(), labelsize=7)
top.set_xlabel(r"photon energy / $k_{\mathrm{B}}T$ (310 K)", fontsize=7.5, color=P.ink())

ax = axs[2]
kT = kB * 310
items = [
    ("UV-B, 300 nm", h * c / 300e-9 / kT, "drug"),
    ("blue, 450 nm", h * c / 450e-9 / kT, "dna"),
    ("green, 500 nm", h * c / 500e-9 / kT, "chloroplast"),
    ("red, 680 nm (P680)", h * c / 680e-9 / kT, "rna"),
    ("far red, 870 nm (P870)", h * c / 870e-9 / kT, "mitochondrion"),
    ("electron, H₂O → NADP⁺ (1.14 V)", 1.14 * 1.602176634e-19 / kT, "enzyme"),
    ("ATP hydrolysis (cell)", 20.0, "atp"),
    ("proton across 200 mV", 7.5, "h"),
    ("H bond in water", 2.0, "neutral"),
    ("thermal energy", 1.0, "neutral"),
]
y = np.arange(len(items))[::-1]
for yi, (name, v, tok) in zip(y, items):
    ax.barh(yi, v, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, height=0.62)
    ax.text(v * 1.12, yi, f"{v:.0f}", va="center", fontsize=7, color=P.ink())
ax.set_yticks(y)
ax.set_yticklabels([it[0] for it in items], fontsize=7)
ax.set_xscale("log")
ax.set_xlim(0.8, 400)
charts.style_axes(ax, r"energy / $k_{\mathrm{B}}T$ (310 K)")
charts.title(ax, "C   A photon among cellular energies")
fig.subplots_adjust(left=0.05, right=0.985, bottom=0.14, top=0.84, wspace=0.42)
