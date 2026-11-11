"""Phase response curves of two oscillator types and the phase locking they predict.

Type 1 oscillator: theta neuron  d theta/dt = (1 - cos theta) + (1 + cos theta) I, I = 0.05
(time in units of 1 ms), the normal form of a saddle-node on invariant circle; spike when theta
crosses pi; a kick dv is applied to its quadratic integrate-and-fire voltage v = tan(theta / 2).
Type 2 oscillator: Hodgkin-Huxley model (standard squid parameters, 6.3 C) driven by
I = 10 uA/cm^2, above its Hopf bifurcation; spike when V crosses 0 mV upward; kick of 1 mV.
A: PRCs measured by the direct method (advance of the next spike per kick, as a fraction of the
   period, normalized to the largest absolute value); phase 0 is the spike.
B: odd part of the interaction function for excitatory coupling through an exponential synapse
   (decay 5 % of the period): G(psi) = H(-psi) - H(psi), H(chi) = int_0^1 Z(phi) s(phi + chi) dphi,
   so that the phase difference psi obeys d psi / dt = eps G(psi). Zeros with negative slope are
   stable (filled dots), with positive slope unstable (open circles).
C: direct simulation of two identical oscillators of each type coupled by weak excitatory
   synapses of that kind, started 0.3 cycles apart: absolute spike-time difference in units of
   the period at each cycle of neuron 1.
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio

P = bio.P
C1, C2 = P.edge("dna"), P.edge("negative")
TAU_S = 0.05  # synaptic decay as a fraction of the period


# ---- models ---------------------------------------------------------------
I1 = 0.05
T1 = np.pi / np.sqrt(I1)


def theta_rhs(t, y, extra=0.0):
    th = y[0]
    return np.array([(1 - np.cos(th)) + (1 + np.cos(th)) * (I1 + extra)])


def theta_kick(y, dv):
    return np.array([2 * np.arctan(np.tan(y[0] / 2) + dv)])


def am(V):
    return 0.1 * (V + 40) / (1 - np.exp(-(V + 40) / 10))


def bm(V):
    return 4 * np.exp(-(V + 65) / 18)


def ah(V):
    return 0.07 * np.exp(-(V + 65) / 20)


def bh(V):
    return 1 / (1 + np.exp(-(V + 35) / 10))


def an(V):
    return 0.01 * (V + 55) / (1 - np.exp(-(V + 55) / 10))


def bn(V):
    return 0.125 * np.exp(-(V + 65) / 80)


I2 = 10.0


def hh_rhs(t, y, extra=0.0):
    V, m, h, n = y
    I_ion = 120 * m ** 3 * h * (V - 50) + 36 * n ** 4 * (V + 77) + 0.3 * (V + 54.4)
    return np.array([-I_ion + I2 + extra,
                     am(V) * (1 - m) - bm(V) * m,
                     ah(V) * (1 - h) - bh(V) * h,
                     an(V) * (1 - n) - bn(V) * n])


def hh_kick(y, dv):
    z = y.copy()
    z[0] += dv
    return z


def ev_theta(t, y):
    return y[0] - np.pi


def ev_hh(t, y):
    return y[0]


for e in (ev_theta, ev_hh):
    e.terminal, e.direction = True, 1


def next_spike(rhs, ev, t0, y0, tmax):
    s = solve_ivp(rhs, [t0, tmax], y0, events=ev, rtol=1e-8, atol=1e-10, max_step=0.2)
    return s.t_events[0][0], s.y_events[0][0]


# state at a spike of the HH limit cycle
s = solve_ivp(hh_rhs, [0, 200], [-65, 0.05, 0.6, 0.32], rtol=1e-8, atol=1e-10, max_step=0.2)
t_a, y_a = next_spike(hh_rhs, ev_hh, 0, s.y[:, -1], 100)
t_b, y_b = next_spike(hh_rhs, ev_hh, t_a + 1.0, solve_ivp(hh_rhs, [t_a, t_a + 1.0], y_a, rtol=1e-8, max_step=0.2).y[:, -1], t_a + 100)
T2 = t_b - t_a
y0_hh = y_b


def prc(rhs, ev, y0, T, kick, dv, n=50):
    phis = np.linspace(0.0, 1.0, n, endpoint=False) + 0.5 / n
    out = []
    for ph in phis:
        t0 = ph * T
        y = solve_ivp(rhs, [0, t0], y0, rtol=1e-8, atol=1e-10, max_step=0.2).y[:, -1]
        y = kick(y, dv)
        tsp, _ = next_spike(rhs, ev, t0, y, t0 + 2 * T)
        out.append((T - tsp) / T)
    return phis, np.array(out)


ph1, z1 = prc(theta_rhs, ev_theta, np.array([-np.pi]), T1, theta_kick, 0.05)
ph2, z2 = prc(hh_rhs, ev_hh, y0_hh, T2, hh_kick, 1.0)
z1n, z2n = z1 / np.abs(z1).max(), z2 / np.abs(z2).max()

# ---- interaction functions ------------------------------------------------
grid = np.linspace(0, 1, 400, endpoint=False)
syn = np.exp(-grid / TAU_S)


def G_of(ph, z):
    Z = np.interp(grid, ph, z, period=1.0)
    n = len(grid)
    H = np.array([np.mean(Z * np.roll(syn, -k)) for k in range(n)])  # H(chi) with chi = k / n
    Hm = np.roll(H[::-1], 1)  # H(-chi)
    return Hm - H


G1, G2 = G_of(ph1, z1n), G_of(ph2, z2n)
psi = np.where(grid >= 0.5, grid - 1.0, grid)
order = np.argsort(psi)
ps, G1s, G2s = psi[order], G1[order], G2[order]


def zeros(G):
    res = []
    for k in range(len(ps) - 1):
        if G[k] == 0 or np.sign(G[k]) != np.sign(G[k + 1]):
            x = ps[k] if G[k] == 0 else ps[k] - G[k] * (ps[k + 1] - ps[k]) / (G[k + 1] - G[k])
            res.append((x, G[k + 1] < G[k - 1]))
    return res


# ---- direct simulation of coupled pairs -----------------------------------
def coupled(rhs, ev_index_thr, y_init, T, g, dt, ncyc=40, wrap=None):
    y = [y_init[0].copy(), y_init[1].copy()]
    sv = np.zeros(2)
    spikes = [[], []]
    t = 0.0
    idx, thr = ev_index_thr
    while t < ncyc * T:
        new = []
        for i in range(2):
            extra = g * sv[1 - i] / (TAU_S * T)
            k1 = rhs(t, y[i], extra)
            k2 = rhs(t, y[i] + dt * k1, extra)
            new.append(y[i] + 0.5 * dt * (k1 + k2))
        for i in range(2):
            if y[i][idx] < thr <= new[i][idx]:
                spikes[i].append(t)
                sv[i] += 1.0
                if wrap is not None:
                    new[i][idx] -= wrap
        y = new
        sv -= dt * sv / (TAU_S * T)
        t += dt
    return spikes


def lag(spikes, T):
    s1, s2 = np.array(spikes[0]), np.array(spikes[1])
    out = []
    for t in s1[1:]:
        j = np.argmin(np.abs(s2 - t))
        out.append(abs(((s2[j] - t) / T + 0.5) % 1.0 - 0.5))
    return np.array(out)


def state_at(rhs, y0, t):
    return solve_ivp(rhs, [0, t], y0, rtol=1e-8, atol=1e-10, max_step=0.2).y[:, -1] if t > 0 else y0.copy()


th0 = np.array([-np.pi])
sp1 = coupled(theta_rhs, (0, np.pi), [state_at(theta_rhs, th0, 0.0), state_at(theta_rhs, th0, 0.3 * T1)],
              T1, g=0.03, dt=0.01, wrap=2 * np.pi)
sp2 = coupled(hh_rhs, (0, 0.0), [state_at(hh_rhs, y0_hh, 0.0), state_at(hh_rhs, y0_hh, 0.3 * T2)],
              T2, g=2.0, dt=0.01)
lag1, lag2 = lag(sp1, T1), lag(sp2, T2)

# ---- figure --------------------------------------------------------------
fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
ax = axs[0]
ax.plot(ph1, z1n, color=C1, lw=2.0, label="type 1 (theta neuron)")
ax.plot(ph2, z2n, color=C2, lw=2.0, label="type 2 (Hodgkin-Huxley)")
ax.axhline(0, color=P.muted(), lw=0.8)
ax.set_xlim(0, 1)
ax.set_xlabel("Phase of the kick $\\phi$ / cycle")
ax.set_ylabel("Phase advance (normalized)")
ax.set_title("A  Phase response curves", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower left")

ax = axs[1]
for G, col, lab, ms in ((G1s, C1, "type 1", 11), (G2s, C2, "type 2", 6)):
    sc = np.abs(G).max()
    ax.plot(ps, G / sc, color=col, lw=2.0, label=lab)
    for x, stable in zeros(G):
        for xx in ((x, -x) if abs(abs(x) - 0.5) < 1e-6 else (x,)):
            ax.plot(xx, 0, "o", ms=ms, color=col, mfc=col if stable else "none", mew=1.8, zorder=5 if ms < 8 else 4, clip_on=False)
ax.axhline(0, color=P.muted(), lw=0.8)
ax.set_xlim(-0.5, 0.5)
ax.set_xlabel("Phase difference $\\psi$ / cycle")
ax.set_ylabel("$G(\\psi)$ (normalized)")
ax.set_title("B  Locking predicted by the phase model", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")

ax = axs[2]
ax.plot(np.arange(len(lag1)), lag1, "o-", ms=3, color=C1, lw=1.2, label="theta neurons")
ax.plot(np.arange(len(lag2)), lag2, "o-", ms=3, color=C2, lw=1.2, label="Hodgkin-Huxley")
ax.set_ylim(-0.02, 0.55)
ax.set_xlabel("Cycle of neuron 1")
ax.set_ylabel("|Spike-time difference| / period")
ax.set_title("C  Two coupled oscillators", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="center right")
for a_ in axs:
    a_.grid(True, alpha=0.3)
fig.tight_layout()
