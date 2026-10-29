# wikibio.neurodev sampler. Top row: neurulation in four transverse sections (neural plate; folds rising
# about the median hinge point; folds converging at the dorsolateral hinges; closed neural tube with the neural
# crest delaminating), with notochord, paraxial mesoderm, lateral plate and endoderm. Bottom row: the
# dorso-ventral progenitor domains of the spinal cord, a strip of late cortex (inside-out cohorts on radial
# glia), a growth cone, and the optic cup with the lens pit.
import wikibio as bio
from wikibio import neurodev as N

fig, ax = bio.canvas(26, 15)
P = bio.P
for k, st in enumerate(("plate", "fold", "converge", "tube")):
    x = 3.3 + k * 6.45
    a = N.neurulation_section(ax, (x, 12.6), 6.0, st)
    bio.label(ax, (x, 14.6), st.capitalize(), bold=True)
    if k == 0:
        bio.callout(ax, a["neural"], (x + 0.5, 13.9), "Neural plate")
        bio.callout(ax, a["crest_r"], (x + 2.2, 13.9), "Border (crest)")
        bio.callout(ax, a["notochord"], (x - 1.6, 10.0), "Notochord")
    if k == 3:
        bio.callout(ax, a["lumen"], (x + 2.6, 13.9), "Neural tube")
        bio.callout(ax, a["somite_r"], (x + 2.9, 10.0), "Somite")
        bio.callout(ax, a["crest_l"], (x - 2.6, 13.9), "Neural crest")

d = N.neural_tube_domains(ax, (3.0, 4.6), 6.0)
for name in ("dP1", "dP6", "p0", "p2", "pMN", "p3"):
    bio.label(ax, (d["right"] + 0.5, d[name][1]), name, size="tiny", ha="left")
    ax.plot([d[name][0], d["right"] + 0.45], [d[name][1], d[name][1]], color=P.muted(), lw=0.5, zorder=19)
bio.callout(ax, d["floor"], (5.6, 1.2), "Floor plate")
bio.callout(ax, d["roof"], (5.6, 8.0), "Roof plate")

c = N.cortex_layers(ax, (8.0, 1.0), 3.6, 7.0, "late")
for name in ("VZ", "SVZ", "IZ", "CP", "MZ"):
    bio.label(ax, (11.8, c[name]), name, size="small", ha="left")

g = N.growth_cone(ax, (19.5, 5.0), angle=15, size=1.6, shaft=3.0)
bio.callout(ax, g["central"], (16.5, 7.5), "Central domain")
bio.callout(ax, g["peripheral"], (19.0, 2.2), "Peripheral domain")
bio.callout(ax, g["filopodia"][-1], (20.5, 7.8), "Filopodia")

e = N.optic_cup(ax, (24.0, 4.6), 1.0, "cup")
bio.callout(ax, e["retina"], (22.5, 7.2), "Neural retina")
bio.callout(ax, e["rpe"], (23.0, 2.0), "RPE")
bio.callout(ax, e["lens"], (25.6, 7.2), "Lens pit")
