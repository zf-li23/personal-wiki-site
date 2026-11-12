# The serial (gill-arch) hypothesis of jaw origin, schematic lateral views of the head skeleton with
# anterior to the left. Homologous elements share the vertskel colours: mandibular arch gold and coral,
# hyoid arch magenta, branchial arches 3-7 blue to violet. Not to scale.
import wikibio as bio
import vertskel as vs

P = bio.P
fig, ax, boxes = vs.panels(3, 9.0, 6.0, titles=["A  Hypothetical jawless ancestor",
                                                 "B  Early gnathostome (amphistylic)",
                                                 "C  Modern shark (hyostylic)"], ncols=3, legend_rows=2)
BR = ["arch_3", "arch_4", "arch_5", "arch_6", "arch_7"]


def arch(parts, x, top, mid, bot, key_up, key_lo, lean=0.5, w=0.32, state="bone"):
    """A gill arch as a forward-pointing chevron: dorsal (epibranchial) and ventral (ceratobranchial) rods."""
    parts.append((key_up, vs.rod((x + lean, top), (x, mid), w), {"state": state}))
    parts.append((key_lo, vs.rod((x, mid), (x + lean, bot), w), {"state": state}))


cranium = vs.smooth([(0.6, 4.7), (2.5, 5.4), (5.5, 5.5), (8.4, 5.1), (8.6, 4.5), (5.5, 4.4), (2.0, 4.2)])

# A: seven similar arches
x, y, w, h = boxes[0]
parts = [("chondrocranium", cranium, {"state": "cartilage"})]
arch(parts, 1.3, 4.2, 2.6, 1.0, "palatoquadrate", "meckel")
arch(parts, 2.3, 4.2, 2.6, 1.0, "hyomandibula", "ceratohyal")
for k, key in enumerate(BR):
    arch(parts, 3.3 + 1.0 * k, 4.2, 2.6, 1.0, key, key)
a = vs.draw(ax, parts, at=(x, y))
vs.callout(ax, a["palatoquadrate"], (x + 0.6, y + 3.6), "arch 1")
vs.callout(ax, a["hyomandibula"], (x + 2.6, y + 3.9), "arch 2")

# B: early gnathostome, palatoquadrate braced against the cranium and the hyomandibula
x, y, w, h = boxes[1]
parts = [("chondrocranium", cranium, {"state": "cartilage"}),
         ("palatoquadrate", vs.smooth([(0.5, 3.6), (1.5, 4.1), (3.2, 3.9), (3.4, 3.2), (1.6, 3.2), (0.6, 3.2)])),
         ("meckel", vs.smooth([(0.5, 3.05), (1.8, 2.8), (3.3, 2.9), (3.4, 2.3), (1.6, 2.4), (0.5, 2.75)])),
         ("hyomandibula", vs.rod((3.8, 4.35), (3.4, 3.0), 0.36)),
         ("ceratohyal", vs.rod((3.4, 2.9), (3.9, 1.4), 0.34))]
for k, key in enumerate(BR):
    arch(parts, 4.6 + 0.85 * k, 4.2, 2.5, 1.1, key, key, lean=0.4)
a = vs.draw(ax, parts, at=(x, y))
vs.callout(ax, a["palatoquadrate"], (x + 1.4, y + 5.0), "palatoquadrate")
vs.callout(ax, a["meckel"], (x + 0.8, y + 1.2), "meckel")
vs.callout(ax, a["hyomandibula"], (x + 3.9, y + 5.0), "hyomandibula")
bio.label(ax, (x + 6.3, y + 0.5), "gill arches 3-7", size="tiny", color=P.muted())

# C: shark, jaws slung from the hyomandibula only; spiracle between arches 1 and 2
x, y, w, h = boxes[2]
parts = [("chondrocranium", cranium, {"state": "cartilage"}),
         ("palatoquadrate", vs.smooth([(0.9, 3.3), (2.2, 3.8), (3.9, 3.6), (4.1, 2.9), (2.0, 2.9), (1.0, 2.9)]),
          {"state": "cartilage"}),
         ("meckel", vs.smooth([(1.0, 2.75), (2.4, 2.4), (4.0, 2.55), (4.1, 2.0), (2.2, 2.0), (1.0, 2.45)]),
          {"state": "cartilage"}),
         ("hyomandibula", vs.rod((4.9, 4.3), (4.1, 2.6), 0.42), {"state": "cartilage"}),
         ("ceratohyal", vs.rod((4.1, 2.5), (4.6, 1.2), 0.36), {"state": "cartilage"})]
for k, key in enumerate(BR):
    arch(parts, 5.4 + 0.75 * k, 4.2, 2.5, 1.1, key, key, lean=0.35, state="cartilage")
a = vs.draw(ax, parts, at=(x, y))
ax.plot([x + 4.55], [y + 3.9], "o", ms=6, mfc="none", mec=P.ink(), zorder=20)
bio.label(ax, (x + 4.2, y + 5.2), "spiracle", size="tiny")
vs.callout(ax, a["hyomandibula"], (x + 6.4, y + 5.0), "hyomandibula")
vs.legend(ax, [("palatoquadrate", "palatoquadrate (upper jaw)"), ("meckel", "Meckel's cartilage (lower jaw)"),
               ("hyomandibula", "hyomandibula"), ("ceratohyal", "ceratohyal"), "arch_3", "arch_4", "arch_5",
               "arch_6", "arch_7", ("chondrocranium", "chondrocranium", "cartilage")],
          at=(0.5, 1.4), width=28.0, ncols=5)
