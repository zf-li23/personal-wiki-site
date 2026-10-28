# Cytogenetics of rearrangements: inversion loop with crossover products, translocation quadrivalent, NAHR, polyploid pairing
import wikibio as bio
from wikibio import cytogenetics as C

P = bio.P
fig, ax = bio.canvas(31, 9.5)
N = list("AB") + ["o"] + list("CDEFG")
bio.panel(ax, "A", (0.2, 9.3))
r = C.inversion_loop(ax, (1.0, 5.6), N, "D", "F", crossover=("D", "E"), unit=0.7)
y = 3.0
for p in r["products"]:
    d = C.describe(p, N)
    o = C.lettered(ax, (1.0, y), p, unit=0.4, height=0.3)
    bio.label(ax, (o["x1"] + 0.3, y), d["kind"], size="tiny", ha="left", color=P.muted())
    y -= 0.6
bio.panel(ax, "B", (10.0, 9.3))
C.translocation_cross(ax, (13.4, 5.2), (["A", "o", "B"], ["C", "D"], ["W", "o", "X"], ["Y", "Z"]), arm=2.7)
bio.panel(ax, "C", (18.4, 9.3))
a = [("A", "dna"), ("R", "highlight"), ("B", "dna"), ("R", "highlight"), ("C", "dna")]
C.lettered(ax, (19.0, 8.0), a, unit=0.5)
C.lettered(ax, (19.0 + 1.0, 7.4), [(n, "receptor" if t == "dna" else t) for n, t in a], unit=0.5)
for i, prod in enumerate(C.nahr_products(a, 3, [(n, "receptor" if t == "dna" else t) for n, t in a], 1)):
    C.lettered(ax, (19.0, 6.2 - 0.6 * i), prod, unit=0.5)
bio.panel(ax, "D", (25.0, 9.3))
C.polyploid_pairing(ax, (28.0, 6.9), "bivalents", length=3.4, alleles=["A", "A", "a", "a"])
C.polyploid_pairing(ax, (28.0, 2.9), "quadrivalent", length=3.4, alleles=["A", "A", "a", "a"])
g = C.tetrasomic_gametes(2, 1 / 7)
bio.label(ax, (28.0, 0.6), f"AAaa, α = 1/7: AA {g[2]:.3f}, Aa {g[1]:.3f}, aa {g[0]:.3f}", size="tiny", color=P.muted())
