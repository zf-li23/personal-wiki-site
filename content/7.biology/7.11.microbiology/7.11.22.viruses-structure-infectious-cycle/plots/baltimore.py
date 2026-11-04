# The Baltimore classification drawn as seven routes to mRNA.
# Each row: the genome carried in the virion (left), the syntheses needed to reach mRNA (arrows, with the
# polymerase named on the arrow), the mRNA column, whether the virion must carry a polymerase, and examples.
# DNA is drawn in the DNA token (blue), RNA in the RNA token (orange); a single line is a single strand,
# two lines a duplex; + and - give the polarity (mRNA sense is +).
import numpy as np

import wikibio as bio

P = bio.P
ROWS = 7
fig, ax = bio.canvas(30, 15.4)


def nucleic(x, y, strands, kind, labels, text=None, w=2.0):
    """Draw a genome/intermediate glyph: 1 or 2 strands, DNA or RNA, with polarity labels. Returns right edge."""
    tok = "dna" if kind == "dna" else "rna"
    col = P.edge(tok) if not P.is_dark() else P.fill(tok)
    dy = 0.17
    ys = [y] if strands == 1 else [y + dy, y - dy]
    for yy in ys:
        ax.plot([x, x + w], [yy, yy], color=col, lw=2.2, solid_capstyle="round", zorder=6)
    for yy, s in zip(ys, labels):
        bio.label(ax, (x - 0.22, yy), s, size="tiny", color=col)
    if text:
        bio.label(ax, (x + w / 2, y - 0.62), text, size="tiny", color=P.muted())
    return x + w


def enzyme_arrow(x0, x1, y, text, token="enzyme"):
    bio.arrow(ax, (x0 + 0.25, y), (x1 - 0.25, y), kind="process", lw=1.1, head=0.2,
              color=P.edge(token) if not P.is_dark() else P.fill(token))
    bio.label(ax, ((x0 + x1) / 2, y + 0.42), text, size="tiny", color=P.muted())


rows = [
    # (class, genome strands, kind, polarity labels, genome caption, chain, carries polymerase, examples, point)
    ("I", 2, "dna", ("+", "−"), "dsDNA", [("host RNA pol", None)], False,
     "phages T4 and λ;\n— (plant DNA viruses are ssDNA\nor pararetroviruses);\nherpes-, adeno-, poxviruses",
     "the simplest route: the cell can read the genome"),
    ("II", 1, "dna", ("+",), "ssDNA", [("host DNA pol", (2, "dna", ("+", "−"), "dsDNA")), ("host RNA pol", None)], False,
     "phages φX174, M13;\ngeminiviruses;\nparvo-, circoviruses",
     "the complementary strand must be made first"),
    ("III", 2, "rna", ("+", "−"), "dsRNA", [("RdRp, in the particle", None)], True,
     "phage φ6;\nplant reoviruses;\nreo-, rotaviruses",
     "transcribed inside the capsid, which hides the dsRNA"),
    ("IV", 1, "rna", ("+",), "(+)ssRNA", [("RdRp", (1, "rna", ("−",), "(−)RNA")), ("RdRp", None)], False,
     "phages MS2, Qβ;\ntobacco mosaic virus;\npolio-, coronaviruses",
     "the genome is mRNA: it is translated on arrival"),
    ("V", 1, "rna", ("−",), "(−)ssRNA", [("RdRp, in the particle", None)], True,
     "—;\nrhabdoviruses of plants;\ninfluenza, measles, rabies, Ebola",
     "no cell can copy it: the enzyme must come in the particle"),
    ("VI", 1, "rna", ("+",), "(+)ssRNA", [("reverse transcriptase", (2, "dna", ("+", "−"), "provirus")), ("host RNA pol", None)], True,
     "—;\n—;\nHIV and other retroviruses",
     "DNA intermediate, integrated into the host genome"),
    ("VII", 2, "dna", ("+", "−"), "dsDNA (gapped)", [("host RNA pol", None)], True,
     "—;\ncauliflower mosaic virus;\nhepatitis B virus",
     "mRNA is also the template for the new DNA genome"),
]

