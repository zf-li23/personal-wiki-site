"""Distribution fractions of acetic, carbonic and phosphoric acid as functions of pH (25 C, pKa values
from the CRC Handbook). delta_j is the fraction of the total acid present as the species that has
lost j protons."""

import numpy as np
import matplotlib.pyplot as plt

pH = np.linspace(0, 14, 600)
h = 10.0 ** -pH


def fractions(pKas):
    Ks = 10.0 ** -np.array(pKas)
    n = len(Ks)
    terms = [h ** (n - j) * np.prod(Ks[:j]) for j in range(n + 1)]
    total = sum(terms)
    return [t / total for t in terms]


systems = [
    ("acetic acid", [4.76], ["HAc", "Ac$^-$"]),
    ("carbonic acid", [6.35, 10.33], ["H$_2$CO$_3$", "HCO$_3^-$", "CO$_3^{2-}$"]),
    ("phosphoric acid", [2.16, 7.21, 12.32], ["H$_3$PO$_4$", "H$_2$PO$_4^-$", "HPO$_4^{2-}$", "PO$_4^{3-}$"]),
]

fig, axes = plt.subplots(1, 3, figsize=(12, 3.6), sharey=True)
for ax, (title, pKas, labels) in zip(axes, systems):
    for j, (d, lab) in enumerate(zip(fractions(pKas), labels)):
        ax.plot(pH, d, lw=1.8, color=f"C{j}", label=lab)
    for pk in pKas:
        ax.axvline(pk, color="0.6", lw=0.8, ls=":")
        ax.text(pk + 0.15, 0.93, f"p$K_a$ = {pk}", fontsize=8, rotation=90, va="top")
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("pH")
    ax.set_xlim(0, 14)
    where = (0.27, 0.06) if len(pKas) == 3 else "center right"
    ax.legend(frameon=False, fontsize=8, loc=where)
axes[0].set_ylabel(r"distribution fraction $\delta$")
fig.tight_layout()
