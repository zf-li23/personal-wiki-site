"""Norms of reaction (schematic, illustrative numbers only).

Phenotype z of three genotypes over an environmental gradient T (e.g. rearing temperature).
A: additive model z = mu_g + b T (parallel lines, no G x E). B: z = mu_g + b_g T with genotype-specific
slopes, so the lines cross (G x E): the ranking of the genotypes depends on the environment.
"""
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24.0, 8.6)
T = np.linspace(15, 30, 50)
toks = ["dna", "highlight", "negative"]
for k, (letter, slopes, inter) in enumerate((("A", [-1.0, -1.0, -1.0], [70, 60, 50]),
                                             ("B", [-40 / 15, -5 / 15, 35 / 15], [60, 45, 25]))):
    x0 = 2.0 + k * 11.8
    bio.panel(ax, letter, (x0 - 1.6, 8.5))
    p = quant.Plot(ax, (x0, 1.5, 8.0, 6.0), xlim=(15, 30), ylim=(0, 70), xlabel="environment (temperature) / °C",
                   ylabel="phenotype (arbitrary units)", xticks=[15, 20, 25, 30], yticks=[0, 20, 40, 60])
    for g, (b, a, tok) in enumerate(zip(slopes, inter, toks)):
        z = a + b * (T - 15)
        p.line(T, z, tok, text=f"genotype {g + 1}", at=1.0, dx=0.1, dy=0.0, size="small")
    bio.label(ax, (x0 + 4.2, 7.9), "no G×E: parallel norms" if k == 0 else "G×E: norms cross", size="normal",
              bold=True)
