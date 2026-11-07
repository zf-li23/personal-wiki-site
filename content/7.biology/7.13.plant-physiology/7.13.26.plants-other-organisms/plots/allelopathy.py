# Dose-response of root elongation to an allelochemical: a sensitive species with hormesis (stimulation at low
# doses; Brain-Cousens model y = (d + phi x) / (1 + (x/e)^b), d = 100 %, phi = 150 % per mM, e = 0.45 mM, b = 2.2)
# and a tolerant species (log-logistic y = d / (1 + (x/e)^b), e = 4 mM, b = 2). The dotted line marks 50 % of the
# control; its intersections give the IC50 values. Parameters are illustrative.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

x = np.logspace(-3, 1.5, 500)  # mM


def sens(x):
    return (100 + 150 * x) / (1 + (x / 0.45) ** 2.2)


def tol(x):
    return 100 / (1 + (x / 4.0) ** 2.0)


fig, ax = plt.subplots(figsize=(7.5, 4.2))
ax.plot(x, sens(x), color="#d9463b", lw=2.2, label="sensitive species (with hormesis)")
ax.plot(x, tol(x), color="#2e9e5b", lw=2.2, label="tolerant species")
ax.axhline(100, color="0.5", lw=0.7)
ax.axhline(50, color="0.5", lw=0.7, ls=":")
for fn, col, k, yy in [(sens, "#d9463b", 0.09, 40), (tol, "#2e9e5b", 1.25, 58)]:
    ic = brentq(lambda z: fn(z) - 50, 0.05, 30)
    ax.plot([ic], [50], "o", color=col, ms=6)
    ax.annotate(f"IC50 = {ic:.2f} mM", (ic, 50), xytext=(ic * k, yy), fontsize=8.5, color=col)
ax.set_xscale("log")
ax.set_xlabel("Allelochemical concentration / mM")
ax.set_ylabel("Root elongation / % of control")
ax.set_ylim(0, 125)
ax.legend(frameon=False, fontsize=8.5, loc="lower left")
fig.tight_layout()
