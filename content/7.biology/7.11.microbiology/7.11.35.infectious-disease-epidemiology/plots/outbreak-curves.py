# Shapes of epidemic curves (point source, propagated, continuing source) and the surveillance pyramid.
import numpy as np
from matplotlib.patches import Polygon
from scipy import stats

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(19.0, 8.4)

# incubation period: lognormal with median 2.5 d
INC = stats.lognorm(s=0.45, scale=2.5)
days = np.arange(0, 42)
edges = np.arange(0, 43)


def hist_panel(box, counts, title, note, token, ymax=None):
    p = quant.Plot(ax, box, xlim=(0, 42), ylim=(0, ymax or counts.max() * 1.25),
                   xlabel="day of onset", ylabel="cases", xticks=[0, 14, 28, 42],
                   yticks=[0, int((ymax or counts.max() * 1.25) // 2)])
    p.bars(edges, counts, token=token)
    bio.label(ax, (box[0] + box[2] / 2, box[1] + box[3] + 0.75), title, size="small", bold=True)
    bio.label(ax, (box[0] + box[2] / 2, box[1] + box[3] + 0.32), note, size="tiny", color=P.muted())
    return p


# ---------------------------------------------------------------- A: common point source
bio.panel(ax, "A", (0.1, 8.1))
counts = 120 * (INC.cdf(edges[1:]) - INC.cdf(edges[:-1]))
pA = hist_panel((1.4, 4.9, 3.9, 2.0), counts, "Common point source", "one exposure; the curve is the\n"
                "incubation-period distribution", "dna")
peak = edges[np.argmax(counts)] + 0.5
pA.vline(peak, token="negative", text=None)
bio.label(ax, (pA.X(peak) + 0.15, pA.Y(counts.max() * 0.75)),
          "peak − median incubation\n= time of exposure", size="tiny", ha="left", color=P.muted())

# ---------------------------------------------------------------- B: propagated
bio.panel(ax, "B", (6.4, 8.1))
serial = stats.lognorm(s=0.18, scale=6.0)
gen = np.zeros_like(days, dtype=float)
gen[0] = 3.0
total = np.zeros_like(days, dtype=float)
wave = np.zeros_like(days, dtype=float)
wave[1] = 3.0
R = 2.1
for g in range(4):                       # successive generations, each convolved with the serial interval
    total += wave
    k = serial.pdf(np.arange(1, 25))
    k /= k.sum()
    wave = R * np.convolve(wave, k)[:len(days)]
hist_panel((7.7, 4.9, 3.9, 2.0), total, "Propagated", "generations one serial interval apart,\n"
           "merging as the epidemic grows", "enzyme")

# ---------------------------------------------------------------- C: continuing common source
bio.panel(ax, "C", (12.7, 8.1))
exposure = np.zeros(42)
exposure[3:22] = 7.0                     # the source is active from day 3 to day 22
k = (INC.cdf(np.arange(1, 20)) - INC.cdf(np.arange(0, 19)))
cont = np.convolve(exposure, k)[:42]
pC = hist_panel((14.0, 4.9, 3.9, 2.0), cont, "Continuing common source",
                "a plateau until the source is removed", "drug")
pC.span(3, 22, token="highlight", text="source active", size="tiny", text_y=4.95 + 2.0 - 0.45)

# ---------------------------------------------------------------- D: the surveillance pyramid
bio.panel(ax, "D", (0.1, 3.7))
bio.label(ax, (9.5, 3.7), "What surveillance sees", size="title", bold=True)
levels = [("Infections", 1.00, "dna"), ("Symptomatic", 0.60, "enzyme"), ("Seek care", 0.25, "receptor"),
          ("Tested", 0.12, "drug"), ("Reported", 0.08, "negative")]
cx, top, hgt, half = 5.6, 3.15, 0.55, 4.1
for i, (name, frac, tok) in enumerate(levels):
    y1, y0 = top - i * hgt, top - (i + 1) * hgt
    w1 = half * (levels[i][1] ** 0.6)
    w0 = half * (levels[i + 1][1] ** 0.6) if i + 1 < len(levels) else half * (0.05 ** 0.6)
    ax.add_patch(Polygon([[cx - w1, y1], [cx + w1, y1], [cx + w0, y0], [cx - w0, y0]], closed=True,
                         facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=6))
    bio.label(ax, (cx, (y0 + y1) / 2), f"{name}  ({frac * 100:.0f} %)", size="tiny", color=P.on_fill())
bio.label(ax, (11.4, 2.6), "Each step loses cases, and each introduces a delay:", size="small", bold=True,
          ha="left")
for k2, t in enumerate(["asymptomatic infections are invisible without serology or wastewater testing",
                        "care-seeking depends on severity, access and cost",
                        "testing policy changes the multiplier overnight, which is why a rise in reported",
                        "cases must always be read beside the number of tests",
                        "reporting delay shifts the curve to the right, so the most recent days are incomplete"]):
    bio.label(ax, (11.4, 2.1 - k2 * 0.42), ("• " if k2 != 3 else "   ") + t, size="tiny", ha="left",
              color=P.muted())
