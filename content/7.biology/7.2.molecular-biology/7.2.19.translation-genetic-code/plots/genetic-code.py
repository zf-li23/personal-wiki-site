# Structure of the standard genetic code, computed from the code table.
# A: degeneracy: number of amino acids encoded by 1, 2, 3, 4 or 6 codons (Ile is the only 3-codon amino acid).
# B: fraction of single-nucleotide substitutions at each codon position that are synonymous, missense or
#    nonsense (all 61 sense codons x 3 alternative bases); the third position is mostly synonymous.
# C: error robustness. Cost of a code = mean squared change of Kyte-Doolittle hydropathy over all single-base
#    missense substitutions. The standard code is compared with 20000 random codes obtained by shuffling the
#    20 amino acids among the 20 synonymous codon blocks of the standard code (stop codons fixed).
import itertools

import matplotlib.pyplot as plt
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
BASES = "UCAG"
AA = ("FFLLSSSSYY**CC*W" "LLLLPPPPHHQQRRRR" "IIIMTTTTNNKKSSRR" "VVVVAAAADDEEGGGG")
code = {a + b + c: AA[16 * i + 4 * j + k] for (i, a), (j, b), (k, c) in
        itertools.product(enumerate(BASES), enumerate(BASES), enumerate(BASES))}
codons = list(code)

KD = {"A": 1.8, "R": -4.5, "N": -3.5, "D": -3.5, "C": 2.5, "Q": -3.5, "E": -3.5, "G": -0.4, "H": -3.2, "I": 4.5,
      "L": 3.8, "K": -3.9, "M": 1.9, "F": 2.8, "P": -1.6, "S": -0.8, "T": -0.7, "W": -0.9, "Y": -1.3, "V": 4.2}

fig, axs = plt.subplots(1, 3, figsize=(12.0, 3.7), gridspec_kw={"width_ratios": [1, 1.1, 1.3]})

# A: degeneracy
counts = {}
for aa in set(code.values()) - {"*"}:
    n = sum(1 for c in codons if code[c] == aa)
    counts[n] = counts.get(n, 0) + 1
ks = [1, 2, 3, 4, 6]
ax = axs[0]
ax.bar([str(k) for k in ks], [counts.get(k, 0) for k in ks], color=P.fill("protein"), edgecolor=P.edge("protein"))
for i, k in enumerate(ks):
    ax.text(i, counts.get(k, 0) + 0.2, str(counts.get(k, 0)), ha="center", va="bottom", fontsize=8, color=P.ink())
ax.set_ylim(0, 11)
charts.style_axes(ax, "codons per amino acid", "number of amino acids")
ax.set_title("A   Degeneracy", loc="left", fontsize=9, color=P.ink())

# B: substitution classes by codon position
frac = np.zeros((3, 3))
for c in codons:
    if code[c] == "*":
        continue
    for pos in range(3):
        for b in BASES:
            if b == c[pos]:
                continue
            m = c[:pos] + b + c[pos + 1:]
            k = 0 if code[m] == code[c] else (2 if code[m] == "*" else 1)
            frac[pos, k] += 1
frac /= frac.sum(axis=1, keepdims=True)
ax = axs[1]
left = np.zeros(3)
for k, (name, tok) in enumerate([("synonymous", "positive"), ("missense", "rna"), ("nonsense", "negative")]):
    ax.barh(["1st", "2nd", "3rd"], frac[:, k], left=left, color=P.fill(tok), edgecolor=P.edge(tok), label=name)
    left += frac[:, k]
ax.invert_yaxis()
ax.set_xlim(0, 1)
ax.legend(fontsize=7, frameon=False, loc="upper center", bbox_to_anchor=(0.5, -0.22), ncol=3)
charts.style_axes(ax, "fraction of single-base substitutions", "codon position")
ax.set_title("B   Effect of point substitutions", loc="left", fontsize=9, color=P.ink())


# C: robustness against random codes
def cost(assign):
    tot, n = 0.0, 0
    for c in codons:
        a = assign[c]
        if a == "*":
            continue
        for pos in range(3):
            for b in BASES:
                if b != c[pos]:
                    m = assign[c[:pos] + b + c[pos + 1:]]
                    if m != "*":
                        tot += (KD[a] - KD[m]) ** 2
                        n += 1
    return tot / n


# vectorized version for the random codes
idx = {c: i for i, c in enumerate(codons)}
aas = sorted(KD)
block = np.array([aas.index(code[c]) if code[c] != "*" else -1 for c in codons])
pairs = []
for c in codons:
    for pos in range(3):
        for b in BASES:
            if b != c[pos]:
                pairs.append((idx[c], idx[c[:pos] + b + c[pos + 1:]]))
pairs = np.array(pairs)
ok = (block[pairs[:, 0]] >= 0) & (block[pairs[:, 1]] >= 0)
pairs = pairs[ok]
ga, gb = block[pairs[:, 0]], block[pairs[:, 1]]
kd = np.array([KD[a] for a in aas])
std = np.mean((kd[ga] - kd[gb]) ** 2)
rng = np.random.default_rng(0)
N = 20000
perms = np.argsort(rng.random((N, 20)), axis=1)
vals = kd[perms]  # vals[r, block] = hydropathy assigned to that block
rand = np.mean((vals[:, ga] - vals[:, gb]) ** 2, axis=1)
better = np.mean(rand <= std)
assert abs(std - cost(code)) < 1e-9

ax = axs[2]
ax.hist(rand, bins=60, color=P.fill("neutral"), edgecolor=P.edge("neutral"), lw=0.3)
ax.axvline(std, color=charts.line("negative"), lw=1.6)
ax.text(std + 0.3, ax.get_ylim()[1] * 0.85, f"standard code\nbetter than {100 * (1 - better):.1f}%\nof random codes",
        fontsize=7.5, color=P.ink(), va="top")
charts.style_axes(ax, "mean squared hydropathy change", "random codes")
ax.set_title("C   Robustness to point errors", loc="left", fontsize=9, color=P.ink())
fig.tight_layout()
