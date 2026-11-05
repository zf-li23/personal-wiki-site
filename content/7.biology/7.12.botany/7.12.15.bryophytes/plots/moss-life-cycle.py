"""Life cycle of a moss (Funaria type) on a circle; blue sector diploid (2n), orange sector haploid (n).
The sporophyte (foot, seta, capsule) grows on the leafy gametophyte; meiosis in the capsule gives spores;
a spore grows into a filamentous protonema, which forms buds and leafy gametophores; antheridia (sperm)
and archegonia (egg) at shoot tips; sperm swim to the egg; the zygote develops into an embryo in the
archegonium and grows into a new sporophyte."""
import numpy as np
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(26, 22)


def d_spores(ax, xy, s):
    for dx, dy in ((-0.35, 0.2), (0.3, 0.3), (0.0, -0.25), (0.45, -0.3), (-0.4, -0.35)):
        t = np.linspace(0, 2 * np.pi, 24)
        bio.shape(ax, np.c_[xy[0] + dx + 0.16 * np.cos(t), xy[1] + dy + 0.16 * np.sin(t)], token="lipid", lw=0.8, zorder=12)


def d_zygote(ax, xy, s):
    x, y = xy
    t = np.linspace(0, 2 * np.pi, 60)
    # archegonium venter with embryo
    bio.shape(ax, np.c_[x + 0.45 * np.cos(t), y - 0.2 + 0.6 * np.sin(t)], token="receptor", lw=0.9, zorder=11)
    bio.shape(ax, [[x - 0.12, y + 0.3], [x + 0.12, y + 0.3], [x + 0.1, y + 1.1], [x - 0.1, y + 1.1]], token="receptor", lw=0.8,
              zorder=11)
    bio.shape(ax, np.c_[x + 0.2 * np.cos(t), y - 0.25 + 0.35 * np.sin(t)], token="dna", lw=0.8, zorder=12)


stages = [
    dict(text="Sporophyte on the gametophyte", icon="wikimedia/moss-gametophyte-sporophyte", icon_size=3.4, size="small", bold=True),
    dict(text="Capsule (2n)", icon="wikimedia/moss-capsule", icon_size=2.0, size="small"),
    dict(text="Spores (n)", draw=d_spores, icon_size=1.2, size="small"),
    dict(text="Protonema", icon="wikimedia/moss-protonema", icon_size=2.0, size="small"),
    dict(text="Leafy gametophore (n)", icon="bioicons/moss-gametophore", icon_size=2.6, size="small", bold=True),
    dict(text="Antheridial head: sperm", icon="wikimedia/moss-antheridial-head", icon_size=2.0, size="small"),
    dict(text="Archegonial head: egg", icon="wikimedia/moss-archegonial-head", icon_size=2.0, size="small"),
    dict(text="Zygote, embryo in the\narchegonium (2n)", draw=d_zygote, icon_size=1.6, size="small"),
]
plant.alternation_of_generations(ax, (13.0, 10.6), 7.2, stages, meiosis=1, fertilization=6, gap=0.25, start=110,
                                 arrow_labels=[None, None, "Germination", "Buds", None, "Sperm swim\nin water", None, "Growth"])
bio.label(ax, (13.0, 21.4), "Life cycle of a moss", size="normal", bold=True)
