"""A: genome size and GC content of obligate endosymbionts of animals compared with free-living bacteria
(symbiont values from Madigan et al. 2019, Table 23.2; ranges shown as segments). B: GC content approaching
mutational equilibrium, GC* = u / (u + v), when selection on base composition is negligible; u is the rate of
AT->GC and v of GC->AT mutations per site (illustrative ratios)."""
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(25, 9.6)

bio.panel(ax, "A", (0.2, 9.4))
p = quant.Plot(ax, (2.0, 1.6, 11.0, 7.0), xlim=(0.1, 10), ylim=(10, 70), xlog=True,
               xlabel="genome size / Mb", ylabel="GC / %",
               xticks=[(0.1, "0.1"), (0.3, "0.3"), (1, "1"), (3, "3"), (10, "10")], yticks=[10, 30, 50, 70])
sym = [("Buchnera", (0.42, 0.62), (20, 26)), ("Wigglesworthia", (0.70, 0.70), (22, 22)),
       ("Blochmannia", (0.71, 0.79), (27, 30)), ("Sulcia", (0.25, 0.25), (22, 22)),
       ("Moranella", (0.54, 0.54), (43.5, 43.5)), ("Tremblaya", (0.14, 0.14), (58.8, 58.8)),
       ("Ruthia (clam)", (1.2, 1.2), (34, 34))]
offs = {"Buchnera": (-0.22, 3.6), "Wigglesworthia": (0.06, -3.2), "Blochmannia": (0.08, 3.0), "Sulcia": (0, -3.2),
        "Moranella": (0, 3.0), "Tremblaya": (0.3, -3.4), "Ruthia (clam)": (0, 3.0)}
for name, (s0, s1), (g0, g1) in sym:
    xs, ys = np.array([s0, s1]), np.array([g0, g1])
    if s0 != s1 or g0 != g1:
        p.line(xs, ys, token="negative", lw=3)
    p.points([np.mean(xs)], [np.mean(ys)], token="negative", r=0.11)
    dx, dy = offs[name]
    p.text(np.mean(xs) * (1 + dx), np.mean(ys) + dy, name, token="negative", italic=not name.startswith("Ruthia"))
free = [("E. coli", 4.64, 50.8), ("B. subtilis", 4.2, 43.5), ("P. aeruginosa", 6.3, 66.6), ("S. meliloti", 6.7, 62.1)]
for name, s, g in free:
    p.points([s], [g], token="dna", r=0.11)
    p.text(s, g - 3.2, name, token="dna", italic=True)
p.text(0.12, 67, "obligate endosymbionts", token="negative", ha="left")
p.text(0.12, 63.5, "free-living bacteria", token="dna", ha="left")

bio.panel(ax, "B", (14.4, 9.4))
q = quant.Plot(ax, (16.2, 1.6, 8.0, 7.0), xlim=(0, 3), ylim=(10, 60), xlabel="mutations per site (u + v) t",
               ylabel="GC / %", xticks=[0, 1, 2, 3], yticks=[10, 30, 50])
tau = np.linspace(0, 3, 300)
for ratio, tok, txt in ((1.0, "dna", "v/u = 1"), (2.0, "enzyme", "v/u = 2"), (3.0, "negative", "v/u = 3")):
    eq = 1 / (1 + ratio)
    gc = eq + (0.5 - eq) * np.exp(-tau)
    q.line(tau, 100 * gc, token=tok)
    q.text(1.5, 100 * eq + (5.5 if ratio == 2.0 else -3.0), f"{txt}: GC* = {100 * eq:.0f} %", token=tok, ha="left")
