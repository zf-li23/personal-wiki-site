"""Approximate time ranges of some hominin species (Section 33.2), from the fossil record as currently
dated (bars; ages in Myr ago). Ranges are approximate and many species are known from few sites;
the bars do not imply ancestor-descendant relationships, which for most species are uncertain. Several
species coexisted at most times: the hominin phylogeny is a bush, and Homo sapiens is its only
surviving branch. Genus groups: Sahelanthropus, Orrorin and Ardipithecus (grey), Australopithecus
(orange), Paranthropus (brown), Homo (blue)."""
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
SP = [("Sahelanthropus tchadensis", 7.0, 6.0, "neutral"), ("Orrorin tugenensis", 6.1, 5.7, "neutral"),
      ("Ardipithecus kadabba", 5.8, 5.2, "neutral"), ("Ardipithecus ramidus", 4.5, 4.3, "neutral"),
      ("Australopithecus anamensis", 4.2, 3.8, "rna"), ("Australopithecus afarensis", 3.9, 2.9, "rna"),
      ("Australopithecus africanus", 3.3, 2.1, "rna"), ("Australopithecus sediba", 2.0, 1.95, "rna"),
      ("Paranthropus aethiopicus", 2.7, 2.3, "bone"), ("Paranthropus boisei", 2.3, 1.3, "bone"),
      ("Paranthropus robustus", 2.0, 1.0, "bone"), ("Homo habilis", 2.4, 1.5, "dna"),
      ("Homo erectus", 1.9, 0.11, "dna"), ("Homo heidelbergensis", 0.7, 0.2, "dna"),
      ("Homo naledi", 0.34, 0.23, "dna"), ("Homo neanderthalensis", 0.43, 0.04, "dna"),
      ("Homo floresiensis", 0.1, 0.05, "dna"), ("Homo sapiens", 0.3, 0.0, "dna")]
fig, ax = plt.subplots(figsize=(10.2, 5.2))
fig.subplots_adjust(left=0.27, right=0.97, bottom=0.11, top=0.98)
for k, (name, old, young, tok) in enumerate(SP):
    y = len(SP) - k
    w = max(old - young, 0.04)
    ax.barh(y, w, left=young, height=0.62, color=P.fill(tok), edgecolor=P.edge(tok), lw=0.9)
    ax.text(7.35, y, name, ha="right", va="center", fontsize=FT["small"], color=P.ink(), style="italic")
ax.set_xlim(7.2, -0.1)
ax.set_ylim(0.3, len(SP) + 0.7)
ax.set_yticks([])
charts.style_axes(ax, "time (Myr ago)")
ax.spines["left"].set_visible(False)
