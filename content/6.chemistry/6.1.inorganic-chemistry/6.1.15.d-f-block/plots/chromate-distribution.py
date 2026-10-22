"""Distribution of Cr(VI) among CrO4^2-, HCrO4^- and Cr2O7^2- against pH, as fractions of the total chromium
(each dichromate ion counts twice). Constants: pKa(HCrO4-) = 6.5 and 2 HCrO4- <=> Cr2O7^2- + H2O, K_D = 12,
so that 2 CrO4^2- + 2 H+ <=> Cr2O7^2- + H2O has K = 1.2e14; ideal solution, H2CrO4 neglected.
Solid lines: total Cr 0.10 mol/L; dashed: 1.0e-3 mol/L."""

import numpy as np
import matplotlib.pyplot as plt

Ka, KD = 10 ** -6.5, 12.0
pH = np.linspace(0, 10, 400)
fig, ax = plt.subplots(figsize=(7.5, 4.6))
for ct, ls in [(0.10, "-"), (1e-3, "--")]:
    h = 10 ** -pH
    a = 2 * KD                      # [HCrO4-] = y solves y + (Ka/h) y + 2 KD y^2 = ct
    b = 1 + Ka / h
    y = (-b + np.sqrt(b * b + 4 * a * ct)) / (2 * a)
    f_h = y / ct
    f_c = (Ka / h) * y / ct
    f_d = 2 * KD * y * y / ct
    ax.plot(pH, f_c, ls=ls, color="C1", label=r"CrO$_4^{2-}$" if ls == "-" else None)
    ax.plot(pH, f_h, ls=ls, color="C2", label=r"HCrO$_4^-$" if ls == "-" else None)
    ax.plot(pH, f_d, ls=ls, color="C3", label=r"Cr$_2$O$_7^{2-}$ (as 2 Cr)" if ls == "-" else None)
ax.plot([], [], "k-", label="total Cr 0.10 mol L$^{-1}$")
ax.plot([], [], "k--", label="total Cr 0.0010 mol L$^{-1}$")
ax.set_xlabel("pH")
ax.set_ylabel("fraction of Cr(VI)")
ax.set_ylim(0, 1.02)
ax.legend(frameon=False, fontsize=8, loc="center right")
fig.tight_layout()
