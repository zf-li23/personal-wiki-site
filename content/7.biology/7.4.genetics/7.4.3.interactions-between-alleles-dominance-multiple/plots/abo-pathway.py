"""Biosynthesis of the ABO antigens on red cells (SNFG symbols, type 2 precursor chain).

Precursor Gal(b1-4)GlcNAc -> FUT1 fucosyltransferase (H gene) adds Fuc(a1-2) -> H antigen; the ABO
glycosyltransferase then adds GalNAc(a1-3) (I^A allele, A antigen) or Gal(a1-3) (I^B allele, B antigen);
the i (O) allele has a single-base deletion (frameshift) and makes no active enzyme, so H remains (type O).
hh (Bombay) makes no H antigen and therefore neither A nor B.
"""
import wikibio as bio
from wikibio import glycan as GL

P = bio.P
fig, ax = bio.canvas(25.0, 9.6)
kw = dict(labels=None, size=0.55, aglycone="R")
GL.draw(ax, "Gal(b1-4)GlcNAc(b1-", at=(4.2, 5.0), **kw)
bio.label(ax, (3.0, 6.3), "Precursor", size="normal", bold=True)
GL.abo(ax, (11.4, 5.0), kind="H", **kw)
bio.label(ax, (10.2, 6.3), "H antigen", size="normal", bold=True)
rows = {"A": 8.0, "B": 5.0, "O": 2.0}
GL.abo(ax, (20.0, rows["A"]), kind="A", **kw)
GL.abo(ax, (20.0, rows["B"]), kind="B", **kw)
GL.abo(ax, (20.0, rows["O"]), kind="H", **kw)
for k, t in (("A", "A antigen\n(type A)"), ("B", "B antigen\n(type B)"), ("O", "H unchanged\n(type O)")):
    bio.label(ax, (21.4, rows[k]), t, size="normal", bold=True, ha="left")

bio.arrow(ax, (5.3, 5.0), (7.6, 5.0), kind="process")
bio.label(ax, (6.45, 5.75), "FUT1 (H gene)", size="small")
bio.label(ax, (6.45, 4.35), "+ Fuc", size="small", color=P.muted())
bio.label(ax, (6.45, 2.6), "hh: no H antigen,\nso no A or B\n(Bombay phenotype)", size="small", color=P.edge("negative"))
for k, txt in (("A", "$I^A$ enzyme: + GalNAc"), ("B", "$I^B$ enzyme: + Gal"), ("O", "$i$ (frameshift):\nno active enzyme")):
    end = (15.6, rows[k])
    bio.arrow(ax, (12.9, 5.0), end, kind="process", dashed=k == "O")
    pos = {"A": (13.8, 7.0), "B": (14.7, 5.45), "O": (14.0, 2.7)}[k]
    bio.label(ax, pos, txt, size="small", ha={"A": "right", "B": "center", "O": "right"}[k])
GL.legend(ax, (1.0, 0.9), ["GlcNAc", "Gal", "GalNAc", "Fuc"], cols=4, dx=2.6)
