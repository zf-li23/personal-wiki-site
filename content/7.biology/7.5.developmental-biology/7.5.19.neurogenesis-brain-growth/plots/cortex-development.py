"""Development of the mammalian neocortex (schematic strips of the dorsal telencephalic wall; ventricle at the
bottom, pial surface at the top). Early: a pseudostratified neuroepithelium and the preplate of the first-born
neurons. Mid-neurogenesis: apical radial glia in the ventricular zone (VZ) with fibres reaching the pia; outer
radial glia (basal fibre only, dashed) and intermediate progenitors in the subventricular zone (SVZ); newborn neurons
migrate along the glial fibres through the intermediate zone (IZ) into the cortical plate (CP), below the marginal
zone (MZ). Late: the cortical plate holds successive cohorts of neurons; each new cohort migrates past the earlier
ones, so the earliest-born neurons lie deepest (teal) and the latest-born most superficial (pink): inside-out."""
import wikibio as bio
from wikibio import neurodev as N

fig, ax = bio.canvas(18, 9.4)
P = bio.P
for k, (st, title) in enumerate((("early", "Early (preplate)"), ("mid", "Mid-neurogenesis"), ("late", "Late: inside-out"))):
    x0 = 0.8 + k * 6.0
    c = N.cortex_layers(ax, (x0, 1.0), 3.6, 7.0, st, glia=4, seed=k)
    bio.label(ax, (x0 + 1.8, 8.7), title, bold=True)
    for name in ("VZ", "SVZ", "IZ", "CP", "MZ", "PP"):
        if name in c:
            bio.label(ax, (x0 + 3.75, c[name]), name, size="small", ha="left")
    bio.label(ax, (x0 + 1.8, 0.55), "ventricle (apical)", size="tiny", color=P.muted())
    bio.label(ax, (x0 + 1.8, 8.25), "pia (basal)", size="tiny", color=P.muted())
bio.label(ax, (15.0, 0.2), "cohorts: early (deep)    middle    late (superficial)", size="tiny", color=P.muted())
for k, tok in enumerate(c["cohorts"]):
    ax.add_patch(__import__("matplotlib").patches.Polygon([(13.55 + k * 1.15, 0.05), (13.43 + k * 1.15, -0.13), (13.67 + k * 1.15, -0.13)],
                 closed=True, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.5))
ax.set_ylim(-0.3, 9.1)
