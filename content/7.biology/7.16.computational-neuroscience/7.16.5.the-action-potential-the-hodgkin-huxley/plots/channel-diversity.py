"""How extra channels change the firing pattern. A: firing rate against current for the Connor-Stevens
model (Na+, K+ delayed rectifier, leak, and the transient K+ A-current; gating functions of Dayan and
Abbott, Appendix 6A, per-area conductances x100 for uA/cm2) with the A-current (gA = 47.7 mS/cm2) and
without it (gA = 0, leak adjusted to keep V_rest and the input conductance): the A-current gives the
continuous (class 1) onset of firing, without it the rate jumps. B: the Connor-Stevens neuron
(with A-current) after current steps from rest to 8.8 and 12 uA/cm2: long first-spike latency and slow
interspike ramps while the A-current inactivates. C: spike-frequency adaptation by the M-current: a Hodgkin-Huxley neuron with an added slow
K+ current I_M = gM p (V - E_K), p relaxing with tau = 100 ms toward a sigmoid of V, under a 15 uA/cm2 step.
D: a passive membrane (g_L = 0.1 mS/cm2) with and without the
hyperpolarization-activated current I_h = gh r (V - E_h), gh = 0.1 mS/cm2, E_h = -30 mV, tau_r = 150 ms,
r_inf half-activation -75 mV (leak reversal adjusted so that both rest at -65 mV), during a 400 ms step of
-1 uA/cm2: I_h produces a depolarizing sag during the step and a rebound depolarization after it."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts, neuro

P = bio.P
FT = bio.core.FONT


def rk4(f, y, Iarr, dt):
    out = np.empty((len(Iarr),) + y.shape)
    for i in range(len(Iarr) - 1):
        out[i] = y
        Ia, Ib = Iarr[i], Iarr[i + 1]
        Im = 0.5 * (Ia + Ib)
        k1 = f(y, Ia); k2 = f(y + dt / 2 * k1, Im); k3 = f(y + dt / 2 * k2, Im); k4 = f(y + dt * k3, Ib)
        y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    out[-1] = y
    return out


# ---- Connor-Stevens (Dayan and Abbott 2001, Eq. 6.4 and Appendix A of chapter 6)
def x_safe(x):
    return np.where(np.abs(x) < 1e-7, 1e-7, x)


def cs_gates(V):
    am = 0.38 * x_safe(V + 29.7) / (1 - np.exp(-0.1 * x_safe(V + 29.7)))
    bm = 15.2 * np.exp(-0.0556 * (V + 54.7))
    ah = 0.266 * np.exp(-0.05 * (V + 48)); bh = 3.8 / (1 + np.exp(-0.1 * (V + 18)))
    an = 0.02 * x_safe(V + 45.7) / (1 - np.exp(-0.1 * x_safe(V + 45.7)))
    bn = 0.25 * np.exp(-0.0125 * (V + 55.7))
    ainf = (0.0761 * np.exp(0.0314 * (V + 94.22)) / (1 + np.exp(0.0346 * (V + 1.17)))) ** (1 / 3)
    taua = 0.3632 + 1.158 / (1 + np.exp(0.0497 * (V + 55.96)))
    binf = (1 / (1 + np.exp(0.0688 * (V + 53.3)))) ** 4
    taub = 1.24 + 2.678 / (1 + np.exp(0.0624 * (V + 50)))
    return am, bm, ah, bh, an, bn, ainf, taua, binf, taub


def cs_model(gA, gL, EL):
    gNa, gK, ENa, EK, EA = 120.0, 20.0, 55.0, -72.0, -75.0

    def f(y, I):
        V, m, h, n, a, b = y
        am, bm, ah, bh, an, bn, ainf, taua, binf, taub = cs_gates(V)
        iion = gL * (V - EL) + gNa * m**3 * h * (V - ENa) + gK * n**4 * (V - EK) + gA * a**3 * b * (V - EA)
        return np.array([I - iion, am * (1 - m) - bm * m, ah * (1 - h) - bh * h, an * (1 - n) - bn * n,
                         (ainf - a) / taua, (binf - b) / taub])
    return f


def cs_rest(gA, gL, EL):
    V = -68.0
    f = cs_model(gA, gL, EL)
    from scipy.optimize import brentq

    def steady(V):
        am, bm, ah, bh, an, bn, ainf, taua, binf, taub = cs_gates(V)
        return np.array([V, am / (am + bm), ah / (ah + bh), an / (an + bn), ainf, binf])
    g = lambda V: f(steady(V), 0.0)[0]
    V0 = brentq(g, -85, -50)
    return steady(V0), V0


# calibrate leak without A: same rest potential, same slope conductance
gA0, gL0, EL0 = 47.7, 0.3, -17.0
y0, V0 = cs_rest(gA0, gL0, EL0)
def iA(V, gA):
    am, bm, ah, bh, an, bn, ainf, taua, binf, taub = cs_gates(V)
    return gA * ainf**3 * binf * (V - (-75.0))
h = 1e-3
slopeA = (iA(V0 + h, gA0) - iA(V0 - h, gA0)) / (2 * h)
gL1 = gL0 + slopeA
EL1 = V0 - (gL0 * (V0 - EL0) + iA(V0, gA0)) / gL1

dt = 0.04
fig, axs = plt.subplots(2, 2, figsize=(10.0, 5.8))
fig.subplots_adjust(wspace=0.3, hspace=0.55, left=0.07, right=0.99, bottom=0.1, top=0.93)

ax = axs[0, 0]
Is = np.concatenate([np.arange(0, 8, 2.0), np.arange(8, 12.1, 0.5), np.arange(13, 25, 2.0), np.arange(25, 90, 5.0)])
T = 300.0
t = np.arange(0, T, dt)
for gA, gL, EL, tok, lab in [(gA0, gL0, EL0, "neuron", "with A-current"), (0.0, gL1, EL1, "negative", "A-current removed")]:
    y = cs_rest(gA, gL, EL)[0][:, None] * np.ones((1, len(Is)))
    Ia = np.tile(Is, (len(t), 1))
    # record V only
    f = cs_model(gA, gL, EL)
    yy = y.copy(); Vs = np.empty((len(t), len(Is)))
    for i in range(len(t) - 1):
        Vs[i] = yy[0]
        k1 = f(yy, Is); k2 = f(yy + dt / 2 * k1, Is); k3 = f(yy + dt / 2 * k2, Is); k4 = f(yy + dt * k3, Is)
        yy = yy + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    Vs[-1] = yy[0]
    rate = []
    for j in range(len(Is)):
        up = np.where((Vs[:-1, j] < 0) & (Vs[1:, j] >= 0))[0]
        tu = t[up]; tu = tu[tu > 60]
        rate.append(1000 / np.mean(np.diff(tu)) if len(tu) > 2 else 0.0)
    ax.plot(Is, rate, "o-", ms=2.5, color=charts.line(tok), lw=1.3, label=lab)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "$I_\\mathrm{ext}$ / $\\mu$A cm$^{-2}$", "firing rate / Hz")
charts.title(ax, "A  Connor-Stevens model: f-I curve")

ax = axs[0, 1]
t = np.arange(0, 300, dt)
f = cs_model(gA0, gL0, EL0)
y = cs_rest(gA0, gL0, EL0)[0]
for step, tok in [(8.8, "neuron"), (12.0, "dna")]:
    I = np.where(t >= 20, step, 0.0)
    V = rk4(f, y, I, dt)[:, 0]
    ax.plot(t - 20, V, color=charts.line(tok), lw=1.2, label=f"step to {step:g} $\\mu$A cm$^{{-2}}$")
ax.set_xlim(-10, 280); ax.set_ylim(-75, 85); ax.set_yticks([-60, -40, -20, 0, 20, 40])
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", ncol=2)
charts.style_axes(ax, "time after step / ms", "$V$ / mV")
charts.title(ax, "B  Long latency and slow ramps")

# ---- HH with M and h currents (arrays shape (4+1, runs))
p = neuro.HH
def hh_ext(gM=0.0, gh=0.0):
    def f(y, I):
        V, m, h, n, pm, r = y
        am, bm, ah, bh, an, bn = neuro.hh_rates(V)
        pinf = 1 / (1 + np.exp(-(V + 35) / 10)); rinf = 1 / (1 + np.exp((V + 75) / 5.5))
        iion = (p["gNa"] * m**3 * h * (V - p["ENa"]) + p["gK"] * n**4 * (V - p["EK"]) + p["gL"] * (V - p["EL"])
                + gM * pm * (V - p["EK"]) + gh * r * (V + 30))
        return np.array([I - iion, am * (1 - m) - bm * m, ah * (1 - h) - bh * h, an * (1 - n) - bn * n,
                         (pinf - pm) / 100.0, (rinf - r) / 150.0])
    return f

def hh_start(gM, gh):
    f = hh_ext(gM, gh)
    m0, h0, n0 = [float(x) for x in neuro.hh_steady(-65.0)]
    y = np.array([-65.0, m0, h0, n0, 0.0, 0.1])
    return rk4(f, y, np.zeros(int(400 / 0.05)), 0.05)[-1]

dt2 = 0.05
ax = axs[1, 0]
t = np.arange(0, 600, dt2)
I = np.where(t >= 50, 15.0, 0.0)
for gM, tok, lab in [(0.0, "negative", "no $I_\\mathrm{M}$"), (1.5, "neuron", "$I_\\mathrm{M}$, $g_\\mathrm{M} = 1.5$")]:
    f = hh_ext(gM, 0.0)
    V = rk4(f, hh_start(gM, 0.0), I, dt2)[:, 0]
    up = np.where((V[:-1] < 0) & (V[1:] >= 0))[0]
    tu = t[up]
    tu = tu[tu > 50]
    isi = np.diff(tu)
    ax.plot(tu[1:] - 50, 1000 / isi, "o-", ms=3, lw=1.2, color=charts.line(tok), label=lab)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, "time after step / ms", "instantaneous rate / Hz")
charts.title(ax, "C  Spike-frequency adaptation")

ax = axs[1, 1]
# passive membrane (no spikes) with or without I_h; leak reversal chosen so that both rest at -65 mV
t = np.arange(0, 900, dt2)
I = np.where((t >= 50) & (t < 450), -1.0, 0.0)
gLp = 0.1
for gh, tok, lab in [(0.0, "negative", "no $I_\\mathrm{h}$"), (0.1, "neuron", "with $I_\\mathrm{h}$")]:
    rinf = lambda V: 1 / (1 + np.exp((V + 75) / 5.5))
    ELp = -65.0 + gh * rinf(-65.0) * (-65.0 + 30.0) / gLp
    def fp(y, Ii, gh=gh, ELp=ELp):
        V, r = y
        return np.array([Ii - gLp * (V - ELp) - gh * r * (V + 30.0), (rinf(V) - r) / 150.0])
    yv = rk4(fp, np.array([-65.0, rinf(-65.0)]), I, dt2)[:, 0]
    ax.plot(t, yv, color=charts.line(tok), lw=1.3, label=lab)
ax.axhline(-65, color=P.muted(), lw=0.6, ls=":")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "D  Sag and rebound from $I_\\mathrm{h}$ (passive membrane)")
