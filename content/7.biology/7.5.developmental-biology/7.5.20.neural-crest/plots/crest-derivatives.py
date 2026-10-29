"""The neural crest and its main derivatives. Centre: a transverse section of the trunk just after neural tube
closure, with neural crest cells (green) leaving the dorsal neural tube. Around it, the cell types the crest forms
at different axial levels: cranial crest gives most of the bone and cartilage of the face and the anterior skull,
the odontoblasts of the teeth and cranial ganglia; cardiac crest the septum of the outflow tract; vagal and sacral
crest the enteric nervous system; trunk crest the dorsal root (sensory) ganglia, the sympathetic chain, the chromaffin
cells of the adrenal medulla and Schwann cells; crest from all levels except the cardiac makes pigment cells
(melanocytes) of the skin."""
import wikibio as bio
from wikibio import neurodev as N

fig, ax = bio.canvas(22, 11)
P = bio.P
a = N.neurulation_section(ax, (11.0, 7.4), 7.0, "tube")
bio.callout(ax, a["crest_l"], (8.3, 9.5), "Neural crest")
bio.callout(ax, a["lumen"], (13.7, 9.5), "Neural tube")
bio.callout(ax, a["somite_r"], (14.6, 4.3), "Somite")
items = [
    ("wikimedia/skull-human-lateral", (2.2, 8.6), "Craniofacial bone,", "cartilage, teeth (cranial)"),
    ("servier/heart", (2.2, 4.6), "Outflow tract septum,", "valves (cardiac)"),
    ("servier/intestine", (2.2, 1.2), "Enteric neurons, glia", "(vagal, sacral)"),
    ("servier/melanocyte", (19.6, 8.6), "Melanocytes", "(all but cardiac)"),
    ("dbcls/neuron-sensory", (19.6, 4.6), "Sensory, sympathetic neurons;", "Schwann cells (trunk)"),
]
for icon, xy, t1, t2 in items:
    if icon == "wikimedia/skull-human-lateral":
        bio.icon(ax, "wikimedia/skull-human-lateral", at=xy, height=1.9)
    elif icon == "servier/heart":
        bio.icon(ax, "servier/heart", at=xy, height=1.7)
    elif icon == "servier/intestine":
        bio.icon(ax, "servier/intestine", at=xy, height=1.6)
    elif icon == "servier/melanocyte":
        bio.icon(ax, "servier/melanocyte", at=xy, height=1.6)
    else:
        bio.icon(ax, "dbcls/neuron-sensory", at=xy, height=1.7)
    side = 1 if xy[0] < 11 else -1
    bio.label(ax, (xy[0], xy[1] - 1.25), t1, size="small")
    bio.label(ax, (xy[0], xy[1] - 1.65), t2, size="tiny", color=P.muted())
    start = a["crest_l"] if side > 0 else a["crest_r"]
    bio.arrow(ax, start, (xy[0] + side * 1.5, xy[1]), kind="process", head=0.15, lw=0.9, dashed=True, bend=0.1 * side)
bio.box(ax, (19.6, 1.5), 4.4, 0.9, token="antibody", text="Adrenal medulla (chromaffin)", size="small")
bio.arrow(ax, a["crest_r"], (17.9, 1.8), kind="process", head=0.15, lw=0.9, dashed=True, bend=-0.1)
