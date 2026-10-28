"""Autotetraploid segregation. A: pairing of four homologues as two bivalents or as a quadrivalent
(partner exchange). B: gametes of a duplex AAaa as functions of the double-reduction rate alpha
(cytogenetics.tetrasomic_gametes): from 1:4:1 under random chromosome segregation (alpha = 0) to 3:8:3
under random chromatid segregation (alpha = 1/7). C: fraction of recessive aaaa offspring on selfing a
duplex (f_aa squared) and of a simplex Aaaa, with a simulation of 20 000 gametes at three values of alpha."""
import numpy as np
import wikibio as bio
from wikibio import charts, cytogenetics as C

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(26, 8.4)
bio.panel(ax, "A", (0.2, 8.2))
C.polyploid_pairing(ax, (3.6, 5.9), "bivalents", length=3.6, alleles=["A", "A", "a", "a"])
bio.label(ax, (3.6, 4.4), "two bivalents", size="small", color=P.muted())
C.polyploid_pairing(ax, (3.6, 2.2), "quadrivalent", length=3.6, alleles=["A", "A", "a", "a"])
bio.label(ax, (3.6, 0.55), "quadrivalent", size="small", color=P.muted())
bio.panel(ax, "B", (7.4, 8.2))
al = np.linspace(0, 1 / 7, 100)
pb = charts.axes_at(ax, (9.0, 1.3, 7.0, 6.2))
f = np.array([[C.tetrasomic_gametes(2, a)[k] for k in (2, 1, 0)] for a in al])
for k, (lab, tok) in enumerate((("AA", "dna"), ("Aa", "enzyme"), ("aa", "receptor"))):
    pb.plot(al, f[:, k], color=charts.line(tok), lw=1.5, ls="-" if k != 2 else "--", label=f"${lab}$ gametes")
pb.set_xlim(0, 1 / 7)
pb.set_xticks([0, 0.05, 0.1, 1 / 7], ["0", "0.05", "0.10", "1/7"])
charts.style_axes(pb, "double-reduction rate α", "gamete frequency (duplex AAaa)")
pb.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
bio.panel(ax, "C", (17.0, 8.2))
pc = charts.axes_at(ax, (18.7, 1.3, 6.8, 6.2))
pc.plot(al, [C.tetrasomic_gametes(2, a)[0] ** 2 for a in al], color=charts.line("dna"), lw=1.5, label="duplex selfed")
pc.plot(al, [C.tetrasomic_gametes(1, a)[0] ** 2 for a in al], color=charts.line("receptor"), lw=1.5, label="simplex selfed")
for a in (0, 1 / 14, 1 / 7):
    for dose, tok in ((2, "dna"), (1, "receptor")):
        g = C.tetrasomic_gametes(dose, a)
        n = 20000
        draws = rng.choice(3, size=(n, 2), p=[g[0], g[1], g[2]])
        pc.plot(a, np.mean((draws == 0).all(axis=1)), "o", mfc="none", color=charts.line(tok), ms=4)
pc.set_xlim(-0.005, 1 / 7 + 0.005)
pc.set_xticks([0, 0.05, 0.1, 1 / 7], ["0", "0.05", "0.10", "1/7"])
charts.style_axes(pc, "double-reduction rate α", "recessive offspring")
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="center right")
