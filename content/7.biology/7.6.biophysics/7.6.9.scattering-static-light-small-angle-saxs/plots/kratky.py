# Kratky plots distinguish compact from disordered macromolecules.
# Models (all normalized to I(0) = 1):
#   folded: uniform sphere with Rg = 15 A;
#   elongated folded: prolate ellipsoid, semi-axes a, a, 3a with Rg = 15 A (orientational average);
#   Gaussian chain: Debye function 2 (exp(-x) - 1 + x) / x^2, x = (q Rg)^2, Rg = 30 A;
#   unfolded chain: 300 conformations of a freely rotating chain of 100 bonds of 3.8 A (C-alpha spacing)
#   with bond-angle cosine 0.5 (C_inf = 3, Rg about 27 A), scattering by the Debye formula.
# A: Kratky plot q^2 I(q)/I(0) against q: the folded protein gives a bell, the Gaussian chain a plateau
#    (2 / Rg^2), the chain with local stiffness a curve that keeps rising at large q (rod-like segments).
# B: dimensionless Kratky plot (q Rg)^2 I(q)/I(0) against q Rg: compact particles of any size peak near
#    q Rg = sqrt(3) with height 3/e = 1.104 (dotted cross; exact for the Guinier function), elongation
#    shifts the peak to the right, disorder replaces the peak by a plateau at 2 or a rise.
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial.distance import pdist

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(2)
q = np.linspace(0.002, 0.5, 500)


def sphere(q, R):
    x = q * R
    return (3 * (np.sin(x) - x * np.cos(x)) / x**3) ** 2


def ellipsoid(q, a, nu, n=200):
    mu = (np.arange(n) + 0.5) / n
    r = a * np.sqrt(1 + (nu**2 - 1) * mu**2)
    x = np.outer(q, r)
    return ((3 * (np.sin(x) - x * np.cos(x)) / x**3) ** 2).mean(axis=1)


def debye(q, rg):
    x = (q * rg) ** 2
    return 2 * (np.expm1(-x) + x) / x**2


def chain(nb=100, b=3.8, cosang=0.5):
    """One conformation of a freely rotating chain (random torsions, fixed bond angle)."""
    v = np.zeros((nb, 3))
    u = rng.normal(size=3)
    u /= np.linalg.norm(u)
    for i in range(nb):
        if i:
            w = rng.normal(size=3)
            w -= w @ u * u
            w /= np.linalg.norm(w)
            u = cosang * u + np.sqrt(1 - cosang**2) * w
        v[i] = u
    return np.vstack([np.zeros(3), np.cumsum(b * v, axis=0)])


bins = np.arange(0, 400, 0.5)
rc = 0.5 * (bins[1:] + bins[:-1])
h = np.zeros(len(rc))
rg2 = 0.0
for _ in range(300):
    x = chain()
    h += np.histogram(pdist(x), bins=bins)[0]
    rg2 += ((x - x.mean(axis=0)) ** 2).sum(axis=1).mean()
n = 101
rg_chain = np.sqrt(rg2 / 300)
Ichain = (300 * n + 2 * (h * np.sinc(np.outer(q, rc) / np.pi)).sum(axis=1)) / (300 * n**2)

a = 15.0 / np.sqrt(11 / 5)
models = (
    ("folded, sphere", sphere(q, 15.0 / np.sqrt(0.6)), 15.0, "protein", "-"),
    ("folded, ellipsoid 1:1:3", ellipsoid(q, a, 3.0), 15.0, "rna", "-"),
    ("Gaussian chain", debye(q, 30.0), 30.0, "negative", "--"),
    ("unfolded chain, 100 residues", Ichain, rg_chain, "dna", "-"),
)

fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.2))
ax = axs[0]
for name, I, rg, tok, ls in models:
    ax.plot(q, q**2 * I * 1e3, color=charts.line(tok), lw=1.8, ls=ls, label=f"{name} (Rg = {rg:.0f} Å)")
ax.set_xlim(0, 0.5)
ax.set_ylim(0, None)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "q / Å⁻¹", "q² I(q) / I(0)  /  (10⁻³ Å⁻²)")
charts.title(ax, "A   Kratky plot")

ax = axs[1]
for name, I, rg, tok, ls in models:
    x = q * rg
    ax.plot(x, x**2 * I, color=charts.line(tok), lw=1.8, ls=ls, label=name)
ax.axvline(np.sqrt(3), color=P.muted(), lw=0.7, ls=":")
ax.axhline(3 / np.e, color=P.muted(), lw=0.7, ls=":")
ax.text(np.sqrt(3) + 0.08, 0.15, "√3", color=P.muted(), fontsize=8)
ax.text(7.3, 3 / np.e + 0.05, "3/e", color=P.muted(), fontsize=8)
ax.axhline(2, color=P.muted(), lw=0.6, ls=(0, (1, 2)))
ax.text(7.3, 2.05, "2", color=P.muted(), fontsize=8)
ax.set_xlim(0, 8)
ax.set_ylim(0, 3.2)
ax.legend(fontsize=7.5, frameon=False, loc="upper left")
charts.style_axes(ax, "q Rg", "(q Rg)² I(q) / I(0)")
charts.title(ax, "B   Dimensionless Kratky plot")
fig.tight_layout()
