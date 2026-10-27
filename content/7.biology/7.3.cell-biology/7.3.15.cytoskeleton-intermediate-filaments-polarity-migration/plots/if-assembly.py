"""Assembly of intermediate filaments (schematic, after the vimentin pathway).

1 Monomer: a central alpha-helical rod domain of about 310 residues (heptad repeats) between nonhelical
head (N) and tail (C) domains. 2 Two monomers wind into a parallel coiled-coil dimer (about 45 nm).
3 Two dimers associate antiparallel and staggered into a tetramer, which has the same ends on both sides:
the polarity is lost, so filaments are nonpolar. 4 Eight tetramers associate laterally into a unit-length
filament (ULF, about 60 nm long, 16 nm wide). 5 ULFs anneal end to end and compact radially into the
mature 10 nm filament, a rope with about 32 polypeptides in cross-section. No nucleotide is involved;
phosphorylation of the head domains disassembles the filaments (lamins at mitosis, vimentin in dividing cells).
"""

import wikibio as bio
from wikibio import cytoskel as C

P = bio.P
fig, ax = bio.canvas(25.0, 5.2)
xs = [0.6, 4.4, 8.4, 13.2, 17.6]
names = ["1  monomer", "2  coiled-coil dimer", "3  antiparallel tetramer", "4  unit-length filament", "5  10 nm filament"]
for k, (x, st, name) in enumerate(zip(xs, ("monomer", "dimer", "tetramer", "ulf", "filament"), names)):
    C.if_assembly(ax, (x, 2.6), st, length=2.6 if st != "filament" else 6.6)
    bio.label(ax, (x, 4.6), name, size="small", ha="left", bold=True)
    if k < 4:
        bio.arrow(ax, (xs[k + 1] - 0.8, 1.2), (xs[k + 1] - 0.25, 1.2), kind="process", head=0.16)
bio.label(ax, (0.6, 1.9), "N (head)", size="tiny", ha="left", color=P.muted())
bio.label(ax, (3.3, 1.9), "C (tail)", size="tiny", ha="right", color=P.muted())
bio.label(ax, (0.6, 3.35), "rod: α-helix, heptad repeats", size="tiny", ha="left", color=P.muted())
bio.label(ax, (8.4, 1.2), "same ends on both sides: nonpolar", size="tiny", ha="left", color=P.muted())
bio.label(ax, (13.2, 1.2), "8 tetramers side by side", size="tiny", ha="left", color=P.muted())
bio.label(ax, (17.6, 1.2), "ULFs anneal end to end, compact", size="tiny", ha="left", color=P.muted())
