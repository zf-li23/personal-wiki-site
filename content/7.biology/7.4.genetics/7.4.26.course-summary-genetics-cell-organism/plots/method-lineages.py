"""Four lineages of genetic method, from Mendel to genome-scale experiments.

Each lane is one lineage; each event is one that a chapter of 7.4 describes (chapter in parentheses).
Arrows join a method to the later method that inherits its logic: the counting of recombinants
becomes the LOD score and then association with linkage disequilibrium; the mutant screen becomes the
saturation screen, the knockout and the pooled CRISPR screen; Mendelian populations become the
diffusion theory of drift and the polygenic models behind GWAS. The axis is compressed threefold
before 1940.
"""

import matplotlib.pyplot as plt

import wikibio as bio
from wikibio import charts

P = bio.P
FS = 6.9


def Y(year):
    """Time axis: 0.3 unit per year before 1940, 1 unit per year after."""
    return (year - 1860) * 0.3 if year < 1940 else 24 + (year - 1940)


lanes = [  # (name, token, events: (key, year, label))
    ("crosses and maps", "dna", [
        ("mendel", 1865, "Mendel: segregation, assortment (2)"), ("morgan", 1910, r"Morgan: $\it{white}$, X linkage (6)"),
        ("sturt", 1913, "Sturtevant: first map (8)"), ("haldane", 1919, "Haldane mapping function (8)"),
        ("mcc", 1931, "Creighton–McClintock: exchange (8)"), ("hfr", 1956, "interrupted mating (10)"),
        ("benzer", 1959, "Benzer: rII fine structure (13)"), ("tetrad", 1933, "Lindegren: ordered tetrads (9)"),
    ]),
    ("mutants and screens", "negative", [
        ("muller", 1927, "Muller: X-rays mutate (12)"), ("beadle", 1941, "Beadle–Tatum (13)"),
        ("luria", 1943, "Luria–Delbrück (12)"), ("brenner", 1974, r"Brenner: $\it{C.\ elegans}$ screen (1)"),
        ("cnv", 1980, "Nüsslein-Volhard–Wieschaus (20)"), ("ko", 1989, "knockout mice (19)"),
        ("crispr", 2014, "genome-wide CRISPR screens (19)"), ("sge", 2018, "saturation genome editing (19)"),
    ]),
    ("human genetics and genomes", "rna", [
        ("garrod", 1902, "Garrod: alkaptonuria (7)"), ("morton", 1955, "Morton: LOD score (14)"),
        ("botstein", 1980, "DNA-marker linkage maps (14)"), ("hd", 1983, "HD linked to 4p (14)"),
        ("cf", 1989, "CF gene cloned (14)"), ("hgp", 2001, "human genome draft (14)"),
        ("gwas", 2007, "WTCCC: GWAS (25)"), ("t2t", 2022, "T2T genome (14)"),
    ]),
    ("populations and quantitative traits", "plant", [
        ("hw", 1908, "Hardy–Weinberg (22)"), ("fisher", 1918, "Fisher: polygenes, variance (24)"),
        ("wright", 1931, "Wright: drift, inbreeding (22, 23)"), ("kimura", 1962, "Kimura: fixation (23)"),
        ("neutral", 1968, "neutral theory (23)"), ("falc", 1965, "Falconer: liability (24)"),
        ("gcta", 2010, "SNP heritability (25)"), ("pgs", 2018, "biobank PGS (25)"),
    ]),
]
links = [("mendel", "morgan"), ("morgan", "sturt"), ("sturt", "haldane"), ("sturt", "morton"),
         ("morton", "botstein"), ("botstein", "hd"), ("hd", "cf"), ("hgp", "gwas"), ("muller", "brenner"),
         ("brenner", "cnv"), ("cnv", "ko"), ("ko", "crispr"), ("crispr", "sge"), ("hw", "wright"),
         ("fisher", "falc"), ("wright", "kimura"), ("kimura", "neutral"), ("fisher", "gcta"), ("gcta", "pgs"),
         ("gcta", "gwas"), ("beadle", "benzer"), ("mendel", "hw")]

fig, ax = plt.subplots(figsize=(14.0, 8.6))
LW = 10.0
anchor = {}
for i, (name, tok, events) in enumerate(lanes):
    x0 = i * LW
    ax.plot([x0, x0], [Y(1860), Y(2025)], color=P.edge(tok), lw=1.2, alpha=0.6)
    ax.text(x0, Y(1860) - 3.0, name, ha="left", va="bottom", fontsize=8.5, color=P.ink(), weight="bold")
    ylab = -1e9
    for key, year, txt in sorted(events, key=lambda e: e[1]):
        y = Y(year)
        ylab = max(y, ylab + 2.4)
        anchor[key] = (x0, y)
        ax.plot([x0, x0 + 0.6, x0 + 1.0], [y, ylab, ylab], color=P.muted(), lw=0.5)
        ax.plot([x0], [y], "o", ms=5.5, color=P.fill(tok), mec=P.edge(tok), mew=1.0, zorder=5)
        ax.text(x0 + 1.2, ylab, f"{year}  {txt}", ha="left", va="center", fontsize=FS, color=P.ink(),
                style="normal")
for a, b in links:
    (xa, ya), (xb, yb) = anchor[a], anchor[b]
    if xa == xb:
        ax.annotate("", xy=(xb - 0.15, yb), xytext=(xa - 0.15, ya),
                    arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.8, connectionstyle="arc3,rad=0.35",
                                    shrinkA=3, shrinkB=3))
    else:
        ax.annotate("", xy=(xb, yb), xytext=(xa, ya),
                    arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.8, ls="--",
                                    connectionstyle="arc3,rad=-0.12", shrinkA=3, shrinkB=3))
ticks = [1860, 1880, 1900, 1920, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
ax.set_yticks([Y(t) for t in ticks])
ax.set_yticklabels([str(t) for t in ticks])
for t in ticks:
    ax.axhline(Y(t), color=P.muted(), lw=0.3, alpha=0.35, zorder=0)
ax.axhline(Y(1940), color=P.muted(), lw=0.8, ls=":")
ax.text(-1.5, Y(1940) - 0.8, "before 1940: ×3 compressed", ha="right", va="bottom", fontsize=FS, color=P.muted())
ax.set_ylim(Y(2026), Y(1860) - 4)
ax.set_xlim(-3.0, 4 * LW)
ax.set_xticks([])
charts.style_axes(ax, None, "year")
ax.spines["bottom"].set_visible(False)
fig.tight_layout()
