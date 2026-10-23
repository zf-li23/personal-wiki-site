"""Left: scalar-theory efficiency of a blazed grating in Littrow mounting,
eta_m(lambda) = sinc^2(lambda_B/lambda - m), for first-order blaze wavelength 500 nm and
orders m = 1, 2, 3; the efficiency falls to (2/pi)^2 = 0.405 at lambda_B/(m +/- 1/2).
Right: schematic two-dimensional echellogram of an echelle grating (79 grooves/mm,
blaze angle 63.4 deg) with a prism cross-disperser; each horizontal stripe is one order,
covering one free spectral range lambda/m."""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axes[0]
lamB = 500.0
lam = np.linspace(150, 1200, 2000)
for m, col in [(1, "C0"), (2, "C1"), (3, "C3")]:
    eta = np.sinc(lamB / lam - m) ** 2
    ax.plot(lam, eta, color=col, lw=1.7, label=f"m = {m}")
    lo, hi = lamB / (m + 0.5), lamB / (m - 0.5)
    ax.plot([lo, hi], [0.405, 0.405], color=col, lw=4, alpha=0.35, solid_capstyle="butt")
ax.axhline(0.405, color="0.6", lw=0.6, ls=":")
ax.set_xlim(150, 1200)
ax.set_ylim(0, 1.05)
ax.set_xlabel(r"$\lambda$ / nm")
ax.set_ylabel("relative efficiency")
ax.set_title(r"blazed grating, $\lambda_{\mathrm{B}}$ = 500 nm (bars: usable range)", fontsize=10)
ax.legend(frameon=False, fontsize=9)

ax = axes[1]
d = 1e6 / 79.0                       # groove spacing in nm
lamB1 = 2 * d * np.sin(np.radians(63.4))
for m in range(36, 116):
    lc = lamB1 / m
    fsr = lc / m
    y = 1e5 / lc ** 1.0              # cross-dispersion grows towards short wavelengths
    x = np.linspace(-0.6, 0.6, 2)
    ax.plot(x, [y, y], color="0.5", lw=1.0, alpha=0.6)
    if m % 12 == 0:
        ax.text(0.66, y, f"m = {m}, {lc:.0f} nm", fontsize=7.5, va="center")
# a few element lines (nm): placed by their position in the order closest to blaze
for wl, lab in [(213.86, "Zn"), (228.80, "Cd"), (285.21, "Mg"), (324.75, "Cu"),
                (396.85, "Ca II"), (422.67, "Ca"), (589.00, "Na")]:
    m = int(round(lamB1 / wl))
    lc = lamB1 / m
    x = (wl - lc) / (lc / m)
    ax.plot(x, 1e5 / lc, "o", color="C3", ms=4)
    ax.text(x - 0.04, 1e5 / lc + 7, lab, fontsize=7.5, color="C3", ha="right")
ax.set_xlim(-0.8, 1.2)
ax.set_xlabel("position along order (units of free spectral range)")
ax.set_ylabel("cross-dispersion direction (arb.)")
ax.set_yticks([])
ax.set_title("echellogram: orders stacked by the cross-disperser", fontsize=10)
fig.tight_layout()
