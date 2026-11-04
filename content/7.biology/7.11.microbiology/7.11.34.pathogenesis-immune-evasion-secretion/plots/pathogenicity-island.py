# A pathogenicity island in a genome browser view: deviant GC content, a tRNA gene, an integrase, direct repeats;
# and the complementary process of genome decay in host-restricted lineages.
import numpy as np
from matplotlib.patches import Rectangle

import wikibio as bio
from wikibio import quant, sequence

P = bio.P
rng = np.random.default_rng(0)
fig, ax = bio.canvas(19.0, 8.6)

# ================================================================ A: the island
bio.panel(ax, "A", (0.1, 8.35))
bio.label(ax, (9.0, 8.35), "A pathogenicity island, and how it is recognized", size="title", bold=True)

start, end = 2_000_000, 2_060_000
gb = sequence.Browser(ax, (start, end), 2.2, 18.2, chrom="chromosome")
gb.axis(3.1)

ISL0, ISL1 = 2_014_000, 2_048_000
gb.highlight(ISL0, ISL1, 3.3, 7.4, token="highlight")

# GC content: the island deviates
win = np.linspace(start, end, 240)
gc = 50.5 + 0.9 * rng.standard_normal(240)
gc[(win > ISL0) & (win < ISL1)] -= 8.0
gb.signal(5.9, 1.3, gc - 38.0, positions=win, token="dna", label="GC / % (38–58)", ymax=20)

genes = [(2_003_000, 2_006_000, "+", None), (2_008_000, 2_012_000, "-", None),
         (2_013_200, 2_013_400, "+", None), (2_014_800, 2_017_000, "+", "integrase"),
         (2_019_000, 2_023_000, "+", None), (2_024_000, 2_031_000, "+", None),
         (2_032_000, 2_036_000, "+", None), (2_037_000, 2_041_000, "+", None),
         (2_042_000, 2_046_000, "+", None), (2_051_000, 2_056_000, "+", None)]
for a, b, strand, nm in genes:
    tok = "positive" if ISL0 < a < ISL1 else "dna"
    gb.gene(4.4, [(a, b)], strand=strand, name=nm, token=tok, italic=False)

for pos in (ISL0, ISL1):
    gb.peaks(3.6, [(pos - 600, pos + 600)], token="negative")
bio.label(ax, (gb.x(2_032_000), 5.05), "secretion apparatus, effectors and their regulator", size="tiny", color=P.muted())
bio.label(ax, (gb.x(2_004_000), 5.05), "core genome", size="tiny", color=P.muted())
bio.label(ax, (gb.x((ISL0 + ISL1) / 2), 7.6), "34 kb absent from closely related non-pathogenic strains",
          size="tiny", color=P.muted())
bio.label(ax, (gb.x(2_013_300), 3.72), "inserted at a tRNA gene; direct repeats (red) at both ends", size="tiny", color=P.muted(), ha="left")

# ================================================================ B: genome decay
bio.panel(ax, "B", (0.1, 2.5))
bio.label(ax, (9.0, 2.5), "The other half of the story: genome decay in host-restricted lineages",
          size="title", bold=True)

rows = [("Escherichia coli K-12", 4.6, 0.0, "free-living and commensal"),
        ("Shigella flexneri", 4.6, 0.25, "+ invasion plasmid; flagella, $\\it{cadA}$ lost"),
        ("Mycobacterium tuberculosis", 4.4, 0.03, "facultative intracellular"),
        ("Mycobacterium leprae", 3.3, 0.49, "obligate; ≈1600 pseudogenes"),
        ("Rickettsia prowazekii", 1.1, 0.20, "obligate intracellular; biosynthesis lost")]
pB = quant.Plot(ax, (5.4, 0.35, 7.6, 1.55), xlim=(0, 5.0), ylim=(-0.6, 4.6),
                xlabel="genome size / Mb", xticks=[0, 1, 2, 3, 4, 5], frame="l")
for i, (sp, size, pseudo, note) in enumerate(reversed(rows)):
    y = i * 0.95 - 0.3
    y0, y1 = pB.Y(y - 0.3), pB.Y(y + 0.3)
    ax.add_patch(Rectangle((pB.X(0), y0), pB.X(size) - pB.X(0), y1 - y0,
                                        facecolor=P.fill("dna"), edgecolor=P.edge("dna"), lw=0.8, zorder=6))
    ax.add_patch(Rectangle((pB.X(size * (1 - pseudo)), y0), pB.X(size) - pB.X(size * (1 - pseudo)),
                                        y1 - y0, facecolor=P.fill("neutral"), edgecolor=P.edge("neutral"),
                                        lw=0.8, zorder=7))
    bio.label(ax, (pB.X(0) - 0.15, pB.Y(y)), sp, size="tiny", ha="right", italic=True)
    bio.label(ax, (pB.X(size) + 0.2, pB.Y(y)), note, size="tiny", ha="left", color=P.muted())
bio.label(ax, (5.4, 2.1), "blue: functional genome   grey: pseudogenes and decayed regions", size="tiny",
          color=P.muted(), ha="left")
