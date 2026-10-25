"""Redox tower: standard transformed reduction potentials E'0 at pH 7 (Lehninger 8e, Table 13-7).
Left axis E'0 (V); right axis the standard Gibbs energy of transferring two electrons from the
reduced member of a pair to O2, dG'0 = -2F (0.816 V - E'0). The arrow marks NADH -> O2
(1.136 V, -219 kJ/mol)."""

import wikibio as bio
from wikibio import charts

P = bio.P
F = 96.485
pairs = [(0.816, "½O₂ / H₂O", "positive"), (0.771, "Fe³⁺ / Fe²⁺", "neutral"),
         (0.421, "NO₃⁻ / NO₂⁻", "neutral"), (0.35, "cyt a₃ (Fe³⁺/Fe²⁺)", "mitochondrion"),
         (0.254, "cyt c (Fe³⁺/Fe²⁺)", "mitochondrion"), (0.077, "cyt b (Fe³⁺/Fe²⁺)", "mitochondrion"),
         (0.045, "ubiquinone / ubiquinol", "lipid"), (0.031, "fumarate / succinate", "metabolite"),
         (-0.166, "oxaloacetate / malate", "metabolite"), (-0.185, "pyruvate / lactate", "metabolite"),
         (-0.197, "acetaldehyde / ethanol", "metabolite"), (-0.219, "FAD / FADH₂ (free)", "enzyme"),
         (-0.29, "lipoate / dihydrolipoate", "enzyme"), (-0.320, "NAD⁺ / NADH", "enzyme"),
         (-0.346, "acetoacetate / β-hydroxybutyrate", "metabolite"), (-0.414, "2H⁺ / H₂ (pH 7)", "neutral"),
         (-0.432, "ferredoxin (ox/red)", "chloroplast")]

fig, ax = bio.canvas(17.0, 13.0)
a = charts.axes_at(ax, (1.6, 0.8, 0.6, 11.6))
a.set_ylim(-0.5, 0.9)
a.set_xlim(0, 1)
a.set_xticks([])
charts.style_axes(a, None, r"$E'^{\circ}$ / V")
b = charts.axes_at(ax, (15.6, 0.8, 0.6, 11.6))
b.set_ylim(-2 * F * (0.816 + 0.5), -2 * F * (0.816 - 0.9))
b.set_xticks([])
charts.style_axes(b, None, None)
b.spines["left"].set_visible(False)
b.spines["right"].set_visible(True)
b.spines["right"].set_color(P.muted())
b.yaxis.tick_right()
b.yaxis.set_label_position("right")
b.tick_params(axis="y", colors=P.ink(), labelsize=bio.core.FONT["small"])
b.set_ylabel(r"$\Delta_{\mathrm{r}}G'^{\circ}$ for 2 e$^-$ to O$_2$ / (kJ mol$^{-1}$)", color=P.ink(),
             fontsize=bio.core.FONT["small"])

def Y(e):
    return 0.8 + 11.6 * (e + 0.5) / 1.4

# lay labels out in two columns, avoiding overlaps by nudging
last = {0: -9, 1: -9}
for k, (e, name, tok) in enumerate(sorted(pairs)):
    col = k % 2
    x = 5.6 if col == 0 else 11.6
    y = max(Y(e), last[col] + 0.62)
    last[col] = y
    ax.plot([2.25, x - (1.9 if col == 0 else 2.3)], [Y(e), y], color=P.muted(), lw=0.6)
    bio.box(ax, (x, y), 3.8 if col == 0 else 4.6, 0.5, tok, name, size="tiny")
    bio.label(ax, (x + (2.0 if col == 0 else 2.4), y), f"{e:+.3f}", size="tiny", ha="left", color=P.muted())
# NADH -> O2 arrow on the axis
bio.arrow(ax, (2.75, Y(-0.320)), (2.75, Y(0.816)), kind="process", color=P.edge("positive"))
bio.label(ax, (2.95, Y(0.62)), "NADH → O₂\nΔE′° = 1.136 V\n−219 kJ mol⁻¹", size="tiny", ha="left", color=P.edge("positive"))
bio.label(ax, (8.6, 12.7), "stronger oxidants (accept electrons)", size="small", color=P.muted())
bio.label(ax, (8.6, 0.35), "stronger reductants (donate electrons)", size="small", color=P.muted())
