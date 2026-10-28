"""Dominant-negative (poison-subunit) mutations in homo-oligomeric proteins.
If a fraction f of the subunits made in a cell are mutant and assemble at random into n-mers, and any mutant
subunit inactivates the complex, the fraction of fully active complexes is (1 - f)^n.
(A) Heterozygote with equal expression (f = 1/2): active complexes fall as (1/2)^n with the number of subunits n,
far below the 1/2 of a heterozygote for a null allele (haploinsufficiency line). (B) Active fraction against
the mutant subunit fraction f for monomers, dimers, tetramers and hexamers; the dotted line marks f = 1/2."""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT

fig, ax = bio.canvas(16.0, 7.6)
bio.panel(ax, "A", (0.1, 7.5))
a = charts.axes_at(ax, (1.9, 1.3, 5.6, 5.6))
n = np.arange(1, 9)
a.plot(n, 0.5 ** n, "o-", color=charts.line("negative"), lw=1.6, ms=5, label="dominant negative, (1/2)^n")
a.axhline(0.5, color=charts.line("channel"), lw=1.6, label="null heterozygote, 1/2")
for k in (2, 4):
    a.text(k + 0.15, 0.5 ** k + 0.02, f"1/{2 ** k}", fontsize=FT["tiny"], color=P.ink())
a.set_ylim(0, 1.02)
a.set_xlim(0.7, 8.3)
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(a, "subunits per complex n", "fraction of active complexes")

bio.panel(ax, "B", (8.3, 7.5))
b = charts.axes_at(ax, (10.1, 1.3, 5.6, 5.6))
f = np.linspace(0, 1, 300)
for k, tok in ((1, "neutral"), (2, "channel"), (4, "negative"), (6, "drug")):
    b.plot(f, (1 - f) ** k, color=charts.line(tok), lw=1.6, label=f"n = {k}")
b.axvline(0.5, color=P.muted(), ls=":", lw=0.9)
b.set_xlim(0, 1)
b.set_ylim(0, 1.02)
b.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(b, "fraction of mutant subunits f", "fraction of active complexes")
