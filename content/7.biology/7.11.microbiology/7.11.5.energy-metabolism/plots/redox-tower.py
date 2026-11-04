"""The redox tower: standard reduction potentials at pH 7 (E0', volts) of couples used in microbial
energy metabolism (values after Thauer et al. 1977 and Madigan et al. 2019; Fe3+/Fe2+ at pH 7 refers
to ferric hydroxide). Left column: couples whose reduced form is a common electron donor; right:
couples whose oxidized form is a common acceptor; middle: cellular carriers. Right panel: Gibbs
energy for H2 (-0.414 V) reducing each acceptor, dG = -z F dE with z = 2 per H2."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
F = 96.485
donors = [("CO₂/glucose (24)", -0.43), ("2H⁺/H₂ (2)", -0.414), ("CO₂/acetate (8)", -0.29),
          ("S⁰/HS⁻ (2)", -0.27), ("Fe³⁺/Fe²⁺, pH 7 (1)", 0.20), ("NO₂⁻/NH₄⁺ (6)", 0.34),
          ("Fe³⁺/Fe²⁺, pH 2 (1)", 0.77)]
carriers = [("ferredoxin (1)", -0.42), ("NAD⁺/NADH (2)", -0.32), ("menaquinone (2)", -0.074),
            ("ubiquinone (2)", 0.11), ("cytochrome c (1)", 0.25)]
acceptors = [("CO₂/CH₄ (8)", -0.244), ("SO₄²⁻/HS⁻ (8)", -0.217), ("pyruvate/lactate (2)", -0.19),
             ("fumarate/succinate (2)", 0.033), ("NO₃⁻/NO₂⁻ (2)", 0.433), ("NO₃⁻/N₂ (5)", 0.75),
             ("MnO₂/Mn²⁺ (2)", 0.80), ("½O₂/H₂O (2)", 0.816)]

fig, ax = bio.canvas(28.0, 14.0)
a = charts.axes_at(ax, (1.8, 0.8, 16.0, 12.6))
a.set_ylim(0.95, -0.55)
a.set_xlim(0, 3)
a.set_xticks([0.75, 1.55, 2.5])
a.set_xticklabels(["electron donors", "carriers", "electron acceptors"])
a.axhspan(-0.55, 0.95, xmin=0.4, xmax=0.62, color=P.mix(P.fill("neutral"), P.surface(), 0.88), zorder=0)


def place(items, x, tok, side):
    ys = [v for _, v in items]
    # spread labels so they do not overlap (minimum spacing 0.045 V)
    lab = []
    for v in sorted(ys):
        lab.append(max(v, lab[-1] + 0.047) if lab else v)
    order = sorted(range(len(items)), key=lambda i: ys[i])
    for rank, i in enumerate(order):
        name, v = items[i]
        a.plot([x - 0.18, x + 0.18], [v, v], color=charts.line(tok), lw=2.4, solid_capstyle="round")
        tx = x + side * 0.24
        a.plot([x + side * 0.18, tx], [v, lab[rank]], color=P.muted(), lw=0.5)
        a.text(tx + side * 0.02, lab[rank], f"{name}  {v:+.2f}", fontsize=bio.core.FONT["tiny"], color=P.ink(),
               ha="left" if side > 0 else "right", va="center")


place(donors, 1.0, "drug", -1)
place(carriers, 1.45, "metabolite", 1)
place(acceptors, 2.25, "enzyme", 1)
a.set_yticks(np.arange(-0.5, 1.0, 0.1))
charts.style_axes(a, None, r"$E^{\circ\prime}$ / V")
a.tick_params(axis="x", length=0)
a.text(0.05, -0.5, "strong donors", fontsize=bio.core.FONT["tiny"], color=P.muted())
a.text(0.05, 0.92, "strong acceptors", fontsize=bio.core.FONT["tiny"], color=P.muted())

b = charts.axes_at(ax, (21.0, 0.8, 6.4, 12.6))
acc = [("O₂ → H₂O", 0.816), ("NO₃⁻ → NO₂⁻", 0.433), ("Fe(III) → Fe²⁺", 0.20), ("fumarate → succinate", 0.033),
       ("SO₄²⁻ → HS⁻", -0.217), ("CO₂ → CH₄", -0.244)]
dg = [-2 * F * (e + 0.414) for _, e in acc]
yy = np.arange(len(acc))
b.barh(yy, dg, color=[P.fill("enzyme")] * len(acc), edgecolor=charts.line("enzyme"), height=0.6)
for k, v in enumerate(dg):
    b.text(v - 6, k, f"{v:.0f}", va="center", ha="right", fontsize=bio.core.FONT["tiny"], color=P.ink())
b.set_yticks(yy)
b.set_yticklabels([n for n, _ in acc])
b.set_ylim(len(acc) - 0.5, -0.5)
b.set_xlim(-290, 0)
charts.style_axes(b, r"$\Delta_{\mathrm{r}}G^{\circ\prime}$ per H$_2$ / (kJ mol$^{-1}$)", None)
charts.title(b, "H₂ as electron donor")
