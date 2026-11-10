# Six families of cytokine receptors: topology and the first intracellular partner.
# Extracellular domains above the membrane band, intracellular parts below.
import wikibio as bio
from wikibio import immuno
from matplotlib.patches import Rectangle

P = bio.P
fig, ax = bio.canvas(24.0, 7.2)
YM = 3.5   # membrane centre
ax.add_patch(Rectangle((0.2, YM - 0.22), 23.6, 0.44, facecolor=P.fill("lipid_tail"), edgecolor=P.edge("lipid_tail"), lw=0.8, zorder=2))
bio.label(ax, (0.3, YM + 0.55), "outside", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.3, YM - 0.55), "inside", size="tiny", ha="left", color=P.muted())

W, H = 0.62, 0.46


def chain(x, n_dom, tok, ext_h=H, tm=True):
    """A single-pass chain with n_dom extracellular domains stacked above the membrane."""
    ax.plot([x, x], [YM - 0.2, YM + 0.2], color=P.edge(tok), lw=3.2, zorder=4, solid_capstyle="round")
    for k in range(n_dom):
        immuno.domain(ax, (x, YM + 0.45 + k * (ext_h + 0.05)), W, ext_h, tok)
    return YM + 0.45 + (n_dom - 1) * (ext_h + 0.05) + ext_h / 2


def below(x, tok, text, h=0.5, w=0.9, y=None):
    y0 = YM - 0.25 - h / 2 - (0 if y is None else y)
    bio.box(ax, (x, y0), w, h, tok, text, size="tiny", radius=0.1)
    return y0


def title(x, t, ex):
    bio.label(ax, (x, 6.55), t, size="normal", bold=True)
    bio.label(ax, (x, 0.3), ex, size="tiny", color=P.muted())


# 1  type I
x = 2.2
top = chain(x - 0.75, 1, "channel"); chain(x, 2, "enzyme"); chain(x + 0.75, 2, "positive")
immuno.cytokine(ax, (x, YM + 1.95), "drug", r=0.22)
bio.box(ax, (x + 0.75, YM - 0.5), 0.7, 0.5, "negative", "JAK3", size="tiny", radius=0.1)
bio.box(ax, (x, YM - 0.5), 0.7, 0.5, "dna2", "JAK1", size="tiny", radius=0.1)
bio.label(ax, (x, YM - 1.3), "STAT5", size="tiny")
bio.arrow(ax, (x, YM - 0.8), (x, YM - 1.1), kind="process")
title(x, "Type I\n(haematopoietin)", "IL-2R: α, β, common γ chain")
# 2  type II
x = 6.1
chain(x - 0.45, 2, "enzyme"); chain(x + 0.45, 2, "positive")
immuno.cytokine(ax, (x, YM + 1.95), "drug", r=0.22)
bio.box(ax, (x - 0.45, YM - 0.5), 0.7, 0.5, "dna2", "JAK1", size="tiny", radius=0.1)
bio.box(ax, (x + 0.45, YM - 0.5), 0.7, 0.5, "drug", "TYK2", size="tiny", radius=0.1)
bio.label(ax, (x, YM - 1.3), "STAT1 / STAT2", size="tiny")
bio.arrow(ax, (x, YM - 0.8), (x, YM - 1.1), kind="process")
title(x, "Type II\n(interferon, IL-10)", "IFNAR1/IFNAR2, IFNGR1/2")
# 3  IL-1 / Toll (TIR)
x = 10.0
chain(x - 0.45, 3, "channel"); chain(x + 0.45, 3, "enzyme")
immuno.cytokine(ax, (x, YM + 2.1), "drug", r=0.22)
bio.box(ax, (x - 0.45, YM - 0.5), 0.7, 0.5, "receptor", "TIR", size="tiny", radius=0.1)
bio.box(ax, (x + 0.45, YM - 0.5), 0.7, 0.5, "receptor", "TIR", size="tiny", radius=0.1)
bio.label(ax, (x, YM - 1.3), "MyD88 → NF-κB", size="tiny")
bio.arrow(ax, (x, YM - 0.8), (x, YM - 1.1), kind="process")
title(x, "IL-1 / Toll\n(TIR)", "IL-1R, IL-18R, Toll-like receptors")
# 4  TNFR trimer
x = 13.9
for dx in (-0.7, 0, 0.7):
    chain(x + dx, 3, "positive", ext_h=0.36)
    bio.box(ax, (x + dx, YM - 0.5), 0.55, 0.5, "negative", "DD", size="tiny", radius=0.1)
for dx in (-0.7, 0, 0.7):
    immuno.cytokine(ax, (x + dx, YM + 2.2 + (0.18 if dx == 0 else 0)), "drug", r=0.2)
bio.label(ax, (x, YM - 1.3), "TRADD, FADD, TRAF", size="tiny")
bio.arrow(ax, (x, YM - 0.8), (x, YM - 1.1), kind="process")
title(x, "TNF receptor\nfamily", "TNFR1, TNFR2, Fas, CD40")
# 5  chemokine GPCR
x = 17.8
for k in range(7):
    xx = x - 0.9 + k * 0.3
    ax.add_patch(Rectangle((xx - 0.1, YM - 0.45), 0.2, 0.9, facecolor=P.fill("receptor"), edgecolor=P.edge("receptor"), lw=0.7, zorder=4))
immuno.cytokine(ax, (x, YM + 1.2), "drug", r=0.22)
bio.box(ax, (x, YM - 1.05), 2.1, 0.5, "enzyme", "Gαi · Gβγ", size="tiny", radius=0.1)
bio.label(ax, (x, YM - 1.7), "Ca²⁺, PI3K, cell migration", size="tiny")
title(x, "Chemokine\nreceptor (GPCR)", "CCR7, CXCR4, CXCR5, CCR2")
# 6  TGF-beta receptors
x = 21.7
chain(x - 0.45, 1, "enzyme"); chain(x + 0.45, 1, "positive")
immuno.cytokine(ax, (x - 0.2, YM + 1.2), "drug", r=0.2); immuno.cytokine(ax, (x + 0.2, YM + 1.2), "drug", r=0.2)
bio.box(ax, (x - 0.45, YM - 0.5), 0.7, 0.5, "enzyme", "II", size="tiny", radius=0.1)
bio.box(ax, (x + 0.45, YM - 0.5), 0.7, 0.5, "positive", "I", size="tiny", radius=0.1)
bio.arrow(ax, (x - 0.1, YM - 0.5), (x + 0.1, YM - 0.5), kind="process")
bio.label(ax, (x, YM - 1.3), "SMAD2/3 → SMAD4", size="tiny")
bio.arrow(ax, (x + 0.45, YM - 0.8), (x + 0.1, YM - 1.1), kind="process")
title(x, "TGF-β receptor\nfamily", "TGF-β RII / RI (Ser/Thr kinases)")
