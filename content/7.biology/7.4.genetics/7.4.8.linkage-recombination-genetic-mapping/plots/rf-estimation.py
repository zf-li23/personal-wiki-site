# Information about r per individual in different crosses, and the log-likelihood of the sweet-pea F2
import itertools

import numpy as np
import wikibio as bio
from wikibio import charts


def info_f2_dominant(r, phase):
    phi = (1 - r) ** 2 if phase == "coupling" else r ** 2
    dphi = -2 * (1 - r) if phase == "coupling" else 2 * r
    p = np.array([(2 + phi) / 4, (1 - phi) / 4, (1 - phi) / 4, phi / 4])
    dp = np.array([0.25, -0.25, -0.25, 0.25]) * dphi
    return np.sum(dp ** 2 / p)


def f2_codominant_probs(r):
    g = {"AB": (1 - r) / 2, "ab": (1 - r) / 2, "Ab": r / 2, "aB": r / 2}
    out = {}
    for a, b in itertools.product(g, g):
        key = ("".join(sorted(a[0] + b[0])), "".join(sorted(a[1] + b[1])))
        out[key] = out.get(key, 0) + g[a] * g[b]
    return out


def info_f2_codominant(r, h=1e-6):
    p, pp, pm = f2_codominant_probs(r), f2_codominant_probs(r + h), f2_codominant_probs(r - h)
    return sum(((pp[k] - pm[k]) / (2 * h)) ** 2 / p[k] for k in p)


fig, ax = bio.canvas(19, 7.6)
r = np.linspace(0.01, 0.49, 200)
a = charts.axes_at(ax, (1.5, 1.2, 7.2, 5.7))
curves = [("testcross", 1 / (r * (1 - r)), "dna"),
          ("F2, codominant", np.array([info_f2_codominant(x) for x in r]), "enzyme"),
          ("F2, dominant, coupling", np.array([info_f2_dominant(x, "coupling") for x in r]), "receptor"),
          ("F2, dominant, repulsion", np.array([info_f2_dominant(x, "repulsion") for x in r]), "antibody")]
for name, I, tok in curves:
    a.plot(r, I, color=charts.line(tok), lw=2, label=name)
a.set_yscale("log")
a.set_xlim(0, 0.5)
charts.style_axes(a, "recombination frequency r", "Fisher information per individual")
leg = a.legend(frameon=False, fontsize=7.5, loc="upper right")
for t in leg.get_texts():
    t.set_color(bio.P.ink())
charts.title(a, "A   information per offspring")

# B: log-likelihood, Bateson's sweet pea (coupling)
n1, n2, n3, n4 = 4831, 390, 393, 1338
rr = np.linspace(0.08, 0.17, 400)
phi = (1 - rr) ** 2
ll = n1 * np.log(2 + phi) + (n2 + n3) * np.log(1 - phi) + n4 * np.log(phi)
ll -= ll.max()
b = charts.axes_at(ax, (11.2, 1.2, 7.0, 5.7))
b.plot(rr, ll, color=charts.line("dna"), lw=2)
b.axhline(-1.92, color=charts.line("neutral"), lw=1, ls="--")
rhat = rr[np.argmax(ll)]
b.axvline(rhat, color=charts.line("receptor"), lw=1, ls=":")
b.text(rhat + 0.002, -6.5, f"r = {rhat:.3f}", fontsize=8, color=bio.P.ink())
b.set_ylim(-10, 0.8)
charts.style_axes(b, "recombination frequency r", "log-likelihood (max = 0)")
charts.title(b, "B   sweet-pea F2, n = 6952")
