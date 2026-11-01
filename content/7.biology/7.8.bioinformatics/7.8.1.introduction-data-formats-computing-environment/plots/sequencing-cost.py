# Cost of sequencing one human genome, 2001-2024, on a log scale. Values are rounded to one or two significant
# figures after the NHGRI Genome Sequencing Program cost table (production costs at NHGRI-funded centres) and,
# for 2024, list prices of high-throughput instruments. The grey line is a cost that halves every two years
# from the 2001 value (Moore's law). The dashed bracket shows the gap that opened between 2008 and 2015.
import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts as C

P = bio.P
year = np.array([2001.7, 2002.5, 2003.5, 2004.5, 2005.5, 2006.5, 2007.8, 2008.3, 2008.8, 2009.3, 2009.8,
                 2010.5, 2011.0, 2011.5, 2012.0, 2013.0, 2014.0, 2015.0, 2016.0, 2017.0, 2018.0, 2019.0,
                 2020.0, 2021.0, 2022.0, 2024.0])
cost = np.array([9.5e7, 6e7, 4e7, 3e7, 2e7, 1.5e7, 1e7, 3e6, 1e6, 2.5e5, 1e5,
                 5e4, 3e4, 1e4, 8e3, 6e3, 4e3, 1.5e3, 1.2e3, 1.1e3, 1.0e3, 9e2,
                 7e2, 6e2, 5e2, 3e2])

fig, ax = bio.canvas(16.0, 9.0)
a = C.axes_at(ax, (1.8, 1.3, 13.4, 7.0))
a.semilogy(year, cost, "o-", color=C.line("dna"), ms=3.5, lw=1.8, label="cost per human genome (30x)")
yy = np.linspace(2001.7, 2024, 100)
moore = 9.5e7 * 0.5 ** ((yy - 2001.7) / 2.0)
a.semilogy(yy, moore, color=P.muted(), lw=1.6, label="halving every 2 years (Moore's law)")
a.axvspan(2007.5, 2011.7, color=P.light("highlight"), lw=0, zorder=0)
a.text(2009.6, 2.5e8, "massively parallel\nsequencing arrives", ha="center", va="top",
       fontsize=bio.core.FONT["tiny"], color=P.ink())
m15 = 9.5e7 * 0.5 ** ((2015.0 - 2001.7) / 2.0)
a.annotate("", xy=(2015.0, 1.5e3), xytext=(2015.0, m15),
           arrowprops=dict(arrowstyle="<->", color=C.line("negative"), lw=1.0, linestyle=(0, (3, 2))))
a.text(2015.4, np.sqrt(1.5e3 * m15), "about 600-fold\nby 2015", ha="left", va="center",
       fontsize=bio.core.FONT["tiny"], color=C.line("negative"))
a.set_xlim(2001, 2025)
a.set_ylim(1e2, 4e8)
C.style_axes(a, "year", "cost per genome (US dollars)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower left")
