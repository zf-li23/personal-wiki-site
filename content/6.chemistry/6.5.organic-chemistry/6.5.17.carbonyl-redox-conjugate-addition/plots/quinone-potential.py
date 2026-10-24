"""Formal potential of the p-benzoquinone/hydroquinone couple against pH at 25 C, for equal total
concentrations of the oxidised form and the reduced form (all protonation states). With
Q + 2H+ + 2e- = H2Q (E0 = 0.699 V) and the acid dissociation constants of hydroquinone (pKa1 9.9,
pKa2 11.4), E = E0 + (0.05916/2) log10([H+]^2 + Ka1[H+] + Ka1 Ka2): the slope is -59 mV per pH
unit below pKa1, -30 mV between the two pKa values and zero above pKa2."""

import matplotlib.pyplot as plt
import numpy as np

E0, k = 0.699, 0.05916
ka1, ka2 = 10 ** -9.9, 10 ** -11.4
pH = np.linspace(0, 14, 400)
h = 10 ** -pH
E = E0 + k / 2 * np.log10(h ** 2 + ka1 * h + ka1 * ka2)

fig, ax = plt.subplots(figsize=(6.0, 3.8))
ax.plot(pH, E, lw=2.2, color="C0")
for p in (9.9, 11.4):
    ax.axvline(p, ls=":", lw=1, color="0.5")
ax.text(9.9, 0.62, r"p$K_{\mathrm{a1}}$", ha="right", va="center", fontsize=10)
ax.text(11.4, 0.62, r"p$K_{\mathrm{a2}}$", ha="left", va="center", fontsize=10)
ax.text(4.0, 0.52, "slope $-59$ mV/pH", fontsize=10)
ax.text(10.65, 0.18, "$-30$", ha="center", fontsize=10)
ax.text(12.8, 0.03, "0", ha="center", fontsize=10)
ax.annotate("Q + 2H$^+$ + 2e$^-$ = H$_2$Q", (1.0, E0 - k * 1.0), xytext=(1.5, 0.75), fontsize=10,
            arrowprops=dict(arrowstyle="-", lw=0.8))
ax.set_xlabel("pH")
ax.set_ylabel(r"$E^{\circ\prime}$ / V (vs SHE)")
ax.set_xlim(0, 14)
ax.set_ylim(-0.1, 0.8)
fig.tight_layout()
