"""Free-electron density of states and its occupation at T = 0 and at a finite temperature."""

import numpy as np
import matplotlib.pyplot as plt

E = np.linspace(0, 1.6, 1200)  # in units of E_F
g = np.sqrt(E)  # g(E) ~ E^(1/2), normalized so that g(E_F) = 1
t = 0.06  # k_B T / E_F, exaggerated for visibility (a metal at room temperature has about 0.004)
f = 1 / (np.exp((E - 1) / t) + 1)

fig, ax = plt.subplots(figsize=(7.5, 4.3))
ax.plot(E, g, color="k", lw=1.5, label=r"$g(E) \propto \sqrt{E}$")
ax.fill_between(E, 0, np.where(E <= 1, g, 0), color="C0", alpha=0.3, label="occupied at T = 0")
ax.plot(E, g * f, color="C3", lw=1.8, label=rf"$g(E)\,\bar N(E)$, $k_{{\mathrm{{B}}}}T = {t:g}\,E_{{\mathrm{{F}}}}$")
ax.axvline(1, color="0.5", ls=":", lw=1)
ax.text(1.01, 1.22, r"$E_{\mathrm{F}}$", fontsize=10)
ax.annotate("", xy=(1 - 2 * t, 0.2), xytext=(1 + 2 * t, 0.2), arrowprops=dict(arrowstyle="<->", lw=1))
ax.text(1 + 2.3 * t, 0.18, r"$\sim 4k_{\mathrm{B}}T$", fontsize=9)
ax.set_xlim(0, 1.6)
ax.set_ylim(0, 1.35)
ax.set_xlabel(r"$E\,/\,E_{\mathrm{F}}$")
ax.set_ylabel(r"states per unit energy, $g\,/\,g(E_{\mathrm{F}})$")
ax.set_title("Free electron gas")
ax.legend(fontsize=8, loc="upper left")
fig.tight_layout()
