# Homology of the tetrapod forelimb: the same bones in the same order (humerus; radius and ulna;
# carpals; metacarpals; phalanges), each coloured identically, adapted to different functions
# (wikibio.zoomorph.forelimb; shoulder at the top, radius and digit I on the left; not to scale). Human:
# five digits, the generalized pattern. Cat: digitigrade, digit I (dewclaw) short, claws. Toothed whale:
# short, flattened bones in a flipper, extra phalanges in digits II and III (hyperphalangy). Horse: the
# ulna reduced and fused to the radius, a single functional digit III on the cannon bone, the
# metacarpals of II and IV reduced to splints, the distal phalanx in the hoof. Bat: radius and the
# metacarpals and phalanges of II-V greatly elongated to span the wing membrane (patagium); the clawed
# thumb free; the ulna reduced. Bird: stout ulna, thin radius, two free carpals, a carpometacarpus of
# fused carpals and metacarpals bearing the alular, major and minor digits (their identity as I-II-III or
# II-III-IV is debated). Below: relationships (Laurasiatheria; branching within Fereuungulata unresolved).
# Similar function with different structure (bat and bird wings) is convergence on a homologous limb.
import wikibio as bio
from wikibio import phylo
from wikibio import zoomorph as zm

P = bio.P
fig, ax = bio.canvas(30, 16.6)
TAXA = [("bird", "Bird", "flight (feathers)"), ("human", "Human", "manipulation"), ("bat", "Bat", "flight (membrane)"),
        ("cat", "Cat", "running, prey capture"), ("horse", "Horse", "running (unguligrade)"), ("whale", "Toothed whale", "swimming")]
X = {t: 2.6 + 4.95 * i for i, (t, _, _) in enumerate(TAXA)}
YL = 10.3
A = {}
for t, name, func in TAXA:
    A[t] = zm.forelimb(ax, (X[t], YL), 9.4 if t != "whale" else 7.2, t, width=4.1)
    bio.label(ax, (X[t], 4.55), name, size="normal", bold=True)
    bio.label(ax, (X[t], 4.1), func, size="tiny", color=P.muted())

h = A["human"]
for d in ("I", "II", "III", "IV", "V"):
    x, y = h["digits"][d]
    bio.label(ax, (x, y - 0.3), d, size="tiny", va="top")
b = A["bird"]
bio.callout(ax, b["metacarpals"], (X["bird"] + 1.5, b["metacarpals"][1] - 0.4), "Carpo-\nmetacarpus", size="tiny")
bio.callout(ax, b["digits"]["alula"], (X["bird"] - 1.7, b["digits"]["alula"][1] - 0.2), "Alula", size="tiny")
bt = A["bat"]
bio.callout(ax, bt["digits"]["I"], (X["bat"] - 1.9, bt["digits"]["I"][1] + 0.6), "Clawed thumb", size="tiny")
bio.callout(ax, bt["skin"], (X["bat"] + 1.8, bt["skin"][1] + 1.6), "Patagium", size="tiny")
bio.callout(ax, bt["ulna"], (X["bat"] + 1.6, bt["ulna"][1] + 0.8), "Reduced ulna", size="tiny")
hs = A["horse"]
bio.callout(ax, hs["metacarpals"], (X["horse"] + 1.4, hs["metacarpals"][1]), "Cannon bone (III)", size="tiny")
bio.callout(ax, (hs["metacarpals"][0] - 0.13, hs["metacarpals"][1] + 0.6), (X["horse"] - 1.6, hs["metacarpals"][1] + 1.2),
            "Splint\n(II, IV)", size="tiny")
bio.callout(ax, hs["digits"]["III"], (X["horse"] + 1.2, hs["digits"]["III"][1] - 0.1), "Hoof", size="tiny")
bio.callout(ax, hs["ulna"], (X["horse"] + 1.4, hs["ulna"][1] + 0.5), "Ulna fused", size="tiny")
w = A["whale"]
bio.callout(ax, w["phalanges"], (X["whale"] + 1.7, w["phalanges"][1] - 1.0), "Hyperphalangy", size="tiny")
c = A["cat"]
bio.callout(ax, c["digits"]["I"], (X["cat"] - 1.8, c["digits"]["I"][1] + 0.3), "Dewclaw (I)", size="tiny")

# phylogeny below the limbs (tips up)
NEWICK = "(Bird,(Human,(Bat,(Cat,Horse,Whale)Fereuungulata)Laurasiatheria)Eutheria)Amniota;"
t = phylo.tree(ax, NEWICK, origin=(X["bird"], 0.7), width=X["whale"] - X["bird"], height=2.75, direction="up", tip_labels=False,
               root_edge=0.3)
nd = t.node("Fereuungulata")
bio.label(ax, (nd.xy[0] + 0.15, nd.xy[1] - 0.05), "?", size="small", bold=True, color=P.muted(), ha="left", va="top")
for name in ("Laurasiatheria", "Eutheria", "Amniota"):
    nd = t.node(name)
    bio.label(ax, (nd.xy[0] + 0.12, nd.xy[1] - 0.08), name, size="tiny", color=P.muted(), ha="left", va="top")

# key
for k, part in enumerate(("humerus", "radius", "ulna", "carpals", "metacarpals", "phalanges")):
    x = 4.6 + k * 3.9
    tok = zm.BONE[part]
    bio.shape(ax, [(x - 0.17, 16.03), (x + 0.17, 16.03), (x + 0.17, 16.37), (x - 0.17, 16.37)], tok, lw=0.8, zorder=20)
    bio.label(ax, (x + 0.35, 16.2), part.capitalize(), size="small", ha="left")
