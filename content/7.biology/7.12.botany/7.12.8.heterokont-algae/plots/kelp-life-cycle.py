"""Life cycle of kelp (Saccharina japonica), heteromorphic alternation of generations. The large diploid
sporophyte (holdfast, stipe, blade) forms sori of unilocular sporangia; meiosis gives 32 zoospores, which grow
into microscopic male and female gametophytes; the egg stays on the oogonium, is fertilized there and the
zygote grows into a young sporophyte. Blue sector: diploid phase; orange sector: haploid phase."""
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(24, 15)
stages = [
    dict(text="Sporophyte (2n)\nholdfast, stipe, blade\n2-4 m", size="small", bold=True, token="dna"),
    dict(text="Sorus: unilocular\nsporangia + paraphyses", size="small"),
    dict(text="Zoospores (n)\n32 per sporangium", size="small"),
    dict(text="Male gametophyte (n)\nbranched filament,\n1 sperm per cell", size="small", token="highlight"),
    dict(text="Female gametophyte (n)\nfew large cells,\noogonia", size="small", token="highlight"),
    dict(text="Egg on the oogonium\nfertilized by sperm", size="small"),
    dict(text="Zygote (2n)\nyoung sporophyte", size="small"),
]
plant.alternation_of_generations(ax, (13.0, 7.5), 5.2, stages, meiosis=1, fertilization=5, gap=0.2,
                                 arrow_labels=[None, None, "Settle and\ngerminate", "Sperm", None, None, "Growth"])
import numpy as np
from matplotlib.patches import Rectangle
kx, ky = 2.6, 3.2
for a in (-60, -35, -15, 15, 35, 60):
    r = np.radians(a - 90)
    ax.plot([kx, kx + 1.0 * np.cos(r)], [ky, ky + 0.7 * np.sin(r)], color=P.edge("plant"), lw=2.2, solid_capstyle="round")
ax.add_patch(Rectangle((kx - 0.13, ky), 0.26, 1.6, facecolor=P.fill("plant"), edgecolor=P.edge("plant"), lw=1.0))
t = np.linspace(0, 1, 80)
w = 0.85 * np.sin(np.pi * t) ** 0.5
ax.fill(np.r_[kx + w, (kx - w)[::-1]], np.r_[ky + 1.6 + 8.0 * t, (ky + 1.6 + 8.0 * t)[::-1]],
        facecolor=P.light("plant"), edgecolor=P.edge("plant"), lw=1.2)
ax.fill(np.r_[kx + 0.55 * w[20:60], (kx - 0.55 * w[20:60])[::-1]], np.r_[ky + 1.6 + 8.0 * t[20:60], (ky + 1.6 + 8.0 * t[20:60])[::-1]],
        facecolor=P.fill("highlight"), edgecolor="none")
bio.callout(ax, (kx + 0.4, ky + 6.0), (4.6, 12.0), "sorus", size="tiny")
bio.callout(ax, (kx + 0.7, ky + 3.0), (4.6, 4.8), "blade", size="tiny")
bio.callout(ax, (kx + 0.1, ky + 0.9), (4.6, 3.4), "stipe", size="tiny")
bio.callout(ax, (kx + 0.8, ky - 0.5), (4.6, 2.0), "holdfast", size="tiny")
