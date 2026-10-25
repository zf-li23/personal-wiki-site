# A consensus sequence and its sequence logo: the P-loop (Walker A motif) of NTP-binding proteins, consensus
# G-x-x-x-x-G-K-[S/T], from twelve unrelated or distantly related proteins (human H-Ras, Rac1, Gai1, RAD51;
# E. coli EF-Tu, RecA, MalK; ATP synthase alpha and beta subunits; myosin II; kinesin-1; CFTR NBD1).
# The logo shows the information content of each column (bits, small-sample corrected); the invariant Gly,
# Lys and Ser/Thr wrap around and bind the phosphates of the bound nucleotide.
import numpy as np
import wikibio as bio
from wikibio import sequence as S

seqs = {
    "H-Ras": "GAGGVGKS", "Rac1": "GDGAVGKT", "Gαi1": "GAGESGKS", "EF-Tu": "GHVDHGKT",
    "RecA": "GPESSGKT", "RAD51": "GEFRTGKT", "F1 β": "GGAGVGKT", "F1 α": "GDRQTGKT",
    "myosin II": "GESGAGKT", "kinesin-1": "GQTSSGKT", "MalK": "GPSGCGKS", "CFTR NBD1": "GSTGAGKT",
}
AA = "ACDEFGHIKLMNPQRSTVWY"
L = 8
counts = np.zeros((L, len(AA)))
for s in seqs.values():
    for i, ch in enumerate(s):
        counts[i, AA.index(ch)] += 1

fig, ax = bio.canvas(16, 7.6)
S.alignment(ax, seqs, at=(2.4, 7.0), cell=(0.42, 0.42), ruler=False, conservation=False, consensus=True)
bio.label(ax, (11.6, 7.0), "Sequence logo", size="normal", bold=True)
S.logo(ax, counts, at=(9.4, 2.2), col_width=0.55, height=4.0, alphabet=AA, kind="counts")
bio.label(ax, (11.6, 1.4), "consensus  G-x-x-x-x-G-K-[S/T]", size="small")
