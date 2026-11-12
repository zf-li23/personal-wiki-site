# Was there an anus in the first bilaterian? Marginal ancestral state reconstruction of a binary character
# (0: mouth only, 1: through-gut with anus) under an asymmetric Mk model (gain rate g, loss rate l) on two
# five-taxon trees that differ only in the position of Xenacoelomorpha. Tip states: Cnidaria 0,
# Xenacoelomorpha 0, Protostomia 1, Ambulacraria 1, Chordata 1; the root (the cnidarian-bilaterian
# ancestor) is fixed in state 0. Branch lengths are in units of the root-to-tip depth (illustrative
# values); q = g + l is the total rate of change per tree depth. Schematic model, not data.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P


def pmat(t, g, l):
    s = g + l
    e = np.exp(-s * t)
    return np.array([[(l + g * e) / s, g * (1 - e) / s], [l * (1 - e) / s, (g + l * e) / s]])


def node_prob(tree, target, g, l):
    """Posterior probability that node `target` is in state 1 (pruning with the node clamped)."""
    out = []
    for s in (0, 1):
        def lk(nd):
            name, bl, ch = nd
            if isinstance(ch, int):
                v = np.zeros(2)
                v[ch] = 1.0
                return v
            v = np.ones(2)
            for c in ch:
                v = v * (pmat(c[1], g, l) @ lk(c))
            if name == target:
                clamp = np.zeros(2)
                clamp[s] = 1.0
                v = v * clamp
            return v
        out.append(lk(tree)[0])
    return out[1] / (out[0] + out[1])


NEPHROZOA = ("root", 0, [("Cni", 1.0, 0), ("Bil", 0.1, [("Xen", 0.9, 0), ("Nep", 0.05, [("Pro", 0.85, 1),
             ("Deu", 0.05, [("Amb", 0.8, 1), ("Cho", 0.8, 1)])])])])
XENAMBULACRARIA = ("root", 0, [("Cni", 1.0, 0), ("Bil", 0.1, [("Pro", 0.9, 1), ("Deu", 0.05, [("Cho", 0.85, 1),
                   ("Xam", 0.05, [("Amb", 0.8, 1), ("Xen", 0.8, 0)])])])])

ratio = np.logspace(-1, 2, 61)
fig, ax = bio.canvas(16, 9.6)
p = quant.Plot(ax, (2.0, 1.5, 10.2, 7.2), xlim=(0.1, 100), ylim=(0, 1), xlog=True,
               xlabel="Loss rate / gain rate  (l / g)", ylabel="P(first bilaterian had an anus)",
               xticks=[0.1, 1, 10, 100], yticks=[0, 0.25, 0.5, 0.75, 1])
for tree, tok, name in ((XENAMBULACRARIA, "negative", "Xenambulacraria"), (NEPHROZOA, "dna", "Nephrozoa")):
    for q, dashed in ((0.5, False), (1.0, True)):
        y = [node_prob(tree, "Bil", q / (1 + r), q * r / (1 + r)) for r in ratio]
        p.line(ratio, y, token=tok, lw=1.8, dashed=dashed)
    bio.label(ax, (p.X(100) + 0.15, p.Y(y[-1])), name + " tree", size="tiny", ha="left", color=quant.line_color(tok))
p.hline(0.5, token="muted")
p.vline(1, token="muted")
p.legend([("q = 0.5 per tree depth", "ink", "-"), ("q = 1", "ink", "--")], at=(2.5, 8.2))
bio.label(ax, p.xy(1.15, 0.06), "losses easier than gains  →", size="tiny", ha="left", color=P.muted())
