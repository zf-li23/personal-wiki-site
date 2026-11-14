# Avoidance learning of a warning signal with one or two components, modeled with the Rescorla-Wagner rule
# (illustrative parameters). In each trial a naive chick meets 5 distasteful yellow crumbs and attacks each
# with probability 1 - V, where V is the summed associative strength of the cues present (color alone, or
# color plus pyrazine odor). Every attack is followed by the unpleasant taste (lambda = 1), and each cue
# present changes by alpha_i (lambda - V) (learning rates 0.12 for color, 0.20 for the odor; expected values
# are plotted). A: expected number of yellow crumbs eaten per trial: with the odor added, chicks learn to
# avoid the prey faster and eat fewer in total (the shape of the result of the chick experiments with pyrazine).
# B: associative strengths after each attack. In the compound group the odor takes much of the learning, and
# the color alone acquires less strength than in the single-signal group (overshadowing), a prediction of the
# rule that real predators often violate: pyrazine enhances learning about the color itself (potentiation).
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
AC, AO, N, TRIALS = 0.12, 0.20, 5, 7


def run(odor):
    vc, vo = 0.0, 0.0
    eaten, hist_c, hist_o = [], [vc], [vo]
    for _ in range(TRIALS):
        e = 0.0
        for _ in range(N):
            v = vc + (vo if odor else 0.0)
            p = min(max(1.0 - v, 0.0), 1.0)
            e += p
            err = 1.0 - v
            vc += p * AC * err
            if odor:
                vo += p * AO * err
            hist_c.append(vc)
            hist_o.append(vo)
        eaten.append(e)
    return np.array(eaten), np.array(hist_c), np.array(hist_o)


e1, c1, _ = run(False)
e2, c2, o2 = run(True)

fig, ax = bio.canvas(20.0, 9.8)
pa = quant.Plot(ax, (2.0, 1.8, 6.8, 6.4), (0.5, 7.5), (0, 5.2), xlabel="Trial", ylabel="Yellow crumbs eaten per trial",
                xticks=[1, 2, 3, 4, 5, 6, 7], yticks=[0, 1, 2, 3, 4, 5])
bio.panel(ax, "A", (0.2, 9.6))
t = np.arange(1, TRIALS + 1)
pa.line(t, e1, "dna", lw=2.0)
pa.points(t, e1, "dna", r=0.1)
pa.line(t, e2, "rna", lw=2.0)
pa.points(t, e2, "rna", r=0.1, hollow=True)
pa.text(4.2, e1[3] + 0.35, "color only", ha="left", token="dna")
pa.text(1.2, 0.3, "color + pyrazine odor", ha="left", va="bottom", token="rna")
pa.text(7.3, 4.9, f"total eaten: {e1.sum():.1f} vs {e2.sum():.1f}", ha="right", va="top", color=P.muted())

pb = quant.Plot(ax, (12.0, 1.8, 7.2, 6.4), (0, N * TRIALS), (0, 1.02), xlabel="Crumbs met",
                ylabel="Associative strength V", xticks=[0, 10, 20, 30], yticks=[0, 0.5, 1])
bio.panel(ax, "B", (10.4, 9.6))
k = np.arange(N * TRIALS + 1)
pb.line(k, c1, "dna", lw=2.0)
pb.line(k, c2 + o2, "rna", lw=2.0)
pb.line(k, c2, "rna", lw=1.4, dashed=True)
pb.line(k, o2, "atp", lw=1.4, dotted=True)
pb.legend([("color, single signal", "dna", "-"), ("color + odor (total)", "rna", "-"),
           ("color in the compound", "rna", "--"), ("odor in the compound", "atp", ":")], at=(14.2, 3.4))
