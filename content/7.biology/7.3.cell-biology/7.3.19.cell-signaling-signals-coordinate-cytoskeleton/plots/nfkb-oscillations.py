"""Negative feedback through IkB-alpha makes nuclear NF-kB pulse.

Three-variable model of Krishna, Jensen and Sneppen (2006): nuclear NF-kB N_n, IkB-alpha mRNA I_m and
cytoplasmic IkB-alpha I (micromolar; total NF-kB N_tot = 1). NF-kB enters the nucleus when free of IkB,
dN_n/dt = k_Nin (N_tot - N_n) K_I/(K_I + I) - k_Iin I N_n/(K_N + N_n); it induces its inhibitor,
dI_m/dt = k_t N_n^2 - gamma_m I_m; and IKK (activated by TNF) causes the degradation of IkB bound to
cytoplasmic NF-kB, dI/dt = k_tl I_m - alpha IKK (N_tot - N_n) I/(K_I + I). Published parameters (per minute):
k_Nin = 5.4, k_Iin = 0.018, k_t = 1.03, k_tl = 0.24, gamma_m = 0.017, alpha = 1.05; K_I = 0.035 and
K_N = 0.029 uM. The cell starts at rest (IKK = 0.02) and TNF raises IKK to 0.7.
A: with continuous TNF, NF-kB enters the nucleus within minutes, is pulled out by newly made IkB-alpha
and returns in pulses spaced by one to two hours. B: a 15-min pulse of TNF gives a single wave.
C: if IkB-alpha synthesis is fixed at its resting rate (no feedback, as in IkB-alpha-deficient cells,
where other IkB isoforms remain), nuclear NF-kB rises and stays high.
"""

import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import charts

P = bio.P
FS = bio.core.FONT["tiny"]
kNin, kIin, kt, ktl, KI, KN, gm, al, Nt = 5.4, 0.018, 1.03, 0.24, 0.035, 0.029, 0.017, 1.05, 1.0


def rhs(t, y, ikk, feedback, basal):
    Nn, Im, I = y
    prod = kt * Nn**2 if feedback else basal
    return [kNin * (Nt - Nn) * KI / (KI + I) - kIin * I * Nn / (KN + Nn), prod - gm * Im,
            ktl * Im - al * ikk(t) * (Nt - Nn) * I / (KI + I)]


rest = solve_ivp(rhs, (0, 30000), [0.01, 0.01, 1.0], args=(lambda t: 0.02, True, 0.0), method="LSODA",
                 rtol=1e-9, atol=1e-12).y[:, -1]
basal = kt * rest[0] ** 2
T = 480.0
t = np.linspace(0, T, 4801)


def run(ikk, feedback=True):
    s = solve_ivp(rhs, (0, T), rest, args=(ikk, feedback, basal), method="LSODA", rtol=1e-8, atol=1e-11, t_eval=t)
    return s.y


cases = [
    ("A", "Continuous TNF", lambda tt: 0.7, True),
    ("B", "15-min pulse of TNF", lambda tt: 0.7 if tt < 15 else 0.02, True),
    ("C", "No IκBα feedback, continuous TNF", lambda tt: 0.7, False),
]
IMAX = run(cases[0][2])[2].max()
fig, ax = bio.canvas(20.0, 6.8)
for k, (letter, ttl, ikk, fb) in enumerate(cases):
    x0 = 1.4 + k * 6.6
    bio.panel(ax, letter, (x0 - 1.3, 6.7))
    a = charts.axes_at(ax, (x0, 1.2, 4.9, 4.7))
    Nn, Im, I = run(ikk, fb)
    a.plot(t / 60, Nn, color=charts.line("highlight"), lw=1.9, label="nuclear NF-κB")
    a.plot(t / 60, I / IMAX * 0.9, color=charts.line("negative"), lw=1.2,
           ls=(0, (4, 2)), label="IκBα (same scale in A–C)")
    a.set_xlim(0, 8)
    a.set_ylim(0, 1.05)
    if k == 0:
        a.legend(frameon=False, fontsize=FS, labelcolor=P.ink(), loc="upper right")
    charts.style_axes(a, "time after TNF / h", "fraction of NF-κB in nucleus" if k == 0 else None)
    charts.title(a, ttl)
