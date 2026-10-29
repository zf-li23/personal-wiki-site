"""Development of the vertebrate eye (schematic sections; brain to the left, surface ectoderm to the right).
(A) The optic vesicle grows out from the diencephalon and contacts the surface ectoderm, which thickens into the
lens placode. (B) The vesicle folds into the two-layered optic cup, whose inner layer becomes the neural retina and
outer layer the retinal pigment epithelium (RPE), while the placode invaginates as the lens pit. (C) The lens vesicle
pinches off and the surface ectoderm closes over it; it will form the corneal epithelium. (D) Cells of the posterior
lens vesicle elongate into lens fibres and fill it, the retina thickens and becomes layered, ganglion cell axons
leave through the optic stalk (optic nerve), and neural crest mesenchyme forms the corneal stroma."""
import wikibio as bio
from wikibio import neurodev as N

fig, ax = bio.canvas(26, 7.6)
P = bio.P
titles = ["Optic vesicle", "Optic cup, lens pit", "Lens vesicle", "Later eye"]
for k, st in enumerate(("vesicle", "cup", "lens-vesicle", "eye")):
    cx = 4.4 + k * 6.4
    a = N.optic_cup(ax, (cx, 3.5), 1.25, st)
    bio.panel(ax, "ABCD"[k], (cx - 4.2, 7.4))
    bio.label(ax, (cx - 0.6, 7.2), titles[k], bold=True)
    if k == 0:
        bio.callout(ax, a["placode"], (cx + 1.5, 0.6), "lens placode")
        bio.callout(ax, a["stalk"], (cx - 1.6, 0.6), "optic stalk")
        bio.callout(ax, a["brain"], (cx - 3.0, 6.3), "diencephalon")
    if k == 1:
        bio.callout(ax, a["retina"], (cx - 1.8, 6.3), "neural retina")
        bio.callout(ax, a["rpe"], (cx - 1.2, 0.6), "RPE")
        bio.callout(ax, a["lens"], (cx + 1.9, 6.3), "lens pit")
    if k == 2:
        bio.callout(ax, a["lens"], (cx + 1.9, 0.6), "lens vesicle")
        bio.callout(ax, a["cornea"], (cx + 1.9, 6.3), "surface ectoderm")
    if k == 3:
        bio.callout(ax, a["lens"], (cx + 1.0, 0.6), "lens fibres")
        bio.callout(ax, a["cornea"], (cx + 1.9, 6.3), "cornea")
        bio.callout(ax, a["stalk"], (cx - 1.2, 0.6), "optic nerve")
