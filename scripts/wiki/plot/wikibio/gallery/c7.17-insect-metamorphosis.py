# Incomplete and complete metamorphosis. A: hemimetabolous development of a grasshopper (Orthoptera;
# drawings after Snodgrass, to relative scale): the egg hatches into a nymph that already resembles the
# adult (compound eyes, the same mouthparts and legs), and grows through five nymphal instars, one moult
# apart; the wings develop outside the body as wing pads that enlarge at each moult and become functional
# only after the final, imaginal moult. B: holometabolous development of a fruit fly (Drosophila, Diptera;
# not to scale): the larva (three instars) differs completely from the adult in form, food and habitat;
# adult structures grow internally from imaginal discs, and the body is rebuilt during the non-feeding
# pupal stage. Holometaboly evolved once, in the common ancestor of the Holometabola.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26, 10.9)

bio.panel(ax, "A", (0.3, 10.7))
bio.label(ax, (0.9, 10.55), "Incomplete metamorphosis (hemimetaboly)", size="title", bold=True, ha="left", va="top")
YA = 7.0
k = 1.12
widths = [0.7 * k, 1.05 * k, 1.8 * k, 2.5 * k, 3.2 * k, 4.0 * k]
names = ["1st instar", "2nd instar", "3rd instar", "4th instar", "5th instar", "Adult"]
x = 1.0
boxes = []
for k2, w in enumerate(widths):
    icon_id = ["wikimedia/grasshopper-instar-1", "wikimedia/grasshopper-instar-2", "wikimedia/grasshopper-instar-3",
               "wikimedia/grasshopper-instar-4", "wikimedia/grasshopper-instar-5", "wikimedia/grasshopper-adult"][k2]
    b = bio.icon(ax, icon_id, at=(x, YA), width=w, anchor="left")
    boxes.append(b)
    bio.label(ax, (x + w / 2, YA - 1.55), names[k2], size="small", bold=k2 == 5)
    if k2 < 5:
        bio.arrow(ax, (x + w + 0.15, YA), (x + w + 0.95, YA), kind="process", color=P.muted(), lw=1.1, head=0.18)
        bio.label(ax, (x + w + 0.55, YA + 0.3), "moult", size="tiny", color=P.muted())
    x += w + 1.1
bio.label(ax, (boxes[0][0] + 0.4, YA + 1.75), "Nymphs: adult body plan, no wings", size="small", color=P.muted(), ha="left")
b5 = boxes[4]
bio.callout(ax, (b5[0] + b5[2] * 0.45, b5[1] + b5[3] * 0.64), (b5[0] + b5[2] * 0.2, YA + 2.0), "Wing pads", size="small")
b6 = boxes[5]
bio.callout(ax, (b6[0] + b6[2] * 0.62, b6[1] + b6[3] * 0.6), (b6[0] + b6[2] * 0.5, YA + 2.3), "Functional wings", size="small")

bio.panel(ax, "B", (0.3, 5.0))
bio.label(ax, (0.9, 4.85), "Complete metamorphosis (holometaboly)", size="title", bold=True, ha="left", va="top")
YB = 2.0
stages = ["Egg", "Larva (3 instars)", "Pupa", "Adult"]
xs = [2.4, 8.4, 14.6, 20.6]
bio.icon(ax, "dbcls/drosophila-egg", at=(xs[0], YB), height=1.1)
bio.icon(ax, "dbcls/drosophila-larva", at=(xs[1], YB), width=3.4)
bio.icon(ax, "dbcls/drosophila-pupa", at=(xs[2], YB), height=2.0)
bio.icon(ax, "phylopic/drosophila", at=(xs[3], YB), width=2.8, color="animal")
for name, xx in zip(stages, xs):
    bio.label(ax, (xx, YB - 1.55), name, size="small", bold=name == "Adult")
for a, b, t in ((xs[0], xs[1], "hatching"), (xs[1], xs[2], "pupation"), (xs[2], xs[3], "eclosion")):
    bio.arrow(ax, (a + (2.1 if a == xs[1] else 1.0), YB), (b - (2.1 if b == xs[1] else 1.6), YB), kind="process", color=P.muted(), lw=1.1, head=0.18)
    bio.label(ax, ((a + b) / 2, YB + 0.3), t, size="tiny", color=P.muted())
bio.label(ax, (xs[1], YB + 1.45), "imaginal discs grow inside", size="tiny", color=P.muted())
bio.label(ax, (xs[2], YB + 1.45), "non-feeding; tissues rebuilt", size="tiny", color=P.muted())
