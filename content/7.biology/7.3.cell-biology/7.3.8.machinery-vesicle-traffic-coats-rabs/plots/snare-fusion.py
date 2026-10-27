# SNARE-driven membrane fusion. A: a v-SNARE on the vesicle and the t-SNAREs syntaxin and SNAP-25 (two
# helices, palmitoylated linker) on the target membrane begin to zipper from their membrane-distal N-terminal
# ends (left) into a four-helix bundle; as zippering proceeds towards the transmembrane domains the two
# membranes are pulled together. B: an illustrative free-energy profile of one round of fusion (kBT; values
# are of the order measured for neuronal SNAREs with optical tweezers and estimated for lipid
# rearrangements): zippering of the trans complex releases about 65 kBT, which pays for the barriers of
# hemifusion and pore opening; after fusion the stable cis complex lies in one membrane, and NSF with alpha-SNAP
# uses ATP hydrolysis to pull it apart, resetting the SNAREs for another round.
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import PchipInterpolator

import wikibio as bio
from wikibio import quant
from wikibio import traffic as T

fig = plt.figure(figsize=(11.0, 4.0))
ax = fig.add_axes([0.0, 0.0, 0.5, 1.0])
ax.set_xlim(0, 12)
ax.set_ylim(0, 8.7)
ax.set_aspect("equal")
ax.axis("off")
bio.panel(ax, "A", (0.1, 8.6))
T.snare_complex(ax, 4.4, 7.0, 4.4, zipped=0.25, length=3.2, labels=True)
bio.label(ax, (2.6, 7.55), "vesicle", size="tiny", color=bio.P.muted())
bio.label(ax, (2.6, 3.85), "target membrane", size="tiny", color=bio.P.muted())
bio.label(ax, (2.6, 8.1), "trans-SNARE complex, N-terminal zippering", size="small")
T.snare_complex(ax, 10.6, 3.0, 1.9, zipped=0.95, length=3.2, labels=False)
bio.label(ax, (8.9, 3.65), "fully zippered: membranes in contact", size="small")
bio.arrow(ax, (5.6, 3.3), (6.6, 2.5), kind="process", bend=0.15)

b = fig.add_axes([0.58, 0.17, 0.39, 0.72])
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
G = np.array([0, -5, -40, -65, -30, -55, -45, -80, 0])
xs = np.linspace(0, 8, 400)
b.plot(xs, PchipInterpolator(x, G)(xs), color=quant.line_color("protein"), lw=1.9)
b.set_xticks(x, ["free", "docked", "half\nzipped", "trans\nzippered", "hemi-\nfusion\nbarrier", "hemi-\nfused",
                 "pore\nbarrier", "cis\ncomplex", "free again\n(NSF)"], fontsize=7)
b.set_ylabel("G / kBT")
b.set_title("B  Energy of one fusion cycle (illustrative)", fontsize=10)
b.text(7.55, -30, "paid by\nATP", fontsize=7, color=bio.P.muted(), ha="right")
b.spines[["top", "right"]].set_visible(False)
