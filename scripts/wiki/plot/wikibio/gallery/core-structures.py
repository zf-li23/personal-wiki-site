import wikibio as bio

fig, ax = bio.canvas(16, 8)
bio.neuron(ax, (3.0, 5.6), (9.2, 5.6))
bio.synapse(ax, (12.5, 5.0))
bio.ribosome(ax, (1.2, 2.2))
bio.actin(ax, (2.2, 2.2), (5.2, 2.2))
bio.microtubule(ax, (2.2, 1.2), (5.2, 1.2))
bio.antibody(ax, (6.8, 1.9), size=1.6)
bio.virus(ax, (9.2, 1.9), 0.7)
bio.virus(ax, (11.4, 1.9), 0.6, kind="enveloped")
for x, t in [(1.2, "Ribosome"), (3.7, "Actin / microtubule"), (6.8, "Antibody"), (9.2, "Capsid"), (11.4, "Enveloped virus")]:
    bio.label(ax, (x, 0.35), t, size="small")
