"""Line profiles in atomic absorption (Na 589.0 nm in an air-acetylene flame, about 2500 K).
Left: Gaussian (Doppler, FWHM 4.4 pm), Lorentzian (pressure, FWHM 2.0 pm) and their
convolution, the Voigt profile, all with unit area. Right: the absorption line compared with
the emission line of a hollow cathode lamp (Doppler width at about 500 K, 2.0 pm, slightly
narrowed by self-absorption is ignored) and with the 0.2 nm band pass of the monochromator."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import voigt_profile

x = np.linspace(-15, 15, 1201)  # wavelength offset / pm
fwhm_g, fwhm_l = 4.4, 2.0
sigma = fwhm_g / (2 * np.sqrt(2 * np.log(2)))
gamma = fwhm_l / 2
gauss = np.exp(-x**2 / (2 * sigma**2)) / (sigma * np.sqrt(2 * np.pi))
lorentz = gamma / np.pi / (x**2 + gamma**2)
voigt = voigt_profile(x, sigma, gamma)

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.0))
ax = axes[0]
ax.plot(x, gauss, color="C0", lw=1.6, label="Gaussian (Doppler)")
ax.plot(x, lorentz, color="C1", lw=1.6, label="Lorentzian (pressure)")
ax.plot(x, voigt, color="k", lw=2.0, label="Voigt (convolution)")
ax.set_xlabel(r"$\lambda - \lambda_0$ / pm")
ax.set_ylabel("normalized profile / pm$^{-1}$")
ax.set_title("Profiles with unit area", fontsize=10)
ax.legend(fontsize=8, frameon=False)
ax.text(6, 0.02, "Lorentzian wings\ndecay as $1/x^2$", fontsize=8, color="C1")

ax = axes[1]
absn = voigt / voigt.max()
sig_s = 2.0 / (2 * np.sqrt(2 * np.log(2)))
lamp = np.exp(-x**2 / (2 * sig_s**2))
ax.fill_between(x, 0, 1.08, color="0.85", lw=0)
ax.plot(x, absn, color="k", lw=2.0, label="absorption line (~5 pm)")
ax.plot(x, lamp, color="C3", lw=1.6, label="lamp emission line (~2 pm)")
ax.text(-14.5, 0.12, "monochromator band pass (200 pm)\nextends far beyond this window",
        fontsize=8, va="bottom", color="0.35")
ax.set_ylim(0, 1.12)
ax.set_xlabel(r"$\lambda - \lambda_0$ / pm")
ax.set_ylabel("relative intensity / absorption coefficient")
ax.set_title("Sharp-line source versus absorption line", fontsize=10)
ax.legend(fontsize=8, frameon=False, loc="center right")
fig.tight_layout()
