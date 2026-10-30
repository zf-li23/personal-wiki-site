"""Epigenetic reprogramming in the mouse germ line and the kinship model of imprinting. A: global CpG
methylation (schematic, after Seisenberger et al. 2012 and others). After fertilization the genome is
demethylated to the blastocyst, except imprinting control regions; the epiblast remethylates to about 70 %.
PGCs lose methylation again during migration and in the gonad, erasing imprints at E10.5-12.5 (to about 5 % at
E13.5); new methylation, including the sex-specific imprints, is laid down in prospermatogonia before birth and
in growing oocytes after birth. B: inclusive fitness of a fetal allele, B(x) - r C(x), against the demand x it
places on the mother (Formula 27.7.1); the optimum x* = ln(1/r) is larger for a paternal allele (r = 1/4 if
half of the mother's other offspring share the father, r = 1/8 if a quarter do) than for a maternal one (r = 1/2)."""
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 3.9), gridspec_kw={"width_ratios": [1.45, 1]})
fig.subplots_adjust(left=0.07, right=0.98, bottom=0.2, top=0.88, wspace=0.25)
stages = ["zygote", "blastocyst", "E6.5\nepiblast", "E9.5\nPGC", "E13.5\nPGC", "E18.5\ngonocyte", "adult\ngamete"]
x = np.arange(len(stages))
som = [55, 20, 72, 72, 75, 75, 75]
male = [55, 20, 72, 30, 6, 60, 82]
fem = [55, 20, 72, 30, 4, 8, 40]
a.plot(x[:3], som[:3], color=charts.line("neutral"), lw=1.6)
a.plot(x[2:], som[2:], color=charts.line("neutral"), lw=1.6, ls="--", label="soma")
a.plot(x[2:], male[2:], color=charts.line("channel"), lw=1.8, marker="o", ms=4, label="male germ line")
a.plot(x[2:], fem[2:], color=charts.line("receptor"), lw=1.8, marker="o", ms=4, label="female germ line")
a.plot(x[:3], som[:3], "o", color=charts.line("neutral"), ms=4)
a.axvspan(3.2, 4.3, color=charts.line("highlight"), alpha=0.25, lw=0)
a.text(3.75, 92, "imprints erased", ha="center", fontsize=FT["tiny"], color=P_.ink())
a.axvspan(4.6, 5.4, color=charts.line("channel"), alpha=0.15, lw=0)
a.axvspan(5.6, 6.4, color=charts.line("receptor"), alpha=0.15, lw=0)
a.text(5.0, 92, "paternal\nimprints", ha="center", va="top", fontsize=FT["tiny"], color=P_.ink())
a.text(6.0, 30, "maternal imprints\n(growing oocyte)", ha="center", fontsize=FT["tiny"], color=P_.ink())
a.set_xticks(x)
a.set_xticklabels(stages, fontsize=FT["tiny"])
a.set_ylim(0, 100)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="lower left")
charts.style_axes(a, None, "CpG methylation / %")
charts.title(a, "A  Reprogramming of the germ line (schematic)")
xx = np.linspace(0, 3.5, 300)
for r, tk, txt in ((0.5, "receptor", "maternal allele, r = 1/2"), (0.25, "channel", "paternal allele, r = 1/4"),
                   (0.125, "drug", "paternal allele, r = 1/8")):
    w = 1 - np.exp(-xx) - r * xx
    b.plot(xx, w, color=charts.line(tk), lw=1.7, label=txt)
    xs = np.log(1 / r)
    b.plot([xs], [1 - np.exp(-xs) - r * xs], "o", color=charts.line(tk), ms=5)
b.set_ylim(-0.1, 0.8)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="lower right")
charts.style_axes(b, "demand on the mother, x", "B(x) - r C(x)")
charts.title(b, "B  Kinship model: optimal demand")
