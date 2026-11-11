"""Classes of excitability and the integrator-resonator distinction. A: f-I curves of the Morris-Lecar
model (C = 20 uF/cm2, g_K = 8, g_L = 2 mS/cm2, E_Ca = 120, E_K = -84, E_L = -60 mV, V_1 = -1.2, V_2 = 18 mV;
w kinetics phi/cosh((V - V_3)/(2 V_4))). Class 1 parameters: phi = 0.067, V_3 = 12, V_4 = 17.4 mV, g_Ca = 4
(SNIC): the rate starts from zero. Class 2: phi = 0.04, V_3 = 2, V_4 = 30 mV, g_Ca = 4.4 (Hopf): the rate
jumps to about 7 Hz. B: the voltage near the onset of firing. C: pairs of brief voltage jumps in the
Na,p+K model (Izhikevich Eqs. 4.1-4.2): the first jump is 3 mV, the plot gives the size of the second jump
needed to fire, divided by the size needed alone, against the interval. Integrator (high-threshold K+,
I = 4): close pulses add, the needed jump falls monotonically to zero as the interval shrinks. Resonator
(low-threshold K+, E_L = -78 mV, I = 10, close to the Hopf bifurcation): the needed jump oscillates
with the interval and is smallest when the second pulse comes one period (3.2 ms) after the first."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def ml(phi, V3, V4, gCa):
    V1, V2, VCa, VK, VL, gK, gL, C = -1.2, 18.0, 120.0, -84.0, -60.0, 8.0, 2.0, 20.0
    minf = lambda V: 0.5 * (1 + np.tanh((V - V1) / V2))
    winf = lambda V: 0.5 * (1 + np.tanh((V - V3) / V4))

    def f(y, I):
        V, w = y
        return np.array([(I - gL * (V - VL) - gK * w * (V - VK) - gCa * minf(V) * (V - VCa)) / C,
                         phi * (winf(V) - w) / np.cosh((V - V3) / (2 * V4))])
    return f, winf


def trace(model, I, T, dt, V0=-60.0):
    f, winf = model
    I = np.atleast_1d(np.asarray(I, float))
    y = np.array([np.full(len(I), V0), winf(np.full(len(I), V0))])
    n = int(T / dt); out = np.empty((n, len(I)))
    for i in range(n):
        out[i] = y[0]
        k1 = f(y, I); k2 = f(y + dt / 2 * k1, I); k3 = f(y + dt / 2 * k2, I); k4 = f(y + dt * k3, I)
        y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return out


def rates(V, dt, T):
    t = np.arange(V.shape[0]) * dt
    r = []
    for j in range(V.shape[1]):
        up = np.where((V[:-1, j] < 0) & (V[1:, j] >= 0))[0]
        tu = t[up]; tu = tu[tu > T / 3]
        r.append(1000 / np.mean(np.diff(tu)) if len(tu) > 2 else 0.0)
    return np.array(r)


M1 = ml(0.067, 12, 17.4, 4.0)
M2 = ml(0.04, 2, 30, 4.4)
fig, axs = plt.subplots(1, 3, figsize=(10.4, 3.3))
fig.subplots_adjust(wspace=0.34, left=0.06, right=0.99, bottom=0.17, top=0.88)

ax = axs[0]
dt, T = 0.1, 2000.0
I1 = np.concatenate([np.arange(36, 40, 1.0), np.arange(40, 44, 0.25), np.arange(44, 90, 4.0)])
I2 = np.concatenate([np.arange(70, 86, 5.0), np.arange(86, 94, 0.5), np.arange(94, 160, 6.0)])
ax.plot(I1, rates(trace(M1, I1, T, dt), dt, T), "o-", ms=2.5, color=charts.line("neuron"), lw=1.3, label="class 1 (SNIC)")
ax.plot(I2, rates(trace(M2, I2, T, dt), dt, T), "s-", ms=2.5, color=charts.line("negative"), lw=1.3, label="class 2 (Hopf)")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "$I_\\mathrm{ext}$ / $\\mu$A cm$^{-2}$", "firing rate / Hz")
charts.title(ax, "A  Morris-Lecar f-I curves")

ax = axs[1]
t = np.arange(0, 400, 0.1)
v1 = trace(M1, [41.0], 400, 0.1)[:, 0]
v2 = trace(M2, [95.0], 400, 0.1)[:, 0]
ax.plot(t, v1, color=charts.line("neuron"), lw=1.1, label="class 1, $I = 41$")
ax.plot(t, v2 - 0, color=charts.line("negative"), lw=1.1, label="class 2, $I = 95$")
ax.set_ylim(-68, 72)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", ncol=2)
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "B  Near the onset of firing")


def napk(EL=-80.0, nh=-25.0, I=0.0):
    gL, gNa, gK, ENa, EK = 8.0, 20.0, 10.0, 60.0, -90.0
    minf = lambda V: 1 / (1 + np.exp((-20 - V) / 15)); ninf = lambda V: 1 / (1 + np.exp((nh - V) / 5))

    def f(t, y):
        return [I - gL * (y[0] - EL) - gNa * minf(y[0]) * (y[0] - ENa) - gK * y[1] * (y[0] - EK), ninf(y[0]) - y[1]]
    g = lambda V: f(0, [V, ninf(V)])[0]
    Vs = np.linspace(-90, -20, 1400)
    gv = np.array([g(v) for v in Vs])
    i = np.where(gv[:-1] * gv[1:] < 0)[0][0]
    Vr = brentq(g, Vs[i], Vs[i + 1])
    return f, np.array([Vr, float(ninf(Vr))])


def spikes(f, y0, T=40):
    s = solve_ivp(f, [0, T], y0, max_step=0.2, rtol=1e-8)
    return s.y[0].max() > 0


def minjump(f, y):
    lo, hi = 0.0, 80.0
    for _ in range(26):
        mid = (lo + hi) / 2
        if spikes(f, y + np.array([mid, 0.0])): hi = mid
        else: lo = mid
    return hi


ax = axs[2]
Ds = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.2, 3.5, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20, 30])
for (EL, nh, I, tok, lab) in [(-80.0, -25.0, 4.0, "neuron", "integrator ($I = 4$)"), (-78.0, -45.0, 10.0, "negative", "resonator ($I = 10$)")]:
    f, yr = napk(EL, nh, I)
    alone = minjump(f, yr)
    r = []
    for D in Ds:
        s = solve_ivp(f, [0, D], yr + np.array([3.0, 0.0]), max_step=0.05, rtol=1e-8)
        r.append(minjump(f, s.y[:, -1]) / alone)
    ax.plot(Ds, r, "o-", ms=3, color=charts.line(tok), lw=1.3, label=lab)
ax.axhline(1.0, color=P.muted(), lw=0.7, ls=":")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="lower right")
charts.style_axes(ax, "interval between jumps / ms", "needed 2nd jump / single jump")
charts.title(ax, "C  Integrator and resonator")
