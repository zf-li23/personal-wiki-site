"""A simplified history of modern and archaic humans (Section 33.3.2), after Futuyma and Kirkpatrick
(2017), Fig. 21.14, with approximate times (kyr ago). The lineage of modern humans separated from that of
Neanderthals and Denisovans in Africa several hundred thousand years ago; the archaic lineage spread into
Eurasia and split into Neanderthals (west) and Denisovans (east). Modern humans left Africa about 60 kyr
ago. Arrows: gene flow from Neanderthals into the ancestors of all non-Africans (with further pulses
into East Asians), and from Denisovans into the ancestors of Melanesians and other Oceanians (and, at
lower levels, East Asians). The timing and number of pulses are simplified."""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
ink, muted = P.ink(), P.muted()
fig, ax = plt.subplots(figsize=(9.4, 4.6))
fig.subplots_adjust(left=0.08, right=0.97, bottom=0.12, top=0.97)
X = {"Africans": 0.0, "Europeans": 1.0, "East Asians": 2.0, "Melanesians": 3.0, "Neanderthals": 4.3, "Denisovans": 5.3}
mod, arc = "dna", "rna"


def seg(x0, y0, x1, y1, tok, lw=3.0):
    ax.plot([x0, x1], [y0, y1], color=P.fill(tok), lw=lw + 2.5, solid_capstyle="round")
    ax.plot([x0, x1], [y0, y1], color=P.edge(tok), lw=1.0)


seg(1.0, 650, 0.0, 0, mod)            # modern stem to Africans
seg(1.0, 650, 4.8, 400, arc)          # archaic stem
seg(4.8, 400, 4.3, 40, arc)           # Neanderthal (ends ~40 kya)
seg(4.8, 400, 5.3, 50, arc)           # Denisovan
seg(0.09, 60, 1.9, 45, mod)           # out of Africa stem
seg(1.9, 45, 3.0, 0, mod)             # Melanesians
seg(1.9, 45, 1.5, 30, mod)
seg(1.5, 30, 1.0, 0, mod)             # Europeans
seg(1.5, 30, 2.0, 0, mod)             # East Asians
ax.plot([1.0], [650], "o", color=ink, ms=4)
for name, x in X.items():
    yy = 40 if name == "Neanderthals" else (50 if name == "Denisovans" else 0)
    ax.text(x, yy - 25, name, ha="center", va="top", fontsize=FT["small"], color=ink)
ax.text(5.3, -10, "(extinct)", ha="center", va="top", fontsize=FT["tiny"], color=muted)
ax.text(4.3, 0, "(extinct)", ha="center", va="top", fontsize=FT["tiny"], color=muted)


def flow(x0, y0, x1, y1, txt, dy=0):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="-|>", color=charts.line("negative"), lw=1.4, connectionstyle="arc3,rad=0.2"))
    ax.text((x0 + x1) / 2, (y0 + y1) / 2 + dy, txt, ha="center", fontsize=FT["tiny"], color=charts.line("negative"))


flow(4.32, 75, 1.2, 55, "~2 % in all non-Africans", 30)
flow(5.25, 60, 2.8, 12, "", 0)
ax.text(4.2, 120, "Denisovan ancestry\nin Oceanians", ha="center", fontsize=FT["tiny"], color=charts.line("negative"))
ax.text(1.05, 660, "~550–750", fontsize=FT["tiny"], color=muted)
ax.text(4.85, 410, "~400–450", fontsize=FT["tiny"], color=muted)
ax.text(0.15, 75, "out of Africa ~60", fontsize=FT["tiny"], color=muted)
ax.set_ylim(-80, 720)
ax.set_xlim(-0.6, 6.0)
ax.set_xticks([])
charts.style_axes(ax, None, "thousand years ago")
ax.spines["bottom"].set_visible(False)
