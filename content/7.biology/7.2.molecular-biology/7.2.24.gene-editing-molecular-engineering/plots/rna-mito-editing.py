# Editing RNA with endogenous ADAR, and editing mitochondrial DNA with protein targeting.
# A: a guide RNA pairs with the transcript and places a cytidine opposite the target adenosine; the A-C
#    mismatch is the substrate ADAR1 prefers, and deamination gives inosine, read as guanosine (UAG -> UGG).
# B: editing efficiency against guide length, linear and circular guides.
# C: the reporter: an in-frame UAG between two fluorescent proteins.
# D: why mitochondria need protein targeting - guide RNA is not imported; TALE arrays are.
# E: the two mitochondrial architectures: a split double-strand-specific deaminase, and a strand-selective
#    nickase-deaminase pair.
# F: heteroplasmy and the threshold: correcting a fifth of the genomes can cross it.
import numpy as np
import wikibio as bio
from wikibio import quant as Q

P = bio.P
fig, ax = bio.canvas(25.0, 13.6)

NEG = P.edge("negative")

# ----------------------------------------------------------------- A: ADAR recruitment
bio.panel(ax, "A", (0.1, 13.4))
bio.label(ax, (6.0, 13.4), "A guide RNA that recruits the cell's own ADAR", size="small", bold=True)
yA = 11.0
x0, n, dx = 1.6, 22, 0.42
ax.plot([x0, x0 + n * dx], [yA, yA], color=P.edge("mrna"), lw=2.4, zorder=6)
ax.plot([x0 + 2 * dx, x0 + (n - 2) * dx], [yA - 0.8, yA - 0.8], color=P.edge("rna"), lw=2.4, zorder=6)
for i in range(3, n - 2):
    if i != 11:
        ax.plot([x0 + i * dx, x0 + i * dx], [yA - 0.08, yA - 0.72], color=P.muted(), lw=0.7, zorder=5)
bio.label(ax, (x0 - 0.25, yA), "5′", size="tiny", ha="right", color=P.edge("mrna"))
bio.label(ax, (x0 + n * dx + 0.25, yA), "3′", size="tiny", ha="left", color=P.edge("mrna"))
bio.label(ax, (x0 + 3 * dx, yA + 0.45), "target mRNA", size="tiny", color=P.edge("mrna"))
bio.label(ax, (x0 + 11 * dx, yA - 1.3), "guide RNA, 100–150 nt", size="tiny", color=P.edge("rna"))
for xy, text, tok in (((x0 + 11 * dx, yA), "A", "negative"), ((x0 + 11 * dx, yA - 0.8), "C", "highlight")):
    ax.add_patch(bio.core.Circle(xy, 0.21, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.9, zorder=12))
    bio.label(ax, xy, text, size="tiny", color=P.on_fill(), zorder=13)
bio.label(ax, (x0 + 14.6 * dx, yA - 0.4), "A–C mismatch", size="tiny", ha="left", color=P.edge("highlight"))
bio.shape(ax, bio.blob((x0 + 11 * dx, yA + 1.6), 1.5, 0.55, wobble=0.05, seed=2), token="enzyme", zorder=9)
bio.label(ax, (x0 + 11 * dx, yA + 1.6), "endogenous ADAR1", size="tiny", color=P.on_fill(), zorder=10)
bio.arrow(ax, (x0 + 11 * dx, yA + 1.0), (x0 + 11 * dx, yA + 0.35), kind="catalysis", color=P.muted())
bio.label(ax, (x0 + 17 * dx, yA + 1.6), "no exogenous protein\nis delivered", size="tiny", ha="left",
          color=P.ink())
bio.label(ax, (6.0, 8.95), "A → I by hydrolytic deamination; the ribosome reads I as G, so UAG becomes UGG (Trp)",
          size="tiny", color=P.muted())

# ----------------------------------------------------------------- C: the reporter
bio.panel(ax, "C", (0.1, 8.55))
bio.label(ax, (6.0, 8.55), "The reporter that makes editing countable", size="small", bold=True)
y = 7.4
bio.box(ax, (2.9, y), 2.4, 0.72, token="negative", text="mCherry", size="tiny", radius=0.1)
bio.box(ax, (4.9, y), 1.1, 0.72, token="neutral", text="UAG", size="tiny", radius=0.1)
bio.box(ax, (7.2, y), 2.4, 0.72, token="positive", text="EGFP", size="tiny", radius=0.1)
bio.arrow(ax, (5.6, y - 0.75), (5.6, y - 1.5), kind="process")
bio.label(ax, (6.0, y - 1.1), "editing", size="tiny", ha="left", color=P.muted())
bio.box(ax, (2.9, y - 1.9), 2.4, 0.72, token="negative", text="mCherry", size="tiny", radius=0.1)
bio.box(ax, (4.9, y - 1.9), 1.1, 0.72, token="highlight", text="UGG", size="tiny", radius=0.1)
bio.box(ax, (7.2, y - 1.9), 2.4, 0.72, token="positive", text="EGFP", size="tiny", radius=0.1)
bio.label(ax, (6.0, y - 2.7), "green cells = edited transcripts; the read-out is a fraction, not a yes or no",
          size="tiny", color=P.muted())

