# Two models of transitive inference in the five-term series task (A+B-, B+C-, C+D-, D+E-, intermixed).
# Associative model (after Wynne 1995 and Vasconcelos 2008): each stimulus has a value V; on each trial the
# animal chooses between the two stimuli with probability given by a softmax of their values (inverse
# temperature beta = 15) and only the chosen stimulus is updated, V <- V + alpha (r - V), alpha = 0.05, r = 1
# for the correct choice. 4000 training trials, mean of 200 simulated subjects. Ordinal model: each stimulus
# occupies a position on a mental line (A = 5 ... E = 1) read with Gaussian noise (s.d. 0.9); the larger
# reading is chosen. A: mean values after training. B: predicted choice of the higher-ranked stimulus in
# the four trained pairs and the six untrained pairs, including the critical pair BD.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
pairs = [(0, 1), (1, 2), (2, 3), (3, 4)]
beta, alpha, T, N = 15.0, 0.05, 4000, 200
Vs = np.zeros((N, 5))
for s in range(N):
    V = np.full(5, 0.5)
    for t in range(T):
        i, j = pairs[rng.integers(4)]
        p = 1 / (1 + np.exp(-beta * (V[i] - V[j])))
        c = i if rng.random() < p else j
        r = 1.0 if c == i else 0.0
        V[c] += alpha * (r - V[c])
    Vs[s] = V
Vm = Vs.mean(axis=0)

test = [(0, 1), (1, 2), (2, 3), (3, 4), (0, 2), (1, 3), (2, 4), (0, 3), (1, 4), (0, 4)]
names = "ABCDE"
assoc = [np.mean(1 / (1 + np.exp(-beta * (Vs[:, i] - Vs[:, j])))) for i, j in test]
from math import erf, sqrt


def phi(x):
    return 0.5 * (1 + erf(x / sqrt(2)))


ordinal = [phi((j - i) / (0.9 * sqrt(2))) for i, j in test]

fig, ax = bio.canvas(23, 9.6)
pa = quant.Plot(ax, (1.9, 1.8, 5.6, 6.6), (-0.5, 4.5), (0, 1.2), xlabel="Stimulus", ylabel="Associative value V",
                xticks=[(k, names[k]) for k in range(5)], yticks=[0, 0.5, 1.0])
bio.panel(ax, "A", (0.2, 9.3))
for k in range(5):
    tok = "positive" if k in (1, 3) else "neutral"
    pa.bars([k - 0.3, k + 0.3], [Vm[k]], tok)
    pa.text(k, Vm[k] + 0.05, f"{Vm[k]:.2f}", size="tiny")
pa.text(2.4, 1.14, "B and D: each rewarded in one pair", size="tiny", token="positive")

pb = quant.Plot(ax, (10.0, 1.8, 12.0, 6.6), (-0.6, 9.6), (0.4, 1.0), xlabel="Test pair",
                ylabel="Choice of higher-ranked item", xticks=[(k, names[i] + names[j]) for k, (i, j) in enumerate(test)],
                yticks=[0.5, 0.75, 1.0])
bio.panel(ax, "B", (8.4, 9.3))
pb.span(-0.5, 3.5, "neutral", text="trained pairs", strength=0.75)
pb.span(4.5, 5.5, "highlight", text="critical", strength=0.6)
pb.hline(0.5, text="chance", side="left")
xs = np.arange(10)
pb.line(xs, assoc, "dna", lw=1.8)
pb.points(xs, assoc, "dna", r=0.1)
pb.line(xs, ordinal, "rna", lw=1.8, dashed=True)
pb.points(xs, ordinal, "rna", r=0.1, hollow=True)
pb.legend([("associative (chosen item updated)", "dna", "-"), ("ordinal (positions on a line)", "rna", "--")],
          at=(16.2, 3.6))
