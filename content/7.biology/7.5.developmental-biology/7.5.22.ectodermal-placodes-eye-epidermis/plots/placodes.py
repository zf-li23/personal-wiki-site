"""Origin of the cranial placodes (schematic dorsal view of the anterior neural plate, anterior up). (A) At the end
of gastrulation the border of the neural plate is subdivided: the neural crest (green) lies along the lateral
border (not at the anterior end), and the preplacodal region (pink), a horseshoe of ectoderm around the anterior neural plate marked by Six1
and Eya1, lies outside it, where BMP and Wnt are low and FGF is present. (B) The preplacodal region resolves into
individual placodes in a fixed order from anterior to posterior: adenohypophyseal, olfactory, lens,
trigeminal (ophthalmic and maxillomandibular), otic and epibranchial (geniculate, petrosal, nodose), and in fishes
and amphibians the lateral line placodes."""
import numpy as np
import wikibio as bio
from wikibio import neurodev as N

fig, ax = bio.canvas(21, 10.5)
P = bio.P
T = N.TISSUE


def plate(ax, cx):
    y = np.linspace(1.0, 9.0, 120)
    hw = 0.55 + 1.3 * np.exp(-((y - 7.6) / 1.4) ** 2)
    hw[y > 7.6] = 1.85 * np.sqrt(np.clip(1 - ((y[y > 7.6] - 7.6) / 1.45) ** 2, 0, 1)) + 0.0
    outline = np.vstack([np.c_[cx + hw, y], np.c_[cx - hw, y][::-1]])
    lat = y < 8.3                             # no crest at the anterior end (anterior neural ridge)
    crest = np.vstack([np.c_[cx + hw[lat] + 0.35, y[lat]], np.c_[cx + hw[lat][::-1], y[lat][::-1]]])
    crest_l = np.vstack([np.c_[cx - hw[lat] - 0.35, y[lat]], np.c_[cx - hw[lat][::-1], y[lat][::-1]]])
    crest = (crest, crest_l)
    ppr = np.vstack([np.c_[cx + hw + 1.05, y], np.c_[cx - hw - 1.05, y][::-1]])
    return outline, crest, ppr, y, hw


cx = 4.5
outline, crest, ppr, y, hw = plate(ax, cx)
bio.shape(ax, np.vstack([np.c_[cx + hw + 1.05, y], np.c_[cx - hw - 1.05, y][::-1]])[np.r_[0:120, 120:240]], T["epidermis"], lw=0.0, zorder=1)
sel = y > 4.6
bio.shape(ax, np.vstack([np.c_[cx + hw[sel] + 1.1, y[sel]], np.c_[cx - hw[sel] - 1.1, y[sel]][::-1]]), T["placode"], lw=0.8, zorder=2)
for cr in crest:
    bio.shape(ax, cr, T["crest"], lw=0.8, zorder=3)
bio.shape(ax, outline, T["neural"], lw=1.0, zorder=4)
bio.panel(ax, "A", (0.2, 10.4))
bio.callout(ax, (cx, 6.0), (cx + 3.5, 4.0), "neural plate")
bio.callout(ax, (cx + hw[60] + 0.18, y[60]), (cx + 3.5, 3.2), "neural crest")
bio.callout(ax, (cx - 2.6, 7.8), (0.5, 9.9), "preplacodal region")
bio.label(ax, (cx, 0.5), "BMP, Wnt low; FGF: placodes", size="tiny", color=P.muted())

bio.panel(ax, "B", (10.0, 10.4))
cx2 = 14.8
outline, crest, ppr, y, hw = plate(ax, cx2)
for cr in crest:
    bio.shape(ax, cr, T["crest"], lw=0.8, zorder=3)
bio.shape(ax, outline, T["neural"], lw=1.0, zorder=4)
plac = [("adenohypophyseal (anterior pituitary)", (cx2, 9.35), 0.45, 0.25),
        ("olfactory (olfactory epithelium)", (cx2 - 1.45, 9.0), 0.42, 0.3),
        ("lens", (cx2 - 2.25, 8.1), 0.38, 0.38),
        ("trigeminal (sensory neurons)", (cx2 - 2.45, 6.8), 0.35, 0.55),
        ("otic (inner ear)", (cx2 - 1.65, 5.2), 0.42, 0.42),
        ("epibranchial (visceral sensory neurons)", (cx2 - 1.75, 4.1), 0.3, 0.22)]
for k, (name, xy, rx, ry) in enumerate(plac):
    bio.shape(ax, bio.blob(xy, rx, ry, wobble=0.05, seed=k, k=8), T["placode"], lw=0.9, zorder=6)
    # mirror on the right
    bio.shape(ax, bio.blob((2 * cx2 - xy[0], xy[1]), rx, ry, wobble=0.05, seed=k + 10, k=8), T["placode"], lw=0.9, zorder=6)
    if k == 5:
        for dy in (-0.55, -1.05):
            bio.shape(ax, bio.blob((xy[0] + 0.1, xy[1] + dy), 0.26, 0.2, wobble=0.05, seed=k + 20, k=8), T["placode"], lw=0.9, zorder=6)
            bio.shape(ax, bio.blob((2 * cx2 - xy[0] - 0.1, xy[1] + dy), 0.26, 0.2, wobble=0.05, seed=k + 30, k=8), T["placode"], lw=0.9, zorder=6)
    bio.callout(ax, (2 * cx2 - xy[0] + rx * 0.7, xy[1]), (cx2 + 3.2, 9.9 - k * 1.25), name)
