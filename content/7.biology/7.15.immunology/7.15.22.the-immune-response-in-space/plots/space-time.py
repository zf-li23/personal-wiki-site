# One primary immune response in space and time. Top: the route of antigen and cells between the
# infected tissue, the draining lymph node and the blood; bottom: the time line of the same events.
import wikibio as bio
from wikibio import immuno, quant

P = bio.P
fig, ax = bio.canvas(28, 14.2)

# ---- compartments ----------------------------------------------------------------------------------------------
bio.box(ax, (4.0, 9.6), 6.8, 5.0, "extracellular")
bio.label(ax, (4.0, 11.75), "Infected tissue", size="small")
bio.box(ax, (14.0, 9.6), 8.6, 5.0, "cytoplasm")
bio.label(ax, (14.0, 11.75), "Draining lymph node", size="small")
bio.box(ax, (24.0, 9.6), 6.8, 5.0, "extracellular")
bio.label(ax, (24.0, 11.75), "Blood → inflamed tissue", size="small")

# tissue: pathogen, resident sentinels, neutrophils, DC leaving
bio.virus(ax, (2.2, 10.3), 0.42, kind="enveloped")
bio.virus(ax, (3.1, 9.2), 0.35, kind="enveloped")
immuno.immune_cell(ax, (4.6, 10.6), r=0.5, kind="dendritic", token="receptor", seed=1)
immuno.immune_cell(ax, (2.4, 8.2), r=0.38, token="enzyme", seed=2)
immuno.immune_cell(ax, (5.6, 8.4), r=0.38, token="enzyme", seed=3)
bio.label(ax, (4.0, 7.45), "sentinels sense PAMPs/DAMPs;\nneutrophils, monocytes arrive (hours)", size="tiny")
bio.label(ax, (5.45, 11.2), "DC", size="tiny", ha="left")

# lymph node: T zone and follicle
bio.box(ax, (12.2, 9.0), 3.6, 2.6, "dna2")
bio.label(ax, (12.2, 10.1), "T-cell zone", size="tiny", color=P.on_fill())
bio.box(ax, (16.3, 10.0), 3.4, 2.6, "antibody")
bio.label(ax, (16.3, 11.05), "B-cell follicle", size="tiny", color=P.on_fill())
immuno.immune_cell(ax, (11.4, 8.7), r=0.42, kind="dendritic", token="receptor", seed=4)
immuno.immune_cell(ax, (12.9, 8.6), r=0.3, token="cd4", seed=5)
immuno.immune_cell(ax, (13.1, 9.4), r=0.3, token="cd8", seed=6)
immuno.immune_cell(ax, (15.7, 9.6), r=0.3, token="neutral", seed=7, receptor_token="antibody", receptors=5)
immuno.immune_cell(ax, (16.9, 9.5), r=0.3, token="neutral", seed=8, receptor_token="antibody", receptors=5)
bio.label(ax, (14.0, 7.45), "naive T cells scan DCs; T–B border;\ngerminal centre in the follicle", size="tiny")

# blood / effector site
immuno.immune_cell(ax, (22.4, 10.3), r=0.38, token="cd8", seed=9)
immuno.immune_cell(ax, (23.6, 9.4), r=0.38, token="cd4", seed=10)
immuno.immune_cell(ax, (25.6, 10.2), r=0.48, kind="plasma", token="neutral", seed=11)
for k, (dx, dy, a) in enumerate(((1.0, 0.4, -60), (1.2, -0.2, -100))):
    bio.antibody(ax, (25.6 + dx, 10.2 + dy), size=0.32, angle=a)
immuno.immune_cell(ax, (24.6, 8.4), r=0.36, kind="memory", token="neutral", seed=12)
bio.label(ax, (24.0, 7.45), "effector T cells home to the site;\nantibody circulates; memory remains", size="tiny")

# routes
bio.arrow(ax, (5.3, 10.9), (10.8, 9.2), kind="process", bend=-0.15)
bio.label(ax, (8.55, 6.55), "afferent lymph: DCs (1–2 d),\nfree antigen (minutes)", size="tiny")
bio.arrow(ax, (17.6, 9.0), (21.8, 9.8), kind="process", bend=0.15)
bio.label(ax, (19.5, 6.55), "efferent lymph,\nthoracic duct", size="tiny")
bio.arrow(ax, (22.6, 12.4), (5.0, 12.4), kind="process", bend=-0.08, dashed=True)
bio.label(ax, (14.0, 13.85), "effector cells and antibody return to the infected tissue via the blood", size="tiny")

# ---- time line ----------------------------------------------------------------------------------------------------
events = [
    (0, 1, "enzyme", "innate response, inflammation"),
    (0.5, 2, "receptor", "DC migration"),
    (1, 5, "dna2", "T-cell priming and expansion"),
    (2, 8, "antibody", "B-cell activation, extrafollicular plasmablasts"),
    (5, 21, "highlight", "germinal centre"),
    (5, 12, "cd8", "effector T cells in tissue, clearance"),
    (12, 24, "neutral", "contraction; memory"),
]
pl = quant.Plot(ax, (5.0, 0.9, 21.0, 4.6), (0, 28), (0, len(events)), xlabel="Days after infection",
                xticks=[0, 2, 4, 7, 10, 14, 21, 28], frame="l")
for k, (a, b, tok, txt) in enumerate(events):
    y = len(events) - k - 0.5
    bio.box(ax, ((pl.X(a) + pl.X(b)) / 2, pl.Y(y)), pl.X(b) - pl.X(a), 0.42, tok)
    bio.label(ax, (pl.X(b) + 0.15, pl.Y(y)), txt, size="tiny", ha="left")
