# A minimal version of the two-stage hypothesis for point following in canids (Udell, Dorey and Wynne 2010),
# as a model. Stage 1: socialization early in life sets the probability s that the animal attends to a
# human at all on a trial. Stage 2: when it attends, it learns the point-food contingency by a delta rule,
# w <- w + alpha (1 - w) after a rewarded follow, with alpha = 0.08; the probability of choosing the
# pointed-at bowl is 0.5 + 0.5 s w (the rest of the time it chooses at random). Groups differ in s and in
# the prior association w0 brought from life with people: pet dogs s = 0.95, w0 = 0.75; shelter dogs
# s = 0.7, w0 = 0.15; hand-reared wolves s = 0.85, w0 = 0.1; wolves not socialized to people s = 0.1,
# w0 = 0. Curves are model predictions (mean of 500 simulated animals), not data.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
rng = np.random.default_rng(0)
groups = [("pet dogs", 0.95, 0.75, "dna"), ("shelter dogs", 0.7, 0.15, "rna"),
          ("hand-reared wolves", 0.85, 0.10, "positive"), ("unsocialized wolves", 0.10, 0.0, "neutral")]
T, N, alpha = 60, 500, 0.08
fig, ax = bio.canvas(16, 9.4)
p = quant.Plot(ax, (2.0, 1.8, 10.0, 6.6), (0, T), (0.4, 1.0), xlabel="Trial", ylabel="Choice of the pointed-at bowl",
               xticks=[0, 20, 40, 60], yticks=[0.5, 0.75, 1.0])
p.hline(0.5, text="chance", side="left")
for name, s, w0, tok in groups:
    acc = np.zeros(T)
    for _ in range(N):
        w = w0
        for t in range(T):
            attend = rng.random() < s
            pc = 0.5 + 0.5 * w if attend else 0.5
            acc[t] += pc
            if attend and rng.random() < pc:
                w += alpha * (1 - w)
    acc /= N
    p.line(np.arange(T), acc, tok, lw=2.0, dashed=(tok == "neutral"))
    p.text(T + 0.8, acc[-1], name, ha="left", token=tok)
