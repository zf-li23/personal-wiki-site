# ABC model of floral organ identity (Arabidopsis) and its ABCDE / floral quartet extension.
# A: expression domains of class A, B and C functions over the four whorls (Se, Pe, St, Ca) and the
# organs that result in the wild type and in loss-of-function mutants; A and C repress each other, so
# in an A mutant C spreads outward and in a C mutant A spreads inward (and the flower becomes
# indeterminate). B: the ABCDE model with E (SEPALLATA) required in all organs and D for ovules; the
# MADS-domain protein tetramers proposed by the floral quartet model for each organ.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(30.0, 13.4)

ORG = {"Se": ("Sepal", "sepal"), "Pe": ("Petal", "petal"), "St": ("Stamen", "anther"), "Ca": ("Carpel", "ovary")}
FUN = {"A": "positive", "B": "highlight", "C": "negative"}

bio.panel(ax, "A", (0.2, 13.2))
bio.label(ax, (8.6, 12.9), "ABC model and homeotic mutants", size="normal", bold=True)
X0, W = 4.8, 2.3
for k in range(4):
    bio.label(ax, (X0 + W * (k + 0.5), 12.1), f"Whorl {k + 1}", size="small", color=P.muted())
rows = [
    ("Wild type", {"A": [0, 1], "B": [1, 2], "C": [2, 3]}, ["Se", "Pe", "St", "Ca"]),
    ("ap2 (no A)", {"B": [1, 2], "C": [0, 1, 2, 3]}, ["Ca", "St", "St", "Ca"]),
    ("ap3, pi (no B)", {"A": [0, 1], "C": [2, 3]}, ["Se", "Se", "Ca", "Ca"]),
    ("ag (no C)", {"A": [0, 1, 2, 3], "B": [1, 2]}, ["Se", "Pe", "Pe", "Se"]),
]
for r, (name, dom, organs) in enumerate(rows):
    y = 10.6 - 2.55 * r
    bio.label(ax, (0.4, y + 0.1), name, size="normal", ha="left", italic=(r > 0))
    for j, f in enumerate("ABC"):
        yy = y + 0.75 - 0.42 * j
        bio.label(ax, (X0 - 0.35, yy), f, size="small", bold=True)
        for k in dom.get(f, []):
            bio.box(ax, (X0 + W * (k + 0.5), yy), W - 0.08, 0.34, token=FUN[f], radius=0.05)
    for k, o in enumerate(organs):
        text, tok = ORG[o]
        bio.box(ax, (X0 + W * (k + 0.5), y - 0.65), W - 0.3, 0.62, token=tok, text=text, size="small", radius=0.15)
bio.label(ax, (X0 + 2 * W, 0.55), "ag: the centre keeps producing Se-Pe-Pe (indeterminate flower)", size="small", color=P.muted())

bio.panel(ax, "B", (15.6, 13.2))
bio.label(ax, (22.8, 12.9), "ABCDE model and floral quartets", size="normal", bold=True)
X1, W1 = 18.6, 2.2
cols = [("Sepal", "sepal"), ("Petal", "petal"), ("Stamen", "anther"), ("Carpel", "ovary"), ("Ovule", "ovule")]
for k, (t, tok) in enumerate(cols):
    bio.box(ax, (X1 + W1 * (k + 0.5), 11.9), W1 - 0.2, 0.62, token=tok, text=t, size="small", radius=0.15)
dom = {"A": [0, 1], "B": [1, 2], "C": [2, 3, 4], "D": [4], "E": [0, 1, 2, 3, 4]}
tokf = {"A": "positive", "B": "highlight", "C": "negative", "D": "ovule", "E": "neutral"}
genes = {"A": "AP1, AP2", "B": "AP3, PI", "C": "AG", "D": "STK, SHP", "E": "SEP1-4"}
for j, f in enumerate("ABCDE"):
    y = 10.9 - 0.62 * j
    bio.label(ax, (X1 - 0.35, y), f, size="small", bold=True)
    bio.label(ax, (X1 - 0.75, y), genes[f], size="tiny", ha="right", italic=True, color=P.muted())
    for k in dom[f]:
        bio.box(ax, (X1 + W1 * (k + 0.5), y), W1 - 0.08, 0.4, token=tokf[f], radius=0.05)
quart = [["AP1", "AP1", "SEP", "SEP"], ["AP1", "SEP", "AP3", "PI"], ["AG", "SEP", "AP3", "PI"],
         ["AG", "AG", "SEP", "SEP"], ["STK", "SEP", "AG", "SEP"]]
ptok = {"AP1": "positive", "AP3": "highlight", "PI": "highlight", "AG": "negative", "SEP": "neutral", "STK": "ovule"}
bio.label(ax, (X1 + 2.5 * W1, 7.15), "Floral quartets: tetramers of MADS-domain proteins bound to DNA", size="small",
          color=P.muted())
for k, q in enumerate(quart):
    cx = X1 + W1 * (k + 0.5)
    for i, g in enumerate(q):
        dx = -0.42 if i % 2 == 0 else 0.42
        dy = 5.9 if i < 2 else 5.0
        bio.box(ax, (cx + dx, dy), 0.8, 0.8, token=ptok[g], text=g, size="tiny", radius=0.38)
    ax.plot([cx - 0.95, cx + 0.95], [4.25, 4.25], color=P.edge("dna"), lw=2.2, zorder=9)
    ax.plot([cx - 0.95, cx + 0.95], [4.05, 4.05], color=P.edge("dna2"), lw=2.2, zorder=9)
bio.label(ax, (X1 + 2.5 * W1, 3.4), "DNA (CArG boxes of target genes)", size="tiny", color=P.muted())
bio.label(ax, (X1 + 2.5 * W1, 2.3), "Sepal = A+E;  petal = A+B+E;  stamen = B+C+E;  carpel = C+E;  ovule = C+D+E",
          size="small")
bio.label(ax, (X1 + 2.5 * W1, 1.5), "sep1 sep2 sep3 sep4: all floral organs become leaf-like", size="small", color=P.muted())
