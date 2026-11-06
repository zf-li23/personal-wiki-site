# Light and warm-temperature signalling to photomorphogenesis as an SBGN Activity Flow map (simplified;
# after Taiz et al. 6e Figs 16.10-16.18 and 16.28, and the thermosensing literature).
# Darkness is the default: PIFs (bHLH factors) drive skotomorphogenic genes and elongation, and the
# COP1-SPA E3 ligase degrades HY5. Active phytochromes (Pfr) promote PIF phosphorylation and
# degradation and inhibit COP1-SPA; blue-light-activated cryptochromes bind SPA and inhibit COP1;
# monomeric UVR8 binds COP1, which then promotes HY5 expression. Warmth inactivates phyB (thermal
# reversion of Pfr) and the evening complex (ELF3 phase separation), releasing PIF4.
import wikibio as bio
from wikibio import network

P = bio.P
fig, ax = bio.canvas(22, 13.0)
d = network.Diagram(ax)
d.compartment("nuc", (8.6, 0.6, 21.6, 12.6), "Nucleus", token="nucleus", label_pos="br")
bio.label(ax, (1.5, 12.6), "Signals", size="small", bold=True, color=P.muted())
bio.label(ax, (5.0, 12.6), "Photoreceptors", size="small", bold=True, color=P.muted())

d.perturbation("warm", (1.5, 11.6), "Warmth", token="positive")
d.perturbation("red", (1.5, 10.2), "Red", token="negative")
d.perturbation("fr", (1.5, 8.4), "Far-red", token="drug")
d.perturbation("blue", (1.5, 4.5), "Blue / UV-A", token="highlight")
d.perturbation("uvb", (1.5, 2.6), "UV-B", token="neutral")

d.activity("phyb", (5.0, 10.2), "phyB (Pfr)", token="receptor")
d.activity("phya", (5.0, 8.4), "phyA (Pfr)", token="receptor")
d.activity("cry", (5.0, 4.5), "cry1/cry2", token="receptor")
d.activity("uvr8", (5.0, 2.6), "UVR8 monomer", token="receptor")

d.activity("ec", (11.6, 11.6), "Evening complex", token="protein", units=["ELF3"])
d.activity("pif", (11.6, 9.3), "PIFs", token="protein")
d.activity("cop", (11.6, 5.0), "COP1-SPA", token="enzyme", h=1.5)
d.activity("hy5", (15.6, 5.0), "HY5", token="protein")
d.activity("aux", (15.6, 9.3), "Auxin, BR", token="metabolite")
d.phenotype("elong", (19.4, 9.3), "Elongation")
d.phenotype("photo", (19.4, 5.0), "Photomorphogenesis", w=3.6)

d.connect("warm", "ec", "negative")
d.connect("warm", "phyb", "negative", via=[(5.0, 11.6)])
d.connect("red", "phyb", "positive")
d.connect("fr", "phyb", "negative", via=[(2.9, 8.4), (2.9, 9.6), (3.3, 9.6)])
d.connect("fr", "phya", "positive")
d.connect("blue", "cry", "positive")
d.connect("uvb", "uvr8", "positive")
d.connect("ec", "pif", "negative")
d.connect("phyb", "pif", "negative", via=[(9.0, 10.2), (9.0, 9.5)])
d.connect("phya", "pif", "negative", via=[(9.6, 8.4), (9.6, 9.1)])
d.connect("phyb", "cop", "negative", via=[(7.0, 10.2), (7.0, 5.5)])
d.connect("phya", "cop", "negative", via=[(7.8, 8.4), (7.8, 5.0)])
d.connect("cry", "cop", "negative")
d.connect("uvr8", "cop", "positive", dashed=True, text="binds", via=[(11.6, 2.6)])
d.connect("uvr8", "hy5", "positive", via=[(15.6, 2.6)])
d.connect("cop", "hy5", "negative")
d.connect("pif", "aux", "positive")
d.connect("aux", "elong", "positive")
d.connect("hy5", "photo", "positive")
d.connect("hy5", "elong", "negative", via=[(15.6, 7.4), (19.4, 7.4)])
