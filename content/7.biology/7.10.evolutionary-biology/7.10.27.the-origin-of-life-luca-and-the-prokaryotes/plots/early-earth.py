"""Timeline of the first two billion years of Earth history (Ga): ICS eons with events from the text:
solar system 4.567, zircons ~4.4, oldest rocks ~4.0, disputed evidence of life 3.8-3.5 (open circles),
stromatolites 3.43, Great Oxidation Event ~2.4, earliest eukaryote fossils ~1.65."""
import wikibio as bio
from wikibio import phylo

P = bio.P
fig, ax = bio.canvas(26, 8)
x0, x1 = 1.0, 25.0
a0, a1 = 4600, 1600


def X(ga):
    return x0 + (a0 - ga * 1000) / (a0 - a1) * (x1 - x0)


phylo.geo_scale(ax, (x0, x1), (a0, a1), 3.6, ranks=("eon", "era"), height=0.55)
for ga in (4.5, 4.0, 3.5, 3.0, 2.5, 2.0):
    ax.plot([X(ga), X(ga)], [2.5, 2.35], color=P.muted(), lw=0.7)
    bio.label(ax, (X(ga), 2.05), f"{ga:.1f}", size="tiny", color=P.muted())
bio.label(ax, (13.0, 1.4), "billions of years ago (Ga)", size="small", color=P.muted())
EVENTS = [(4.567, "solar system\nforms", 1, True), (4.4, "oldest zircons:\nliquid water?", 3, True),
          (4.0, "oldest rocks\n(Acasta gneiss)", 1, True), (3.75, "isotopic evidence\nof life (disputed)", 2, False),
          (3.465, "Apex chert\n'microfossils' (disputed)", 3.3, False), (3.43, "Strelley Pool\nstromatolites", 1.2, True),
          (2.4, "Great Oxidation\nEvent", 1.6, True), (1.65, "earliest eukaryote\nfossils", 1, True)]
for ga, text, lev, solid in EVENTS:
    x = X(ga)
    yb = 3.7
    yt = yb + 0.9 * lev
    ax.plot([x, x], [yb, yt - 0.1], color=P.muted(), lw=0.7)
    ax.plot([x], [yb], "o", ms=5, color=P.ink() if solid else P.surface(), markeredgecolor=P.ink(), zorder=12)
    bio.label(ax, (x, yt), text, size="tiny", va="bottom")
