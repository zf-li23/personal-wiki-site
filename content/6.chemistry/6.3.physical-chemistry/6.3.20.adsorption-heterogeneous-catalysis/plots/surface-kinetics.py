"""Rates of gas-solid catalytic reactions when the surface step is rate-determining and
adsorption follows Langmuir's isotherm. Left: unimolecular A -> B, r = k a p / (1 + a p), first
order at low pressure and zero order at high pressure. Right: bimolecular A + B at fixed p_B
against p_A: the Langmuir-Hinshelwood rate k a_A a_B p_A p_B / (1 + a_A p_A + a_B p_B)^2 passes
through a maximum, the Eley-Rideal rate k a_A p_A p_B / (1 + a_A p_A + a_B p_B) saturates."""

import numpy as np
import matplotlib.pyplot as plt

p = np.linspace(0, 10, 500)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.6, 3.6))
a = 1.0
ax1.plot(p, a * p / (1 + a * p), color="C0", lw=1.8, label=r"$r/k = ap/(1+ap)$")
ax1.plot(p[p < 1.2], a * p[p < 1.2], color="C1", lw=1, ls=":", label="first order")
ax1.axhline(1, color="C3", lw=1, ls=":", label="zero order")
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 1.1)
ax1.set_xlabel(r"$p_\mathrm{A}$ (units of $1/a$)")
ax1.set_ylabel(r"$r/k$")
ax1.legend(frameon=False, fontsize=8, loc="lower right")

aA, aB, pB = 1.0, 1.0, 1.0
lh = aA * aB * p * pB / (1 + aA * p + aB * pB) ** 2
er = aA * p * pB / (1 + aA * p + aB * pB)
ax2.plot(p, lh / lh.max(), color="C0", lw=1.8, label="Langmuir-Hinshelwood")
ax2.plot(p, er / er.max(), color="C3", lw=1.8, label="Eley-Rideal")
pmax = (1 + aB * pB) / aA
ax2.axvline(pmax, color="0.6", lw=0.8, ls="--")
ax2.text(pmax + 0.15, 0.08, r"$a_\mathrm{A}p_\mathrm{A} = 1 + a_\mathrm{B}p_\mathrm{B}$", fontsize=8)
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 1.08)
ax2.set_xlabel(r"$p_\mathrm{A}$ (fixed $p_\mathrm{B}$)")
ax2.set_ylabel("rate (normalized)")
ax2.legend(frameon=False, fontsize=8, loc="center right")
fig.tight_layout()
