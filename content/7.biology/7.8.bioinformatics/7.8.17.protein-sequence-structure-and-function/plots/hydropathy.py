# Predicting transmembrane helices from the sequence: bacteriorhodopsin of Halobacterium salinarum
# (UniProt P02945, 262 residues). The Kyte-Doolittle hydropathy of each residue is averaged over a sliding
# window of 19 residues, the length of a helix that crosses a lipid bilayer. A: the averaged hydropathy
# (one value per window, plotted at the central residue); the bands are the seven transmembrane helices
# annotated in UniProt and the dashed line is the classical threshold of 1.6. B: the maximum of the
# averaged hydropathy inside each annotated helix; two helices (C and F), which line the proton pathway
# and carry polar residues, stay below the threshold, which is why hydropathy plots are only a first pass.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT
SEQ = ("MLELLPTAVEGVSQAQITGRPEWIWLALGTALMGLGTLYFLVKGMGVSDPDAKKFYAITTLVPAIAFTMYLSMLLGYGLTMVPFGGEQNPIYWARYADWL"
       "FTTPLLLLDLALLVDADQGTILALVGADGIMIGTGLVGALTKVYSYRFVWWAISTAAMLYILYVLFFGFTSKAESMRPEVASTFKVLRNVTVVLWSAYPV"
       "VWLIGSEGAGIVPLNIETLLFMVLDVSAKVGFGLILLRSRAIFGEAEAPEPSAGDGAAATSD")
KD = dict(I=4.5, V=4.2, L=3.8, F=2.8, C=2.5, M=1.9, A=1.8, G=-0.4, T=-0.7, S=-0.8, W=-0.9, Y=-1.3, P=-1.6,
          H=-3.2, E=-3.5, Q=-3.5, D=-3.5, N=-3.5, K=-3.9, R=-4.5)
TM = [(23, 42, "A"), (57, 75, "B"), (93, 109, "C"), (121, 140, "D"), (148, 167, "E"), (186, 204, "F"),
      (217, 236, "G")]
w = 19
h = np.array([KD[a] for a in SEQ])
avg = np.convolve(h, np.ones(w) / w, mode="valid")
pos = np.arange(len(avg)) + w // 2 + 1
peak = [avg[(pos >= a) & (pos <= b)].max() for a, b, _ in TM]

fig, ax = bio.canvas(26.0, 9.0)
a = C.axes_at(ax, (2.0, 1.4, 15.5, 7.0))
for lo, hi, name in TM:
    a.axvspan(lo, hi, color=P.mix(P.light("membrane"), P.surface(), 0.55), lw=0)
    a.text((lo + hi) / 2, 3.1, name, ha="center", fontsize=FT["tiny"], color=C.line("membrane"))
a.plot(pos, avg, color=P.ink(), lw=1.1)
a.axhline(1.6, color=C.line("negative"), ls=(0, (4, 2)), lw=1.0)
a.axhline(0, color=P.muted(), lw=0.6)
a.text(252, 2.6, "threshold 1.6", fontsize=FT["tiny"], color=C.line("negative"), ha="right")
a.set_ylim(-3.2, 3.4)
C.style_axes(a, "residue (center of the 19-residue window)", "mean Kyte-Doolittle hydropathy")
bio.panel(ax, "A", (0.2, 8.6))
b = C.axes_at(ax, (20.0, 1.4, 5.4, 7.0))
xs = np.arange(len(TM))
b.bar(xs, peak, color=[C.line("membrane") if p >= 1.6 else C.line("negative") for p in peak], width=0.65)
b.axhline(1.6, color=C.line("negative"), ls=(0, (4, 2)), lw=1.0)
b.set_xticks(xs)
b.set_xticklabels([t[2] for t in TM], fontsize=FT["tiny"])
b.set_ylim(0, 2.4)
C.style_axes(b, "annotated helix", "maximum of the window average")
bio.panel(ax, "B", (18.8, 8.6))
