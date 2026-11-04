# DNA uptake in natural transformation (schematic; proteins named for Bacillus subtilis and Streptococcus
# pneumoniae on the left, for Neisseria and Vibrio on the right).
# A, Gram-positive: a type IV competence pseudopilus (ComGC) reaches through the thick wall and pulls bound
#    double-stranded DNA to the membrane receptor ComEA; a nuclease (EndA in S. pneumoniae) degrades one
#    strand and the other is threaded through the ComEC channel, driven by the ATPase ComFA.
# B, Gram-negative: a type IV pilus extends through the PilQ secretin of the outer membrane, binds DNA and
#    retracts (PilT ATPase), pulling the double strand into the periplasm, where ComEA binding ratchets it
#    inward; a single strand crosses the inner membrane through ComEC (ComA in Neisseria).
# In both, the incoming strand is coated by DprA and SsbB, loaded with RecA, and recombines with the
# homologous region of the chromosome.
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(26.0, 11.0)
Y = 3.0  # inner membrane mid-plane


def band(x0, x1, y0, y1, color, z=1):
    ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, facecolor=color, edgecolor="none", zorder=z))


def channel(x, y, h, tok, text, at, w=0.62, ha="left"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=1.0, zorder=12))
    bio.label(ax, at, text, size="tiny", ha=ha)


def pilus(x, y0, y1, tok="enzyme"):
    for yy in np.arange(y0, y1, 0.2):
        ax.add_patch(bio.core.Circle((x, yy), 0.13, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.6, zorder=11))


def cytoplasm_part(x0, x1, xin, name_x):
    # single strand entering, coated by DprA/RecA, pairing with the chromosome
    bio.strand(ax, (xin, Y - 0.45), (xin + 1.6, 1.45), token="dna", ends=False, zorder=12)
    for k in range(5):
        t = 0.2 + 0.16 * k
        p = (xin + 1.6 * t, Y - 0.45 + (1.45 - Y + 0.45) * t)
        ax.add_patch(bio.core.Circle(p, 0.11, facecolor=P.fill("protein"), edgecolor=P.edge("protein"), lw=0.6, zorder=13))
    bio.dna(ax, (x0 + 0.4, 0.85), (x1 - 0.4, 0.85), style="duplex", width=0.22, ends=False, zorder=10)
    bio.label(ax, (name_x, 1.55), "RecA-coated single strand\nsearches for homology", size="tiny", ha="left")
    bio.label(ax, (x1 - 0.5, 0.35), "chromosome", size="tiny", ha="right", color=P.muted())


# ---------------- A: Gram-positive -------------------------------------------------------------------
x0, x1 = 0.4, 12.4
band(x0, x1, 0.2, Y, P.fill("cytoplasm"))
band(x0, x1, Y, 10.2, P.fill("extracellular"))
xs_ch = 6.6
M.bilayer(ax, x0, x1, Y, skip=[(xs_ch - 0.42, xs_ch + 0.42), (3.4, 3.8)], zorder=6)
pg_top = M.peptidoglycan(ax, x0, x1, Y + 0.9, layers=6, spacing=0.36, seed=3, zorder=7)
bio.label(ax, (x1 - 0.1, pg_top + 0.35), "thick peptidoglycan", size="tiny", ha="right", color=P.muted())
pilus(3.6, Y - 0.3, pg_top + 2.3)
bio.callout(ax, (3.6, pg_top + 1.6), (1.6, pg_top + 2.6), "ComGC\npseudopilus", size="tiny")
bio.dna(ax, (3.75, pg_top + 2.3), (8.8, pg_top + 3.6), style="helix", width=0.32, ends=False, zorder=12)
bio.label(ax, (9.0, pg_top + 3.85), "double-stranded DNA", size="tiny", ha="left")
bio.protein(ax, (5.6, Y + 0.6), 0.8, 0.55, token="receptor", text="ComEA", zorder=13)
channel(xs_ch, Y, 1.0, "channel", "ComEC channel", (xs_ch + 0.45, Y - 0.62))
bio.protein(ax, (8.0, Y + 0.6), 0.8, 0.5, token="drug", text="EndA", zorder=13)
for k in range(5):
    ax.add_patch(bio.core.Circle((8.6 + 0.22 * k, Y + 0.62 + 0.08 * (k % 2)), 0.05, color=P.edge("dna"), zorder=13))
