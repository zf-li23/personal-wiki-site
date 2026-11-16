# Light in water (computed from the Beer-Lambert law).
# A: spectral irradiance with depth in pure water, E(lambda, z) = E(lambda, 0) exp(-a_w(lambda) z), using the
#    absorption coefficients of pure water of Pope and Fry (1997) at 25 nm intervals (scattering neglected);
#    the surface spectrum is taken as flat across 400-700 nm (relative units).
# B: total PAR against depth for three diffuse attenuation coefficients Kd typical of clear ocean (0.05 m^-1),
#    coastal water (0.3 m^-1) and a turbid eutrophic lake (1.5 m^-1); the 1% level marks the base of the
#    euphotic zone, z_eu = ln(100) / Kd.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
wl = np.array([400, 425, 450, 475, 500, 525, 550, 575, 600, 625, 650, 675, 700])
aw = np.array([0.0066, 0.0048, 0.0092, 0.0114, 0.0204, 0.0368, 0.0565, 0.0918, 0.2224, 0.2955, 0.34,
               0.425, 0.65])
grid = np.linspace(400, 700, 301)
a_i = np.interp(grid, wl, aw)

fig, (a, b) = plt.subplots(1, 2, figsize=(10.8, 4.3))
for z, tok in ((0, "neutral"), (1, "highlight"), (5, "atp"), (10, "rna"), (25, "enzyme"), (50, "dna"),
               (100, "metabolite")):
    a.plot(grid, np.exp(-a_i * z), color=P.edge(tok), lw=1.8, label="%d m" % z)
a.set_xlim(400, 700)
a.set_ylim(0, 1.05)
a.set_xlabel("Wavelength / nm")
a.set_ylabel("Irradiance relative to surface")
a.legend(frameon=False, fontsize=7.5, loc="upper right", title="depth", title_fontsize=7.5)
a.set_title("A  Spectrum with depth (pure water)", loc="left", fontweight="bold")

z = np.linspace(0, 120, 601)
for kd, tok, name in ((0.05, "dna", "clear ocean"), (0.3, "enzyme", "coastal"), (1.5, "plant", "turbid lake")):
    b.plot(100 * np.exp(-kd * z), z, color=P.edge(tok), lw=2, label="%s, Kd = %g m⁻¹" % (name, kd))
    zeu = np.log(100) / kd
    if zeu < 120:
        b.plot(1, zeu, "o", color=P.edge(tok), ms=5)
        b.text(1.3, zeu, "  z_eu = %.0f m" % zeu, va="center", fontsize=7.5, color=P.edge(tok))
b.set_xscale("log")
b.set_xlim(0.1, 120)
b.set_ylim(120, 0)
b.axvline(1, color=P.muted(), lw=0.7, ls=":")
b.set_xlabel("PAR / % of surface (log scale)")
b.set_ylabel("Depth / m")
b.legend(frameon=False, fontsize=7.5, loc="lower left")
b.set_title("B  Attenuation and the euphotic zone", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
