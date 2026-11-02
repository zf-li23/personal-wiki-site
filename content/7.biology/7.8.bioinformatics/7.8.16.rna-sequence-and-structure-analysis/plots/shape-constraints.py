# Chemical probing data as folding constraints (simulated reactivities). The tRNA-Phe sequence and the
# simplified energy model of the previous figure. Reactivities are drawn from an exponential distribution
# with mean 0.2 for paired nucleotides of the native cloverleaf and mean 1.0 for unpaired ones, except that
# a fraction f of the unpaired nucleotides is protected (mean 0.2), as tertiary contacts and stacking
# protect many loop nucleotides of a real tRNA. Each reactivity S enters the minimum free energy
# computation as a pseudo-energy m ln(S + 1) + b per nucleotide in each stacked pair (Deigan and colleagues
# 2009; m = 10.9 and b = -3.3 kJ/mol). A: one simulated profile (f = 0.2) above the native pairing state.
# B: sensitivity (fraction of native pairs predicted) of the prediction without and with the constraints,
# mean and 10th-90th percentile band over 12 simulated profiles for each fraction of protected loop nucleotides.
# Simplified nearest-neighbor model (kJ/mol, 37 C), Zuker MFE and McCaskill partition function with sampling.
import math

import numpy as np
RT = 8.314462618e-3 * 310.15
K = 4.184
PAIRS = {('A','U'),('U','A'),('G','C'),('C','G'),('G','U'),('U','G')}
# Xia et al. (1998) Watson-Crick stacks, kcal/mol, written 5'XY3'/3'X'Y'5' with XY on one strand
WC = {'AA':-0.93,'UU':-0.93,'AU':-1.10,'UA':-1.33,'CU':-2.08,'AG':-2.08,'CA':-2.11,'UG':-2.11,
      'GU':-2.24,'AC':-2.24,'GA':-2.35,'UC':-2.35,'CG':-2.36,'GG':-3.26,'CC':-3.26,'GC':-3.42}
GU_STACK = -1.0 * K
def stack(s, i, j, k, l):
    # pair (i,j) outer, (k,l)=(i+1,j-1) inner
    a, b = s[i] + s[k], s[l] + s[j]   # 5' i k 3' on top strand, 5' l j 3' on bottom
    if (s[i], s[j]) in (('G','U'),('U','G')) or (s[k], s[l]) in (('G','U'),('U','G')):
        return GU_STACK
    return WC[a] * K
def au(s, i, j):
    return 0.0 if {s[i], s[j]} == {'G', 'C'} else 2.1
def hairpin(s, i, j):
    n = j - i - 1
    if n < 3: return math.inf
    return 22.6 + 1.75 * RT * math.log(n / 3) + au(s, i, j)
def interior(s, i, j, k, l):
    n1, n2 = k - i - 1, j - l - 1
    if n1 == 0 and n2 == 0: return stack(s, i, j, k, l)
    if n1 == 0 or n2 == 0:
        n = n1 + n2
        if n == 1: return 16.0 + stack(s, i, j, k, l)
        return 11.7 + 1.08 * RT * math.log(n / 2) + au(s, i, j) + au(s, k, l)
    n = n1 + n2
    return 8.4 + 1.08 * RT * math.log(n / 6) + min(2.5 * abs(n1 - n2), 12.6) + au(s, i, j) + au(s, k, l)
MA, MB, MC = 14.2, 1.7, 0.0   # multiloop: closing, per branch, per unpaired
MAXLOOP = 30

def can(s, i, j): return j - i > 3 and (s[i], s[j]) in PAIRS

