# Parts of a complete flower (template with coloured parts) and the stamen with an anther in section.
import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(24.0, 12.0)

bio.panel(ax, "A", (0.2, 11.8))
PM.specimen(ax, "wikimedia/flower-section", at=(7.0, 5.9), height=9.6, left=1.8, right=12.4, gap=0.6, labels=[
    dict(part="petal", text="Petal (corolla)", side="left", where="top"),
    dict(at=(0.41, 0.80), text="Anther", side="left"),
    dict(at=(0.355, 0.62), text="Filament", side="left"),
    dict(at=(0.33, 0.47), text="Sepal (calyx)", side="left"),
    dict(at=(0.43, 0.24), text="Receptacle", side="left"),
    dict(at=(0.40, 0.07), text="Pedicel", side="left"),
    dict(at=(0.54, 0.84), text="Stigma", side="right"),
    dict(at=(0.535, 0.70), text="Style", side="right"),
    dict(at=(0.53, 0.43), text="Ovary", side="right"),
    dict(at=(0.455, 0.535), text="Ovule", side="right"),
])
bio.label(ax, (7.0, 11.4), "Complete flower, longitudinal section", size="normal", bold=True)

bio.panel(ax, "B", (15.2, 11.8))
PM.specimen(ax, "wikimedia/stamen", at=(17.2, 8.4), height=4.8, left=14.9, right=19.4, labels=[
    dict(part="anther", text="Anther", side="right", where="top"),
    dict(at=(0.2, 0.3), text="Filament", side="left"),
])
PM.specimen(ax, "wikimedia/anther", at=(21.6, 3.6), height=4.6, left=19.4, right=23.8, gap=0.5, labels=[
    dict(part="pollen-sac", text="Pollen sac", side="left"),
    dict(part="theca", text="Theca", side="left", where="left"),
    dict(part="connective", text="Connective", side="right"),
    dict(part="vascular-bundle", text="Vascular bundle", side="right"),
    dict(part="filament", text="Filament", side="right", where="bottom"),
])
bio.label(ax, (21.6, 0.6), "anther in cross-section", size="small", color=P.muted())
