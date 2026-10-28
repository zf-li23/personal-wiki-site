"""An F3 screen for recessive mutations on chromosome 2 of Drosophila. A mutagenized chromosome (asterisk)
is kept opposite the balancer CyO through two generations of crosses; in the F3 a quarter of the zygotes,
and a third of the survivors, are homozygous for the mutagenized chromosome and are scored."""
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(16.0, 12.0)
LAB = {"*": "receptor", "+": "dna", "CyO": "neutral"}


def pair(x, y, left, right, length=1.5):
    """Two homologous chromosomes 2 side by side, labelled under each."""
    for dx, name in ((-0.32, left), (0.32, right)):
        G.chromosome(ax, (x + dx, y), length=length, centromere=0.45, width=0.34, token=LAB[name], sister=False)
        bio.label(ax, (x + dx, y - length / 2 - 0.3), name if name != "*" else "$*$", size="small", italic=name == "CyO")
    return (x, y - length / 2 - 0.3)


rows = [10.9, 8.2, 5.5, 2.4]
names = ["P", "F1", "F2", "F3"]
for y, n in zip(rows, names):
    bio.label(ax, (0.6, y), n, size="title", bold=True, ha="left")

# P: mutagenized male x balancer female
pair(3.0, rows[0], "*", "+")
bio.label(ax, (3.0, rows[0] + 1.15), "mutagenized male", size="small")
bio.label(ax, (5.3, rows[0]), "×", size="title")
pair(7.6, rows[0], "CyO", "+")
bio.label(ax, (7.6, rows[0] + 1.15), "balancer female", size="small")
bio.arrow(ax, (1.7, rows[0] - 1.0), (1.7, rows[1] + 1.0), kind="process")

# F1: single males */CyO, each a separate line
pair(3.0, rows[1], "*", "CyO")
bio.label(ax, (3.4, rows[1] + 1.15), "single male, one mutagenized genome", size="small")
bio.label(ax, (5.3, rows[1]), "×", size="title")
pair(7.6, rows[1], "CyO", "+")
bio.label(ax, (7.6, rows[1] + 1.15), "balancer female", size="small")
bio.label(ax, (11.2, rows[1]), "one vial per male:\nseparate lines", size="small", color=P.muted())
bio.arrow(ax, (1.7, rows[1] - 1.0), (1.7, rows[2] + 1.0), kind="process")

# F2: intercross of siblings
pair(3.0, rows[2], "*", "CyO")
bio.label(ax, (5.3, rows[2]), "×", size="title")
pair(7.6, rows[2], "*", "CyO")
bio.label(ax, (5.3, rows[2] + 1.2), "siblings of one line, intercrossed", size="small")
bio.arrow(ax, (1.7, rows[2] - 1.0), (1.7, rows[3] + 1.0), kind="process")

# F3: the three classes
classes = [("*", "*", "1/4", "scored:\nhomozygous"), ("*", "CyO", "1/2", "Curly"),
           ("CyO", "CyO", "1/4", "dies")]
for k, (a, b, frac, note) in enumerate(classes):
    x = 3.0 + k * 3.3
    pair(x, rows[3], a, b)
    bio.label(ax, (x, rows[3] - 1.35), frac, size="normal", bold=True)
    bio.label(ax, (x, rows[3] - 1.95), note, size="small", va="top",
              color=P.edge("positive") if k == 0 else P.muted())
bio.label(ax, (13.4, rows[3] - 0.2), "a third of the\nsurvivors are $*/*$", size="small", color=P.muted())
bio.label(ax, (13.4, rows[2] + 0.5), "no crossing over\nwith the balancer", size="small", color=P.muted())
