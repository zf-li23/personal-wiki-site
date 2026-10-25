# Pollination and double fertilization in angiosperms. A: a mature (bicellular) pollen grain: the tube
# cell and the generative cell inside the sculptured wall (exine). B: after pollination the pollen grain
# germinates on the stigma; the pollen tube grows down through the style to an ovule; the generative cell
# divides into two sperm cells. C: the mature ovule with its seven-celled, eight-nucleate embryo sac
# (female gametophyte): egg apparatus (egg and two synergids) at the micropylar end, the large central
# cell with two polar nuclei, three antipodal cells at the opposite (chalazal) end. The tube enters
# through the micropyle and releases both sperm cells. D: one sperm fuses with the egg (zygote, 2n, the
# future embryo); the other fuses with the two polar nuclei (primary endosperm nucleus, 3n, the future
# endosperm). The integuments become the seed coat.
import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(31.4, 12.6)

bio.panel(ax, "A", (0.2, 12.4))
bio.label(ax, (2.9, 11.4), "Pollen grain", size="normal", bold=True)
PM.specimen(ax, "wikimedia/pollen-grain", at=(2.9, 8.6), height=3.4, left=0.9, right=4.9, labels=[
    dict(part="wall", text="Exine", side="left", where="left"),
    dict(at=(0.48, 0.71), text="Generative cell", side="right"),
    dict(at=(0.5, 0.25), text="Tube cell", side="right"),
])
bio.label(ax, (2.9, 6.4), "n", size="small", color=P.muted())

bio.panel(ax, "B", (7.1, 12.4))
bio.label(ax, (10.0, 11.4), "Pollen tube growth", size="normal", bold=True)
PM.specimen(ax, "wikimedia/pistil-pollination", at=(10.0, 5.6), height=9.6, left=7.9, right=12.3, gap=0.6, labels=[
    dict(at=(0.4, 0.95), text="Pollen grain", side="left"),
    dict(at=(0.5, 0.92), text="Stigma", side="right"),
    dict(at=(0.47, 0.7), text="Style", side="left"),
    dict(part="pollen-tube", text="Pollen tube", side="right"),
    dict(at=(0.15, 0.3), text="Ovary wall", side="left"),
    dict(at=(0.555, 0.27), text="Ovule", side="right"),
])

bio.panel(ax, "C", (14.4, 12.4))
bio.label(ax, (19.9, 11.4), "Mature ovule at fertilization", size="normal", bold=True)
o = PM.specimen(ax, "wikimedia/ovule-double-fertilization", at=(19.9, 6.2), height=7.0, left=16.3, right=23.0, gap=0.62, labels=[
    dict(at=(0.36, 0.86), text="Integuments", side="left"),
    dict(at=(0.5, 0.75), text="Antipodal cells", side="right"),
    dict(at=(0.485, 0.53), text="Polar nuclei", side="right"),
    dict(at=(0.40, 0.62), text="Central cell", side="left"),
    dict(at=(0.54, 0.46), text="Sperm cell", side="right"),
    dict(at=(0.38, 0.31), text="Synergid", side="left"),
    dict(at=(0.47, 0.29), text="Egg", side="right"),
    dict(at=(0.48, 0.19), text="Sperm cell ", side="right"),
    dict(at=(0.05, 0.6), text="Pollen tube", side="left"),
    dict(at=(0.42, 0.2), text="Micropyle", side="left"),
])
bio.label(ax, (19.9, 2.2), "embryo sac (female gametophyte, n): 7 cells, 8 nuclei", size="small", color=P.muted())

bio.panel(ax, "D", (25.4, 12.4))
bio.label(ax, (28.3, 11.4), "Double fertilization", size="normal", bold=True)
rows = [("Sperm + egg", "Zygote (2n)", "Embryo", "positive", 10.3),
        ("Sperm + 2 polar nuclei", "Endosperm nucleus (3n)", "Endosperm", "highlight", 8.3)]
for a, b, c, tok, y in rows:
    bio.box(ax, (28.3, y), 4.8, 0.62, token=tok, text=a, size="small")
    bio.arrow(ax, (28.3, y - 0.36), (28.3, y - 0.78), kind="process", head=0.16)
    bio.label(ax, (28.3, y - 1.05), b, size="small", bold=True)
s = PM.specimen(ax, "wikimedia/seed-section", at=(27.9, 3.4), height=3.0, left=25.8, right=30.0, labels=[
    dict(part="seed-coat", text="Seed coat", side="left", where="left"),
    dict(at=(0.45, 0.65), text="Endosperm (3n)", side="right"),
    dict(part="embryo", text="Embryo (2n)", side="right"),
])
bio.label(ax, (27.9, 1.4), "seed: integuments become the seed coat", size="tiny", color=P.muted())
bio.arrow(ax, (24.4, 6.2), (25.6, 6.2), kind="process", lw=1.6)
