# Alternation of generations in a homosporous fern (e.g. Dryopteris): the diploid sporophyte is the
# dominant, free-living generation; meiosis in the sporangia gives haploid spores, which grow into the
# small free-living gametophyte (prothallus). Sperm swim to the archegonium in a film of water;
# fertilization gives the zygote, which grows into a new sporophyte on the gametophyte.
import wikibio as bio
from wikibio import plant


def draw_fern(ax, xy, s):
    plant.fern(ax, (xy[0], xy[1] - s * 0.28), s * 0.8)


def draw_sorus(ax, xy, s):
    plant.leaf(ax, (xy[0] - s * 0.75, xy[1] - s * 0.25), s * 1.0, s * 0.42, angle=18, veins=True)
    for f in (0.3, 0.5, 0.7):
        for sg in (1, -1):
            x = xy[0] - s * 0.75 + f * s * 0.95
            y = xy[1] - s * 0.25 + f * s * 0.32 + sg * s * 0.08
            plant.cell(ax, (x, y), s * 0.07, token="animal", nucleus=False)
    plant.sporangium(ax, (xy[0] + s * 0.45, xy[1] + s * 0.05), s * 0.6)


def draw_spores(ax, xy, s):
    plant.spores(ax, xy, s * 0.9, n=7)


def draw_gametophyte(ax, xy, s):
    plant.prothallus(ax, (xy[0], xy[1] + s * 0.1), s * 0.95)


def draw_gametes(ax, xy, s):
    plant.cell(ax, (xy[0] - s * 0.3, xy[1]), s * 0.55, token="receptor")
    plant.sperm(ax, (xy[0] + s * 0.35, xy[1] + s * 0.2), s * 0.45, angle=200)
    plant.sperm(ax, (xy[0] + s * 0.5, xy[1] - s * 0.25), s * 0.4, angle=170)


def draw_zygote(ax, xy, s):
    plant.cell(ax, xy, s * 0.55, token="positive")


def draw_young(ax, xy, s):
    plant.prothallus(ax, (xy[0], xy[1] - s * 0.15), s * 0.75, gametangia=False, sporophyte=True)


fig, ax = bio.canvas(16, 14.6)
stages = [
    dict(text="Sporophyte (2n)", draw=draw_fern, icon_size=2.0, bold=True),
    dict(text="Sorus: sporangia", draw=draw_sorus, icon_size=1.4),
    dict(text="Spores (n)", draw=draw_spores, icon_size=1.0),
    dict(text="Gametophyte (prothallus, n)", draw=draw_gametophyte, icon_size=1.5, bold=True),
    dict(text="Egg and sperm (n)", draw=draw_gametes, icon_size=1.0),
    dict(text="Zygote (2n)", draw=draw_zygote, icon_size=0.9),
    dict(text="Young sporophyte", draw=draw_young, icon_size=1.6),
]
plant.alternation_of_generations(ax, (8.0, 7.3), 4.9, stages, meiosis=1, fertilization=4, gap=0.25,
                                 arrow_labels=[None, None, "Germination", "Gametangia", None, "Mitosis", "Growth"])
