# Model: patterns of temperature-dependent sex determination (Bull 1980), drawn as logistic reaction norms
# m(T) = 1 / (1 + exp(+-(T - T_piv) / s)) for the proportion of males hatching at constant incubation
# temperature T. T_piv, the pivotal temperature, gives a 1:1 sex ratio; the transitional range (about 4 s
# wide) gives mixed sexes. Parameters are approximate literature values: pattern Ia (males cool, females
# warm), loggerhead sea turtle Caretta caretta, T_piv ~ 29 C; pattern Ib (females cool, males warm), tuatara
# Sphenodon punctatus, T_piv ~ 22 C; pattern II (females at both extremes, males in between), American
# alligator Alligator mississippiensis, males at 32-33 C. Schematic.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
T = np.linspace(18, 37, 400)


def logistic(T, piv, s, up=True):
    z = (T - piv) / s
    return 1 / (1 + np.exp(-z if up else z))


fig, ax = bio.canvas(16, 8.5)
p = quant.Plot(ax, (1.8, 1.4, 12.6, 6.0), xlim=(18, 37), ylim=(0, 1.05), xlabel="incubation temperature / C",
               ylabel="proportion male", xticks=[18, 22, 26, 30, 34], yticks=[0, 0.5, 1])
p.hline(0.5, text="1:1", size="tiny")
p.line(T, logistic(T, 29.0, 0.45, up=False), "dna")
p.text(27.2, 0.62, "Ia  Caretta (males cool)", token="dna", ha="right")
Tt = T[T <= 25.5]  # tuatara eggs are incubated at 18-25 C in nature
p.line(Tt, logistic(Tt, 22.0, 0.5, up=True), "positive")
p.text(22.4, 0.35, "Ib  Sphenodon (males warm)", token="positive", ha="left")
m2 = logistic(T, 31.5, 0.35, up=True) * logistic(T, 34.3, 0.3, up=False)
p.line(T, m2, "mrna", text="II  Alligator", at=0.83, dy=0.1)
p.vline(29.0, text="pivotal temperature", size="tiny")
