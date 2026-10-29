# Scaling of a morphogen gradient by expansion-repression (Formula 16.6.1), in dimensionless units. A morphogen M
# (standing for BMP activity) enters at the ventral end (x = 0) with a constant flux and is degraded; an expander E,
# stable and freely diffusing, reduces the degradation of M; E is made only where M is below a threshold. In a large
# (L = 1) and a half-sized (L = 0.5) field, E accumulates until M at the far end has fallen to near the threshold, so
# the gradient adjusts to the size of the field. A: with the expander, profiles against relative position x / L
# nearly coincide. B: with the expander level held fixed, the same morphogen gives an absolute profile that does not
# scale: the small field is flooded.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P


def lapmat(N, dx):
    A = np.zeros((N, N))
    for i in range(N):
        A[i, i] = -2
        if i > 0:
            A[i, i - 1] = 1
        if i < N - 1:
            A[i, i + 1] = 1
    A[0, 1] = 2
    A[-1, -2] = 2
    return A / dx ** 2


def run(L, expander=True, N=81, T=20000.0, dt=2.0):
    x = np.linspace(0, L, N)
    dx = x[1] - x[0]
    Lp = lapmat(N, dx)
    I = np.eye(N)
    DM, k, DE, kE, eta, Tm, KE, j0 = 0.01, 1.0, 0.2, 1e-5, 0.01, 0.05, 1.0, 0.1
    AM = np.linalg.inv(I - dt * DM * Lp)
    AE = np.linalg.inv(I - dt * DE * Lp)
    M = np.zeros(N)
    E = np.zeros(N) if expander else np.full(N, 5.0)
    src = np.zeros(N)
    src[0] = 2 * j0 / dx
    for _ in range(int(T / dt)):
        M = AM @ (M + dt * (-k * M / (1 + E / KE) + src))
        if expander:
            E = AE @ (E + dt * (-kE * E + eta / (1 + (M / Tm) ** 4)))
    return x, M


fig, ax = bio.canvas(20.0, 7.8)
for k, (expander, letter, title) in enumerate([(True, "A", "with expander"), (False, "B", "expander fixed")]):
    pa = C.axes_at(ax, (1.6 + k * 10.0, 1.4, 7.4, 5.0))
    for L, t, lab in [(1.0, 0.0, "full embryo (L = 1)"), (0.5, 0.5, "half embryo (L = 0.5)")]:
        x, M = run(L, expander)
        pa.plot(x / L, M, color=P.mix(C.line("drug"), P.surface(), t), lw=2.0, label=lab)
    pa.set_xlim(0, 1)
    pa.set_ylim(0, None)
    C.style_axes(pa, "relative position x / L (ventral → dorsal)", "BMP activity")
    pa.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink(), loc="upper right")
    bio.panel(ax, letter, (0.2 + k * 10.0, 7.7))
    bio.label(ax, (1.6 + k * 10.0, 7.0), title, size="small", bold=True, ha="left")
