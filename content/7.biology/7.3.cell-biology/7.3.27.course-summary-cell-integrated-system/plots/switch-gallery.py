"""Six circuits of the course, simulated with the equations and parameters of their own chapters.

A: positive feedback with cooperativity, Eq. (18.2) with K = 0.5, n = 4, f = 0.8: two stable
branches (solid) joined by an unstable one (dashed) between the fold points: bistability and
hysteresis. B: the Rab5 -> Rab7 cut-out switch, Eq. (8.3) (parameters of 7.3.8, c = 0.02, h = 1.5).
C: the caspase switch, Eq. (25.1) (a = b = 1, c = 32, d = 0.1, p = q = 0.02, e = 4 per minute):
stronger stimuli shorten the delay, but every rise is equally steep. D: the cyclin B-Cdk1
oscillator, Eq. (20.1) (parameters of 7.3.20). E: the Hes1 delayed negative feedback, Eq. (24.4)
(tau = 18.7 min). F: perfect adaptation by an incoherent feed-forward loop, Eq. (18.3)
(tau_Y = 5, tau_R = 1), for stimulus steps 1 -> 2 -> 4.
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts, quant

P = bio.P
L = quant.line_color

fig, axs = plt.subplots(2, 3, figsize=(12.5, 6.6))
(aA, aB, aC), (aD, aE, aF) = axs

# A: bistable positive feedback, steady states s = x - f x^n / (K^n + x^n)
K, N, f = 0.5, 4, 0.8
x = np.linspace(0, 1.3, 2000)
s = x - f * x ** N / (K ** N + x ** N)
ds = np.gradient(s, x)
stable = ds > 0
for mask, ls in ((stable, "-"), (~stable, "--")):
    xs = np.where(mask, x, np.nan)
    aA.plot(s, xs, color=L("enzyme"), lw=1.8, ls=ls)
aA.annotate("", xy=(0.215, 0.95), xytext=(0.215, 0.12),
            arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.9))
aA.annotate("", xy=(0.05, 0.08), xytext=(0.05, 0.72),
            arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.9))
aA.set(xlim=(-0.05, 0.4), ylim=(0, 1.3))
charts.style_axes(aA, "stimulus s", "steady activity x")
charts.title(aA, "A  positive feedback: memory (Eq. 18.2)")

# B: Rab5 -> Rab7 cut-out switch
k5, f5, K5, g5 = 0.02, 1.0, 0.5, 0.15
k7, Kc, f7, K7, g7, Kh = 0.001, 0.7, 0.6, 0.5, 0.1, 0.4
c_, h_ = 0.02, 1.5


def rab(t, y):
    r5, r7 = y
    return [(k5 + f5 * r5 ** 2 / (K5 ** 2 + r5 ** 2)) * (1 - r5) - (g5 + h_ * r7 ** 4 / (Kh ** 4 + r7 ** 4)) * r5,
            (k7 + c_ * r5 ** 4 / (Kc ** 4 + r5 ** 4) + f7 * r7 ** 2 / (K7 ** 2 + r7 ** 2)) * (1 - r7) - g7 * r7]


t = np.linspace(0, 60, 1200)
sol = solve_ivp(rab, (0, 60), [0.05, 0.0], t_eval=t, rtol=1e-8, max_step=0.05)
aB.plot(t, sol.y[0], color=L("positive"), lw=1.8)
aB.plot(t, sol.y[1], color=L("negative"), lw=1.8)
aB.text(8, 0.85, "Rab5", color=L("positive"), fontsize=8)
aB.text(45, 0.85, "Rab7", color=L("negative"), fontsize=8)
aB.set(ylim=(0, 1.05))
charts.style_axes(aB, "t / min", "active fraction")
charts.title(aB, "B  Rab conversion: handover (Eq. 8.3)")

# C: caspase switch with variable delay
a, b, c, d, p, q, e = 1.0, 1.0, 32.0, 0.1, 0.02, 0.02, 4.0


def casp(t, Y, u):
    xx, yy, zz = Y
    return [(u + a * yy) * (1 - xx) - d * xx, b * xx * (1 - yy) - (c * zz + d) * yy, p - (q + e * yy) * zz]


tc = np.linspace(0, 1500, 6001)
for u, tok in ((0.0045, "negative"), (0.006, "enzyme"), (0.01, "receptor"), (0.03, "positive")):
    sc = solve_ivp(casp, (0, 1500), [0.0, 0.0, 1.0], args=(u,), method="LSODA", rtol=1e-7, atol=1e-10,
                   dense_output=True)
    aC.plot(tc / 60, sc.sol(tc)[1], color=L(tok), lw=1.6, label=f"u = {u:g}")
sc = solve_ivp(casp, (0, 1500), [0.0, 0.0, 1.0], args=(0.002,), method="LSODA", rtol=1e-7, atol=1e-10,
               dense_output=True)
aC.plot(tc / 60, sc.sol(tc)[1], color=P.muted(), lw=1.2, ls=":", label="u = 0.002")
aC.legend(frameon=False, fontsize=6.8, loc="center right", labelcolor=P.ink())
aC.set(ylim=(0, 1.05), xlim=(0, 25))
charts.style_axes(aC, "t / h", "active caspase-3")
charts.title(aC, "C  caspase switch: delay, then all (Eq. 25.1)")

# D: Cdk1 oscillator
BASE = dict(ks=2.0, K=20.0, n=4, k25a=0.03, k25b=1.0, kwa=0.02, kwb=0.2, kd0=0.01, kd1=0.4, ka=0.3, Ka=20.0, m=4,
            ki=0.08)


def cdk(t, y, pp=BASE):
    C, uu, A = y
    hh = uu ** pp["n"] / (pp["K"] ** pp["n"] + uu ** pp["n"])
    kd = pp["kd0"] + pp["kd1"] * A
    du = (pp["k25a"] + pp["k25b"] * hh) * (C - uu) - (pp["kwa"] + pp["kwb"] * (1 - hh)) * uu - kd * uu
    g = uu ** pp["m"] / (pp["Ka"] ** pp["m"] + uu ** pp["m"])
    return [pp["ks"] - kd * C, du, pp["ka"] * g * (1 - A) - pp["ki"] * A]


sd = solve_ivp(cdk, (0, 400), [0.0, 0.0, 0.0], max_step=0.2, rtol=1e-8, atol=1e-10)
aD.plot(sd.t, sd.y[0], color=L("chromatin"), lw=1.4, ls="--", label="total cyclin B–Cdk1")
aD.plot(sd.t, sd.y[1], color=L("negative"), lw=1.8, label="active Cdk1")
aD.legend(frameon=False, fontsize=6.8, loc="upper left", labelcolor=P.ink())
aD.set(xlim=(0, 400), ylim=(-2, 78))
charts.style_axes(aD, "t / min", "concentration (a.u.)")
charts.title(aD, "D  Cdk1: relaxation oscillator (Eq. 20.1)")

# E: Hes1 delayed negative feedback
am, ap, mm, mp, p0, nn, tau = 1.0, 1.0, np.log(2) / 24, np.log(2) / 22.3, 100.0, 5, 18.7
dt, T = 0.05, 1500.0
steps, lag = int(T / dt), int(round(tau / dt))
m_ = np.zeros(steps + 1)
p_ = np.zeros(steps + 1)
m_[0], p_[0] = 3.0, 100.0
for i in range(steps):
    pd = p_[i - lag] if i >= lag else p_[0]
    m_[i + 1] = m_[i] + dt * (am / (1 + (pd / p0) ** nn) - mm * m_[i])
    p_[i + 1] = p_[i] + dt * (ap * m_[i] - mp * p_[i])
th = np.arange(steps + 1) * dt / 60
aE.plot(th, p_, color=L("dna"), lw=1.8, label="Hes1 protein")
aE.plot(th, m_ * 10, color=L("mrna"), lw=1.3, ls="--", label="mRNA × 10")
aE.legend(frameon=False, fontsize=6.8, loc="upper right", labelcolor=P.ink())
aE.set(xlim=(0, 25))
charts.style_axes(aE, "t / h", "molecules (a.u.)")
charts.title(aE, "E  Hes1: delayed negative feedback (Eq. 24.4)")

# F: incoherent feed-forward adaptation
tauY, tauR = 5.0, 1.0


def S_of(tt):
    return 1.0 if tt < 10 else 2.0 if tt < 30 else 4.0


def iffl(tt, y):
    Y_, R_ = y
    S = S_of(tt)
    return [(S - Y_) / tauY, (S / Y_ - R_) / tauR]


tf = np.linspace(0, 50, 2001)
sf = solve_ivp(iffl, (0, 50), [1.0, 1.0], t_eval=tf, max_step=0.02)
aF.plot(tf, sf.y[1], color=L("receptor"), lw=1.8, label="output R")
aF.step(tf, [S_of(tt) / 2 for tt in tf], where="post", color=P.muted(), lw=1.0, ls=":", label="stimulus S / 2")
aF.legend(frameon=False, fontsize=6.8, loc="upper left", labelcolor=P.ink())
aF.set(ylim=(0, 2.3))
charts.style_axes(aF, "t (units of τ_R)", "response")
charts.title(aF, "F  feed-forward loop: adaptation (Eq. 18.3)")

fig.tight_layout()
