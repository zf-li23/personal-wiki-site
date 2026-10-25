# RNA editing (schematic sequences, illustrative).
# A: guide-RNA-directed U insertion in trypanosome mitochondria. The 5' anchor of a guide RNA pairs with
# already-edited (or never-edited) mRNA just 3' of the site; where the guide has an unpaired A or G, the
# editosome cuts the mRNA, the TUTase adds U from UTP to the 5' fragment to pair with the guide purine (G-U
# pairs allowed), and the RNA ligase rejoins the pieces. Deletion uses the same cut and ligation, with an
# exonuclease removing U residues that have no partner in the guide. Editing proceeds 3' to 5' along the mRNA.
# B: deamination. ADAR converts A to I (read as G) in double-stranded RNA: the glutamine codon CAG of the
# glutamate-receptor GluA2 mRNA becomes CIG, read as CGG (arginine), the Q/R site. APOBEC1 converts C to U:
# codon 2153 of apolipoprotein B mRNA, CAA (Gln), becomes the stop codon UAA in the intestine, giving the
# truncated apoB-48 instead of the liver form apoB-100.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(24.0, 7.6)
dx = 0.42


def seq(x, y, s, token="mrna", bold_idx=(), color_idx=None):
    for i, ch in enumerate(s):
        col = P.edge(token)
        if color_idx and i in color_idx:
            col = P.edge(color_idx[i])
        bio.label(ax, (x + i * dx, y), ch, size="small", bold=(i in bold_idx), color=col)
    return x + len(s) * dx


def pairs(x, y0, y1, idx):
    for i in idx:
        ax.plot([x + i * dx, x + i * dx], [y0, y1], color=P.muted(), lw=0.8)


# --- A ---------------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.45))
bio.label(ax, (5.6, 7.15), "Guide-RNA-directed U insertion", size="small", bold=True)
# step 1: pre-mRNA and gRNA
y = 5.9
m5, m3 = "GGAUC", "GCAAGA"
x1 = seq(0.8, y, m5)
x2 = seq(x1 + 3 * dx, y, m3)
bio.label(ax, (0.35, y), "5′", size="tiny", bold=True)
bio.label(ax, (x2 + 0.15, y), "3′", size="tiny", bold=True)
ax.plot([x1 + 0.35, x1 + 0.75], [y + 0.45, y - 0.45], color=P.edge("negative"), lw=1.0)
bio.label(ax, (x1 + 0.55, y + 0.7), "cut", size="tiny", color=P.edge("negative"))
# guide below, 3'<-5' antiparallel: written 3' ... 5' left to right
g = "CCUAGAAACGUUCU"
gx = 0.8
seq(gx, y - 1.2, "CCUAG", token="trna")
seq(x1, y - 1.2, "AAA", token="trna", bold_idx=(0, 1, 2), color_idx={0: "negative", 1: "negative", 2: "negative"})
seq(x1 + 3 * dx, y - 1.2, "CGUUCU", token="trna")
pairs(0.8, y - 0.3, y - 0.9, range(5))
pairs(x1 + 3 * dx, y - 0.3, y - 0.9, range(6))
bio.label(ax, (0.35, y - 1.2), "3′", size="tiny", bold=True)
bio.label(ax, (x2 + 0.15, y - 1.2), "5′", size="tiny", bold=True)
bio.label(ax, (x2 + 0.6, y - 1.2), "guide RNA (anchor at its 5′ end)", size="tiny", ha="left", color=P.edge("trna"))
bio.label(ax, (x2 + 0.6, y), "pre-mRNA", size="tiny", ha="left", color=P.edge("mrna"))
# step 2: edited
y2 = 2.8
seq(0.8, y2, "GGAUC")
seq(0.8 + 5 * dx, y2, "UUU", bold_idx=(0, 1, 2), color_idx={0: "positive", 1: "positive", 2: "positive"})
seq(0.8 + 8 * dx, y2, "GCAAGA")
seq(0.8, y2 - 1.2, "CCUAGAAACGUUCU", token="trna")
pairs(0.8, y2 - 0.3, y2 - 0.9, range(14))
bio.arrow(ax, (3.2, y - 1.75), (3.2, y2 + 0.55), kind="process")
bio.label(ax, (3.45, (y + y2) / 2 - 0.55), "endonuclease → TUTase (+3 U from UTP) → RNA ligase", size="tiny", ha="left")
bio.label(ax, (7.5, y2 - 2.0), "U deletion: same cut and ligation, U removed by a U-specific exonuclease", size="tiny",
          color=P.muted())

# --- B ---------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (13.6, 7.45))
bio.label(ax, (18.8, 7.15), "Editing by deamination", size="small", bold=True)
y = 5.7
bio.label(ax, (14.0, y + 0.75), "ADAR2: A → I in GluA2 mRNA (Q/R site)", size="small", ha="left")
seq(14.2, y, "…CAG…", color_idx={3: "negative"})
bio.arrow(ax, (16.9, y), (17.9, y), kind="process")
seq(18.2, y, "…CIG…", color_idx={3: "positive"})
bio.label(ax, (21.3, y), "read as CGG: Gln → Arg", size="tiny", ha="left")
bio.label(ax, (14.2, y - 0.75), "needs a double-stranded stem formed with the downstream intron;", size="tiny", ha="left",
          color=P.muted())
bio.label(ax, (14.2, y - 1.2), "edited receptor channels are impermeable to Ca²⁺", size="tiny", ha="left", color=P.muted())
y = 2.6
bio.label(ax, (14.0, y + 0.75), "APOBEC1: C → U in apoB mRNA (codon 2153)", size="small", ha="left")
seq(14.2, y, "…CAA…", color_idx={1: "negative"})
bio.arrow(ax, (16.9, y), (17.9, y), kind="process")
seq(18.2, y, "…UAA…", color_idx={1: "positive"})
bio.label(ax, (21.3, y), "stop: apoB-48 (intestine)", size="tiny", ha="left")
bio.label(ax, (14.2, y - 0.75), "unedited liver mRNA encodes apoB-100 (4536 aa); apoB-48 is its N-terminal 48 %", size="tiny",
          ha="left", color=P.muted())