# ----------------------------------------------------------------- B: length and circularization
bio.panel(ax, "B", (0.1, 4.3))
bio.label(ax, (6.0, 4.3), "Guide length and circularization", size="small", bold=True)
L = np.array([51.0, 71, 111, 151])
lin = np.array([0.03, 0.10, 0.22, 0.26])
circ = np.array([0.10, 0.26, 0.45, 0.50])
pl = Q.Plot(ax, (2.2, 0.9, 7.2, 2.7), xlim=(40, 165), ylim=(0, 0.6),
            xlabel="guide length / nt", ylabel="fraction of transcripts edited",
            xticks=[51, 71, 111, 151], yticks=[0, 0.3, 0.6], ylabel_offset=1.0)
pl.line(L, lin, "rna", text="linear guide", at=0.72, dy=-0.5)
pl.points(L, lin, "rna", r=0.08)
pl.line(L, circ, "positive", text="circular guide", at=0.5, dy=0.45)
pl.points(L, circ, "positive", r=0.08)
bio.label(ax, (11.0, 2.2), "a circle has no free ends,\nso exonucleases (7.2.18)\ncannot start on it:\nmore editing, "
          "longer,\nat a lower dose", size="tiny", ha="left", color=P.ink())

# ----------------------------------------------------------------- D: why mitochondria are different
bio.panel(ax, "D", (13.2, 13.4))
bio.label(ax, (19.4, 13.4), "Why mitochondrial editing needs protein targeting", size="small", bold=True)
yD = 10.8
bio.bilayer(ax, [(15.0, yD + 1.1), (23.4, yD + 1.1)])
bio.bilayer(ax, [(15.0, yD), (23.4, yD)])
bio.label(ax, (14.7, yD + 1.1), "outer", size="tiny", ha="right", color=P.muted())
bio.label(ax, (14.7, yD), "inner", size="tiny", ha="right", color=P.muted())
bio.label(ax, (19.2, yD - 0.75), "matrix: mitochondrial DNA", size="tiny", color=P.muted())
bio.dna(ax, (17.2, yD - 1.35), (21.2, yD - 1.35), style="duplex")
# guide RNA blocked
ax.plot([16.6, 16.6], [yD + 1.95, yD + 1.6], color=P.edge("rna"), lw=2.4, zorder=8)
bio.label(ax, (16.6, yD + 2.25), "guide RNA", size="tiny", color=P.edge("rna"))
bio.arrow(ax, (16.6, yD + 1.55), (16.6, yD + 1.32), kind="inhibition", color=NEG)
bio.label(ax, (17.1, yD + 1.78), "not imported", size="tiny", ha="left", color=NEG)
# TALE protein imported
bio.protein(ax, (21.6, yD + 2.1), 1.9, 0.58, token="protein", text="TALE fusion", size="tiny")
bio.arrow(ax, (21.6, yD + 1.75), (21.6, yD - 0.95), kind="process", color=P.edge("positive"))
bio.label(ax, (24.1, yD - 1.05), "imported with\na presequence", size="tiny", ha="right",
          color=P.edge("positive"))

# ----------------------------------------------------------------- E: the two architectures
bio.panel(ax, "E", (13.2, 8.1))
bio.label(ax, (19.4, 8.1), "Two mitochondrial architectures", size="small", bold=True)
for k, (title, note, tok) in enumerate((
        ("split double-strand deaminase", "halves reassemble only where both arrays bind;\nedits C on both strands in the window", "negative"),
        ("strand-selective nickase + deaminase", "the nick decides which strand is edited and repaired;\nhigh purity, either C→T or A→G", "positive"))):
    y = 7.0 - k * 2.3
    bio.box(ax, (16.6, y), 5.6, 0.62, token=tok, text=title, size="tiny", radius=0.1)
    bio.label(ax, (19.6, y - 0.95), note, size="tiny", color=P.muted())
    ax.plot([15.4, 23.4], [y - 0.42, y - 0.42], color=P.edge("dna"), lw=1.6, zorder=4)

# ----------------------------------------------------------------- F: heteroplasmy
bio.panel(ax, "F", (13.2, 3.15))
bio.label(ax, (19.4, 3.15), "Heteroplasmy has a threshold", size="small", bold=True)
f = np.linspace(0, 1, 200)
phen = 1 / (1 + np.exp(-(f - 0.7) / 0.04))
pl = Q.Plot(ax, (15.6, 0.8, 5.6, 2.0), xlim=(0, 1), ylim=(0, 1.05),
            xlabel="fraction of mutant mitochondrial genomes", ylabel="severity",
            xticks=[(0, "0"), (0.5, "0.5"), (1, "1")], yticks=[0, 1], ylabel_offset=0.65)
pl.line(f, phen, "negative", lw=1.8)
pl.vline(0.7, token="muted", text="threshold")
pl.points([0.85, 0.65], [phen[np.argmin(abs(f - 0.85))], phen[np.argmin(abs(f - 0.65))]], "positive", r=0.09)
bio.arrow(ax, (pl.X(0.85), pl.Y(0.75)), (pl.X(0.65), pl.Y(0.75)), kind="process", color=P.edge("positive"))
bio.label(ax, (22.0, 2.0), "correcting a fifth of the\ngenomes can be enough", size="tiny", ha="left",
          color=P.edge("positive"))
