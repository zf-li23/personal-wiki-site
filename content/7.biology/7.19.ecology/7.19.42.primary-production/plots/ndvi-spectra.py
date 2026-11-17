# Schematic reflectance spectra of four surfaces and their NDVI in Landsat-like bands
# (red 630-690 nm, NIR 770-900 nm). Curves are smooth idealizations, not measured spectra.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio

P = bio.P
wl = np.linspace(400, 1100, 701)


def sig(x, x0, w):
    return 1 / (1 + np.exp(-(x - x0) / w))


green = 0.05 + 0.07 * np.exp(-((wl - 550) / 30) ** 2) - 0.02 * np.exp(-((wl - 670) / 20) ** 2) \
    + 0.43 * sig(wl, 715, 12) - 0.03 * np.exp(-((wl - 970) / 25) ** 2)
dry = 0.08 + 0.22 * sig(wl, 560, 60) + 0.12 * sig(wl, 720, 40)
soil = 0.10 + 0.20 * (wl - 400) / 700
water = 0.07 * np.exp(-(wl - 400) / 180) + 0.005
surfaces = [("green vegetation", green, "plant"), ("dry vegetation", dry, "antibody"),
            ("bare soil", soil, "animal"), ("clear water", water, "dna")]
red = (wl >= 630) & (wl <= 690)
nir = (wl >= 770) & (wl <= 900)
fig, ax = plt.subplots(figsize=(9.2, 4.6))
ax.axvspan(630, 690, color=P.fill("negative"), alpha=0.35, lw=0)
ax.axvspan(770, 900, color=P.fill("protein"), alpha=0.3, lw=0)
ax.text(660, 0.6, "red", ha="center", fontsize=8, color=P.ink())
ax.text(835, 0.6, "near infrared", ha="center", fontsize=8, color=P.ink())
for name, r, tok in surfaces:
    nd = (r[nir].mean() - r[red].mean()) / (r[nir].mean() + r[red].mean())
    ax.plot(wl, r, color=P.edge(tok), lw=2, label=f"{name}: NDVI = {nd:.2f}")
ax.annotate("red edge", (715, 0.27), xytext=(560, 0.42), fontsize=8, color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
ax.annotate("chlorophyll\nabsorption", (670, 0.035), xytext=(470, 0.22), fontsize=8, color=P.ink(),
            arrowprops=dict(arrowstyle="-", color=P.muted(), lw=0.8))
ax.set_xlim(400, 1100)
ax.set_ylim(0, 0.65)
ax.set_xlabel("Wavelength / nm")
ax.set_ylabel("Reflectance")
ax.legend(frameon=False, fontsize=8, loc="upper left", bbox_to_anchor=(1.0, 1.0))
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
fig.tight_layout()
