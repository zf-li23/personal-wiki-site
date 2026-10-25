# Homology of the vertebrate forelimb, drawn from a template (Commons, CC0; a parametric version with six
# taxa is c7.10-forelimb-homology). The forelimbs of a human (grasping hand), a dog (running), a bird
# (flight) and a whale (swimming flipper) serve different functions yet are built from the same series of
# bones in the same order from the shoulder outwards: one upper-arm bone (humerus), two forearm bones
# (radius and ulna), a group of wrist bones (carpals) and the bones of the hand and digits (metacarpals and
# phalanges). Homologous bones share a colour. In the bird the carpals and metacarpals are reduced and
# partly fused (carpometacarpus) and only three digits remain; in the whale the phalanges are multiplied
# (hyperphalangy) inside the flipper. The shared pattern reflects descent from a common tetrapod ancestor,
# not similar function: homology, as opposed to the analogy of, say, bird and insect wings.
import wikibio as bio
from wikibio import animalmorph as AM

P = bio.P
fig, ax = bio.canvas(22, 11.2)

items = [dict(icon="wikimedia/forelimb-human", title="Human", subtitle="grasping"),
         dict(icon="wikimedia/forelimb-dog", title="Dog", subtitle="running"),
         dict(icon="wikimedia/forelimb-bird", title="Bird", subtitle="flying"),
         dict(icon="wikimedia/forelimb-whale", title="Whale", subtitle="swimming")]
xs = [5.6, 10.0, 14.0, 18.6]
row = AM.homology_row(ax, items, AM.FORELIMB, y=2.2, height=8.6, x=xs, anchor="bottom")

names = {"humerus": "Humerus", "radius": "Radius", "ulna": "Ulna", "carpals": "Carpals",
         "metacarpals-phalanges": "Metacarpals and phalanges"}
hum = row[0]
AM.callouts(ax, [(hum.point(p), names[p], "left") for p in ("humerus", "radius", "carpals")]
            + [(hum.point("ulna", where="top"), "Ulna", "left")]
            + [(hum.point("metacarpals-phalanges", where="bottom"), "Metacarpals\nand phalanges", "left")],
            left=3.0, gap=0.9)
whale = row[3]
AM.callouts(ax, [(whale.point("metacarpals-phalanges"), "Extra phalanges\n(hyperphalangy)", "right")], right=21.2)
bird = row[2]
AM.callouts(ax, [(bird.point("metacarpals-phalanges"), "Fused carpometacarpus,\nthree digits", "right")], right=15.7)

AM.part_legend(ax, (3.0, 0.45), AM.FORELIMB, names=names, step=None)
