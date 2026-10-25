# A: the twin-supercoiled-domain model (Liu & Wang 1987). A transcribing RNA polymerase that cannot rotate
#    around the DNA (it drags a nascent RNA and ribosomes, or is anchored) overwinds the template ahead of
#    it (positive supercoils, removed by gyrase in bacteria) and underwinds it behind (negative supercoils,
#    removed by topoisomerase I). The helix pitch is drawn tighter ahead and looser behind.
# B: supercoiling ahead of a replication fork. A domain of L0 = 50 kb between the fork and a topological
#    barrier starts at sigma0 = -0.06. The fork unwinds v = 1000 bp/s; its linking number Lk is conserved
#    except for removal by topoisomerases at r turns per second, while the duplex that remains shrinks:
#    sigma(t) = (Lk(0) - r t) / ((L0 - v t) / h) - 1, Lk(0) = (1 + sigma0) L0 / h, h = 10.5 bp per turn.
#    r = v / h = 95 turns/s is the rate at which the fork itself removes helical turns.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
fig, ax = bio.canvas(20, 10.6)

# --- A: twin-domain schematic -------------------------------------------------------------------
y = 8.3
bio.dna(ax, (0.8, y), (8.4, y), turns=3.2, ends=False)
bio.dna(ax, (11.6, y), (19.2, y), turns=8.0, ends=False)
bio.dna(ax, (8.4, y), (11.6, y), turns=2.4, ends=False)
bio.protein(ax, (10.0, y), 2.2, 1.5, "enzyme", text="RNAP")
bio.strand(ax, (9.4, y + 0.75), (7.2, y + 1.85), token="mrna", ends=False)
bio.label(ax, (6.9, y + 2.0), "RNA", size="tiny", color=P.edge("mrna"))
bio.arrow(ax, (11.4, y - 1.05), (13.6, y - 1.05), kind="process")
bio.label(ax, (12.5, y - 1.4), "direction of transcription", size="tiny", va="top")
bio.label(ax, (4.6, y + 0.85), "Behind: underwound, (−) supercoils", size="small")
bio.label(ax, (15.4, y + 0.85), "Ahead: overwound, (+) supercoils", size="small")
bio.label(ax, (4.6, y - 0.85), "relaxed by topoisomerase I", size="tiny", color=P.muted())
bio.label(ax, (15.4, y - 0.85), "relaxed by gyrase (bacteria), topo I/II (eukaryotes)", size="tiny", color=P.muted())
bio.panel(ax, "A", (0.1, 10.3))

# --- B: sigma ahead of a replication fork -------------------------------------------------------
b = C.axes_at(ax, (2.0, 1.2, 15.0, 4.6))
h, L0, v, s0 = 10.5, 50000.0, 1000.0, -0.06
t = np.linspace(0, 30, 600)
lk_init = (1 + s0) * L0 / h
for r, tok, text in ((0, "negative", "no topoisomerase (r = 0)"),
                     (48, "highlight", "r = 48 turns/s"),
                     (95.2, "dna", "r = v/h = 95 turns/s")):
    sig = (lk_init - r * t) / ((L0 - v * t) / h) - 1
    b.plot(t, sig, color=C.line(tok), lw=1.6, label=text)
b.axhline(0, color=P.muted(), lw=0.7)
b.axhline(s0, color=P.muted(), lw=0.7, ls=(0, (3, 2)))
b.text(29.6, s0 + 0.008, "initial σ = −0.06", fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="right", va="bottom")
b.set_xlim(0, 30)
b.set_ylim(-0.16, 0.3)
b.set_xticks([0, 5, 10, 15, 20, 25, 30])
b.set_yticks([-0.1, 0, 0.1, 0.2, 0.3], ["−0.1", "0", "0.1", "0.2", "0.3"])
C.style_axes(b, "Time after the fork enters the domain t / s", "σ of the unreplicated duplex")
leg = b.legend(loc="upper left", frameon=False, fontsize=bio.core.FONT["tiny"])
for tx in leg.get_texts():
    tx.set_color(P.ink())
bio.panel(ax, "B", (0.1, 6.5))
