"""Pattern separation by sparse expansion (a dentate-gyrus-like random projection).

Input layer (entorhinal cortex): N_in = 400 binary units, 10 % active. Pairs of input patterns
are built with a controlled overlap: the second pattern keeps a fraction q of the active units
of the first and replaces the rest by randomly chosen inactive ones. Output layer: N_out = 4000
units with random excitatory weights (each output unit receives 40 inputs, weight 1); the
output is formed by k-winners-take-all (feedback inhibition), keeping the fraction f of units
with the largest input active. Similarity of two patterns is the Pearson correlation of the
binary vectors. 40 pairs per point, seed 0.
A: output against input correlation for output sparseness f = 0.5, 0.1 and 0.02; the identity
   line marks no change: below it, similar inputs are made less similar (separation).
B: output correlation for input correlation of about 0.75 as a function of f.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(0)
Nin, Nout, a_in, fan = 400, 4000, 0.1, 40
C = np.zeros((Nout, Nin))
for i in range(Nout):
    C[i, rng.choice(Nin, fan, replace=False)] = 1.0
kin = int(a_in * Nin)


def pair(q):
    x = np.zeros(Nin)
    on = rng.choice(Nin, kin, replace=False)
    x[on] = 1
    keep = rng.choice(on, int(round(q * kin)), replace=False)
    off = np.setdiff1d(np.arange(Nin), on)
    new = rng.choice(off, kin - keep.size, replace=False)
    y = np.zeros(Nin)
    y[keep] = 1
    y[new] = 1
    return x, y


def kwta(h, f):
    k = max(1, int(f * h.size))
    out = np.zeros_like(h)
    # tie-breaking by tiny noise so that exactly k units are active
    out[np.argsort(h + 1e-6 * rng.random(h.size))[-k:]] = 1
    return out


corr = lambda a, b: np.corrcoef(a, b)[0, 1]
qs = np.linspace(0.0, 1.0, 11)
fig, axs = plt.subplots(1, 2, figsize=(10, 3.9))
cols = [P.edge("neutral"), P.edge("dna"), P.edge("negative")]
for f, c in zip((0.5, 0.1, 0.02), cols):
    xin, xout = [], []
    for q in qs:
        ri, ro = [], []
        for _ in range(40):
            x, y = pair(q)
            ri.append(corr(x, y))
            ro.append(corr(kwta(C @ x, f), kwta(C @ y, f)))
        xin.append(np.mean(ri))
        xout.append(np.mean(ro))
    axs[0].plot(xin, xout, "o-", ms=4, color=c, lw=1.8, label=f"f = {f}")
axs[0].plot([0, 1], [0, 1], ls="--", color=P.muted(), lw=1)
axs[0].set_xlabel("Input correlation (EC)")
axs[0].set_ylabel("Output correlation (DG)")
axs[0].set_title("A  Separation by sparse expansion", loc="left", fontsize=10)
axs[0].legend(frameon=False, fontsize=8, loc="upper left")
fs = np.array([0.5, 0.3, 0.2, 0.1, 0.05, 0.02, 0.01])
vals = []
for f in fs:
    ro = []
    for _ in range(40):
        x, y = pair(0.775)
        ro.append(corr(kwta(C @ x, f), kwta(C @ y, f)))
    vals.append(np.mean(ro))
axs[1].semilogx(fs, vals, "o-", color=P.edge("dna"), lw=1.8)
axs[1].axhline(0.75, ls="--", color=P.muted(), lw=1)
axs[1].text(0.012, 0.77, "input correlation", fontsize=8, color=P.muted())
axs[1].set_xlabel("Output sparseness f (fraction active)")
axs[1].set_ylabel("Output correlation")
axs[1].set_ylim(0, 1)
axs[1].set_title("B  Sparser codes separate more", loc="left", fontsize=10)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
