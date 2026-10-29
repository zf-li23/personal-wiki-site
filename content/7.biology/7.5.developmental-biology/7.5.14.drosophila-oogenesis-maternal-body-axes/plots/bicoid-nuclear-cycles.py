# Formation of the Bicoid gradient by synthesis, diffusion and degradation (Formula 14.3.1), solved numerically on
# 0 <= x <= L = 500 um with no-flux ends. Synthesis from bicoid mRNA in the anterior 10 % of the egg starts at egg
# deposition (t = 0) and stops at cellularization (about 150 min); D = 4 um^2/s, lifetime 1/k = 50 min, so the
# decay length is lambda = sqrt(D/k) = 110 um. A: profiles at successive times (the steady state dashed). B: the time
# at which the concentration reaches 90 % of its steady value grows with distance from the source: the anterior is at
# steady state well before cycle 14, the posterior is not.
import numpy as np
import wikibio as bio
from wikibio import charts as C

P = bio.P
L, N = 500.0, 201
x = np.linspace(0, L, N)
dx = x[1] - x[0]
D, k = 4.0, 1 / (50 * 60.0)
s = np.where(x < 50, 1.0, 0.0)
dt = 0.2 * dx ** 2 / D
T = 150 * 60.0
nsteps = int(T / dt)
c = np.zeros(N)
times = [15, 30, 60, 90, 150]
snap = {}
hist_t, hist = [], []
for n in range(nsteps + 1):
    t = n * dt
    if any(abs(t / 60 - tt) < dt / 120 for tt in times):
        snap[min(times, key=lambda tt: abs(tt - t / 60))] = c.copy()
    if n % 50 == 0:
        hist_t.append(t / 60)
        hist.append(c.copy())
    lap = np.empty(N)
    lap[1:-1] = c[2:] - 2 * c[1:-1] + c[:-2]
    lap[0] = 2 * (c[1] - c[0])
    lap[-1] = 2 * (c[-2] - c[-1])
    c = c + dt * (D * lap / dx ** 2 - k * c + s * k)
# steady state by solving the linear system
A = np.zeros((N, N))
for i in range(N):
    A[i, i] = -2 * D / dx ** 2 - k
    if i > 0:
        A[i, i - 1] = D / dx ** 2
    if i < N - 1:
        A[i, i + 1] = D / dx ** 2
A[0, 1] = 2 * D / dx ** 2
A[-1, -2] = 2 * D / dx ** 2
css = np.linalg.solve(A, -s * k)
hist = np.array(hist)
hist_t = np.array(hist_t)

fig, ax = bio.canvas(20.0, 8.0)
pa = C.axes_at(ax, (1.6, 1.4, 8.0, 5.6))
for i, tt in enumerate(times):
    shade = P.mix(C.line("receptor"), P.surface(), 0.65 - 0.15 * i)
    pa.plot(x, snap[tt] / css[0], color=shade, lw=1.6, label=f"{tt} min")
pa.plot(x, css / css[0], color=P.ink(), lw=1.2, ls=(0, (4, 3)), label="steady state")
pa.set_xlim(0, L)
pa.set_ylim(0, 1.05)
C.style_axes(pa, "x / µm (anterior → posterior)", "Bicoid / steady value at x = 0")
pa.legend(fontsize=bio.core.FONT["tiny"], frameon=False, labelcolor=P.ink())
bio.panel(ax, "A", (0.2, 7.9))

pb = C.axes_at(ax, (12.4, 1.4, 6.8, 5.6))
xs = np.arange(25, 401, 25)
t90 = []
for xv in xs:
    i = int(round(xv / dx))
    above = np.nonzero(hist[:, i] >= 0.9 * css[i])[0]
    t90.append(hist_t[above[0]] if len(above) else np.nan)
pb.plot(xs, t90, "o-", color=C.line("receptor"), ms=3.5, lw=1.4)
pb.axhline(150, color=P.muted(), lw=0.8, ls=(0, (2, 2)))
pb.text(30, 154, "cellularization (cycle 14)", fontsize=bio.core.FONT["tiny"], color=P.muted())
pb.set_xlim(0, 410)
pb.set_ylim(0, 200)
C.style_axes(pb, "x / µm", "time to 90 % of steady state / min")
bio.panel(ax, "B", (11.0, 7.9))
