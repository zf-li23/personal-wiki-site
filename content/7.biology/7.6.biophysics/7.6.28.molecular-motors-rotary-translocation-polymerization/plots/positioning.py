# Centering an aster by microtubule forces (two-dimensional toy model). An aster at distance X from the center of
# a circular cell of radius R sends 360 microtubules radially at equally spaced angles; each reaches the cortex
# at distance l(phi) = -X cos(phi) + sqrt(R^2 - X^2 sin^2(phi)).
# Pushing: a microtubule growing against the cortex pushes back with at most its Euler buckling force
# pi^2 kappa / l^2 (pinned ends; kappa = l_p kBT with l_p = 5 mm, R = 10 um), so short microtubules push harder.
# Pulling by cytoplasmic dynein distributed along each microtubule: force proportional to its length,
# f = 0.1 pN per um.  A: geometry. B: net force on the aster against its position: both mechanisms restore it
# to the center (negative slope), with a stiffness of order pN/um; pulling with a constant force per
# microtubule at the cortex gives no restoring force in this geometry (the angular distribution of
# microtubules does not change with X).
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
R, M = 10.0, 360
phi = (np.arange(M) + 0.5) * 2 * np.pi / M
kappa = 5000.0 * 4.1e-3  # pN um^2 (l_p = 5 mm)


def lengths(X):
    return -X * np.cos(phi) + np.sqrt(R**2 - X**2 * np.sin(phi) ** 2)


def push(X):
    l = lengths(X)
    return np.sum(-np.pi**2 * kappa / l**2 * np.cos(phi))  # reaction on the aster points away from the wall


def pull_length(X):
    l = lengths(X)
    return np.sum(0.1 * l * np.cos(phi))


fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.2), gridspec_kw={"width_ratios": [1, 1.4]})
ax = axs[0]
X0 = 4.0
th = np.linspace(0, 2 * np.pi, 200)
ax.plot(R * np.cos(th), R * np.sin(th), color=P.edge("membrane"), lw=2.0)
for p in phi[::12]:
    l = -X0 * np.cos(p) + np.sqrt(R**2 - X0**2 * np.sin(p) ** 2)
    ax.plot([X0, X0 + l * np.cos(p)], [0, l * np.sin(p)], color=charts.line("channel"), lw=0.9)
ax.plot(X0, 0, "o", color=charts.line("highlight"), ms=8)
ax.plot(0, 0, "+", color=P.muted(), ms=10)
ax.annotate("", xy=(1.0, -1.2), xytext=(X0 - 0.3, -1.2), arrowprops=dict(arrowstyle="-|>", color=charts.line("negative"), lw=1.6))
ax.text(2.4, -2.2, "net force", fontsize=8, color=P.ink(), ha="center")
ax.set_aspect("equal"); ax.axis("off")
charts.title(ax, "A   Aster off center in a cell")

ax = axs[1]
Xs = np.linspace(-7, 7, 141)
ax.plot(Xs, [push(x) for x in Xs], color=charts.line("channel"), lw=2.0, label="pushing (buckling-limited)")
ax.plot(Xs, [pull_length(x) for x in Xs], color=charts.line("protein"), lw=2.0, label="length-dependent pulling")
ax.plot(Xs, 0 * Xs, color=P.muted(), lw=1.0, ls="--", label="constant pull per microtubule")
ax.set_ylim(-300, 300)
ax.legend(fontsize=7.5, frameon=False, loc="upper right")
charts.style_axes(ax, "aster position $X$ / µm", "net force on aster / pN")
charts.title(ax, "B   Restoring forces center the aster")
fig.tight_layout()
