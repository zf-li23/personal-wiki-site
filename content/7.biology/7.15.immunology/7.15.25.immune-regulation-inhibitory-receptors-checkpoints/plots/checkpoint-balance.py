# Costimulatory and coinhibitory receptors set the threshold of T-cell activation.
# At the T cell-APC contact the TCR signal (signal 1) is read together with CD28 (activating; ligands B7),
# CTLA-4 (same B7 ligands, about 10x tighter binding) and PD-1 (ligands PD-L1/PD-L2; recruits SHP-2).
# An antibody against CTLA-4, PD-1 or PD-L1 removes a brake (checkpoint blockade).
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(15, 8)
t = (5.0, 6.8)
bio.shape(ax, bio.blob(t, 4.8, 1.1, wobble=0.015, seed=3), "cytoplasm", zorder=3)
bio.label(ax, (5.0, 6.9), "T cell", size="small")
a = (5.0, 1.1)
bio.shape(ax, bio.blob(a, 4.8, 1.1, wobble=0.015, seed=7), "extracellular", zorder=3)
bio.label(ax, (5.0, 1.1), "antigen-presenting cell", size="small")
cols = [(1.3, "receptor", "TCR", "protein", "pMHC", "link", "signal 1"),
        (3.6, "enzyme", "CD28", "carbohydrate", "B7", "activation", "signal 2"),
        (6.0, "negative", "CTLA-4", "carbohydrate", "B7", "inhibition", "tighter binding"),
        (8.3, "negative", "PD-1", "drug", "PD-L1/2", "inhibition", "SHP-2")]
for x, tk, tn, lk, ln, kind, note in cols:
    bio.protein(ax, (x, 5.2), 1.0, 0.45, tk, text=tn)
    bio.protein(ax, (x, 2.9), 1.0, 0.45, lk, text=ln)
    bio.arrow(ax, (x, 3.3), (x, 4.8), kind=kind)
    bio.label(ax, (x + 0.15, 4.05), note, size="tiny", color=P.muted(), ha="left")
bio.box(ax, (12.9, 5.2), 2.6, 1.2, "positive", text="activation:\nIL-2, proliferation", size="tiny")
bio.arrow(ax, (9.0, 5.2), (11.5, 5.2), kind="process")
bio.label(ax, (10.2, 5.6), "net signal", size="tiny", color=P.muted())
bio.antibody(ax, (12.2, 3.0), size=0.6, angle=0)
bio.label(ax, (12.9, 1.9), "anti-CTLA-4, anti-PD-1,\nanti-PD-L1 block a brake", size="tiny")
