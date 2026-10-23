"""Response of a pH glass electrode at 25 C.
Ideal Nernstian response E = K - S pH (S = 59.16 mV) compared with the Nikolsky-Eisenman
equation E = K + S lg(a_H + K_HNa a_Na) for K_HNa = 1e-12 at three sodium activities
(alkaline or sodium error). The acid error below pH ~ 1 is drawn schematically
(apparent pH higher than the true pH)."""

import numpy as np
import matplotlib.pyplot as plt

S = 59.16  # mV per decade
K_el = 400.0
K_HNa = 1e-12
pH = np.linspace(-1, 14, 600)
aH = 10.0 ** (-pH)

fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.2))
ax = axes[0]
ax.plot(pH, K_el - S * pH, color="k", lw=1.2, ls="--", label="ideal Nernst response")
for aNa, col in [(0.01, "C0"), (0.1, "C1"), (1.0, "C3")]:
    E = K_el + S * np.log10(aH + K_HNa * aNa)
    m = pH > 2
    ax.plot(pH[m], E[m], color=col, lw=1.7, label=rf"$a(\mathrm{{Na^+}})$ = {aNa:g}")
# schematic acid error: apparent pH exceeds true pH in very strong acid
delta = 0.35 * np.log1p(np.exp(-(pH - 0.6) / 0.35))
m = pH < 2.5
ax.plot(pH[m], K_el - S * (pH[m] + delta[m]), color="C2", lw=1.7, label="acid error (schematic)")
ax.set_xlim(-1, 14)
ax.set_xlabel("true pH")
ax.set_ylabel(r"$E$ / mV")
ax.legend(frameon=False, fontsize=8.5, loc="lower left")
ax.set_title(r"Nikolsky-Eisenman, $K^{\mathrm{pot}}_{\mathrm{H,Na}} = 10^{-12}$", fontsize=10)

ax = axes[1]
for aNa, col in [(0.01, "C0"), (0.1, "C1"), (1.0, "C3")]:
    app = -np.log10(aH + K_HNa * aNa)
    m = pH > 7
    ax.plot(pH[m], app[m] - pH[m], color=col, lw=1.7, label=rf"$a(\mathrm{{Na^+}})$ = {aNa:g}")
ax.axhline(0, color="0.6", lw=0.6)
ax.set_xlim(7, 14)
ax.set_xlabel("true pH")
ax.set_ylabel(r"pH$_{\mathrm{measured}}$ - pH$_{\mathrm{true}}$")
ax.set_title("alkaline (sodium) error is negative", fontsize=10)
ax.legend(frameon=False, fontsize=9, loc="lower left")
fig.tight_layout()
