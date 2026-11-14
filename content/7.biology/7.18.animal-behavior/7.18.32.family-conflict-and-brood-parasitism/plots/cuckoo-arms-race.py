"""The cuckoo-host arms race and the cost of egg rejection.

A: the likely sequence of the arms race at the egg stage (Davies and Brooke 1989), with the escalation to the
chick stage. B: a signal detection model of egg rejection (after Davies and colleagues 1996; Reeve 1989). The
appearance of a host's own eggs is normally distributed (mean 0, SD 1) and that of a cuckoo egg has mean d (the
poorer the mimicry, the larger d). A host rejects an egg whose appearance exceeds a threshold t. Accepting a
cuckoo egg costs the whole brood (1); rejecting one of its own four eggs by mistake costs 1/4 of a brood. With a
probability pi that the nest is parasitized, the expected loss per nest is
pi Phi(t - d) + (1 - pi) (1 - Phi(t)) / 4 (counting one suspect egg per nest). The curves show the probability
that a cuckoo egg is rejected when the host uses the threshold that minimizes this loss, for poor (d = 3) and
good (d = 1) mimicry: when mimicry is good and parasitism rare, the best host accepts most cuckoo eggs.
"""

import math

import numpy as np
import wikibio as bio
from wikibio import charts as Ch

P = bio.P
FS = bio.core.FONT


def Phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


fig, ax = bio.canvas(32.0, 11.0)
bio.panel(ax, "A", (0.2, 10.8))
steps = [("1", "no parasitism:\nhosts accept odd eggs", "neutral"),
         ("2", "parasitism: hosts evolve\nrejection, distinctive eggs", "rna"),
         ("3", "cuckoos evolve egg mimicry,\nfast laying, egg removal", "dna"),
         ("4", "good mimicry: rejection\ncostly, hosts often accept", "neutral"),
         ("5", "chick stage: ejection, vocal\nand visual trickery", "dna")]
y = 9.6
for k, (n, text, tok) in enumerate(steps):
    bio.box(ax, (7.2, y), 9.6, 1.45, tok, text, size="small")
    bio.label(ax, (1.6, y), n, size="title", bold=True)
    if k < len(steps) - 1:
        bio.arrow(ax, (7.2, y - 0.75), (7.2, y - 1.15), kind="process")
    y -= 1.95

p = Ch.axes_at(ax, (17.6, 2.0, 13.0, 7.6))
pis = np.linspace(0.005, 0.6, 120)
ts = np.linspace(-3, 8, 2201)
for d, tok, name in ((3.0, "rna", "poor mimicry (d = 3)"), (1.0, "dna", "good mimicry (d = 1)")):
    rej = []
    for pi in pis:
        loss = [pi * Phi(t - d) + (1 - pi) * (1 - Phi(t)) / 4 for t in ts]
        t = ts[int(np.argmin(loss))]
        rej.append(1 - Phi(t - d))
    p.plot(pis, rej, color=Ch.line(tok), lw=1.9, label=name)
p.set_xlim(0, 0.6)
p.set_ylim(0, 1.02)
Ch.style_axes(p, "probability that a nest is parasitized", "cuckoo eggs rejected (optimal host)")
Ch.title(p, "Hosts should reject less when mimicry is good and parasitism rare")
leg = p.legend(fontsize=FS["tiny"], frameon=False, loc="lower right")
for t in leg.get_texts():
    t.set_color(P.ink())
bio.panel(ax, "B", (15.6, 10.8))
