"""Phase plane of the persistent sodium plus potassium model (Izhikevich 2007, Eqs. 4.1-4.2, Fig. 4.1):
C dV/dt = I - g_L(V - E_L) - g_Na m_inf(V)(V - E_Na) - g_K n (V - E_K), dn/dt = (n_inf(V) - n)/tau,
C = 1, tau = 1 ms, g_L = 8, g_Na = 20, g_K = 10 mS/cm2, E_L = -80, E_Na = 60, E_K = -90 mV; m_inf has
V_1/2 = -20, k = 15 mV, n_inf has V_1/2 = -25, k = 5 mV (high-threshold K+ current). A: V-nullcline
(dV/dt = 0), n-nullcline (dn/dt = 0), vector field, the three equilibria (stable node = rest, saddle,
unstable focus) at I = 0, trajectories started by brief voltage jumps to -60, -58 and -52 mV (n unchanged),
and the stable manifold of the saddle (dashed), computed by integrating backward from the saddle along its
stable eigenvector: the manifold is the threshold. B: voltage time courses of the trajectories. C: the same
model with a low-threshold K+ current (n_1/2 = -45 mV, E_L = -78 mV) at I = 0: the rest state is a stable
focus, so perturbations produce damped oscillations (resonance), and C shows a response to a brief pulse."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT


def model(EL=-80.0, nh=-25.0):
    gL, gNa, gK, ENa, EK = 8.0, 20.0, 10.0, 60.0, -90.0
    minf = lambda V: 1 / (1 + np.exp((-20 - V) / 15))
    ninf = lambda V: 1 / (1 + np.exp((nh - V) / 5))

    def f(t, y, I=0.0):
        V, n = y
        return [I - gL * (V - EL) - gNa * minf(V) * (V - ENa) - gK * n * (V - EK), ninf(V) - n]

    def vnull(V, I=0.0):
        return (I - gL * (V - EL) - gNa * minf(V) * (V - ENa)) / (gK * (V - EK))
    return f, vnull, ninf


def equilibria(f, ninf):
    Vs = np.linspace(-90, 40, 2601)
    g = lambda V: f(0, [V, ninf(V)])[0]
    gv = np.array([g(v) for v in Vs])
    out = []
    for i in range(len(Vs) - 1):
        if gv[i] * gv[i + 1] < 0:
            V = brentq(g, Vs[i], Vs[i + 1]); n = float(ninf(V))
            J = np.zeros((2, 2)); h = 1e-5
            for j in range(2):
                e = np.zeros(2); e[j] = h
                J[:, j] = (np.array(f(0, np.array([V, n]) + e)) - np.array(f(0, np.array([V, n]) - e))) / (2 * h)
            out.append((V, n, J))
    return out


fig = plt.figure(figsize=(10.4, 3.8))
gs = fig.add_gridspec(1, 3, width_ratios=[1.25, 1, 1], wspace=0.34, left=0.06, right=0.99, bottom=0.16, top=0.88)

f, vnull, ninf = model()
ax = fig.add_subplot(gs[0, 0])
V = np.linspace(-90, 30, 400)
ax.plot(V, vnull(V), color=charts.line("neuron"), lw=1.5, label="$V$-nullcline")
ax.plot(V, ninf(V), color=charts.line("highlight"), lw=1.5, label="$n$-nullcline")
Vg, ng = np.meshgrid(np.linspace(-85, 25, 20), np.linspace(0, 1, 16))
dv, dn = np.array(f(0, [Vg, ng]))
nrm = np.hypot(dv / 100.0, dn / 1.0)
ax.quiver(Vg, ng, dv / 100 / nrm, dn / nrm, color=P.muted(), width=0.0025, scale=45, alpha=0.7, zorder=1)
eqs = equilibria(f, ninf)
for V0, n0, J in eqs:
    ev = np.linalg.eigvals(J)
    stable = np.all(ev.real < 0)
    ax.plot([V0], [n0], "o", ms=6, mfc=(charts.line("neuron") if stable else "white"), mec=P.ink(), zorder=6)
# stable manifold of the saddle
for V0, n0, J in eqs:
    ev, vec = np.linalg.eig(J)
    if np.isreal(ev).all() and ev.min() < 0 < ev.max():
        v = vec[:, np.argmin(ev)].real
        for sgn in (1, -1):
            y0 = np.array([V0, n0]) + sgn * 1e-4 * v / np.hypot(*v)
            s = solve_ivp(lambda t, y: [-a for a in f(t, y)], [0, 12], y0, max_step=0.02, rtol=1e-8)
            ok = (s.y[0] > -95) & (s.y[0] < 45) & (s.y[1] > -0.1) & (s.y[1] < 1.1)
            ax.plot(s.y[0][ok], s.y[1][ok], "--", color=P.ink(), lw=1.1)
n_rest = [e for e in eqs if np.all(np.linalg.eigvals(e[2]).real < 0)][0]
trajs = []
for V0, tok in [(-60, "dna"), (-58, "neutral"), (-52, "blood")]:
    s = solve_ivp(f, [0, 12], [V0, n_rest[1]], max_step=0.02, rtol=1e-8)
    trajs.append((V0, s, tok))
    ax.plot(s.y[0], s.y[1], color=charts.line(tok), lw=1.4)
ax.set_xlim(-90, 30); ax.set_ylim(-0.02, 0.8)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
charts.style_axes(ax, "$V$ / mV", "$n$")
charts.title(ax, "A  Phase plane, $I = 0$")

ax = fig.add_subplot(gs[0, 1])
for V0, s, tok in trajs:
    ax.plot(s.t, s.y[0], color=charts.line(tok), lw=1.4, label=f"$V(0) = {V0}$")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="center right")
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "B  Voltage time courses")

f2, vnull2, ninf2 = model(EL=-78.0, nh=-45.0)
eq2 = equilibria(f2, ninf2)
ax = fig.add_subplot(gs[0, 2])
n0 = eq2[0][1]; V0 = eq2[0][0]
for dV, tok in [(8, "dna"), (-8, "neutral")]:
    s = solve_ivp(f2, [0, 20], [V0 + dV, n0], max_step=0.02, rtol=1e-8)
    ax.plot(s.t, s.y[0], color=charts.line(tok), lw=1.4, label=f"jump {dV:+d} mV")
ax.axhline(V0, color=P.muted(), lw=0.7, ls=":")
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right")
charts.style_axes(ax, "t / ms", "$V$ / mV")
charts.title(ax, "C  Low-threshold K$^+$: damped oscillation")
