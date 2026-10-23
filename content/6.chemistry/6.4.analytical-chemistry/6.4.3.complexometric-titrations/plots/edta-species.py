"""Distribution fractions of the seven EDTA species H6Y2+ ... Y4- as functions of pH
(25 C, I = 0.1 mol/L; pKa1..pKa6 = 0.0, 1.5, 2.00, 2.69, 6.13, 10.37)."""

import numpy as np
import matplotlib.pyplot as plt

pKa = [0.0, 1.5, 2.00, 2.69, 6.13, 10.37]
pH = np.linspace(0, 14, 700)
h = 10.0 ** -pH
Ks = 10.0 ** -np.array(pKa)
n = len(Ks)
terms = [h ** (n - j) * np.prod(Ks[:j]) for j in range(n + 1)]
total = sum(terms)
labels = ["H$_6$Y$^{2+}$", "H$_5$Y$^{+}$", "H$_4$Y", "H$_3$Y$^{-}$", "H$_2$Y$^{2-}$", "HY$^{3-}$", "Y$^{4-}$"]

fig, ax = plt.subplots(figsize=(6.8, 4))
for j, (t, lab) in enumerate(zip(terms, labels)):
    d = t / total
    ax.plot(pH, d, lw=1.8, color=f"C{j}")
    k = np.argmax(d)
    x = min(max(pH[k], 0.6), 13.0)
    ax.text(x, d[np.searchsorted(pH, x)] + 0.03, lab, ha="center", fontsize=8, color=f"C{j}")
ax.set_xlabel("pH")
ax.set_ylabel(r"distribution fraction $\delta$")
ax.set_xlim(0, 14)
ax.set_ylim(0, 1.1)
fig.tight_layout()
