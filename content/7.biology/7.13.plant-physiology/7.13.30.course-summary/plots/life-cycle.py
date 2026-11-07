# From seed to seed: the developmental programme of an annual seed plant as a schematic time course
# (illustrative curves, not data); phase labels are spread evenly above and joined to their bands. Seed reserves fall after germination; shoot dry mass follows a
# logistic growth curve (Eq. 17.9); green leaf area rises and then falls in senescence; grain dry mass
# follows a later logistic filling curve (Eq. 23.3) fed partly by remobilized leaf nitrogen and carbon.
# Coloured bands mark the phases; the row above lists the decision taken in each phase and the cue
# and hormone balance that control it.
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
t = np.linspace(0, 150, 600)


def logistic(t, K, r, tm):
    return K / (1 + np.exp(-r * (t - tm)))


reserve = 1 - logistic(t, 1, 0.45, 9)
shoot = logistic(t, 1, 0.075, 62)
leaf = logistic(t, 1, 0.12, 45) * (1 - logistic(t, 1, 0.14, 118))
grain = logistic(t, 0.48, 0.16, 118)

fig, ax = bio.canvas(30.0, 15.0)
pa = charts.axes_at(ax, (2.0, 1.6, 27.0, 8.2))

PHASES = [  # start, end, token, name, decision, cues
    (0, 6, "neutral", "Seed", "dormant or not?", "ABA/GA, DOG1; light (phyB),\ncold, nitrate, smoke"),
    (6, 16, "chloroplast", "Germination &\nestablishment", "emerge, de-etiolate", "imbibition; phy, cry;\nethylene, GA, BR"),
    (16, 62, "plant", "Vegetative\ngrowth", "juvenile → adult;\nbranching", "miR156/SPL; auxin, CK,\nstrigolactone; nutrients"),
    (62, 82, "highlight", "Floral\ninduction", "flower now?", "photoperiod (CO → FT),\nvernalization (FLC), GA"),
    (82, 100, "petal", "Flowering &\nfertilization", "accept pollen?", "self-incompatibility;\npollen-tube guidance"),
    (100, 135, "ovary", "Seed & fruit\ndevelopment", "fill, mature, ripen", "sink strength; ABA, LEA;\nethylene switch (fruit)"),
    (135, 150, "negative", "Senescence", "recycle, die", "ethylene, ABA, JA;\nN remobilization"),
]
EDGES = np.array([p[0] for p in PHASES] + [PHASES[-1][1]], float)


def U(x):
    return x


for t0, t1, tok, name, dec, cue in PHASES:
    pa.axvspan(U(t0), U(t1), color=P.mix(P.fill(tok), P.surface(), 0.78 if not P.is_dark() else 0.82), lw=0, zorder=0)
    k = [q[0] for q in PHASES].index(t0)
    X = 2.0 + 27.0 * (k + 0.5) / len(PHASES)
    ax.plot([X, 2.0 + 27.0 * (t0 + t1) / 2 / 150], [10.75, 9.85], color=P.muted(), lw=0.6)
    bio.label(ax, (X, 14.3), name, size="small", bold=True, va="top")
    bio.label(ax, (X, 12.6), dec, size="tiny", va="top", italic=True)
    bio.label(ax, (X, 11.5), cue, size="tiny", va="top", color=P.muted())

pa.plot(U(t), reserve, color=charts.line("atp"), lw=2, ls="--", label="seed reserves")
pa.plot(U(t), shoot, color=charts.line("dna"), lw=2.4, label="shoot dry mass (logistic)")
pa.plot(U(t), leaf, color=charts.line("chloroplast"), lw=2.0, label="green leaf area")
pa.plot(U(t), grain, color=charts.line("rna"), lw=2.4, label="grain dry mass")
pa.annotate("", xy=(U(126), 0.36), xytext=(U(121), 0.62),
            arrowprops=dict(arrowstyle="->", color=P.muted(), lw=1.0, connectionstyle="arc3,rad=-0.3"))
pa.text(U(121), 0.66, "remobilization", fontsize=8, color=P.muted(), ha="center")
for x, txt in ((6, "radicle emerges"), (62, "floral transition"), (90, "double fertilization")):
    pa.axvline(U(x), color=P.muted(), lw=0.8, ls=":")
    pa.text(U(x) + 0.8, 1.06, txt, fontsize=7.5, color=P.muted(), ha="left", va="bottom")
pa.set_xlim(0, 150)
pa.set_ylim(0, 1.15)
pa.set_yticks([0, 0.5, 1])
pa.legend(frameon=False, fontsize=8, loc="center left", bbox_to_anchor=(0.12, 0.62), labelcolor=P.ink())
charts.style_axes(pa, "Days after sowing (schematic)", "Relative amount")
