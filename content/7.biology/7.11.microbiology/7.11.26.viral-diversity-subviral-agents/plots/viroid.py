# Viroids: structure, rolling-circle replication and pathogenesis by RNA silencing.
# A: the rod-like secondary structure of a Pospiviroidae genome (schematic, 359 nt for PSTVd), with
#    the five domains and the central conserved region.
# B: rolling-circle replication in the two families.
# C: pathogenesis - replication intermediates are processed into siRNAs that silence host mRNAs.
import numpy as np

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(17.4, 8.8)

# --- A  the rod ----------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.55))
bio.label(ax, (5.6, 8.55), "A circular RNA folded into a rod", size="title", bold=True)

x0, x1, y = 1.0, 10.2, 7.1
rng = np.random.default_rng(0)
t = np.linspace(0, 1, 400)
xs = x0 + t * (x1 - x0)
half = 0.16 + 0.05 * np.sin(2 * np.pi * 7 * t) ** 2          # small internal loops
top = np.stack([xs, y + half], 1)
bot = np.stack([xs[::-1], y - half[::-1]], 1)
bio.shape(ax, np.concatenate([top, bot]), token="rna", lw=1.2, zorder=6)
for k in np.linspace(0.02, 0.98, 46):                         # base pairs
    xk = x0 + k * (x1 - x0)
    hk = np.interp(xk, xs, half)
    ax.plot([xk, xk], [y - hk + 0.045, y + hk - 0.045], color=P.edge("rna"), lw=0.5, zorder=7)
ax.add_patch(__import__("matplotlib.patches", fromlist=["Rectangle"]).Rectangle(
    (x0 + 0.40 * (x1 - x0), y - 0.42), 0.13 * (x1 - x0), 0.84,
    facecolor=P.light("highlight"), edgecolor=P.edge("highlight"), lw=0.8, zorder=4))
for frac, dyl, name in ((0.08, 0.55, "terminal left"), (0.26, 0.95, "pathogenicity"),
                        (0.465, 0.55, "central conserved region"), (0.68, 0.95, "variable"),
                        (0.92, 0.55, "terminal right")):
    bio.callout(ax, (x0 + frac * (x1 - x0), y + 0.22), (x0 + frac * (x1 - x0), y + dyl), name)
bio.label(ax, (5.6, 5.85), "246–401 nucleotides, covalently closed, no open reading frame; "
                           "the intramolecular pairing makes it stable outside the cell",
          size="tiny", color=P.muted())
bio.label(ax, (14.0, 7.6), "no capsid → no receptor:\nentry only through wounds,\nspread through "
                           "plasmodesmata\nand the phloem", size="small", color=P.muted())

# --- B  rolling circle ---------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 5.3))
bio.label(ax, (4.4, 5.15), "Rolling-circle replication", size="title", bold=True)

cx, cy, r = 1.9, 3.1, 0.62
th = np.linspace(0, 2 * np.pi, 200)
bio.shape(ax, np.stack([cx + r * np.cos(th), cy + r * np.sin(th)], 1), token="rna", lw=1.3, fill=False)
bio.label(ax, (cx, cy), "(+)", size="tiny")
bio.label(ax, (cx, cy - 1.1), "circular genome", size="tiny", color=P.muted())

bio.arrow(ax, (cx + 0.85, cy), (cx + 1.75, cy), kind="process")
bio.label(ax, (cx + 1.3, cy + 0.42), "host RNA\npolymerase", size="tiny", color=P.muted())

bio.strand(ax, (4.4, cy + 0.25), (7.6, cy + 0.25), token="rna", wave=0.07)
bio.strand(ax, (4.4, cy - 0.25), (7.6, cy - 0.25), token="mrna", wave=0.07)
bio.label(ax, (6.0, cy + 0.72), "concatemeric (−) strand", size="tiny", color=P.muted())
bio.label(ax, (6.0, cy - 0.66), "concatemeric (+) strands", size="tiny", color=P.muted())

for xk in (5.2, 6.0, 6.8):
    bio.arrow(ax, (xk, cy - 1.30), (xk, cy - 0.82), kind="process", color=P.edge("negative"))
bio.label(ax, (6.0, cy - 1.60), "cleavage to unit length", size="tiny", color=P.edge("negative"))

bio.arrow(ax, (7.9, cy), (8.7, cy), kind="process")
th2 = np.linspace(0, 2 * np.pi, 200)
bio.shape(ax, np.stack([9.5 + 0.5 * np.cos(th2), cy + 0.5 * np.sin(th2)], 1), token="rna", lw=1.3, fill=False)
bio.label(ax, (9.5, cy - 0.95), "ligation to a\nnew circle", size="tiny", color=P.muted())

bio.box(ax, (3.1, 0.72), 5.8, 0.92, token="neutral", radius=0.18)
bio.label(ax, (3.1, 0.92), "Pospiviroidae: nucleus, RNA polymerase II,", size="tiny", color=P.on_fill())
bio.label(ax, (3.1, 0.57), "cleavage by host RNase III, ligation by DNA ligase I", size="tiny", color=P.on_fill())
bio.box(ax, (9.4, 0.72), 6.6, 0.92, token="highlight", radius=0.18)
bio.label(ax, (9.4, 0.92), "Avsunviroidae: chloroplast, nuclear-encoded polymerase,", size="tiny", color=P.on_fill())
bio.label(ax, (9.4, 0.57), "self-cleavage by a hammerhead ribozyme, tRNA ligase", size="tiny", color=P.on_fill())

# --- C  silencing --------------------------------------------------------------------------------------
bio.panel(ax, "C", (11.4, 5.3))
bio.label(ax, (14.6, 5.15), "Disease by RNA silencing", size="title", bold=True)

bio.strand(ax, (12.1, 4.5), (14.8, 4.5), token="rna", wave=0.06)
bio.strand(ax, (12.1, 4.28), (14.8, 4.28), token="mrna", wave=0.06)
bio.label(ax, (16.4, 4.4), "double-stranded\nreplication\nintermediate", size="tiny", color=P.muted())
bio.arrow(ax, (13.6, 4.0), (13.6, 3.45), kind="process")
bio.label(ax, (14.3, 3.72), "Dicer-like", size="tiny", color=P.muted())
for k in range(4):
    xk = 12.3 + k * 0.85
    bio.strand(ax, (xk, 3.15), (xk + 0.6, 3.15), token="rna", wave=0.05, ends=False)
bio.label(ax, (15.9, 3.15), "siRNAs", size="tiny", color=P.muted())
bio.arrow(ax, (13.6, 2.85), (13.6, 2.35), kind="process")
bio.label(ax, (15.3, 2.6), "loaded into the\nsilencing complex", size="tiny", color=P.muted())
bio.strand(ax, (12.1, 2.0), (15.6, 2.0), token="mrna", wave=0.06, cap=True, polya=True)
bio.label(ax, (13.6, 1.62), "host mRNA with partial complementarity", size="tiny", color=P.muted())
bio.arrow(ax, (14.0, 1.55), (14.0, 1.1), kind="inhibition", color=P.edge("negative"))
bio.label(ax, (14.6, 0.78), "cleavage → chlorosis, stunting,\nleaf and fruit deformation",
          size="tiny", color=P.edge("negative"))
