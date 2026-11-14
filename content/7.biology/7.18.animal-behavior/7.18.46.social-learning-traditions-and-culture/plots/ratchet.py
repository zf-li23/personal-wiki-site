# Cumulative culture and population size (after Henrich 2004). In each generation, each of N learners copies
# the most skilled member of the previous generation. Copying is imperfect: the learner's skill is the
# model's skill minus a mean loss alpha plus a random deviation drawn from a Gumbel distribution of scale
# beta (most copies are worse than the model, a few are better: innovations). The expected change in mean
# skill per generation is Delta z = -alpha + beta (gamma + ln N), where gamma = 0.577 is Euler's constant,
# so skill accumulates only above the critical size N* = exp(alpha / beta - gamma). Parameters: alpha = 1,
# beta = 0.25, giving N* = 31. A: mean skill over 60 generations for four population sizes (one simulated
# run each). B: change in mean skill per generation against N (log scale): formula (line) and simulation
# (points, mean over 200 generations).
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
alpha, beta, g = 1.0, 0.25, 0.5772
Nstar = np.exp(alpha / beta - g)


def run(N, T, z0=10.0):
    z = np.full(N, z0)
    means = [z.mean()]
    for _ in range(T):
        z = z.max() - alpha + rng.gumbel(0.0, beta, N)
        means.append(z.mean())
    return np.array(means)


fig, ax = bio.canvas(22, 9.6)
T = 60
pa = quant.Plot(ax, (2.0, 1.8, 8.0, 6.6), (0, T), (-15, 50), xlabel="Generation", ylabel="Mean skill",
                xticks=[0, 20, 40, 60], yticks=[-10, 0, 10, 20, 30, 40, 50])
bio.panel(ax, "A", (0.2, 9.3))
for N, tok in ((300, "dna"), (100, "positive"), (30, "neutral"), (10, "rna")):
    m = run(N, T)
    pa.line(np.arange(T + 1), m, tok, lw=2.0)
    pa.text(T + 1.5, m[-1], f"N = {N}", ha="left", token=tok)

pb = quant.Plot(ax, (13.4, 1.8, 7.6, 6.6), (np.log(3), np.log(1000)), (-0.8, 1.0), xlabel="Population size N",
                ylabel="Change in mean skill per generation",
                xticks=[(np.log(3), "3"), (np.log(10), "10"), (np.log(30), "30"), (np.log(100), "100"),
                        (np.log(300), "300"), (np.log(1000), "1000")], yticks=[-0.8, -0.4, 0, 0.4, 0.8])
bio.panel(ax, "B", (11.6, 9.3))
lnN = np.linspace(np.log(3), np.log(1000), 200)
pb.line(lnN, -alpha + beta * (g + lnN), "dna", lw=2.0)
pb.hline(0.0, text="no change", side="left")
for N in (3, 10, 30, 100, 300, 1000):
    m = run(N, 200)
    pb.points([np.log(N)], [(m[-1] - m[0]) / 200], "rna", r=0.11)
pb.vline(np.log(Nstar), text=f"N* = {Nstar:.0f}")
pb.text(np.log(5), 0.6, "accumulation", ha="left", color=P.edge("positive"))
pb.text(np.log(110), -0.6, "loss", ha="left", color=P.edge("negative"))
