"""Feedback control of the branched aspartate pathway in Escherichia coli, and what enzyme multiplicity buys.

A: aspartate is phosphorylated by three aspartokinases (AK I, II, III); aspartate beta-semialdehyde (ASA) is
the branch point to lysine (diaminopimelate pathway; first committed enzyme dihydrodipicolinate synthase,
DHDPS) and, through homoserine dehydrogenase (HDH I, II), to homoserine, which branches to methionine
(homoserine succinyltransferase, MetA) and threonine; threonine dehydratase begins the path from threonine to
isoleucine. Bars: allosteric inhibition by end products (Thr inhibits AK I and HDH I; Lys inhibits AK III and
DHDPS; Met inhibits MetA; Ile inhibits threonine dehydratase). Dashed bars: repression of enzyme synthesis
(Met represses AK II-HDH II). Each end product inhibits the first enzyme after its own branch point
(sequential feedback) and one of the isozymes of the common steps (enzyme multiplicity).
B: relative flux through the aspartokinase step as lysine rises (in units of its inhibition constant), for a
single lysine-sensitive enzyme and for three equal isozymes of which only one is lysine-sensitive (with
threonine low or high); with multiplicity, excess lysine cannot starve the cell of threonine and
methionine.
"""

import numpy as np

import wikibio as bio
from wikibio import charts
from wikibio import metabolism as M

P = bio.P
fig, ax = bio.canvas(28.0, 12.6, scale=0.42)
bio.panel(ax, "A", (0.2, 12.4))
pw = M.Pathway(ax, size="small")
X0 = 2.8
pw.node("asp", (X0, 10.2), "Aspartate", bold=True)
pw.node("asp4p", (X0, 7.4), "Aspartyl-β-P")
pw.node("asa", (X0, 4.6), "Asp β-semialdehyde")
pw.node("lys", (X0, 1.0), "Lysine", token="negative", bold=True)
pw.node("hse", (8.4, 4.6), "Homoserine")
pw.node("met", (8.4, 1.0), "Methionine", token="negative", bold=True)
pw.node("thr", (13.4, 4.6), "Threonine", token="negative", bold=True)
pw.node("akb", (13.4, 7.4), "α-Ketobutyrate")
pw.node("ile", (13.4, 10.2), "Isoleucine", token="negative", bold=True)
pw.step("asp", "asp4p", enzyme="AK I, II, III", side=("ATP", "ADP"), enzyme_offset=0.15, flip=True)
pw.step("asp4p", "asa", side=("NADPH", "NADP⁺ + Pᵢ"), flip=True)
pw.step("asa", "lys", enzyme="DHDPS …", enzyme_offset=0.15, enzyme_flip=True)
pw.step("asa", "hse", enzyme="HDH I, II", side=("NADPH", "NADP⁺"), enzyme_offset=0.15)
pw.step("hse", "met", enzyme="MetA …", enzyme_offset=0.15, enzyme_flip=True)
pw.step("hse", "thr", enzyme="2 steps", enzyme_offset=0.15)
pw.step("thr", "akb", enzyme="Thr dehydratase", side=(None, "NH₃"), enzyme_offset=0.15)
pw.step("akb", "ile", side=("pyruvate", None), flip=True)

NEG = P.edge("negative")


def inh(a, b, bend=0.0, text=None, txy=None, ha="center"):
    bio.arrow(ax, a, b, kind="inhibition", color=NEG, bend=bend, lw=1.4)
    if text:
        bio.label(ax, txy, text, size="tiny", color=NEG, bold=True, ha=ha)


inh((14.6, 10.0), (13.75, 6.0), bend=-0.25, text="Ile ⊣ Thr dehydratase", txy=(15.0, 8.6), ha="left")
inh((12.3, 5.0), (3.3, 8.8), text="Thr ⊣ AK I", txy=(8.4, 7.3))
inh((12.6, 4.15), (5.6, 4.35), bend=0.28, text="Thr ⊣ HDH I", txy=(11.4, 3.45))
inh((1.35, 1.3), (1.35, 8.8), text="Lys ⊣ AK III", txy=(1.15, 5.9), ha="right")
inh((3.9, 1.3), (3.25, 2.7), bend=0.3, text="Lys ⊣ DHDPS", txy=(5.2, 2.0))
inh((9.5, 1.3), (8.85, 2.7), bend=0.3, text="Met ⊣ MetA", txy=(10.8, 2.0))
bio.label(ax, (5.6, 9.6), "AK II, HDH II:\nrepressed by Met", size="tiny", color=NEG)

bio.panel(ax, "B", (17.6, 12.4))
c = charts.axes_at(ax, (19.4, 1.6, 7.8, 9.6))
L = np.logspace(-2, 2, 400)
c.semilogx(L, 1 / (1 + L), color=charts.line("negative"), lw=2.0, label="one Lys-sensitive enzyme")
c.semilogx(L, (1 / (1 + L)) / 3 + 2 / 3, color=charts.line("positive"), lw=2.0,
           label="three isozymes (I: Thr, II: none, III: Lys)")
c.semilogx(L, (1 / (1 + L)) / 3 + (1 / 11) / 3 + 1 / 3, color=charts.line("dna"), lw=2.0, ls="--",
           label="three isozymes, Thr also high")
c.set_ylim(0, 1.05)
c.set_xlim(1e-2, 1e2)
charts.style_axes(c, r"[Lys] / $K_\mathrm{I}$", "relative aspartokinase flux")
c.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="lower left")
