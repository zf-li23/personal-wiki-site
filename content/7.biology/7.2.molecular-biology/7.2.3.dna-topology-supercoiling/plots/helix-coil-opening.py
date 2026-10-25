# Helix-coil (zipper) model of DNA melting under torque, solved exactly by transfer matrices.
# Each base pair n is helical (h) or open (c). Weight of a configuration: s_n for every helical pair and
# sigma for every h/c boundary, with s_n = exp(dE_n / RT), dE_n = E_c - E_h the free-energy cost of opening
# pair n, and sigma = exp(-J / RT) the boundary (nucleation) penalty. A negative torque tau lowers the cost of
# opening by tau * theta0 per pair, theta0 = 2 pi / 10.5 being the twist released when one pair melts.
# Parameters (two-state model): dE_AT = 3.60 kJ/mol, dE_GC = 7.82 kJ/mol, J = 18.8 kJ/mol, T = 310 K.
# The sequence is synthetic: 5000 bp of random DNA with 50 % GC, an AT-rich block of 400 bp (85 % AT,
# like a replication origin) and a shorter, weaker AT-rich block of 90 bp (80 % AT).
# The forward-backward recursion gives the exact probability P(c_n) that pair n is open.
import numpy as np
import wikibio as bio
from wikibio import charts as C

R, T = 8.314, 310.0
RT = R * T
NA = 6.02214076e23
dE = {"A": 3600.0, "T": 3600.0, "G": 7820.0, "C": 7820.0}
J = 18800.0
theta0 = 2 * np.pi / 10.5

rng = np.random.default_rng(7)
N = 5000


def block(n, gc):
    return rng.choice(list("AGCT"), n, p=[(1 - gc) / 2, gc / 2, gc / 2, (1 - gc) / 2])


seq = block(N, 0.5)
seq[2300:2700] = block(400, 0.15)
seq[3700:3790] = block(90, 0.20)


def open_probability(tau_pn_nm):
    """P(pair n is open) for a torque tau (pN nm, positive number = magnitude of the negative torque)."""
    work = tau_pn_nm * 1e-21 * theta0 * NA          # J/mol released per opened pair
    s = np.exp(np.array([dE[b] for b in seq]) / RT - work / RT)
    sig = np.exp(-J / RT)
    # forward vectors a[n] = (weight ending in h, weight ending in c), normalised at each step
    a = np.empty((N, 2))
    a[0] = (s[0], 1.0)
    a[0] /= a[0].sum()
    for n in range(1, N):
        h = s[n] * (a[n - 1, 0] + sig * a[n - 1, 1])
        c = sig * a[n - 1, 0] + a[n - 1, 1]
        a[n] = (h, c)
        a[n] /= h + c
    b = np.empty((N, 2))
    b[-1] = (1.0, 1.0)
    for n in range(N - 2, -1, -1):
        h = s[n + 1] * b[n + 1, 0] + sig * b[n + 1, 1]
        c = sig * s[n + 1] * b[n + 1, 0] + b[n + 1, 1]
        b[n] = (h, c)
        b[n] /= h + c
    p = a * b
    return p[:, 1] / p.sum(axis=1)


x = np.arange(1, N + 1)
fig, ax = bio.canvas(20, 9.4)
P = bio.P

# A: GC content in a 50-bp window
top = C.axes_at(ax, (1.6, 6.8, 18.0, 1.6))
gc = np.convolve(np.isin(seq, ["G", "C"]).astype(float), np.ones(50) / 50, mode="same")
top.fill_between(x, gc, color=P.fill("dna"), lw=0)
top.plot(x, gc, color=C.line("dna"), lw=0.8)
top.set_xlim(1, N)
top.set_ylim(0, 1)
top.set_yticks([0, 0.5, 1])
top.set_xticks([])
C.style_axes(top, None, "GC fraction")
bio.panel(ax, "A", (0.15, 9.1))
bio.label(ax, (1.6 + 18.0 * 2500 / N, 8.75), "AT-rich block, 400 bp", size="tiny", color=P.muted())
bio.label(ax, (1.6 + 18.0 * 3745 / N, 8.75), "90 bp", size="tiny", color=P.muted())

# B: open probability along the sequence
low = C.axes_at(ax, (1.6, 1.3, 11.6, 4.5))
curves = [(0, "neutral", "τ = 0"), (11.5, "highlight", "τ = −11.5 pN nm"), (13, "negative", "τ = −13 pN nm")]
for tau, tok, text in curves:
    low.plot(x, open_probability(tau), color=C.line(tok), lw=1.4, label=text)
low.set_xlim(1, N)
low.set_ylim(-0.02, 1.02)
low.set_yticks([0, 0.5, 1])
low.set_xticks([1, 1000, 2000, 3000, 4000, 5000])
C.style_axes(low, "Base-pair position n", "P(pair n open)")
leg = low.legend(loc="upper left", frameon=False, fontsize=bio.core.FONT["tiny"])
for t in leg.get_texts():
    t.set_color(P.ink())
bio.panel(ax, "B", (0.15, 6.3))

# C: titration of the two blocks with torque
tit = C.axes_at(ax, (15.0, 1.3, 4.6, 4.5))
taus = np.linspace(9, 15, 49)
big, small = [], []
for tau in taus:
    p = open_probability(tau)
    big.append(p[2300:2700].mean())
    small.append(p[3700:3790].mean())
tit.plot(taus, big, color=C.line("negative"), lw=1.6, label="400 bp block")
tit.plot(taus, small, color=C.line("dna"), lw=1.6, ls=(0, (4, 2)), label="90 bp block")
tit.set_xlim(9, 15)
tit.set_ylim(-0.02, 1.02)
tit.set_xticks([9, 11, 13, 15], ["−9", "−11", "−13", "−15"])
tit.set_yticks([0, 0.5, 1])
C.style_axes(tit, "τ / (pN nm)", "Mean P(open)")
leg = tit.legend(loc="upper left", frameon=False, fontsize=bio.core.FONT["tiny"])
for t in leg.get_texts():
    t.set_color(P.ink())
bio.panel(ax, "C", (13.6, 6.3))
