# Hydrogen-deuterium exchange through the Linderstrom-Lang scheme closed <-> open -> exchanged,
# k_obs = k_op k_int / (k_op + k_cl + k_int).
# A: k_obs as the intrinsic (chemical) rate is raised by raising the pH (base catalysis, k_int = 10^(pH - 7) x
#    10 s^-1 for an unprotected amide at 25 C, an order-of-magnitude model), for a site with k_op = 1 s^-1 and
#    k_cl = 10^3 s^-1 (K_op = 10^-3, Delta G_op = 17 kJ/mol): EX2 regime k_obs = K_op k_int while k_int << k_cl,
#    EX1 regime k_obs = k_op when k_int >> k_cl.
# B: fraction of amide H remaining in D2O for protection factors P = k_int / k_obs = 1 to 10^6 (EX2,
#    k_int = 10 s^-1), with the corresponding Delta G_op = RT ln P at 298 K.
# C: simulated mass spectra (isotope fine structure ignored) of a peptide with 12 exchangeable amides after
#    labeling for 1, 10 and 100 s. EX2: each amide exchanges independently with k_obs = 0.03 s^-1, the envelope
#    shifts gradually. EX1: the segment exchanges in one cooperative opening event with k_op = 0.03 s^-1, two
#    populations (unexchanged and fully exchanged) are seen side by side.
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

import wikibio as bio
from wikibio import charts

P = bio.P
fig, axs = plt.subplots(1, 3, figsize=(13.0, 4.0))

ax = axs[0]
pH = np.linspace(4, 13, 400)
kint = 10 * 10 ** (pH - 7)
kop, kcl = 1.0, 1e3
kobs = kop * kint / (kop + kcl + kint)
ax.semilogy(pH, kint, color=P.muted(), lw=1.0, ls="--", label=r"$k_{\mathrm{int}}$ (unprotected)")
ax.semilogy(pH, kobs, color=charts.line("protein"), lw=2.0, label=r"$k_{\mathrm{obs}}$")
ax.semilogy(pH, kop * kint / kcl, color=charts.line("enzyme"), lw=0.9, ls=":", label=r"EX2: $K_{\mathrm{op}}k_{\mathrm{int}}$")
ax.axhline(kop, color=charts.line("rna"), lw=0.9, ls=":", label=r"EX1: $k_{\mathrm{op}}$")
ax.axvline(7 + np.log10(kcl / 10), color=P.muted(), lw=0.6)
ax.text(9.1, 1e-4, r"$k_{\mathrm{int}} = k_{\mathrm{cl}}$", fontsize=7.5, color=P.muted())
ax.set_xlim(4, 13)
ax.set_ylim(1e-6, 1e7)
ax.legend(fontsize=7.3, frameon=False, loc="upper left")
charts.style_axes(ax, r"pH (sets $k_{\mathrm{int}}$)", "rate / s⁻¹")
charts.title(ax, "A   EX2 and EX1 regimes")

ax = axs[1]
t = np.logspace(-3, 7, 400)
R, T = 8.314, 298.15
for Pf, tok in ((1, "neutral"), (1e2, "enzyme"), (1e4, "protein"), (1e6, "rna")):
    ax.semilogx(t, np.exp(-10 / Pf * t), color=charts.line(tok), lw=1.8,
                label=f"$P = 10^{{{int(np.log10(Pf))}}}$:  " + r"$\Delta G_{\mathrm{op}}$" + f" = {R * T * np.log(Pf) / 1000:.0f} kJ/mol")
ax.set_xlim(1e-3, 1e7)
ax.set_ylim(0, 1.05)
for x, lab in ((60, "1 min"), (3600, "1 h"), (86400 * 7, "1 week")):
    ax.axvline(x, color=P.muted(), lw=0.5, ls=":")
    ax.text(x * 1.2, 1.0, lab, fontsize=7, color=P.muted())
ax.legend(fontsize=7.3, frameon=False, loc="lower left")
charts.style_axes(ax, "time in D₂O / s", "fraction of amide ¹H left")
charts.title(ax, r"B   Protection factors (EX2, $k_{\mathrm{int}} = 10\ \mathrm{s^{-1}}$)")

ax = axs[2]
n = 12
m = np.arange(n + 1)
k = 0.03
for row, tt in enumerate((1.0, 10.0, 100.0)):
    p = 1 - np.exp(-k * tt)
    ex2 = binom.pmf(m, n, p)
    f_open = 1 - np.exp(-k * tt)
    ex1 = (1 - f_open) * binom.pmf(m, n, 0.03) + f_open * binom.pmf(m, n, 0.92)
    y0 = 2.4 * (2 - row)
    ax.bar(m - 0.18, ex2 / ex2.max(), width=0.34, bottom=y0, color=P.fill("protein"), edgecolor=P.edge("protein"),
           lw=0.5, label="EX2" if row == 0 else None)
    ax.bar(m + 0.18, ex1 / ex1.max(), width=0.34, bottom=y0, color=P.fill("rna"), edgecolor=P.edge("rna"), lw=0.5,
           label="EX1" if row == 0 else None)
    ax.text(6.0, y0 + 1.25, f"t = {tt:.0f} s", fontsize=7.5, color=P.ink(), ha="center")
ax.set_xlim(-0.8, 12.8)
ax.set_ylim(0, 7.3)
ax.set_yticks([])
ax.legend(fontsize=7.5, frameon=False, loc="upper left", bbox_to_anchor=(0.0, 1.0), ncol=2)
charts.style_axes(ax, "deuterons incorporated (mass shift / Da)", None)
charts.title(ax, "C   HDX-MS: EX2 shifts, EX1 is bimodal")
fig.tight_layout()
