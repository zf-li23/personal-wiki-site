# Acidity of rain and its effect on aluminium in surface waters (25 degC).
# A: pH of rain water in equilibrium with atmospheric CO2 (Henry constant 0.0334 mol L^-1 atm^-1,
#    pK1 = 6.35) as strong acid (sulfuric and nitric) is added; for 280 and 420 ppm CO2 the pH of
#    unpolluted rain is about 5.6. B: solubility of aluminium in equilibrium with gibbsite,
#    log[Al3+] = 8.1 - 3 pH (mol/L), which rises a thousandfold for each unit decrease in pH.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio

P = bio.P
K0, K1, Kw = 0.0334, 10 ** -6.35, 1e-14

def ph(acid, pco2):
    co2 = K0 * pco2 * 1e-6
    h = brentq(lambda h: h - acid - K1 * co2 / h - Kw / h, 1e-9, 1)
    return -np.log10(h)

fig, (a, b) = plt.subplots(1, 2, figsize=(10.8, 4.2))
acid = np.logspace(-1, 3, 300)          # strong acid, micro-equivalents per litre
for pc, tok, ls in ((280, "dna", "--"), (420, "negative", "-")):
    a.plot(acid, [ph(x * 1e-6, pc) for x in acid], color=P.fill(tok), lw=2, ls=ls, label=f"CO$_2$ = {pc} ppm")
a.axhline(5.6, color=P.muted(), lw=0.8, ls=":")
a.text(0.12, 5.75, "pH 5.6: definition of acid rain", fontsize=7.5, color=P.muted())
for v, t in ((4.5, "typical acid rain\n(1980s, Europe and N. America)"), (4.0, "severe")):
    a.axhspan(v - 0.25, v + 0.25, color=P.fill("highlight"), alpha=0.25, lw=0)
    a.text(250, v, t, fontsize=7, ha="right", va="center", color=P.ink())
a.set_xscale("log")
a.set_xlim(0.1, 1000)
a.set_ylim(2.8, 6.1)
a.set_xlabel("Strong acid (sulfate + nitrate) / µeq L$^{-1}$")
a.set_ylabel("pH of rain")
a.legend(frameon=False, fontsize=7.5, loc="lower left")
a.set_title("A  Acidity of rain", loc="left", fontweight="bold")

p = np.linspace(4, 6.5, 200)
al = 10 ** (8.1 - 3 * p) * 26.98e6          # micrograms per litre
b.plot(p, al, color=P.ink(), lw=2)
b.axhspan(100, 1e5, color=P.fill("negative"), alpha=0.18, lw=0)
b.text(6.4, 1.5e3, "inorganic Al toxic to fish\n(above about 100 µg L$^{-1}$)", fontsize=7.5, ha="right", color=P.ink())
b.set_yscale("log")
b.set_ylim(0.1, 1e5)
b.set_xlim(4, 6.5)
b.set_xlabel("pH of water")
b.set_ylabel("Dissolved Al$^{3+}$ (gibbsite equilibrium) / µg L$^{-1}$")
b.set_title("B  Mobilization of aluminium", loc="left", fontweight="bold")
for ax in (a, b):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
fig.tight_layout()
