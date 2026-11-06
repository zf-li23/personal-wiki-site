# Dual-beam experiment on detached epidermis (design after Schwartz & Zeiger 1984), simulated.
# (A) Aperture under saturating red light relaxes to a photosynthesis-driven plateau; adding low-fluence
# blue light on the red background drives a further, blue-specific opening (first-order kinetics, with a
# short lag). (B) A schematic action spectrum for blue-light-stimulated opening under a red background:
# three peaks near 420, 450 and 470 nm, little activity beyond 500 nm.
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 4, 400)  # h
red = 7.5 * (1 - np.exp(-t / 0.45))
t_on = 1.6
lag = 0.03
blue = red + 4.0 * np.clip(1 - np.exp(-(t - t_on - lag) / 0.5), 0, None)

wl = np.linspace(350, 600, 500)
spec = (0.55 * np.exp(-((wl - 420) / 15) ** 2) + 1.0 * np.exp(-((wl - 450) / 15) ** 2)
        + 0.8 * np.exp(-((wl - 472) / 13) ** 2) + 0.28 * np.exp(-((wl - 380) / 30) ** 2))
spec = spec * (1 / (1 + np.exp((wl - 500) / 6)))
spec /= spec.max()

fig, (a, b) = plt.subplots(1, 2, figsize=(10.5, 4.0), gridspec_kw=dict(width_ratios=[1.2, 1]))
a.plot(t, blue, color="#3b6fd8", lw=2.2, label="red + blue")
a.plot(t, red, color="#d9463b", lw=2.2, label="red only (saturating)")
a.annotate("blue light on", xy=(t_on, 7.0), xytext=(t_on - 0.2, 11.3), fontsize=9,
           arrowprops=dict(arrowstyle="->", lw=1.0, color="0.4"), ha="center")
a.set_xlabel("Time / h")
a.set_ylabel("Stomatal aperture / µm")
a.set_xlim(0, 4)
a.set_ylim(0, 13)
a.legend(frameon=False, fontsize=9, loc="lower right")
a.set_title("A   Blue light on a saturating red background", loc="left", fontsize=10)
b.fill_between(wl, spec, color="#6a7fe0", alpha=0.25, lw=0)
b.plot(wl, spec, color="#3b4fc0", lw=2.0)
for p in (420, 450, 472):
    b.axvline(p, color="0.6", lw=0.6, ls=":")
b.set_xlim(350, 600)
b.set_ylim(0, 1.1)
b.set_xlabel("Wavelength / nm")
b.set_ylabel("Relative effectiveness")
b.set_title("B   Action spectrum (schematic)", loc="left", fontsize=10)
for ax in (a, b):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
