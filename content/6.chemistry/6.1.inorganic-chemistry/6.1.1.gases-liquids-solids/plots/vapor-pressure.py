"""ln p versus 1/T for three liquids (Antoine equations, NIST constants, p in bar)."""

import numpy as np
import matplotlib.pyplot as plt

R = 8.314462618
# log10(p/bar) = A - B / (T/K + C)
liquids = {
    "water": (4.6543, 1435.264, -64.848, (280, 373.2)),
    "ethanol": (5.24677, 1598.673, -46.424, (293, 366)),
    "benzene": (4.01814, 1203.835, -53.226, (288, 354)),
}

fig, ax = plt.subplots(figsize=(7.0, 4.4))
for i, (name, (A, B, C, (T1, T2))) in enumerate(liquids.items()):
    T = np.linspace(T1, T2, 200)
    p_kPa = 100 * 10 ** (A - B / (T + C))
    x = 1000 / T
    y = np.log(p_kPa)
    slope = np.polyfit(1 / T, y, 1)[0]
    dH = -slope * R / 1000
    ax.plot(x, y, color=f"C{i}", lw=1.8,
            label=rf"{name}: fitted $\Delta_{{\mathrm{{vap}}}}H_{{\mathrm{{m}}}}$ = {dH:.1f} kJ/mol")
    # normal boiling point
    Tb = B / (A - np.log10(1.01325)) - C
    ax.plot(1000 / Tb, np.log(101.325), "o", color=f"C{i}")

ax.axhline(np.log(101.325), color="0.55", lw=0.9, ls="--")
ax.text(3.45, np.log(101.325) + 0.12, "p = 101.325 kPa", fontsize=8)
ax.set_xlabel(r"$1000\,\mathrm{K}\,/\,T$")
ax.set_ylabel(r"$\ln(p/\mathrm{kPa})$")
ax.legend(fontsize=8, loc="lower left")
fig.tight_layout()
