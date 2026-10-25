# Inflorescence types, drawn from rules in the style of a botany manual plate (wikibio.botany). Flower size
# shows the order of opening (larger = older; ovoid buds = youngest). Racemose (indeterminate)
# inflorescences keep growing at the apex and open from the base upwards or from the edge inwards: raceme
# (pedicellate flowers on an unbranched axis), spike (sessile flowers), catkin (a pendulous spike of small
# unisexual flowers among scale-like bracts), spadix (a fleshy spike enclosed by a spathe), corymb (lower
# pedicels longer, flowers in a flat top), umbel (pedicels from one point, with an involucre of bracts),
# compound umbel (rays bearing umbellets, each with an involucel), panicle (a branched raceme) and capitulum
# (a head of sessile florets on a receptacle within an involucre of phyllaries: ray florets around the
# edge, disc florets in the centre). Cymose (determinate) inflorescences end in a flower that opens first;
# growth continues from lateral branches below it: one branch per node in monochasial cymes (scorpioid:
# alternating sides, zigzag; helicoid: always the same side, coiled), two in a dichasium.
import wikibio as bio
from wikibio import botany as B

P = bio.P
fig, ax = bio.canvas(30.0, 14.6)
H = 4.4
COL = [3.0 + 4.75 * i for i in range(6)]
Y1, Y2 = 8.3, 1.0

bio.label(ax, (0.3, 14.35), "Racemose (indeterminate)", size="title", ha="left", va="top", bold=True)
row1 = ["raceme", "spike", "catkin", "spadix", "corymb", "umbel"]
A = {}
for x, k in zip(COL, row1):
    A[k] = B.inflorescence(ax, (x, Y1), H, kind=k)
    bio.label(ax, (x, Y1 - 0.4), k.capitalize(), size="normal")
row2 = ["compound umbel", "panicle", "capitulum", "scorpioid cyme", "helicoid cyme", "dichasium"]
for x, k in zip(COL, row2):
    A[k] = B.inflorescence(ax, (x, Y2), H, kind=k)
    bio.label(ax, (x, Y2 - 0.4), k.capitalize(), size="normal")
# divider between the racemose and cymose types in the lower row
xd = (COL[2] + COL[3]) / 2 + 0.2
ax.plot([xd, xd], [0.2, 6.6], color=P.muted(), lw=0.8, ls=(0, (4, 3)))
bio.label(ax, (xd + 0.3, 7.0), "Cymose (determinate)", size="title", ha="left", va="center", bold=True)

r = A["raceme"]
bio.callout(ax, r["pedicel"], (COL[0] + 1.6, Y1 + 1.9), "Pedicel", size="tiny")
bio.callout(ax, r["bract"], (COL[0] - 1.7, Y1 + 2.1), "Bract", size="tiny")
bio.callout(ax, r["peduncle"], (COL[0] - 1.3, Y1 + 0.5), "Peduncle", size="tiny")
bio.callout(ax, r["rachis"], (COL[0] - 1.5, Y1 + 3.4), "Rachis", size="tiny")
s = A["spadix"]
bio.callout(ax, s["spathe"], (COL[3] + 1.7, Y1 + 1.5), "Spathe", size="tiny")
bio.callout(ax, s["spadix"], (COL[3] + 1.7, Y1 + 3.4), "Spadix", size="tiny")
u = A["umbel"]
bio.callout(ax, u["involucre"], (COL[5] + 1.6, Y1 + 1.2), "Involucre", size="tiny")
cu = A["compound umbel"]
bio.callout(ax, cu["ray"], (COL[0] + 1.9, Y2 + 1.3), "Ray", size="tiny")
bio.callout(ax, cu["umbellet"], (COL[0] + 1.9, Y2 + 4.9), "Umbellet", size="tiny")
bio.callout(ax, cu["involucel"], (COL[0] + 2.1, Y2 + 2.4), "Involucel", size="tiny")
c = A["capitulum"]
bio.callout(ax, c["ray_floret"], (COL[2] + 1.9, Y2 + 4.6), "Ray floret", size="tiny")
bio.callout(ax, c["disc_floret"], (COL[2] - 1.5, Y2 + 4.6), "Disc florets", size="tiny")
bio.callout(ax, c["phyllary"], (COL[2] + 1.7, Y2 + 1.7), "Phyllaries", size="tiny")
d = A["dichasium"]
bio.callout(ax, d["terminal"], (COL[5] + 1.4, Y2 + 4.7), "Terminal flower\n(opens first)", size="tiny")
sc = A["scorpioid cyme"]
bio.callout(ax, sc["terminal"], (COL[3] - 1.3, Y2 + 2.3), "First flower", size="tiny")
