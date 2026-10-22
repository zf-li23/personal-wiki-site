"""Hard-sphere collision theory. Left: reaction cross section sigma_r(eps) = pi d^2 (1 - eps_c/eps)
for eps > eps_c. Right: flux-weighted Maxwell-Boltzmann distribution of the relative kinetic
energy, eps exp(-eps/kT), and its product with sigma_r, whose integral gives k(T)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

x = np.linspace(0, 12, 600)          # eps / kT
xc = 4.0                             # eps_c / kT
sig = np.where(x > xc, 1 - xc / np.maximum(x, 1e-12), 0.0)

fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
axs[0].plot(x / xc, sig, color="C0")
axs[0].axvline(1, color="0.6", ls=":", lw=1)
axs[0].set_xlim(0, 3)
axs[0].set_xlabel(r"$\varepsilon/\varepsilon_{\mathrm{c}}$")
axs[0].set_ylabel(r"$\sigma_{\mathrm{r}}/(\pi d_{\mathrm{AB}}^2)$")
axs[0].set_title("reaction cross section", fontsize=10)

flux = x * np.exp(-x)
react = flux * sig
axs[1].plot(x, flux, color="C0", label=r"$\varepsilon\,\mathrm{e}^{-\varepsilon/k_{\mathrm{B}}T}$ (collision flux)")
axs[1].fill_between(x, react, color="C3", alpha=0.35, lw=0)
axs[1].plot(x, react, color="C3", label=r"$\times\,\sigma_{\mathrm{r}}/(\pi d^2)$ (reactive)")
axs[1].axvline(xc, color="0.6", ls=":", lw=1)
num = quad(lambda u: u * np.exp(-u) * (1 - xc / u), xc, np.inf)[0]
axs[1].set_title(rf"$\varepsilon_{{\mathrm{{c}}}} = 4k_{{\mathrm{{B}}}}T$: reactive fraction {num:.4f} = $\mathrm{{e}}^{{-4}}$", fontsize=10)
axs[1].set_xlabel(r"$\varepsilon/k_{\mathrm{B}}T$")
axs[1].set_ylabel("weight (arb. units)")
axs[1].legend(frameon=False, fontsize=8)
fig.tight_layout()
