# Qualitative time course of innate and adaptive immunity in a first and a second infection with the
# same pathogen. Curves are schematic shapes (no numeric y scale): pathogen load, innate response,
# adaptive response (effector cells and antibody).
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(18.0, 6.4)
t = np.linspace(0, 14, 700)


def sig(x, c, k):
    return 1.0 / (1.0 + np.exp(-(x - c) * k))


def bump(x, peak, width):
    return np.exp(-((np.log(np.maximum(x, 1e-3)) - np.log(peak)) ** 2) / (2 * width ** 2))


# first infection
path1 = 0.95 * sig(t, 1.6, 3.0) * (1 - sig(t, 7.6, 1.6))
innate1 = 0.62 * bump(t, 1.6, 0.75)
adapt1 = 0.9 * sig(t, 5.6, 1.5) * (1 - 0.82 * sig(t, 10.5, 0.9))
# second infection: memory cells respond before the pathogen grows
path2 = 0.22 * sig(t, 0.9, 4.0) * (1 - sig(t, 2.6, 2.6))
innate2 = 0.35 * bump(t, 1.1, 0.7)
adapt2 = 0.2 + 0.9 * sig(t, 1.8, 2.6) * (1 - 0.6 * sig(t, 9.0, 0.9))

ticks = [(0, "0"), (1, "1 d"), (4, "4 d"), (7, "7 d"), (14, "14 d")]
for k, (title, (pa, inn, ad)) in enumerate((("A  First infection", (path1, innate1, adapt1)),
                                            ("B  Second infection, same pathogen", (path2, innate2, adapt2)))):
    x0 = 1.0 + k * 8.9
    bio.label(ax, (x0 - 0.6, 6.1), title, size="title", bold=True, ha="left")
    pl = quant.Plot(ax, (x0, 1.1, 7.6, 3.9), xlim=(0, 14), ylim=(0, 1.15), xticks=ticks, yticks=[],
                    xlabel="time after infection", ylabel="magnitude (schematic)" if k == 0 else None)
    pl.band(t, 0 * t, pa, "neutral", alpha=0.45)
    pl.line(t, pa, "muted", lw=1.4)
    pl.line(t, inn, "drug", lw=2.0)
    pl.line(t, ad, "dna", lw=2.0)
    pl.legend([("pathogen", "muted", "-"), ("innate response", "drug", "-"), ("adaptive response", "dna", "-")],
              at=(x0 + 4.9, 4.9))
    if k == 0:
        pl.text(11.0, 0.24, "memory", size="tiny", color=quant.line_color("dna"))
        pl.text(3.3, 1.0, "innate control", size="tiny")
    else:
        pl.text(6.0, 0.55, "fast memory response;\npathogen kept below\nthe symptom level", size="tiny", ha="left")
