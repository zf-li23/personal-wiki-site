# Endocrine control of molting in decapod crustaceans. Neurosecretory cells of the X-organ in the eyestalk
# send their axons to the sinus gland, which releases molt-inhibiting hormone (MIH) and the related
# crustacean hyperglycemic hormone (CHH) into the hemolymph. MIH suppresses the Y-organs, a pair of
# glands in the anterior thorax that secrete ecdysteroids. When environmental and internal cues (growth,
# limb loss, temperature, photoperiod) reduce MIH release, the Y-organs secrete ecdysone, which is
# converted to 20-hydroxyecdysone and starts premolt. Removing the eyestalks removes the source of MIH and
# of the vitellogenesis-inhibiting hormone (VIH), inducing molting and ovarian maturation, a practice
# used in shrimp aquaculture.
import wikibio as bio
from wikibio import ecology as eco

P = bio.P
fig, ax = bio.canvas(22, 8.6)
cues = eco.node(ax, (2.6, 6.8), "Environmental and\ninternal cues", token="neutral", w=4.2, h=1.3, size="small")
xo = eco.node(ax, (8.4, 6.8), "X-organ\n(eyestalk neurons)", token="neuron", w=4.0, h=1.3, size="small")
sg = eco.node(ax, (14.2, 6.8), "Sinus gland\n(neurohemal organ)", token="neuron", w=4.0, h=1.3, size="small")
yo = eco.node(ax, (14.2, 3.4), "Y-organs\n(anterior thorax)", token="enzyme", w=4.0, h=1.3, size="small")
ec = eco.node(ax, (8.4, 3.4), "Ecdysone →\n20-hydroxyecdysone", token="protein", w=4.2, h=1.3, size="small")
mo = eco.node(ax, (2.6, 3.4), "Premolt:\napolysis, new cuticle", token="rna", w=4.2, h=1.3, size="small")
ov = eco.node(ax, (19.6, 6.8), "Ovary", token="ovary", w=2.4, h=1.1, size="small")
eco.connect(ax, cues, xo, kind="inhibition")
eco.connect(ax, xo, sg, kind="process", text="axons")
eco.connect(ax, sg, yo, kind="inhibition", text="MIH")
eco.connect(ax, yo, ec, kind="process")
eco.connect(ax, ec, mo, kind="activation")
eco.connect(ax, sg, ov, kind="inhibition", text="VIH")
bio.label(ax, (8.4, 1.2), "Eyestalk ablation removes MIH and VIH: molting and ovarian maturation are induced", size="small", color=P.muted())
