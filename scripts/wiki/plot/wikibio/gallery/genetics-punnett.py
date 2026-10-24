# Dihybrid cross RrYy x RrYy (Mendel's pea seeds): 16 combinations of gametes, 9:3:3:1 phenotypes
import wikibio as bio
from wikibio import genetics as G

fig, ax = bio.canvas(12.4, 6.2)
names = {"R_Y_": "Round, yellow", "R_yy": "Round, green", "rrY_": "Wrinkled, yellow", "rryy": "Wrinkled, green"}
G.punnett(ax, (2.0, 4.9), "RrYy", "RrYy", cell=1.15, phenotype=names, titles=("Pollen", "Egg cells"),
          colors={"Round, yellow": "highlight", "Round, green": "positive", "Wrinkled, yellow": "trna",
                  "Wrinkled, green": "enzyme"})
