# Life cycle of the Chinese mitten crab Eriocheir sinensis (catadromous migration between rivers and the estuary).
# The shaded band marks the part of the cycle that needs brackish or sea water.
import wikibio as bio
from wikibio import ecology as eco

P = bio.P
fig, ax = bio.canvas(18, 13.2)

bio.label(ax, (9.0, 12.8), "Eriocheir sinensis", size="title", bold=True, italic=True)
eco.cycle(ax, (9.0, 6.3), 4.5, [
    dict(text="Adults in rivers and lakes\n(1.5-2 years of growth)", icon="phylopic/crab", icon_size=1.6, token="animal", bold=True),
    dict(text="Autumn: maturity molt;\nmigration downstream", token="neutral"),
    dict(text="Winter: mating in the estuary;\nfemale broods eggs on pleopods", token="neutral"),
    dict(text="Spring: zoea larvae\n(5 stages, about 1 month)", token="neutral"),
    dict(text="Megalopa", token="neutral"),
    dict(text="Juvenile crabs migrate\nupstream", token="neutral"),
], start=90, arrow_labels=["", "", "Hatching", "", "Metamorphosis", ""],
    sectors=[dict(start=1.6, end=4.4, token="dna", r0=2.6, r1=5.9, text="Brackish water")], size="small")
bio.label(ax, (9.0, 6.3), "Fresh water:\ngrowth", size="small", color=P.muted())
