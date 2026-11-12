# The 19 pairs of appendages of a crayfish (Malacostraca: Astacidea), from head to tail, drawn as schematic
# left limbs (not to scale) and coloured by function. Head: first antennae (antennules: two flagella,
# statocyst at the base), second antennae (long flagellum and a scale, the exopod), mandibles (with palp),
# first maxillae (maxillules), second maxillae (with the scaphognathite, which bails water through the
# gill chamber). Thorax: three maxillipeds, the cheliped and four walking legs (pereiopods 2-3 with small
# chelae). Abdomen: five pleopods (in males the first two are gonopods) and the uropods, which with the
# telson form the tail fan. All are serial homologues of one biramous limb.
import numpy as np
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(29, 10.6)
FUN = {"sense": "receptor", "feed": "enzyme", "vent": "chloroplast", "walk": "protein", "swim": "dna",
       "sex": "atp", "tail": "rna"}


def line(pts, tok, lw=2.2):
    pts = np.asarray(pts, float)
    ax.plot(pts[:, 0], pts[:, 1], color=P.edge(tok), lw=lw, solid_capstyle="round", zorder=6)


def blob(c, w, h, tok, ang=0):
    from matplotlib.patches import Ellipse
    ax.add_patch(Ellipse(c, w, h, angle=ang, facecolor=P.fill(tok), edgecolor=P.edge(tok), lw=0.8, zorder=7))


def limb(x, kind, tok):
    y = 7.6  # attachment
    blob((x, y), 0.45, 0.55, "neutral")                     # protopod
    if kind == "antennule":
        line([(x, y - 0.2), (x + 0.1, y - 1.0)], tok)
        line([(x + 0.1, y - 1.0), (x - 0.3, y - 3.6)], tok, 1.2)
        line([(x + 0.1, y - 1.0), (x + 0.4, y - 3.2)], tok, 1.2)
    elif kind == "antenna":
        line([(x, y - 0.2), (x, y - 1.0)], tok)
        line([(x, y - 1.0), (x - 0.15, y - 5.0)], tok, 1.0)
        blob((x + 0.35, y - 1.4), 0.32, 1.3, tok, 10)
    elif kind == "mandible":
        blob((x, y - 0.8), 0.7, 0.7, tok)
        line([(x + 0.2, y - 1.1), (x + 0.3, y - 2.0)], tok, 1.4)
    elif kind == "maxillule":
        blob((x - 0.1, y - 0.9), 0.35, 0.9, tok)
        blob((x + 0.2, y - 1.0), 0.3, 0.7, tok)
    elif kind == "maxilla":
        blob((x - 0.1, y - 0.9), 0.35, 0.9, tok)
        blob((x + 0.3, y - 1.2), 0.45, 1.4, FUN["vent"])
    elif kind.startswith("mxp"):
        n = int(kind[-1])
        line([(x, y - 0.2), (x - 0.1, y - 1.0 - 0.6 * n)], tok)
        line([(x + 0.1, y - 0.4), (x + 0.4, y - 1.3 - 0.3 * n)], tok, 1.2)
    elif kind in ("cheliped", "chela", "leg"):
        L = 3.2 if kind == "cheliped" else 2.6
        pts = [(x, y - 0.2), (x + 0.1, y - 0.6), (x - 0.05, y - 1.5), (x + 0.05, y - 2.1), (x, y - L)]
        line(pts, tok, 2.6 if kind == "cheliped" else 2.0)
        if kind == "cheliped":
            blob((x, y - L - 0.35), 0.55, 1.0, tok)
            line([(x + 0.12, y - L - 0.8), (x + 0.12, y - L - 1.2)], tok, 2.0)
        elif kind == "chela":
            line([(x, y - L), (x - 0.12, y - L - 0.35)], tok, 1.4)
            line([(x, y - L), (x + 0.12, y - L - 0.35)], tok, 1.4)
    elif kind in ("pleopod", "gonopod"):
        line([(x, y - 0.2), (x, y - 1.0)], tok)
        if kind == "gonopod":
            line([(x, y - 1.0), (x + 0.15, y - 2.4)], tok, 2.4)
        else:
            for dx in (-0.18, 0.18):
                blob((x + dx, y - 1.8), 0.25, 1.3, tok)
    elif kind == "uropod":
        line([(x, y - 0.2), (x, y - 0.8)], tok)
        blob((x - 0.25, y - 1.8), 0.5, 1.7, tok, 10)
        blob((x + 0.3, y - 1.8), 0.55, 1.8, tok, -10)


spec = [("antennule", "sense", "Antennule"), ("antenna", "sense", "Antenna"), ("mandible", "feed", "Mandible"),
        ("maxillule", "feed", "Maxillule"), ("maxilla", "feed", "Maxilla"),
        ("mxp1", "feed", "Maxilliped 1"), ("mxp2", "feed", "Maxilliped 2"), ("mxp3", "feed", "Maxilliped 3"),
        ("cheliped", "walk", "Cheliped"), ("chela", "walk", "Pereiopod 2"), ("chela", "walk", "Pereiopod 3"),
        ("leg", "walk", "Pereiopod 4"), ("leg", "walk", "Pereiopod 5"),
        ("gonopod", "sex", "Pleopod 1"), ("gonopod", "sex", "Pleopod 2"), ("pleopod", "swim", "Pleopod 3"),
        ("pleopod", "swim", "Pleopod 4"), ("pleopod", "swim", "Pleopod 5"), ("uropod", "tail", "Uropod")]
xs = 1.0 + np.arange(19) * 1.45
for x, (kind, fn, name) in zip(xs, spec):
    limb(x, kind, FUN[fn])
    bio.label(ax, (x, 8.55), name, size="tiny", rotation=50, ha="left", va="bottom")
# segment brackets
for a, b, txt in ((0, 4, "Head (cephalon)"), (5, 12, "Thorax (pereon)"), (13, 18, "Abdomen (pleon)")):
    ax.plot([xs[a] - 0.4, xs[b] + 0.4], [1.3, 1.3], color=P.muted(), lw=1.0)
    bio.label(ax, ((xs[a] + xs[b]) / 2, 0.9), txt, size="small", color=P.muted())
for k, (fn, txt) in enumerate((("sense", "sensory"), ("feed", "feeding"), ("vent", "gill ventilation"), ("walk", "grasping, walking"),
                                ("sex", "sperm transfer (male)"), ("swim", "swimming, brooding eggs"), ("tail", "tail fan, escape"))):
    bio.box(ax, (1.0 + k * 3.9, 0.3), 0.4, 0.28, FUN[fn])
    bio.label(ax, (1.35 + k * 3.9, 0.3), txt, size="tiny", ha="left")
