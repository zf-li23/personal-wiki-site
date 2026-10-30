"""A toggle switch for gonadal fate: testis module S (SOX9, FGF9, PGD2) and ovary module W (WNT4/RSPO1/beta-catenin,
FOXL2) with self-activation and mutual repression, driven by a transient SRY pulse."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import wikibio as bio
from wikibio import charts

P_ = bio.P
FT = bio.core.FONT
aS, aW, b, K = 0.05, 0.15, 3.0, 0.6


def rhs(S, W, sig):
    dS = (aS + S * S / (1 + S * S)) / (1 + (W / K) ** 2) * b + sig - S
    dW = (aW + W * W / (1 + W * W)) / (1 + (S / K) ** 2) * b - W
    return dS, dW


def run(A, t0, d=1.0, T=20.0, dt=0.01, S0=0.05, W0=0.05, keep=False):
    S = np.full(np.shape(A), S0, float)
    W = np.full(np.shape(A), W0, float)
    tr = []
    for k in range(int(T / dt)):
        t = k * dt
        sig = np.where((t >= t0) & (t < t0 + d), A, 0.0)
        dS, dW = rhs(S, W, sig)
        S, W = S + dt * dS, W + dt * dW
        if keep:
            tr.append((t, float(S), float(W)))
    return (S, W, np.array(tr)) if keep else (S, W)


fig, axs = plt.subplots(1, 4, figsize=(14.0, 3.6))
fig.subplots_adjust(left=0.05, right=0.985, bottom=0.17, top=0.86, wspace=0.36)
a = axs[0]
s = np.linspace(0.005, 3.4, 600)
fS = aS + s * s / (1 + s * s)
wS = K * np.sqrt(np.clip(b * fS / s - 1, 0, None))
a.plot(s, wS, color=charts.line("drug"), lw=1.5, label="S nullcline")
w = np.linspace(0.005, 3.4, 600)
gW = aW + w * w / (1 + w * w)
sW = K * np.sqrt(np.clip(b * gW / w - 1, 0, None))
a.plot(sW, w, color=charts.line("dna"), lw=1.5, label="W nullcline")
fps = set()
for g in [(0.01, 3.0), (2.8, 0.02), (0.6, 0.6), (0.4, 0.8), (0.8, 0.4)]:
    r = fsolve(lambda v: rhs(v[0], v[1], 0.0), g)
    if np.allclose(rhs(r[0], r[1], 0.0), 0, atol=1e-8):
        fps.add((round(r[0], 4), round(r[1], 4)))
for (x, y) in fps:
    stable = abs(x - y) > 1.0
    a.plot(x, y, "o", ms=6, color=P_.ink(), mfc=P_.ink() if stable else P_.surface())
_, _, tr1 = run(1.5, 1.0, keep=True)
_, _, tr0 = run(0.0, 1.0, keep=True)
a.plot(tr1[:, 1], tr1[:, 2], color=charts.line("positive"), lw=1.2)
a.plot(tr0[:, 1], tr0[:, 2], color=charts.line("positive"), lw=1.2, ls="--")
a.set_xlim(0, 3.4)
a.set_ylim(0, 3.4)
a.text(2.3, 0.25, "testis", fontsize=FT["tiny"], color=P_.ink())
a.text(0.12, 3.0, "ovary", fontsize=FT["tiny"], color=P_.ink())
a.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="center right")
charts.style_axes(a, "testis module S", "ovary module W")
charts.title(a, "A  Phase plane")

c2 = axs[1]
for t0, ls, lab in ((1.0, "-", "SRY at t = 1"), (4.0, "--", "SRY at t = 4")):
    _, _, tr = run(1.5, t0, T=12.0, keep=True)
    c2.plot(tr[:, 0], tr[:, 1], color=charts.line("drug"), lw=1.5, ls=ls, label="S, " + lab)
    c2.plot(tr[:, 0], tr[:, 2], color=charts.line("dna"), lw=1.5, ls=ls, label="W, " + lab)
c2.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P_.ink(), loc="center right")
charts.style_axes(c2, "time", "activity")
charts.title(c2, "B  Early and late SRY")

c = axs[2]
t0s = np.linspace(0, 8, 41)
As = np.linspace(0, 6, 41)
TT, AA = np.meshgrid(t0s, As)
S, W = run(AA, TT)
c.contourf(TT, AA, (S > W).astype(float), levels=[-0.5, 0.5, 1.5], colors=[P_.light("receptor"), P_.light("enzyme")])
c.contour(TT, AA, (S > W).astype(float), levels=[0.5], colors=[P_.ink()], linewidths=1.0)
c.text(1.0, 5.0, "testis", fontsize=FT["small"], color=P_.on_fill())
c.text(5.0, 0.8, "ovary", fontsize=FT["small"], color=P_.on_fill())
charts.style_axes(c, "SRY onset t0", "SRY amplitude A", box=True)
charts.title(c, "C  Time window")

d = axs[3]
rng = np.random.default_rng(0)
amps = 1.5 * np.exp(0.35 * rng.standard_normal(300))
t0s2 = np.linspace(0, 4, 33)
frac = []
for t0 in t0s2:
    S, W = run(amps, t0)
    frac.append(np.mean(S > W))
d.plot(t0s2, frac, color=charts.line("enzyme"), lw=1.7)
d.axhspan(0.1, 0.9, color=P_.light("highlight"), lw=0)
d.text(0.2, 0.5, "ovotestis", fontsize=FT["tiny"], color=P_.ink())
d.set_ylim(-0.03, 1.03)
charts.style_axes(d, "SRY onset t0", "fraction of Sertoli cells")
charts.title(d, "D  Variable SRY levels")
