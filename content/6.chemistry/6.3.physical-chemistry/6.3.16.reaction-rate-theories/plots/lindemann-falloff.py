"""Lindemann mechanism: k_uni/k_inf = 1/(1 + p_half/p) (fall-off curve) and the linear
Lindemann plot 1/k_uni = 1/k_inf + 1/(k1 [M]) in reduced units."""

import numpy as np
import matplotlib.pyplot as plt

x = np.logspace(-3, 3, 400)          # p / p_half
fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
axs[0].semilogx(x, 1 / (1 + 1 / x), color="C0", label="Lindemann")
axs[0].semilogx(x, x, color="C1", ls="--", label=r"low pressure: $k_{\mathrm{uni}} = k_1[\mathrm{M}]$ (second order)")
axs[0].axhline(1, color="C2", ls=":", label=r"high pressure: $k_\infty$ (first order)")
axs[0].plot([1], [0.5], "o", color="C0", ms=4)
axs[0].annotate(r"$p_{1/2}$", (1, 0.5), (3, 0.4), fontsize=9, arrowprops=dict(arrowstyle="-", lw=0.6))
axs[0].set_ylim(0, 1.45)
axs[0].set_xlabel(r"$p/p_{1/2}$")
axs[0].set_ylabel(r"$k_{\mathrm{uni}}/k_\infty$")
axs[0].set_title("fall-off curve", fontsize=10)
axs[0].legend(frameon=False, fontsize=7, loc="upper left")

inv = np.linspace(0.05, 5, 100)      # p_half / p
axs[1].plot(inv, 1 + inv, color="C0")
axs[1].set_xlabel(r"$p_{1/2}/p$  ($\propto 1/[\mathrm{M}]$)")
axs[1].set_ylabel(r"$k_\infty/k_{\mathrm{uni}}$")
axs[1].text(0.3, 4.6, r"intercept $1/k_\infty$, slope $1/k_1$", fontsize=9)
axs[1].set_title("Lindemann plot", fontsize=10)
fig.tight_layout()
