# Representatives of the antliophoran orders and of the main groups of Diptera (PhyloPic silhouettes,
# not to scale), with field characters and approximate numbers of described species.
import wikibio as bio
from wikibio.icons import size as icon_size

P = bio.P
CELLS = [
    ("Mecoptera", "hangingflies", "~270", "enzyme", "phylopic/hangingfly", "raptorial tarsi;\nnuptial prey gifts"),
    ("Siphonaptera", "fleas", "~2,600", "negative", "phylopic/flea", "wingless; laterally\ncompressed; jumping"),
    ("Diptera", "crane flies", "~15,000", "protein", "phylopic/crane-fly", "long legs; V-shaped\nmesonotal suture"),
    ("Diptera", "mosquitoes", "~3,700", "protein", "phylopic/mosquito", "long proboscis; scaled\nwing veins"),
    ("Diptera", "horse flies", "~4,500", "protein", "phylopic/horse-fly", "large eyes; blade-like\nmandibles in females"),
    ("Diptera", "hover flies", "~6,000", "protein", "phylopic/hoverfly", "vena spuria; wasp and\nbee mimics"),
    ("Diptera", "fruit flies", "~4,000", "protein", "phylopic/drosophila", "arista plumose;\nbroken costa"),
    ("Diptera", "house flies", "~5,000", "protein", "phylopic/housefly", "calypters; sponging\nlabella"),
]
NC, CW, CH = 4, 5.6, 5.4
NR = (len(CELLS) + NC - 1) // NC
W, H = NC * CW, NR * CH + 1.6
fig, ax = bio.canvas(W, H)
for i, (order, common, n, tok, icon, chars) in enumerate(CELLS):
    c, r = i % NC, i // NC
    x0, y0 = c * CW, H - 1.6 - (r + 1) * CH
    bio.label(ax, (x0 + CW / 2, y0 + CH - 0.35), order, size="normal", bold=True)
    bio.label(ax, (x0 + CW / 2, y0 + CH - 0.85), f"{common} ({n} spp.)", size="tiny", color=P.muted())
    iw, ih = icon_size(icon)
    w = min(CW - 1.2, 2.6 * iw / ih)
    bio.icon(ax, icon, at=(x0 + CW / 2, y0 + 2.75), width=w, color=tok)
    bio.label(ax, (x0 + CW / 2, y0 + 0.75), chars, size="tiny")
bio.label(ax, (W - 0.3, H - 0.8), "Silhouettes not to scale", size="tiny", color=P.muted(), ha="right")
