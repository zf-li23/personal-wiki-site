"""Maximum likelihood estimation of the distance t and omega from two coding sequences under the codon
model of Eq. (23.1). Two sequences of 400 codons were simulated from a common ancestor drawn from the
stationary distribution (F3x4 frequencies resembling an AT-rich gene), evolving for a total distance
t = 0.6 nucleotide substitutions per codon with kappa = 2.5 and omega = 0.2. A: log likelihood
surface in (t, omega) with kappa fixed at its true value, contours 2, 5, 10, 20 and 50 units below the
maximum (cross: MLE; dot: true values). B: profile log likelihood of omega (kappa and t maximized);
the approximate 95 % interval is where it lies within 1.92 of the maximum (shaded)."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm
from scipy.optimize import minimize
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
rng = np.random.default_rng(7)
B = "TCAG"
AA = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
codons = [a + b + c for a in B for b in B for c in B]
code = dict(zip(codons, AA))
sense = [c for c in codons if code[c] != "*"]
n = len(sense)
pos = [{"T": 0.30, "C": 0.20, "A": 0.28, "G": 0.22}, {"T": 0.28, "C": 0.22, "A": 0.30, "G": 0.20},
       {"T": 0.40, "C": 0.15, "A": 0.30, "G": 0.15}]
pi = np.array([pos[0][c[0]] * pos[1][c[1]] * pos[2][c[2]] for c in sense])
pi /= pi.sum()
TS = np.zeros((n, n), bool)
NS = np.zeros((n, n), bool)
ONE = np.zeros((n, n), bool)
for i, c in enumerate(sense):
    for j, d in enumerate(sense):
        diff = [k for k in range(3) if c[k] != d[k]]
        if len(diff) == 1:
            ONE[i, j] = True
            k = diff[0]
            TS[i, j] = {c[k], d[k]} in ({"A", "G"}, {"C", "T"})
            NS[i, j] = code[c] != code[d]


def qmat(kappa, omega):
    q = np.where(ONE, pi[None, :], 0.0)
    q = q * np.where(TS, kappa, 1.0) * np.where(NS, omega, 1.0)
    np.fill_diagonal(q, 0.0)
    np.fill_diagonal(q, -q.sum(1))
    return q / (-(pi * np.diag(q)).sum())


def simulate(L, t, kappa, omega):
    pt = expm(qmat(kappa, omega) * t / 2)
    anc = rng.choice(n, L, p=pi)
    s1 = np.array([rng.choice(n, p=pt[x]) for x in anc])
    s2 = np.array([rng.choice(n, p=pt[x]) for x in anc])
    return s1, s2


s1, s2 = simulate(400, 0.6, 2.5, 0.2)
counts = np.zeros((n, n))
np.add.at(counts, (s1, s2), 1)


def loglik(t, kappa, omega):
    pt = expm(qmat(kappa, omega) * t)
    return float((counts * np.log(pi[:, None] * pt + 1e-300)).sum())


res = minimize(lambda v: -loglik(*np.exp(v)), np.log([0.5, 2.0, 0.3]), method="Nelder-Mead",
               options=dict(xatol=1e-4, fatol=1e-4))
that, khat, what = np.exp(res.x)
lmax = -res.fun
fig, (a, b) = plt.subplots(1, 2, figsize=(10.0, 3.8))
fig.subplots_adjust(left=0.08, right=0.98, bottom=0.15, top=0.9, wspace=0.3)
ts = np.linspace(0.3, 1.0, 26)
ws = np.linspace(0.05, 0.5, 26)
Z = np.array([[loglik(t, 2.5, w) for t in ts] for w in ws])
cs = a.contour(ts, ws, Z.max() - Z, levels=[2, 5, 10, 20, 50], colors=[charts.line("dna")], linewidths=0.9)
a.clabel(cs, fontsize=FT["tiny"], fmt="%g")
a.scatter([0.6], [0.2], color=P.ink(), s=16, zorder=4)
a.scatter([that], [what], marker="x", color=charts.line("negative"), s=30, zorder=5)
charts.style_axes(a, "distance $t$ (substitutions per codon)", "$\\omega$")
charts.title(a, "A  Log likelihood surface ($\\kappa = 2.5$)")
wg = np.linspace(0.08, 0.45, 24)
prof = []
x0 = np.log([that, khat])
for w in wg:
    r = minimize(lambda v: -loglik(np.exp(v[0]), np.exp(v[1]), w), x0, method="Nelder-Mead",
                 options=dict(xatol=1e-3, fatol=1e-3))
    prof.append(-r.fun - lmax)
    x0 = r.x
prof = np.array(prof)
b.plot(wg, prof, color=charts.line("dna"), lw=1.8)
inside = prof > -1.92
b.fill_between(wg, -12, 0.5, where=inside, color=P.fill("dna"), alpha=0.35, lw=0)
b.axhline(-1.92, color=P.muted(), lw=0.8, ls="--")
b.axvline(0.2, color=P.ink(), lw=0.8, ls=":")
b.set_ylim(-12, 0.5)
b.text(what, -11, f"$\\hat\\omega = {what:.3f}$", fontsize=FT["tiny"], color=P.ink(), ha="center")
charts.style_axes(b, "$\\omega$", "profile log likelihood $-\\,\\ell_{\\max}$")
charts.title(b, "B  Profile likelihood of $\\omega$")
