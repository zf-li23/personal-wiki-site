# From gametophyte to sporophyte dominance in land plants. A: a moss (Polytrichum type). The leafy
# gametophore (haploid gametophyte, grown from a filamentous protonema) is the plant; the sporophyte (seta
# and capsule with its operculum) stays attached to it and depends on it. Gametangia sit at the shoot
# tips: archegonia (flask-shaped, one egg in the venter) in an archegonial head, antheridia (producing
# flagellate sperm) in an antheridial head. B: a fern: the sporophyte with its fronds is the large,
# independent plant; the gametophyte is a small free-living prothallus with rhizoids. C: a pine: the
# sporophyte is a tree; the gametophytes are reduced and enclosed in the cones. Pollen cones shed pollen;
# seed cones carry ovules (and later seeds) on their scales. The ovule of a gymnosperm is naked on the
# scale; that of an angiosperm is enclosed in the ovary wall.
import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(34.0, 16.4)
GAM, SPO = P.edge("rna"), P.edge("dna")

# ---- A: moss --------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.2, 16.2))
bio.label(ax, (6.4, 15.6), "Moss: gametophyte dominant", size="normal", bold=True)
PM.specimen(ax, "wikimedia/moss-gametophyte-sporophyte", at=(2.6, 8.4), height=11.0, left=1.6, right=3.9, gap=0.6, labels=[
    dict(at=(0.7, 0.9), text="Capsule (2n)", side="right"),
    dict(at=(0.55, 0.7), text="Seta (2n)", side="right"),
    dict(at=(0.4, 0.3), text="Leafy gametophore (n)", side="right"),
    dict(at=(0.5, 0.02), text="Rhizoids", side="right"),
])
PM.specimen(ax, "wikimedia/moss-archegonial-head", at=(9.2, 12.4), width=3.6, left=7.0, right=11.3, gap=0.5, labels=[
    dict(at=(0.56, 0.72), text="Archegonium", side="right"),
    dict(at=(0.57, 0.4), text="Egg", side="right"),
    dict(at=(0.15, 0.3), text="Leaf", side="left"),
], size="small")
bio.label(ax, (9.2, 10.1), "female shoot tip (section)", size="tiny", color=P.muted())
PM.specimen(ax, "wikimedia/moss-antheridial-head", at=(9.2, 7.6), width=3.6, left=7.0, right=11.3, gap=0.5, labels=[
    dict(at=(0.45, 0.6), text="Antheridium", side="right"),
    dict(at=(0.22, 0.5), text="Sperm", side="left"),
], size="small")
bio.label(ax, (9.2, 5.7), "male shoot tip (section)", size="tiny", color=P.muted())
PM.specimen(ax, "wikimedia/moss-protonema", at=(9.2, 3.3), width=3.6, left=7.0, right=11.3, labels=[
    dict(at=(0.6, 0.12), text="Protonema", side="right"),
    dict(at=(0.1, 0.6), text="Young gametophore", side="left"),
], size="small")

# ---- B: fern ---------------------------------------------------------------------------------------
bio.panel(ax, "B", (12.8, 16.2))
bio.label(ax, (16.2, 15.6), "Fern: sporophyte dominant", size="normal", bold=True)
PM.specimen(ax, "wikimedia/fern-sporophyte", at=(16.0, 11.2), width=5.6, left=13.0, right=19.0, parts={"rhizome": "animal"}, labels=[
    dict(at=(0.85, 0.8), text="Frond (2n)", side="right"),
    dict(part="rhizome", text="Rhizome", side="right"),
])
PM.specimen(ax, "wikimedia/fern-gametophyte", at=(15.6, 4.2), height=3.0, left=13.6, right=17.4, labels=[
    dict(at=(0.5, 0.6), text="Prothallus (n)", side="right"),
    dict(at=(0.45, 0.03), text="Rhizoids", side="right"),
], size="small")
bio.label(ax, (15.6, 2.2), "gametophyte, a few mm wide", size="tiny", color=P.muted())

# ---- C: pine ---------------------------------------------------------------------------------------
bio.panel(ax, "C", (21.4, 16.2))
bio.label(ax, (27.4, 15.6), "Pine: sporophyte dominant, seeds", size="normal", bold=True)
bio.icon(ax, "wikimedia/pine-tree", at=(23.0, 11.6), height=6.2)
bio.label(ax, (23.0, 8.15), "Sporophyte (2n)", size="small", color=SPO)
PM.specimen(ax, "wikimedia/pine-branch-cone", at=(27.4, 12.6), width=3.8, right=29.6, labels=[
    dict(part="cone", text="Seed cone", side="right"), dict(at=(0.3, 0.8), text="Needles", side="right", y=14.2)])
PM.specimen(ax, "wikimedia/pine-pollen-cone", at=(32.2, 12.4), height=3.0, left=31.2, labels=[
    dict(at=(0.5, 0.6), text="Pollen cone", side="left", y=14.4)])
PM.specimen(ax, "wikimedia/pine-seed-cone-section", at=(24.0, 4.4), height=4.6, left=21.9, right=26.4, parts={"scale": "animal", "axis": "bone"}, labels=[
    dict(at=(0.5, 0.4), text="Cone axis", side="left"),
    dict(at=(0.22, 0.52), text="Ovuliferous scale", side="left"),
], size="small")
bio.label(ax, (24.0, 1.6), "seed cone, longitudinal section", size="tiny", color=P.muted())
PM.specimen(ax, "wikimedia/ovule-gymno-angio", at=(30.6, 4.6), width=5.0, left=27.7, right=33.2, gap=0.5, labels=[
    dict(at=(0.03, 0.55), text="Integument", side="left"),
    dict(at=(0.15, 0.45), text="Nucellus", side="left"),
    dict(at=(0.15, 0.32), text="Megaspore", side="left"),
    dict(at=(0.97, 0.5), text="Ovary wall", side="right"),
], size="small")
bio.label(ax, (28.9, 1.6), "naked ovule\n(gymnosperm)", size="tiny", color=P.muted())
bio.label(ax, (31.9, 1.6), "enclosed ovule\n(angiosperm)", size="tiny", color=P.muted())
