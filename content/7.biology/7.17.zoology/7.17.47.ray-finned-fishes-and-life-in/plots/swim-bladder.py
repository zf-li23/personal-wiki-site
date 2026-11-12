# Model: Boyle's law and the swim bladder. Pressure at depth d (m) in seawater is p = p0 + rho*g*d, about
# (1 + d/10) atm. A bladder that holds a fixed amount of gas has volume V = V_n * p_n / p, where V_n is the
# volume that gives neutral buoyancy at the fish's home depth d_n. (A) V/V_n against depth for fish neutral
# at 0, 10, 50 and 200 m. (B) Fractional volume change per metre of vertical movement, 1/(10 + d), which
# sets how quickly a fish without gas secretion must correct its buoyancy.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22, 8.5)
d = np.linspace(0, 100, 300)
p = quant.Plot(ax, (1.6, 1.4, 8.6, 6.0), xlim=(0, 100), ylim=(0, 4), xlabel="depth / m",
               ylabel="bladder volume / volume at home depth", xticks=[0, 25, 50, 75, 100],
               yticks=[0, 1, 2, 3, 4])
p.hline(1, text="neutral buoyancy", size="tiny")
for dn, tok in ((0, "lipid"), (10, "dna"), (50, "metabolite")):
    v = (10 + dn) / (10 + d)
    keep = v <= 4
    p.line(d[keep], v[keep], tok, text=f"neutral at {dn} m", at=0.3 if dn else 0.08)
    p.points([dn], [1], tok)
bio.panel(ax, "A", (0.4, 8.1))
q = quant.Plot(ax, (13.0, 1.4, 8.4, 6.0), xlim=(0, 200), ylim=(0, 10.5), xlabel="depth / m",
               ylabel="volume change per metre / %", xticks=[0, 50, 100, 150, 200], yticks=[0, 2, 4, 6, 8, 10])
dd = np.linspace(0, 200, 300)
q.line(dd, 100 / (10 + dd), "dna")
q.text(60, 7.0, "relative change 1/(10 m + d)", size="tiny", ha="left")
bio.panel(ax, "B", (11.8, 8.1))
