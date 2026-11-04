# Patterns of infection and the target-cell model.
# A: the classical time courses of virus production in a host (schematic, after the standard figure).
# B: the target-cell model dT/dt = lambda - dT - beta V T, dI/dt = beta V T - delta I, dV/dt = pI - cV
#    simulated for an acute infection, with the sub-threshold case for comparison.
# C: the decay of plasma virus when replication is blocked completely at t = 0, the perturbation that
#    measures the turnover of infected cells and virions.
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(18.0, 7.6)

# --- A  patterns ----------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.4))
bio.label(ax, (3.0, 7.25), "Patterns of infection", size="title", bold=True)

t = np.linspace(0, 10, 600)


def bump(centre, width, height=1.0):
    return height * np.exp(-((t - centre) ** 2) / (2 * width ** 2))


PATTERNS = [
    ("Acute", bump(1.2, 0.45), [(0.7, 2.0)], "rhinovirus, rotavirus,\ninfluenza virus"),
    ("Latent", bump(1.0, 0.35) + 0.55 * bump(4.5, 0.25) + 0.5 * bump(7.5, 0.25),
     [(0.6, 1.6), (4.1, 4.9), (7.1, 7.9)], "herpes simplex virus,\nvaricella-zoster virus"),
    ("Persistent", np.clip(bump(1.0, 0.4) + 0.35, 0, 1.2), [(0.6, 1.6)],
     "hepatitis B and C viruses,\nLCMV"),
    ("Slow", bump(0.9, 0.35) + 0.08 + 0.9 / (1 + np.exp(-(t - 8.0) * 1.6)),
     [(7.6, 10.0)], "HIV-1 untreated,\nmeasles virus in SSPE"),
]
for k, (name, y, sympt, examples) in enumerate(PATTERNS):
    y0 = 6.0 - k * 1.45
    pl = quant.Plot(ax, (1.1, y0 - 0.45, 3.1, 1.0), xlim=(0, 10), ylim=(0, 1.35),
                    xticks=[], yticks=[], frame="l" if k < 3 else "bl",
                    xlabel="time" if k == 3 else None)
    for a, b in sympt:
        pl.span(a, b, "negative", strength=0.4)
    pl.line(t, y, "virus", lw=1.8)
    bio.label(ax, (0.95, y0 + 0.25), name, size="small", bold=True, ha="right")
    bio.label(ax, (4.35, y0 + 0.05), examples, size="tiny", color=P.muted(), ha="left")
bio.label(ax, (3.0, 0.45), "curve: virus production; shading: symptoms", size="tiny", color=P.muted())

# --- B  the target-cell model ---------------------------------------------------------------------
bio.panel(ax, "B", (6.9, 7.4))
bio.label(ax, (10.2, 7.25), "The target-cell model", size="title", bold=True)

LAM, DT, DELTA, PV, CV = 1e4, 0.01, 1.0, 1e3, 23.0   # per day; T0 = LAM/DT = 1e6 cells


def tcl(t_, y, beta):
    T, I, V = y
    return [LAM - DT * T - beta * V * T, beta * V * T - DELTA * I, PV * I - CV * V]


def r0_of(beta):
    return beta * PV * (LAM / DT) / (DELTA * CV)


tt = np.linspace(0, 20, 1000)
runs = {}
for beta, tok, name in ((2.4e-7, "virus", "$R_0 = %.0f$" % r0_of(2.4e-7)),
                        (1.0e-8, "muted", "$R_0 = %.1f$" % r0_of(1.0e-8))):
    s = solve_ivp(tcl, (0, 20), [LAM / DT, 0.0, 1e-2], args=(beta,), t_eval=tt, method="LSODA",
                  rtol=1e-9, atol=1e-6)
    runs[name] = (s, tok)

pl2 = quant.Plot(ax, (8.1, 1.7, 4.1, 4.8), xlim=(0, 20), ylim=(-1, 8),
                 xlabel="days after infection", ylabel="$\\log_{10}$ (cells or virions ml$^{-1}$)",
                 xticks=[0, 5, 10, 15, 20], yticks=[0, 2, 4, 6, 8])
(s, tok), name = list(runs.values())[0], list(runs.keys())[0]
pl2.line(s.t, np.log10(np.maximum(s.y[0], 1e-6)), "bacterium", text="target cells $T$", at=0.62, dy=0.30)
pl2.line(s.t, np.log10(np.maximum(s.y[1], 1e-6)), "enzyme", text="infected cells $I$", at=0.52, dy=-0.38)
pl2.line(s.t, np.log10(np.maximum(s.y[2], 1e-6)), "virus", text="free virus $V$", at=0.30, dy=0.32)
s2, tok2 = runs[list(runs.keys())[1]]
pl2.line(s2.t, np.log10(np.maximum(s2.y[2], 1e-1)), "muted", dashed=True,
         text="below threshold (" + list(runs.keys())[1] + ")", at=0.36, dy=0.45)
pl2.hline(np.log10(LAM / DT / r0_of(2.4e-7)), token="negative", dashed=True, text="$T_0/R_0$")
bio.label(ax, (10.2, 0.45), "the virus peaks as $T$ falls through $T_0/R_0$;\n"
                            "below $R_0 = 1$ there is no takeoff", size="tiny", color=P.muted())

# --- C  perturbation ---------------------------------------------------------------------------------
bio.panel(ax, "C", (13.2, 7.4))
bio.label(ax, (16.2, 7.25), "Turnover under therapy", size="title", bold=True)

td = np.linspace(0, 14, 600)
V0 = 1e5
# complete block from t = 0: free virions decay at c, and the cells that were already infected decay at delta
V = V0 * (CV * np.exp(-DELTA * td) - DELTA * np.exp(-CV * td)) / (CV - DELTA)
pl3 = quant.Plot(ax, (14.6, 1.7, 3.0, 4.8), xlim=(0, 14), ylim=(0, 6.0),
                 xlabel="days of therapy", ylabel="$\\log_{10}$ (plasma virus ml$^{-1}$)",
                 xticks=[0, 7, 14], yticks=[0, 2, 4, 6])
pl3.line(td, np.log10(np.maximum(V, 1e-2)), "virus", lw=1.9)
pl3.span(0.0, 0.4, "highlight")
pl3.text(3.2, 5.6, "shoulder: virion clearance $c$", size="tiny")
pl3.text(7.2, 3.6, "slope $= -\\delta/\\ln 10$:\nloss of productively\ninfected cells", size="tiny")
bio.label(ax, (16.2, 0.45), "fitted to patient data: an infected cell lives $\\approx 1$ day,\n"
                            "a virion a few hours; $\\sim 10^{10}$ virions are made per day",
          size="tiny", color=P.muted())
