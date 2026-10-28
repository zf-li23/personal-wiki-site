"""Dihybrid cross RrYy x RrYy (Mendel's seed shape and cotyledon color): 16 gamete combinations,
nine genotypes, four phenotypes in the ratio 9:3:3:1."""
import wikibio as bio
from wikibio import genetics as G

fig, ax = bio.canvas(14.0, 6.6)
names = {"R_Y_": "Round, yellow", "R_yy": "Round, green", "rrY_": "Wrinkled, yellow", "rryy": "Wrinkled, green"}
G.punnett(ax, (2.0, 5.2), "RrYy", "RrYy", cell=1.15, phenotype=names, titles=("Pollen", "Egg cells"),
          colors={"Round, yellow": "highlight", "Round, green": "positive", "Wrinkled, yellow": "trna",
                  "Wrinkled, green": "enzyme"})
