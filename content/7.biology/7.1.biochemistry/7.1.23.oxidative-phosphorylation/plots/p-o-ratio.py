"""Energetics and stoichiometry of chemiosmotic ATP synthesis.
(A) Free energy released per mole of protons returning across the membrane, dmu_H+ = F dpsi + 2.303 RT dpH,
split into its electrical and chemical parts: respiring mitochondria (dpsi 0.15-0.20 V, dpH 0.75, 37 C)
and illuminated chloroplasts (dpH about 3, small dpsi, 25 C).
(B) Protons translocated through Fo per ATP, c/3, for measured c-ring sizes (bovine mitochondria 8; yeast
mitochondria, E. coli and Bacillus PS3 10; Ilyobacter tartaricus 11, a Na+ enzyme; Bacillus TA2.A1 13;
spinach chloroplasts 14; Spirulina 15; Burkholderia pseudomallei 17), and the P/O ratios predicted for
mitochondria with one additional proton per ATP for transport (10 H+ per NADH, 6 per succinate)."""

import numpy as np

import wikibio as bio
from wikibio import bioenergetics as be
from wikibio import charts

P = bio.P
F, R = be.F, be.R
fig, ax = bio.canvas(20.0, 8.6)

# ---- A: proton-motive force ---------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.5))
a = charts.axes_at(ax, (2.0, 1.4, 5.4, 6.2))
cases = [("mitochondria\nΔψ = 0.15 V", 0.15, 0.75, 310.15), ("mitochondria\nΔψ = 0.20 V", 0.20, 0.75, 310.15),
         ("chloroplasts\nΔψ ≈ 0.02 V", 0.02, 3.0, 298.15)]
for k, (name, dpsi, dph, T) in enumerate(cases):
    el, ch = F * dpsi, np.log(10) * R * T * dph
    a.bar(k, el, color=P.fill("channel"), edgecolor=P.edge("channel"), width=0.6, label="electrical, FΔψ" if k == 0 else None)
    a.bar(k, ch, bottom=el, color=P.fill("h"), edgecolor=P.edge("h"), width=0.6,
          label="chemical, 2.303RTΔpH" if k == 0 else None)
    a.text(k, el + ch + 0.6, f"{el + ch:.1f}", ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink())
a.set_xticks(range(3))
a.set_xticklabels([c[0] for c in cases], fontsize=bio.core.FONT["tiny"])
a.set_ylim(0, 33)
a.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(a, None, "Δμ̃(H⁺) / (kJ mol⁻¹)")

# ---- B: c ring and stoichiometry ----------------------------------------------------------------------
bio.panel(ax, "B", (9.0, 8.5))
b = charts.axes_at(ax, (10.6, 1.4, 8.8, 6.2))
c = np.linspace(7.5, 17.5, 50)
b.plot(c, c / 3, color=charts.line("atp_synthase"), lw=1.8, label="H⁺ through F$_\\mathrm{o}$ per ATP (c/3)")
b.plot(c, be.p_o(c, 10), color=charts.line(be.COLOR["complex_i"]), lw=1.6, ls="--", label="P/O, NADH (mitochondria)")
b.plot(c, be.p_o(c, 6), color=charts.line(be.COLOR["complex_ii"]), lw=1.6, ls="--", label="P/O, succinate")
species = [(8, "bovine mito."), (10, r"yeast mito., $\it{E.\ coli}$"), (11, r"$\it{Ilyobacter}$ (Na⁺)"), (13, r"$\it{Bacillus}$ TA2.A1"),
           (14, "spinach chloroplast"), (15, r"$\it{Spirulina}$"), (17, r"$\it{Burkholderia}$")]
for k, (n, name) in enumerate(species):
    b.plot([n], [n / 3], "o", color=charts.line("atp_synthase"), ms=5)
    b.text(n + 0.15, n / 3 - 0.32 + 0.0 * k, name, fontsize=bio.core.FONT["tiny"], color=P.ink(), rotation=0,
           ha="left", va="top")
b.set_xlim(7, 18.5)
b.set_ylim(0, 6.5)
b.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(b, "c subunits per ring", "H⁺ per ATP  ·  P/O")
