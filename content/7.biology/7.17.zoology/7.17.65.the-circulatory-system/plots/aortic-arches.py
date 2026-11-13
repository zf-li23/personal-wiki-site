# Fate of the six aortic arches in six vertebrates (vertskel.aortic_arches; ventral view, anterior up,
# the animal's left on the viewer's right). Not to scale.
import wikibio as bio
import vertskel as vs

titles = ["A  Shark", "B  Teleost", "C  Frog", "D  Lizard", "E  Bird", "F  Mammal"]
fig, ax, boxes = vs.panels(6, 4.2, 7.2, titles=titles, ncols=6, legend_rows=2)
G = "gill"
specs = [
    dict(arches={1: "absent", 2: G, 3: G, 4: G, 5: G, 6: G}, carotid_duct=True, ductus=True),
    dict(arches={1: "absent", 2: "absent", 3: G, 4: G, 5: G, 6: G}, carotid_duct=True, ductus=True),
    dict(arches={1: "absent", 2: "absent", 5: "absent"}, carotid_duct="absent", ductus="absent", pulmonary=True),
    dict(arches={1: "absent", 2: "absent", 5: "absent"}, carotid_duct=True, ductus="absent", pulmonary=True),
    dict(arches={1: "absent", 2: "absent", 5: "absent", 4: ("absent", "present")}, carotid_duct="absent",
         ductus="ligament", roots=("absent", "present"), pulmonary=True),
    dict(arches={1: "absent", 2: "absent", 5: "absent", 4: ("present", "reduced")}, carotid_duct="absent",
         ductus=("ligament", "absent"), roots=("present", "absent"), pulmonary=True,
         labels={(4, "L"): "aortic arch", (6, "L"): "lig. arteriosum"}),
]
for (x, y, w, h), sp in zip(boxes, specs):
    vs.aortic_arches(ax, (x + 0.2, y), w - 0.4, h, **sp)
vs.legend(ax, [("aortic_1", "I"), ("aortic_2", "II"), ("aortic_3", "III carotid"), ("aortic_4", "IV systemic"),
               ("aortic_5", "V"), ("aortic_6", "VI pulmonary, ductus arteriosus"), ("dorsal_aorta", "dorsal aorta"),
               ("ventral_aorta", "ventral aorta")], at=(0.6, 1.3), width=26, ncols=4)
