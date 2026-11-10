# Hematopoietic lineages of immune cells (simplified tree) with the main lineage-determining
# transcription factors next to each branch. Myeloid branch in warm tokens, lymphoid branch in cool ones.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25.0, 11.5)


def node(xy, text, tok, w=2.1, h=0.75, size="small"):
    bio.box(ax, xy, w, h, token=tok, text=text, size=size)
    return xy


def edge(a, b, tf=None, dashed=False, frac=0.5, off=(0.0, 0.25)):
    bio.arrow(ax, (a[0], a[1] - 0.42), (b[0], b[1] + 0.42), kind="process", head=0.15, dashed=dashed)
    if tf:
        x = a[0] + (b[0] - a[0]) * frac + off[0]
        y = a[1] - 0.42 + (b[1] - a[1] + 0.84) * frac + off[1]
        bio.label(ax, (x, y), tf, size="tiny", color=P.muted())


hsc = node((12.5, 10.6), "HSC", "highlight", w=1.8)
mpp = node((12.5, 8.9), "MPP", "neutral", w=1.8)
edge(hsc, mpp)
cmp_ = node((6.5, 7.1), "CMP (myeloid)", "drug", w=2.8)
clp = node((19.0, 7.1), "CLP (lymphoid)", "dna", w=2.8)
edge(mpp, cmp_, "PU.1 high", off=(-0.9, 0.1))
edge(mpp, clp, "PU.1 low, Ikaros", off=(1.1, 0.1))
mep = node((2.0, 5.2), "MEP", "blood", w=1.6)
gmp = node((8.0, 5.2), "GMP", "drug", w=1.6)
edge(cmp_, mep, "GATA1", off=(-0.6, 0))
edge(cmp_, gmp, "C/EBPα", off=(0.7, 0))
# MEP progeny
ery = node((1.1, 2.4), "erythrocyte", "blood", w=1.8, size="tiny")
meg = node((3.2, 2.4), "megakaryocyte\n→ platelets", "blood", w=2.0, h=0.95, size="tiny")
edge(mep, ery)
edge(mep, meg)
# GMP progeny
neu = node((5.2, 2.4), "neutrophil", "drug", w=1.7, size="tiny")
eos = node((7.0, 2.4), "eosinophil", "drug", w=1.7, size="tiny")
bas = node((8.8, 2.4), "basophil /\nmast cell", "drug", w=1.7, h=0.95, size="tiny")
mdp = node((11.6, 3.9), "MDP", "antibody", w=1.4)
edge(gmp, neu, "C/EBPε", off=(-0.6, 0))
edge(gmp, eos, "GATA1", off=(-0.25, -0.35))
edge(gmp, bas, "GATA2", off=(0.7, 0))
edge(gmp, mdp, "IRF8", off=(0.4, 0.3))
mono = node((10.8, 1.75), "monocyte", "antibody", w=1.7, size="tiny")
cdp = node((13.4, 1.75), "CDP", "antibody", w=1.4, size="tiny")
edge(mdp, mono, "KLF4", off=(-0.75, 0))
edge(mdp, cdp, off=(0, 0))
mac = node((10.8, 0.45), "macrophage, moDC", "antibody", w=2.4, h=0.6, size="tiny")
bio.arrow(ax, (10.8, 1.33), (10.8, 0.77), kind="process", head=0.12)
cdc = node((14.6, 0.45), "cDC1 (BATF3), cDC2 (IRF4)", "antibody", w=3.4, h=0.6, size="tiny")
bio.arrow(ax, (13.6, 1.33), (14.2, 0.77), kind="process", head=0.12)
# lymphoid progeny
pdc = node((16.4, 3.3), "pDC (E2-2)", "channel", w=1.9, size="tiny")
tp = node((18.8, 4.7), "T precursor", "channel", w=1.9, size="tiny")
bc = node((21.3, 4.7), "B cell", "channel", w=1.6, size="tiny")
ilc = node((23.6, 4.7), "NK cell, ILC", "channel", w=1.8, size="tiny")
edge(clp, pdc, dashed=True)
bio.arrow(ax, (13.9, 2.15), (15.9, 2.95), kind="process", head=0.12, dashed=True)
edge(clp, tp, off=(0, 0))
edge(clp, bc, "E2A, EBF1, PAX5", off=(1.6, 0.2))
edge(clp, ilc, "Id2, NFIL3", off=(1.1, 0.0))
thy = node((18.8, 2.4), "thymus: αβ and γδ\nT cells (Notch1,\nTCF-1, GATA3, BCL11B)", "dna2", w=3.0, h=1.4, size="tiny")
bio.arrow(ax, (18.8, 4.28), (18.8, 3.12), kind="process", head=0.14)
pc = node((21.6, 2.4), "plasma cell", "channel", w=1.8, size="tiny")
bio.arrow(ax, (21.4, 4.28), (21.55, 2.82), kind="process", head=0.12)
bio.label(ax, (5.5, 0.45), "Myeloid", size="title", bold=True, color=P.edge("drug"))
bio.label(ax, (22.8, 0.75), "Lymphoid", size="title", bold=True, color=P.edge("dna"))
