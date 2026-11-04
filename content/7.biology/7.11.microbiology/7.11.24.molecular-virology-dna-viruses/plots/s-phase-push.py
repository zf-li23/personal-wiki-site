# How small DNA viruses create their own S phase. Three unrelated viruses converge on the same two targets:
# the retinoblastoma protein, which holds E2F inactive, and p53, which would arrest or kill a cell whose DNA
# is replicated out of turn. Arrowheads follow SBGN: bar = inhibition, open arrow = activation.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(16, 8.6)

bio.label(ax, (8.0, 8.25), "Viral proteins", size="title", bold=True)
vir = [("SV40 large T", 2.4), ("Adenovirus E1A", 6.2), ("HPV E7", 9.6), ("Adenovirus E1B-55K", 13.2)]
for text, x in vir:
    bio.box(ax, (x, 7.4), 3.0 if "E1B" in text else 2.6, 0.72, "virus", text=text, size="small")
bio.box(ax, (2.4, 6.2), 2.6, 0.62, "virus", text="HPV E6", size="small")

# targets
bio.box(ax, (5.0, 4.8), 2.4, 0.8, "protein", text="Rb", size="normal")
bio.box(ax, (11.4, 4.8), 2.4, 0.8, "protein", text="p53", size="normal")
bio.box(ax, (5.0, 2.9), 2.4, 0.8, "receptor", text="E2F", size="normal")

for x in (2.4, 6.2, 9.6):
    bio.arrow(ax, (x, 7.05), (5.0, 5.3), kind="inhibition", bend=0.05 if x < 5 else -0.05)
bio.arrow(ax, (13.2, 7.05), (11.4, 5.3), kind="inhibition")
bio.arrow(ax, (2.4, 6.51), (10.6, 5.3), kind="inhibition", bend=0.3)
bio.arrow(ax, (2.4, 7.05), (11.9, 5.3), kind="inhibition", bend=0.18)
bio.label(ax, (8.2, 6.0), "degradation or sequestration", size="tiny", color=P.muted())

bio.arrow(ax, (5.0, 4.35), (5.0, 3.35), kind="inhibition")
bio.label(ax, (5.55, 3.85), "Rb holds E2F inactive", size="tiny", color=P.muted(), ha="left")

# outputs
bio.box(ax, (4.3, 1.5), 4.6, 0.85, "positive", text="S-phase genes: dNTP supply,\npolymerases, PCNA", size="small")
bio.arrow(ax, (4.6, 2.45), (4.4, 1.98), kind="activation")
bio.box(ax, (11.4, 2.9), 3.4, 0.8, "negative", text="Arrest / apoptosis", size="small")
bio.arrow(ax, (11.4, 4.35), (11.4, 3.35), kind="activation", dashed=True)
bio.label(ax, (13.7, 3.85), "prevented, so replication\nstress is tolerated", size="tiny", color=P.muted())

bio.box(ax, (8.6, 0.45), 6.2, 0.7, "dna", text="Viral genome replicated by the cellular machine", size="small")
bio.arrow(ax, (6.3, 1.3), (7.0, 0.8), kind="process")
bio.label(ax, (14.3, 1.6), "the same two lesions,\nwithout a productive cycle,\nstart transformation",
          size="tiny", color=P.muted())
