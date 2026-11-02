"""The course as a map: chapters 7.9.1-7.9.17 in three layers (measurement, networks, dynamics and
design), the main dependencies within each layer (arrows: the count model of 7.9.2 reused by
7.9.3-7.9.5, single cells extended to space and to trajectories, interaction and regulatory networks
analyzed and applied in 7.9.13, kinetic models used for the motifs of 7.9.15-7.9.17), the
passage from one layer to the next (thick arrows) and the earlier courses each layer draws on (right
column, dashed)."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(23, 13.2)

# ---------------------------------------------------------------- boxes
W8, H = 2.15, 1.35
meas = [
    (2, "Bulk\ntranscriptomics", "rna"),
    (3, "Gene-set\nanalysis", "rna"),
    (4, "RNA processing,\ntranslation", "mrna"),
    (5, "Single-cell\ntranscriptomics", "rna"),
    (6, "Spatial\nomics", "rna"),
    (7, "Trajectories\nand fates", "rna"),
    (8, "Epigenome,\n3D genome", "chromatin"),
    (9, "Proteome,\nmetabolome", "protein"),
]
nets = [
    (10, "Interactomes,\ngenetic interactions", "protein"),
    (11, "Inferring regulatory\nnetworks", "dna"),
    (12, "Network analysis,\nnetwork medicine", "neutral"),
    (13, "Cancer systems\nbiology", "negative"),
]
dyn = [
    (14, "Kinetic models:\nbuild, solve, fit", "enzyme"),
    (15, "Transcription networks,\nnetwork motifs", "dna"),
    (16, "Feedback, decisions,\noscillations", "receptor"),
    (17, "Noise, robustness,\nevolution, design", "highlight"),
]

pos = {}
Y_TOP, Y_M, Y_N, Y_D = 11.9, 9.3, 6.2, 3.1
x0, dx = 1.35, 2.42
for i, (n, t, tok) in enumerate(meas):
    pos[n] = (x0 + i * dx, Y_M)
xs4 = [2.4, 7.0, 12.6, 17.2]
for i, (n, t, tok) in enumerate(nets):
    pos[n] = (xs4[i], Y_N)
for i, (n, t, tok) in enumerate(dyn):
    pos[n] = (xs4[i], Y_D)
pos[1] = (9.8, Y_TOP)

wid = {**{n: W8 for n, _, _ in meas}, **{n: 3.6 for n, _, _ in nets + dyn}, 1: 6.4}
for n, t, tok in meas + nets + dyn + [(1, "Questions, data and methods", "neutral")]:
    x, y = pos[n]
    bio.box(ax, (x, y), wid[n], H, tok, text=f"{t}", size="small")
    bio.label(ax, (x - wid[n] / 2 + 0.08, y - H / 2 - 0.22), f"7.9.{n}", size="tiny", ha="left", color=P.muted())

# ---------------------------------------------------------------- layer labels and brackets
for y in (Y_M, Y_N, Y_D):
    ax.plot([0.02, 0.02], [y - 1.05, y + 1.05], color=P.muted(), lw=1.0)
for y, name in ((Y_M, "parts and states"), (Y_N, "wiring"), (Y_D, "behavior")):
    bio.label(ax, (-0.25, y), name, size="small", rotation=90, color=P.muted())

# ---------------------------------------------------------------- arrows within and between layers
def edge(a, b, bend=0.0, dashed=False, sa=(0, 0), sb=(0, 0)):
    (xa, ya), (xb, yb) = pos[a], pos[b]
    bio.arrow(ax, (xa + sa[0], ya + sa[1]), (xb + sb[0], yb + sb[1]), kind="process", bend=bend,
              dashed=dashed, color=P.muted(), lw=1.1)


top = H / 2 + 0.05
# chapter 1 introduces the three layers
bio.arrow(ax, (pos[1][0], Y_TOP - top), (pos[1][0], Y_M + top + 0.32), kind="process", color=P.muted(), lw=1.1)
# measurement row: the count model of 7.9.2 reused, single cells extended to space and dynamics
edge(2, 3, sa=(W8 / 2, 0), sb=(-W8 / 2, 0))
edge(2, 4, bend=0.3, sa=(0.3, top), sb=(-0.3, top))
edge(2, 5, bend=0.3, sa=(0.6, top), sb=(-0.5, top))
edge(5, 6, sa=(W8 / 2, 0), sb=(-W8 / 2, 0))
edge(5, 7, bend=0.3, sa=(0.5, top), sb=(-0.3, top))
# layer to layer: measured data become edges, edges become rate equations
for ya, yb, txt in ((Y_M, Y_N, "data become edges"), (Y_N, Y_D, "edges get rates")):
    xm = 9.8
    bio.arrow(ax, (xm, ya - top - 0.3), (xm, yb + top + 0.05), kind="process", color=P.muted(), lw=1.6)
    bio.label(ax, (xm + 0.15, (ya + yb) / 2 - 0.2), txt, size="tiny", ha="left", color=P.muted())
# networks row
edge(11, 12, sa=(1.8, 0), sb=(-1.8, 0))
edge(12, 13, sa=(1.8, 0), sb=(-1.8, 0))
# dynamics row
edge(14, 15, sa=(1.8, 0), sb=(-1.8, 0))
edge(15, 16, sa=(1.8, 0), sb=(-1.8, 0))
edge(16, 17, sa=(1.8, 0), sb=(-1.8, 0))

# ---------------------------------------------------------------- earlier courses (right column)
XR, WR = 21.3, 2.9
pre = [
    (Y_M + 0.75, "7.7 Biostatistics", Y_M),
    (Y_M - 0.75, "7.8 Bioinformatics", Y_M),
    (Y_N + 0.45, "1.4.7 Network science", Y_N),
    (Y_N - 0.95, "3.x Statistics,\n4.x Machine learning", Y_N),
    (Y_D + 0.75, "2.4 Differential\nequations", Y_D),
    (Y_D - 0.75, "7.6 Quantitative\nbiology", Y_D),
]
bio.label(ax, (XR, Y_TOP), "Earlier courses", size="small", bold=True)
for y, t, yt in pre:
    bio.box(ax, (XR, y), WR, 1.0 if "\n" in t else 0.7, "neutral", text=t, size="tiny")
xr_edge = {Y_M: x0 + 7 * dx + W8 / 2, Y_N: xs4[3] + 1.8, Y_D: xs4[3] + 1.8}
for y, t, yt in pre:
    bio.arrow(ax, (XR - WR / 2 - 0.05, y), (xr_edge[yt] + 0.12, yt + (y - yt) * 0.35), kind="process", dashed=True,
              color=P.muted(), lw=0.9)

bio.label(ax, (9.8, 0.9), "Arrows: one chapter uses the data, models or results of another; dashed: methods carried over from earlier courses",
          size="tiny", color=P.muted())
ax.set_xlim(-0.6, 23)
ax.set_ylim(0.4, 13.2)
