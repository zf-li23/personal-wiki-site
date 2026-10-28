"""The full mass-action model of E + S <=> ES -> E + P against the steady-state approximation.

With conservation [E] = [E]0 - [ES] and [P] = [S]0 - [S] - [ES], the system reduces to two ODEs:
d[S]/dt = -k1([E]0 - [ES])[S] + k-1[ES], d[ES]/dt = k1([E]0 - [ES])[S] - (k-1 + k2)[ES].
Rate constants k1 = k-1 = k2 = 1 (so K_M = 2); concentrations in units of K_M, time in 1/k2.
A: [E]0 = 0.02 K_M, [S]0 = 2 K_M: [ES] rises within t_c = 1/(k1([S]0 + K_M)) to the value predicted
by the steady-state formula and then follows it (the formula evaluated on the simulated [S]) while
the substrate is consumed on the much longer time scale t_S = ([S]0 + K_M)/(k2 [E]0).
B: phase plane: trajectories from several [S]0 first move almost vertically (fast binding) onto the
steady-state curve [ES]/[E]0 = [S]/(K_M + [S]), the slow manifold, then slide along it to the origin.
C: product formation for [S]0 = K_M and three enzyme concentrations, time scaled by t_S: the
integrated Michaelis-Menten equation (dashed; in these units it is one curve for all three) is accurate while eps = [E]0/([S]0 + K_M) << 1 (Segel's
criterion) and fails when the enzyme is as concentrated as the substrate."""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import lambertw
import wikibio as bio
from wikibio import charts

P = bio.P
k1 = km1 = k2 = 1.0
KM = (km1 + k2) / k1
tiny = bio.core.FONT["tiny"]


def full(E0, S0, t):
    def f(_, y):
        S, C = y
        b = k1 * (E0 - C) * S
        return [-b + km1 * C, b - (km1 + k2) * C]

    sol = solve_ivp(f, (0, t[-1]), [S0, 0.0], t_eval=t, method="LSODA", rtol=1e-10, atol=1e-13)
    return sol.y


def mm_substrate(E0, S0, t):
    vmax = k2 * E0
    return KM * np.real(lambertw(S0 / KM * np.exp((S0 - vmax * t) / KM)))


fig, ax = bio.canvas(24.0, 8.4)

bio.panel(ax, "A", (0.1, 8.3))
a = charts.axes_at(ax, (1.5, 1.0, 6.3, 6.4))
E0, S0 = 0.02 * KM, 2 * KM
t = np.logspace(-3, np.log10(800), 600)
S, C = full(E0, S0, t)
tc = 1 / (k1 * (S0 + KM))
tS = (S0 + KM) / (k2 * E0)
a.semilogx(t, C / E0, color=charts.line("enzyme"), lw=2.0, label="[ES] / [E]$_0$, full model")
a.semilogx(t, S / (KM + S), color=charts.line("negative"), lw=1.4, ls="--", label="steady state $[S]/(K_\\mathrm{M}+[S])$")
a.semilogx(t, S / S0, color=charts.line("channel"), lw=1.4, label="[S] / [S]$_0$")
for tt, lab in ((tc, "$t_\\mathrm{c}$"), (tS, "$t_S$")):
    a.axvline(tt, color=P.muted(), lw=0.7, ls=":")
    a.text(tt * 1.15, 1.02, lab, fontsize=tiny, color=P.ink())
a.set_xlim(1e-3, 800)
a.set_ylim(0, 1.1)
a.legend(frameon=False, fontsize=tiny, labelcolor=P.ink(), loc="lower left")
charts.style_axes(a, "$k_2 t$", "fraction")
charts.title(a, "Fast transient, slow consumption")

bio.panel(ax, "B", (8.9, 8.3))
b = charts.axes_at(ax, (10.3, 1.0, 5.8, 6.4))
s = np.linspace(0, 8, 300)
b.plot(s, s / (1 + s), color=P.ink(), lw=1.1, ls="--", label="slow manifold", zorder=5)
E0 = 0.05 * KM
tt = np.logspace(-3, 3.5, 2000)
for S0x, tok in ((1, "channel"), (3, "protein"), (8, "enzyme")):
    S, C = full(E0, S0x * KM, tt)
    b.plot(S / KM, C / E0, color=charts.line(tok), lw=1.8)
    b.plot([S0x], [0], "o", ms=5, mfc=P.fill(tok), mec=charts.line(tok))
b.annotate("fast binding", (8, 0.45), (5.0, 0.25), fontsize=tiny, color=P.ink(),
           arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.7))
b.annotate("slow slide", (2.2, 0.69), (2.8, 0.95), fontsize=tiny, color=P.ink(),
           arrowprops=dict(arrowstyle="-|>", color=P.muted(), lw=0.7))
b.set_xlim(0, 8.4)
b.set_ylim(0, 1.05)
b.legend(frameon=False, fontsize=tiny, labelcolor=P.ink(), loc="lower right")
charts.style_axes(b, "[S] / $K_\\mathrm{M}$", "[ES] / [E]$_0$")
charts.title(b, "Phase plane")

bio.panel(ax, "C", (17.2, 8.3))
c = charts.axes_at(ax, (18.6, 1.0, 5.3, 6.4))
S0 = KM
for eps, tok in ((0.01, "channel"), (0.1, "protein"), (1.0, "negative")):
    E0 = eps * (S0 + KM)
    tS = (S0 + KM) / (k2 * E0)
    tau = np.linspace(0, 3, 400)
    S, C = full(E0, S0, tau * tS)
    Pf = S0 - S - C
    Pq = S0 - mm_substrate(E0, S0, tau * tS)
    c.plot(tau, Pf / S0, color=charts.line(tok), lw=2.0, label=f"$\\varepsilon$ = {eps:g}")
c.plot(tau, Pq / S0, color=P.ink(), lw=1.1, ls="--", label="Michaelis–Menten", zorder=5)
c.text(1.55, 0.1, "one dashed curve\nfor every $\\varepsilon$", fontsize=tiny, color=P.ink())
c.set_xlim(0, 3)
c.set_ylim(0, 1)
c.legend(frameon=False, fontsize=tiny, labelcolor=P.ink(), loc="upper left")
charts.style_axes(c, "$t / t_S$", "[P] / [S]$_0$")
charts.title(c, "When the approximation fails")
