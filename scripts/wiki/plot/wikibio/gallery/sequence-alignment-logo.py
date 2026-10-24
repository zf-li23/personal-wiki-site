# A: multiple alignment of the N-terminal region of mitochondrial cytochrome c (human numbering 1-40), with the
# CXXCH motif whose two cysteines attach the heme and whose histidine is an axial heme ligand.
# B, C: a TATA-box-like binding-site motif (illustrative counts from 60 sites) as an information-content
# logo and as a probability logo.
import numpy as np

import wikibio as bio
from wikibio import sequence

fig, ax = bio.canvas(17.6, 9.6)

bio.panel(ax, "A", (0.1, 9.5))
cytc = {
    "Human": "GDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKT",
    "Chicken": "GDIEKGKKIFVQKCSQCHTVEKGGKHKTGPNLHGLFGRKT",
    "Tuna": "GDVAKGKKTFVQKCAQCHTVENGGKHKVGPNLWGLFGRKT",
    "Wheat": "GNPDAGAKIFKTKCAQCHTVDAGAGHKQGPNLHGLFGRQS",
    "Yeast": "GSAKKGATLFKTRCLQCHTVEKGGPHKVGPNLHGIFGRHS",
}
sequence.alignment(ax, cytc, at=(3.0, 8.4), cell=(0.34, 0.42), highlight=[(13, 17, "CXXCH (heme)")])

# a TATA-box-like motif: counts of A, C, G, T at 12 positions
counts = np.array([
    [12, 18, 18, 12], [6, 22, 12, 20], [2, 4, 1, 53], [55, 1, 1, 3], [3, 2, 1, 54], [52, 1, 2, 5],
    [36, 1, 1, 22], [50, 2, 3, 5], [33, 2, 3, 22], [25, 6, 24, 5], [15, 16, 18, 11], [14, 17, 17, 12],
])
bio.panel(ax, "B", (0.1, 3.9))
sequence.logo(ax, counts, at=(1.5, 0.45), col_width=0.55, height=2.4, title="Information content")
bio.panel(ax, "C", (9.3, 3.9))
sequence.logo(ax, counts, at=(10.7, 0.45), col_width=0.55, height=2.4, ic=False, title="Probability")
