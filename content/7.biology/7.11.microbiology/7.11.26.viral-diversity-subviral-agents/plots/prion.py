# Prions: the conversion reaction, its kinetics and the three origins of a TSE.
# B simulates nucleated polymerization with fragmentation:
#   dP/dt = k_n m^2 + k_- M        (new fibrils by primary nucleation and by breakage)
#   dM/dt = 2 k_+ m P              (growth at the two ends of every fibril)
#   m = m_tot - M                  (monomer depleted into fibrils)
# which gives the long lag, the autocatalytic rise, and the abolition of the lag by preformed seed -
# the same reaction used in vitro by the RT-QuIC and PMCA amplification assays.
import numpy as np
from scipy.integrate import solve_ivp

import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(17.4, 7.6)

# --- A  the conversion ---------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.35))
bio.label(ax, (3.6, 7.2), "Templated misfolding", size="title", bold=True)

bio.protein(ax, (1.5, 5.6), 1.1, 0.85, "protein", text="PrP$^{\\mathrm{C}}$", size="small")
bio.label(ax, (1.5, 4.85), "$\\alpha$-helical, soluble,\nGPI-anchored", size="tiny", color=P.muted())
bio.protein(ax, (5.6, 5.6), 1.0, 0.8, "negative", text="PrP$^{\\mathrm{Sc}}$", size="small")
bio.label(ax, (5.6, 4.85), "$\\beta$-sheet-rich,\ninsoluble", size="tiny", color=P.muted())
bio.arrow(ax, (2.2, 5.6), (4.9, 5.6), kind="process")
bio.arrow(ax, (5.6, 6.25), (2.6, 6.25), kind="catalysis", bend=0.10, color=P.edge("negative"))
bio.label(ax, (4.1, 6.75), "the misfolded form templates the conversion", size="tiny",
          color=P.edge("negative"))
bio.label(ax, (3.55, 5.85), "same sequence,\ndifferent conformation", size="tiny", color=P.muted())

for k in range(6):                                   # the fibril
    bio.protein(ax, (1.3 + 0.62 * k, 3.5), 0.58, 0.62, "negative", wobble=0.03)
bio.arrow(ax, (5.6, 5.1), (4.6, 3.9), kind="process", color=P.edge("negative"))
bio.label(ax, (3.6, 2.9), "amyloid fibril: protease-resistant core PrP 27–30, insoluble aggregates,\n"
                          "neuronal loss and spongiform vacuolation", size="tiny", color=P.muted())
bio.label(ax, (3.6, 2.0), "proteinase K digests PrP$^{\\mathrm{C}}$ completely but leaves the core:\n"
                          "the diagnostic signature of the pathogenic conformer", size="tiny",
          color=P.muted())

# --- B  kinetics ---------------------------------------------------------------------------------------
bio.panel(ax, "B", (7.2, 7.35))
bio.label(ax, (10.4, 7.2), "Nucleated polymerization", size="title", bold=True)

KN, KP, KM, MTOT = 3e-8, 60.0, 3e-5, 1.0


def poly(t, y):
    Pn, M = y
    m = max(MTOT - M, 0.0)
    return [KN * m ** 2 + KM * M, 2 * KP * m * Pn]


tt = np.linspace(0, 200, 1600)
un = solve_ivp(poly, (0, 200), [0.0, 0.0], t_eval=tt, method="LSODA", rtol=1e-9, atol=1e-14)
sd = solve_ivp(poly, (0, 200), [1e-5, 1e-4], t_eval=tt, method="LSODA", rtol=1e-9, atol=1e-14)

pl = quant.Plot(ax, (8.3, 1.75, 4.6, 4.4), xlim=(0, 200), ylim=(0, 1.05),
                xlabel="time / h", ylabel="fraction of PrP in fibrils",
                xticks=[0, 50, 100, 150, 200], yticks=[0, 0.5, 1])
pl.line(un.t, un.y[1] / MTOT, "negative", text="no seed", at=0.62, dy=-0.32)
pl.line(sd.t, sd.y[1] / MTOT, "virus", dashed=True, text="with preformed seed", at=0.30, dy=0.32)
lag = tt[np.argmax(un.y[1] / MTOT > 0.1)]
pl.span(0, lag, "highlight", text="lag", text_y=0.95)
bio.label(ax, (10.6, 0.55), "adding seed abolishes the lag — the basis of infection,\n"
                            "and of the RT-QuIC and PMCA assays", size="tiny", color=P.muted())

# --- C  three origins ----------------------------------------------------------------------------------
bio.panel(ax, "C", (13.2, 7.35))
bio.label(ax, (15.6, 7.2), "Three origins", size="title", bold=True)

for y, tok, title, sub in ((6.2, "neutral", "Sporadic", "rare spontaneous conversion;\n85–90 % of human cases"),
                           (4.6, "highlight", "Inherited", "a dominant $\\it{PRNP}$ mutation;\nover 40 are known"),
                           (3.0, "virus", "Acquired", "ingestion, or iatrogenic:\ngrafts, instruments, hormones")):
    bio.box(ax, (15.6, y), 3.3, 1.05, token=tok, radius=0.18)
    bio.label(ax, (15.6, y + 0.26), title, size="small", bold=True, color=P.on_fill())
    bio.label(ax, (15.6, y - 0.22), sub, size="tiny", color=P.on_fill())
    bio.arrow(ax, (15.6, y - 0.55), (15.6, y - 1.0), kind="process") if y > 3.0 else None
bio.arrow(ax, (15.6, 2.45), (15.6, 1.95), kind="process")
bio.box(ax, (15.6, 1.45), 3.3, 0.85, token="negative", radius=0.18)
bio.label(ax, (15.6, 1.45), "self-propagating PrP$^{\\mathrm{Sc}}$\nin the brain", size="tiny", color=P.on_fill())
bio.label(ax, (15.6, 0.7), "no inflammatory or antibody response;\nincubation of months to decades",
          size="tiny", color=P.muted())
