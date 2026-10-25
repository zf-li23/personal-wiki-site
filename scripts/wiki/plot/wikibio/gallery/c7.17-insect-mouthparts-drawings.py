# Insect mouthparts in frontal view, drawn from templates (a parametric lateral version is
# c7.17-insect-mouthparts). The same four appendages, coloured by homology as in the parametric figures,
# are remodelled for different diets: labrum (upper lip), paired mandibles, paired maxillae and the
# labium (lower lip, formed by fused second maxillae). Chewing (grasshopper): head above, the parts
# separated below. Chewing-lapping (honey bee): mandibles kept for handling wax and pollen, the maxillae and
# labium elongated into a tongue for nectar. Siphoning (butterfly): the two maxillary galeae interlock as a
# coiled proboscis; mandibles are lost. Piercing-sucking (mosquito female): mandibles and maxillae are fine
# stylets that pierce skin, sheathed by the grooved labium, which does not enter the wound.
import wikibio as bio
from wikibio import animalmorph as AM

P = bio.P
fig, ax = bio.canvas(25, 11.6)
items = [dict(icon="wikimedia/mouthparts-grasshopper", title="Chewing", subtitle="grasshopper"),
         dict(icon="wikimedia/mouthparts-bee", title="Chewing-lapping", subtitle="honey bee"),
         dict(icon="wikimedia/mouthparts-butterfly", title="Siphoning", subtitle="butterfly"),
         dict(icon="wikimedia/mouthparts-mosquito", title="Piercing-sucking", subtitle="mosquito")]
xs = [3.4, 9.6, 15.2, 21.2]
row = AM.homology_row(ax, items, AM.MOUTHPARTS, y=2.0, height=8.4, x=xs, mute="neutral", keep=["outline"])

g = row[0]
AM.callouts(ax, [(g.point(p, where=w), t, "left") for p, t, w in (("labrum", "Labrum", "left"), ("mandible", "Mandible", "left"),
                                                                 ("maxilla", "Maxilla", "left"), ("labium", "Labium", "left"))],
            left=0.9, gap=0.7)
b = row[2]
AM.callouts(ax, [(b.point("maxilla"), "Proboscis\n(maxillary galeae)", "right")], right=17.4)
m = row[3]
AM.callouts(ax, [(m.point("labium", where="bottom"), "Labium\n(sheath)", "right"), (m.point("maxilla"), "Stylets", "right")],
            right=23.8, gap=1.0)
AM.part_legend(ax, (6.2, 0.45), AM.MOUTHPARTS, names={"labrum": "Labrum", "mandible": "Mandible", "maxilla": "Maxilla",
                                                     "labium": "Labium"})
