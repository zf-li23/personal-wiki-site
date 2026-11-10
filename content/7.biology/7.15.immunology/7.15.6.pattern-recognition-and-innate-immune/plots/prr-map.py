# Map of pattern-recognition receptors in a cell and their signalling (SBGN-style activity flow):
# plasma-membrane TLRs (MyD88 -> NF-kB), endosomal TLRs (TRIF -> IRF3; MyD88 -> IRF7), cytosolic RLRs
# (MAVS on mitochondria), cGAS-STING (ER), NOD1/2 (RIPK2), and the NLRP3 inflammasome (caspase-1).
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 12.0)
bio.cell(ax, (12.0, 5.6), 11.6, 5.4, kind="animal", seed=7)
bio.label(ax, (12.0, 11.7), "Extracellular: bacteria, fungi", size="small", bold=True)
bio.nucleus(ax, (12.0, 2.3), 2.0, pores=10, nucleolus=False, chromatin=False)


def B(xy, text, tok="protein", w=1.9, h=0.62, size="tiny"):
    bio.box(ax, xy, w, h, token=tok, text=text, size=size, zorder=20)
    return xy


def A(a, b, kind="activation"):
    bio.arrow(ax, a, b, kind=kind, head=0.16, zorder=19)


# plasma membrane TLR4 / TLR2 / TLR5
t4 = B((4.0, 10.4), "TLR4 · TLR2 · TLR5", "receptor", w=3.0)
my = B((4.0, 8.9), "MyD88", "enzyme")
ir = B((4.0, 7.7), "IRAK4 · TRAF6", "enzyme", w=2.4)
tak = B((4.0, 6.5), "TAK1 → IKK", "enzyme", w=2.4)
A((4.0, 10.08), (4.0, 9.22)); A((4.0, 8.58), (4.0, 8.02)); A((4.0, 7.38), (4.0, 6.82))
# endosome
bio.vesicle(ax, (8.9, 8.2), 1.35, token="vesicle")
bio.label(ax, (8.9, 9.75), "endosome", size="tiny")
e3 = B((8.4, 8.6), "TLR3 · TLR4", "receptor", w=1.9)
e7 = B((9.4, 7.8), "TLR7 · 9", "receptor", w=1.5)
trif = B((7.5, 6.3), "TRIF", "enzyme", w=1.3)
A((8.2, 8.28), (7.6, 6.62))
A((8.7, 7.48), (5.2, 6.65))
# mitochondrion with MAVS, RIG-I
bio.mitochondrion(ax, (16.0, 9.0), 2.6, 0.9, angle=-10)
rig = B((16.0, 10.4), "RIG-I · MDA5 (RNA)", "receptor", w=3.0)
mavs = B((16.0, 8.0), "MAVS", "enzyme", w=1.3)
A((16.0, 10.08), (16.0, 8.32))
# ER with STING, cGAS
bio.er(ax, (20.2, 7.7), 2.4, 1.4, sheets=3)
cg = B((20.2, 10.1), "cGAS (DNA) → cGAMP", "receptor", w=3.1)
st = B((20.2, 7.0), "STING", "enzyme", w=1.3)
A((20.2, 9.78), (20.2, 7.32))
# TBK1 -> IRF3
tbk = B((14.0, 5.9), "TBK1", "enzyme", w=1.3)
A((7.95, 6.25), (13.35, 5.95)); A((16.0, 7.68), (14.4, 6.22)); A((19.6, 6.8), (14.65, 6.0))
# NOD1/2 and NLRP3
nod = B((19.8, 4.6), "NOD1 · NOD2 → RIPK2", "receptor", w=3.2)
nl = B((20.0, 3.1), "NLRP3 · ASC · caspase-1", "highlight", w=3.6)
A((18.2, 4.6), (5.25, 6.35))
bio.label(ax, (20.0, 2.45), "IL-1β, IL-18 maturation;\ngasdermin D pores (pyroptosis)", size="tiny", va="top")
# nuclear outputs
nf = B((10.6, 3.0), "NF-κB · AP-1", "dna", w=2.2)
irf = B((13.4, 3.0), "IRF3 · IRF7", "dna", w=2.0)
A((4.0, 6.18), (9.6, 3.3))
A((14.0, 5.58), (13.5, 3.32))
A((9.7, 7.48), (12.6, 3.3))
bio.label(ax, (10.6, 1.6), "TNF, IL-1β, IL-6,\nIL-12, chemokines", size="tiny")
bio.label(ax, (13.6, 1.6), "type I interferons", size="tiny")
bio.label(ax, (4.0, 11.25), "plasma membrane", size="tiny", color=P.muted())
bio.label(ax, (17.7, 0.6), "Cytosol", size="small", bold=True)
