"""Average net charge of five amino acids as a function of pH, from their pKa values
(25 C, values used in the text): every ionizable group contributes +1/(1 + 10^(pH - pKa))
if it is a base's conjugate acid (alpha-NH3+, Lys, Arg, His side chains) and
-1/(1 + 10^(pKa - pH)) if it is an acid (alpha-COOH, Asp side chain). The isoelectric point
is where the curve crosses zero; the shaded band marks physiological pH."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

AA = {  # name: (acid pKa list, base (conjugate acid) pKa list)
    "Gly": ([2.34], [9.60]),
    "Asp": ([1.99, 3.90], [9.90]),
    "His": ([1.82], [9.17, 6.00]),
    "Lys": ([2.16], [9.06, 10.54]),
    "Arg": ([2.17], [9.04, 12.48]),
}
COLOURS = ["#6b7280", "#dc2626", "#d97706", "#2563eb", "#7c3aed"]


def charge(ph, acids, bases):
    return sum(1 / (1 + 10 ** (ph - p)) for p in bases) - sum(1 / (1 + 10 ** (p - ph)) for p in acids)


ph = np.linspace(0, 14, 600)
fig, ax = plt.subplots(figsize=(7.5, 4.2))
ax.axvspan(7.0, 7.8, color="#16a34a", alpha=0.12, lw=0)
ax.axhline(0, color="0.5", lw=0.8)
for (name, (a, b)), c in zip(AA.items(), COLOURS):
    ax.plot(ph, [charge(x, a, b) for x in ph], color=c, lw=2, label=name)
    pi = brentq(lambda x: charge(x, a, b), 0, 14)
    ax.plot([pi], [0], "o", color=c, ms=5)
    ax.annotate(f"pI {pi:.2f}", (pi, 0), xytext=(0, 10 if name in ("Gly", "Lys") else -16), textcoords="offset points",
                ha="center", fontsize=8, color=c)
ax.set_xlabel("pH")
ax.set_ylabel("average net charge")
ax.set_xlim(0, 14)
ax.set_ylim(-2.1, 2.1)
ax.legend(frameon=False, ncol=5, loc="upper right", fontsize=9)
