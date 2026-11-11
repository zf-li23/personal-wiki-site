"""Oscillations in the Wilson-Cowan model and the Hopf bifurcation.

tau_E dE/dt = -E + f(w_EE E - w_EI I + h_E),  tau_I dI/dt = -I + f(w_IE E - w_II I),
f(x) = 1 / (1 + exp(-(x - 4))), w_EE = 10, w_EI = 10, w_IE = 8, w_II = 2, tau_E = 5 ms,
tau_I = 10 ms; E and I are fractions of active cells (0..1), h_E is the drive to the E cells.
A: phase plane at h_E = 3: E nullcline (blue), I nullcline (red), the unstable fixed point
   (open circle) and the limit cycle (purple) that the trajectory reaches from a point near it.
B: bifurcation diagram: the fixed-point value E* (solid where stable, dashed where unstable) and
   the minimum and maximum of E on the limit cycle (dots) against h_E. Two Hopf bifurcations
   enclose the oscillatory window.
C: frequency of the oscillation (Hz) against h_E (from the simulated period; the imaginary part
   of the Jacobian eigenvalue at the fixed point is the small-amplitude estimate, line).
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

import wikibio as bio

P = bio.P
wEE, wEI, wIE, wII = 10.0, 10.0, 8.0, 2.0
tE, tI = 5.0, 10.0


def f(x):
    return 1 / (1 + np.exp(-(x - 4.0)))


def df(x):
    e = np.exp(-(x - 4.0))
    return e / (1 + e) ** 2


def rhs(t, y, hE):
    E, I = y
    return [(-E + f(wEE * E - wEI * I + hE)) / tE, (-I + f(wIE * E - wII * I)) / tI]


def fixed_point(hE):
    # solve on the E nullcline: I(E) from E = f(.), then match the I equation
    def g(E):
        I = (wEE * E + hE - 4.0 - np.log(E / (1 - E))) / wEI
        return I - f(wIE * E - wII * I)
    Es = np.linspace(1e-4, 1 - 1e-4, 4000)
    gs = np.array([g(E) for E in Es])
    i = np.flatnonzero(np.sign(gs[:-1]) != np.sign(gs[1:]))
    E = brentq(g, Es[i[0]], Es[i[0] + 1])
    I = (wEE * E + hE - 4.0 - np.log(E / (1 - E))) / wEI
    return E, I


def eig(hE):
    E, I = fixed_point(hE)
    xE, xI = wEE * E - wEI * I + hE, wIE * E - wII * I
    J = np.array([[(-1 + wEE * df(xE)) / tE, -wEI * df(xE) / tE], [wIE * df(xI) / tI, (-1 - wII * df(xI)) / tI]])
    return np.linalg.eigvals(J)


hs = np.arange(0.0, 8.01, 0.1)
Estar, stab, fr_lin = [], [], []
for h in hs:
    E, I = fixed_point(h)
    ev = eig(h)
    Estar.append(E)
    stab.append(ev.real.max() < 0)
    fr_lin.append(abs(ev.imag.max()) / (2 * np.pi) * 1000.0 if abs(ev.imag.max()) > 0 else np.nan)
Estar, stab = np.array(Estar), np.array(stab)
fr_lin = np.array(fr_lin)

# simulated limit cycles
cyc = {}
for h in hs[(hs >= 0.9) & (hs <= 5.0)]:
    sol = solve_ivp(rhs, [0, 1500], [0.2, 0.1], args=(h,), t_eval=np.arange(1000, 1500, 0.05), rtol=1e-8, atol=1e-10)
    E = sol.y[0]
    if E.max() - E.min() > 0.02:
        peaks = np.flatnonzero((E[1:-1] > E[:-2]) & (E[1:-1] >= E[2:])) + 1
        per = np.mean(np.diff(sol.t[peaks])) if len(peaks) > 2 else np.nan
        cyc[round(h, 2)] = (E.min(), E.max(), 1000.0 / per if per == per else np.nan)

fig, axs = plt.subplots(1, 3, figsize=(13, 3.9))
ax = axs[0]
h0 = 3.0
Is = np.linspace(1e-4, 1 - 1e-4, 400)
En = np.linspace(1e-4, 1 - 1e-4, 400)
ax.plot(En, (wEE * En + h0 - 4.0 - np.log(En / (1 - En))) / wEI, color=P.edge("dna"), lw=2.0, label="E nullcline")
ax.plot((4.0 + np.log(Is / (1 - Is)) + wII * Is) / wIE, Is, color=P.edge("negative"), lw=2.0, label="I nullcline")
E0, I0 = fixed_point(h0)
sol = solve_ivp(rhs, [0, 600], [E0 + 0.02, I0], args=(h0,), t_eval=np.arange(0, 600, 0.1), rtol=1e-8)
ax.plot(sol.y[0][3000:], sol.y[1][3000:], color=P.edge("protein"), lw=2.0, label="limit cycle")
ax.plot(sol.y[0][:1200], sol.y[1][:1200], color=P.muted(), lw=0.8)
ax.plot(E0, I0, "o", ms=8, mfc="none", mec=P.ink(), mew=1.6, zorder=5)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xlabel("$E$")
ax.set_ylabel("$I$")
ax.set_title("A  Phase plane, $h_E$ = 3", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")

ax = axs[1]
ax.plot(hs, np.where(stab, Estar, np.nan), "-", color=P.ink(), lw=1.8, label="fixed point, stable")
unst = ~stab | np.r_[~stab[1:], False] | np.r_[False, ~stab[:-1]]
ax.plot(hs, np.where(unst, Estar, np.nan), "--", color=P.ink(), lw=1.8, label="fixed point, unstable")
hh = np.array(sorted(cyc))
ax.plot(hh, [cyc[h][0] for h in hh], "o", ms=3, color=P.edge("protein"), label="limit cycle (min, max)")
ax.plot(hh, [cyc[h][1] for h in hh], "o", ms=3, color=P.edge("protein"))
ax.set_xlabel("Drive to E cells $h_E$")
ax.set_ylabel("$E$")
ax.set_title("B  Bifurcation diagram", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8, loc="lower right")

ax = axs[2]
ax.plot(hh, [cyc[h][2] for h in hh], "o", ms=3, color=P.edge("protein"), label="simulated limit cycle")
ax.plot(hs[~stab], fr_lin[~stab], color=P.ink(), lw=1.4, label="linear estimate $\\mathrm{Im}\\,\\lambda/2\\pi$")
ax.set_xlabel("Drive to E cells $h_E$")
ax.set_ylabel("Frequency / Hz")
ax.set_title("C  Frequency", loc="left", fontsize=10)
ax.legend(frameon=False, fontsize=8)
for a in axs:
    a.grid(True, alpha=0.3)
fig.tight_layout()
