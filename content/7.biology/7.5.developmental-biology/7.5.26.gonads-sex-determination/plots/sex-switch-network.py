"""Gene network of primary sex determination in the supporting cells of the gonad (activity flow)."""
import wikibio as bio

fig, ax = bio.canvas(22, 10.5)
P = bio.P
B = {"bip": (3.0, 8.8, "SF1, WT1(+KTS),\nGATA4, CBX2", "neutral", 3.6, 1.2), "sry": (3.0, 6.2, "SRY", "receptor", 2.0, 0.9),
     "sox9": (8.0, 6.2, "SOX9", "enzyme", 2.2, 0.9), "fgf9": (8.0, 9.0, "FGF9 / FGFR2", "dna2", 2.8, 0.9),
     "pgd2": (12.0, 8.4, "PGD2 (paracrine)", "dna2", 3.0, 0.9), "amh": (8.0, 3.4, "AMH", "enzyme", 2.0, 0.9),
     "wnt4": (16.5, 9.0, "WNT4, RSPO1", "receptor", 2.8, 0.9), "bcat": (16.5, 6.2, "beta-catenin", "receptor", 2.6, 0.9),
     "foxl2": (20.0, 6.2, "FOXL2", "receptor", 2.0, 0.9), "gran": (17.5, 3.4, "granulosa fate\n(follistatin)", "receptor", 3.2, 1.2),
     "sert": (12.0, 3.4, "Sertoli fate", "enzyme", 2.6, 0.9), "dmrt1": (12.0, 1.0, "adult: DMRT1 vs FOXL2", "highlight", 4.2, 0.9)}
for k, (x, y, t, tok, w, h) in B.items():
    bio.box(ax, (x, y), w, h, token=tok, text=t, size="small", italic=k in ("sry",))
A = lambda p, q, kind="activation", bend=0.0: bio.arrow(ax, p, q, kind=kind, bend=bend)
A((3.0, 8.15), (3.0, 6.7))
A((4.05, 6.2), (6.85, 6.2))
bio.label(ax, (5.45, 6.55), "Enh13, TESCO", size="tiny", color=P.muted())
A((7.5, 6.7), (7.5, 8.5))
A((8.5, 8.5), (8.5, 6.7))
A((8.9, 6.65), (10.6, 7.95))
A((10.6, 8.2), (9.15, 6.75), bend=-0.2)
A((8.0, 5.7), (8.0, 3.9))
A((9.1, 5.85), (11.0, 3.9))
A((9.4, 9.0), (15.05, 9.0), kind="inhibition")
A((16.5, 8.5), (16.5, 6.7))
A((15.15, 6.0), (9.15, 6.0), kind="inhibition", bend=0.12)
A((20.0, 5.7), (18.6, 4.05))
A((16.5, 5.7), (17.0, 4.05))
A((20.0, 5.7), (8.6, 5.7), kind="inhibition", bend=0.3)
bio.label(ax, (13.4, 6.45), "mutual repression", size="tiny", color=P.muted())
bio.label(ax, (3.0, 10.1), "bipotential gonad", size="tiny", color=P.muted())
bio.label(ax, (8.0, 10.1), "testis pathway (XY)", size="tiny", color=P.muted())
bio.label(ax, (17.8, 10.1), "ovary pathway (XX)", size="tiny", color=P.muted())
