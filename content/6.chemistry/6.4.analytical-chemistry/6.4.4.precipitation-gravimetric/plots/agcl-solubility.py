"""Solubility of AgCl in chloride solutions: common-ion effect at low [Cl-], complexation (AgCl(aq),
AgCl2-, AgCl3 2-, AgCl4 3-) at high [Cl-]. Ksp = 1.77e-10; lg beta1..4 = 3.04, 5.04, 5.04, 5.30."""

import numpy as np
import matplotlib.pyplot as plt

Ksp = 1.77e-10
lgb = [3.04, 5.04, 5.04, 5.30]
pCl = np.linspace(0, 6, 600)
Cl = 10.0 ** -pCl
terms = [Ksp / Cl] + [Ksp * 10 ** b * Cl ** i for i, b in enumerate(lgb)]
labels = ["Ag$^+$", "AgCl(aq)", "AgCl$_2^-$", "AgCl$_3^{2-}$", "AgCl$_4^{3-}$"]
s = sum(terms)

fig, ax = plt.subplots(figsize=(6.4, 4))
ax.semilogy(pCl, s, color="k", lw=2.0, label="total solubility $s$")
for i, (t, lab) in enumerate(zip(terms, labels)):
    ax.semilogy(pCl, t, color=f"C{i}", lw=1.0, ls="--", label=lab)
k = np.argmin(s)
ax.plot(pCl[k], s[k], "o", color="C3")
ax.annotate(f"minimum at pCl = {pCl[k]:.1f}", (pCl[k], s[k]), xytext=(8, 8), textcoords="offset points", fontsize=8)
ax.set_xlabel("pCl")
ax.set_ylabel(r"concentration / (mol L$^{-1}$)")
ax.set_xlim(6, 0)
ax.set_ylim(1e-9, 1e-3)
ax.legend(frameon=False, fontsize=8, loc="upper center", ncol=2)
fig.tight_layout()
