# Types of insect wings by texture, drawn by one rule set (wikibio.zoomorph.wing), with the fills used
# throughout: membranous (wasps, flies); tegmen, a leathery forewing that still shows veins (grasshoppers,
# cockroaches); elytron, a hardened forewing without functional venation that covers the folded hind
# wing (beetles); hemelytron, a forewing with a thickened basal corium and clavus and a membranous apex
# (true bugs); scaled wings (butterflies and moths); and the haltere, the hind wing reduced to a club
# that acts as a gyroscopic sense organ (true flies). Hymenoptera couple fore and hind wings by a row of
# hooks (hamuli) on the hind wing's costal margin.
import wikibio as bio
from wikibio import zoomorph as zm

P = bio.P
fig, ax = bio.canvas(26, 12.6)
cells = [("Membranous", "Hymenoptera, Diptera"), ("Tegmen", "Orthoptera, Blattodea"), ("Elytron", "Coleoptera"),
         ("Hemelytron", "Heteroptera"), ("Scaled", "Lepidoptera"), ("Haltere", "Diptera (hind wing)")]
CW, CH = 8.6, 6.2
for i, (t, ex) in enumerate(cells):
    c, r = i % 3, i // 3
    x0, y0 = c * CW, 12.6 - (r + 1) * CH
    bio.label(ax, (x0 + 0.4, y0 + CH - 0.4), t, size="normal", bold=True, ha="left")
    bio.label(ax, (x0 + 0.4, y0 + CH - 0.95), ex, size="tiny", ha="left", color=P.muted())
    base = (x0 + 0.9, y0 + 3.0)
    if i == 0:
        a = zm.wing(ax, (x0 + 0.9, y0 + 3.6), 6.2, "hymenoptera_fore", angle=0)
        b = zm.wing(ax, (x0 + 1.1, y0 + 2.3), 4.3, "hymenoptera_hind", angle=-6)
        if "hamuli" in b:
            bio.callout(ax, b["hamuli"], (x0 + 6.5, y0 + 1.0), "Hamuli", size="tiny")
        bio.callout(ax, a["pterostigma"], (x0 + 6.0, y0 + 4.8), "Pterostigma", size="tiny") if "pterostigma" in a else None
    elif i == 1:
        zm.wing(ax, base, 6.8, "orthoptera_fore", angle=0)
    elif i == 2:
        zm.wing(ax, (x0 + 1.0, y0 + 2.2), 5.8, "elytron", angle=0)
    elif i == 3:
        a = zm.wing(ax, base, 6.4, "hemelytron", angle=0)
        bio.callout(ax, a["corium"], (x0 + 2.5, y0 + 0.8), "Corium", size="tiny")
        bio.callout(ax, a["clavus"], (x0 + 1.0, y0 + 1.2), "Clavus", size="tiny")
        bio.callout(ax, a["membrane"], (x0 + 6.5, y0 + 1.3), "Membrane", size="tiny")
    elif i == 4:
        zm.wing(ax, (x0 + 0.9, y0 + 4.0), 6.0, "lepidoptera_fore", angle=-8)
    else:
        a = zm.haltere(ax, (x0 + 3.0, y0 + 4.2), 2.6, angle=-60)
        bio.callout(ax, a["haltere"], (x0 + 5.8, y0 + 2.0), "Knob (capitellum)", size="tiny")
for c in (1, 2):
    ax.plot([c * CW, c * CW], [0.2, 12.4], color=P.muted(), lw=0.4, alpha=0.5)
ax.plot([0.2, 25.8], [CH, CH], color=P.muted(), lw=0.4, alpha=0.5)
