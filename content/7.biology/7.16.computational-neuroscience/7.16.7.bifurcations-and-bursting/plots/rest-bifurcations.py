"""Four bifurcations of the resting state, all in the persistent sodium plus potassium model (Izhikevich
2007, Eqs. 4.1-4.2): C dV/dt = I - g_L(V - E_L) - g_Na m_inf(V)(V - E_Na) - g_K n (V - E_K), dn/dt =
(n_inf(V) - n)/tau with C = 1, E_Na = 60, E_K = -90 mV; m_inf: V_1/2 = -20, k = 15 mV. Parameter sets:
A (Fig. 4.1a): E_L = -80, g_L = 8, g_Na = 20, g_K = 10, n_inf: V_1/2 = -25, k = 5, tau = 1: saddle-node on an
invariant circle. B (Fig. 4.1b): E_L = -78, n_inf: V_1/2 = -45: supercritical Andronov-Hopf. C: as B but
g_L = 1, g_Na = g_K = 4, m_inf: V_1/2 = -30, k = 7: subcritical Andronov-Hopf with a coexisting limit
cycle. D: as A with tau = 0.16 ms: the resting state disappears in a saddle-node bifurcation off the
limit cycle, which already exists (it is born in a saddle homoclinic orbit bifurcation at I = 3.1), so rest
and spiking coexist for 3.1 < I < 4.5. Each panel: equilibrium voltage (solid = stable, dashed =
unstable, from the Jacobian) and the minimum and maximum of V on the attractor reached by integrating for
400 ms from just above the resting equilibrium and from the state (V, n) = (-20, 0.6) (dots); where an
equilibrium is stable and dots exist at the same I the system is bistable."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
import wikibio as bio
from wikibio import charts

P = bio.P
FT = bio.core.FONT
SETS = {
    "A": dict(EL=-80, gL=8, gNa=20, gK=10, mh=-20, mk=15, nh=-25, nk=5, tau=1.0),
    "B": dict(EL=-78, gL=8, gNa=20, gK=10, mh=-20, mk=15, nh=-45, nk=5, tau=1.0),
    "C": dict(EL=-78, gL=1, gNa=4, gK=4, mh=-30, mk=7, nh=-45, nk=5, tau=1.0),
    "D": dict(EL=-80, gL=8, gNa=20, gK=10, mh=-20, mk=15, nh=-25, nk=5, tau=0.16),
}
RANGES = {"A": (0, 8), "B": (5, 30), "C": (30, 70), "D": (2, 6)}
TITLES = {"A": "A  Saddle-node on invariant circle", "B": "B  Supercritical Hopf",
          "C": "C  Subcritical Hopf", "D": "D  Saddle-node off the invariant circle"}


def parts(p):
    minf = lambda V: 1 / (1 + np.exp((p["mh"] - V) / p["mk"]))
    ninf = lambda V: 1 / (1 + np.exp((p["nh"] - V) / p["nk"]))

    def f(y, I):
        V, n = y
        return np.array([I - p["gL"] * (V - p["EL"]) - p["gNa"] * minf(V) * (V - 60.0) - p["gK"] * n * (V + 90.0),
                         (ninf(V) - n) / p["tau"]])
    return f, minf, ninf


def equilibria(p, I):
    f, minf, ninf = parts(p)
    g = lambda V: f([V, ninf(V)], I)[0]
    Vs = np.linspace(-90, 40, 1301); gv = np.array([g(v) for v in Vs])
    out = []
    for i in np.where(gv[:-1] * gv[1:] < 0)[0]:
        V = brentq(g, Vs[i], Vs[i + 1]); n = float(ninf(V)); h = 1e-5
        J = np.array([(f(np.array([V, n]) + e, I) - f(np.array([V, n]) - e, I)) / (2 * h)
                      for e in (np.array([h, 0.0]), np.array([0.0, h]))]).T
        out.append((V, np.all(np.linalg.eigvals(J).real < 0)))
    return out


def attractor(p, Is, y0, T=300.0, dt=0.02):
    """Min and max of V over the last 30% of a run, for all currents at once (vectorized RK4)."""
    f, _, _ = parts(p)
    y = np.array(y0, float)
    n = int(T / dt); mn = np.full(len(Is), 1e9); mx = np.full(len(Is), -1e9)
    for i in range(n):
        k1 = f(y, Is); k2 = f(y + dt / 2 * k1, Is); k3 = f(y + dt / 2 * k2, Is); k4 = f(y + dt * k3, Is)
        y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if i > 0.7 * n:
            mn = np.minimum(mn, y[0]); mx = np.maximum(mx, y[0])
    return mn, mx


def branches(p, a, b):
    """Equilibrium curve parametrized by V: I = I_ss(V), split into stable and unstable pieces."""
    f, minf, ninf = parts(p)
    Vs = np.linspace(-90, 30, 2401)
    Iss = p["gL"] * (Vs - p["EL"]) + p["gNa"] * minf(Vs) * (Vs - 60.0) + p["gK"] * ninf(Vs) * (Vs + 90.0)
    stab = np.empty(len(Vs), bool)
    h = 1e-5
    for k, (V, I) in enumerate(zip(Vs, Iss)):
        n = float(ninf(V)); y = np.array([V, n])
        J = np.array([(f(y + e, I) - f(y - e, I)) / (2 * h) for e in (np.array([h, 0.0]), np.array([0.0, h]))]).T
        stab[k] = np.all(np.linalg.eigvals(J).real < 0)
    keep = (Iss >= a) & (Iss <= b)
    return Vs, Iss, stab, keep


fig, axs = plt.subplots(2, 2, figsize=(10.0, 6.2))
fig.subplots_adjust(wspace=0.28, hspace=0.5, left=0.07, right=0.99, bottom=0.09, top=0.93)
for ax, key in zip(axs.flat, "ABCD"):
    p = SETS[key]; a, b = RANGES[key]
    Vs, Iss, stab, keep = branches(p, a, b)
    for flag, ls, tok in [(True, "-", "neuron"), (False, "--", "negative")]:
        y = np.where(keep & (stab == flag), Vs, np.nan)
        ax.plot(Iss, y, ls, color=charts.line(tok), lw=1.6)
    Is = np.linspace(a, b, 90)
    _, _, ninf = parts(p)
    rest = np.empty(len(Is))
    for j, I in enumerate(Is):
        eq = equilibria(p, I)
        stv = [V for V, s_ in eq if s_]
        rest[j] = min(stv) if stv else eq[0][0]
    mn1, mx1 = attractor(p, Is, [rest + 0.5, ninf(rest)], T=400.0)
    mn2, mx2 = attractor(p, Is, [np.full(len(Is), -20.0), np.full(len(Is), 0.6)], T=400.0)
    thr = 1.0 if key == "B" else 5.0
    osc1 = mx1 - mn1 > thr; osc2 = mx2 - mn2 > thr
    for osc, mn, mx in [(osc2, mn2, mx2), (osc1, mn1, mx1)]:
        ax.plot(Is[osc], mx[osc], "o", ms=2.6, color=charts.line("highlight"))
        ax.plot(Is[osc], mn[osc], "o", ms=2.6, color=charts.line("highlight"))
    if key == "A":
        ax.plot([], [], "-", color=charts.line("neuron"), lw=1.6, label="stable equilibrium")
        ax.plot([], [], "--", color=charts.line("negative"), lw=1.6, label="unstable equilibrium")
        ax.plot([], [], "o", ms=3, color=charts.line("highlight"), label="spiking: max and min of $V$")
        ax.legend(frameon=False, fontsize=FT["tiny"], labelcolor=P.ink(), loc="upper left")
    charts.style_axes(ax, "$I$ / $\\mu$A cm$^{-2}$", "$V$ / mV")
    charts.title(ax, TITLES[key])
