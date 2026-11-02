# The cost of sequencing one human genome (values of 7.8.1: rounded after the NHGRI Genome Sequencing
# Program cost table, vendor list prices for 2024) against a cost halving every two years (Moore's law),
# with the year in which each method of the course that answered the new data appeared (chapters 7.8.n):
# BLAT 2002 (4), MAFFT 2002 (5), Li-Stephens 2003 (13), BWA, Bowtie and SAM 2009 (10), HMMER3 2011 (5),
# BWA-MEM 2013 (10), DeepSEA 2015 (15), DADA2 2016 (14), MMseqs2 2017 (4), minimap2 2018 (10),
# Kraken 2 2019 (14), AlphaFold2 2020 (17), UShER 2021 (6), AlphaFold 3 2024 (17).
# Each method trades exhaustive computation for an index, a seed, a model or a learned predictor.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT
year = np.array([2001.7, 2002.5, 2003.5, 2004.5, 2005.5, 2006.5, 2007.8, 2008.3, 2008.8, 2009.3, 2009.8,
                 2010.5, 2011.0, 2011.5, 2012.0, 2013.0, 2014.0, 2015.0, 2016.0, 2017.0, 2018.0, 2019.0,
                 2020.0, 2021.0, 2022.0, 2024.0])
cost = np.array([9.5e7, 6e7, 4e7, 3e7, 2e7, 1.5e7, 1e7, 3e6, 1e6, 2.5e5, 1e5,
                 5e4, 3e4, 1e4, 8e3, 6e3, 4e3, 1.5e3, 1.2e3, 1.1e3, 1.0e3, 9e2,
                 7e2, 6e2, 5e2, 3e2])
methods = [(2002, "BLAT, MAFFT"), (2003, "Li-Stephens"), (2009, "BWA, Bowtie, SAM"), (2011, "HMMER3"),
           (2013, "BWA-MEM"), (2015, "DeepSEA"), (2016, "DADA2"), (2017, "MMseqs2"), (2018, "minimap2"),
           (2019, "Kraken 2"), (2020, "AlphaFold2"), (2021, "UShER"), (2024, "AlphaFold 3")]

fig, ax = bio.canvas(18.0, 12.0)
a = C.axes_at(ax, (2.0, 4.6, 15.2, 6.8))
a.semilogy(year, cost, "o-", color=C.line("dna"), ms=3.5, lw=1.8, label="sequencing cost per human genome (30x)")
yy = np.linspace(2001.7, 2024, 100)
a.semilogy(yy, 9.5e7 * 0.5 ** ((yy - 2001.7) / 2.0), color=P.muted(), lw=1.6, label="halving every 2 years")
a.set_xlim(2001, 2025)
a.set_ylim(1e2, 4e8)
C.style_axes(a, None, "US dollars")
a.legend(fontsize=FT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower left")
b = C.axes_at(ax, (2.0, 0.9, 15.2, 2.9))
b.set_xlim(2001, 2025)
b.set_ylim(0, 4.2)
for k, (y, name) in enumerate(methods):
    h = 0.6 + (k % 4) * 0.9
    b.plot([y, y], [0, h], color=C.line("protein"), lw=0.8)
    b.scatter([y], [h], s=12, color=C.line("protein"), zorder=4)
    b.text(y + 0.15, h, name, fontsize=FT["tiny"], color=P.ink(), va="center")
b.set_yticks([])
C.style_axes(b, "year", None)
b.spines["left"].set_visible(False)
bio.panel(ax, "A", (0.3, 11.6))
bio.panel(ax, "B", (0.3, 4.0))
