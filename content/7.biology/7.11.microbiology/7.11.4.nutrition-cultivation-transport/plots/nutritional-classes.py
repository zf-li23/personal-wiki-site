"""Nutritional classes as a decision tree: energy source -> electron donor -> carbon source.
Leaves give the class and representative organisms (genus names in italics). A note names
facultative switches (purple nonsulfur bacteria: photoheterotroph <-> chemoorganotroph in the dark
with O2; hydrogen bacteria: chemolithoautotroph <-> chemoorganoheterotroph)."""

import wikibio as bio

P = bio.P
fig, ax = bio.canvas(26.0, 11.6)


def node(xy, text, token, w=4.2, h=0.9, size="small"):
    bio.box(ax, xy, w, h, token, text, size=size)


def edge(a, b, text=None, off=(0.0, 0.0)):
    bio.arrow(ax, a, b, kind="process", color=P.muted(), lw=1.0, head=0.16)
    if text:
        m = ((a[0] + b[0]) / 2 + off[0], (a[1] + b[1]) / 2 + off[1])
        bio.label(ax, m, text, size="tiny", color=P.muted())


# level 0
node((13.0, 10.6), "Energy source?", "neutral", w=4.6)
# level 1
node((5.5, 8.6), "Light: phototroph", "highlight", w=5.0)
node((19.0, 8.6), "Chemicals: chemotroph", "enzyme", w=5.6)
edge((12.0, 10.15), (6.6, 9.05))
edge((14.0, 10.15), (17.9, 9.05))
# level 2 (electron donor) for chemotrophs
node((14.6, 6.5), "Inorganic donor:\nlithotroph", "metabolite", w=4.4, h=1.15)
node((22.6, 6.5), "Organic donor:\norganotroph", "carbohydrate", w=4.4, h=1.15)
edge((18.2, 8.15), (15.4, 7.07))
edge((19.8, 8.15), (21.8, 7.07))

# leaves: (x, carbon, class, token, examples, italic examples)
leaves = [
    (2.4, "CO₂", "Photoautotroph", "chloroplast", ["cyanobacteria, algae", "purple and green", "sulfur bacteria"], [False, False, False]),
    (7.9, "organic C", "Photoheterotroph", "highlight", ["purple nonsulfur", "bacteria", "heliobacteria"], [False, False, False]),
    (13.0, "CO₂", "Chemolitho-\nautotroph", "metabolite", ["Nitrosomonas", "Acidithiobacillus", "methanogens"], [True, True, False]),
    (17.8, "organic C", "Mixotroph", "metabolite", [r"$\it{Beggiatoa}$", "(some strains)"], [False, False]),
    (23.2, "organic C", "Chemoorgano-\nheterotroph", "carbohydrate", ["Escherichia coli", "fungi, protozoa", "animals"], [True, False, False]),
]
src = {2.4: (4.3, 8.15), 7.9: (6.7, 8.15), 13.0: (13.8, 5.92), 17.8: (15.4, 5.92), 23.2: (22.6, 5.92)}
for x, carbon, cls, tok, ex, it in leaves:
    y = 3.9
    node((x, y), cls, tok, w=4.0, h=1.15)
    a = src[x]
    edge(a, (x, y + 0.6), text="C: " + carbon, off=(-0.9, 0.0) if x < 10 else ((-0.8, 0.0) if x == 13.0 else (1.0, 0.0)))
    for k, (t, ital) in enumerate(zip(ex, it)):
        bio.label(ax, (x, 2.75 - 0.52 * k), t, size="tiny", italic=ital, color=P.ink())

# facultative switches (note)
bio.label(ax, (13.0, 0.5), "Facultative switches are common: purple nonsulfur bacteria grow chemoorganotrophically in the dark with O₂;"
          " hydrogen bacteria use organic compounds when available.", size="tiny", color=P.edge("positive"))
