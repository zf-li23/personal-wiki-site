"""Lomakin-Scheibe calibration I = a c^b on logarithmic axes. Simulated line intensities
follow I = a c (1 + c/c_s)^(-1/2): at low concentration b = 1; at high concentration
self-absorption lowers the slope towards b = 1/2. Points carry 3 % random scatter;
the line is a least-squares fit of lg I against lg c over the linear part."""

import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
a, cs = 1.0e3, 100.0
c = np.logspace(-2, 4, 25)            # concentration, ug/mL
I_true = a * c / np.sqrt(1 + c / cs)
I = I_true * (1 + 0.03 * rng.standard_normal(c.size))

fig, ax = plt.subplots(figsize=(6.8, 4.6))
ax.loglog(c, I, "o", color="C0", ms=4.5, label="measured")
m = c < 10
b, lga = np.polyfit(np.log10(c[m]), np.log10(I[m]), 1)
cc = np.logspace(-2, 4, 100)
ax.loglog(cc, 10 ** lga * cc ** b, color="k", lw=1, ls="--", label=f"fit below 10 $\\mu$g/mL: b = {b:.2f}")
ax.loglog(cc, a * np.sqrt(cs) * cc ** 0.5, color="C3", lw=1, ls=":", label="slope b = 0.5 (strong self-absorption)")
ax.set_xlabel(r"$c$ / ($\mu$g mL$^{-1}$)")
ax.set_ylabel(r"line intensity $I$ (arb.)")
ax.set_ylim(5, 3e6)
ax.legend(frameon=False, fontsize=9, loc="upper left")
fig.tight_layout()
