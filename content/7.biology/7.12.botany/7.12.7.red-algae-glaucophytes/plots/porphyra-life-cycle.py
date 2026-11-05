"""Life cycle of Porphyra / Pyropia (laver). The haploid blade forms spermatangia and carpogonia; the zygote
divides mitotically into diploid carpospores, which bore into mollusc shells and grow into the filamentous
conchocelis phase (diploid), which survives the summer; in autumn the conchocelis releases conchospores,
and meiosis takes place when a conchospore germinates into a new blade. Monospores from blades give new
blades directly (dashed)."""
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(18, 14.4)
stages = [
    dict(text="Leafy blade (n)\nautumn to spring", size="small", bold=True, token="positive"),
    dict(text="Spermatangia and\ncarpogonia", size="small"),
    dict(text="Zygote (2n)", size="small"),
    dict(text="Carpospores (2n)", size="small"),
    dict(text="Conchocelis (2n)\nin mollusc shells, summer", size="small", bold=True, token="dna"),
    dict(text="Conchospores (2n)\nreleased in autumn", size="small"),
    dict(text="Young blade (n)", size="small"),
]
plant.alternation_of_generations(ax, (9.0, 7.0), 4.7, stages, meiosis=5, fertilization=1, gap=0.2,
                                 arrow_labels=[None, None, "Mitosis", "Bore into shell", None, "Meiosis at\ngermination", "Growth"],
                                 chords=[(0, 6, dict(dashed=True, text="monospores", bend=0.0))])
