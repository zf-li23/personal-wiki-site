# Why compound eyes have the facets they have: a model of resolution (after Barlow 1952; Kirschfeld 1976).
# In an eye of radius R with facet diameter D, the sampling angle between neighbouring ommatidia is
# Delta phi = D / R, and diffraction at each facet blurs the image over about lambda / D. The total blur
# sqrt((D/R)^2 + (lambda/D)^2) is smallest at D* = sqrt(lambda R). Curves: lambda = 0.5 um; eye radii
# 0.25, 0.5, 1 and 2 mm. Even at the optimum a 1-mm eye resolves only about 1.8 deg, some hundred times
# coarser than the human fovea (about 0.017 deg).
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(15, 9)
lam = 0.5e-6
D = np.linspace(3e-6, 60e-6, 400)
p = quant.Plot(ax, (1.8, 1.4, 12.4, 6.8), xlim=(0, 60), ylim=(0, 6), xlabel="Facet diameter D / µm",
               ylabel="Angular resolution / °", xticks=[0, 10, 20, 30, 40, 50, 60], yticks=[0, 1, 2, 3, 4, 5, 6])
for R, tok in ((0.25e-3, "rna"), (0.5e-3, "protein"), (1e-3, "dna"), (2e-3, "enzyme")):
    blur = np.degrees(np.sqrt((D / R) ** 2 + (lam / D) ** 2))
    m = blur <= 6
    p.line(D[m] * 1e6, blur[m], tok)
    Ds = np.sqrt(lam * R)
    b = np.degrees(np.sqrt(2 * lam / R))
    p.points([Ds * 1e6], [b], tok, r=0.09)
    j = np.nonzero(m)[0][-1]
    xe = min(D[j] * 1e6, 52)
    ye = blur[np.searchsorted(D * 1e6, xe)]
    bio.label(ax, p.xy(xe + 0.8, ye - 0.25), f"R = {R * 1e3:g} mm", size="tiny", color=quant.line_color(tok), ha="left")
bio.label(ax, p.xy(28, 0.95), "Dots: optimum D* = √(λR)", size="small")
bio.label(ax, p.xy(4.5, 0.5), "diffraction\nλ/D", size="tiny", color=P.muted())
bio.label(ax, p.xy(45, 0.5), "sampling D/R", size="tiny", color=P.muted())
