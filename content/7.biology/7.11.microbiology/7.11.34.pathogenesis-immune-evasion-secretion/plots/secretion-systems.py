# The secretion systems of a Gram-negative bacterium, drawn against the envelope (T1SS-T6SS, Sec and Tat).
import numpy as np
from matplotlib.patches import Circle, Polygon, Rectangle

import wikibio as bio
from wikibio import microbio as M

P = bio.P
fig, ax = bio.canvas(19.0, 9.4)
bio.label(ax, (9.5, 9.15), "Protein secretion across the Gram-negative envelope", size="title", bold=True)

IM, OM = 1.9, 4.6          # mid-planes of the inner and outer membranes
X0, X1 = 0.5, 18.5

# background bands: cytoplasm, periplasm, outside
ax.add_patch(Rectangle((X0, 0.4), X1 - X0, IM - 0.4, facecolor=P.fill("cytoplasm"), edgecolor="none", zorder=0))
ax.add_patch(Rectangle((X0, IM), X1 - X0, OM - IM, facecolor=P.mix(P.fill("extracellular"), P.fill("carbohydrate"), 0.25),
                       edgecolor="none", zorder=0))
ax.add_patch(Rectangle((X0, OM), X1 - X0, 2.6, facecolor=P.fill("extracellular"), edgecolor="none", zorder=0))
bio.label(ax, (X0 + 0.1, 1.28), "cytoplasm", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (X0 + 0.1, 3.95), "periplasm", size="tiny", color=P.muted(), ha="left")
bio.label(ax, (X0 + 0.1, 6.6), "outside", size="tiny", color=P.muted(), ha="left")

systems = [(1.9, "Sec / Tat"), (4.3, "T2SS"), (6.5, "T5SS"), (9.0, "T1SS"), (11.4, "T3SS"), (14.0, "T4SS"),
           (16.7, "T6SS")]
gaps_im = [(c - 0.55, c + 0.55) for c, _ in systems]
gaps_om = [(c - 0.55, c + 0.55) for c, _ in systems if _ != "Sec / Tat"]
M.bilayer(ax, X0, X1, IM, skip=gaps_im, zorder=5)
M.bilayer(ax, X0, X1, OM, skip=gaps_om, zorder=5)
M.peptidoglycan(ax, X0 + 0.2, X1 - 0.2, 3.25, layers=1, spacing=0.3, zorder=4)


def channel(c, lo, hi, token="channel", width=0.92, taper=0.0):
    """A pore drawn as two posts between lo and hi."""
    for s in (-1, 1):
        ax.add_patch(Polygon([[c + s * width / 2, lo], [c + s * (width / 2 + taper), hi],
                              [c + s * (width / 2 + taper) - s * 0.2, hi], [c + s * width / 2 - s * 0.2, lo]],
                             closed=True, facecolor=P.fill(token), edgecolor=P.edge(token), lw=1.0, zorder=10))


def cargo(c, y, token="protein", r=0.17):
    ax.add_patch(Circle((c, y), r, facecolor=P.fill(token), edgecolor=P.edge(token), lw=0.9, zorder=14))


def name(c, text, sub):
    bio.label(ax, (c, 8.45), text, size="small", bold=True)
    bio.label(ax, (c, 8.05), sub, size="tiny", color=P.muted())


# ---------------------------------------------------------------- Sec / Tat (inner membrane only)
c = 1.9
channel(c - 0.35, IM - 0.45, IM + 0.45, token="enzyme", width=0.55)
channel(c + 0.45, IM - 0.45, IM + 0.45, token="receptor", width=0.55)
bio.label(ax, (c - 0.45, IM - 0.95), "SecYEG", size="tiny")
bio.label(ax, (c + 0.6, IM - 0.95), "TatABC", size="tiny")
cargo(c - 0.45, 0.72, "protein")
bio.strand(ax, (c - 0.7, 2.75), (c, 2.75), token="protein", wave=0.09, ends=False)
bio.protein(ax, (c + 0.45, 2.8), 0.5, 0.4, "protein", text=None)
bio.arrow(ax, (c - 0.35, 1.15), (c - 0.35, IM - 0.5), kind="process")
bio.arrow(ax, (c + 0.45, 1.15), (c + 0.45, IM - 0.5), kind="process")
cargo(c + 0.6, 0.72, "protein")
name(c, "Sec / Tat", "inner membrane only")

# ---------------------------------------------------------------- T2SS
c = 4.3
channel(c, OM - 0.45, OM + 0.55, token="channel", width=1.0)
for k in range(4):
    ax.add_patch(Circle((c, IM + 0.5 + k * 0.42), 0.17, facecolor=P.fill("enzyme"), edgecolor=P.edge("enzyme"),
                        lw=0.8, zorder=11))
cargo(c, 3.95, "drug")
cargo(c, 5.6, "drug")
bio.arrow(ax, (c, 4.2), (c, 5.3), kind="process")
name(c, "T2SS", "Sec, then a secretin")

