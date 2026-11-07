# Conformers and regulators (schematic; the curves follow the classic forms, not one data set).
# A: body-fluid osmolality against that of the medium. An osmoconformer (a marine mussel) follows the
#    medium; a hyper-regulating crab (a shore crab) keeps its blood above dilute media but conforms in
#    and above seawater; a teleost fish regulates near 300-400 mOsm kg-1 over a wide range. Dotted line:
#    internal = external.
# B: body temperature against ambient temperature. An ectothermic conformer (a lizard at rest, without
#    behavioural thermoregulation) follows the air; an endotherm (a mammal) holds 37 C over a wide range,
#    and fails at the extremes (hypothermia and hyperthermia).
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
fig, ax = bio.canvas(24.0, 9.4)

# ---- A ------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 9.3))
pa = charts.axes_at(ax, (2.2, 1.5, 8.8, 6.7))
x = np.linspace(0, 1300, 400)
pa.plot(x, x, color=P.muted(), lw=0.8, ls=":")
pa.plot(x, x + 15, color=charts.line("dna"), lw=1.8, label="osmoconformer (mussel)")
crab = np.maximum(x, 600 - 0.25 * (600 - x)) + 10
pa.plot(x[x <= 1150], crab[x <= 1150], color=charts.line("protein"), lw=1.8, label="hyper-regulator (shore crab)")
fish = 300 + 80 / (1 + np.exp(-(x - 600) / 150))
pa.plot(x, fish, color=charts.line("rna"), lw=1.8, label="regulator (teleost fish)")
pa.axvline(1000, color=P.muted(), lw=0.7, ls="--")
pa.text(1010, 80, "seawater", fontsize=7.5, color=P.muted(), rotation=90, va="bottom")
leg = pa.legend(loc="upper left", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pa.set_xlim(0, 1300)
pa.set_ylim(0, 1300)
charts.style_axes(pa, "osmolality of the medium / (mOsm kg⁻¹)", "body fluid / (mOsm kg⁻¹)")
charts.title(pa, "Osmotic conformers and regulators")

# ---- B ------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (12.6, 9.3))
pb = charts.axes_at(ax, (14.6, 1.5, 8.8, 6.7))
ta = np.linspace(-10, 45, 400)
pb.plot(ta, ta, color=P.muted(), lw=0.8, ls=":")
pb.plot(ta, ta + 0.8, color=charts.line("dna"), lw=1.8, label="ectotherm, conforming")
body = 37 + 0.02 * (ta - 20)
body = np.where(ta < 0, body - 0.25 * (ta - 0) ** 2, body)
body = np.where(ta > 38, body + 0.3 * np.clip(ta - 38, 0, None) ** 1.6, body)
pb.plot(ta, body, color=charts.line("rna"), lw=1.8, label="endotherm, regulating")
pb.text(-4.5, 18, "hypothermia", fontsize=7.5, color=charts.line("rna"))
pb.text(37, 44.5, "hyperthermia", fontsize=7.5, color=charts.line("rna"), ha="right")
pb.axvspan(0, 38, color=P.mix(P.muted(), P.surface(), 0.85), lw=0)
pb.text(19, 3, "range of regulation", fontsize=7.5, color=P.ink(), ha="center")
leg = pb.legend(loc="lower right", fontsize=7.5, frameon=False)
for txt in leg.get_texts():
    txt.set_color(P.ink())
pb.set_xlim(-10, 45)
pb.set_ylim(-10, 48)
charts.style_axes(pb, "ambient temperature / °C", "body temperature / °C")
charts.title(pb, "Thermal conformers and regulators")
