"""Direction of inquiry in the three basic observational designs (schematic).

Cohort: people free of disease are classified by exposure and followed forward to new cases.
Case-control: cases and controls are identified first and their past exposure is ascertained.
Cross-sectional: exposure and disease are measured at the same moment, in a sample of the population.
"""
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(17, 10.4)
rows = [("Cohort study", 8.7), ("Case-control study", 5.3), ("Cross-sectional study", 1.9)]
for name, y in rows:
    bio.label(ax, (1.6, y + 1.35), name, size="normal", bold=True, ha="left")
# time axis
ax.annotate("", xy=(16.6, 0.25), xytext=(3.4, 0.25), arrowprops=dict(arrowstyle="->", color=P.muted(), lw=1.0))
bio.label(ax, (16.5, 0.6), "time", size="tiny", color=P.muted(), ha="right")

# cohort: two exposure groups at the start, followed forward
y = 8.7
bio.box(ax, (3.6, y + 0.45), 2.6, 0.75, token="rna", text="exposed", size="small")
bio.box(ax, (3.6, y - 0.45), 2.6, 0.75, token="dna", text="unexposed", size="small")
for dy, tok in ((0.45, "rna"), (-0.45, "dna")):
    bio.arrow(ax, (5.0, y + dy), (12.2, y + dy), kind="process", color=P.edge(tok))
    bio.box(ax, (13.6, y + dy), 2.4, 0.7, token="neutral", text="disease?", size="tiny")
bio.label(ax, (8.6, y + 1.25), "follow forward: incidence in each group, RR, RD", size="tiny", color=P.muted())
bio.label(ax, (2.2, y - 1.15), "free of disease at entry", size="tiny", color=P.muted(), ha="left")

# case-control: cases and controls now, look back to exposure
y = 5.3
bio.box(ax, (12.4, y + 0.45), 2.4, 0.75, token="rna", text="cases", size="small")
bio.box(ax, (12.4, y - 0.45), 2.4, 0.75, token="dna", text="controls", size="small")
for dy, tok in ((0.45, "rna"), (-0.45, "dna")):
    bio.arrow(ax, (11.1, y + dy), (5.2, y + dy), kind="process", color=P.edge(tok), dashed=True)
    bio.box(ax, (3.9, y + dy), 2.4, 0.7, token="neutral", text="exposed?", size="tiny")
bio.label(ax, (8.2, y + 1.25), "look back: exposure odds in each group, OR only", size="tiny", color=P.muted())

# cross-sectional: one snapshot
y = 1.9
bio.box(ax, (10.0, y), 4.6, 1.3, token="neutral", text="exposure and disease\nmeasured together", size="small")
bio.label(ax, (10.0, y + 1.25), "snapshot: prevalence, prevalence ratio", size="tiny", color=P.muted())
