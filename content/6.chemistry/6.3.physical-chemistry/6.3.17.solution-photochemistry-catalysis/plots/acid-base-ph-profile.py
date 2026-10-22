"""pH-rate profile of a specific acid-base catalysed reaction, k = k0 + kH[H+] + kOH[OH-]
(illustrative constants close to ester hydrolysis at 25 C), with Kw = 1.0e-14."""

import numpy as np
import matplotlib.pyplot as plt

kH, kOH, k0, Kw = 1.1e-4, 0.11, 1.0e-10, 1.0e-14   # L/(mol s), L/(mol s), 1/s
pH = np.linspace(0, 14, 400)
H = 10.0 ** -pH
k = k0 + kH * H + kOH * Kw / H
pHmin = -np.log10(np.sqrt(kOH * Kw / kH))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(pH, np.log10(k), color="C0", label="total")
ax.plot(pH, np.log10(kH * H), color="C3", ls="--", label=r"$k_{\mathrm{H^+}}[\mathrm{H^+}]$ (slope $-1$)")
ax.plot(pH, np.log10(kOH * Kw / H), color="C2", ls="--", label=r"$k_{\mathrm{OH^-}}[\mathrm{OH^-}]$ (slope $+1$)")
ax.axhline(np.log10(k0), color="C1", ls=":", label=r"$k_0$")
ax.axvline(pHmin, color="0.6", ls=":", lw=1)
ax.text(pHmin + 0.2, -11.5, rf"pH$_{{\min}}$ = {pHmin:.1f}", fontsize=8)
ax.set_ylim(-12, 2)
ax.set_xlabel("pH")
ax.set_ylabel(r"$\lg(k/\mathrm{s^{-1}})$")
ax.legend(frameon=False, fontsize=8, loc="upper center")
fig.tight_layout()
