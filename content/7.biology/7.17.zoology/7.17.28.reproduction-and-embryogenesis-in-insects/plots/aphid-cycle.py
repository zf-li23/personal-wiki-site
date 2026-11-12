# Annual holocycle of a host-alternating aphid (schematic): overwintering fertilized egg on the woody primary
# host -> fundatrix -> parthenogenetic spring generations -> winged spring migrants -> many viviparous
# parthenogenetic generations on the herbaceous secondary host (wingless, winged when crowded) -> autumn
# gynoparae and males return to the primary host -> oviparae mate and lay eggs. Sectors mark the two hosts.
import wikibio as bio
from wikibio import ecology

P = bio.P
fig, ax = bio.canvas(22, 15)
steps = [
    dict(text="Overwintering egg", sub="fertilized, cold-hardy", token="ovule"),
    dict(text="Fundatrix", sub="wingless, parthenogenetic", token="positive"),
    dict(text="Spring generations", sub="parthenogenetic, viviparous", token="positive"),
    dict(text="Winged migrants", sub="fly to summer host", token="enzyme"),
    dict(text="Summer generations", sub="many, viviparous; winged\nwhen crowded", token="positive"),
    dict(text="Gynoparae and males", sub="winged; short days", token="enzyme"),
    dict(text="Oviparae x males", sub="sexual generation, mating", token="negative"),
]
ecology.cycle(ax, (11, 7.3), 5.2, steps, start=90, clockwise=True, size="small",
              arrow_labels=["spring", "", "", "", "autumn", "", "egg laying"],
              sectors=[dict(start=-1.5, end=2.5, token="plant"),
                       dict(start=2.5, end=5.5, token="bract")],
              center_text=None)
bio.label(ax, (11, 7.9), "Only the egg is fertilized;", size="small", color=P.muted())
bio.label(ax, (11, 7.3), "all other generations are", size="small", color=P.muted())
bio.label(ax, (11, 6.7), "parthenogenetic females", size="small", color=P.muted())
bio.label(ax, (19.6, 13.6), "Primary host", size="small", bold=True, color=P.edge("plant"))
bio.label(ax, (19.6, 13.0), "(woody, e.g. bird cherry)", size="tiny", color=P.edge("plant"))
bio.label(ax, (2.6, 1.6), "Secondary host", size="small", bold=True, color=P.edge("bract"))
bio.label(ax, (2.6, 1.0), "(herbaceous, e.g. cereals)", size="tiny", color=P.edge("bract"))
bio.label(ax, (11, 0.5), "In mild climates: anholocycly (parthenogenetic females overwinter, no sexual phase)",
          size="tiny", color=P.muted())
