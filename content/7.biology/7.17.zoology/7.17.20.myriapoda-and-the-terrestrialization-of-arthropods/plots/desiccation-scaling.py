# A model of desiccation and body size. A cylindrical animal of radius r and length L holds water in
# proportion to its volume (pi r^2 L) but loses it through its surface (2 pi r L), so the time to lose a
# given fraction f of its water is t = f w rho r / (2 P dp): proportional to radius and inversely
# proportional to the cuticular permeability P. Here f = 0.2 (a lethal loss for many arthropods), body water
# w = 0.7, density rho = 1 g cm^-3, and dp = 3.2 kPa (24 mmHg, dry air at 25 C); respiratory loss is
# ignored. The three permeabilities (1, 10 and 100 ug cm^-2 h^-1 mmHg^-1) are illustrative values spanning
# the range reported for terrestrial arthropods, from desert scorpions and beetles to woodlice and
# centipedes (Hadley 1994). Schematic model, not data.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(15, 9)
d_mm = np.logspace(-1, 1, 200)            # body diameter, mm
r_cm = d_mm / 20.0
f, w, rho_ug = 0.2, 0.7, 1e6               # rho in ug cm^-3
dp = 24.0                                  # mmHg
p = quant.Plot(ax, (1.8, 1.4, 12.4, 6.9), xlim=(0.1, 10), ylim=(0.01, 1000), xlog=True, ylog=True,
               xlabel="Body diameter / mm", ylabel="Time to lose 20 % of body water / h",
               xticks=[0.1, 1, 10], yticks=[0.01, 0.1, 1, 10, 100, 1000])
for Pc, tok, lab in ((1, "dna", "P = 1 (waxed, desert)"), (10, "enzyme", "P = 10"), (100, "rna", "P = 100 (unwaxed, humid habitats)")):
    t = f * w * rho_ug * r_cm / (2 * Pc * dp)
    p.line(d_mm, t, tok)
    x, y = p.xy(0.12, t[2] * 1.6)
    bio.label(ax, (x, y), lab, size="tiny", ha="left", color=quant.line_color(tok))
p.hline(24, text="one day", side="right")
p.hline(1, text="one hour", side="right")
bio.label(ax, p.xy(1.5, 0.02), "t ∝ r / P: halving size halves survival time", size="small")
