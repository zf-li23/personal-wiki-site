# Anatomy of the angiosperm flower. A: a perfect (bisexual) flower in longitudinal section: the
# perianth (sepals of the calyx, petals of the corolla), the androecium (stamens: anther on a filament)
# and the gynoecium (here one pistil: stigma, style and ovary with ovules), all borne on the receptacle
# at the tip of the pedicel. B: a stamen shedding pollen, and an anther in cross-section: two thecae
# joined by the connective (with its vascular bundle), each theca with two pollen sacs (microsporangia).
# C: position of the ovary relative to the attachment of the other floral organs: superior ovary
# (hypogynous flower, organs inserted below the ovary), half-inferior and inferior ovary (epigynous
# flower, the receptacle or floral cup fused to the ovary wall, organs inserted above it).
# D: a disc floret of the Asteraceae: inferior ovary, calyx reduced to a pappus of bristles, five fused
# petals (sympetalous corolla), anthers fused into a tube around the style, two-lobed stigma.
import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(29.6, 14.6)

# ---- A: flower section --------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 14.4))
PM.specimen(ax, "wikimedia/flower-section", at=(6.2, 7.6), height=8.0, left=1.6, right=10.9, gap=0.55, labels=[
    dict(part="petal", text="Petal", side="left", where="top"),
    dict(at=(0.41, 0.80), text="Anther", side="left"),
    dict(at=(0.355, 0.62), text="Filament", side="left"),
    dict(at=(0.33, 0.47), text="Sepal", side="left"),
    dict(at=(0.43, 0.24), text="Receptacle", side="left"),
    dict(at=(0.40, 0.07), text="Pedicel", side="left"),
    dict(at=(0.54, 0.84), text="Stigma", side="right"),
    dict(at=(0.535, 0.70), text="Style", side="right"),
    dict(at=(0.53, 0.43), text="Ovary", side="right"),
    dict(at=(0.455, 0.535), text="Ovule", side="right"),
])
bio.label(ax, (6.2, 13.25), "Perfect flower, longitudinal section", size="normal", bold=True)

# ---- B: stamen and anther -----------------------------------------------------------------------
bio.panel(ax, "B", (12.0, 14.4))
bio.label(ax, (16.0, 13.25), "Stamen and anther", size="normal", bold=True)
PM.specimen(ax, "wikimedia/stamen", at=(14.7, 10.1), height=3.6, left=13.1, right=16.8, labels=[
    dict(part="anther", text="Anther", side="right", where="top"),
    dict(at=(0.88, 0.72), text="Pollen", side="right"),
    dict(at=(0.2, 0.3), text="Filament", side="left"),
])
PM.specimen(ax, "wikimedia/anther", at=(19.6, 10.2), height=3.4, left=17.8, right=21.3, gap=0.5, labels=[
    dict(at=(0.22, 0.9), text="Pollen sac", side="left"),
    dict(at=(0.25, 0.55), text="Theca", side="left"),
    dict(at=(0.49, 0.83), text="Connective", side="right"),
    dict(at=(0.48, 0.93), text="Vascular bundle", side="right"),
    dict(at=(0.5, 0.15), text="Filament", side="right"),
])
bio.label(ax, (19.6, 8.15), "anther in cross-section", size="small", color=P.muted())

# ---- C: ovary position ----------------------------------------------------------------------------
bio.panel(ax, "C", (12.0, 7.4))
bio.label(ax, (17.0, 7.2), "Position of the ovary", size="normal", bold=True)
TOK = {"ovary": "ovary", "style": "ovary", "petal": "petal", "sepal": "sepal", "anther": "anther", "filament": "anther",
       "receptacle": "neutral"}
for k, (iid, name, note) in enumerate((("superior", "Superior", "hypogynous"), ("half", "Half-inferior", "partly sunk in the receptacle"),
                                         ("inferior", "Inferior", "epigynous"))):
    x = 14.3 + 3.5 * k
    if iid == "superior":
        b = bio.icon(ax, "wikimedia/ovary-superior", at=(x, 3.9), height=4.0, parts=TOK)
    elif iid == "half":
        b = bio.icon(ax, "wikimedia/ovary-half-inferior", at=(x, 3.9), height=4.0, parts=TOK)
    else:
        b = bio.icon(ax, "wikimedia/ovary-inferior", at=(x, 3.9), height=4.0, parts=TOK)
    bio.label(ax, (x, 1.35), name, size="small", bold=True)
    bio.label(ax, (x, 0.95), f"({note} flower)" if k != 1 else f"({note})", size="tiny", color=P.muted())
for k, (tok, text) in enumerate((("ovary", "Ovary"), ("neutral", "Receptacle / floral cup"), ("petal", "Petal"),
                                  ("sepal", "Sepal"), ("anther", "Stamen"))):
    x = 12.9 + [0, 1.5, 5.4, 6.9, 8.4][k]
    bio.box(ax, (x, 6.45), 0.32, 0.32, token=tok, radius=0.06)
    bio.label(ax, (x + 0.28, 6.45), text, size="small", ha="left")

# ---- D: disc floret -------------------------------------------------------------------------------
bio.panel(ax, "D", (23.9, 14.4))
bio.label(ax, (26.6, 13.25), "Disc floret (Asteraceae)", size="normal", bold=True)
PM.specimen(ax, "wikimedia/disc-floret", at=(26.3, 7.6), height=9.0, left=24.9, right=28.0, gap=0.55, labels=[
    dict(at=(0.07, 0.86), text="Stigma", side="left"),
    dict(part="anther-tube", text="Anther tube", side="right"),
    dict(part="corolla", text="Corolla", side="right", where="right"),
    dict(at=(0.57, 0.30), text="Pappus", side="left"),
    dict(part="ovary", text="Inferior ovary", side="right"),
])
