"""Why loss-of-function alleles are usually recessive (Kacser and Burns 1981).

Flux through a pathway as a function of the amount E of one enzyme (wild-type homozygote E = 1):
J(E) = Jmax E / (E + K_E), K_E = 1/(k R) with R the resistance of the other steps (Formula 3.2.1).
Curves for K_E = 0.05 (low control, C = 0.048 at E = 1) and K_E = 1 (high control, C = 0.5). Markers:
homozygous null (E = 0), heterozygote (E = 0.5), wild type (E = 1). Fluxes relative to the wild type.
"""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(14.0, 9.6)
p = quant.Plot(ax, (2.0, 1.6, 10.8, 7.2), xlim=(0, 1.6), ylim=(0, 1.2), xlabel="enzyme amount E (wild type = 1)",
               ylabel="flux J / J(wild type)", xticks=[0, 0.5, 1, 1.5], yticks=[0, 0.25, 0.5, 0.75, 1.0], grid=True)
E = np.linspace(0, 1.6, 300)
for K, tok, txt, xy in ((0.05, "positive", "$K_E = 0.05$: null allele recessive", (0.1, 1.08)),
                        (1.0, "negative", "$K_E = 1$: heterozygote intermediate", (1.03, 0.8))):
    J = (E / (E + K)) / (1 / (1 + K))
    p.line(E, J, tok)
    p.text(xy[0], xy[1], txt, size="small", token=tok, ha="left")
    for e, name in ((0.0, "aa"), (0.5, "Aa"), (1.0, "AA")):
        j = (e / (e + K)) / (1 / (1 + K))
        p.points([e], [j], tok, r=0.11)
    j5 = (0.5 / (0.5 + K)) / (1 / (1 + K))
    p.text(0.53, j5 - 0.06, f"{j5:.2f}", size="tiny", token=tok, ha="left")
for e, name in ((0.0, "null homozygote"), (0.5, "heterozygote"), (1.0, "wild type")):
    p.vline(e, text=name, top=True) if e > 0 else None
p.hline(1.0, text=None)
