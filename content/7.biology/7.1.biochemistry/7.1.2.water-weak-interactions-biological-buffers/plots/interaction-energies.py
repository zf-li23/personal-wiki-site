# Energies of the interactions that hold biomolecules together, on a log scale: typical ranges of the
# net (in water) Gibbs energy of single noncovalent interactions, compared with the thermal energy RT
# at 37 C, the Gibbs energy of ATP hydrolysis in the cell and the dissociation energies of covalent bonds.
import numpy as np
import wikibio as bio
from wikibio import charts as C

rows = [
    ("van der Waals contact", 0.4, 4.0, "neutral"),
    ("hydrophobic effect (per CH$_2$ buried)", 2.5, 4.0, "lipid_tail"),
    ("H bond, neutral groups (net, in water)", 4.0, 6.0, "dna"),
    ("H bond, one group charged", 6.0, 10.0, "dna"),
    ("H bond in liquid water (dissociation)", 20.0, 23.0, "h"),
    ("ion pair (salt bridge) in water", 4.0, 20.0, "positive"),
    ("ATP hydrolysis in the cell", 50.0, 65.0, "atp"),
    ("covalent C–C, C–H, O–H bonds", 348.0, 463.0, "protein"),
]

fig, ax = bio.canvas(16, 8.6)
a = C.axes_at(ax, (7.2, 1.5, 8.3, 6.6))
for i, (name, lo, hi, tok) in enumerate(rows):
    y = len(rows) - 1 - i
    a.barh(y, hi - lo, left=lo, height=0.55, color=bio.P.fill(tok), edgecolor=bio.P.edge(tok), lw=0.9)
RT = 8.314e-3 * 310.15
a.axvline(RT, color=bio.P.muted(), lw=1.0, ls=(0, (4, 3)))
a.text(RT * 1.08, 1.35, "RT at 37 °C\n= 2.6 kJ mol$^{-1}$", fontsize=bio.core.FONT["tiny"], color=bio.P.ink(), va="top")
a.set_xscale("log")
a.set_xlim(0.2, 800)
a.set_ylim(-0.6, len(rows) - 0.3)
a.set_yticks(range(len(rows)), [r[0] for r in rows][::-1])
a.set_xticks([0.3, 1, 3, 10, 30, 100, 300], ["0.3", "1", "3", "10", "30", "100", "300"])
C.style_axes(a, "energy / kJ mol$^{-1}$")
a.tick_params(axis="y", length=0, labelsize=bio.core.FONT["small"])
