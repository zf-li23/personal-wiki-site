"""Zeeman background correction with a transverse magnetic field at the atomizer (Cd 228.8 nm,
a 1S0-1P1 line with a normal Zeeman pattern; B = 1.0 T shifts the sigma components by about
2.4 pm). Left, field off: the lamp line sees atomic absorption plus background. Right, field
on, light polarized perpendicular to B: the pi component (which absorbs only light polarized
parallel to B) is invisible and the sigma components have moved off the lamp line, so only
the broad background absorbs."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import voigt_profile

x = np.linspace(-6, 6, 1201)  # pm
sig, gam = 0.8 / 2.3548, 0.25
prof = voigt_profile(x, sig, gam)
prof = prof / prof.max()
shift = 2.4
sigma_comp = 0.5 * (voigt_profile(x - shift, sig, gam) + voigt_profile(x + shift, sig, gam))
sigma_comp = sigma_comp / voigt_profile(0, sig, gam)
bg = 0.25 + 0.01 * x
lamp = np.exp(-x**2 / (2 * (0.3 / 2.3548) ** 2))

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.0), sharey=True)
ax = axes[0]
ax.plot(x, prof + bg, color="k", lw=1.8, label="atomic + background")
ax.plot(x, bg, color="0.5", lw=1.3, ls="--", label="background")
ax.fill_between(x, 0, 1.25 * lamp, color="C3", alpha=0.35, lw=0, label="lamp line")
ax.set_title("Field off: measures $A_{\\mathrm{atomic}} + A_{\\mathrm{bg}}$", fontsize=10)
ax.set_xlabel(r"$\lambda - \lambda_0$ / pm")
ax.set_ylabel("absorbance (arbitrary)")
ax.legend(fontsize=8, frameon=False, loc="upper right")

ax = axes[1]
ax.plot(x, prof + bg, color="C0", lw=1.0, ls=":", label=r"$\pi$ component (parallel to $B$, blocked)")
ax.plot(x, sigma_comp + bg, color="k", lw=1.8, label=r"$\sigma^{\pm}$ components + background")
ax.plot(x, bg, color="0.5", lw=1.3, ls="--")
ax.fill_between(x, 0, 1.25 * lamp, color="C3", alpha=0.35, lw=0)
ax.annotate("", xy=(shift, 0.85), xytext=(-shift, 0.85), arrowprops=dict(arrowstyle="<->", color="0.3"))
ax.text(0, 0.9, r"$2\Delta\lambda_{\mathrm{Z}}$", ha="center", fontsize=9)
ax.set_title("Field on, light perpendicular to $B$: measures $A_{\\mathrm{bg}}$", fontsize=10)
ax.set_xlabel(r"$\lambda - \lambda_0$ / pm")
ax.set_ylim(0, 1.45)
ax.legend(fontsize=8, frameon=False, loc="upper right")
fig.tight_layout()
