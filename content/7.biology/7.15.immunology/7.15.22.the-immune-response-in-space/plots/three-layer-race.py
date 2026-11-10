# A minimal three-layer model of one infection: pathogen P, innate effectors I, adaptive effectors E, memory M.
#   dP/dt = r P (1 - P) - k_I I P - k_E E P                  (logistic growth, killed by both arms)
#   dI/dt = s_I P / (P + h) - d_I I                          (innate cells activated within hours)
#   dE/dt = rho a(t) (E + M) (1 - E) - d_E (1 - a(t)) (E - E0)      (clonal expansion while antigen is sensed,
#   dM/dt = phi d_E (1 - a(t)) (E - E0) - d_M M                    contraction after; a fraction becomes memory)
# with a(t) = P(t - tau) / (P(t - tau) + h_A): adaptive cells see antigen only after the delay tau needed for
# antigen transport to the lymph node, priming and migration back to the tissue. Units are relative
# (P = 1 is the maximal pathogen load); all parameters are illustrative.
import numpy as np

import wikibio as bio
from wikibio import charts, quant

P = bio.P
PAR = dict(kI=1.5, sI=1.0, dI=1.0, h=1e-4, rho=3.0, kE=10.0, dE=0.5, hA=1e-4, phi=0.05, dM=0.002)


def sim(r=2.0, tau=4.0, E0=1e-5, T=30.0, dt=0.005):
    p = PAR
    n = int(T / dt)
    t = np.arange(n) * dt
    Pa, I, E, M = np.zeros(n), np.zeros(n), np.zeros(n), np.zeros(n)
    Pa[0], E[0] = 1e-6, E0
    lag = int(tau / dt)
    for i in range(n - 1):
        pd = Pa[i - lag] if i >= lag else 0.0
        a = pd / (pd + p["hA"])
        dP = r * Pa[i] * (1 - Pa[i]) - p["kI"] * I[i] * Pa[i] - p["kE"] * E[i] * Pa[i]
        Pa[i + 1] = Pa[i] + dt * dP
        if Pa[i + 1] < 1e-9:
            Pa[i + 1] = 1e-12  # cleared
        I[i + 1] = I[i] + dt * (p["sI"] * Pa[i] / (Pa[i] + p["h"]) - p["dI"] * I[i])
        E[i + 1] = E[i] + dt * (p["rho"] * a * (E[i] + M[i]) * (1 - E[i]) - p["dE"] * (1 - a) * max(E[i] - E0, 0.0))
        M[i + 1] = M[i] + dt * (p["phi"] * p["dE"] * (1 - a) * max(E[i] - E0, 0.0) - p["dM"] * M[i])
    return t, Pa, I, E, M


fig, ax = bio.canvas(27, 9.6)

# ---- A: one infection ---------------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 9.4))
t, Pa, I, E, M = sim()
pa = quant.Plot(ax, (1.9, 1.6, 6.6, 6.6), (0, 30), (1e-6, 2), ylog=True, xlabel="Days after infection",
                ylabel="Relative level", xticks=[0, 5, 10, 15, 20, 25, 30],
                yticks=[(1e-6, "10⁻⁶"), (1e-4, "10⁻⁴"), (1e-2, "10⁻²"), (1, "1")], grid=True)
pa.line(t, np.maximum(Pa, 1e-7), "virus", lw=1.9, text="pathogen", at=0.12, dy=0.25, va="bottom", ha="left")
pa.line(t, np.maximum(I, 1e-7), "enzyme", lw=1.4, text="innate", at=0.05, dx=0.1, dy=-0.5, va="top", ha="left")
pa.line(t, np.maximum(E, 1e-7), "dna", lw=1.9, text="adaptive effectors", at=0.5, dx=0.1, dy=0.2, va="bottom", ha="left")
pa.line(t, np.maximum(M, 1e-7), "positive", lw=1.4, dashed=True, text="memory", at=0.92, dy=0.2, va="bottom")
pa.span(0, 4, "highlight", text="delay τ = 4 d", text_y=pa.Y(1.3))

# ---- B: outcome map ------------------------------------------------------------------------------------------
bio.panel(ax, "B", (9.6, 9.4))
taus = np.linspace(1, 8, 22)
rs = np.linspace(0.5, 3.5, 22)
peak = np.zeros((rs.size, taus.size))
for i, r in enumerate(rs):
    for j, tau in enumerate(taus):
        peak[i, j] = np.log10(max(sim(r=r, tau=tau, T=25, dt=0.01)[1].max(), 1e-6))
hx = charts.axes_at(ax, (11.4, 1.6, 6.0, 6.6))
im = hx.imshow(peak, origin="lower", aspect="auto", extent=(1, 8, 0.5, 3.5), cmap="magma", vmin=-6, vmax=0)
cs = hx.contour(taus, rs, peak, levels=[-2, -1], colors="white", linewidths=0.8)
hx.clabel(cs, fmt={-2: "10⁻²", -1: "10⁻¹"}, fontsize=7)
charts.style_axes(hx, "Adaptive delay τ / d", "Pathogen growth rate r / d⁻¹")
charts.title(hx, "Peak pathogen load (log₁₀)")
cb = fig.colorbar(im, ax=hx, fraction=0.05, pad=0.03)
cb.ax.tick_params(labelsize=7, colors=P.muted())
cb.outline.set_edgecolor(P.muted())

# ---- C: re-infection with memory -------------------------------------------------------------------------------
bio.panel(ax, "C", (19.4, 9.4))
_, P1, _, _, M1 = sim(r=2.0, tau=4.0)
t2, P2, _, E2, _ = sim(r=2.0, tau=1.5, E0=M1[-1])
pc = quant.Plot(ax, (21.2, 1.6, 5.4, 6.6), (0, 20), (1e-6, 2), ylog=True, xlabel="Days after infection",
                ylabel="Pathogen load", xticks=[0, 5, 10, 15, 20],
                yticks=[(1e-6, "10⁻⁶"), (1e-4, "10⁻⁴"), (1e-2, "10⁻²"), (1, "1")], grid=True)
m = t < 20
pc.line(t[m], np.maximum(P1[m], 1e-7), "virus", lw=1.8, text="first infection", at=0.45, dy=0.2, va="bottom", ha="left")
pc.line(t2[m], np.maximum(P2[m], 1e-7), "positive", lw=1.8, text="second: memory, τ = 1.5 d", at=0.1, dx=0.1, dy=-0.6,
        va="top", ha="left")
