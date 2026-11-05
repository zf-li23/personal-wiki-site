# Inflorescence types (schematic side views; flower size shows the order of opening: larger = older,
# ovoid buds = youngest). Top row: simple racemose (indeterminate) inflorescences. Bottom row: compound
# racemose inflorescences (left of the dashed line) and cymose (determinate) inflorescences, which end in
# a flower that opens first: monochasia (scorpioid: branches alternating; helicoid: always the same side),
# dichasium, pleiochasium and the verticillaster of the Lamiaceae.
import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(36.0, 14.4)
H = 4.4
COL = [2.4 + 4.45 * i for i in range(8)]
Y1, Y2 = 8.3, 1.1
row1 = [("raceme", "Raceme"), ("corymb", "Corymb"), ("umbel", "Umbel"), ("spike", "Spike"), ("catkin", "Catkin"),
        ("spadix", "Spadix"), ("capitulum", "Capitulum"), ("hypanthodium", "Hypanthodium")]
row2 = [("panicle", "Panicle"), ("compound spike", "Compound spike"), ("compound umbel", "Compound umbel"),
        ("scorpioid cyme", "Scorpioid cyme"), ("helicoid cyme", "Helicoid cyme"), ("dichasium", "Dichasium"),
        ("pleiochasium", "Pleiochasium"), ("verticillaster", "Verticillaster")]
bio.label(ax, (0.3, 14.2), "Racemose (indeterminate): simple", size="title", ha="left", va="top", bold=True)
A = {}
for x, (k, n) in zip(COL, row1):
    A[k] = B.inflorescence(ax, (x, Y1), H, kind=k)
    bio.label(ax, (x, Y1 - 0.45), n, size="normal")
for x, (k, n) in zip(COL, row2):
    A[k] = B.inflorescence(ax, (x, Y2), H, kind=k)
    bio.label(ax, (x, Y2 - 0.45), n, size="normal")
bio.label(ax, (0.3, 6.9), "Racemose: compound", size="title", ha="left", va="center", bold=True)
xd = (COL[2] + COL[3]) / 2 + 0.2
ax.plot([xd, xd], [0.2, 6.6], color=P.muted(), lw=0.8, ls=(0, (4, 3)))
bio.label(ax, (xd + 0.3, 6.9), "Cymose (determinate)", size="title", ha="left", va="center", bold=True)
r = A["raceme"]
bio.callout(ax, r["pedicel"], (COL[0] + 1.6, Y1 + 1.9), "Pedicel", size="tiny")
bio.callout(ax, r["bract"], (COL[0] - 1.6, Y1 + 2.1), "Bract", size="tiny")
bio.callout(ax, r["peduncle"], (COL[0] - 1.3, Y1 + 0.5), "Peduncle", size="tiny")
s = A["spadix"]
bio.callout(ax, s["spathe"], (COL[5] + 1.7, Y1 + 1.5), "Spathe", size="tiny")
c = A["capitulum"]
bio.callout(ax, c["phyllary"], (COL[6] + 1.7, Y1 + 1.4), "Involucre", size="tiny")
h = A["hypanthodium"]
bio.callout(ax, h["ostiole"], (COL[7] + 1.5, Y1 + 4.3), "Ostiole", size="tiny")
d = A["dichasium"]
bio.callout(ax, d["terminal"], (COL[5] + 1.4, Y2 + 4.7), "Terminal flower\n(opens first)", size="tiny")
