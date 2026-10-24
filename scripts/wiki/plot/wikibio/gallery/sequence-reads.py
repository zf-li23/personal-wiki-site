# A: short reads aligned to a reference: a heterozygous SNV (C>T in about half the reads), a 2-bp deletion
# carried by some reads, and scattered sequencing errors. B: a self dot plot of a DNA sequence with a
# direct repeat (parallel diagonal) and an inverted repeat (anti-diagonal, reverse-complement matches).
# C: cytochrome c, human against yeast (window 3, at most one mismatch). Synthetic data, numpy seed.
import numpy as np

import wikibio as bio
from wikibio import sequence

P = bio.P
rng = np.random.default_rng(11)
fig, ax = bio.canvas(20, 13.0)

# --- A: pileup
ref = "".join(rng.choice(list("ACGT"), 64))
ref = ref[:30] + "C" + ref[31:]
snv, dele = 30, 46
reads, used, carriers = [], {snv, dele, dele + 1}, 0
for k in range(26):
    s = int(rng.integers(-10, 52))
    s = max(s, 0)
    seq = list(ref[s:s + 22])
    if s <= snv < s + len(seq) and rng.random() < 0.5:
        seq[snv - s] = "T"
    if s <= dele and dele + 2 < s + len(seq):
        carriers += 1
        if carriers % 2:  # every other read across the site carries the deletion
            seq[dele - s] = seq[dele - s + 1] = "-"
    if rng.random() < 0.3:  # one sequencing error
        j = int(rng.integers(0, len(seq)))
        if s + j not in used:  # errors are isolated: never two in one column
            used.add(s + j)
            seq[j] = str(rng.choice([b for b in "ACGT" if b != seq[j]]))
    reads.append((s, "".join(seq), "+" if rng.random() < 0.5 else "-"))
bio.panel(ax, "A", (0.1, 12.9))
g = sequence.pileup(ax, ref, reads, at=(2.6, 11.6), cell=0.27, row=0.27, ref_start=10_481)
yb = g["bottom"]
bio.callout(ax, (g["x"](snv), yb + 0.05), (g["x"](snv) - 0.8, yb - 0.55), "C>T, heterozygous")
bio.callout(ax, (g["x"](dele) + 0.135, yb + 0.05), (g["x"](dele) + 0.9, yb - 0.55), "2-bp deletion")

# --- B: self dot plot of a DNA sequence with a direct and an inverted repeat
unit = "GATTACAGCT"
spacer = "".join(rng.choice(list("ACGT"), 8))
pal = "CCTAGGTA"
dna = "".join(rng.choice(list("ACGT"), 4)) + unit + spacer + unit + "TGA" + pal + "ACT" + sequence.revcomp(pal) + "".join(rng.choice(list("ACGT"), 3))
bio.panel(ax, "B", (0.1, 6.0))
sequence.dotplot(ax, dna, dna, at=(1.3, 0.4), size=5.0, window=4, reverse=True, names=("sequence", "sequence"), ticks=10)
bio.label(ax, (6.6, 1.6), "forward match", size="tiny", ha="left", color=P.edge("dna"))
bio.label(ax, (6.6, 1.25), "reverse complement", size="tiny", ha="left", color=P.edge("rna"))

# --- C: two homologous proteins
human = "GDVEKGKKIFVQKCAQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLENPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE"
yeast = "TEFKAGSAKKGATLFKTRCLQCHTVEKGGPHKVGPNLHGIFGRHSGQAEGYSYTDANIKKNVLWDENNMSEYLTNPKKYIPGTKMAFGGLKKEKDRNDLITYLKKACE"
bio.panel(ax, "C", (10.6, 6.0))
sequence.dotplot(ax, human, yeast, at=(12.2, 0.4), size=5.0, window=3, mismatches=1, names=("human cytochrome c", "yeast iso-1"),
                 ticks=20, token="protein")
