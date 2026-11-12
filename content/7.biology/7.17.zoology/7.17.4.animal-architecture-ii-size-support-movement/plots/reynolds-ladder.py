"""Reynolds numbers of moving organisms, Re = rho U L / mu, on a logarithmic scale.

Values from Vogel (1994), Life in Moving Fluids, 2nd ed. (Princeton University Press), for the speeds
stated there. Shaded regions: viscosity-dominated (Re < 1), intermediate, and inertia-dominated (Re > 1000)
regimes, with the typical propulsive mechanisms of each.
"""

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(24.0, 11.0)

ROWS = [
    ("bacterium, swimming at 0.01 mm/s", 1e-5, "bacterium"),
    ("sea urchin sperm at 0.2 mm/s", 3e-2, "neutral"),
    ("invertebrate larva, 0.3 mm long, at 1 mm/s", 0.3, "neutral"),
    ("smallest flying insects", 30, "positive"),
    ("copepod in a pulse of 20 cm/s", 300, "positive"),
    ("large dragonfly at 7 m/s", 3e4, "atp"),
    ("duck flying at 20 m/s", 3e5, "atp"),
    ("tuna swimming at 10 m/s", 3e7, "dna"),
    ("large whale swimming at 10 m/s", 3e8, "dna"),
]

box = (1.0, 1.6, 22.0, 7.6)
p = quant.Plot(ax, box, xlim=(1e-6, 1e9), ylim=(0, len(ROWS) + 0.6), xlabel="Reynolds number  Re = ρUL/μ",
               xlog=True, frame=None,
               xticks=[(10.0 ** k, f"10$^{{{k}}}$") for k in range(-6, 10, 2)])
x0, y0, w, h = box
ax.plot([x0, x0 + w], [y0, y0], color=P.muted(), lw=0.8)
p.span(1e-6, 1.0, "dna", text="viscosity dominates: cilia, flagella", strength=0.8)
p.span(1.0, 1e3, "highlight", text="intermediate", strength=0.8)
p.span(1e3, 1e9, "atp", text="inertia dominates: fins, tails, wings, jets", strength=0.85)
for k, (name, re, tok) in enumerate(ROWS):
    yy = k + 0.9
    p.points([re], [yy], token=tok, r=0.16)
    if re < 1e5:
        p.text(re, yy, "   " + name, size="small", ha="left")
    else:
        p.text(re, yy, name + "   ", size="small", ha="right")
