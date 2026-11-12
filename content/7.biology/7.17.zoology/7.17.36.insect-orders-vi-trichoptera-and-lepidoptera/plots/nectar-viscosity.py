# Sucking nectar through a proboscis: a Hagen-Poiseuille model. For a tube of radius r and length L under a
# suction pressure dP, the volume flow is Q = pi r^4 dP / (8 mu L); the rate of sugar intake is Q times the
# sugar mass per volume, c * rho, so at fixed r, L and dP it is proportional to c rho / mu. Viscosity mu and
# density rho of sucrose solutions at 20 C are handbook values (CRC Handbook of Chemistry and Physics,
# concentrative properties of aqueous sucrose); the curve is a model, not data on any species.
import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
w = np.array([0, 10, 20, 30, 40, 50, 60])                    # % sucrose by mass
mu = np.array([1.002, 1.333, 1.945, 3.187, 6.162, 15.43, 58.49])  # mPa s
rho = np.array([0.998, 1.038, 1.081, 1.127, 1.176, 1.230, 1.287])  # g/mL
x = np.linspace(0, 60, 400)
lmu = np.interp(x, w, np.log(mu))
rx = np.interp(x, w, rho)
rate = x * rx / np.exp(lmu)
rate /= rate.max()
fig, ax = bio.canvas(16, 9.5)
a = charts.axes_at(ax, (1.9, 1.4, 13.2, 7.4))
a.plot(x, rate, color=P.edge("positive"), lw=2.2, label="sugar intake rate (relative)")
a2 = a.twinx()
a2.semilogy(x, np.exp(lmu), color=P.edge("enzyme"), lw=1.6, ls="--", label="viscosity")
a2.semilogy(w, mu, "o", color=P.edge("enzyme"), ms=3.5)
a2.set_ylabel("Viscosity (mPa s, log scale)")
i = np.argmax(rate)
a.axvline(x[i], color=P.muted(), lw=0.8, ls=":")
a.text(x[i] + 1, 0.15, f"optimum about {x[i]:.0f}%", fontsize=7, color=P.ink())
a.set_xlim(0, 60)
a.set_ylim(0, 1.08)
a.set_xlabel("Nectar sugar concentration (% sucrose by mass)")
a.set_ylabel("Relative rate of sugar intake, c rho / mu")
h1, l1 = a.get_legend_handles_labels()
h2, l2 = a2.get_legend_handles_labels()
a.legend(h1 + h2, l1 + l2, fontsize=7, frameon=False, loc="upper right")
