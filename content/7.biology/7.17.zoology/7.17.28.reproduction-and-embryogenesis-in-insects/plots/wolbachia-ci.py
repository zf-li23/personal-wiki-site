# Spread of a cytoplasmic-incompatibility Wolbachia (Turelli & Hoffmann 1995 bookkeeping, Eq. 28.3):
# p' = p F (1 - mu) / ( p F (1 - mu sh p) + (1 - p)(1 - sh p) ); illustrative F = 0.9, sh = 0.9, mu = 0 or 0.03.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
F, sh = 0.9, 0.9


def nxt(p, mu):
    return p * F * (1 - mu) / (p * F * (1 - mu * sh * p) + (1 - p) * (1 - sh * p))


fig, ax = bio.canvas(24, 10.5)
pA = quant.Plot(ax, (2.0, 1.7, 7.6, 7.2), xlim=(0, 1), ylim=(-0.02, 0.16), xlabel="Infection frequency p",
                ylabel="Change per generation p' - p", xticks=[0, 0.25, 0.5, 0.75, 1], yticks=[0, 0.04, 0.08, 0.12, 0.16],
                ylabel_offset=1.1)
p = np.linspace(0, 1, 400)
pA.hline(0, token="muted", dashed=False)
pA.line(p, nxt(p, 0.0) - p, "enzyme", text="mu = 0", at=0.3, dy=0.3)
pA.line(p, nxt(p, 0.03) - p, "channel", dashed=True, text="mu = 0.03", at=0.62, dy=-0.9)
for ph, tok in (((1 - F) / sh, "enzyme"), (0.146, "channel"), (0.996, "channel")):
    pA.points([ph], [0], tok, r=0.12, hollow=True)
pA.text(0.13, -0.013, "unstable thresholds 0.11, 0.15", ha="left")
bio.label(ax, (5.8, 9.7), "A  Recursion and equilibria", size="small", bold=True)

pB = quant.Plot(ax, (13.4, 1.7, 9.6, 7.2), xlim=(0, 30), ylim=(0, 1), xlabel="Generation",
                ylabel="Infection frequency", xticks=[0, 10, 20, 30], yticks=[0, 0.25, 0.5, 0.75, 1])
for p0, tok in ((0.08, "negative"), (0.13, "negative"), (0.18, "positive"), (0.3, "positive"), (0.5, "positive")):
    xs, ys = [0], [p0]
    for g in range(30):
        ys.append(nxt(ys[-1], 0.03))
        xs.append(g + 1)
    pB.line(np.array(xs), np.array(ys), tok, lw=1.4)
    pB.text(0.4, p0 + 0.02, "%.2f" % p0, ha="left")
pB.hline(0.146, token="muted", text="threshold 0.15", size="tiny")
bio.label(ax, (18.2, 9.7), "B  Trajectories from different releases (mu = 0.03)", size="small", bold=True)
