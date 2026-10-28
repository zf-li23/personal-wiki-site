"""The breakage-fusion-bridge cycle drawn on a lettered chromosome A B o C D E F that has lost its right
telomere: replication, fusion of the sister chromatids at their broken ends (a dicentric chromatid), the
anaphase bridge, breakage at a random point, and the two daughter chromosomes, one with an inverted
duplication and one with a larger deletion, both again with broken ends."""
import wikibio as bio
from wikibio import cytogenetics as C

fig, ax = bio.canvas(20.0, 9.6)
P = bio.P
U = 0.52
N = ["A", "B", "o", "C", "D", "E", "F"]
BROKEN = P.edge("negative")


def broken_end(x, y, h=0.34):
    """A red tick marking a broken chromosome end without a telomere."""
    ax.plot([x, x], [y - h * 0.62, y + h * 0.62], color=BROKEN, lw=3.0, zorder=20)


def step(y, text):
    bio.label(ax, (0.3, y), text, size="small", ha="left")


# 1: the broken chromosome
step(8.9, "1  Chromosome without its right telomere")
o = C.lettered(ax, (9.2, 8.9), N, unit=U)
broken_end(o["x1"], 8.9)
bio.label(ax, (o["x1"] + 0.3, 8.9), "broken end", size="tiny", color=P.muted(), ha="left")

# 2: replication
step(7.55, "2  Replication: two sister chromatids")
a = C.lettered(ax, (9.2, 7.8), N, unit=U)
b = C.lettered(ax, (9.2, 7.3), N, unit=U)
broken_end(a["x1"], 7.8)
broken_end(b["x1"], 7.3)

# 3: fusion of the sister chromatids at their broken ends
step(6.1, "3  Sister chromatids fuse at the broken ends: dicentric")
dic = N + N[::-1]
d = C.lettered(ax, (9.2, 6.1), dic, unit=U)
fx = d["x0"] + (d["x1"] - d["x0"]) / 2
ax.plot([fx, fx], [5.75, 6.45], color=P.muted(), lw=1.0, ls=":", zorder=21)
bio.label(ax, (fx, 6.65), "fusion point", size="tiny", color=P.muted())

# 4: anaphase bridge
step(4.75, "4  Anaphase: centromeres pulled apart, bridge breaks")
cents = d["centromeres"]
bio.arrow(ax, (cents[0], 4.25), (cents[0] - 1.4, 4.25), kind="process", head=0.16)
bio.arrow(ax, (cents[1], 4.25), (cents[1] + 1.4, 4.25), kind="process", head=0.16)
d2 = C.lettered(ax, (9.2, 4.75), dic, unit=U)
# the break: between E and D of the right half
xs_e = d2["x"]["E"][1]
xs_d = d2["x"]["D"][1]
bx = (xs_e + xs_d) / 2
for s in (1, -1):
    ax.plot([bx - 0.12, bx + 0.12], [4.75 - s * 0.32, 4.75 + s * 0.32], color=BROKEN, lw=2.2, zorder=22)
bio.label(ax, (bx, 5.3), "random break", size="tiny", color=BROKEN)

# 5: daughters
step(2.9, "5  Daughter nuclei")
left = N + ["F", "E"]
right = ["D", "C", "o", "B", "A"]
l = C.lettered(ax, (9.2, 3.2), left, unit=U)
broken_end(l["x1"], 3.2)
bio.label(ax, (l["x1"] + 0.3, 3.2), "inverted duplication of F E", size="tiny", color=P.muted(), ha="left")
r = C.lettered(ax, (9.2, 2.45), right[::-1], unit=U)
broken_end(r["x1"], 2.45)
bio.label(ax, (r["x1"] + 0.3, 2.45), "deletion of E F", size="tiny", color=P.muted(), ha="left")

bio.label(ax, (0.3, 1.2), "Both daughters again end in a broken end: in the next division the cycle repeats, until the end is healed by a new telomere.",
          size="small", ha="left", color=P.muted())

ax.set_xlim(0, 20.0)
ax.set_ylim(0.6, 9.6)
