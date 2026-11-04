"""Assembly of the gut community in the first years of life (schematic trajectories, drawn from the pattern
described by Madigan et al. 2019 and the cohort studies cited there; not measured data).
A: relative abundance of four groups from birth to adulthood, with weaning as the decisive transition.
B: diversity (richness) rising to an adult plateau, with a cesarean-born, formula-fed trajectory lagging."""
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25, 9.6)


def logistic(x, x0, k):
    return 1 / (1 + np.exp(-(x - x0) / k))


m = np.linspace(0, 36, 400)  # age in months

bio.panel(ax, "A", (0.2, 9.4))
p = quant.Plot(ax, (2.2, 1.8, 11.4, 7.0), xlim=(0, 36), ylim=(0, 0.72), xlabel="age / months",
               ylabel="relative abundance", xticks=[0, 6, 12, 18, 24, 30, 36],
               yticks=[(0, "0"), (0.2, "0.2"), (0.4, "0.4"), (0.6, "0.6")])
bifido = 0.62 * (1 - logistic(m, 11, 3.0)) + 0.04
entero = 0.30 * np.exp(-m / 2.5) + 0.03
bacteroides = 0.05 + 0.26 * logistic(m, 10, 3.5)
firmicutes = 0.06 + 0.42 * logistic(m, 13, 4.0)
p.line(m, bifido, token="positive")
p.text(2.0, 0.60, "Bifidobacterium", token="positive", ha="left", italic=True)
p.line(m, entero, token="negative")
p.text(2.0, 0.26, "Enterobacteriaceae", token="negative", ha="left")
p.line(m, bacteroides, token="metabolite")
p.text(26, 0.345, "Bacteroidota", token="metabolite", ha="right")
p.line(m, firmicutes, token="enzyme")
p.text(26, 0.52, "Bacillota (fiber degraders)", token="enzyme", ha="right")
p.span(9, 15, "highlight", strength=0.4)
p.text(12, 0.69, "weaning", color=P.muted())

bio.panel(ax, "B", (14.6, 9.4))
q = quant.Plot(ax, (16.6, 1.8, 7.4, 7.0), xlim=(0, 36), ylim=(0, 1.05), xlabel="age / months",
               ylabel="richness (rel. to adult)", xticks=[0, 12, 24, 36], yticks=[0, 0.5, 1])
vag = logistic(m, 9, 4.5) * 0.98 + 0.02
csec = logistic(m, 14, 5.0) * 0.98 + 0.01
q.line(m, vag, token="dna")
q.text(13, 0.92, "vaginal birth,\nbreast-fed", token="dna", ha="left")
q.line(m, csec, token="negative", dashed=True)
q.text(20, 0.33, "cesarean birth,\nformula-fed", token="negative", ha="left")
q.hline(1.0, text="adult level", size="tiny")
