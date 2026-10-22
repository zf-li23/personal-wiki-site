"""Butler-Volmer kinetics at 25 C for O + e- = R (anodic current positive, eta = E - E_eq).
Left: net current j/j0 = exp(alpha_a f eta) - exp(-alpha_c f eta) with alpha_a = alpha_c = 0.5, its
anodic and cathodic partial currents, an asymmetric case (alpha_a = 0.3), and the same kinetics with
mass-transport limits j_L = +-20 j0 (bulk concentrations of O and R equal).
Right: Tafel plot lg|j/j0| against eta; at |eta| > ~0.12 V the branches become straight lines of
slope alpha F / (2.303 RT), i.e. 0.118 V per decade for alpha = 0.5."""

import numpy as np
import matplotlib.pyplot as plt

f = 96485.33212 / (8.314462618 * 298.15)      # F/RT in 1/V
eta = np.linspace(-0.25, 0.25, 801)
ja = np.exp(0.5 * f * eta)
jc = -np.exp(-0.5 * f * eta)

fig, axes = plt.subplots(1, 2, figsize=(10, 4.3))
ax = axes[0]
ax.plot(eta, ja + jc, color="k", lw=1.9, label=r"net, $\alpha_\mathrm{a} = \alpha_\mathrm{c} = 0.5$")
ax.plot(eta, ja, color="C3", lw=1.0, ls="--", label="anodic partial current")
ax.plot(eta, jc, color="C0", lw=1.0, ls="--", label="cathodic partial current")
ax.plot(eta, np.exp(0.3 * f * eta) - np.exp(-0.7 * f * eta), color="C2", lw=1.3, label=r"net, $\alpha_\mathrm{a} = 0.3$")
jl = 20.0
num = np.exp(0.5 * f * eta) - np.exp(-0.5 * f * eta)
den = 1 + np.exp(0.5 * f * eta) / jl + np.exp(-0.5 * f * eta) / jl
ax.plot(eta, num / den, color="C4", lw=1.3, ls="-.", label=r"with transport, $|j_\mathrm{L}| = 20 j_0$")
ax.axhline(0, color="0.6", lw=0.6)
ax.axvline(0, color="0.6", lw=0.6)
ax.set_xlim(-0.25, 0.25)
ax.set_ylim(-40, 40)
ax.set_xlabel(r"$\eta$ / V")
ax.set_ylabel(r"$j/j_0$")
ax.legend(frameon=False, fontsize=8, loc="upper left")

ax = axes[1]
ax.plot(eta, np.log10(np.abs(ja + jc) + 1e-12), color="k", lw=1.9)
tafel = eta > 0.03
ax.plot(eta[tafel], 0.5 * f * eta[tafel] / np.log(10), color="C3", lw=1.0, ls="--")
tafel = eta < -0.03
ax.plot(eta[tafel], -0.5 * f * eta[tafel] / np.log(10), color="C0", lw=1.0, ls="--")
ax.text(0.13, 0.6, "anodic Tafel line\nslope 1/(0.118 V)", fontsize=8.5, color="C3")
ax.text(-0.245, 0.6, "cathodic Tafel line", fontsize=8.5, color="C0")
ax.text(-0.06, -1.6, "linear region\n" + r"$j \approx j_0 F\eta/RT$", fontsize=8.5)
ax.set_xlim(-0.25, 0.25)
ax.set_ylim(-2, 2.4)
ax.set_xlabel(r"$\eta$ / V")
ax.set_ylabel(r"$\lg\,|j/j_0|$")
fig.tight_layout()
