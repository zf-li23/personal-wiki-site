# The carbonate system of seawater (15 degC, salinity 35; constants of Lueker et al. 2000 and
# Weiss 1974, borate included; total alkalinity held at 2300 umol/kg).
# A: Bjerrum plot of the fractions of CO2(aq), bicarbonate and carbonate against pH.
# B: surface-ocean pH and carbonate ion against atmospheric CO2. C: the Revelle factor.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio

P = bio.P
T, S = 288.15, 35.0
pK1 = 3633.86 / T - 61.2172 + 9.67770 * np.log(T) - 0.011555 * S + 0.0001152 * S ** 2
pK2 = 471.78 / T + 25.9290 - 3.16967 * np.log(T) - 0.01781 * S + 0.0001122 * S ** 2
K1, K2 = 10 ** -pK1, 10 ** -pK2
TK = T / 100
K0 = np.exp(-60.2409 + 93.4517 / TK + 23.3585 * np.log(TK) + S * (0.023517 - 0.023656 * TK + 0.0047036 * TK ** 2))
KB, TB, Kw, TA = 10 ** -8.70, 416e-6, 4.0e-14, 2300e-6

def state(pco2):
    co2 = K0 * pco2 * 1e-6
    f = lambda h: K1 * co2 / h + 2 * K1 * K2 * co2 / h ** 2 + TB * KB / (KB + h) + Kw / h - h - TA
    h = brentq(f, 1e-10, 1e-6, xtol=1e-22, rtol=1e-14)
    return -np.log10(h), co2 + K1 * co2 / h + K1 * K2 * co2 / h ** 2, K1 * K2 * co2 / h ** 2

fig, (a, b, c) = plt.subplots(1, 3, figsize=(13.4, 4.2), gridspec_kw={"width_ratios": [1.1, 1.15, 0.85]})
ph = np.linspace(4, 11, 400)
h = 10 ** -ph
den = h ** 2 + K1 * h + K1 * K2
for frac, lab, tok in ((h ** 2 / den, "CO$_2$(aq)", "neutral"), (K1 * h / den, "HCO$_3^-$", "dna"),
                       (K1 * K2 / den, "CO$_3^{2-}$", "rna")):
    a.plot(ph, frac, color=P.edge(tok) if tok == "neutral" else P.fill(tok), lw=2, label=lab)
a.axvspan(7.7, 8.2, color=P.fill("highlight"), alpha=0.35, lw=0)
a.text(7.95, 1.04, "surface ocean", ha="center", fontsize=7.5, color=P.muted())
a.axvline(pK1, color=P.muted(), lw=0.7, ls=":")
a.axvline(pK2, color=P.muted(), lw=0.7, ls=":")
a.text(pK1 - 0.1, 0.78, f"pK$_1$* = {pK1:.2f}", rotation=90, fontsize=7.5, ha="right", color=P.muted())
a.text(pK2 + 0.1, 0.78, f"pK$_2$* = {pK2:.2f}", rotation=90, fontsize=7.5, ha="left", color=P.muted())
a.set_xlim(4, 11)
a.set_ylim(0, 1.09)
a.set_xlabel("pH")
a.set_ylabel("Fraction of dissolved inorganic carbon")
a.legend(frameon=False, fontsize=8, loc="center left")
a.set_title("A  Carbonate speciation", loc="left", fontweight="bold")

pc = np.linspace(200, 1200, 120)
st = np.array([state(p) for p in pc])
rev = []
for p in pc:
    s1, s2 = state(p * 0.995), state(p * 1.005)
    rev.append(0.01 / ((s2[1] - s1[1]) / (0.5 * (s1[1] + s2[1]))))
b.plot(pc, st[:, 0], color=P.ink(), lw=2, label="pH")
for p, txt in ((280, "1750"), (423, "2024"), (850, "2100, very high emissions")):
    v = state(p)[0]
    b.plot([p], [v], "o", color=P.ink(), ms=4)
    b.annotate(f"{txt}: pH {v:.2f}", (p, v), xytext=(6, 6) if p < 800 else (-10, -16), ha="left" if p < 800 else "right",
               textcoords="offset points", fontsize=7.5, color=P.ink())
b.set_xlabel("Atmospheric CO$_2$ / ppm")
b.set_ylabel("pH")
b.set_ylim(7.5, 8.35)
b2 = b.twinx()
b2.plot(pc, st[:, 2] * 1e6, color=P.fill("rna"), lw=1.8, ls="--", label="CO$_3^{2-}$ / µmol kg$^{-1}$")
b2.set_ylim(0, 300)
b2.set_ylabel("CO$_3^{2-}$ / µmol kg$^{-1}$")
h1, l1 = b.get_legend_handles_labels()
h2, l2 = b2.get_legend_handles_labels()
b.legend(h1 + h2, l1 + l2, frameon=False, fontsize=7.5, loc="lower left")
b.set_title("B  Ocean acidification", loc="left", fontweight="bold")
c.plot(pc, rev, color=P.fill("dna"), lw=2)
for p in (280, 423, 850):
    c.plot([p], [np.interp(p, pc, rev)], "o", color=P.ink(), ms=4)
    c.annotate(f"{np.interp(p, pc, rev):.1f}", (p, np.interp(p, pc, rev)), xytext=(-4, 7), textcoords="offset points",
               fontsize=7.5, ha="right", color=P.ink())
c.set_xlabel("Atmospheric CO$_2$ / ppm")
c.set_ylabel("Revelle factor")
c.set_ylim(8, 18)
c.spines["right"].set_visible(False)
c.spines["top"].set_visible(False)
c.set_title("C  Buffer factor", loc="left", fontweight="bold")
for ax in (a, b):
    ax.spines["top"].set_visible(False)
a.spines["right"].set_visible(False)
b2.spines["top"].set_visible(False)
fig.tight_layout()
