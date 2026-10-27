"""The three branches of the unfolded protein response (SBGN activity flow; open arrows activate, bars inhibit).

Unfolded proteins in the ER lumen titrate BiP away from the luminal domains of the sensors and bind IRE1
directly. IRE1 oligomerizes, autophosphorylates and its RNase splices XBP1 mRNA (26-nt intron; RtcB ligates);
XBP1s is a transcription factor; IRE1 also degrades ER-bound mRNAs (RIDD). PERK phosphorylates eIF2alpha,
which lowers global translation (less load) while ATF4 is translated; ATF4 induces CHOP and GADD34, which
dephosphorylates eIF2alpha (negative feedback). ATF6 travels to the Golgi, where S1P and S2P release ATF6(N).
In the nucleus the three transcription factors induce chaperones (BiP), ERAD components, lipid synthesis and
ER expansion (adaptation); prolonged signalling through CHOP and other routes leads to apoptosis.
"""

from matplotlib.patches import FancyBboxPatch

import wikibio as bio
from wikibio import network
from wikibio import photosynthesis as ps

P = bio.P
fig, ax = bio.canvas(26.0, 14.0, scale=0.42)
for (x0, y0, x1, y1), tok, txt in (((0.3, 10.2, 17.8, 13.7), "er", "ER lumen"),
                                   ((0.3, 0.3, 17.8, 9.8), "cytoplasm", "Cytosol"),
                                   ((18.2, 10.2, 25.7, 13.7), "golgi", "Golgi"),
                                   ((18.2, 0.3, 25.7, 9.8), "nucleus", "Nucleus")):
    ax.add_patch(FancyBboxPatch((x0, y0), x1 - x0, y1 - y0, boxstyle="round,pad=0,rounding_size=0.5",
                                facecolor=ps.tint(tok, 0.55, 0.82), edgecolor=P.edge(tok), lw=1.4, zorder=1))
    bio.label(ax, (x0 + 0.3, y1 - 0.35), txt, size="small", bold=True, ha="left", color=P.edge(tok))

d = network.Diagram(ax, size="small")
d.activity("unf", (3.2, 12.0), "unfolded\nproteins", token="negative", w=3.0, h=1.3)
d.activity("bip", (8.5, 12.4), "BiP", token="enzyme", w=1.8)
d.connect("unf", "bip", "negative", text="titrate", text_offset=(0.0, 0.25))
d.activity("ire1", (3.2, 8.4), "IRE1\n(kinase, RNase)", token="receptor", w=3.0, h=1.3)
d.activity("perk", (9.0, 8.4), "PERK", token="receptor", w=2.4)
d.activity("atf6", (15.0, 8.4), "ATF6 (p90)", token="receptor", w=2.8)
d.connect("unf", "ire1", "positive")
for s in ("ire1", "perk", "atf6"):
    d.connect("bip", s, "negative")

d.activity("xbp1", (3.2, 5.6), "XBP1 mRNA splicing", token="rna", w=3.6)
d.connect("ire1", "xbp1", "positive")
d.activity("ridd", (3.2, 3.4), "RIDD (mRNA decay)", token="rna", w=3.6)
d.connect("ire1", "ridd", "positive", via=[(1.2, 7.0), (1.2, 3.4)], start=(1.7, 8.0), end=(1.4, 3.4))
d.activity("eif", (9.0, 6.1), "eIF2α-P", token="protein", w=2.4)
d.connect("perk", "eif", "positive")
d.activity("trans", (7.3, 3.6), "global\ntranslation", token="neutral", w=2.4, h=1.2)
d.activity("atf4", (11.4, 3.6), "ATF4\ntranslation", token="protein", w=2.4, h=1.2)
d.connect("eif", "trans", "negative")
d.connect("eif", "atf4", "positive")
d.connect("trans", "unf", "positive", via=[(7.3, 10.6), (5.0, 10.6)], start=(7.3, 4.2), end=(4.5, 11.35), dashed=True,
          text="load", text_at=0.55, text_offset=(0.3, 0.0))
d.activity("s12p", (21.0, 11.9), "S1P, S2P cleavage", token="enzyme", w=3.6)
d.connect("atf6", "s12p", "positive", via=[(17.2, 8.4), (17.2, 11.9)], end=(19.2, 11.9),
          text="COPII", text_at=0.45, text_offset=(0.45, 0.0))
d.activity("xbp1s", (20.0, 7.9), "XBP1s", token="dna", w=2.2)
d.activity("atf6n", (24.0, 7.9), "ATF6(N)", token="dna", w=2.2)
d.activity("atf4n", (21.8, 6.1), "ATF4", token="dna", w=2.0)
d.activity("chop", (21.8, 4.6), "CHOP", token="dna", w=2.0)
d.connect("xbp1", "xbp1s", "positive", via=[(6.0, 5.6), (6.0, 4.8), (17.6, 4.8), (17.6, 7.9)], start=(5.0, 5.6),
          end=(18.9, 7.9))
d.connect("s12p", "atf6n", "positive", end=(24.0, 8.4))
d.connect("atf4", "atf4n", "positive", end=(20.8, 6.1))
d.connect("atf4n", "chop", "positive")
d.activity("gadd", (14.6, 1.6), "GADD34–PP1", token="enzyme", w=3.0)
d.connect("chop", "gadd", "positive", via=[(18.6, 4.6), (18.6, 1.6)], start=(20.8, 4.6), end=(16.1, 1.6))
d.connect("gadd", "eif", "negative", via=[(12.2, 1.6), (12.2, 6.1)], end=(10.2, 6.1))
d.phenotype("adapt", (21.0, 3.2), "adaptation: chaperones,\nERAD, lipids, ER growth", token="positive", w=6.6, h=1.2)
d.phenotype("death", (23.4, 1.25), "apoptosis", token="negative", w=3.0, h=0.9)
d.connect("xbp1s", "adapt", "positive", start=(19.6, 7.4), end=(19.6, 3.8))
d.connect("atf6n", "adapt", "positive", start=(23.6, 7.4), end=(23.3, 3.8))
d.connect("chop", "death", "positive", via=[(25.1, 4.6), (25.1, 1.25)], start=(22.8, 4.6), end=(24.9, 1.25), dashed=True)
