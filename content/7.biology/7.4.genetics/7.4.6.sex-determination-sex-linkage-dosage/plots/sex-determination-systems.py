"""A gallery of sex-determining systems: female and male chromosome constitutions (or the environmental
cue) with an example organism."""
import wikibio as bio
from wikibio import genetics as G

P = bio.P
fig, ax = bio.canvas(19.0, 13.2)
X, Y = "receptor", "dna"
rows = [
    ("XX / XY (male heterogametic)", [[X, X]], [[X, (Y, 0.45)]], "humans: Y ($\\it{SRY}$) makes males\n$\\it{Drosophila}$: X number decides"),
    ("XX / XO", [[X, X]], [[X]], "$\\it{C.\\ elegans}$ (XX hermaphrodites),\ngrasshoppers"),
    ("ZW / ZZ (female heterogametic)", [["chloroplast", ("enzyme", 0.45)]], [["chloroplast", "chloroplast"]], "birds, butterflies and moths"),
    ("haplodiploidy", [["protein", "protein"]], [["protein"]], "bees, ants, wasps: diploid females,\nhaploid males from unfertilized eggs"),
    ("temperature-dependent", None, None, "many turtles: warm eggs female;\ncrocodilians: extremes female"),
]
bio.label(ax, (6.2, 12.7), "female", size="small", bold=True)
bio.label(ax, (9.2, 12.7), "male", size="small", bold=True)
for i, (name, fem, mal, note) in enumerate(rows):
    y = 11.3 - i * 2.45
    bio.label(ax, (0.3, y), name, size="small", ha="left")
    for x0, sets in ((6.2, fem), (9.2, mal)):
        if sets is None:
            continue
        chroms = sets[0]
        n = len(chroms)
        for k, c in enumerate(chroms):
            tok, L = (c, 1.4) if isinstance(c, str) else (c[0], 1.4 * c[1])
            G.chromosome(ax, (x0 + (k - (n - 1) / 2) * 0.6, y), length=L, centromere=0.35, width=0.38, token=tok,
                         anchor="center")
    if i == 4:
        bio.label(ax, (6.2, y), "warm", size="small", color=P.edge("negative"))
        bio.label(ax, (9.2, y), "cool", size="small", color=P.edge("dna"))
    bio.label(ax, (13.4, y + 0.0), note, size="tiny", ha="left")
bio.icon(ax, "phylopic/human", at=(11.9, 11.3), height=1.3, color="animal")
bio.icon(ax, "phylopic/c-elegans", at=(11.9, 8.85), height=0.8, color="animal")
bio.icon(ax, "phylopic/chicken", at=(11.9, 6.4), height=1.2, color="animal")
bio.icon(ax, "phylopic/honey-bee", at=(11.9, 3.95), height=1.0, color="highlight")
bio.icon(ax, "phylopic/turtle", at=(11.9, 1.5), height=0.9, color="plant")
for xx, t in ((6.2, "X X"), (9.2, "X Y")):
    pass
bio.label(ax, (6.2, 10.2), "XX", size="tiny", color=P.muted())
bio.label(ax, (9.2, 10.2), "XY", size="tiny", color=P.muted())
bio.label(ax, (6.2, 7.75), "XX", size="tiny", color=P.muted())
bio.label(ax, (9.2, 7.75), "XO", size="tiny", color=P.muted())
bio.label(ax, (6.2, 5.3), "ZW", size="tiny", color=P.muted())
bio.label(ax, (9.2, 5.3), "ZZ", size="tiny", color=P.muted())
bio.label(ax, (6.2, 2.85), "2n", size="tiny", color=P.muted())
bio.label(ax, (9.2, 2.85), "n", size="tiny", color=P.muted())
