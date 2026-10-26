"""Hydropathy plots (Kyte and Doolittle, 1982) of two integral membrane proteins.

The hydropathy index of each residue (Kyte-Doolittle scale) is averaged over a sliding window of
19 residues and plotted at the central residue; a segment whose average exceeds about 1.6 is a
candidate transmembrane alpha helix. Shaded bands: transmembrane segments annotated in UniProt
from the known structures.
A: human glycophorin A (UniProt P02724, precursor numbering; residues 1-19 are the signal peptide):
one transmembrane helix.
B: bacteriorhodopsin of Halobacterium salinarum (UniProt P02945, precursor numbering): seven
transmembrane helices; the plot resolves helices F and G (residues 186-236) less clearly, because
helix G carries the retinal-binding Lys and other polar residues.
"""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P

KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5, "G": -0.4, "H": -3.2, "I": 4.5,
      "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2}

GYPA = ("MYGKIIFVLLLSEIVSISALSTTEVAMHTSTSSSVTKSYISSQTNDTHKRDTYAATPRAH"
        "EVSEISVRTVYPPEEETGERVQLAHHFSEPEITLIIFGVMAGVIGTILLISYGIRRLIKK"
        "SPSDVKPLPSPDTDVPLSSVEIENPETSDQ")
BR = ("MLELLPTAVEGVSQAQITGRPEWIWLALGTALMGLGTLYFLVKGMGVSDPDAKKFYAITT"
      "LVPAIAFTMYLSMLLGYGLTMVPFGGEQNPIYWARYADWLFTTPLLLLDLALLVDADQGT"
      "ILALVGADGIMIGTGLVGALTKVYSYRFVWWAISTAAMLYILYVLFFGFTSKAESMRPEV"
      "ASTFKVLRNVTVVLWSAYPVVWLIGSEGAGIVPLNIETLLFMVLDVSAKVGFGLILLRSR"
      "AIFGEAEAPEPSAGDGAAATSD")

TM_GYPA = [(92, 114)]
TM_BR = [(23, 42), (57, 75), (93, 109), (121, 140), (148, 167), (186, 204), (217, 236)]
W = 19


def profile(seq, w=W):
    h = np.array([KD[a] for a in seq])
    avg = np.convolve(h, np.ones(w) / w, mode="valid")
    centre = np.arange(len(avg)) + (w + 1) // 2  # 1-based residue number of the window centre
    return centre, avg


fig, ax = bio.canvas(21.0, 7.4)
panels = [("A", "Glycophorin A (human, P02724)", GYPA, TM_GYPA, 0.6, 6.4), ("B", "Bacteriorhodopsin (P02945)", BR, TM_BR, 9.1, 11.6)]
for letter, name, seq, tms, x0, wdt in panels:
    bio.panel(ax, letter, (x0 - 0.5, 7.3))
    pa = charts.axes_at(ax, (x0 + 0.9, 1.3, wdt - 0.3, 5.2))
    for k, (a, b) in enumerate(tms):
        pa.axvspan(a, b, color=P.fill("highlight"), alpha=0.45, lw=0)
        if letter == "B":
            pa.text((a + b) / 2, 3.55, "ABCDEFG"[k], ha="center", fontsize=bio.core.FONT["small"], color=P.ink(), weight="bold")
    x, y = profile(seq)
    pa.plot(x, y, color=charts.line("protein"), lw=1.5)
    pa.axhline(1.6, color=charts.line("negative"), lw=0.9, ls=(0, (4, 3)))
    pa.axhline(0, color=P.muted(), lw=0.6)
    pa.text(len(seq) * 0.03, -2.9, "dashed line: threshold 1.6", ha="left", fontsize=bio.core.FONT["tiny"], color=charts.line("negative"))
    pa.set_xlim(1, len(seq))
    pa.set_ylim(-3.2, 4.0)
    charts.style_axes(pa, "residue number", "mean hydropathy (19 residues)")
    charts.title(pa, name)
