"""Exchange between two equally populated sites, as for the axial and equatorial protons of
cyclohexane during ring flipping. Lineshapes from the Bloch-McConnell equations for a chemical
shift difference of 192 Hz (0.48 ppm at 400 MHz) and a natural linewidth of 1 Hz. Slow exchange
gives two lines, coalescence occurs at k = pi * dnu / sqrt(2) = 426 s^-1, and fast exchange gives
one line at the average shift. Right: rate constant from the Eyring equation for
dG = 45 kJ/mol, with the coalescence rate at 400 MHz marked."""

import numpy as np
import matplotlib.pyplot as plt

dnu = 192.0
nu = np.linspace(-260, 260, 4000)
R2 = np.pi * 1.0  # natural linewidth 1 Hz


def lineshape(k):
    out = []
    p = np.array([0.5, 0.5])
    for v in nu:
        w = 2 * np.pi * v
        wa, wb = 2 * np.pi * dnu / 2, -2 * np.pi * dnu / 2
        m = np.array([[1j * (w - wa) + R2 + k, -k], [-k, 1j * (w - wb) + R2 + k]])
        out.append(np.real(np.ones(2) @ np.linalg.solve(m, p)))
    return np.array(out)


kc = np.pi * dnu / np.sqrt(2)
fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 4.2), gridspec_kw={"width_ratios": [1.3, 1]})
for i, k in enumerate([10, 150, kc, 1500, 2e4]):
    y = lineshape(k)
    ax.plot(nu, y / y.max() * 0.85 + i, color="C0" if k != kc else "C3", lw=1.2)
    ax.text(250, i + 0.3, f"k = {k:.0f} s$^{{-1}}$", ha="right", fontsize=9)
ax.set_yticks([])
ax.set_xlabel("frequency from the average shift / Hz")
ax.set_title("two-site exchange (red: coalescence)", fontsize=10)

kB, h, R = 1.380649e-23, 6.62607015e-34, 8.314462618
T = np.linspace(170, 300, 400)
k = kB * T / h * np.exp(-45000 / (R * T))
bx.semilogy(T - 273.15, k, color="C0", lw=1.6)
bx.axhline(kc, color="C3", lw=1, ls="--")
Tc = T[np.argmin(np.abs(k - kc))]
bx.plot(Tc - 273.15, kc, "o", color="C3")
bx.text(Tc - 273.15 + 3, kc / 3, f"$T_c$ = {Tc - 273.15:.0f} °C", fontsize=9, color="C3")
bx.set_xlabel(r"$t$ / °C")
bx.set_ylabel(r"$k$ / s$^{-1}$")
bx.set_title(r"Eyring, $\Delta G^\ddagger$ = 45 kJ mol$^{-1}$", fontsize=10)
fig.tight_layout()
