# Vertebrate hearts compared. Top: schematics in ventral view (the animal's right on the viewer's left),
# chambers coloured by the blood they carry: deoxygenated (blue), oxygenated (red), mixed (purple).
# Fishes: a single circuit; the heart (sinus venosus, atrium, ventricle, bulbus arteriosus in series) pumps
# only deoxygenated blood to the gills. Amphibians: double circulation with two atria but one ventricle,
# in which streams partly mix (a spiral valve in the conus arteriosus helps keep them apart); the skin also
# exchanges gases. Non-crocodilian reptiles: an incomplete ventricular septum separates the streams
# functionally and allows shunting during diving. Crocodilians: four chambers, but the left aorta leaves the
# right ventricle and the two aortae communicate through the foramen of Panizza. Birds and mammals:
# four chambers with a complete septum, separating the pulmonary and systemic circuits entirely; the
# systemic arch turns right in birds and left in mammals, so full separation evolved twice. Bottom:
# drawings of a fish, an amphibian and a mammalian heart.
import wikibio as bio
from wikibio import animalmorph as AM

P = bio.P
fig, ax = bio.canvas(28.8, 15.0)
KINDS = [("fish", "Fish", "SV → A → V → B → gills\nsingle circulation"),
         ("amphibian", "Amphibian", "3 chambers\nventricle undivided"),
         ("reptile", "Lizard, snake, turtle", "3 chambers\nincomplete septum"),
         ("crocodilian", "Crocodilian", "4 chambers\nforamen of Panizza"),
         ("bird", "Bird", "4 chambers\nright aortic arch"),
         ("mammal", "Mammal", "4 chambers\nleft aortic arch")]
YH = 11.0
for k, (kind, name, note) in enumerate(KINDS):
    x = 2.4 + k * 4.45
    a = AM.heart(ax, (x, YH), 2.6, kind)
    bio.label(ax, (x, 14.6), name, size="normal", bold=True)
    bio.label(ax, (x, 8.75), note, size="tiny", color=P.muted(), va="top")
    if "panizza" in a:
        bio.callout(ax, a["panizza"], (x + 1.3, YH + 1.9), "Foramen", size="tiny")
    if "septum" in a and kind == "reptile":
        bio.callout(ax, a["septum"], (x + 1.5, YH - 1.6), "Partial\nseptum", size="tiny")
    if "conus" in a:
        bio.callout(ax, a["conus"], (x + 1.3, YH + 1.9), "Conus", size="tiny")
    if kind in ("bird", "mammal"):
        bio.callout(ax, a["aorta"], (x + (1.5 if kind == "mammal" else -1.5), YH + 2.1), "Aorta", size="tiny")
AM.part_legend(ax, (18.6, 7.45), {"deoxy": AM.BLOOD["deoxy"], "oxy": AM.BLOOD["oxy"], "mixed": AM.BLOOD["mixed"]},
               names={"deoxy": "Deoxygenated", "oxy": "Oxygenated", "mixed": "Mixed"})
bio.label(ax, (1.0, 7.45), "SV: sinus venosus; A: atrium; B: bulbus arteriosus; RA, LA: right and left atrium; V: ventricle; RV, LV: right and left ventricle", size="tiny",
          color=P.muted(), ha="left")

# drawings
f = AM.Specimen("wikimedia/heart-fish", at=(4.4, 4.0), width=7.4)
f.draw(ax)
fp = f.point("myocardium")
bio.callout(ax, fp, (fp[0] + 1.2, 1.6), "Ventricle (spongy myocardium)")
bio.label(ax, (4.4, 6.3), "Fish heart (blood flows right to left)", size="small", bold=True)
am = AM.Specimen("wikimedia/heart-amphibian", at=(13.2, 3.4), height=5.6)
am.draw(ax)
AM.callouts(ax, [(am.point("right-atrium"), "Right atrium", "left"), (am.point("ventricle"), "Ventricle", "left")], left=11.0,
            gap=0.6)
AM.callouts(ax, [(am.point("left-atrium"), "Left atrium", "right"), (am.point("conus-arteriosus"), "Conus arteriosus", "right")],
            right=15.5, gap=0.6)
mm = AM.Specimen("wikimedia/heart-mammal", at=(23.3, 3.4), height=5.9)
mm.draw(ax)
AM.callouts(ax, [(mm.point("vena-cava"), "Venae cavae", "left"), (mm.point("right-chambers"), "Right atrium\nand ventricle", "left")],
            left=20.2, gap=0.9)
AM.callouts(ax, [(mm.point("aorta", where="top"), "Aorta", "right"), (mm.point("pulmonary-artery"), "Pulmonary artery", "right"),
                 (mm.point("left-chambers"), "Left ventricle", "right")], right=26.2, gap=0.7)
