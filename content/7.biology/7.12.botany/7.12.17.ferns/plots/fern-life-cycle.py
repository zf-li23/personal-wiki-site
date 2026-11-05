"""Life cycle of a homosporous leptosporangiate fern (e.g. Pteridium): sporophyte (2n) with sori; meiosis in
the sporangia gives spores (n); a spore germinates into a filament and a plate and grows into the
heart-shaped prothallus with rhizoids, antheridia and archegonia; multiflagellate sperm swim to the egg;
the zygote develops into an embryo and a young sporophyte on the prothallus."""
import numpy as np

import wikibio as bio
from wikibio import plant

P = bio.P


def draw_fern(ax, xy, s):
    bio.icon(ax, "wikimedia/fern-sporophyte", at=(xy[0], xy[1] + 0.55), height=s * 1.25)


def draw_sorus(ax, xy, s):
    plant.pinnule(ax, (xy[0] - s * 0.55, xy[1] - s * 0.35), s * 1.15, angle=90, sorus="round", indusium="reniform")
    plant.leptosporangium(ax, (xy[0] + s * 0.45, xy[1] + s * 0.3), s * 0.65, stage="closed")


def draw_spores(ax, xy, s):
    plant.spores(ax, xy, s * 0.9, n=7)


def draw_filament(ax, xy, s):
    x, y = xy
    for k in range(5):
        plant.cell(ax, (x - s * 0.4 + k * s * 0.2, y), s * 0.2, token="plant", nucleus=False)
    ax.plot([x - s * 0.5, x - s * 0.62], [y, y - s * 0.4], color=P.muted(), lw=0.7)
    pts = np.array([[x + s * 0.35, y + s * 0.15], [x + s * 0.7, y + s * 0.45], [x + s * 0.85, y + s * 0.1], [x + s * 0.65, y - s * 0.2]])
    bio.shape(ax, pts, token="plant", zorder=11)


def draw_gametophyte(ax, xy, s):
    bio.icon(ax, "wikimedia/fern-gametophyte", at=(xy[0], xy[1] + 0.1), height=s * 1.1)


def draw_gametes(ax, xy, s):
    plant.cell(ax, (xy[0] - s * 0.3, xy[1]), s * 0.55, token="receptor")
    plant.sperm(ax, (xy[0] + s * 0.35, xy[1] + s * 0.2), s * 0.45, angle=200)
    plant.sperm(ax, (xy[0] + s * 0.5, xy[1] - s * 0.25), s * 0.4, angle=170)


def draw_young(ax, xy, s):
    plant.prothallus(ax, (xy[0], xy[1] + s * 0.2), s * 0.7, gametangia=False, sporophyte=True)


fig, ax = bio.canvas(18, 16)
stages = [
    dict(text="Sporophyte (2n)", draw=draw_fern, icon_size=2.2, bold=True),
    dict(text="Sori and sporangia", draw=draw_sorus, icon_size=1.5),
    dict(text="Spores (n), 64 per sporangium", draw=draw_spores, icon_size=1.0),
    dict(text="Filament and plate", draw=draw_filament, icon_size=1.2),
    dict(text="Prothallus (n)", draw=draw_gametophyte, icon_size=1.6, bold=True),
    dict(text="Egg in archegonium,\nmultiflagellate sperm", draw=draw_gametes, icon_size=1.0),
    dict(text="Embryo and young\nsporophyte on the prothallus", draw=draw_young, icon_size=1.6),
]
plant.alternation_of_generations(ax, (9.0, 8.0), 5.4, stages, meiosis=1, fertilization=5, gap=0.25,
                                 arrow_labels=[None, None, "Germination", "Growth", "Gametangia", None, "Growth"])
