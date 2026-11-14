# Three phenomena of classical conditioning in simple prediction-error models (expected-value updates,
# illustrative parameters). A: contingency (Rescorla 1967) in the Rescorla-Wagner rule with the experimental
# context as a cue that is always present. Time is divided into bins, one in four containing the CS. In the
# paired group the US occurs with probability 0.4 in CS bins and never otherwise; in the truly random group it
# occurs with probability 0.4 in every bin. The CS gains strength at first in both groups, but in the random
# group the context comes to predict the US and the CS loses its strength again. B: conditioned inhibition:
# A+ and AX- trials alternate; X acquires negative strength, cancelling the prediction made by A. C: latent
# inhibition: 30 preexposures to the CS alone, then 30 CS-US pairings, in a hybrid model in which the change
# of strength is kappa * alpha * (lambda - V) and the associability alpha of the CS follows the Pearce-Hall
# rule alpha <- gamma |lambda - V| + (1 - gamma) alpha (kappa = 0.5, gamma = 0.1, initial alpha = 0.6).
# Preexposure lowers alpha and retards acquisition; the Rescorla-Wagner rule with a fixed alpha predicts no
# effect of preexposure (dashed), because nothing is learned when lambda - V = 0.
import numpy as np

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(27.0, 9.6)

# A: contingency
AB = 0.05
paired, rand = [], []
for p_out in (0.0, 0.4):
    vcs, vctx, hist = 0.0, 0.0, [0.0]
    for k in range(4 * 300):
        cs = k % 4 == 0
        lam = 0.4 if cs else p_out
        err = lam - (vctx + (vcs if cs else 0.0))
        vctx += AB * err
        if cs:
            vcs += 2 * AB * err
            hist.append(vcs)
    (paired if p_out == 0 else rand).extend(hist)
n = np.arange(len(paired))
pa = quant.Plot(ax, (1.9, 1.8, 6.4, 6.4), (0, 300), (-0.05, 0.45), xlabel="CS trials", ylabel="Associative strength of CS",
                xticks=[0, 100, 200, 300], yticks=[0, 0.2, 0.4])
bio.panel(ax, "A", (0.2, 9.4))
pa.line(n, paired, "dna", lw=2.0, text="paired: P(US | CS) = 0.4, P(US | no CS) = 0", at=0.35, dy=0.45, ha="left")
pa.line(n, rand, "rna", lw=2.0, dashed=True, text="truly random: both 0.4", at=0.55, dy=0.3, ha="left")

# B: conditioned inhibition
va, vx, ha_, hx = 0.0, 0.0, [0.0], [0.0]
for k in range(80):
    if k % 2 == 0:
        va += 0.15 * (1 - va)
    else:
        e = 0 - (va + vx)
        va += 0.15 * e
        vx += 0.15 * e
    ha_.append(va)
    hx.append(vx)
t = np.arange(len(ha_))
pb = quant.Plot(ax, (10.6, 1.8, 6.4, 6.4), (0, 80), (-1.1, 1.1), xlabel="Trials (A+ and AX- alternate)",
                ylabel="Associative strength", xticks=[0, 40, 80], yticks=[-1, -0.5, 0, 0.5, 1])
bio.panel(ax, "B", (9.0, 9.4))
pb.hline(0, dashed=False, lw=0.6)
pb.line(t, ha_, "dna", lw=2.0, text="A", at=0.9, dy=0.15)
pb.line(t, hx, "negative", lw=2.0, text="X (inhibitor)", at=0.75, dy=-0.28)
tot = np.array(ha_) + np.array(hx)
pb.line(t[::2], tot[::2], "muted", lw=1.2, dotted=True, text="A + X", at=0.45, dy=0.16)

# C: latent inhibition
def acquire(pre, kappa=0.5, gamma=0.1, alpha0=0.6, ph=True):
    v, a = 0.0, alpha0
    for _ in range(pre):
        e = 0.0 - v
        v += kappa * a * e
        if ph:
            a = gamma * abs(e) + (1 - gamma) * a
    out = [v]
    for _ in range(30):
        e = 1.0 - v
        v += kappa * a * e
        if ph:
            a = gamma * abs(e) + (1 - gamma) * a
        out.append(v)
    return np.array(out)


k = np.arange(31)
pc = quant.Plot(ax, (19.6, 1.8, 6.6, 6.4), (0, 30), (0, 1.05), xlabel="CS-US pairings", ylabel="Associative strength of CS",
                xticks=[0, 10, 20, 30], yticks=[0, 0.5, 1])
bio.panel(ax, "C", (18.0, 9.4))
pc.line(k, acquire(0), "dna", lw=2.0, text="no preexposure", at=0.12, dx=0.25, dy=0.05)
pc.line(k, acquire(30), "rna", lw=2.0, text="30 CS preexposures", at=0.5, dx=0.2, dy=-0.35)
pc.line(k, acquire(0, ph=False), "muted", lw=1.2, dashed=True, text="Rescorla-Wagner, both groups", at=0.55, dy=0.38,
        ha="left")
