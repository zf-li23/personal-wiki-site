# Where self-tolerance is enforced: central tolerance, peripheral tolerance and antigen sequestration.
import wikibio as bio
from wikibio import immuno

P = bio.P
fig, ax = bio.canvas(28, 12.4)

cols = [(4.7, 9.3, "A  Central tolerance", "thymus (T cells), bone marrow (B cells)"),
        (14.0, 9.3, "B  Peripheral tolerance", "lymph nodes, spleen, tissues"),
        (23.3, 9.3, "C  Evasion", "sequestration and immune privilege")]
for x, w, title, sub in cols:
    bio.box(ax, (x, 6.2), w, 11.2, "cytoplasm", radius=0.3, zorder=1)
    bio.label(ax, (x, 11.2), title, size="title", bold=True)
    bio.label(ax, (x, 10.55), sub, size="small", color=P.muted())

def outcome(x, y, token, text, w=3.5, h=1.5):
    bio.box(ax, (x, y), w, h, token, text=text, size="tiny")

# A: immature lymphocyte meets self antigen strongly
immuno.immune_cell(ax, (4.7, 9.2), r=0.55, token="cd4", seed=21)
bio.label(ax, (5.5, 9.2), "immature lymphocyte,\nstrong self-recognition", size="tiny", ha="left")
for (x, y, tok, txt) in [(2.75, 6.1, "negative", "Deletion\n(apoptosis)"), (6.65, 6.1, "highlight", "Receptor editing\n(B cells)"),
                         (2.75, 3.6, "positive", "Thymic Treg\n(T cells)"), (6.65, 3.6, "neutral", "Anergy\n(B cells)")]:
    outcome(x, y, tok, txt)
    bio.arrow(ax, (4.7, 8.5), (x, y + 0.8), kind="process", bend=0.1 if x < 4.7 else -0.1)
bio.label(ax, (4.7, 1.9), "weak or no self-recognition: the cell matures\nand leaves (positive selection)", size="tiny", color=P.muted())
bio.label(ax, (4.7, 1.0), "AIRE-driven self antigens in the thymic medulla", size="tiny", color=P.muted())

# B: escaped cell meets self antigen on an immature DC
immuno.immune_cell(ax, (11.6, 9.2), r=0.5, kind="dendritic", token="receptor", seed=22)
immuno.immune_cell(ax, (14.6, 9.2), r=0.5, token="cd8", seed=23)
bio.label(ax, (11.6, 8.3), "immature DC,\nself antigen,\nno costimulation", size="tiny", va="top")
bio.label(ax, (16.2, 9.2), "escaped\nnaive cell", size="tiny", ha="left")
for (x, y, tok, txt) in [(12.05, 6.1, "neutral", "Ignorance\n(low antigen,\nlow affinity)"), (15.95, 6.1, "enzyme", "Anergy\n(signal 1 without 2)"),
                         (12.05, 3.6, "negative", "Deletion\n(Fas, Bim)"), (15.95, 3.6, "positive", "Suppression\n(Treg, IL-10, TGF-β)")]:
    outcome(x, y, tok, txt)
    bio.arrow(ax, (14.6, 8.5), (x, y + 0.8), kind="process", bend=0.1 if x < 14.6 else -0.1)
bio.label(ax, (14.0, 1.9), "the same cell may be activated if antigen is\ndelivered with danger signals", size="tiny", color=P.muted())

# C: barrier between lymphocytes and antigen
immuno.immune_cell(ax, (20.5, 9.2), r=0.5, token="cd4", seed=24)
bio.box(ax, (22.3, 9.2), 0.4, 2.4, "membrane", zorder=5)
bio.label(ax, (22.3, 7.75), "barrier", size="tiny")
bio.protein(ax, (24.6, 9.2), 1.5, 1.0, "enzyme", text="self Ag")
bio.arrow(ax, (21.2, 9.2), (21.9, 9.2), kind="inhibition")
outcome(23.3, 6.1, "neutral", "Sequestration\n(little lymphatic drainage)", w=7.2)
outcome(23.3, 3.6, "positive", "Active suppression\n(TGF-β, FasL, Treg)", w=7.2)
bio.label(ax, (23.3, 1.9), "eye, testis, brain, placenta: relative, not absolute", size="tiny", color=P.muted())
