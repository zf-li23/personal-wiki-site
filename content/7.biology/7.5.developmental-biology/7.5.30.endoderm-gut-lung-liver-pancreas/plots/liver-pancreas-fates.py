"""Liver or pancreas, and the cell types of each (SBGN activity flow, simplified). A: the ventral foregut endoderm,
made competent by the pioneer factors FoxA1/FoxA2 and GATA4/6, becomes liver where FGF from the cardiac mesoderm
and BMP from the septum transversum (with signals from endothelial cells) reach it; the part of the ventral
endoderm out of their range keeps Pdx1 and forms the ventral pancreas. The dorsal pancreas forms where the
notochord (activin, FGF2) represses Shh in the dorsal endoderm. B: the hepatoblast gives hepatocytes (HNF4a,
Wnt, HGF) or, next to the portal vein, cholangiocytes of the bile ducts (Jagged1-Notch, TGF-beta, Sox9).
C: Pdx1-positive pancreatic progenitors segregate into tip cells (Ptf1a, acinar cells) and trunk cells (Nkx6-1,
Sox9), which give duct cells and, through a pulse of Ngn3, the endocrine cells; Pax4 favours beta and delta
cells (MafA marks mature, insulin-secreting beta cells), Arx favours alpha (glucagon) and PP cells."""
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(29, 10.5)


def node(xy, txt, tk, w=2.4, h=0.8, it=False):
    bio.box(ax, xy, w, h, tk, txt, size="tiny", italic=it)


def link(a, b, kind="activation", bend=0.0):
    bio.arrow(ax, a, b, kind=kind, shrink=0.55, bend=bend)


bio.panel(ax, "A", (0.2, 10.3))
node((1.8, 9.0), "cardiac mesoderm:\nFGF", "muscle", 2.8, 1.0)
node((5.6, 9.0), "septum transversum:\nBMP", "drug", 3.0, 1.0)
node((3.7, 6.6), "ventral foregut\n(FoxA1/2, GATA4/6)", "highlight", 3.4, 1.0)
node((1.8, 4.0), "liver\n(Hhex, Prox1)", "drug", 2.6, 1.0)
node((5.6, 4.0), "ventral pancreas\n(Pdx1)", "k", 2.8, 1.0)
node((3.7, 1.0), "dorsal pancreas\n(Pdx1, Ptf1a)", "k", 2.8, 1.0)
node((8.4, 6.6), "notochord", "drug", 1.9, 0.8)
node((8.4, 3.0), "Shh in dorsal\nendoderm", "neutral", 2.4, 1.0)
link((1.8, 8.5), (3.2, 7.1))
link((5.6, 8.5), (4.2, 7.1))
link((3.3, 6.1), (2.2, 4.5))
link((4.1, 6.1), (5.2, 4.5), kind="process")
link((8.4, 6.2), (8.4, 3.5), kind="inhibition")
link((7.2, 2.6), (5.1, 1.3), kind="inhibition")
bio.label(ax, (5.5, 5.4), "out of range", size="tiny", color=P.muted())

bio.panel(ax, "B", (10.4, 10.3))
node((13.0, 8.8), "hepatoblast", "drug", 2.4)
node((11.6, 6.4), "hepatocyte\nHNF4a", "drug", 2.4, 1.0)
node((14.6, 6.4), "cholangiocyte\nSox9, HNF1b", "enzyme", 2.6, 1.0)
link((12.6, 8.4), (11.8, 6.9))
link((13.4, 8.4), (14.3, 6.9))
bio.label(ax, (10.9, 7.7), "Wnt, HGF", size="tiny", color=P.muted())
bio.label(ax, (15.6, 7.8), "Jag1-Notch,\nTGF-beta", size="tiny", color=P.muted())
bio.label(ax, (13.1, 4.9), "near the portal vein:\nductal plate, bile ducts", size="tiny", color=P.muted())

bio.panel(ax, "C", (17.2, 10.3))
N = {"Pdx1+ progenitor": (21.8, 9.2, "k"), "tip (Ptf1a, Cpa1)": (19.2, 7.4, "lipid_head"), "trunk (Nkx6-1, Sox9)": (24.2, 7.4, "enzyme"),
     "acinar": (19.2, 5.4, "lipid_head"), "duct": (22.4, 5.4, "enzyme"), "Ngn3+ endocrine\nprecursor": (25.8, 5.4, "protein"),
     "Pax4": (23.4, 3.4, "protein"), "Arx": (26.8, 3.4, "protein"), "beta (MafA)\ninsulin": (21.4, 1.2, "dna"), "delta\nsomatostatin": (23.8, 1.2, "channel"),
     "alpha\nglucagon": (26.2, 1.2, "receptor"), "PP": (28.2, 1.2, "antibody")}
for k, (x, y, tk) in N.items():
    node((x, y), k, tk, 2.4 if len(k) > 6 else 1.2, 0.95 if "\n" in k else 0.7)
E = [("Pdx1+ progenitor", "tip (Ptf1a, Cpa1)"), ("Pdx1+ progenitor", "trunk (Nkx6-1, Sox9)"), ("tip (Ptf1a, Cpa1)", "acinar"),
     ("trunk (Nkx6-1, Sox9)", "duct"), ("trunk (Nkx6-1, Sox9)", "Ngn3+ endocrine\nprecursor"), ("Ngn3+ endocrine\nprecursor", "Pax4"),
     ("Ngn3+ endocrine\nprecursor", "Arx"), ("Pax4", "beta (MafA)\ninsulin"), ("Pax4", "delta\nsomatostatin"), ("Arx", "alpha\nglucagon"), ("Arx", "PP")]
for a_, b_ in E:
    link(N[a_][:2], N[b_][:2], kind="process")
bio.arrow(ax, (24.2, 3.55), (26.0, 3.55), kind="inhibition", shrink=0.1)
bio.arrow(ax, (26.0, 3.25), (24.2, 3.25), kind="inhibition", shrink=0.1)
