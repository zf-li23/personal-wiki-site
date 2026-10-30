"""The primitive gut tube and its organ buds (lateral view, anterior left, dorsal up; about the fifth week of
human development), with the anterior-posterior regionalization of the endoderm below. The pharynx bears the
pharyngeal pouches and the thyroid diverticulum; the lung bud grows from the ventral foregut; the stomach is a
dilation of the foregut; the hepatic diverticulum (with the gallbladder) and the ventral pancreatic bud arise
ventrally and the dorsal pancreatic bud dorsally near the foregut-midgut junction; the midgut is connected to the
yolk sac by the yolk stalk, and the allantois leaves the hindgut ventrally near the cloaca. Below: transcription
factors that divide the endoderm (Sox2 in the foregut, Nkx2-1 in lung and thyroid, Hhex in liver, Pdx1 in the
posterior foregut, Cdx2 in midgut and hindgut), set by graded Wnt, FGF and BMP signalling, high posteriorly, and
by retinoic acid."""
import numpy as np
import wikibio as bio
from wikibio import organogenesis as O

P = bio.P
fig, ax = bio.canvas(24, 12)
g = O.gut_tube(ax, (1.0, 8.0), 21.0, h=0.6)
for key, txt, xy in (("pharynx", "Pharynx", (1.0, 11.4)), ("pouch2", "Pharyngeal pouches", (4.6, 11.6)), ("thyroid", "Thyroid", (0.6, 5.0)),
                     ("lung", "Lung bud", (3.2, 4.0)), ("esophagus", "Esophagus", (6.4, 10.2)), ("stomach", "Stomach", (9.0, 10.6)),
                     ("liver", "Liver", (7.2, 3.6)), ("gallbladder", "Gallbladder", (10.4, 4.3)), ("ventral_pancreas", "Ventral pancreas", (12.6, 5.6)),
                     ("dorsal_pancreas", "Dorsal pancreas", (12.8, 10.8)), ("midgut", "Midgut", (16.0, 9.4)), ("yolk_stalk", "Yolk stalk", (16.6, 3.6)),
                     ("hindgut", "Hindgut", (20.0, 9.8)), ("allantois", "Allantois", (22.4, 5.4)), ("cloaca", "Cloaca", (23.4, 8.6))):
    bio.callout(ax, g[key], xy, txt)
x = g["x"]
y0 = 1.8
for f0, f1, tk, txt in ((0.0, 0.42, "lipid_head", "Sox2"), (0.36, 0.52, "k", "Pdx1"), (0.48, 1.0, "enzyme", "Cdx2")):
    row = 1 if txt == "Pdx1" else 0
    yy = y0 + 0.75 * row
    bio.shape(ax, [(x(f0), yy - 0.28), (x(f1), yy - 0.28), (x(f1), yy + 0.28), (x(f0), yy + 0.28)], tk, lw=0.7, zorder=6)
    bio.label(ax, ((x(f0) + x(f1)) / 2, yy), txt, size="tiny", italic=True, color=P.on_fill())
for f, tk, txt in ((0.12, "dna2", "Nkx2-1"), (0.45, "drug", "Hhex")):
    bio.box(ax, (x(f), y0 + 1.5), 1.6, 0.5, tk, txt, size="tiny", italic=True)
xs = np.linspace(x(0), x(1), 60)
for k in range(len(xs) - 1):
    t = k / (len(xs) - 2)
    col = P.mix(P.surface(), P.fill("protein"), 0.15 + 0.8 * t)
    ax.add_patch(bio.core.FancyBboxPatch((xs[k], 0.55), xs[k + 1] - xs[k], 0.4, boxstyle="square,pad=0", facecolor=col, edgecolor="none", zorder=5))
bio.label(ax, (x(0.0), 0.25), "low Wnt, FGF, BMP", size="tiny", ha="left", color=P.muted())
bio.label(ax, (x(1.0), 0.25), "high Wnt, FGF, BMP", size="tiny", ha="right", color=P.muted())
bio.label(ax, (x(0.5), 7.2 + 4.3), "dorsal", size="tiny", color=P.muted())
