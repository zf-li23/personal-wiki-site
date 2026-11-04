"""Four types of prokaryotic cell envelope in cross-section: Gram-positive, Gram-negative, acid-fast
(mycobacterial) and archaeal S-layer envelope (schematic)."""
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(34, 12)
Y, TOP = 3.2, 10.0


def header(x0, letter, title):
    bio.panel(ax, letter, (x0 - 0.6, 11.8))
    bio.label(ax, (x0 + 2.5, 11.5), title, size="normal", bold=True)


def sides(x1, bottom):
    bio.label(ax, (x1 - 0.1, TOP - 0.25), "Outside", size="tiny", ha="right", va="top", color=P.muted())
    bio.label(ax, (x1 - 0.1, bottom + 0.15), "Cytoplasm", size="tiny", ha="right", va="bottom", color=P.muted())


def band(x0, x1, y0, y1, color, z=5):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=color, edgecolor="none", zorder=z))


# A: Gram-positive
x0, x1 = 1.0, 6.4
header(x0, "A", "Gram-positive")
A = M.envelope(ax, x0, x1, Y, kind="gram+", top=TOP, seed=4)
sides(x1, A["bottom"])
c = x1 + 0.3
bio.callout(ax, A["wta"][-1][1], (c, TOP - 0.9), "Teichoic acid")
bio.callout(ax, (x1 - 0.4, (A["pg_lo"] + A["pg_hi"]) / 2), (c, (A["pg_lo"] + A["pg_hi"]) / 2), "Peptidoglycan")
bio.callout(ax, (x1 - 0.3, A["im_hi"] - 0.1), (c, A["im"]), "Membrane")

# B: Gram-negative
x0, x1 = 9.4, 14.8
header(x0, "B", "Gram-negative")
B = M.envelope(ax, x0, x1, Y, kind="gram-", top=TOP, seed=5)
sides(x1, B["bottom"])
c = x1 + 0.3
tip = max(B["lps_tips"], key=lambda t: t[0] + 0.3 * t[1])
bio.callout(ax, (tip[0] + 0.05, tip[1] - 0.3), (c, B["om_hi"] + 1.1), "LPS")
bio.callout(ax, (x1 - 0.3, B["om"]), (c, B["om"]), "Outer membrane")
bio.callout(ax, (B["porins"][1] + 0.3, B["om"]), (c, B["om"] - 0.6), "Porin")
bio.callout(ax, (x1 - 1.5, B["pg_lo"] + 0.05), (c, B["pg_lo"] - 0.1), "Peptidoglycan")
bio.callout(ax, (x1 - 0.4, B["im"] + 0.7), (c, B["im"] + 0.75), "Periplasm")
bio.callout(ax, (x1 - 0.3, B["im_hi"] - 0.1), (c, B["im"]), "Inner membrane")

# C: acid-fast (mycobacterial)
x0, x1 = 17.8, 23.2
header(x0, "C", "Acid-fast (mycobacteria)")
band(x0, x1, Y - 1.3, Y, P.fill("cytoplasm"))
band(x0, x1, Y, TOP, P.fill("extracellular"))
lo, hi = M.bilayer(ax, x0, x1, Y, zorder=6)
pg_lo = hi + 0.4
pg_hi = M.peptidoglycan(ax, x0, x1, pg_lo, layers=2, spacing=0.3, seed=7, zorder=7)
# arabinogalactan: branched sugar chains rising from peptidoglycan
ag_lo, ag_hi = pg_hi + 0.15, pg_hi + 1.5
rng = np.random.default_rng(3)
xs = np.arange(x0 + 0.2, x1 - 0.1, 0.22)
for xx in xs:
    yy = np.linspace(ag_lo, ag_hi, 6)
    jit = xx + 0.05 * np.sin(np.arange(6) * 1.7 + xx * 3)
    ax.plot(jit, yy, color=P.edge("carbohydrate"), lw=0.8, zorder=7)
    for a, b in zip(jit, yy):
        ax.plot([a], [b], "h", ms=3.2, color=P.fill("carbohydrate"), markeredgecolor=P.edge("carbohydrate"),
                markeredgewidth=0.4, zorder=8)
# mycolic acids: long chains forming the inner leaflet of the mycomembrane
my_lo, my_hi = ag_hi + 0.05, ag_hi + 1.55
for xx in xs:
    for dx in (-0.04, 0.04):
        ax.plot([xx + dx, xx + dx], [my_lo, my_hi], color=P.edge("lipid_tail"), lw=0.9, zorder=8)
# outer leaflet: free glycolipids (heads up)
M.leaflet(ax, x0, x1, my_hi, side=1, zorder=8)
sides(x1, Y - 1.3)
c = x1 + 0.3
bio.callout(ax, (x1 - 0.3, my_hi + 0.55), (c, my_hi + 1.1), "Free glycolipids")
bio.callout(ax, (x1 - 0.3, (my_lo + my_hi) / 2), (c, (my_lo + my_hi) / 2), "Mycolic acids")
bio.callout(ax, (x1 - 0.3, (ag_lo + ag_hi) / 2), (c, (ag_lo + ag_hi) / 2), "Arabinogalactan")
bio.callout(ax, (x1 - 0.3, (pg_lo + pg_hi) / 2), (c, (pg_lo + pg_hi) / 2 - 0.15), "Peptidoglycan")
bio.callout(ax, (x1 - 0.3, hi - 0.1), (c, Y - 0.15), "Membrane")
bio.label(ax, (x0 + 0.1, my_hi + 0.85), "mycomembrane", size="tiny", ha="left", color=P.muted())

# D: archaeal S-layer
x0, x1 = 26.2, 31.6
header(x0, "D", "Archaeon with S-layer")
band(x0, x1, Y - 1.3, Y, P.fill("cytoplasm"))
lo, hi = M.bilayer(ax, x0, x1, Y, zorder=6)
s_lo, s_hi = hi + 1.6, hi + 2.3
band(x0, x1, hi, s_lo, M.periplasm_color())
band(x0, x1, s_lo, TOP, P.fill("extracellular"))
xs = np.arange(x0 + 0.3, x1 - 0.2, 0.62)
for xx in xs:
    ax.plot([xx, xx], [hi - 0.05, s_lo], color=P.edge("protein"), lw=1.6, zorder=7)
    ax.add_patch(FancyBboxPatch((xx - 0.26, s_lo), 0.52, s_hi - s_lo, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.9, zorder=8))
    for k in range(3):
        ax.plot([xx - 0.12 + 0.12 * k], [s_hi + 0.12], "h", ms=3.0, color=P.fill("carbohydrate"),
                markeredgecolor=P.edge("carbohydrate"), markeredgewidth=0.4, zorder=8)
sides(x1, Y - 1.3)
c = x1 + 0.3
bio.callout(ax, (x1 - 0.5, s_hi + 0.12), (c, s_hi + 0.8), "Glycans")
bio.callout(ax, (x1 - 0.45, (s_lo + s_hi) / 2), (c, (s_lo + s_hi) / 2), "S-layer protein")
bio.callout(ax, (x1 - 0.75, (hi + s_lo) / 2), (c, (hi + s_lo) / 2 - 0.1), "Quasi-periplasm")
bio.callout(ax, (x1 - 0.3, hi - 0.1), (c, Y - 0.15), "Membrane\n(ether lipids)")
