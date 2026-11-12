# Antennae of Diptera (schematic, drawn with wikibio.zoomorph.antenna; scape, pedicel and flagellum
# coloured). The many-segmented antennae of the nematoceran grade (crane flies, mosquitoes, March flies)
# contrast with the short antennae of Brachycera, whose flagellum is reduced to a compact first
# flagellomere with an annulated tip (horse flies), a terminal stylus (robber flies) or a dorsal arista
# (Cyclorrhapha: house flies, fruit flies).
import wikibio as bio
from wikibio import zoomorph as zm

P = bio.P
ANT = [("Tipulidae", "crane flies", "filiform", 4.4, "many flagellomeres"),
       ("Culicidae (male)", "mosquitoes", "plumose", 3.6, "whorls of long setae"),
       ("Bibionidae", "March flies", "moniliform", 2.0, "short, bead-like"),
       ("Tabanidae", "horse flies", "setaceous", 2.4, "flagellum annulated"),
       ("Asilidae", "robber flies", "setaceous", 2.0, "terminal stylus"),
       ("Muscidae", "house flies", "aristate", 1.8, "dorsal arista")]
W = 3.6
fig, ax = bio.canvas(W * len(ANT), 9.0)
for i, (fam, common, kind, L, note) in enumerate(ANT):
    x = i * W + W / 2
    zm.antenna(ax, (x - 0.2, 2.2), 80, L, kind, colored=True)
    bio.label(ax, (x, 8.5), fam, size="small", bold=True)
    bio.label(ax, (x, 8.0), common, size="tiny", color=P.muted())
    bio.label(ax, (x, 1.4), note, size="tiny")
for x0, x1, t, tok in ((0.2, 3 * W - 0.2, "Nematocera (grade): antennae long, many segments", "neutral"),
                       (3 * W + 0.2, 6 * W - 0.2, "Brachycera: antennae short", "positive")):
    ax.plot([x0, x1], [0.7, 0.7], color=P.edge(tok), lw=2.0)
    bio.label(ax, ((x0 + x1) / 2, 0.3), t, size="tiny")
