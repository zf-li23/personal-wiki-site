"""20.00 mL of 0.1000 mol/L Na2CO3 titrated with 0.1000 mol/L HCl in a closed system
(pKa1 6.35, pKa2 10.33, CRC), from the charge balance. The first stoichiometric point
(NaHCO3, pH 8.34) lies on a very shallow part of the curve; the second (CO2 solution) is
sharper but is moved by dissolved CO2. Inset: pH within +-1 % of the first point."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

Kw = 1.0e-14
K1, K2 = 10.0 ** -6.35, 10.0 ** -10.33
c0, V0, ca = 0.1000, 20.00, 0.1000


def pH(v):
    ct, na, cl = c0 * V0 / (V0 + v), 2 * c0 * V0 / (V0 + v), ca * v / (V0 + v)
    def f(p):
        h = 10.0 ** -p
        D = h * h + K1 * h + K1 * K2
        return h + na - cl - Kw / h - ct * (K1 * h + 2 * K1 * K2) / D
    return brentq(f, -1.0, 15.0, xtol=1e-10)


v = np.linspace(0, 50, 600)
p = np.array([pH(x) for x in v])
fig, ax = plt.subplots(figsize=(7.5, 4.4))
ax.plot(v, p, color="C0", lw=1.8)
for lo, hi, col, name in [(8.2, 10.0, "C3", "phenolphthalein"), (3.1, 4.4, "C1", "methyl orange"),
                          (4.4, 6.2, "C2", "methyl red")]:
    ax.axhspan(lo, hi, xmin=0.93, xmax=1.0, color=col, alpha=0.3, lw=0)
    ax.text(46.2, (lo + hi) / 2, name, fontsize=8, va="center", ha="right")
for vv in (20.0, 40.0):
    ax.plot([vv], [pH(vv)], "o", color="C3", ms=4)
    ax.annotate(f"pH {pH(vv):.2f}", (vv, pH(vv)), xytext=(vv - 7.5, pH(vv) - 1.2), fontsize=9)
ax.set_xlabel(r"$V$(HCl) / mL")
ax.set_ylabel("pH")
ax.set_xlim(0, 50)
ax.set_ylim(0, 13)
ins = ax.inset_axes([0.08, 0.10, 0.32, 0.36])
vi = np.linspace(19.6, 20.4, 100)
ins.plot((vi - 20) / 20 * 100, [pH(x) for x in vi], color="C0")
ins.set_xlabel("deviation from sp1 / %", fontsize=7)
ins.set_ylabel("pH", fontsize=7)
ins.tick_params(labelsize=7)
fig.tight_layout()
