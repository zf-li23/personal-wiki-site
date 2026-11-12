"""How large an animal can be if oxygen reaches its tissues by diffusion alone.

Steady-state diffusion with uniform consumption M (per unit volume) and surface concentration c0 gives a
maximum radius R = sqrt(6 D c0 / M) for a sphere, sqrt(4 D c0 / M) for a long cylinder and a maximum
half-thickness sqrt(2 D c0 / M) for a flat sheet (Formula 17.2.2 of 7.14.17). Parameters as there:
D = 2e-9 m^2/s in tissue, c0 = 0.25 mol/m^3 (water in equilibrium with air at 25 C). The vertical lines
mark an average human tissue consumption (2.6e-3 mol m^-3 s^-1) and one ten times lower, typical of
flatworms and the living tissue of jellyfish. Because the limit scales only as the inverse square root
of the metabolic rate, flattening or thinning the body does more than lowering the rate.
"""

import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(16.0, 9.6)
D, c0 = 2e-9, 0.25
M = np.logspace(-5, -2, 200)
p = quant.Plot(ax, (2.0, 1.5, 10.0, 7.2), xlim=(1e-5, 1e-2), ylim=(0.1, 20), xlabel="O$_2$ consumption M / (mol m$^{-3}$ s$^{-1}$)",
               ylabel="maximum size / mm", xlog=True, ylog=True, xticks=[1e-5, 1e-4, 1e-3, 1e-2], yticks=[0.1, 1, 10])
for k, tok, text in ((6, "dna", "sphere: radius"), (4, "positive", "cylinder: radius"), (2, "negative", "sheet: half-thickness")):
    p.line(M, np.sqrt(k * D * c0 / M) * 1e3, tok)
p.legend([("sphere: radius", "dna", "-"), ("long cylinder: radius", "positive", "-"), ("flat sheet: half-thickness", "negative", "-")], at=(2.5, 3.4), size="small", step=0.5)
p.vline(2.6e-3, text="human tissue", top=True)
p.vline(2.6e-4, text="flatworm, jellyfish", top=True)
bio.label(ax, (13.0, 7.6), "Diffusion alone", size="small", bold=True, ha="left")
bio.label(ax, (13.0, 6.9), "R ∝ (D c$_0$ / M)$^{1/2}$", size="small", ha="left")
bio.label(ax, (13.0, 5.8), "Solutions above\nthe limit:", size="small", ha="left")
bio.label(ax, (13.0, 4.3), "flatten (flatworms)\nthin and long (nemerteans)\ninert core (mesoglea)\ncirculation, gills,\ntracheae", size="tiny", ha="left", color=P.muted())
