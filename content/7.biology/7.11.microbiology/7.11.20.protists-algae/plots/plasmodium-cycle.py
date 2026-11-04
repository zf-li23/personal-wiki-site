"""The life cycle of Plasmodium falciparum (schematic). In the human: sporozoites from the mosquito bite reach
the liver, where each multiplies in a hepatocyte (liver schizont) and releases merozoites; merozoites invade
erythrocytes and cycle through ring, trophozoite and schizont, releasing new merozoites every 48 h; a few
develop into male and female gametocytes. In the female Anopheles mosquito: gametes fuse in the midgut, the
zygote (the only diploid stage) becomes a motile ookinete and an oocyst on the gut wall, meiosis follows, and
thousands of sporozoites migrate to the salivary glands."""
import wikibio as bio
from wikibio import ecology as E

P = bio.P
fig, ax = bio.canvas(19, 15)
steps = [dict(text="sporozoites", icon="servier/sporozoites", icon_size=1.2, shape="none"),
         dict(text="liver schizont", icon="servier/liver", icon_size=1.4, shape="none"),
         dict(text="merozoites", icon="servier/merozoites", icon_size=1.2, shape="none"),
         dict(text="ring stage in\nerythrocyte", icon="bioicons/plasmodium-ring", icon_size=1.2, shape="none"),
         dict(text="erythrocytic schizont", icon="bioicons/plasmodium-schizont", icon_size=1.2, shape="none"),
         dict(text="gametocytes", icon="servier/gametocyte-female", icon_size=1.2, shape="none"),
         dict(text="zygote (2n) and\nookinete", shape="box", token="dna"),
         dict(text="oocyst on\nmidgut wall", icon="servier/oocyst", icon_size=1.2, shape="none")]
E.cycle(ax, (9.5, 7.3), 5.2, steps, start=100, clockwise=True, size="small", label_size="tiny",
        arrow_labels=["bite: to the liver", "", "invasion of red cells", "growth, 48 h", "", "blood meal",
                      "meiosis", "to salivary glands"],
        chords=[(4, 2, dict(text="new merozoites:\nfever cycle", bend=0.3))],
        sectors=[dict(start=-0.5, end=5.5, token="blood", text="human", r0=1.8, r1=7.0),
                 dict(start=5.5, end=7.5, token="neutral", text="mosquito", r0=1.8, r1=7.0)])
bio.icon(ax, "servier/anopheles", at=(16.8, 2.0), height=1.8)
bio.label(ax, (16.8, 0.8), "Anopheles", size="small", italic=True)
