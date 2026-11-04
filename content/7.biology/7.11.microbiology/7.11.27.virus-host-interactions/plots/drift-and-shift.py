# Antigenic drift and antigenic shift.
# A: a minimal model of drift as a travelling wave in a one-dimensional antigenic space. Strains at
#    antigenic position x grow at rate R times their susceptibility S(x) = exp(-I(x)), where I is the
#    accumulated immunity of the population convolved with a cross-immunity kernel; mutation diffuses
#    the population along x. The result is the characteristic steady advance: each variant is replaced
#    by a descendant slightly further along the axis, and the antigenic distance from a fixed vaccine
#    strain grows without bound.
# B: shift, drawn as a reassortment between a human and an avian virus in a coinfected cell.
import numpy as np
from scipy.ndimage import gaussian_filter1d

import wikibio as bio
from wikibio import charts, quant

P = bio.P
fig, ax = bio.canvas(17.4, 7.8)

# --- A  drift -------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.6))
bio.label(ax, (4.6, 7.45), "Antigenic drift as a travelling wave", size="title", bold=True)

GRID = np.linspace(-1.0, 12.0, 521)
DX = GRID[1] - GRID[0]
SIGMA_MUT = 0.09          # antigenic effect of mutation per generation
CROSS = 0.9               # width of cross-immunity in the same units
R0, PREV = 1.6, 1.0       # reproduction number and the (fixed) total prevalence
GENS = 150

n = np.exp(-((GRID - 0.0) ** 2) / (2 * 0.05 ** 2))
n *= PREV / n.sum()
immunity = np.zeros_like(GRID)
history = np.zeros((GENS, GRID.size))
for t in range(GENS):
    history[t] = n
    cross = gaussian_filter1d(immunity, CROSS / DX, mode="nearest")
    s = np.exp(-cross)
    n = n * R0 * s
    n = gaussian_filter1d(n, SIGMA_MUT / DX, mode="nearest")
    n = np.maximum(n, 0)
    n *= PREV / max(n.sum(), 1e-12)
    immunity += n

pax = charts.axes_at(ax, (1.3, 1.75, 6.6, 5.1))
pax.imshow(np.log10(history + 1e-6), origin="lower", aspect="auto", cmap="magma" if P.is_dark() else "YlOrRd",
           extent=(GRID[0], GRID[-1], 0, GENS), vmin=-4, vmax=np.log10(history.max()))
mean_x = (history * GRID).sum(1) / history.sum(1)
pax.plot(mean_x, np.arange(GENS), color=charts.line("dna"), lw=1.6)
pax.axvline(mean_x[20], color=charts.line("positive"), lw=1.4, ls=(0, (4, 2.4)))
pax.annotate("vaccine strain\nchosen here", xy=(mean_x[20], 22), xytext=(mean_x[20] + 2.6, 26),
             fontsize=7, color=charts.line("positive"),
             arrowprops=dict(arrowstyle="->", color=charts.line("positive"), lw=0.9))
pax.annotate("antigenic distance from it\ngrows every season",
             xy=(mean_x[115], 115), xytext=(0.7, 131), fontsize=7, color=P.ink(),
             arrowprops=dict(arrowstyle="->", color=P.ink(), lw=0.9))
charts.style_axes(pax, "antigenic position", "generations")
bio.label(ax, (4.3, 0.5), "colour: strain abundance at each antigenic position (log scale);\n"
                          "line: the population mean", size="tiny", color=P.muted())

# --- B  shift -------------------------------------------------------------------------------------
bio.panel(ax, "B", (8.9, 7.6))
bio.label(ax, (13.4, 7.45), "Antigenic shift: reassortment", size="title", bold=True)

SEG = ["PB2", "PB1", "PA", "HA", "NP", "NA", "M", "NS"]


def genome(x, y, tokens, label=None, scale=0.34):
    for i, tok in enumerate(tokens):
        yy = y - i * scale
        bio.box(ax, (x, yy), 1.5, 0.27, token=tok, radius=0.08)
        bio.label(ax, (x, yy), SEG[i], size="tiny", color=P.on_fill())
    if label:
        bio.label(ax, (x, y + 0.45), label, size="small", bold=True)


genome(10.0, 6.3, ["dna"] * 8, "human virus")
genome(12.3, 6.3, ["negative"] * 8, "avian virus")
bio.label(ax, (11.15, 2.95), "one cell infected\nby both", size="tiny", color=P.muted())
bio.arrow(ax, (11.15, 2.5), (11.15, 2.0), kind="process")

for i, tok in enumerate(["dna", "dna", "dna", "negative", "dna", "dna", "dna", "dna"]):
    bio.box(ax, (9.3 + i * 0.66, 1.6), 0.60, 0.32, token=tok, radius=0.08)
    bio.label(ax, (9.3 + i * 0.66, 1.6), SEG[i], size="tiny", color=P.on_fill())
bio.label(ax, (11.6, 1.1), "reassortant: an avian HA on an otherwise human-adapted background",
          size="tiny", color=P.muted())
bio.label(ax, (11.6, 0.5), "the population has no immunity to the new HA: a pandemic.\n"
                           "The viruses of 1957, 1968 and 2009 arose this way", size="tiny",
          color=P.edge("negative"))

bio.label(ax, (15.7, 5.2), "segments are packaged\nindependently, so any\ncombination can be\nassembled",
          size="tiny", color=P.muted())
