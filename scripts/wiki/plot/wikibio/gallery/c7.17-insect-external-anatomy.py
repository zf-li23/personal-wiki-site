# External anatomy of an insect. Top: a grasshopper (Orthoptera) in lateral view, its three tagmata
# coloured: the head (antennae, compound eyes, mouthparts), the thorax (prothorax with the saddle-shaped
# pronotum; meso- and metathorax bearing the two pairs of wings, here the leathery forewing or tegmen
# covering the membranous hindwing; one pair of legs on each thoracic segment) and the abdomen (eleven
# segments, with spiracles opening into the tracheal system). The jumping hind leg is coloured by segment.
# Right: the segments of a walking leg, from the body outwards: coxa, trochanter, femur, tibia, tarsus
# (here four tarsomeres) and the pretarsus with its claws. Bottom: a worker ant (Hymenoptera, Formicidae)
# shows how tagmata can be regrouped: the first abdominal segment (propodeum) is fused to the thorax,
# forming the mesosoma, and the narrow petiole is followed by the swollen gaster.
import wikibio as bio
from wikibio import animalmorph as AM

P = bio.P
fig, ax = bio.canvas(27, 14.9)

HEAD, THORAX, ABDOMEN = AM.TAGMA["head"], AM.TAGMA["thorax"], AM.TAGMA["abdomen"]
g = AM.Specimen("wikimedia/grasshopper", at=(9.4, 9.6), width=14.5)
g.draw(ax, parts={"head": HEAD, "mouthparts": HEAD, "compound-eye": "dna", "antenna": HEAD,
                  "pronotum": THORAX, "pterothorax": THORAX, "forewing": "tegmen", "foreleg": THORAX, "midleg": THORAX,
                  "hind-femur": "femur", "hind-tibia": "tibia", "hind-tarsus": "tarsus",
                  "abdomen": ABDOMEN, "spiracle": "neutral"}, mute="neutral")

# tagma brackets above the body
yb = 13.25
head_l, head_r = g.point("antenna", where="right")[0] - 0.05, g.point("pronotum", where="left")[0]
th_r = g.point("pterothorax", where="right")[0]
ab_r = g.point("abdomen", where="right")[0]
AM.bracket(ax, (head_l - 0.9, yb), (head_r, yb), "Head", token=HEAD, depth=0.26, bold=True)
AM.bracket(ax, (head_r + 0.05, yb), (th_r, yb), "Thorax", token=THORAX, depth=0.26, bold=True)
AM.bracket(ax, (th_r + 0.05, yb), (ab_r, yb), "Abdomen", token=ABDOMEN, depth=0.26, bold=True)

AM.callouts(ax, [
    (g.point("antenna", where="left"), "Antenna", "left"),
    (g.point("compound-eye"), "Compound eye", "left"),
    (g.point("mouthparts"), "Mouthparts", "left"),
    (g.point("foreleg", where="bottom"), "Foreleg", "left"),
], left=1.6, gap=0.55)
AM.callouts(ax, [
    (g.point("forewing"), "Forewing (tegmen)", "right"),
    (g.point("spiracle"), "Spiracle", "right"),
    (g.point("hind-femur"), "Femur", "right"),
    (g.point("hind-tibia", where="right"), "Tibia", "right"),
    (g.point("hind-tarsus"), "Tarsus", "right"),
], right=17.4, gap=0.55, top=12.1)
pn = g.point("pronotum")
bio.callout(ax, pn, (pn[0] - 1.3, pn[1] + 1.9), "Pronotum")
bio.label(ax, (g.point("midleg", where="bottom")[0], g.point("midleg", where="bottom")[1] - 0.35), "Midleg", size="small",
          va="top")

# leg segments
bio.panel(ax, "B", (19.6, 14.5))
leg = AM.Specimen("wikimedia/insect-leg", at=(22.4, 7.2), height=8.6)
leg.draw(ax, parts=AM.LEG, mute="neutral")
AM.callouts(ax, [(leg.point(p), t, "right") for p, t in (("coxa", "Coxa"), ("trochanter", "Trochanter"), ("femur", "Femur"),
                                                         ("tibia", "Tibia"), ("tarsus", "Tarsus (tarsomeres)"),
                                                         ("pretarsus", "Pretarsus (claws)"))], right=24.6, gap=0.6)
bio.label(ax, (22.6, 14.0), "Walking leg", size="normal", bold=True)

# ant: tagmata regrouped
bio.panel(ax, "C", (0.3, 5.3))
bio.panel(ax, "A", (0.3, 14.5))
ant = AM.Specimen("wikimedia/ant-worker", at=(5.6, 2.55), width=5.8)
ant.draw(ax, parts={"head": HEAD, "antenna": HEAD, "mandible": HEAD, "compound-eye": "dna", "mesosoma": THORAX,
                    "petiole": "drug", "gaster": ABDOMEN, "sting": ABDOMEN}, mute="neutral")
AM.callouts(ax, [(ant.point("head"), "Head", "left")], left=1.9)
AM.callouts(ax, [(ant.point("mesosoma", where="top"), "Mesosoma (thorax + propodeum)", "right"),
                 (ant.point("petiole", where="top"), "Petiole", "right"), (ant.point("gaster"), "Gaster", "right")],
            right=9.4, gap=0.55, top=4.7)
bio.label(ax, (5.4, 5.2), "Worker ant", size="normal", bold=True)
