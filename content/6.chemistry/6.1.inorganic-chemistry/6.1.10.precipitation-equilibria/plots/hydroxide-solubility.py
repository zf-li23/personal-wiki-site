"""lg[M n+] against pH for saturated solutions of metal hydroxides, lg[M] = lg Ksp + n pKw - n pH
(Ksp at 25 C, CRC Handbook; Al(OH)3 from a common textbook table). Al(OH)3 also dissolves in base as
Al(OH)4-: Al(OH)3(s) + OH- <=> Al(OH)4-, K = Ksp * beta4 = 1.3."""

import numpy as np
import matplotlib.pyplot as plt

pKw = 14.0
data = [("Fe(OH)$_3$", 2.79e-39, 3), ("Al(OH)$_3$", 1.3e-33, 3), ("Cu(OH)$_2$", 2.2e-20, 2),
        ("Fe(OH)$_2$", 4.87e-17, 2), ("Mn(OH)$_2$", 2.06e-13, 2), ("Mg(OH)$_2$", 5.61e-12, 2)]
pH = np.linspace(0, 14, 400)

fig, ax = plt.subplots(figsize=(7, 4.4))
for i, (name, K, n) in enumerate(data):
    lgM = np.log10(K) + n * pKw - n * pH
    m = lgM < 1.5
    ax.plot(pH[m], lgM[m], color=f"C{i}", lw=1.8, label=name)
# amphoteric branch of Al(OH)3: lg[Al(OH)4-] = lg K + pH - pKw
lgAl4 = np.log10(1.3) + pH - pKw
ax.plot(pH[lgAl4 > -9], lgAl4[lgAl4 > -9], color="C1", lw=1.8, ls="--")
ax.text(11.2, -3.8, r"Al(OH)$_4^-$", color="C1", fontsize=9)
ax.axhline(-2, color="0.6", lw=0.8, ls=":")
ax.axhline(-5, color="0.6", lw=0.8, ls=":")
ax.text(0.1, -1.85, "0.010 M: precipitation begins", fontsize=8)
ax.text(0.1, -4.85, r"$10^{-5}$ M: precipitation complete", fontsize=8)
ax.set_xlim(0, 14)
ax.set_ylim(-9, 1.5)
ax.set_xlabel("pH")
ax.set_ylabel(r"$\lg[\mathrm{M}^{n+}]$")
ax.legend(frameon=False, fontsize=8, loc="upper right")
fig.tight_layout()
