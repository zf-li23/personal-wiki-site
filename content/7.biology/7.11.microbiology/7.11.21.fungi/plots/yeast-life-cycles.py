"""Three life cycles of ascomycete yeasts, distinguished by which ploidy can grow vegetatively. A: Saccharomyces
cerevisiae, haploid and diploid cells both bud indefinitely; diploids sporulate under starvation. B:
Schizosaccharomyces pombe, vegetative cells are haploid and divide by fission; the zygote formed by
conjugation undergoes meiosis at once (zygotic meiosis) and becomes an ascus of four spores (eight in
S. octosporus, after a further mitosis). C: Saccharomycodes ludwigii, vegetative cells are diploid; the four
ascospores fuse in pairs inside the ascus, so the haploid phase lasts only from meiosis to this fusion."""
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(30, 11.5)
specs = [
    ("A", "Saccharomyces cerevisiae", ["haploid a and α\ncells bud", "mating:\nzygote", "diploid cells\nbud", "ascus,\n4 ascospores"], 2, 0,
     ["", "", "", "germination"]),
    ("B", "Schizosaccharomyces pombe", ["haploid cells\n(fission)", "conjugation:\nzygote (2n)", "zygotic ascus,\n4 spores", ""], 1, 0,
     ["", "", "germination", ""]),
    ("C", "Saccharomycodes ludwigii", ["diploid cells\nbud", "ascus,\n4 ascospores", "spores fuse\nin pairs", ""], 0, 1,
     ["", "", "germination", ""]),
]
for k, (lt, name, st, mei, fert, labs) in enumerate(specs):
    cx = 5.0 + 10.0 * k
    steps = [s for s in st if s]
    n = len(steps)
    nodes = plant.alternation_of_generations(ax, (cx, 5.2), 3.0, [dict(text=s, shape="box", token="neutral") for s in steps],
                                             meiosis=mei, fertilization=fert, start=90,
                                             size="tiny", label_size="tiny", arrow_labels=labs[:n])
    bio.panel(ax, lt, (cx - 4.8, 11.2))
    bio.label(ax, (cx, 10.6), name, size="small", italic=True)
