"""Classes of DNA sequence variants in a schematic alignment of two haplotypes with a reference: a
single-nucleotide variant, a short insertion-deletion, a short tandem repeat with different numbers of
units, and a copy-number variant of a larger segment."""
import wikibio as bio
from wikibio import sequence as S, cytogenetics as C

P = bio.P
fig, ax = bio.canvas(27.5, 8.0)
blocks = [
    ("A  SNP", {"reference": "ACGTTAGCCTA", "haplotype 1": "ACGTTAGCCTA", "haplotype 2": "ACGTCAGCCTA"}, [(4, 4, "T>C")]),
    ("B  Indel", {"reference": "ACGGATTCCAT", "haplotype 1": "ACGGATTCCAT", "haplotype 2": "ACG---TCCAT"}, [(3, 5, "deletion")]),
    ("C  Short tandem repeat", {"reference": "T" + "CAT" * 3 + "-" * 9 + "G", "haplotype 1": "T" + "CAT" * 6 + "G",
                                "haplotype 2": "T" + "CAT" * 2 + "-" * 12 + "G"}, [(0, 17, "")]),
]
x = 0.4
for title, seqs, hl in blocks:
    bio.label(ax, (x, 7.6), title, size="small", ha="left")
    S.alignment(ax, seqs, at=(x + 2.6, 6.8), cell=(0.36, 0.48), scheme="nucleotide", color_by="residue", consensus=False,
                conservation=False, ruler=False, marks=False, highlight=hl if hl[0][2] else ())
    x += 2.8 + len(next(iter(seqs.values()))) * 0.36 + 0.4
bio.label(ax, (22.0, 5.0), "(CAT)n: reference 3 units, haplotype 1 six, haplotype 2 two", size="tiny", color=P.muted(), ha="center")
bio.label(ax, (0.4, 3.6), "D  Copy-number variant (segment of tens of kb to Mb)", size="small", ha="left")
seg = "highlight"
rows = [("1 copy (deletion carrier)", [("A", "dna"), ("B", "dna"), ("D", "dna"), ("E", "dna")]),
        ("2 copies (reference)", [("A", "dna"), ("B", "dna"), ("C", seg), ("D", "dna"), ("E", "dna")]),
        ("3 copies (duplication)", [("A", "dna"), ("B", "dna"), ("C", seg), ("C", seg), ("D", "dna"), ("E", "dna")])]
bio.label(ax, (0.6, 2.9), "per haplotype:", size="tiny", color=P.muted(), ha="left")
y = 2.9
for name, chrom in [("0 copies", rows[0][1]), ("1 copy (reference)", rows[1][1]), ("2 copies", rows[2][1])]:
    bio.label(ax, (5.2, y), name, size="tiny", ha="right")
    C.lettered(ax, (5.5, y), chrom, unit=0.8, height=0.4)
    y -= 0.8
bio.label(ax, (11.5, 2.1), "Unequal crossing over or NAHR between flanking repeats (7.4.15)", size="tiny", ha="left",
          color=P.muted())
bio.label(ax, (11.5, 1.6), "changes the copy number of segment C; read depth or array intensity measures it", size="tiny",
          ha="left", color=P.muted())
