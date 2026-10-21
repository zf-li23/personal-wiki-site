"""Fermi-Dirac distribution at several temperatures, and the three occupation laws compared."""

import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 4.2))

E = np.linspace(0, 2, 1000)  # in units of E_F; take mu = E_F for simplicity
ax1.plot([0, 1, 1, 2], [1, 1, 0, 0], color="k", lw=1.5, label="T = 0")
for i, t in enumerate([0.02, 0.1, 0.3]):
    ax1.plot(E, 1 / (np.exp((E - 1) / t) + 1), color=f"C{i}", lw=1.6, label=rf"$k_{{\mathrm{{B}}}}T = {t:g}\,E_{{\mathrm{{F}}}}$")
ax1.set_xlabel(r"$E\,/\,E_{\mathrm{F}}$")
ax1.set_ylabel(r"$\bar N(E)$")
ax1.set_ylim(0, 1.08)
ax1.set_xlim(0, 2)
ax1.set_title(r"Fermi-Dirac distribution ($\mu \approx E_{\mathrm{F}}$)")
ax1.legend(fontsize=8)

x = np.linspace(-3, 5, 1000)  # (E - mu) / kT
xb = x[x > 0.05]
ax2.plot(x, 1 / (np.exp(x) + 1), color="C0", lw=1.7, label="Fermi-Dirac")
ax2.plot(xb, 1 / (np.exp(xb) - 1), color="C1", lw=1.7, label="Bose-Einstein")
ax2.plot(x, np.exp(-x), color="k", ls="--", lw=1.2, label="Maxwell-Boltzmann")
ax2.set_yscale("log")
ax2.set_ylim(5e-3, 20)
ax2.set_xlim(-3, 5)
ax2.set_xlabel(r"$(E - \mu)\,/\,k_{\mathrm{B}}T$")
ax2.set_ylabel(r"$\bar N(E)$")
ax2.set_title(r"The three laws coincide for $E - \mu \gg k_{\mathrm{B}}T$")
ax2.legend(fontsize=8)

fig.tight_layout()
