# Habituation and its rate sensitivity in a cascaded-integrator model (after Staddon and Higa 1996).
# A stimulus of size 1 passes through two units in series; each unit subtracts its state V_i from its input
# and passes on the positive remainder, and its state is updated every time step as V_i <- a_i V_i + b_i x_i,
# where x_i is the unit's input. The first unit is fast (a = 0.8, b = 0.3), the second slow (a = 0.995,
# b = 0.04). The response is the output of the second unit. A: responses to 30 stimuli presented every 2 or
# every 10 time steps: habituation is faster and deeper at the short interstimulus interval (ISI). B:
# spontaneous recovery, the response to a single probe stimulus given at different delays after the end of
# training: although habituation was deeper at the short ISI, the response recovers faster after it and soon
# exceeds the response of animals trained at the long ISI, because habituation was then carried mainly by the
# fast unit (rate sensitivity; Davis 1970 found the same in the startle response of rats).
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
A_, B_ = (0.8, 0.995), (0.3, 0.04)


def step(V, x):
    out = x
    for i in range(2):
        o = max(out - V[i], 0.0)
        V[i] = A_[i] * V[i] + B_[i] * out
        out = o
    return out


def train(isi, n=30):
    V = [0.0, 0.0]
    resp = []
    for k in range(isi * n):
        x = 1.0 if k % isi == 0 else 0.0
        r = step(V, x)
        if x:
            resp.append(r)
    return np.array(resp), V


def probe(V, d):
    W = list(V)
    for _ in range(d - 1):
        W = [A_[i] * W[i] for i in range(2)]
    return step(W, 1.0)


fig, ax = bio.canvas(21.0, 9.4)
pa = quant.Plot(ax, (2.0, 1.8, 7.4, 6.4), (0, 31), (0, 1.05), xlabel="Stimulus number", ylabel="Response",
                xticks=[1, 10, 20, 30], yticks=[0, 0.5, 1])
bio.panel(ax, "A", (0.2, 9.2))
delays = np.unique(np.round(np.geomspace(1, 600, 40)).astype(int))
pb = quant.Plot(ax, (12.4, 1.8, 7.8, 6.4), (0, np.log10(600)), (0, 1.05), xlabel="Delay after training (time steps)",
                ylabel="Response to probe", xticks=[(0, "1"), (1, "10"), (2, "100"), (np.log10(600), "600")],
                yticks=[0, 0.5, 1])
bio.panel(ax, "B", (10.6, 9.2))
for isi, tok, dash in ((2, "rna", False), (10, "dna", True)):
    r, V = train(isi)
    n = np.arange(1, len(r) + 1)
    pa.line(n, r, tok, lw=1.8, dashed=dash)
    pa.points(n[::3], r[::3], tok, r=0.09, hollow=dash)
    rec = [probe(V, d) for d in delays]
    pb.line(np.log10(delays), rec, tok, lw=2.0, dashed=dash)
pa.text(6.5, 0.12, "ISI = 2", ha="left", token="rna")
pa.text(17, 0.62, "ISI = 10", ha="left", token="dna")
pb.text(0.9, 0.78, "trained at ISI = 2", ha="right", token="rna")
pb.text(1.6, 0.36, "trained at ISI = 10", ha="left", token="dna")
