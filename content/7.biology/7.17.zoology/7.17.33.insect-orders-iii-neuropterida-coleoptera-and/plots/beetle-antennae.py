# Antennae and tarsal formulae of some beetle families (schematic, drawn with wikibio.zoomorph.antenna;
# scape, pedicel and flagellum coloured). Antennal type and the number of tarsomeres on fore, middle and
# hind legs (written as true count, with the apparent count where a tarsomere is minute and hidden) are the first characters used to place a beetle in its family.
import wikibio as bio
from wikibio import zoomorph as zm

P = bio.P
FAM = [("Carabidae", "filiform", 3.6, "5-5-5", "ground beetles"),
       ("Elateridae", "serrate", 3.2, "5-5-5", "click beetles"),
       ("Scarabaeidae", "lamellate", 2.4, "5-5-5", "scarabs"),
       ("Coccinellidae", "clavate", 1.8, "4-4-4, look 3-3-3", "ladybirds"),
       ("Nitidulidae", "capitate", 2.0, "5-5-5", "sap beetles"),
       ("Tenebrionidae", "moniliform", 2.6, "5-5-4", "darkling beetles"),
       ("Cerambycidae", "setaceous", 4.6, "5-5-5, look 4-4-4", "longhorn beetles"),
       ("Curculionidae", "geniculate", 2.6, "5-5-5, look 4-4-4", "weevils")]
W = 3.2
fig, ax = bio.canvas(W * len(FAM), 8.2)
for i, (fam, kind, L, tars, common) in enumerate(FAM):
    x = i * W + W / 2
    zm.antenna(ax, (x - 0.3, 2.0), 80, min(L, 4.6), kind, colored=True)
    bio.label(ax, (x, 7.7), fam, size="small", bold=True)
    bio.label(ax, (x, 7.2), common, size="tiny", color=P.muted())
    bio.label(ax, (x, 1.3), kind, size="tiny")
    bio.label(ax, (x, 0.6), "tarsi " + tars, size="tiny", color=P.muted())