def fold(s, shape=None, beta=1 / RT):
    n = len(s)
    # pseudo-energy per nucleotide for stacked pairs (Deigan et al. 2009): m ln(S+1) + b, kJ/mol
    ps = np.zeros(n) if shape is None else 10.9 * np.log(np.asarray(shape) + 1) - 3.3
    def IL(i, j, k, l):
        e = interior(s, i, j, k, l)
        if k == i + 1 and l == j - 1: e += ps[i] + ps[j] + ps[k] + ps[l]
        return e
    INF = math.inf
    V = np.full((n, n), INF); WM = np.full((n, n), INF); WM1 = np.full((n, n), INF)
    Qb = np.zeros((n, n)); Qm = np.zeros((n, n)); Qm1 = np.zeros((n, n))
    B = lambda e: math.exp(-beta * e)
    for d in range(4, n):
        for i in range(n - d):
            j = i + d
            if can(s, i, j):
                v = hairpin(s, i, j); q = B(v) if v < INF else 0.0
                for k in range(i + 1, min(i + MAXLOOP + 2, j - 4)):
                    for l in range(j - 1, k + 3, -1):
                        if (k - i - 1) + (j - l - 1) > MAXLOOP: break
                        if V[k, l] < INF:
                            e = IL(i, j, k, l)
                            v = min(v, e + V[k, l]); q += B(e) * Qb[k, l]
                cm = MA + MB + au(s, i, j)
                for u in range(i + 2, j - 1):
                    if WM[i + 1, u - 1] < INF and WM1[u, j - 1] < INF:
                        v = min(v, cm + WM[i + 1, u - 1] + WM1[u, j - 1])
                    q += B(cm) * Qm[i + 1, u - 1] * Qm1[u, j - 1]
                V[i, j] = v; Qb[i, j] = q
            # WM1: one stem starting at i, ending at l <= j, rest unpaired
            w1 = INF; q1 = 0.0
            for l in range(i + 4, j + 1):
                if V[i, l] < INF:
                    e = V[i, l] + MB + au(s, i, l) + MC * (j - l)
                    w1 = min(w1, e); q1 += Qb[i, l] * B(MB + au(s, i, l) + MC * (j - l))
            WM1[i, j] = w1; Qm1[i, j] = q1
            wm = INF; qm = 0.0
            for u in range(i, j - 3):
                left = MC * (u - i)
                if WM1[u, j] < INF:
                    wm = min(wm, left + WM1[u, j])
                    if u - 1 > i and WM[i, u - 1] < INF: wm = min(wm, WM[i, u - 1] + WM1[u, j])
                qm += (B(left) + (Qm[i, u - 1] if u - 1 > i else 0.0)) * Qm1[u, j]
            WM[i, j] = wm; Qm[i, j] = qm
    # exterior
    W = np.zeros(n + 1); Z = np.ones(n + 1)
    for j in range(1, n + 1):
        w = W[j - 1]; z = Z[j - 1]
        for i in range(1, j - 3):
            if V[i - 1, j - 1] < INF:
                e = V[i - 1, j - 1] + au(s, i - 1, j - 1)
                w = min(w, W[i - 1] + e)
                z += Z[i - 1] * Qb[i - 1, j - 1] * B(au(s, i - 1, j - 1))
        W[j] = w; Z[j] = z
    return dict(s=s, V=V, WM=WM, WM1=WM1, W=W, Qb=Qb, Qm=Qm, Qm1=Qm1, Z=Z, IL=IL, beta=beta, B=B)

def mfe_structure(F):
    s, V, WM, WM1, W, IL = F['s'], F['V'], F['WM'], F['WM1'], F['W'], F['IL']
    n = len(s); pairs = []; eps = 1e-6
    stack_ = [('W', n)]
    while stack_:
        t = stack_.pop()
        if t[0] == 'W':
            j = t[1]
            if j <= 0: continue
            if abs(W[j] - W[j - 1]) < eps: stack_.append(('W', j - 1)); continue
            for i in range(1, j - 3):
                if V[i - 1, j - 1] < math.inf and abs(W[j] - (W[i - 1] + V[i - 1, j - 1] + au(s, i - 1, j - 1))) < eps:
                    stack_ += [('W', i - 1), ('V', i - 1, j - 1)]; break
        elif t[0] == 'V':
            i, j = t[1], t[2]; pairs.append((i, j)); v = V[i, j]
            if abs(v - hairpin(s, i, j)) < eps: continue
            done = False
            for k in range(i + 1, min(i + MAXLOOP + 2, j - 4)):
                for l in range(j - 1, k + 3, -1):
                    if (k - i - 1) + (j - l - 1) > MAXLOOP: break
                    if V[k, l] < math.inf and abs(v - (IL(i, j, k, l) + V[k, l])) < eps:
                        stack_.append(('V', k, l)); done = True; break
                if done: break
            if done: continue
            cm = MA + MB + au(s, i, j)
            for u in range(i + 2, j - 1):
                if abs(v - (cm + WM[i + 1, u - 1] + WM1[u, j - 1])) < eps:
                    stack_ += [('WM', i + 1, u - 1), ('WM1', u, j - 1)]; break
        elif t[0] == 'WM1':
            i, j = t[1], t[2]
            for l in range(i + 4, j + 1):
                if V[i, l] < math.inf and abs(WM1[i, j] - (V[i, l] + MB + au(s, i, l) + MC * (j - l))) < eps:
                    stack_.append(('V', i, l)); break
        elif t[0] == 'WM':
            i, j = t[1], t[2]
            for u in range(i, j - 3):
                if WM1[u, j] < math.inf and abs(WM[i, j] - (MC * (u - i) + WM1[u, j])) < eps:
                    stack_.append(('WM1', u, j)); break
                if u - 1 > i and WM1[u, j] < math.inf and abs(WM[i, j] - (WM[i, u - 1] + WM1[u, j])) < eps:
                    stack_ += [('WM', i, u - 1), ('WM1', u, j)]; break
    return sorted(pairs), W[n]

