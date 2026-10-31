# The Guinier approximation I(q) = I(0) exp(-q^2 Rg^2 / 3) and its range of validity.
# A: Guinier plot ln[I(q)/I(0)] against q^2 for a solid sphere (R = 25 A, Rg = 19.4 A) and an elongated
#    cylinder (radius 10 A, length 150 A, Rg = 43.9 A), with the Guinier lines of slope -Rg^2/3.
#    Ticks mark q Rg = 1.3 (the usual upper limit for globular particles) and q Rg = 0.8 (the stricter
#    limit used for elongated ones).
# B: relative error of the Guinier approximation, I_exact / I_Guinier - 1, against q Rg for the sphere,
#    the cylinder of panel A, a thin disc (radius 50 A, thickness 4 A) and a Gaussian chain (Debye
#    function 2 (exp(-x) - 1 + x) / x^2 with x = q^2 Rg^2). The exact form factors of cylinder and disc
#    are averaged numerically over orientations.
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import j1

import wikibio as bio
from wikibio import charts

P = bio.P


def sphere(q, R):
    x = q * R
    return (3 * (np.sin(x) - x * np.cos(x)) / x**3) ** 2


def cylinder(q, R, L, n=400):
    """Orientationally averaged form factor of a uniform cylinder (radius R, length L)."""
    mu = (np.arange(n) + 0.5) / n                    # cos(alpha), midpoint rule on [0, 1]
    s = np.sqrt(1 - mu**2)
    a = np.outer(q, R * s)
    b = np.outer(q, L * mu / 2)
    fr = np.where(a > 1e-9, 2 * j1(a) / np.where(a > 1e-9, a, 1), 1.0)
    fl = np.sinc(b / np.pi)
    return (fr * fl) ** 2 @ np.full(n, 1.0 / n)


def debye(q, rg):
    x = (q * rg) ** 2
    return 2 * (np.expm1(-x) + x) / x**2


fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.2))

ax = axs[0]
cases = (("sphere, Rg = 19.4 Å", lambda q: sphere(q, 25.0), np.sqrt(3 / 5) * 25.0, "protein"),
         ("cylinder, Rg = 43.9 Å", lambda q: cylinder(q, 10.0, 150.0), np.sqrt(10.0**2 / 2 + 150.0**2 / 12),
          "dna"))
q = np.linspace(1e-3, 0.075, 300)
for name, f, rg, tok in cases:
    col = charts.line(tok)
    ax.plot(q**2 * 1e3, np.log(f(q)), color=col, lw=1.9, label=name)
    ax.plot(q**2 * 1e3, -(q * rg) ** 2 / 3, color=col, lw=0.9, ls=(0, (3, 2)))
    for lim, mk in ((1.3, "o"), (0.8, "s")):
        qq = lim / rg
        if qq < q[-1]:
            ax.plot(qq**2 * 1e3, np.log(f(np.array([qq])))[0], mk, color=col, ms=5, mfc="none", mew=1.2)
ax.plot([], [], "o", color=P.muted(), mfc="none", label="q Rg = 1.3")
ax.plot([], [], "s", color=P.muted(), mfc="none", label="q Rg = 0.8")
ax.plot([], [], color=P.muted(), lw=0.9, ls=(0, (3, 2)), label="Guinier line")
ax.set_xlim(0, 5.6)
ax.set_ylim(-4.5, 0.1)
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(ax, "q² / (10⁻³ Å⁻²)", "ln[I(q) / I(0)]")
charts.title(ax, "A   Guinier plot")

ax = axs[1]
x = np.linspace(0.02, 2.0, 300)
rows = (("sphere", lambda q: sphere(q, 25.0), np.sqrt(3 / 5) * 25.0, "protein", "-"),
        ("cylinder 10 × 150 Å", lambda q: cylinder(q, 10.0, 150.0), np.sqrt(50 + 150.0**2 / 12), "dna", "-"),
        ("disc 50 × 4 Å", lambda q: cylinder(q, 50.0, 4.0), np.sqrt(50.0**2 / 2 + 4.0**2 / 12), "rna", "-"),
        ("Gaussian chain", lambda q: debye(q, 30.0), 30.0, "negative", "--"))
for name, f, rg, tok, ls in rows:
    qq = x / rg
    err = f(qq) / np.exp(-(x**2) / 3) - 1
    ax.plot(x, 100 * err, color=charts.line(tok), lw=1.8, ls=ls, label=name)
ax.axhline(0, color=P.muted(), lw=0.6)
for lim in (0.8, 1.3):
    ax.axvline(lim, color=P.muted(), lw=0.7, ls=":")
    ax.text(lim + 0.02, 13, f"{lim}", color=P.muted(), fontsize=7.5)
ax.set_xlim(0, 2.0)
ax.set_ylim(-20, 15)
ax.legend(fontsize=7.5, frameon=False, loc="lower left")
charts.style_axes(ax, "q Rg", "deviation from Guinier  (%)")
charts.title(ax, "B   Error of the Guinier approximation")
fig.tight_layout()
