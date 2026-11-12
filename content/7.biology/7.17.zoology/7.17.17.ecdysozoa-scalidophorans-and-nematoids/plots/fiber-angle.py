# The helically wound cylinder model (Clark & Cowey 1958): a cylinder wrapped in inextensible fibers of
# length D making n turns at angle theta to the long axis has length L = D cos(theta) and volume
# V = D^3 sin^2(theta) cos(theta) / (4 pi n^2), maximal at theta = 54.7 deg. Ascaris cuticle fibers cross
# at about 75 deg (Harris & Crofton 1957) and the body is round in section, so the worm lies on the curve:
# shortening (theta up) would need a volume the cuticle cannot hold, so longitudinal muscle pull raises the
# internal pressure and bends the body instead of shortening it.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(15, 8.6)
th = np.linspace(1, 89, 400)
r = np.radians(th)
v = np.sin(r) ** 2 * np.cos(r) / (2 / (3 * np.sqrt(3)))
L = np.cos(r)
p = quant.Plot(ax, (1.6, 1.4, 12.4, 6.4), xlim=(0, 90), ylim=(0, 1.1), xlabel="Fiber angle to long axis θ / °",
               ylabel="Relative value", xticks=[0, 15, 30, 45, 54.7, 60, 75, 90], yticks=[0, 0.25, 0.5, 0.75, 1])
p.line(th, v, "dna")
bio.label(ax, p.xy(19, 0.52), "Maximum volume V/Vmax", size="small", color=quant.line_color("dna"))
p.line(th, L, "rna", dashed=True, text="Length L/D", at=0.12, dy=0.06)
p.vline(54.7, text="54.7°: largest volume", top=True)
p.span(72, 78, "highlight")
bio.label(ax, p.xy(75, 1.07), "Ascaris", size="tiny", italic=True)
bio.label(ax, p.xy(75, 1.0), "cuticle, ~75°", size="tiny")
x75 = np.radians(75)
p.points([75], [np.sin(x75) ** 2 * np.cos(x75) / 0.3849], "negative", r=0.1)
bio.arrow(ax, p.xy(76.5, 0.66), p.xy(83, 0.4), kind="process", color=P.muted(), bend=-0.15)
bio.label(ax, p.xy(84, 0.75), "Shortening would need\nmore volume than the\ncuticle can enclose", size="tiny", ha="center")
bio.label(ax, p.xy(42, 0.13), "Below the curve: body flattened,\nlength changes freely\n(flatworms, nemerteans)", size="tiny", ha="center")
