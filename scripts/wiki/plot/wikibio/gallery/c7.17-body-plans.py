# Animal body plans in cross-section, coloured by germ layer (ectoderm blue, mesoderm red, endoderm yellow).
# Diploblastic cnidarians have two epithelia separated by the acellular mesoglea. Triploblastic bilaterians
# add mesoderm: in acoelomate flatworms it fills the space between gut and body wall; in pseudocoelomate
# nematodes it lines only the body wall, leaving a fluid-filled pseudocoel; in coelomate annelids it lines
# both body wall (somatic) and gut (splanchnic), enclosing the coelom. These are grades of organization,
# not clades: body cavities were gained and lost repeatedly (see the animal phylogeny).
import wikibio as bio
from wikibio import zoology as zoo

P = bio.P
fig, ax = bio.canvas(26, 11.6)

COLS = [
    dict(kind="diploblast", title="Diploblastic", sub="two germ layers", x=3.3,
         icon="phylopic/hydra", example="Cnidaria", genus="Hydra", cavity="No body cavity"),
    dict(kind="acoelomate", title="Acoelomate", sub="triploblastic, no body cavity", x=9.8,
         icon="phylopic/planarian", icon_w=1.6, example="Platyhelminthes", genus="Schmidtea", cavity="Solid mesoderm (parenchyma)"),
    dict(kind="pseudocoelomate", title="Pseudocoelomate", sub="cavity not lined by mesoderm", x=16.3,
         icon="phylopic/c-elegans", icon_h=1.6, rotate=75, example="Nematoda", genus="Caenorhabditis", cavity="Pseudocoel = blastocoel"),
    dict(kind="coelomate", title="Coelomate", sub="cavity lined by mesoderm", x=22.8,
         icon="phylopic/earthworm", icon_w=1.5, example="Annelida", genus="Lumbricus", cavity="Coelom within mesoderm"),
]
Y, R = 6.15, 2.25
for c in COLS:
    x = c["x"]
    bio.label(ax, (x, 11.15), c["title"], size="title", bold=True)
    bio.label(ax, (x, 10.6), c["sub"], size="small", color=P.muted())
    a = zoo.body_plan(ax, (x, Y), R, c["kind"])
    k = c["kind"]
    if k == "diploblast":
        bio.label(ax, (x, Y), "Gastrovascular\ncavity", size="tiny")
        bio.callout(ax, (x + 0.75 * R * 0.94, Y + 0.75 * R * 0.34), (x + 1.75, Y + 2.35), "Mesoglea", size="tiny")
    elif k == "acoelomate":
        bio.label(ax, (x, Y), "Gut", size="tiny")
        bio.label(ax, (x - 1.45, Y), "Mesoderm", size="tiny", color=P.on_fill())
    elif k == "pseudocoelomate":
        bio.label(ax, (x, Y), "Gut", size="tiny")
        bio.label(ax, (x, Y + 1.19), "Pseudocoel", size="tiny")
        bio.callout(ax, a["cuticle"], (x - 1.7, Y + 2.35), "Cuticle", size="tiny")
    else:
        bio.label(ax, (x, Y), "Gut", size="tiny")
        for s in (-1, 1):
            bio.label(ax, (x + s * 1.3, Y), "Coelom", size="tiny")
        bio.callout(ax, (x + 0.02, Y + 1.15), (x + 1.75, Y + 2.35), "Mesentery", size="tiny")
        bio.callout(ax, (x - 0.86, Y - 0.24), (x - 1.75, Y - 2.4), "Splanchnic", size="tiny")
        bio.callout(ax, (x + 0.7 * 0.8 * R, Y - 0.7 * 0.8 * R), (x + 1.75, Y - 2.4), "Somatic", size="tiny")
    bio.label(ax, (x, Y - R - 0.45), c["cavity"], size="small", va="top")
    if "icon_w" in c:  # long, low silhouettes: fit by width
        bio.icon(ax, c["icon"], at=(x - 1.25, 2.15), width=c["icon_w"], color="animal")
    else:
        bio.icon(ax, c["icon"], at=(x - 0.9, 2.15), height=c.get("icon_h", 0.95), rotate=c.get("rotate", 0), color="animal")
    bio.label(ax, (x - 0.15, 2.35), c["example"], size="small", ha="left", bold=True)
    bio.label(ax, (x - 0.15, 1.9), f"e.g. {c['genus']}", size="tiny", ha="left", italic=True, color=P.muted())

# bracket: triploblastic grades
ax.plot([7.0, 7.0, 25.6, 25.6], [10.15, 10.0, 10.0, 10.15], color=P.muted(), lw=0.9)
bio.label(ax, (16.3, 9.75), "Bilateria: mesoderm (triploblasty)", size="tiny", color=P.muted(), va="top")
zoo.germ_layer_legend(ax, (3.0, 0.6), cavities=("pseudocoel", "coelom"), step=3.4)
