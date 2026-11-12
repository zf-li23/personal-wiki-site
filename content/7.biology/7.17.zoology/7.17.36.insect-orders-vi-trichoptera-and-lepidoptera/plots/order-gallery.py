# Representatives of Trichoptera and Lepidoptera (PhyloPic silhouettes, not to scale), with field characters
# and approximate numbers of described species (Morse's world Trichoptera checklist; van Nieukerken et al.
# 2011 for Lepidoptera).
import wikibio as bio
from wikibio.icons import size as icon_size

P = bio.P
CELLS = [
    ("Trichoptera", "caddisflies", "~16,000", "enzyme", "phylopic/caddisfly", "hairy wings held\nroof-like; long antennae"),
    ("Bombycidae", "silkworm moths", "~200", "protein", "phylopic/silkmoth", "pectinate antennae;\nmouthparts vestigial"),
    ("Sphingidae", "hawk moths", "~1,500", "protein", "phylopic/hawkmoth", "stout; narrow forewings;\nvery long proboscis"),
    ("Noctuoidea", "owlet and tiger moths", "~42,000", "protein", "phylopic/moth", "metathoracic ears;\nthe largest superfamily"),
    ("Papilionidae", "swallowtails", "~570", "highlight", "phylopic/swallowtail", "tailed hind wings;\nosmeterium in larva"),
    ("Nymphalidae", "brush-footed butterflies", "~6,000", "highlight", "phylopic/nymphalid", "forelegs reduced,\nbrush-like"),
]
NC, CW, CH = 6, 5.0, 5.4
W, H = NC * CW, CH + 1.6
fig, ax = bio.canvas(W, H)
for i, (grp, common, n, tok, icon, chars) in enumerate(CELLS):
    x0, y0 = i * CW, 0
    bio.label(ax, (x0 + CW / 2, y0 + CH - 0.35), grp, size="normal", bold=True)
    bio.label(ax, (x0 + CW / 2, y0 + CH - 0.85), f"{common} ({n} spp.)", size="tiny", color=P.muted())
    iw, ih = icon_size(icon)
    w = min(CW - 1.2, 2.6 * iw / ih)
    bio.icon(ax, icon, at=(x0 + CW / 2, y0 + 2.75), width=w, color=tok)
    bio.label(ax, (x0 + CW / 2, y0 + 0.75), chars, size="tiny")
for k, (name, tok) in enumerate([("Trichoptera", "enzyme"), ("moths", "protein"), ("butterflies", "highlight")]):
    x = 1.0 + k * 6.0
    bio.box(ax, (x + 0.3, H - 0.8), 0.5, 0.5, token=tok)
    bio.label(ax, (x + 0.8, H - 0.8), name, size="small", ha="left")
bio.label(ax, (W - 0.3, H - 0.8), "Silhouettes not to scale", size="tiny", color=P.muted(), ha="right")
