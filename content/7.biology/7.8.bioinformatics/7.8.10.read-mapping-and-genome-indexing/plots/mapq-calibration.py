# Calibration of mapping qualities on a simulated genome with repeats. A random 300 kb genome carries
# 40 copies of a 1.5 kb repeat (each diverged from the consensus by 0-4 % substitutions) and 5 identical
# copies of a 1 kb segmental duplication. 20 000 reads of 100 nt are sampled with per-base qualities Q20,
# Q30 or Q37 and errors at those rates. Each read is mapped by five non-overlapping exact 20-mer seeds
# (pigeonhole: up to four mismatches always leave one exact seed) and ungapped scoring of every candidate;
# MAPQ is the Phred-scaled posterior probability that the best candidate is wrong, capped at 60.
# A: reported MAPQ against the empirical error rate in bins (a calibrated caller lies on the diagonal).
# B: distribution of MAPQ for reads from unique sequence, diverged repeat copies and identical copies.
import numpy as np
import wikibio as bio
from wikibio import charts as C

rng = np.random.default_rng(0)
B = np.array(list("ACGT"))
G = 300_000
genome = rng.integers(0, 4, G)
label = np.zeros(G, dtype=int)  # 0 unique, 1 diverged repeat, 2 identical duplication
rep = rng.integers(0, 4, 1500)
starts = np.sort(rng.choice(np.arange(0, G - 2000, 2000), 85, replace=False))
for s in starts[:80]:
    d = rng.uniform(0.0, 0.02)
    cp = rep.copy()
    m = rng.random(1500) < d
    cp[m] = (cp[m] + rng.integers(1, 4, m.sum())) % 4
    genome[s:s + 1500] = cp
    label[s:s + 1500] = 1
dup = rng.integers(0, 4, 1000)
for s in starts[80:]:
    genome[s:s + 1000] = dup
    label[s:s + 1000] = 2

K, RL, NR = 20, 100, 40_000
code = genome.copy()
# integer encoding of every 20-mer by a rolling sum
vals = np.zeros(G - K + 1, dtype=np.int64)
for j in range(K):
    vals = vals * 4 + code[j:G - K + 1 + j]
index = {}
for pos, v in enumerate(vals.tolist()):
    index.setdefault(v, []).append(pos)

qual_levels = np.array([20, 30, 37])
true_pos = rng.integers(0, G - RL, NR)
mapq = np.zeros(NR)
mapq0 = np.zeros(NR)
wrong0 = np.zeros(NR, dtype=bool)
wrong = np.zeros(NR, dtype=bool)
klass = np.zeros(NR, dtype=int)
for r in range(NR):
    t = true_pos[r]
    q = qual_levels[rng.choice(3, RL, p=[0.1, 0.3, 0.6])]
    perr = 10.0 ** (-q / 10)
    read = genome[t:t + RL].copy()
    e = rng.random(RL) < perr
    read[e] = (read[e] + rng.integers(1, 4, e.sum())) % 4
    cands = set()
    for off in range(0, RL, K):
        v = 0
        for j in range(K):
            v = v * 4 + int(read[off + j])
        for p in index.get(v, ()):
            s = p - off
            if 0 <= s <= G - RL:
                cands.add(s)
    lab = label[t:t + RL].max()
    klass[r] = lab
    if not cands:
        mapq[r] = 0
        wrong[r] = True
        continue
    cands = np.array(sorted(cands))
    mism = genome[cands[:, None] + np.arange(RL)] != read[None, :]
    ll = np.where(mism, np.log(perr / 3), np.log1p(-perr)).sum(axis=1)
    post = np.exp(ll - ll.max())
    post /= post.sum()
    best = rng.choice(np.flatnonzero(post == post.max()))
    pw = max(1.0 - post[best], 1e-12)
    mapq[r] = min(60.0, -10 * np.log10(pw))
    wrong[r] = cands[best] != t
    # the same posterior if base qualities are ignored (every base assumed Q20)
    ll0 = np.where(mism, np.log(0.01 / 3), np.log1p(-0.01)).sum(axis=1)
    post0 = np.exp(ll0 - ll0.max())
    post0 /= post0.sum()
    best0 = rng.choice(np.flatnonzero(post0 == post0.max()))
    mapq0[r] = min(60.0, -10 * np.log10(max(1.0 - post0[best0], 1e-12)))
    wrong0[r] = cands[best0] != t

fig, ax = bio.canvas(24.0, 10.0)
a = C.axes_at(ax, (2.0, 1.6, 8.6, 7.6))
from scipy.stats import beta as _beta
edges = [0, 1, 2, 4, 7, 10, 15, 20, 25, 30, 35, 40, 50, 59.5, 61]
a.plot([0, 62], [0, 62], "--", color=C.line("neutral"), lw=0.9)
rows = []
for mq, wr, tok, dx in ((mapq, wrong, "dna", -0.6), (mapq0, wrong0, "negative", 0.6)):
    for lo, hi in zip(edges[:-1], edges[1:]):
        sel = (mq >= lo) & (mq < hi)
        n = int(sel.sum())
        if n < 10:
            continue
        k = int(wr[sel].sum())
        x_ = mq[sel].mean() + dx
        if k > 0:
            y_ = -10 * np.log10(k / n)
            lo_p, hi_p = _beta.ppf(0.025, k, n - k + 1), _beta.ppf(0.975, k + 1, n - k)
            a.errorbar([x_], [y_], yerr=[[y_ + 10 * np.log10(hi_p)], [-10 * np.log10(lo_p) - y_]], fmt="o", ms=4.5,
                       color=C.line(tok), ecolor=C.line(tok), elinewidth=0.9, capsize=2, zorder=5)
        else:
            y_ = -10 * np.log10(3.0 / n)
            a.plot([x_], [y_], "^", ms=5.5, color=C.line(tok), zorder=5)
        rows.append((tok, round(x_ - dx, 1), k, n, round(y_, 1)))
a.plot([], [], "o", ms=4.5, color=C.line("dna"), label="posterior with base qualities")
a.plot([], [], "o", ms=4.5, color=C.line("negative"), label="qualities ignored (all bases Q20)")
a.plot([], [], "^", ms=5.5, color=C.line("neutral"), label="no error in bin: bound -10 log10(3/n)")
a.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=bio.P.ink(), loc="upper left")
a.set_xlim(-1, 63)
a.set_ylim(-1, 63)
C.style_axes(a, "reported MAPQ (bin mean)", "empirical MAPQ, -10 log10(error rate)", box=True)
C.title(a, "A  Calibration")
b = C.axes_at(ax, (14.0, 1.6, 9.0, 7.6))
names = ["unique", "diverged repeat", "identical copies"]
toks = ["dna", "positive", "negative"]
bins = np.arange(0, 64, 3)
for k_, (nm, tk) in enumerate(zip(names, toks)):
    sel = klass == k_
    b.hist(mapq[sel], bins=bins, histtype="step", lw=1.4, color=C.line(tk),
           label=f"{nm} (n = {sel.sum()}, {100 * wrong[sel].mean():.1f} % wrong)")
b.set_yscale("log")
C.style_axes(b, "MAPQ", "reads")
b.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=bio.P.ink(), loc="upper center")
C.title(b, "B  MAPQ by origin of the read")
print("summary", [(names[k_], int((klass == k_).sum()), round(100 * wrong[klass == k_].mean(), 2)) for k_ in range(3)])
print("bins", rows)