# ---------------------------------------------------------------- T5SS
c = 6.5
channel(c, OM - 0.45, OM + 0.45, token="receptor", width=0.8)
cargo(c, 3.6, "drug")
bio.arrow(ax, (c, 3.9), (c, 5.2), kind="process")
bio.protein(ax, (c, 5.6), 0.7, 0.45, "drug", text=None)
name(c, "T5SS", "autotransporter")

# ---------------------------------------------------------------- T1SS
c = 9.0
channel(c, IM - 0.45, IM + 0.45, token="enzyme", width=0.9)
channel(c, OM - 0.45, OM + 0.45, token="channel", width=0.9)
ax.add_patch(Rectangle((c - 0.34, IM + 0.4), 0.68, OM - IM - 0.8, facecolor=P.light("channel"),
                       edgecolor=P.edge("channel"), lw=0.9, zorder=9))
cargo(c, 1.0, "drug")
bio.arrow(ax, (c, 1.25), (c, 5.4), kind="process")
cargo(c, 5.7, "drug")
name(c, "T1SS", "one step out")

# ---------------------------------------------------------------- T3SS: the needle
c = 11.4
channel(c, IM - 0.45, IM + 0.45, token="enzyme", width=1.0)
channel(c, OM - 0.5, OM + 0.3, token="channel", width=1.0)
ax.add_patch(Rectangle((c - 0.4, IM + 0.4), 0.8, OM - IM - 0.7, facecolor=P.light("enzyme"),
                       edgecolor=P.edge("enzyme"), lw=0.9, zorder=9))
ax.add_patch(Rectangle((c - 0.13, OM + 0.25), 0.26, 1.55, facecolor=P.fill("channel"), edgecolor=P.edge("channel"),
                       lw=0.9, zorder=11))
ax.add_patch(Rectangle((c - 0.9, 6.85), 1.8, 0.35, facecolor=P.fill("animal"), edgecolor=P.edge("animal"),
                       lw=1.0, zorder=11))
bio.label(ax, (c, 7.45), "host cell", size="tiny", color=P.muted())
cargo(c, 1.0, "drug")
bio.arrow(ax, (c, 1.25), (c, 6.75), kind="process")
name(c, "T3SS", "injects effectors")

# ---------------------------------------------------------------- T4SS
c = 14.0
channel(c, IM - 0.45, IM + 0.45, token="enzyme", width=1.1)
channel(c, OM - 0.5, OM + 0.4, token="channel", width=1.1)
ax.add_patch(Rectangle((c - 0.45, IM + 0.4), 0.9, OM - IM - 0.8, facecolor=P.light("channel"),
                       edgecolor=P.edge("channel"), lw=0.9, zorder=9))
ax.add_patch(Rectangle((c - 0.1, OM + 0.3), 0.2, 1.5, facecolor=P.fill("cell_wall"), edgecolor=P.edge("cell_wall"),
                       lw=0.9, zorder=11))
bio.dna(ax, (c - 1.3, 1.1), (c - 0.3, 1.1), style="duplex", width=0.3, ends=False)
cargo(c + 0.45, 1.1, "drug")
bio.arrow(ax, (c, 1.4), (c, 6.3), kind="process")
name(c, "T4SS", "protein and DNA")

# ---------------------------------------------------------------- T6SS
c = 16.7
channel(c, IM - 0.45, IM + 0.45, token="enzyme", width=1.2)
channel(c, OM - 0.5, OM + 0.4, token="channel", width=1.2)
for k in range(5):           # the contractile sheath
    ax.add_patch(Rectangle((c - 0.55, IM + 0.5 + k * 0.42), 1.1, 0.32, facecolor=P.fill("muscle"),
                           edgecolor=P.edge("muscle"), lw=0.8, zorder=9))
ax.add_patch(Rectangle((c - 0.14, IM + 0.5), 0.28, 4.3, facecolor=P.fill("channel"), edgecolor=P.edge("channel"),
                       lw=0.9, zorder=10))
ax.add_patch(Polygon([[c - 0.3, 6.5], [c + 0.3, 6.5], [c, 7.05]], closed=True, facecolor=P.fill("negative"),
                     edgecolor=P.edge("negative"), lw=1.0, zorder=12))
ax.add_patch(Rectangle((c - 1.0, 7.1), 2.0, 0.35, facecolor=P.fill("bacterium"), edgecolor=P.edge("bacterium"),
                       lw=1.0, zorder=11))
bio.label(ax, (c - 1.15, 7.28), "another\nbacterium", size="tiny", color=P.muted(), ha="right")
name(c, "T6SS", "contractile tail")

bio.label(ax, (9.5, 0.15), "red-filled cargo: the exported protein. Systems left of the dashed division need Sec or Tat "
                           "first; those to the right export in one step from the cytoplasm", size="tiny",
          color=P.muted())
ax.plot([7.75, 7.75], [0.55, 7.75], color=P.muted(), lw=0.9, ls=(0, (4, 3)), zorder=16)
