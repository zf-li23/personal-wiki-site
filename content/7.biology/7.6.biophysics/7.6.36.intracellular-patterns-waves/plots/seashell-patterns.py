"""Shell patterns as space-time records of a one-dimensional reaction-diffusion system along the
growing edge of the shell (Meinhardt's interpretation): each row is the pigment pattern laid down
at one time, and time runs downwards as the shell grows. Activator-inhibitor dynamics
(Gierer-Meinhardt), da/dt = rho a^2/h - mu a + rho0 + D_a a_xx, dh/dt = rho a^2 - nu h + D_h h_xx,
on a ring of 150 cells with random source densities rho = 1 +- 2 %. A: fast, far-reaching
inhibitor (D_h = 0.4, nu = 0.07, mu = 0.05, D_a = 0.005): stationary peaks draw lines along the
direction of growth. B: inhibitor slower than the activator (nu = 0.02 < mu = 0.05) with
little spread (D_h = 0.004): the edge oscillates almost synchronously and draws bands parallel to
the margin. C: an excitable margin (Barkley's model, an
activator u with a slow recovery variable v) in which resting regions fire spontaneously at random:
each firing launches two waves that travel along the margin and annihilate when they meet, drawing
oblique lines, chevrons and triangles. Darker means more activator (pigment)."""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import wikibio as bio
from wikibio import charts

P = bio.P
cmap = LinearSegmentedColormap.from_list("shell", [P.surface(), P.fill("lipid_head"), P.edge("lipid_head")])


def excitable(T=400.0, n=300, dx=0.5, dt=0.005, seed=3, rate=0.12):
    """Barkley's excitable medium, du/dt = u(1 - u)(u - (v + b)/a)/eps + D u_xx, dv/dt = u - v,
    with spontaneous local firing of resting regions at a small random rate."""
    rng = np.random.default_rng(seed)
    a, b, eps, D = 0.75, 0.06, 0.02, 0.3
    u = np.zeros(n)
    v = np.zeros(n)
    rows = []
    for i in range(int(T / dt)):
        lu = (np.roll(u, 1) + np.roll(u, -1) - 2 * u) / dx ** 2
        u = u + dt * (u * (1 - u) * (u - (v + b) / a) / eps + D * lu)
        v = v + dt * (u - v)
        if rng.random() < dt * rate:
            j = rng.integers(n)
            if v[j] < 0.05:
                u[max(0, j - 3):j + 3] = 1.0
        if i % 200 == 0:
            rows.append(u.copy())
    return np.array(rows)


def shell(Da, Dh, mu, nu, rho0, T, n=150, dt=0.1, every=10, seed=1):
    rng = np.random.default_rng(seed)
    rho = 1 + 0.02 * rng.standard_normal(n)
    a = 1 + 0.1 * rng.random(n)
    h = np.ones(n) * mu / nu * 1.0
    rows = []
    for i in range(int(T / dt)):
        la = np.roll(a, 1) + np.roll(a, -1) - 2 * a
        lh = np.roll(h, 1) + np.roll(h, -1) - 2 * h
        a2 = rho * a * a
        a = a + dt * (a2 / h - mu * a + rho0 + Da * la)
        h = h + dt * (a2 - nu * h + Dh * lh)
        if i % every == 0:
            rows.append(a.copy())
    return np.array(rows)


cases = [
    (r"A  stationary peaks", dict(Da=0.005, Dh=0.4, mu=0.05, nu=0.07, rho0=0.001, T=1500)),
    (r"B  oscillation", dict(Da=0.005, Dh=0.004, mu=0.05, nu=0.02, rho0=0.001, T=1500)),
    (r"C  traveling waves", None),
]
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.6))
fig.subplots_adjust(wspace=0.12, left=0.05, right=0.98, bottom=0.12, top=0.9)
for ax, (ttl, kw) in zip(axs, cases):
    r = shell(**kw) if kw else excitable()
    r = r[r.shape[0] // 5:]
    hi = np.percentile(r, 99)
    ax.imshow(np.clip(r / hi, 0, 1), aspect="auto", cmap=cmap, interpolation="bilinear")
    ax.set_xticks([])
    ax.set_yticks([])
    charts.style_axes(ax, "position along the shell margin", "growth (time)" if ax is axs[0] else None, box=True)
    charts.title(ax, ttl)
