"""Spectrophotometric pKa of p-nitrophenol (pKa = 7.15). Left: simulated spectra of a
fixed total concentration at different pH, built from Gaussian bands of the acid
(317 nm) and the phenolate (400 nm); all curves cross at the isosbestic point.
Right: absorbance at 400 nm against pH (2 % noise) fitted with
A = (A_HB + A_B 10^(pH - pKa)) / (1 + 10^(pH - pKa)) by scipy.optimize.curve_fit."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

lam = np.linspace(250, 500, 501)
c, pKa = 5.0e-5, 7.15
def band(l0, eps, w):
    return eps * np.exp(-0.5 * ((lam - l0) / w) ** 2)
eps_HB = band(317, 1.0e4, 22) + band(225, 6.0e3, 15)
eps_B = band(400, 1.8e4, 30) + band(228, 8.0e3, 15)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.6, 4.0))
pHs = np.arange(5.0, 9.6, 0.5)
cmap = plt.get_cmap("viridis")
for i, pH in enumerate(pHs):
    aB = 1 / (1 + 10 ** (pKa - pH))
    A = c * ((1 - aB) * eps_HB + aB * eps_B)
    ax1.plot(lam, A, color=cmap(i / (len(pHs) - 1)), lw=1.1, label=f"pH {pH:.1f}" if i % 2 == 0 else None)
d = eps_B - eps_HB
idx = np.where((lam > 330) & (lam < 380))[0]
iso = idx[np.argmin(np.abs(d[idx]))]
ax1.plot(lam[iso], c * eps_HB[iso], "o", mfc="none", mec="C3", ms=8)
ax1.annotate(f"isosbestic point\n{lam[iso]:.0f} nm", (lam[iso], c * eps_HB[iso]),
             (380, 0.62), fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.7))
ax1.set_xlabel(r"$\lambda$ / nm")
ax1.set_ylabel(r"absorbance $A$ ($b$ = 1 cm)")
ax1.legend(frameon=False, fontsize=7)

def model(pH, AHB, AB, pK):
    r = 10 ** (pH - pK)
    return (AHB + AB * r) / (1 + r)
rng = np.random.default_rng(0)
pHd = np.linspace(4.5, 10, 16)
i400 = np.argmin(np.abs(lam - 400))
Ad = model(pHd, c * eps_HB[i400], c * eps_B[i400], pKa) * (1 + 0.02 * rng.standard_normal(pHd.size))
p, cov = curve_fit(model, pHd, Ad, p0=[0.0, 1.0, 7.0])
pp = np.linspace(4.5, 10, 200)
ax2.plot(pHd, Ad, "o", color="C0", ms=4, label="measured at 400 nm")
ax2.plot(pp, model(pp, *p), color="k", lw=1, label=rf"fit: p$K_a$ = {p[2]:.2f} $\pm$ {np.sqrt(cov[2, 2]):.2f}")
ax2.axvline(p[2], color="0.5", lw=0.8, ls=":")
ax2.set_xlabel("pH")
ax2.set_ylabel(r"$A_{400}$")
ax2.legend(frameon=False, fontsize=8, loc="upper left")
fig.tight_layout()
