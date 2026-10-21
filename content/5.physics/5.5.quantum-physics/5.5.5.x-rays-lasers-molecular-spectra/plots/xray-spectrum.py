"""X-ray tube spectrum of a molybdenum target (Kramers continuum plus K lines), and Moseley's plot of K-alpha lines."""

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.3))

# Left: continuum after Kramers, I(lambda) ~ (1/lambda_min - 1/lambda) / lambda^2, plus Mo K lines
lam = np.linspace(0.02, 0.12, 2000)  # nm
U_K = 20.0  # Mo K-shell binding energy in keV (excitation threshold of the K series)
lines = [(0.0709, 1.0), (0.0632, 0.22)]  # K-alpha, K-beta wavelengths in nm, relative strengths
for i, U in enumerate([15, 20, 25, 30]):
    lmin = 1.23984 / U  # nm, Duane-Hunt limit
    cont = np.where(lam > lmin, (1 / lmin - 1 / lam) / lam**2, 0.0) / 1e3
    spec = cont.copy()
    if U > U_K:
        strength = 6.0 * (U / U_K - 1) ** 1.5
        for l0, s in lines:
            spec += strength * s * np.exp(-0.5 * ((lam - l0) / 4e-4) ** 2)
    ax1.plot(lam, spec, color=f"C{i}", lw=1.5, label=f"U = {U} kV")
    ax1.plot([lmin], [0], marker="|", color=f"C{i}", ms=10)
ax1.text(0.0718, 3.75, r"K$_\alpha$", fontsize=9)
ax1.text(0.0640, 2.65, r"K$_\beta$", fontsize=9)
ax1.set_xlim(0.02, 0.12)
ax1.set_ylim(0, 4.3)
ax1.set_xlabel(r"$\lambda$ / nm")
ax1.set_ylabel("intensity (arb. units)")
ax1.set_title(r"Mo target: continuum with cutoff $\lambda_{\min} = hc/eU$")
ax1.legend(fontsize=8)

# Right: Moseley plot, sqrt(nu) of K-alpha1 lines against Z
data = {11: 1.041, 13: 1.487, 16: 2.308, 20: 3.692, 22: 4.511, 24: 5.415, 26: 6.404, 27: 6.930,
        28: 7.478, 29: 8.048, 30: 8.639, 32: 9.886, 40: 15.775, 42: 17.479, 47: 22.163,
        50: 25.271, 56: 32.194, 60: 37.36, 74: 59.318, 79: 68.804, 82: 74.969}
Z = np.array(sorted(data))
E = np.array([data[z] for z in Z])  # keV
sqrt_nu = np.sqrt(E * 1e3 * 1.602176634e-19 / 6.62607015e-34) / 1e8  # units of 1e8 Hz^(1/2)
zz = np.linspace(5, 90, 100)
ax2.plot(zz, 0.4967 * (zz - 1), "k--", lw=1.2, label=r"$\sqrt{\nu} = 0.497\times10^{8}\,(Z-1)$")
ax2.plot(Z, sqrt_nu, "o", color="C0", ms=5, label=r"measured K$_{\alpha 1}$")
for z, name in [(29, "Cu"), (42, "Mo"), (74, "W")]:
    ax2.annotate(name, (z, sqrt_nu[list(Z).index(z)]), textcoords="offset points", xytext=(-16, 6), fontsize=8)
ax2.set_xlim(5, 90)
ax2.set_ylim(0, 46)
ax2.set_xlabel("atomic number Z")
ax2.set_ylabel(r"$\sqrt{\nu}\ /\ (10^{8}\ \mathrm{Hz}^{1/2})$")
ax2.set_title("Moseley's law")
ax2.legend(fontsize=8, loc="upper left")

fig.tight_layout()
