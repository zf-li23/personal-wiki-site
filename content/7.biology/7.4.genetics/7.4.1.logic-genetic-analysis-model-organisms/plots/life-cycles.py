"""The three eukaryotic life cycles, classified by where meiosis falls (Definition 1.4.2).

Blue sector: diploid (2n) phase; orange sector: haploid (n) phase. Zygotic meiosis (Chlamydomonas,
Neurospora): only the zygote is diploid. Gametic meiosis (animals): only the gametes are haploid.
Sporic meiosis (land plants): a multicellular sporophyte (2n) alternates with a multicellular gametophyte (n).
"""
import wikibio as bio
from wikibio import plant

fig, ax = bio.canvas(30.0, 11.2)
r = 2.9
cycles = [
    ("A", "Zygotic meiosis", "Chlamydomonas, Neurospora",
     ["Zygote (2n)", "Spores (n)", "Haploid\norganism (n)", "Gametes (n)"], 0, 3,
     [None, "Mitosis", "Mitosis or\ndifferentiation", None]),
    ("B", "Gametic meiosis", "animals",
     ["Diploid\norganism (2n)", "Gametes (n)", "Zygote (2n)"], 0, 1, [None, None, "Mitosis"]),
    ("C", "Sporic meiosis", "land plants: alternation of generations",
     ["Sporophyte (2n)", "Spores (n)", "Gametophyte (n)", "Gametes (n)", "Zygote (2n)"], 0, 3,
     [None, "Mitosis", "Mitosis", None, "Mitosis"]),
]
for k, (letter, title, who, steps, mei, fert, labs) in enumerate(cycles):
    cx = 5.0 + k * 10.0
    bio.panel(ax, letter, (cx - 4.8, 10.9))
    bio.label(ax, (cx, 10.6), title, size="title", bold=True)
    bio.label(ax, (cx, 10.0), who, size="small", italic=k == 0)
    plant.alternation_of_generations(ax, (cx, 5.0), r, [dict(text=s, w=2.6, h=0.95) for s in steps],
                                     meiosis=mei, fertilization=fert, arrow_labels=labs, size="small",
                                     shape="box", token="neutral", labels=("", ""))

from matplotlib.patches import FancyBboxPatch

P = bio.P
for i, (tok, text) in enumerate((("dna", "diploid phase (2n)"), ("rna", "haploid phase (n)"))):
    x = 10.6 + i * 5.2
    ax.add_patch(FancyBboxPatch((x, 0.45), 0.6, 0.45, boxstyle="round,pad=0,rounding_size=0.08",
                                facecolor=P.mix(P.surface(), P.fill(tok), 0.3), edgecolor=P.edge(tok), lw=0.8))
    bio.label(ax, (x + 0.8, 0.67), text, size="small", ha="left")
