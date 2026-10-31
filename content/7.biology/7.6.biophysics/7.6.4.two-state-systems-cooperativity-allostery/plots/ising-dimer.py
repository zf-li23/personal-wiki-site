"""Cooperativity from interactions between sites. A: mean occupancy per site of a dimer with
site energy eps and interaction energy J between bound sites (energies in kBT), against
x = (c/c0) exp[-(eps - mu0)/kBT], for J = 0 (independent sites), -2.5 and -5 (positive
cooperativity) and +2.5 (negative cooperativity). B: Hill coefficient at half-saturation,
n_H = 2/(1 + e^{J/2}) (line), checked numerically (dots); it tends to the number of sites, 2, as
J -> -infinity. C: oxygen binding by a tetramer: the MWC curve of 7.1.7 (L = 1e4, c = 0.01,
K_R = 0.35 kPa) and a Pauling model of pairwise interacting sites with the same p50 = 3.5 kPa and
Hill coefficient (omega = e^-J = 5.3) are nearly indistinguishable; the hyperbola with the same
p50 shows what cooperativity buys between the lungs (13 kPa) and active tissue (about 2.5 kPa)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
lg = lambda y: np.log(y / (1 - y))


def dimer(x, J):
    w = np.exp(-J)
    return (x + w * x ** 2) / (1 + 2 * x + w * x ** 2)


def hill_num(f):
    x50 = brentq(lambda lx: f(10 ** lx) - 0.5, -8, 8)
    h = 1e-4
    return (lg(f(10 ** (x50 + h))) - lg(f(10 ** (x50 - h)))) / (2 * h * np.log(10))


fig, axs = plt.subplots(1, 3, figsize=(10.5, 3.3))
fig.subplots_adjust(wspace=0.42, left=0.07, right=0.98, bottom=0.17, top=0.88)

ax = axs[0]
x = np.logspace(-3, 3, 500)
for J, tok in ((2.5, "negative"), (0.0, "neutral"), (-2.5, "enzyme"), (-5.0, "blood")):
    ax.plot(x, dimer(x, J), color=charts.line(tok), lw=1.8, label=f"J = {J:+.1f}" if J else "J = 0")
ax.set_xscale("log")
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"$x = (c/c_0)\,\mathrm{e}^{-\beta(\varepsilon-\mu_0)}$", r"$\langle N\rangle/2$")
charts.title(ax, "A  Dimer with interaction J")

ax = axs[1]
J = np.linspace(-10, 6, 300)
ax.plot(J, 2 / (1 + np.exp(J / 2)), color=charts.line("protein"), lw=1.8)
Jd = np.arange(-9, 7, 2.0)
ax.plot(Jd, [hill_num(lambda xx: dimer(xx, j)) for j in Jd], "o", color=charts.line("blood"), ms=3.5)
ax.axhline(1, color=P.muted(), lw=0.5, ls=":")
ax.axhline(2, color=P.muted(), lw=0.5, ls=":")
ax.text(2.2, 1.65, r"$n_\mathrm{H} = \dfrac{2}{1 + \mathrm{e}^{J/2}}$", fontsize=bio.core.FONT["small"], color=P.ink())
charts.style_axes(ax, r"$J$ / $k_\mathrm{B}T$", r"$n_\mathrm{H}$ at half-saturation")
charts.title(ax, "B  Hill coefficient of the dimer")

ax = axs[2]
KR, cc, L = 0.35, 0.01, 1e4


def mwc(p):
    a = p / KR
    return (a * (1 + a) ** 3 + L * cc * a * (1 + cc * a) ** 3) / ((1 + a) ** 4 + L * (1 + cc * a) ** 4)


def pauling(y, w):
    Z = 1 + 4 * y + 6 * w * y ** 2 + 4 * w ** 3 * y ** 3 + w ** 6 * y ** 4
    N = 4 * y + 12 * w * y ** 2 + 12 * w ** 3 * y ** 3 + 4 * w ** 6 * y ** 4
    return N / (4 * Z)


nh_target = hill_num(mwc)
w = brentq(lambda w_: hill_num(lambda y: pauling(y, w_)) - nh_target, 1.01, 100)
y50 = 10 ** brentq(lambda ly: pauling(10 ** ly, w) - 0.5, -6, 6)
p = np.linspace(0, 16, 400)
ax.plot(p, mwc(p), color=charts.line("blood"), lw=2.2, label="MWC")
ax.plot(p, pauling(p * y50 / 3.5, w), color=charts.line("protein"), lw=1.2, ls="--", label=rf"Pauling, $\omega = {w:.1f}$")
ax.plot(p, p / (p + 3.5), color=P.muted(), lw=1.2, label="no cooperativity")
for pp, txt in ((13.0, "lungs"), (2.5, "tissue")):
    ax.axvline(pp, color=P.muted(), lw=0.5, ls=":")
    ax.text(pp + 0.2, 0.05, txt, fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, r"$p_{\mathrm{O_2}}$ / kPa", r"saturation $\theta$")
charts.title(ax, "C  Two mechanisms, one curve")