def sample(F, rng, nsamp=1000):
    s, Qb, Qm, Qm1, Z, IL, B = F['s'], F['Qb'], F['Qm'], F['Qm1'], F['Z'], F['IL'], F['B']
    n = len(s); counts = np.zeros((n, n)); structs = []
    for _ in range(nsamp):
        pairs = []; todo = [('Z', n)]
        while todo:
            t = todo.pop()
            if t[0] == 'Z':
                j = t[1]
                if j <= 0: continue
                r = rng.random() * Z[j]; acc = Z[j - 1]
                if r < acc: todo.append(('Z', j - 1)); continue
                for i in range(1, j - 3):
                    acc += Z[i - 1] * Qb[i - 1, j - 1] * B(au(s, i - 1, j - 1))
                    if r < acc: todo += [('Z', i - 1), ('B', i - 1, j - 1)]; break
            elif t[0] == 'B':
                i, j = t[1], t[2]; pairs.append((i, j))
                r = rng.random() * Qb[i, j]; acc = B(hairpin(s, i, j)) if hairpin(s, i, j) < math.inf else 0
                if r < acc: continue
                done = False
                for k in range(i + 1, min(i + MAXLOOP + 2, j - 4)):
                    for l in range(j - 1, k + 3, -1):
                        if (k - i - 1) + (j - l - 1) > MAXLOOP: break
                        if Qb[k, l] > 0:
                            acc += B(IL(i, j, k, l)) * Qb[k, l]
                            if r < acc: todo.append(('B', k, l)); done = True; break
                    if done: break
                if done: continue
                cm = MA + MB + au(s, i, j)
                for u in range(i + 2, j - 1):
                    acc += B(cm) * Qm[i + 1, u - 1] * Qm1[u, j - 1]
                    if r < acc: todo += [('M', i + 1, u - 1), ('M1', u, j - 1)]; break
            elif t[0] == 'M1':
                i, j = t[1], t[2]; r = rng.random() * Qm1[i, j]; acc = 0
                for l in range(i + 4, j + 1):
                    acc += Qb[i, l] * B(MB + au(s, i, l) + MC * (j - l))
                    if r < acc: todo.append(('B', i, l)); break
            elif t[0] == 'M':
                i, j = t[1], t[2]; r = rng.random() * Qm[i, j]; acc = 0
                for u in range(i, j - 3):
                    acc += B(MC * (u - i)) * Qm1[u, j]
                    if r < acc: todo.append(('M1', u, j)); break
                    if u - 1 > i:
                        acc += Qm[i, u - 1] * Qm1[u, j]
                        if r < acc: todo += [('M', i, u - 1), ('M1', u, j)]; break
        for (i, j) in pairs: counts[i, j] += 1
        structs.append(sorted(pairs))
    return counts / nsamp, structs

def db(pairs, n):
    c = ['.'] * n
    for i, j in pairs: c[i] = '('; c[j] = ')'
    return ''.join(c)
def pairs_of(dbs):
    st = []; out = []
    for k, ch in enumerate(dbs):
        if ch == '(': st.append(k)
        elif ch == ')': out.append((st.pop(), k))
    return sorted(out)


import wikibio as bio
from wikibio import charts as C

P = bio.P
FT = bio.core.FONT
seq = "GCGGAUUUAGCUCAGUUGGGAGAGCGCCAGACUGAAGAUCUGGAGGUCCUGUGUUCGAUCCACAGAAUUCGCACCA"
native = "(((((((..((((........)))).(((((.......))))).....(((((.......))))))))))))...."
n = len(seq)
NP = set(pairs_of(native))
paired = np.array([ch != "." for ch in native])


def sens(pairs):
    return len(set(pairs) & NP) / len(NP)


base = sens(mfe_structure(fold(seq))[0])
rng = np.random.default_rng(2)
fr = [0.0, 0.2, 0.4, 0.6, 0.8]
res = []
example = None
for f in fr:
    r = []
    for rep in range(12):
        prot = rng.random(n) < f
        shp = np.where(paired | prot, rng.exponential(0.2, n), rng.exponential(1.0, n))
        if f == 0.2 and example is None:
            example = shp
        r.append(sens(mfe_structure(fold(seq, shape=shp))[0]))
    res.append(r)
res = np.array(res)

fig, ax = bio.canvas(28.0, 9.0)
a = C.axes_at(ax, (1.8, 1.5, 14.0, 6.6))
xs = np.arange(1, n + 1)
a.bar(xs, example, width=0.8, color=[C.line("dna") if p else C.line("rna") for p in paired])
a.set_xlim(0.5, n + 0.5)
C.style_axes(a, "nucleotide", "reactivity (simulated)")
a.text(2, example.max() * 0.95, "paired in native structure", color=C.line("dna"), fontsize=FT["tiny"])
a.text(2, example.max() * 0.86, "unpaired", color=C.line("rna"), fontsize=FT["tiny"])
b = C.axes_at(ax, (19.5, 1.5, 7.8, 6.6))
m = res.mean(1)
lo, hi = np.percentile(res, 10, 1), np.percentile(res, 90, 1)
b.fill_between(fr, lo, hi, color=P.light("positive"), lw=0)
b.plot(fr, m, "o-", color=C.line("positive"), lw=1.4, label="with simulated reactivities")
b.axhline(base, color=C.line("negative"), ls=(0, (4, 2)), lw=1.2, label="sequence only")
b.set_ylim(0, 1.05)
C.style_axes(b, "fraction of loop nucleotides protected", "sensitivity (native pairs found)")
b.legend(fontsize=FT["tiny"], frameon=False, labelcolor=P.ink(), loc="lower left")
bio.panel(ax, "A", (0.2, 8.6))
bio.panel(ax, "B", (17.6, 8.6))
