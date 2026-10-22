import numpy as np
import matplotlib.pyplot as plt


def wavelength_rgb(nm):
    """Approximate colour of monochromatic light (Bruton's piecewise model)."""
    if nm < 440:
        r, g, b = (440 - nm) / 60, 0.0, 1.0
    elif nm < 490:
        r, g, b = 0.0, (nm - 440) / 50, 1.0
    elif nm < 510:
        r, g, b = 0.0, 1.0, (510 - nm) / 20
    elif nm < 580:
        r, g, b = (nm - 510) / 70, 1.0, 0.0
    elif nm < 645:
        r, g, b = 1.0, (645 - nm) / 65, 0.0
    else:
        r, g, b = 1.0, 0.0, 0.0
    fade = 0.3 + 0.7 * (nm - 380) / 40 if nm < 420 else (0.3 + 0.7 * (750 - nm) / 50 if nm > 700 else 1.0)
    return (r * fade, g * fade, b * fade)


nu = np.linspace(12000, 30000, 600)  # wavenumber / cm^-1
band = np.exp(-(((nu - 20450) / 2300) ** 2)) + 0.5 * np.exp(-(((nu - 17400) / 1700) ** 2))
band /= band.max()

fig, (ax, strip) = plt.subplots(2, 1, figsize=(9, 5.2), sharex=True, gridspec_kw={"height_ratios": [5, 0.6]})
ax.plot(nu, band, color="#7c3aed", lw=2.2)
ax.axvline(20300, color="#94a3b8", lw=1, ls="--")
ax.text(20500, 1.02, r"$\tilde\nu_{max}$ = 20 300 cm$^{-1}$ = $\Delta_o$", fontsize=10)
ax.annotate("shoulder (Jahn-Teller splitting\nof the excited state)", xy=(17600, 0.84), xytext=(12600, 0.95), fontsize=9,
            arrowprops=dict(arrowstyle="->", color="#94a3b8"))
ax.set_ylabel("relative absorbance")
ax.set_ylim(0, 1.15)
ax.set_title(r"[Ti(H$_2$O)$_6$]$^{3+}$: $t_{2g}^1 \to e_g^1$ absorbs blue-green light; the solution looks red-violet", fontsize=11)

top = ax.secondary_xaxis("top", functions=(lambda w: 1e7 / np.maximum(w, 1), lambda l: 1e7 / np.maximum(l, 1)))
top.set_xticks([800, 700, 600, 500, 450, 400, 350])
top.set_xlabel("wavelength / nm")

img = np.array([[wavelength_rgb(min(max(1e7 / w, 380), 750)) if 1e7 / w <= 750 and 1e7 / w >= 380 else (0.5, 0.5, 0.5) for w in nu]])
strip.imshow(img, aspect="auto", extent=(nu[0], nu[-1], 0, 1))
strip.set_yticks([])
strip.set_xlabel(r"wavenumber / cm$^{-1}$")
fig.tight_layout()
