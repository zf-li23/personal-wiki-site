"""Five routes to loss of heterozygosity at a tumor suppressor locus in a cell heterozygous for a germline
mutation. The chromosome carrying the mutant allele (m) and its homolog with the normal allele (+) carry
three linked markers; the copy number and the markers that remain heterozygous distinguish the mechanisms."""
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(19.0, 13.0)
LEN, WID = 3.4, 0.5
MARK = [(0.18, "1"), (0.55, "2"), (0.8, "3")]
Y = 9.3


def chrom(x, allele, token, markers=MARK, length=LEN, cut=None):
    loci = [(f, t, "right") for f, t in markers] + [(0.38, allele, "left")]
    G.chromosome(ax, (x, Y), length=length, centromere=0.12, width=WID, token=token, sister=False, loci=loci)


panels = [
    ("Normal heterozygote", [("m", "receptor", None), ("+", "dna", None)], "2 copies", "all markers heterozygous"),
    ("Chromosome loss", [("m", "receptor", None)], "1 copy", "all markers lost"),
    ("Loss and duplication", [("m", "receptor", None), ("m", "receptor", None)], "2 copies", "all markers homozygous"),
    ("Mitotic recombination", [("m", "receptor", None), ("m", "receptor", "recomb")], "2 copies",
     "markers distal to the crossover homozygous"),
    ("Interstitial deletion", [("m", "receptor", None), ("+", "dna", "del")], "2 copies (1 at the locus)",
     "only the markers next to the gene lost"),
    ("Point mutation or methylation", [("m", "receptor", None), ("m*", "dna", None)], "2 copies",
     "no marker changes"),
]
for k, (title, chroms, copies, markers) in enumerate(panels):
    col, row = k % 3, k // 3
    cx, yoff = 3.2 + col * 6.2, -row * 6.3
    globals()["Y"] = 9.3 + yoff
    bio.label(ax, (cx, Y + 2.35), title, size="normal", bold=True)
    for j, (allele, tok, special) in enumerate(chroms):
        x = cx + (j - (len(chroms) - 1) / 2) * 1.6
        if special == "recomb":
            # distal part derived from the mutant homologue: drawn as a two-coloured chromatid
            G.chromosome(ax, (x, Y), length=LEN, centromere=0.12, width=WID, token="dna", sister=False,
                         colors=[[(0.0, 0.3, "dna"), (0.3, 1.0, "receptor")]],
                         loci=[(f, t, "right") for f, t in MARK] + [(0.38, "m", "left")])
            bio.label(ax, (x + 1.15, Y + 0.72), "crossover", size="tiny", color=P.muted())
        elif special == "del":
            G.chromosome(ax, (x, Y), length=LEN, centromere=0.12, width=WID, token="dna", sister=False,
                         loci=[(f, t, "right") for f, t in MARK[:1] + MARK[2:]])
            bio.label(ax, (x + 1.0, Y + 0.05), "deleted", size="tiny", color=P.muted())
        else:
            chrom(x, allele, tok)
    bio.label(ax, (cx, Y - 2.05), copies, size="small")
    bio.label(ax, (cx, Y - 2.55), markers, size="small", color=P.muted(), va="top")
