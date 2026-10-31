"""Force-extension relations of ideal chains.

A: relative extension z = <x>/L against the dimensionless force F lp / kBT (logarithmic axis) for the
one-dimensional freely jointed chain z = tanh(Fb/kBT), the three-dimensional freely jointed chain
z = coth(Fb/kBT) - kBT/(Fb) (Langevin function), both with Kuhn length b = 2 lp, the worm-like chain
computed exactly (ground state of the rotor Hamiltonian in a Legendre basis of 60 functions), and the
Marko-Siggia interpolation F lp/kBT = z + 1/(4(1-z)^2) - 1/4. All agree at small force, where
z = 2 F lp/(3 kBT); at large force the FJC approaches full extension as 1/F and the WLC as F^(-1/2).
B: lambda DNA (L = 16.5 um, lp = 50 nm) in physical units: force (logarithmic axis) against extension for the exact
WLC, the FJC with b = 100 nm, and the extensible WLC with stretch modulus S = 1000 pN, with the
overstretching transition near 65 pN (treated in 7.6.17) marked."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
KT = 4.11  # pN nm at 298 K
LP = 50.0  # nm


def wlc_exact(f):
    """Relative extension of the WLC for dimensionless forces f = F lp / kBT (array)."""
    n = 60
    l = np.arange(n)
    off = (l[:-1] + 1) / np.sqrt((2 * l[:-1] + 1) * (2 * l[:-1] + 3))
    z = []
    for fi in np.atleast_1d(f):
        H = np.diag(l * (l + 1) / 2.0) - fi * (np.diag(off, 1) + np.diag(off, -1))
        w, v = np.linalg.eigh(H)
        g = v[:, 0]
        z.append(2 * np.dot(g[:-1], off * g[1:]))  # <cos theta> in the ground state = -dE0/df
    return np.array(z)


def marko_siggia_force(z):
    return z + 1.0 / (4.0 * (1.0 - z) ** 2) - 0.25


f = np.logspace(-2, 3, 300)
b = 2.0  # Kuhn length in units of lp
fig, axs = plt.subplots(1, 2, figsize=(9.8, 3.6))
fig.subplots_adjust(wspace=0.3, left=0.08, right=0.97, bottom=0.16, top=0.88)
ax = axs[0]
ax.plot(f, np.tanh(f * b), color=charts.line("neutral"), lw=1.0, ls="--", label="FJC, one dimension")
x = f * b
ax.plot(f, 1 / np.tanh(x) - 1 / x, color=charts.line("protein"), lw=1.3, label="FJC, three dimensions")
ax.plot(f, wlc_exact(f), color=charts.line("dna"), lw=1.6, label="WLC, exact")
zz = np.linspace(0.001, 0.984, 400)
ax.plot(marko_siggia_force(zz), zz, color=charts.line("rna"), lw=1.0, ls=":", label="Marko-Siggia")
ax.plot(f[f < 0.6], 2 * f[f < 0.6] / 3, color=P.muted(), lw=0.8, ls="-.", label=r"linear: $z = 2F\ell_{\mathrm{p}}/3k_{\mathrm{B}}T$")
ax.set_xscale("log")
ax.set_ylim(0, 1.02)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, r"$F\ell_{\mathrm{p}}/k_{\mathrm{B}}T$", r"relative extension $z = \langle x\rangle/L$")
charts.title(ax, "A  Ideal chains under tension")

ax = axs[1]
L = 16.5  # um
F = np.logspace(-2.5, np.log10(70), 400)
fd = F * LP / KT
ax.plot(L * wlc_exact(fd), F, color=charts.line("dna"), lw=1.6, label="WLC, lp = 50 nm")
S = 1000.0
ax.plot(L * (wlc_exact(fd) + F / S), F, color=charts.line("dna"), lw=1.0, ls="--", label="extensible WLC, S = 1000 pN")
xb = F * 100.0 / KT
ax.plot(L * (1 / np.tanh(xb) - 1 / xb), F, color=charts.line("protein"), lw=1.2, label="FJC, b = 100 nm")
ax.axhline(65, color=P.muted(), lw=0.7, ls=":")
ax.text(0.5, 75, "overstretching (about 65 pN)", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.axvline(L, color=P.muted(), lw=0.7, ls=":")
ax.text(L + 0.15, 0.02, "contour length", rotation=90, ha="left", fontsize=bio.core.FONT["tiny"], color=P.ink())
ax.set_xlim(0, 18.5)
ax.set_yscale("log")
ax.set_ylim(3e-3, 150)
ax.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center left", bbox_to_anchor=(0.0, 0.62))
charts.style_axes(ax, r"extension / $\mu$m", "force / pN")
charts.title(ax, "B  Lambda DNA")
