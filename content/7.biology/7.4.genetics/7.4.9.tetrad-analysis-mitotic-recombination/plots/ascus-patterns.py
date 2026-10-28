# Ordered asci (MI and MII patterns) and the three kinds of unordered tetrads
import wikibio as bio
from wikibio import transmission as T

fig, ax = bio.canvas(24, 9.6)
W, K = "bone", "ink"
bio.panel(ax, "A", (0.2, 9.4))
pats = [("MI", [K] * 4 + [W] * 4), ("MI", [W] * 4 + [K] * 4),
        ("MII", [K, K, W, W, K, K, W, W]), ("MII", [W, W, K, K, W, W, K, K]),
        ("MII", [K, K, W, W, W, W, K, K]), ("MII", [W, W, K, K, K, K, W, W])]
for k, (name, sp) in enumerate(pats):
    x = 1.5 + k * 1.55 + (0.6 if k >= 2 else 0)
    T.ascus(ax, (x, 4.9), sp, spore=0.42)
    bio.label(ax, (x, 1.7), name, size="small")
bio.label(ax, (2.3, 8.7), "first-division\nsegregation", size="small")
bio.label(ax, (7.6, 8.7), "second-division segregation", size="small")
bio.label(ax, (5.5, 0.8), r"dark spores: $\it{ws}^{+}$   pale spores: $\it{ws}$", size="tiny", color=bio.P.muted())

bio.panel(ax, "B", (12.6, 9.4))
tets = [("PD", ["AB", "AB", "ab", "ab"]), ("NPD", ["Ab", "Ab", "aB", "aB"]), ("T", ["AB", "Ab", "aB", "ab"])]
tok = {"AB": "dna", "ab": "receptor", "Ab": "enzyme", "aB": "antibody"}
for k, (name, g) in enumerate(tets):
    x = 14.6 + k * 3.3
    T.tetrad(ax, (x, 5.0), g, tokens=[tok[s] for s in g], r=0.5, spread=0.62, size="small")
    bio.label(ax, (x, 3.2), name, size="normal", bold=True)
    bio.label(ax, (x, 2.5), {"PD": "parental ditype", "NPD": "nonparental ditype", "T": "tetratype"}[name],
              size="tiny", color=bio.P.muted())
bio.label(ax, (17.9, 8.7), r"unordered tetrads from $\it{AB} \times \it{ab}$", size="small")
