"""20.00 mL of 0.1000 mol/L H3PO4 titrated with 0.1000 mol/L NaOH (pKa 2.16, 7.21, 12.32, CRC).
Top: pH from the exact charge balance, solved in the variable pH with brentq; the two
stoichiometric points (NaH2PO4 and Na2HPO4) and the transition ranges of methyl orange and
phenolphthalein. Bottom: distribution fractions of the four species along the same titration."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

Kw = 1.0e-14
Ka = 10.0 ** -np.array([2.16, 7.21, 12.32])
c0, V0, cb = 0.1000, 20.00, 0.1000


def fractions(h):
    terms = np.array([h ** 3, h ** 2 * Ka[0], h * Ka[0] * Ka[1], Ka[0] * Ka[1] * Ka[2]])
    return terms / terms.sum()


def pH(v):
    ct, na = c0 * V0 / (V0 + v), cb * v / (V0 + v)
    def f(p):
        h = 10.0 ** -p
        d = fractions(h)
        return h + na - Kw / h - ct * (d[1] + 2 * d[2] + 3 * d[3])
    return brentq(f, -1.0, 15.0, xtol=1e-10)


v = np.linspace(0, 70, 700)
p = np.array([pH(x) for x in v])
a = v * cb / (V0 * c0)                       # titration fraction (equivalents of NaOH)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.5, 6.6), sharex=True, gridspec_kw={"height_ratios": [3, 2]})
ax1.plot(a, p, color="C0", lw=1.8)
for lo, hi, col, name in [(3.1, 4.4, "C1", "methyl orange"), (8.2, 10.0, "C3", "phenolphthalein")]:
    ax1.axhspan(lo, hi, xmin=0, xmax=0.07, color=col, alpha=0.3, lw=0)
    ax1.text(0.23, (lo + hi) / 2, name, fontsize=8, va="center")
for x0 in (1, 2):
    y0 = pH(x0 * V0)
    ax1.plot([x0], [y0], "o", color="C3", ms=4)
    ax1.annotate(f"sp{x0}: pH {y0:.2f}", (x0, y0), xytext=(x0 + 0.12, y0 - 1.6), fontsize=9)
ax1.set_ylabel("pH")
ax1.set_ylim(0, 14)
ax1.set_title(r"NaOH into H$_3$PO$_4$ (0.1000 M each)", fontsize=10)
D = np.array([fractions(10.0 ** -x) for x in p])
names = [r"H$_3$PO$_4$", r"H$_2$PO$_4^-$", r"HPO$_4^{2-}$", r"PO$_4^{3-}$"]
for j in range(4):
    ax2.plot(a, D[:, j], lw=1.6, label=names[j])
for x0 in (1, 2):
    ax2.axvline(x0, color="0.6", lw=0.8, ls=":")
ax2.set_xlabel("equivalents of NaOH added per H$_3$PO$_4$")
ax2.set_ylabel(r"distribution fraction $\delta$")
ax2.set_xlim(0, 3.5)
ax2.legend(frameon=False, fontsize=8.5, ncol=4, loc="upper center", bbox_to_anchor=(0.5, 1.18))
fig.tight_layout()
