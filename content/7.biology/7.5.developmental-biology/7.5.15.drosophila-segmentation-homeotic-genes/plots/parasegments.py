# Parasegments and segments in the Drosophila germ band (schematic, about four cell rows per parasegment, anterior
# left). Rows: even-skipped is expressed in the odd-numbered parasegments and fushi tarazu in the even-numbered ones;
# engrailed and hedgehog are on in the anterior row of every parasegment and wingless in the posterior row, so each
# parasegment boundary lies between a wingless row and an engrailed row. Segments are offset by about half a
# parasegment: each segment consists of the posterior compartment of one parasegment (en-expressing) and the anterior
# compartment of the next; the segment boundary lies just posterior to the engrailed row.
import wikibio as bio
from wikibio import development as D

fig, ax = bio.canvas(22.0, 9.0)
P = bio.P
n_ps, w = 4, 4
cells = n_ps * w
x0, x1 = 2.8, 21.4
cw = (x1 - x0) / cells
rows = {"eve": 6.7, "ftz": 5.9, "en": 5.1, "wg": 4.3}
tok = {"eve": "receptor", "ftz": "k", "en": "channel", "wg": "positive", "off": "neutral"}
for g, y in rows.items():
    fates = []
    for i in range(cells):
        ps, j = divmod(i, w)
        if g == "eve":
            on = ps % 2 == 0 and j < 3
        elif g == "ftz":
            on = ps % 2 == 1 and j < 3
        elif g == "en":
            on = j == 0
        else:
            on = j == w - 1
        fates.append(1 if on else 0)
    D.cell_row(ax, x0, x1, y, fates, [tok["off"], tok[g]], h=0.62, nuclei=False)
    bio.label(ax, (x0 - 0.3, y), g if g != "en" else "en, hh", size="small", italic=True, ha="right")
# parasegment brackets above
from wikibio import quant as Q
for ps in range(n_ps):
    a, b = x0 + ps * w * cw, x0 + (ps + 1) * w * cw
    Q.bracket(ax, (a + 0.05, 7.25), (b - 0.05, 7.25), side=1)
    bio.label(ax, ((a + b) / 2, 7.75), f"PS {ps + 3}", size="small")
    ax.plot([a, a], [3.5, 7.1], color=P.edge("receptor"), lw=1.1, ls=(0, (3, 2)), zorder=20)
# segments below: segment boundary posterior to the en row
segs = ["T2", "T3", "A1"]
for k in range(n_ps - 1):
    a = x0 + (k * w + 1) * cw
    b = a + w * cw
    Q.bracket(ax, (a + 0.05, 3.3), (b - 0.05, 3.3), side=-1)
    bio.label(ax, ((a + b) / 2, 2.65), segs[k], size="small")
    ax.plot([a, a], [3.45, 7.1], color=P.ink(), lw=1.1, zorder=20)
    # compartments (A anterior, P posterior; labels in the gap below the cells)
    bio.label(ax, (a + 1.5 * cw, 3.75), "A", size="tiny", color=P.muted())
    bio.label(ax, (a + 3.5 * cw, 3.75), "P", size="tiny", color=P.muted())
bio.label(ax, (x0 - 0.3, 7.75), "parasegments", size="small", color=P.muted(), ha="right")
bio.label(ax, (x0 - 0.3, 2.65), "segments", size="small", color=P.muted(), ha="right")
ax.plot([3.2, 4.0], [1.0, 1.0], color=P.edge("receptor"), lw=1.1, ls=(0, (3, 2)))
bio.label(ax, (4.2, 1.0), "parasegment boundary (between wg and en)", size="tiny", ha="left")
ax.plot([12.0, 12.8], [1.0, 1.0], color=P.ink(), lw=1.1)
bio.label(ax, (13.0, 1.0), "segment boundary (posterior to en)", size="tiny", ha="left")
bio.label(ax, (11.9, 8.6), "anterior → posterior", size="small", color=P.muted())
