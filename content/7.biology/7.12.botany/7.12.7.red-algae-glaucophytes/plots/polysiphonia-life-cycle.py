"""Triphasic life cycle of Polysiphonia. Blue sector: diploid phase; orange sector: haploid phase. The three
generations are boxed in different colours: gametophytes (green), carposporophyte (orange), tetrasporophyte
(blue). Gametophytes and tetrasporophyte look alike (isomorphic)."""
import wikibio as bio
from wikibio import plant

fig, ax = bio.canvas(18, 15)
G, C, T = "positive", "highlight", "dna"
stages = [
    dict(text="Tetraspores (n)", size="small"),
    dict(text="Male and female\ngametophytes (n)", size="small", bold=True, token=G),
    dict(text="Spermatium on the\ntrichogyne of a carpogonium", size="small", token=G),
    dict(text="Zygote (2n)\nin the carpogonium", size="small"),
    dict(text="Carposporophyte (2n)\nin a cystocarp, on the female", size="small", bold=True, token=C),
    dict(text="Carpospores (2n)", size="small", token=C),
    dict(text="Tetrasporophyte (2n)", size="small", bold=True, token=T),
    dict(text="Tetrasporangia", size="small", token=T),
]
plant.alternation_of_generations(ax, (9.0, 7.4), 5.0, stages, meiosis=7, fertilization=2, gap=0.2,
                                 arrow_labels=["Germination", None, None, "Gonimoblast", "Release", "Germination", None, None])
