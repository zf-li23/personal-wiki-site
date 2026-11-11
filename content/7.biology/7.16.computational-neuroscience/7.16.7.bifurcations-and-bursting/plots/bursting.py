"""Fast-slow analysis of "fold/homoclinic" (square-wave) bursting in the I_Na,p + I_K + I_K(M) model
(Izhikevich 2007, Fig. 9.4): C dV/dt = I - g_L(V - E_L) - g_Na m_inf(V)(V - E_Na) - g_K n (V - E_K)
- g_slow n_s (V - E_K), dn/dt = (n_inf(V) - n)/tau, dn_s/dt = (n_s,inf(V) - n_s)/tau_slow, with
C = 1, E_L = -80, g_L = 8, g_Na = 20, g_K = 9, g_slow = 5 mS/cm2, E_Na = 60, E_K = -90 mV, tau = 0.152 ms,
tau_slow = 20 ms; m_inf: V_1/2 = -20, k = 15; n_inf: V_1/2 = -25, k = 5; n_s,inf: V_1/2 = -20, k = 5 mV;
I = 5 uA/cm2. A: membrane potential and the slow gate n_s: n_s grows during a burst and decays during
the silent phase. B: the fast subsystem (V, n) with n_s frozen as a parameter: equilibria (solid stable,
dashed unstable) form a Z-shaped curve whose lower knee is a fold (saddle-node) bifurcation; the band
of dots marks the maximum and minimum of V on the spiking limit cycle, which ends in a saddle homoclinic
orbit bifurcation when it touches the middle branch. The burst trajectory (thin line) is superimposed:
it leaves rest at the fold and stops spiking at the homoclinic bifurcation."""

import numpy as np
import matplotlib.pyplot as plt
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
EL, gL, gNa, gK, gs, I0, tau, taus = -80.0, 8.0, 20.0, 9.0, 5.0, 5.0, 0.152, 20.0
minf = lambda V: 1 / (1 + np.exp((-20 - V) / 15))
ninf = lambda V: 1 / (1 + np.exp((-25 - V) / 5))
nsinf = lambda V: 1 / (1 + np.exp((-20 - V) / 5))


def fast(V, n, ns):
    dV = I0 - gL * (V - EL) - gNa * minf(V) * (V - 60) - gK * n * (V + 90) - gs * ns * (V + 90)
    return dV, (ninf(V) - n) / tau


def full(y):
    V, n, ns = y
    dV, dn = fast(V, n, ns)
    return np.array([dV, dn, (nsinf(V) - ns) / taus])


dt = 0.005
t = np.arange(0, 260, dt)
y = np.array([-65.0, ninf(-65.0), 0.0])
out = np.empty((len(t), 3))
for i in range(len(t)):
    out[i] = y
    k1 = full(y); k2 = full(y + dt / 2 * k1); k3 = full(y + dt / 2 * k2); k4 = full(y + dt * k3)
    y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
keep = t > 60
tb, Vb, nsb = t[keep] - 60, out[keep, 0], out[keep, 2]

fig = plt.figure(figsize=(10.4, 3.6))
gs_ = fig.add_gridspec(2, 2, width_ratios=[1.15, 1.0], height_ratios=[2.2, 1.0], wspace=0.25, hspace=0.25,
                       left=0.07, right=0.99, bottom=0.15, top=0.9)
ax = fig.add_subplot(gs_[0, 0])
ax.plot(tb, Vb, color=charts.line("blood"), lw=0.9)
charts.style_axes(ax, None, "$V$ / mV")
ax.tick_params(labelbottom=False)
charts.title(ax, "A  Square-wave bursting")
ax2 = fig.add_subplot(gs_[1, 0], sharex=ax)
ax2.plot(tb, nsb, color=charts.line("k"), lw=1.2)
charts.style_axes(ax2, "t / ms", "$n_\\mathrm{s}$")

# B: bifurcation diagram of the fast subsystem against n_s
ax = fig.add_subplot(gs_[:, 1])
Vs = np.linspace(-80, 20, 4001)
ns_eq = (I0 - gL * (Vs - EL) - gNa * minf(Vs) * (Vs - 60) - gK * ninf(Vs) * (Vs + 90)) / (gs * (Vs + 90))
stab = np.empty(len(Vs), bool)
h = 1e-5
for k, (V, ns) in enumerate(zip(Vs, ns_eq)):
    n = ninf(V)
    a = [(np.array(fast(V + h, n, ns)) - np.array(fast(V - h, n, ns))) / (2 * h),
         (np.array(fast(V, n + h, ns)) - np.array(fast(V, n - h, ns))) / (2 * h)]
    stab[k] = np.all(np.linalg.eigvals(np.array(a).T).real < 0)
rng_ = (ns_eq > -0.01) & (ns_eq < 0.16)
ax.plot(ns_eq, np.where(rng_ & stab, Vs, np.nan), "-", color=charts.line("neuron"), lw=1.6, label="stable equilibrium")
ax.plot(ns_eq, np.where(rng_ & ~stab, Vs, np.nan), "--", color=charts.line("negative"), lw=1.4, label="unstable equilibrium")
# limit cycles of the fast subsystem for frozen n_s (vectorized), started on the spiking branch
nsv = np.linspace(0.0, 0.15, 76)
V = np.full(len(nsv), -20.0); n = np.full(len(nsv), 0.5)
mn = np.full(len(nsv), 1e9); mx = np.full(len(nsv), -1e9)
dt2 = 0.005; steps = int(40 / dt2)
for i in range(steps):
    def F(V, n):
        return fast(V, n, nsv)
    a1 = F(V, n); a2 = F(V + dt2 / 2 * a1[0], n + dt2 / 2 * a1[1]); a3 = F(V + dt2 / 2 * a2[0], n + dt2 / 2 * a2[1])
    a4 = F(V + dt2 * a3[0], n + dt2 * a3[1])
    V = V + dt2 / 6 * (a1[0] + 2 * a2[0] + 2 * a3[0] + a4[0]); n = n + dt2 / 6 * (a1[1] + 2 * a2[1] + 2 * a3[1] + a4[1])
    if i > 0.75 * steps:
        mn = np.minimum(mn, V); mx = np.maximum(mx, V)
osc = mx - mn > 5
ax.plot(nsv[osc], mx[osc], "o", ms=2.6, color=charts.line("highlight"), label="spiking: max and min of $V$")
ax.plot(nsv[osc], mn[osc], "o", ms=2.6, color=charts.line("highlight"))
ax.plot(nsb, Vb, color=P.muted(), lw=0.4, alpha=0.8, label="burst trajectory")
ax.set_xlim(-0.005, 0.12); ax.set_ylim(-80, 5)
ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper right", bbox_to_anchor=(1.0, 0.86))
charts.style_axes(ax, "slow K$^+$ gate $n_\\mathrm{s}$ (frozen)", "$V$ / mV")
charts.title(ax, "B  Fast subsystem: fold and homoclinic")
