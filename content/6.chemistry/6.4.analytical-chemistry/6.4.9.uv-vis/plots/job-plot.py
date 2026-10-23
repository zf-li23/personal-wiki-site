"""Method of continuous variations (Job plot). Solutions with c_M + c_L = 1.0e-3 mol/L and
ligand mole fraction x; only the complex absorbs (eps = 5000, b = 1 cm). The exact
equilibrium for M + nL = ML_n is solved with brentq. The maximum lies at x = n/(n+1);
a weaker complex gives a rounded maximum, and the tangents at the ends cross at that x."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

ctot, eps = 1.0e-3, 5000.0
x = np.linspace(0.001, 0.999, 300)

def absorbance(n, beta):
    out = []
    for xi in x:
        cM, cL = (1 - xi) * ctot, xi * ctot
        f = lambda y: y - beta * (cM - y) * (cL - n * y) ** n
        out.append(eps * brentq(f, 0, min(cM, cL / n) * (1 - 1e-12)))
    return np.array(out)

fig, ax = plt.subplots(figsize=(6.6, 4.2))
for n, beta, col, ls in [(1, 1e8, "C0", "-"), (1, 1e4, "C0", "--"), (2, 1e14, "C3", "-"), (2, 1e8, "C3", "--")]:
    lab = "ML" if n == 1 else r"ML$_2$"
    ax.plot(x, absorbance(n, beta), color=col, ls=ls, lw=1.4,
            label=rf"{lab}, $\lg\beta$ = {np.log10(beta):.0f}")
for xm in (0.5, 2 / 3):
    ax.axvline(xm, color="0.5", lw=0.8, ls=":")
ax.text(0.505, 0.05, "x = 1/2", fontsize=8)
ax.text(0.672, 0.05, "x = 2/3", fontsize=8)
ax.set_xlabel(r"ligand mole fraction $x = c_{\mathrm{L}}/(c_{\mathrm{M}} + c_{\mathrm{L}})$")
ax.set_ylabel(r"absorbance $A$")
ax.set_xlim(0, 1)
ax.set_ylim(0, None)
ax.legend(frameon=False, fontsize=8, loc="upper left")
fig.tight_layout()
