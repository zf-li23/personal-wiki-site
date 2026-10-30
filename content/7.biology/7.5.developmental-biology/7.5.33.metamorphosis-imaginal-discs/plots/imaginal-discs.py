"""Imaginal discs of Drosophila and the adult structures they form (schematic, not to scale).

A: third-instar larva (lateral view, anterior left) with its imaginal discs: eye-antennal, three pairs of leg discs,
wing, haltere and genital discs (the labial, humeral and clypeolabral discs are omitted). B: the adult fly in dorsal
view; the coloured labels match the discs. Each wing disc forms one wing and the dorsal mesothorax (notum); the
larval cells themselves die at metamorphosis, except the precursors of the abdominal epidermis (histoblasts).
"""

import wikibio as bio
from wikibio import limbdev as LD
from wikibio import zoomorph as zm

P = bio.P
fig, ax = bio.canvas(30.0, 11.0)
bio.panel(ax, "A", (0.2, 10.8))
lv = LD.larva(ax, (7.6, 5.6), 13.0, height=4.0)
d = lv["discs"]
names = {"eye-antenna": "Eye-antennal disc", "leg 1": "Leg discs (T1-T3)", "wing": "Wing disc", "haltere": "Haltere disc",
         "genital": "Genital disc"}
pos = {"eye-antenna": (1.2, 9.3), "leg 1": (3.2, 1.6), "wing": (6.4, 9.6), "haltere": (10.0, 9.3), "genital": (12.2, 1.6)}
for k, txt in names.items():
    bio.callout(ax, d[k], pos[k], txt, size="small")
bio.label(ax, (7.6, 0.6), "third-instar larva (lateral, anterior left)", size="tiny", color=P.muted())

bio.panel(ax, "B", (16.2, 10.8))
f = zm.insect(ax, (23.0, 5.4), 5.6, order="Diptera", view="dorsal")
lab = [("eye", (18.4, 9.6), "Eye, antenna (eye-antennal disc)", "neuron"), ("forewing", (27.4, 9.6), "Wing (wing disc)", "channel"),
       ("thorax", (17.4, 6.5), "Notum (wing disc)", "channel"), ("haltere", (27.4, 4.2), "Haltere (haltere disc)", "receptor"),
       ("abdomen", (27.4, 1.4), "Genitalia (genital disc)", "protein")]
for key, xy, txt, tk in lab:
    if key in f and f[key] is not None:
        bio.callout(ax, f[key], xy, txt, size="small", color=P.edge(tk) if not P.is_dark() else P.fill(tk))
legs = f.get("legs", {})
if "hind" in legs:
    m = legs["hind"]
    pt = m.get("femur") or next(iter(m.values()))
    bio.callout(ax, pt, (17.2, 2.6), "Legs (leg discs)", size="small", color=P.edge("tibia") if not P.is_dark() else P.fill("tibia"))
