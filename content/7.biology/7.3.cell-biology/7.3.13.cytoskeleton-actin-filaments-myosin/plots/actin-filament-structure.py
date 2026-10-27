"""Structure and polarity of the actin filament (schematic).

Top: a filament from its minus (pointed) end on the left to its plus (barbed) end on the right, decorated
with myosin heads that form arrowheads pointing to the minus end; subunits are coloured by bound nucleotide:
ATP near the growing plus end, ADP-Pi behind it and ADP in the older part. Bottom left: an Arp2/3 branch.
Bottom right: legend.
"""

import wikibio as bio
from wikibio import cytoskel as C

P = bio.P
fig, ax = bio.canvas(20.0, 5.6)
C.actin_filament(ax, (0.8, 4.3), (19.2, 4.3), r=0.17, states="DDDDDDPPPTT", decorate=True)
bio.label(ax, (0.8, 5.25), "pointed (minus) end", size="small", ha="left")
bio.label(ax, (19.2, 5.25), "barbed (plus) end", size="small", ha="right")
bio.label(ax, (10.0, 5.25), "myosin S1 arrowheads point to the minus end", size="tiny", color=P.muted())
C.branch(ax, (0.8, 1.1), (10.5, 1.1), at=0.4, length=2.0, detailed=True, r=0.12, states="DDPT")
bio.callout(ax, (4.75, 1.25), (6.6, 2.8), "Arp2/3 complex: 70° branch", size="tiny")
C.nucleotide_legend(ax, (12.5, 1.2), kind="actin", step=2.2)
