# Crick's central dogma (1958, restated 1970) as a diagram of possible transfers of sequence information.
# Solid arrows: general transfers, found in all cells (replication DNA -> DNA by DNA polymerase,
# transcription DNA -> RNA by RNA polymerase, translation RNA -> protein by the ribosome).
# Dashed arrows: special transfers, found in particular systems (reverse transcription RNA -> DNA by
# reverse transcriptase: retroviruses, retrotransposons, telomerase; RNA replication RNA -> RNA by an
# RNA-dependent RNA polymerase: RNA viruses). Direct DNA -> protein translation has been seen only in vitro.
# No transfer leaves protein: that is the actual content of the dogma. Beside each carrier, its role in the
# cell (archive, working copy, machine) in the analogy of a computer's disk, memory and processor.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(17, 10.4)
D, R, Pr = np.array([3.4, 7.2]), np.array([13.6, 7.2]), np.array([8.5, 2.4])
w, h = 2.6, 1.0
for c, tok, text in ((D, "dna", "DNA"), (R, "rna", "RNA"), (Pr, "protein", "Protein")):
    bio.box(ax, c, w, h, tok, text, radius=0.45, size="title")

ink, mut = P.ink(), P.muted()
# general transfers
bio.arrow(ax, D + (1.45, 0.1), R - (1.45, -0.1), kind="process", lw=2.0)
bio.label(ax, ((D + R) / 2) + (0, 0.7), "Transcription", size="normal", bold=True, va="bottom")
bio.label(ax, ((D + R) / 2) + (0, 0.3), "RNA polymerase", size="small", color=mut, va="bottom")
bio.arrow(ax, R + (-0.7, -0.6), Pr + (1.05, 0.6), kind="process", lw=2.0)
bio.label(ax, (12.2, 4.6), "Translation", size="normal", bold=True, ha="left")
bio.label(ax, (12.2, 4.15), "ribosome", size="small", color=mut, ha="left")
# replication: a loop over DNA
bio.arrow(ax, D + (-0.6, 0.55), D + (0.6, 0.55), kind="process", bend=0.9, lw=2.0)
bio.label(ax, D + (0, 2.15), "Replication", size="normal", bold=True, va="bottom")
bio.label(ax, D + (0, 1.8), "DNA polymerase", size="small", color=mut, va="bottom")

# special transfers
bio.arrow(ax, R - (1.45, 0.3), D + (1.45, -0.3), kind="process", dashed=True, color=mut, lw=1.3)
bio.label(ax, ((D + R) / 2) + (0, -0.75), "Reverse transcription (reverse transcriptase)", size="small", color=mut, va="top")
bio.arrow(ax, R + (-0.6, 0.55), R + (0.6, 0.55), kind="process", bend=0.9, dashed=True, color=mut, lw=1.3)
bio.label(ax, R + (0, 1.8), "RNA replication (RNA viruses)", size="small", color=mut, va="bottom")
bio.arrow(ax, D + (0.7, -0.6), Pr + (-1.05, 0.6), kind="process", dashed=True, color=mut, lw=1.0)
bio.label(ax, (4.8, 4.6), "DNA → protein", size="small", color=mut, ha="right")
bio.label(ax, (4.8, 4.15), "(in vitro only)", size="small", color=mut, ha="right")

# nothing leaves protein
bio.label(ax, Pr + (0, -1.0), "No transfer of sequence information out of protein", size="small", va="top")

# roles
for c, text in ((D, "archive: stable,\n1–2 copies per cell"), (R, "working copy: short-lived,\nmany copies, also catalytic"),
                (Pr, None)):
    if text:
        bio.label(ax, c + (0, -1.25 if c is R else -1.25), text, size="tiny", color=mut, va="top")
bio.label(ax, Pr + (2.2, 0.0), "machine: catalysis,\nstructure, regulation", size="tiny", color=mut, ha="left")
