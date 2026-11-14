"""Maternal licking and grooming, GR promoter methylation and the HPA axis in rats (schematic loop)."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 13.0)
nodes = {
    "lg": ((4.2, 10.6), "high licking and\ngrooming by mother", "positive"),
    "ht": ((12.6, 10.6), "5-HT signaling and\nNGFI-A in hippocampus", "neuron"),
    "me": ((21.4, 10.6), "GR promoter\ndemethylated", "dna"),
    "gr": ((21.4, 6.2), "more hippocampal\nGR", "receptor"),
    "hpa": ((12.6, 6.2), "stronger negative feedback\non HPA axis", "protein"),
    "ad": ((4.2, 6.2), "adult: low stress\nreactivity", "positive"),
}
for k, (xy, txt, tok) in nodes.items():
    bio.box(ax, xy, 6.6, 2.3, tok)
    bio.label(ax, xy, txt, size="small", color=P.on_fill())
bio.arrow(ax, (7.6, 10.6), (9.2, 10.6), kind="activation")
bio.arrow(ax, (16.0, 10.6), (18.0, 10.6), kind="activation")
bio.arrow(ax, (21.4, 9.4), (21.4, 7.4), kind="activation")
bio.arrow(ax, (18.0, 6.2), (16.0, 6.2), kind="activation")
bio.arrow(ax, (9.2, 6.2), (7.6, 6.2), kind="activation")
bio.arrow(ax, (3.0, 7.4), (3.0, 9.4), kind="process", dashed=True)
bio.label(ax, (1.0, 8.4), "daughters\nbecome high-\nlicking mothers", size="tiny", ha="left", color=P.muted())
bio.label(ax, (13.0, 3.6), "CRH (hypothalamus) → ACTH (pituitary) → corticosterone (adrenal)", size="small",
          color=P.muted())
bio.arrow(ax, (12.6, 5.0), (12.6, 4.1), kind="inhibition")
bio.label(ax, (13.0, 2.0), "cross-fostering: the phenotype follows the rearing mother, not the genetic mother;",
          size="tiny", color=P.muted())
bio.label(ax, (13.0, 1.2), "low-licking mothers: promoter stays methylated, less GR, more reactive adults",
          size="tiny", color=P.muted())
