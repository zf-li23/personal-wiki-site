import wikibio as bio

fig, ax = bio.canvas(16, 7)
bio.dna(ax, (0.8, 5.8), (7.5, 5.8), style="helix")
bio.dna(ax, (8.5, 5.8), (15.2, 5.8), style="duplex")
bio.strand(ax, (1.0, 4.2), (7.0, 4.2), cap=True, polya=True)
for i in range(5):
    bio.protein(ax, (9.0 + 1.35 * i, 4.2), 1.05, 0.8, bio.P.protein(i), text=f"P{i + 1}")
y = 2.6
x = 0.8
for kind in ["process", "activation", "inhibition", "catalysis", "necessary"]:
    bio.arrow(ax, (x, y), (x + 1.8, y), kind=kind)
    bio.label(ax, (x + 0.9, y - 0.45), kind, size="small")
    x += 2.6
bio.arrow(ax, (13.8, 2.8), (15.4, 2.2), kind="activation", bend=0.35, dashed=True)
bio.domains(ax, 0.8, 1.0, [("SH2", 1.0, "receptor"), ("SH3", 0.8, "antibody"), ("Kinase", 2.2, "enzyme")])
bio.reaction(ax, (7.0, 1.0), (10.0, 1.0), side=[("ATP", "in"), ("ADP", "out")])
bio.molecule(ax, (6.5, 1.0), "metabolite", "Glc")
bio.molecule(ax, (10.6, 1.0), "metabolite", "G6P", r=0.28)
