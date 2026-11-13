# Number of cervical vertebrae in representative mammals, birds and other reptiles (log axis). Typical counts
# from the literature: mammals (Narita & Kuratani 2005; Galis 1999): mouse, human, bat, giraffe, dolphin, horse 7,
# manatee 6, two-toed sloth Choloepus 6 (5-7), three-toed sloth Bradypus 9 (8-10); birds (Bohmer et al. 2019 and
# standard anatomies): pigeon 12, sparrow 13, chicken 14, barn owl 14, flamingo 17, ostrich 18, mute swan 24;
# reptiles: turtles 8, lizards 8, crocodylians 9, Tanystropheus 13, Mamenchisaurus 19, Elasmosaurus 72.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(22, 8)
data = {
    "Mammals": [(7, "most mammals"), (6, "manatee, two-toed sloth"), (9, "three-toed sloth")],
    "Birds": [(12, "pigeon"), (13, "sparrow"), (14, "chicken, owl"), (17, "flamingo"), (18, "ostrich"), (24, "mute swan")],
    "Other reptiles": [(8, "turtles, lizards"), (9, "crocodylians"), (13, "Tanystropheus"), (19, "Mamenchisaurus"), (72, "Elasmosaurus")],
}
toks = {"Mammals": "dna", "Birds": "mrna", "Other reptiles": "positive"}
p = quant.Plot(ax, (4.5, 1.4, 16.5, 6.0), xlim=(4, 100), ylim=(0, 3), xlog=True,
               xlabel="number of cervical vertebrae (log scale)", xticks=[5, 7, 10, 20, 50, 100], yticks=[])
p.vline(7, text="7", top=True)
for i, (grp, pts) in enumerate(data.items()):
    y = 2.5 - i
    p.text(3.6, y, grp, ha="right")
    for k, (n, name) in enumerate(pts):
        p.points([n], [y], toks[grp], r=0.12)
        off = [0.25, -0.28, 0.5][k % 3] if grp == "Birds" else (0.25 if k % 2 == 0 else -0.28)
        p.text(n, y + off, name, ha="center", italic=name[0].isupper() and " " not in name)
