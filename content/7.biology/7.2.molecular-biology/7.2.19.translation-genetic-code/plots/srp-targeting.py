# Cotranslational targeting to the endoplasmic reticulum (the SRP cycle).
# 1: a signal sequence (positive n-region, hydrophobic h-region of 7-15 residues, polar c-region ending in a
#    small residue before the cleavage site) emerges from the exit tunnel of a ribosome in the cytosol.
# 2: the signal recognition particle (SRP: 7SL RNA and six proteins; SRP54 binds the signal) binds the signal
#    and the ribosome and slows elongation.
# 3: SRP-GTP docks on the SRP receptor (SR-GTP) in the ER membrane; the ribosome is handed to the Sec61
#    translocon, and reciprocal GTP hydrolysis by SRP54 and SRalpha releases SRP.
# 4: translation resumes; the chain is threaded through the Sec61 channel, signal peptidase removes the signal
#    in the lumen, and oligosaccharyltransferase adds N-linked glycans to Asn-X-Ser/Thr.
import numpy as np
import wikibio as bio
from wikibio import molbio as MB

P = bio.P
fig, ax = bio.canvas(25.0, 9.0)
ym = 2.3
bio.bilayer(ax, [(0.3, ym), (24.7, ym)])
bio.label(ax, (0.5, 0.6), "ER lumen", size="small", ha="left", bold=True)
bio.label(ax, (0.5, 3.2), "Cytosol", size="small", ha="left", bold=True)


from matplotlib.transforms import Affine2D


def rib(cx, cy, w=3.0):
    """A ribosome with the large subunit facing down (towards the membrane), mRNA on top."""
    n0 = len(ax.patches)
    MB.ribosome(ax, (cx, cy), width=w, height=1.9)
    flip = Affine2D().scale(1, -1).translate(0, 2 * cy) + ax.transData
    for patch in ax.patches[n0:]:
        patch.set_transform(flip)
    ax.plot([cx - 2.2, cx + 2.2], [cy, cy], color=P.edge("mrna"), lw=1.6, zorder=10)
    bio.label(ax, (cx - 2.45, cy), "5′", size="tiny", bold=True)
    bio.label(ax, (cx + 2.45, cy), "3′", size="tiny", bold=True)


def chain(pts, n_signal=3, tok="highlight"):
    p = np.asarray(pts, float)
    ax.plot(p[:, 0], p[:, 1], color=P.edge("protein"), lw=2.0, zorder=14, solid_capstyle="round")
    if n_signal:
        q = p[-n_signal:]
        ax.plot(q[:, 0], q[:, 1], color=P.edge(tok), lw=4.0, zorder=15, solid_capstyle="round")


# 1
rib(3.0, 7.2)
chain([(3.0, 6.9), (3.0, 5.0), (2.6, 4.6), (2.0, 4.5), (1.6, 4.3)])
bio.label(ax, (3.0, 8.65), "1  signal sequence emerges", size="tiny", bold=True)
bio.label(ax, (1.3, 3.85), "n · h · c", size="tiny", color=P.edge("highlight"))

# 2
rib(8.8, 7.2)
chain([(8.8, 6.9), (8.8, 5.0), (8.4, 4.6), (7.9, 4.5)])
bio.protein(ax, (7.6, 4.6), 1.2, 0.8, "enzyme", text="SRP54")
ax.plot([8.2, 9.9, 10.8], [4.3, 4.0, 4.9], color=P.edge("rna"), lw=2.0, zorder=13)
bio.label(ax, (11.0, 4.5), "7SL RNA", size="tiny", color=P.edge("rna"), ha="left")
bio.label(ax, (8.8, 8.65), "2  SRP binds, elongation slows", size="tiny", bold=True)

# 3
rib(14.6, 5.0)
chain([(14.6, 4.7), (14.6, 3.25), (14.2, 3.0), (13.7, 3.0)])
bio.protein(ax, (13.4, 3.2), 1.1, 0.7, "enzyme", text="SRP")
bio.protein(ax, (12.2, ym + 0.95), 1.1, 0.7, "receptor", text="SR")
bio.label(ax, (11.2, ym + 1.25), "GTP", size="tiny", color=P.muted())
bio.box(ax, (14.6, ym), 1.0, 1.1, token="channel", text="Sec61", size="tiny", radius=0.12, zorder=12)
bio.label(ax, (14.6, 8.65), "3  docking; GTP hydrolysis releases SRP", size="tiny", bold=True)

# 4
rib(20.6, 5.0)
bio.box(ax, (20.6, ym), 1.0, 1.1, token="channel", text="", size="tiny", radius=0.12, zorder=12)
chain([(20.6, 4.7), (20.6, 1.4), (21.0, 0.9), (21.7, 0.8), (22.6, 1.0)], n_signal=0)
ax.plot([19.6, 20.1], [1.4, 1.0], color=P.edge("highlight"), lw=4.0, zorder=15, solid_capstyle="round")
bio.label(ax, (19.2, 0.65), "cleaved signal", size="tiny", color=P.edge("highlight"))
bio.protein(ax, (22.0, 1.6), 0.9, 0.55, "lysosome", text="SPase")
ax.add_patch(bio.core.Circle((22.6, 1.0), 0.16, facecolor=P.fill("carbohydrate"), edgecolor=P.edge("carbohydrate"), zorder=16))
bio.label(ax, (23.4, 0.6), "N-glycan", size="tiny")
bio.label(ax, (20.6, 8.65), "4  cotranslational translocation", size="tiny", bold=True)

for a, b in (((5.4, 6.0), (6.4, 6.0)), ((11.2, 6.0), (12.2, 5.6)), ((17.0, 5.6), (18.2, 5.6))):
    bio.arrow(ax, a, b, kind="process")
