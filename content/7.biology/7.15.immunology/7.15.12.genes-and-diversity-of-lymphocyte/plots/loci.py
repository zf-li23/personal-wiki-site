# Immunoglobulin heavy- and light-chain loci and their rearrangement (human, simplified; segment numbers are not to scale).
# A: IGH: D-to-J, then V-to-DJ joining deletes the DNA between the selected segments; transcription of VDJ-Cmu and splicing
#    give the mRNA. Red ticks mark N/P nucleotides added at the two junctions.
# B: IGK: one joining step, V-to-J; the C segment is spliced to the joined VJ exon.
import wikibio as bio
from matplotlib.patches import Rectangle

P = bio.P
fig, ax = bio.canvas(23.0, 11.0)
H = 0.55
TOK = {"V": "channel", "D": "highlight", "J": "positive", "C": "negative"}


def seg(x, w, kind, y, on=True, text=None):
    tok = TOK[kind]
    ax.add_patch(Rectangle((x, y - H / 2), w, H, facecolor=P.fill(tok) if on else P.light(tok), edgecolor=P.edge(tok),
                           lw=0.9, zorder=6))
    if text:
        bio.label(ax, (x + w / 2, y), text, size="tiny", color=P.on_fill() if on else P.muted(), zorder=8)


def line(x0, x1, y):
    ax.plot([x0, x1], [y, y], color=P.edge("neutral"), lw=1.2, zorder=3)


def row_label(y, text):
    bio.label(ax, (0.2, y), text, size="small", ha="left", bold=True)


# ---- A  IGH ---------------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 10.9))
bio.label(ax, (11.5, 10.75), "Heavy-chain locus (IGH, chromosome 14)", size="title", bold=True)
vx = [3.2 + 0.85 * i for i in range(7)]       # V segments (about 40 functional in total)
dx = [10.2 + 0.7 * i for i in range(4)]       # D segments (about 23)
jx = [14.0 + 0.55 * i for i in range(4)]      # J segments (6)
cx = [17.0, 18.35, 19.7, 21.05]
cnames = ["Cμ", "Cδ", "Cγ", "Cα"]
SELV, SELD, SELJ = 5, 2, 1


def germline(y, selv=None, seld=None, selj=None):
    line(2.9, 22.2, y)
    for i, x in enumerate(vx):
        seg(x, 0.55, "V", y, on=(selv is None or i == selv), text=None)
    bio.label(ax, (vx[-1] + 0.95, y), "…", size="normal")
    for i, x in enumerate(dx):
        seg(x, 0.4, "D", y, on=(seld is None or i == seld))
    for i, x in enumerate(jx):
        seg(x, 0.35, "J", y, on=(selj is None or i == selj))
    for x, n in zip(cx, cnames):
        seg(x, 1.0, "C", y, text=n)


y1, y2, y3, y4 = 9.6, 8.0, 6.4, 4.9
row_label(y1 + 0.55, "germline")
germline(y1)
bio.label(ax, (vx[2], y1 + 0.55), "V$_\\mathrm{H}$ (~40)", size="tiny", color=P.muted())
bio.label(ax, (dx[1], y1 + 0.55), "D (~23)", size="tiny", color=P.muted())
bio.label(ax, (jx[1], y1 + 0.55), "J (6)", size="tiny", color=P.muted())
# 1  D to J: the DNA between the selected D and J is deleted
row_label(y2 + 0.55, "① D–J joining")
line(2.9, 22.2, y2)
for x in vx:
    seg(x, 0.55, "V", y2, on=False)
bio.label(ax, (vx[-1] + 0.95, y2), "…", size="normal")
seg(10.2, 0.4, "D", y2); seg(10.6, 0.35, "J", y2)
ax.add_patch(Rectangle((10.56, y2 - H / 2), 0.08, H, facecolor=P.fill("negative"), edgecolor="none", zorder=9))
for x, n in zip(cx, cnames):
    seg(x, 1.0, "C", y2, text=n)
bio.label(ax, (6.3, y2 + 0.5), "D and J segments between the selected ones are deleted", size="tiny", ha="left", color=P.muted())
# 2  V to DJ
row_label(y3 + 0.55, "② V–DJ joining")
line(2.9, 22.2, y3)
seg(3.2, 0.55, "V", y3); seg(3.75, 0.4, "D", y3); seg(4.15, 0.35, "J", y3)
for xx in (3.72, 4.12):
    ax.add_patch(Rectangle((xx, y3 - H / 2), 0.08, H, facecolor=P.fill("negative"), edgecolor="none", zorder=9))
for x, n in zip(cx, cnames):
    seg(x, 1.0, "C", y3, text=n)
bio.label(ax, (6.3, y3 + 0.45), "red: N / P nucleotides at the two junctions; V segments between are deleted", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (3.9, y3 - 0.45), (3.9, y4 + 0.55), kind="process")
bio.label(ax, (4.4, (y3 + y4) / 2), "transcription, splicing", size="tiny", ha="left", color=P.muted())
row_label(y4 + 0.55, "③ mRNA")
seg(3.2, 0.55, "V", y4); seg(3.75, 0.4, "D", y4); seg(4.15, 0.35, "J", y4); seg(4.5, 1.0, "C", y4, text="Cμ")
bio.label(ax, (6.3, y4), "μ heavy chain (V$_\\mathrm{H}$–D–J–C$_\\mathrm{H}$)", size="tiny", ha="left")

# ---- B  IGK ---------------------------------------------------------------------------------------------------
bio.panel(ax, "B", (0.1, 3.7))
bio.label(ax, (11.5, 3.55), "Light-chain locus (IGK, chromosome 2)", size="title", bold=True)
kv = [3.2 + 0.85 * i for i in range(7)]
kj = [14.0 + 0.55 * i for i in range(5)]
yb1, yb2 = 2.2, 0.8
row_label(yb1 + 0.55, "germline")
line(2.9, 22.2, yb1)
for i, x in enumerate(kv):
    seg(x, 0.55, "V", yb1)
bio.label(ax, (kv[-1] + 0.95, yb1), "…", size="normal")
bio.label(ax, (kv[2], yb1 + 0.55), "V$_\\kappa$ (~35)", size="tiny", color=P.muted())
for x in kj:
    seg(x, 0.35, "J", yb1)
bio.label(ax, (kj[2], yb1 + 0.55), "J$_\\kappa$ (5)", size="tiny", color=P.muted())
seg(17.4, 1.0, "C", yb1, text="Cκ")
row_label(yb2 + 0.55, "rearranged")
line(2.9, 22.2, yb2)
seg(3.2, 0.55, "V", yb2); seg(3.75, 0.35, "J", yb2)
ax.add_patch(Rectangle((3.71, yb2 - H / 2), 0.08, H, facecolor=P.fill("negative"), edgecolor="none", zorder=9))
seg(17.4, 1.0, "C", yb2, text="Cκ")
bio.label(ax, (6.3, yb2 + 0.5), "κ light chain (V$_\\kappa$–J–C$_\\kappa$); one junction", size="tiny", ha="left", color=P.muted())
