# Bond rupture under force: dynamic force spectroscopy and catch bonds.
# Bell bond: k(F) = k0 exp(F x/kT), k0 = 0.1 /s, x = 0.5 nm, kT = 4.11 pN nm. Under a constant loading rate
# r = dF/dt the rupture force has survival S(F) = exp[-(k0 kT/(r x)) (exp(F x/kT) - 1)].
# A: histograms of 2000 simulated rupture forces (sampled exactly from S(F)) at r = 10, 100, 1000 and 10^4 pN/s,
#    with the theoretical densities. B: most probable rupture force against ln r: the Evans-Ritchie line
#    F* = (kT/x) ln(r x/(k0 kT)) (slope kT/x = 8.2 pN per e-fold) and a bond with an additional inner barrier
#    (k0' = 10 /s, x' = 0.12 nm, rates in series) whose slope steepens at high loading rates.
# C: lifetime against force for a slip bond (Bell), an ideal bond and a catch-slip bond in the two-pathway model
#    k(F) = kc exp(-F xc/kT) + ks exp(F xs/kT) with kc = 2 /s, xc = 1.0 nm, ks = 0.02 /s, xs = 0.4 nm.
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

import wikibio as bio
from wikibio import charts

P = bio.P
rng = np.random.default_rng(0)
kT, k0, x = 4.11, 0.1, 0.5
fig, axs = plt.subplots(1, 3, figsize=(13.5, 4.1))
toks = ("dna", "neutral", "enzyme", "rna")
for r, tok in zip((1e1, 1e2, 1e3, 1e4), toks):
    u = rng.random(2000)
    Fr = kT / x * np.log(1 - r * x / (k0 * kT) * np.log(u))
    axs[0].hist(Fr, bins=40, density=True, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.3, alpha=0.75)
    F = np.linspace(0, 90, 400)
    a = k0 * kT / (r * x)
    dens = k0 * np.exp(F * x / kT) / r * np.exp(-a * (np.exp(F * x / kT) - 1))
    axs[0].plot(F, dens, color=charts.line(tok), lw=1.4, label=f"r = {r:g} pN/s")
charts.style_axes(axs[0], "rupture force / pN", "probability density / pN⁻¹")
axs[0].legend(fontsize=7.5, frameon=False)
charts.title(axs[0], "A   Rupture forces depend on loading rate")


def fstar(r, kfun):
    # most probable force: maximum of k(F) S(F)/r, i.e. d/dF [ln k(F)] = k(F)/r
    lnk = lambda F: np.log(kfun(F))
    g = lambda F: (lnk(F + 1e-4) - lnk(F - 1e-4)) / 2e-4 - kfun(F) / r
    try:
        return brentq(g, 1e-3, 400)
    except ValueError:
        return 0.0


rs = np.logspace(-1, 6, 60)
bell = lambda F: k0 * np.exp(F * x / kT)
inner = lambda F: 1 / (1 / bell(F) + 1 / (10.0 * np.exp(F * 0.12 / kT)))
axs[1].semilogx(rs, [fstar(r, bell) for r in rs], color=charts.line("dna"), lw=1.8, label="single barrier, x = 0.5 nm")
axs[1].semilogx(rs, [fstar(r, inner) for r in rs], color=charts.line("rna"), lw=1.8, ls="--",
                label="plus inner barrier, x′ = 0.12 nm")
charts.style_axes(axs[1], "loading rate r / (pN s⁻¹)", "most probable rupture force F* / pN")
axs[1].legend(fontsize=7.5, frameon=False, loc="upper left")
axs[1].text(30, 4, "slope kT/x = 8.2 pN per e-fold", fontsize=7.5, color=P.muted())
charts.title(axs[1], "B   Dynamic force spectrum")

F = np.linspace(0, 40, 300)
axs[2].semilogy(F, 1 / bell(F), color=charts.line("dna"), lw=1.8, label="slip bond")
kcs = 2.0 * np.exp(-F * 1.0 / kT) + 0.02 * np.exp(F * 0.4 / kT)
axs[2].semilogy(F, 1 / kcs, color=charts.line("rna"), lw=1.8, label="catch–slip bond")
axs[2].semilogy(F, np.full_like(F, 10.0), color=P.muted(), lw=1.2, ls=":", label="ideal bond")
charts.style_axes(axs[2], "force / pN", "mean lifetime / s")
axs[2].legend(fontsize=7.5, frameon=False, loc="lower left")
charts.title(axs[2], "C   Slip, catch and ideal bonds")
fig.tight_layout()
