"""20.00 mL of 0.1000 mol/L glycine hydrochloride (H3N+CH2COOH) titrated with 0.1000 mol/L NaOH
(pKa1 2.34, pKa2 9.60, CRC), from the charge balance. Top: pH; the first equivalent leaves the
zwitterion at pH = pI. Bottom: fractions of the cation, the zwitterion and the anion."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

Kw = 1.0e-14
K1, K2 = 10.0 ** -2.34, 10.0 ** -9.60
c0, V0, cb = 0.1000, 20.00, 0.1000


def fr(h):
    t = np.array([h * h, K1 * h, K1 * K2])
    return t / t.sum()


def pH(v):
    ct, na, cl = c0 * V0 / (V0 + v), cb * v / (V0 + v), c0 * V0 / (V0 + v)
    def f(p):
        h = 10.0 ** -p
        d = fr(h)
        return h + na + ct * d[0] - cl - Kw / h - ct * d[2]
    return brentq(f, -1.0, 15.0, xtol=1e-10)


v = np.linspace(0, 50, 600)
p = np.array([pH(x) for x in v])
a = v / V0
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7.2, 6.2), sharex=True, gridspec_kw={"height_ratios": [3, 2]})
ax1.plot(a, p, color="C0", lw=1.8)
pI = (2.34 + 9.60) / 2
ax1.plot([1], [pH(V0)], "o", color="C3", ms=4)
ax1.annotate(f"pI = {pI:.2f}", (1, pH(V0)), xytext=(1.1, pI - 1.5), fontsize=9)
for k, pk in [(1, 2.34), (2, 9.60)]:
    ax1.axhline(pk, color="C2", lw=0.8, ls=":")
    ax1.text(2.48, pk + 0.2, rf"p$K_{{a{k}}}$ = {pk:.2f}", fontsize=9, color="C2", ha="right")
ax1.set_ylabel("pH")
ax1.set_ylim(0, 13.5)
ax1.set_title("NaOH into glycine hydrochloride (0.1000 M each)", fontsize=10)
D = np.array([fr(10.0 ** -x) for x in p])
for j, name in enumerate([r"H$_3$N$^+$CH$_2$COOH", r"H$_3$N$^+$CH$_2$COO$^-$ (zwitterion)", r"H$_2$NCH$_2$COO$^-$"]):
    ax2.plot(a, D[:, j], lw=1.6, label=name)
ax2.set_xlabel("equivalents of NaOH added")
ax2.set_ylabel(r"$\delta$")
ax2.set_xlim(0, 2.5)
ax2.legend(frameon=False, fontsize=8, loc="center right")
fig.tight_layout()
