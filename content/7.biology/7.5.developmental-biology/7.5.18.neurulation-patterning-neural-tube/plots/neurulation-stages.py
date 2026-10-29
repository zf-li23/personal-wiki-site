"""Primary neurulation in transverse section (amniote trunk, dorsal up). (A) The neural plate, a thickened
columnar epithelium, lies in the midline of the ectoderm above the notochord; its border with the epidermis is
the neural plate border, the future neural crest. (B) The plate bends at the median hinge point (wedge-shaped
cells anchored to the notochord) and the neural folds rise. (C) The folds bend again at the dorsolateral hinge
points and converge. (D) The folds fuse; the neural tube separates from the epidermis, which closes over it, and
neural crest cells delaminate from the dorsal tube and migrate. Somites form from the paraxial mesoderm."""
import wikibio as bio
from wikibio import neurodev as N

fig, ax = bio.canvas(27, 7.0)
ax.set_ylim(1.75, 8.75)
P = bio.P
y = 6.0
titles = ["Neural plate", "Neural folds rise", "Folds converge", "Neural tube closed"]
for k, st in enumerate(("plate", "fold", "converge", "tube")):
    x = 3.4 + k * 6.7
    a = N.neurulation_section(ax, (x, y), 6.2, st)
    bio.panel(ax, "ABCD"[k], (x - 3.2, 8.5))
    bio.label(ax, (x, 8.25), titles[k], bold=True)
    if k == 0:
        bio.callout(ax, a["neural"], (x + 0.6, 7.4), "Neural plate")
        bio.callout(ax, a["crest_r"], (x + 2.3, 7.4), "Plate border")
        bio.callout(ax, a["epidermis_l"], (x - 2.6, 7.4), "Epidermis")
        bio.callout(ax, a["notochord"], (x - 0.6, 3.4), "Notochord")
        bio.callout(ax, a["somite_r"], (x + 0.9, 3.0), "Paraxial mesoderm")
        bio.callout(ax, a["endoderm"], (x + 2.2, 2.2), "Endoderm")
        bio.callout(ax, a["lateral_l"], (x - 2.4, 2.2), "Lateral plate")
    if k == 1:
        bio.callout(ax, a["mhp"], (x + 1.0, 3.0), "Median hinge point")
        bio.callout(ax, a["crest_r"], (x + 2.1, 7.6), "Neural fold")
    if k == 2:
        bio.callout(ax, a["dlhp_r"], (x + 1.6, 3.0), "Dorsolateral hinge")
        bio.callout(ax, a["groove"], (x - 1.2, 7.6), "Neural groove")
    if k == 3:
        bio.callout(ax, a["lumen"], (x + 2.6, 7.4), "Neural tube")
        bio.callout(ax, a["crest_l"], (x - 2.6, 7.4), "Neural crest")
        bio.callout(ax, a["somite_r"], (x + 2.2, 3.4), "Somite")
        bio.callout(ax, a["notochord"], (x - 1.2, 2.3), "Notochord")
    if k:
        bio.arrow(ax, (x - 3.55, 6.5), (x - 3.15, 6.5), kind="process", head=0.16)