bio.label(ax, (9.8, Y + 0.65), "degraded strand", size="tiny", ha="left", color=P.muted())
bio.dna(ax, (5.6, Y + 0.95), (6.6, Y + 0.75), style="duplex", width=0.18, ends=False, zorder=12)
bio.protein(ax, (xs_ch - 0.75, Y - 0.85), 0.75, 0.45, token="atp", text="ComFA", zorder=13)
bio.label(ax, (xs_ch - 1.25, Y - 0.85), "(ATPase)", size="tiny", ha="right")
cytoplasm_part(x0, x1, xs_ch, xs_ch + 2.3)
bio.label(ax, (x0, 10.6), "A   Gram-positive", size="small", bold=True, ha="left")

# ---------------- B: Gram-negative -------------------------------------------------------------------
x0, x1 = 13.4, 25.6
OM = Y + 2.6
band(x0, x1, 0.2, Y, P.fill("cytoplasm"))
band(x0, x1, Y, OM, M.periplasm_color())
band(x0, x1, OM, 10.2, P.fill("extracellular"))
xp, xc = 16.4, 20.2
M.bilayer(ax, x0, x1, Y, skip=[(xp - 0.42, xp + 0.42), (xc - 0.42, xc + 0.42)], zorder=6)
M.bilayer(ax, x0, x1, OM, skip=[(xp - 0.6, xp + 0.6)], zorder=6)
M.peptidoglycan(ax, x0, x1, Y + 1.5, layers=1, seed=5, zorder=7)
bio.label(ax, (x1 - 0.1, OM + 0.75), "outer membrane", size="tiny", ha="right", color=P.muted())
bio.label(ax, (x1 - 0.1, Y + 1.15), "periplasm", size="tiny", ha="right", color=P.muted())
channel(xp, OM, 1.0, "channel", "PilQ secretin", (xp - 0.6, OM + 0.8), w=0.9, ha="right")
pilus(xp, Y - 0.2, OM + 2.6)
bio.dna(ax, (xp + 0.15, OM + 2.6), (xp + 4.2, OM + 3.8), style="helix", width=0.32, ends=False, zorder=12)
bio.label(ax, (xp + 0.75, OM + 1.6), "pilus binds DNA\nand retracts", size="tiny", ha="left")
bio.arrow(ax, (xp + 0.45, OM + 2.4), (xp + 0.45, OM + 0.8), kind="process", lw=1.0, head=0.16)
bio.protein(ax, (xp, Y - 0.8), 0.9, 0.45, token="atp", text="PilT", zorder=13)
bio.label(ax, (xp - 0.6, Y - 0.8), "(retraction ATPase)", size="tiny", ha="right")
# dsDNA in the periplasm held by ComEA
bio.dna(ax, (xp + 0.6, OM - 0.6), (xc - 0.3, Y + 0.9), style="duplex", width=0.18, ends=False, zorder=12)
for k in range(3):
    p = (xp + 1.3 + 0.75 * k, OM - 0.75 - 0.35 * k)
    bio.protein(ax, p, 0.5, 0.35, token="receptor", zorder=13)
bio.label(ax, (xp + 3.7, Y + 1.0), "ComEA binds DNA:\na ratchet into the periplasm", size="tiny", ha="left")
channel(xc, Y, 1.0, "channel", "ComEC (ComA)", (xc + 0.45, Y - 0.62))
cytoplasm_part(x0, x1, xc, xc + 2.3)
bio.label(ax, (x0, 10.6), "B   Gram-negative", size="small", bold=True, ha="left")
bio.label(ax, (0.5, 9.6), "Outside", size="tiny", ha="left", color=P.muted())
bio.label(ax, (0.5, 2.1), "Cytoplasm", size="tiny", ha="left", color=P.muted())
