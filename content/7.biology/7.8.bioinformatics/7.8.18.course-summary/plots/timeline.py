"""Methods of bioinformatics, 1958-2024, with the chapters (7.8.n) where they appear.

Left of the time axis: algorithms and models; right: data, sequencing technology and resources.
Years as given in the chapters: UPGMA 1958 (6); Dayhoff's Atlas 1965 (1); Jukes-Cantor 1969 (6);
Needleman-Wunsch 1970 (3); Fitch 1971 (6); Hirschberg 1975 (3); Sanger sequencing 1977 (1); PAM 1978 (3);
Smith-Waterman 1981 (3); Felsenstein pruning 1981 (6); GenBank 1982 (1); Gotoh 1982 (3); FASTA 1985 (4);
neighbor joining 1987 (6); Karlin-Altschul statistics and BLAST 1990 (4); McCaskill 1990 (16);
BLOSUM 1992 (3); Gibbs motif sampler 1993 (8); profile HMMs, MEME, covariance models, the BWT 1994
(5, 8, 16, 10); first free-living genome 1995 (1); PSI-BLAST and GENSCAN 1997 (5, 7); FM-index and
STRUCTURE 2000 (10, 13); human genome 2001 (1); BLAT and MAFFT 2002 (4, 5); Li-Stephens 2003 (13);
massively parallel sequencing 2005 (1); SAM format, BWA and Bowtie 2009 (10); single-molecule real-time
sequencing 2010 (1); HMMER3 2011 (5); BWA-MEM 2013 (10); nanopore sequencing 2014 (1); DeepSEA 2015
(15); DADA2 2016 (14); MMseqs2 2017 (4); minimap2 2018 (10); SpliceAI and Kraken 2 2019 (8, 14);
AlphaFold2 2020 (17); UShER and Enformer 2021 (6, 15); T2T-CHM13 2022 (2); human pangenome reference
and ESM-2 2023 (2, 15); AlphaFold 3 2024 (17)."""

import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
F = bio.core.FONT
A, D = "dna", "protein"

events = [
    (1958, "UPGMA (6)", A),
    (1965, "Dayhoff's Atlas of Protein Sequence (1)", D),
    (1969, "Jukes-Cantor substitution model (6)", A),
    (1970, "Needleman-Wunsch alignment (3)", A),
    (1971, "Fitch parsimony (6)", A),
    (1975, "Hirschberg linear space (3)", A),
    (1977, "Sanger sequencing (1)", D),
    (1978, "PAM matrices (3)", A),
    (1981, "Smith-Waterman; Felsenstein pruning (3, 6)", A),
    (1982, "GenBank founded (1)", D),
    (1985, "FASTA (4)", A),
    (1987, "neighbor joining (6)", A),
    (1990, "BLAST, Karlin-Altschul statistics (4)", A),
    (1992, "BLOSUM matrices (3)", A),
    (1994, "profile HMMs, MEME, covariance models, BWT (5, 8, 16, 10)", A),
    (1995, "first free-living genome sequenced (1)", D),
    (1997, "PSI-BLAST, GENSCAN (5, 7)", A),
    (2000, "FM-index; STRUCTURE (10, 13)", A),
    (2001, "draft human genome (1)", D),
    (2002, "BLAT, MAFFT (4, 5)", A),
    (2003, "Li-Stephens haplotype model (13)", A),
    (2005, "massively parallel short reads (1, 9)", D),
    (2009, "BWA, Bowtie, SAM format (10)", A),
    (2010, "single-molecule real-time reads (1, 9)", D),
    (2011, "HMMER3 (5)", A),
    (2013, "BWA-MEM (10)", A),
    (2014, "nanopore reads (1, 9)", D),
    (2015, "DeepSEA, DeepBind (15)", A),
    (2016, "DADA2 (14)", A),
    (2017, "MMseqs2 (4)", A),
    (2018, "minimap2 (10)", A),
    (2019, "SpliceAI, Kraken 2 (8, 14)", A),
    (2020, "AlphaFold2 (17)", D),
    (2021, "Enformer; UShER (15, 6)", A),
    (2022, "T2T-CHM13 complete human genome (2)", D),
    (2023, "human pangenome reference; ESM-2 (2, 15)", D),
    (2024, "AlphaFold 3 (17)", D),
]

Y0, Y1 = 1954, 2028
H = 9.6
fig, ax = plt.subplots(figsize=(8.6, H))
fig.subplots_adjust(left=0.02, right=0.98, top=0.95, bottom=0.03)
ax.set_xlim(-1, 1)
ax.set_ylim(Y1, Y0)
ax.axis("off")
ax.plot([0, 0], [Y0 + 2, Y1 - 2], color=P.ink(), lw=1.0)
for y in range(1960, 2030, 10):
    ax.plot([-0.012, 0.012], [y, y], color=P.ink(), lw=0.8)
    ax.text(-0.99, y, str(y), fontsize=F["tiny"], color=P.muted(), ha="left", va="center")
    ax.plot([-0.93, -0.9], [y, y], color=P.muted(), lw=0.6)

GAP = 2.05


def spread(ys):
    out = []
    for y in ys:
        out.append(max(y, out[-1] + GAP) if out else y)
    over = out[-1] - (Y1 - 1) if out else 0
    if over > 0:
        out = [y - over for y in out]
        for i in range(len(out) - 2, -1, -1):
            out[i] = min(out[i], out[i + 1] - GAP)
    return out


left = [e for e in events if e[2] == A]
right = [e for e in events if e[2] != A]
for side, evs in ((-1, left), (1, right)):
    ys = spread([e[0] for e in evs])
    for (year, text, tok), yl in zip(evs, ys):
        ax.plot([0], [year], "o", ms=5, mfc=P.fill(tok), mec=P.edge(tok), mew=0.9, zorder=5)
        xl = side * 0.12
        ax.plot([0, side * 0.05, xl], [year, year, yl], color=P.edge(tok), lw=0.6, zorder=4)
        ax.text(xl + side * 0.01, yl, f"{year}  {text}" if side > 0 else f"{text}  {year}", fontsize=F["tiny"],
                color=P.ink(), ha="left" if side > 0 else "right", va="center")
ax.text(-0.5, Y0 - 1, "algorithms and models", fontsize=F["small"], color=charts.line(A), ha="center",
        weight="bold")
ax.text(0.5, Y0 - 1, "data, technology and resources", fontsize=F["small"], color=charts.line(D),
        ha="center", weight="bold")