X_CLASS, X_GEN, X_MRNA, X_ENZ, X_EX = 0.5, 1.6, 13.4, 17.0, 18.6
top = 13.9
bio.label(ax, (X_GEN + 1.0, top + 0.75), "genome in the virion", size="small", bold=True)
bio.label(ax, (X_MRNA + 1.0, top + 0.75), "mRNA", size="small", bold=True)
bio.label(ax, (X_ENZ + 0.6, top + 1.05), "polymerase\nin the virion", size="small", bold=True)
bio.label(ax, (X_EX, top + 0.75), "examples (bacterial; plant; animal)", size="small", bold=True, ha="left")
bio.label(ax, (X_EX + 7.2, top + 0.75), "the point of the strategy", size="small", bold=True, ha="left")
ax.plot([X_MRNA - 0.55, X_MRNA - 0.55], [0.4, top + 0.35], color=P.muted(), lw=0.7, ls=(0, (2, 3)), zorder=2)
ax.plot([X_MRNA + 2.75, X_MRNA + 2.75], [0.4, top + 0.35], color=P.muted(), lw=0.7, ls=(0, (2, 3)), zorder=2)

for i, (cls, ns, kind, pol, cap, chain, carries, ex, point) in enumerate(rows):
    y = top - i * 1.95
    bio.label(ax, (X_CLASS, y), cls, size="title", bold=True)
    x = nucleic(X_GEN, y, ns, kind, pol, cap, w=1.9)
    # intermediates along the route; the last arrow lands on the mRNA column
    for enz, inter in chain:
        if inter is None:
            enzyme_arrow(x, X_MRNA - 0.25, y, enz)
            x = X_MRNA
        else:
            step = (X_MRNA - 0.35 - x) * 0.3
            enzyme_arrow(x, x + step, y, enz)
            x = nucleic(x + step, y, inter[0], inter[1], inter[2], inter[3], w=1.5)
    nucleic(X_MRNA, y, 1, "rna", ("+",), None, w=1.6)
    bio.label(ax, (X_MRNA + 0.8, y - 0.55), "mRNA", size="tiny", color=P.muted())
    if cls == "VII":  # the RNA pregenome is reverse-transcribed back into the genome
        bio.arrow(ax, (X_MRNA + 0.9, y - 0.95), (X_GEN + 0.9, y - 0.95), kind="process", bend=0.07, lw=1.0, head=0.18,
                  color=P.edge("enzyme") if not P.is_dark() else P.fill("enzyme"))
        bio.label(ax, (X_MRNA - 5.0, y - 1.5), "reverse transcriptase (the mRNA is the pregenome)", size="tiny",
                  color=P.muted())
    if cls == "IV":
        bio.label(ax, (X_MRNA + 0.8, y + 0.55), "= the genome", size="tiny", color=P.muted())
    col = P.edge("negative") if not P.is_dark() else P.fill("negative")
    bio.label(ax, (X_ENZ + 0.6, y), "yes" if carries else "no", size="small",
              color=col if carries else P.muted(), bold=carries)
    bio.label(ax, (X_EX, y), ex, size="tiny", ha="left")
    bio.label(ax, (X_EX + 7.2, y), point, size="tiny", ha="left", color=P.muted())

# legend
lx, ly = X_EX, 0.75
for k, (tok, txt) in enumerate((("dna", "DNA"), ("rna", "RNA"))):
    c = P.edge(tok) if not P.is_dark() else P.fill(tok)
    ax.plot([lx + k * 3.0, lx + k * 3.0 + 0.8], [ly, ly], color=c, lw=2.2, solid_capstyle="round")
    bio.label(ax, (lx + k * 3.0 + 1.0, ly), txt, size="tiny", ha="left")
bio.label(ax, (lx + 6.4, ly), "one line, single strand;  two lines, duplex;  + = mRNA sense", size="tiny",
          ha="left", color=P.muted())
_ = np.array([0])
