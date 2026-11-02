# Orders of magnitude of the course, on logarithmic axes, with the values used in the chapters (7.8.n).
# A: lengths of the objects analyzed (nucleotides or residues): tRNA-Phe 76 nt (16); a short read 150 nt (9);
#    human MCM6 821 aa (3); a HiFi read about 15 kb (9); SARS-CoV-2 29,903 nt (2); E. coli K-12 4.64 Mb (7);
#    the human genome 3.1 Gb, 6.2 Gb on both strands (10).
# B: counts: de novo mutations per child 74 (12); variants per genome 4.5e6 (12); PDB 2.3e5 entries (17);
#    Swiss-Prot 5.7e5 sequences (4); AlphaFold DB 2e8 models (17); UniProtKB 2.5e8 sequences (4);
#    reads of a 30x genome 6.2e8 (10); residues in the largest protein databases 1e11 (4); genotype matrix
#    of a biobank 5e12 entries (13); raw data in the SRA 9e16 bytes (1).
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT

lengths = [
    (76, "tRNA-Phe (16)", "rna"),
    (150, "short read (9)", "dna"),
    (821, "human MCM6, aa (3)", "protein"),
    (1.5e4, "HiFi read (9)", "dna"),
    (29903, "SARS-CoV-2 genome (2)", "virus"),
    (4.64e6, r"$\it{E.\ coli}$ genome (7)", "bacterium"),
    (3.1e9, "human genome (10)", "dna"),
    (6.2e9, "both strands (10)", "dna"),
]
counts = [
    (74, "de novo SNVs per child (12)", "negative"),
    (4.5e6, "variants per genome (12)", "negative"),
    (2.3e5, "PDB entries (17)", "protein"),
    (5.7e5, "Swiss-Prot sequences (4)", "protein"),
    (2e8, "AlphaFold DB models (17)", "protein"),
    (2.5e8, "UniProtKB sequences (4)", "protein"),
    (6.2e8, "reads of a 30x genome (10)", "dna"),
    (1e11, "residues in nr (4)", "protein"),
    (5e12, "biobank genotypes (13)", "neutral"),
    (9e16, "bytes in the SRA (1)", "neutral"),
]

fig, ax = bio.canvas(30.0, 13.0)

def strip(rect, items, lo, hi, xlabel, letter):
    a = C.axes_at(ax, rect)
    a.set_xscale("log")
    a.set_xlim(lo, hi)
    a.set_ylim(-2.3, 2.3)
    a.axhline(0, color=P.muted(), lw=0.8)
    items = sorted(items)
    for k, (v, name, tok) in enumerate(items):
        side = 1 if k % 2 == 0 else -1
        h = side * (0.4 + 0.42 * ((k // 2) % 3))
        a.plot([v, v], [0, h], color=P.edge(tok), lw=0.7)
        a.scatter([v], [0], s=30, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=5)
        a.text(v, h + 0.08 * side, f"{name}\n{v:.3g}", ha="center", va="bottom" if side > 0 else "top",
               fontsize=FT["tiny"], color=P.ink())
    a.set_yticks([])
    a.spines["left"].set_visible(False)
    C.style_axes(a, xlabel, None)
    a.spines["left"].set_visible(False)
    bio.panel(ax, letter, (rect[0] - 1.4, rect[1] + rect[3] + 0.1))
    return a

strip((1.8, 7.6, 27.0, 4.4), lengths, 30, 3e10, "length (nt or aa)", "A")
strip((1.8, 1.3, 27.0, 4.4), counts, 20, 4e17, "count", "B")
