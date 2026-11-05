"""Two hypotheses for the origin of the land-plant alternation of generations. Blue: diploid; orange:
haploid. A: antithetic (interpolation) theory: a haplontic charophyte-like ancestor; mitoses inserted in
the zygote before meiosis give a small multicellular diploid phase on the gametophyte (bryophyte-like);
this phase enlarges into an independent, dominant sporophyte (vascular plants). B: homologous theory: an
ancestor with isomorphic alternation of generations; after the move to land the two generations diverge,
towards gametophyte dominance (bryophytes) or sporophyte dominance (vascular plants)."""
import wikibio as bio
from wikibio import plant

P = bio.P
fig, ax = bio.canvas(36, 23)
R = 2.7


def st(t, bold=False):
    return dict(text=t, size="small", bold=bold)


def ring(c, stages, mei, fert):
    plant.alternation_of_generations(ax, c, R, [st(*s) if isinstance(s, tuple) else st(s) for s in stages],
                                     meiosis=mei, fertilization=fert, gap=0.18, labels=("2n", "n"))


def title(c, t, sub):
    bio.label(ax, (c[0], c[1] + R + 2.0), t, size="normal", bold=True)
    bio.label(ax, (c[0], c[1] + R + 1.45), sub, size="small", color=P.muted())


XS = (5.6, 18.0, 30.4)
YA, YB = 16.4, 4.6
bio.panel(ax, "A", (0.2, 22.8))
bio.label(ax, (18.0, 22.4), "Antithetic (interpolation) theory", size="title", bold=True)
ring((XS[0], YA), [("Thallus (n)", True), "Gametes", "Zygote", "Meiospores"], 2, 1)
title((XS[0], YA), "Ancestor", "zygote the only 2n cell")
ring((XS[1], YA), [("Gametophyte (n)", True), "Gametes", "Zygote", ("Small sporophyte\non gametophyte", True), "Spores"], 3, 1)
title((XS[1], YA), "Mitoses inserted", "before meiosis")
ring((XS[2], YA), [("Sporophyte (2n)", True), "Spores", "Small\ngametophyte", "Gametes", "Zygote"], 0, 3)
title((XS[2], YA), "Sporophyte dominant", "independent, branched")
for a, b in zip(XS[:-1], XS[1:]):
    bio.arrow(ax, (a + R + 1.7, YA), (b - R - 1.7, YA), kind="process", color=P.muted(), lw=2.0)

bio.panel(ax, "B", (0.2, 10.9))
bio.label(ax, (18.0, 10.5), "Homologous theory", size="title", bold=True)
ring((XS[1], YB), [("Gametophyte (n)", True), "Gametes", "Zygote", ("Sporophyte (2n)\nsame form", True), "Spores"], 3, 1)
bio.label(ax, (XS[1], YB - R - 1.7), "Ancestor: isomorphic alternation", size="normal", bold=True)
ring((XS[0], YB), [("Gametophyte (n)\ndominant", True), "Gametes", "Zygote", "Sporophyte\n(dependent)", "Spores"], 3, 1)
bio.label(ax, (XS[0], YB - R - 1.7), "Bryophytes", size="normal", bold=True)
ring((XS[2], YB), [("Sporophyte (2n)\ndominant", True), "Spores", "Gametophyte\n(reduced)", "Gametes", "Zygote"], 0, 3)
bio.label(ax, (XS[2], YB - R - 1.7), "Vascular plants", size="normal", bold=True)
bio.arrow(ax, (XS[1] - R - 1.7, YB), (XS[0] + R + 1.7, YB), kind="process", color=P.muted(), lw=2.0)
bio.arrow(ax, (XS[1] + R + 1.7, YB), (XS[2] - R - 1.7, YB), kind="process", color=P.muted(), lw=2.0)
