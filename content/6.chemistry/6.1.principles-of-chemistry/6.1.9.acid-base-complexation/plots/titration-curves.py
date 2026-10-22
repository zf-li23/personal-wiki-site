"""Titration curves computed from the charge balance, solved for [H+] by bracketing root finding in the variable pH.
Left: 20.00 mL of HCl titrated with NaOH of the same concentration (0.1000 and 0.01000 mol/L),
with the transition ranges of three indicators. Right: 0.1000 mol/L HAc versus HCl."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

Kw, Ka = 1.0e-14, 1.75e-5
V0 = 20.00
Vb = np.concatenate([np.linspace(0, 19.9, 200), np.linspace(19.9, 20.1, 200), np.linspace(20.1, 40, 200)])


def pH_strong(c, v):
    excess = c * (v - V0) / (V0 + v)                  # [Na+] - [Cl-]
    f = lambda p: 10.0**-p - Kw * 10.0**p + excess        # solve in pH, not [H+], for accuracy
    return brentq(f, -1.0, 15.0, xtol=1e-10)


def pH_weak(c, v):
    ct, na = c * V0 / (V0 + v), c * v / (V0 + v)
    def f(p):
        x = 10.0**-p
        return x + na - Kw / x - ct * Ka / (Ka + x)
    return brentq(f, -1.0, 15.0, xtol=1e-10)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2), sharey=True)
for c, col in [(0.1000, "C0"), (0.01000, "C3")]:
    ax1.plot(Vb, [pH_strong(c, v) for v in Vb], color=col, lw=1.8, label=f"c = {c:g} M")
indicators = [("methyl orange", 3.1, 4.4, "C1"), ("methyl red", 4.4, 6.2, "C3"), ("phenolphthalein", 8.0, 10.0, "C4")]
for name, lo, hi, col in indicators:
    ax1.axhspan(lo, hi, xmin=0.0, xmax=0.12, color=col, alpha=0.25, lw=0)
    ax1.text(0.3, (lo + hi) / 2, name, fontsize=8, va="center")
ax1.set_title("NaOH into 20.00 mL HCl", fontsize=10)
ax1.set_xlabel(r"$V$(NaOH) / mL")
ax1.set_ylabel("pH")
ax1.legend(frameon=False, fontsize=9, loc="lower right")

ax2.plot(Vb, [pH_strong(0.1, v) for v in Vb], color="C0", lw=1.4, ls="--", label="HCl")
ax2.plot(Vb, [pH_weak(0.1, v) for v in Vb], color="C2", lw=1.8, label="HAc")
ax2.plot([10.0], [pH_weak(0.1, 10.0)], "o", color="C2", ms=4)
ax2.annotate(r"half-neutralized: pH = p$K_a$", (10.0, pH_weak(0.1, 10.0)), xytext=(3, 6.3), fontsize=9,
             arrowprops=dict(arrowstyle="-", color="0.5"))
ax2.plot([20.0], [pH_weak(0.1, 20.0)], "s", color="C2", ms=4)
ax2.annotate("equivalence point pH 8.73", (20.0, pH_weak(0.1, 20.0)), xytext=(23, 6.0), fontsize=9,
             arrowprops=dict(arrowstyle="-", color="0.5"))
ax2.set_title("NaOH into 20.00 mL acid, 0.1000 M", fontsize=10)
ax2.set_xlabel(r"$V$(NaOH) / mL")
ax2.legend(frameon=False, fontsize=9, loc="lower right")
for ax in (ax1, ax2):
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 14)
fig.tight_layout()
