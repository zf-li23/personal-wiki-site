# Life cycles of two human nematodes. A: Ascaris lumbricoides, direct (one host), transmitted by eggs
# in soil; the larva migrates through liver, heart and lungs before settling in the small intestine.
# B: Wuchereria bancrofti (lymphatic filariasis), indirect, with a mosquito as intermediate host and
# vector; microfilariae circulate in the blood at night, when the vector bites.
import wikibio as bio
from wikibio import ecology as eco

P = bio.P
fig, ax = bio.canvas(26, 12.5)

A = [dict(text="Adults in small\nintestine (human)", token="animal"),
     dict(text="Unembryonated eggs\npassed in feces", token="plant"),
     dict(text="Embryonation in soil\n(2–3 weeks): infective egg", token="plant"),
     dict(text="Egg swallowed;\nlarva hatches in gut", token="neutral"),
     dict(text="Larva in blood:\nliver, heart, lungs", token="blood"),
     dict(text="Coughed up, swallowed;\nmolts to adult", token="neutral")]
B = [dict(text="Adults in lymphatic\nvessels (human)", token="animal"),
     dict(text="Microfilariae in\nblood (at night)", token="blood"),
     dict(text="Ingested by a\nfeeding mosquito", token="highlight"),
     dict(text="Develop to infective\nL3 in flight muscle", token="highlight"),
     dict(text="L3 enter the skin\nat the next bite", token="neutral"),
     dict(text="Mature in lymphatics\n(6–12 months)", token="neutral")]
eco.cycle(ax, (6.4, 5.9), 4.3, A, size="small")
eco.cycle(ax, (19.6, 5.9), 4.3, B, size="small")
bio.panel(ax, "A", (0.3, 12.3))
bio.label(ax, (1.2, 12.0), "Ascaris lumbricoides", size="title", italic=True, ha="left")
bio.panel(ax, "B", (13.5, 12.3))
bio.label(ax, (14.4, 12.0), "Wuchereria bancrofti", size="title", italic=True, ha="left")
bio.icon(ax, "servier/roundworm", at=(6.4, 5.9), height=1.6, color="animal")
bio.icon(ax, "phylopic/mosquito", at=(19.6, 5.9), height=1.4, color="animal")
for x, tok, txt in ((1.0, "plant", "outside the host (soil)"), (8.0, "blood", "migrating in blood")):
    bio.box(ax, (x, 0.5), 0.5, 0.35, tok)
    bio.label(ax, (x + 0.4, 0.5), txt, size="small", ha="left")
for x, tok, txt in ((14.2, "highlight", "in the mosquito (intermediate host)"), (21.6, "blood", "in human blood")):
    bio.box(ax, (x, 0.5), 0.5, 0.35, tok)
    bio.label(ax, (x + 0.4, 0.5), txt, size="small", ha="left")
