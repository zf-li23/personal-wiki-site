"""Genetic compensation: why a mutant can look normal when a knockdown does not.

Top: a mutant allele with a premature termination codon (PTC) is transcribed; its mRNA is degraded by
nonsense-mediated decay (NMD). In zebrafish, the NMD factor Upf3a and components of the COMPASS histone
H3K4 methyltransferase complex then raise H3K4 trimethylation at related genes and increase their
transcription (Ma and colleagues 2019; El-Brolosy and colleagues 2019 showed that degradation fragments
of the mutant mRNA are required and that genes with sequence similarity are favoured). The paralogue
replaces the lost function and the phenotype is mild. Middle: a translation-blocking morpholino removes the
protein but leaves the mRNA intact: no decay, no compensation, a strong phenotype. Bottom: an allele that
makes no mRNA (promoter deleted) also fails to trigger compensation.
"""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(25.6, 9.4)


def row(y, title, steps, outcome, good):
    bio.label(ax, (0.3, y + 0.85), title, size="small", bold=True, ha="left")
    x = 1.6
    prev = None
    for text, tok, w in steps:
        cx = x + w / 2
        bio.box(ax, (cx, y), w, 1.0, tok, text=text, size="tiny")
        if prev is not None:
            bio.arrow(ax, (prev + 0.08, y), (x - 0.08, y), kind="process", head=0.18)
        prev = x + w
        x += w + 0.75
    bio.arrow(ax, (prev + 0.08, y), (x - 0.08, y), kind="process", head=0.18)
    bio.box(ax, (x + 1.95, y), 3.9, 1.0, "positive" if good else "negative", text=outcome, size="tiny")


row(7.6, "Mutant allele with a premature stop codon",
    [("DNA: PTC\nin gene A", "dna", 2.3), ("mutant mRNA", "mrna", 2.2), ("NMD (Upf1,\nUpf3a): decay", "enzyme", 2.6),
     ("Upf3a + COMPASS:\nH3K4me3 at paralogues", "protein", 3.6), ("paralogue A'\ntranscribed more", "dna2", 3.0)],
    "A' compensates:\nmild phenotype", True)
row(4.6, "Morpholino knockdown of gene A",
    [("DNA: gene A\nnormal", "dna", 2.3), ("normal mRNA", "mrna", 2.2), ("morpholino\nblocks translation", "drug", 3.0)],
    "no protein A, no compensation:\nstrong phenotype", False)
row(1.6, "Allele that makes no mRNA",
    [("DNA: promoter\ndeleted", "dna", 2.3), ("no mRNA", "neutral", 2.2), ("nothing to\ndegrade", "neutral", 2.2)],
    "no compensation:\nstrong phenotype", False)

bio.label(ax, (17.4, 4.85), r"Zebrafish $\it{capn3a}$: knockdown gives a small liver;", size="tiny", ha="left",
          color=P.muted())
bio.label(ax, (17.4, 4.35), "PTC mutants: normal liver, related genes up", size="tiny", ha="left",
          color=P.muted())
