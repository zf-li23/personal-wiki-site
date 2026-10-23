"""
Predator-mediated coexistence of two competitors (normalized model of Section 4.4.2).
Species 1 is the superior competitor (a < 1 < b); the predator prefers it (kappa = c2/c1 < 1).
Left: 3D trajectories for four predator mortalities d. Right: outcome map in the (d, kappa) plane
with the invasion boundaries derived in the answer.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from scipy.integrate import solve_ivp

a, b, rho, e1, e2 = 0.5, 1.5, 1.0, 1.0, 0.2


def rhs(t, z, d, kappa):
    u1, u2, v = z
    return [u1 * (1 - u1 - a * u2 - v),
            rho * u2 * (1 - u2 - b * u1 - kappa * v),
            v * (-d + e1 * u1 + e2 * u2)]


def simulate(d, kappa, T=1500.0, z0=(0.3, 0.3, 0.1), n=3000):
    sol = solve_ivp(rhs, [0, T], z0, args=(d, kappa), method='LSODA',
                    rtol=1e-7, atol=1e-10, dense_output=True)
    t = np.linspace(0, T, n)
    return t, sol.sol(t)


def outcome(d, kappa):
    """0: species 1 alone, 1: species 1 + predator, 2: all three, 3: species 2 + predator."""
    _, y = simulate(d, kappa, n=200)
    alive = y[:, -1] > 1e-3
    if alive.all():
        return 2
    if alive[0] and alive[2]:
        return 1
    if alive[1] and alive[2]:
        return 3
    return 0


fig = plt.figure(figsize=(13, 5.5))

ax = fig.add_subplot(1, 2, 1, projection='3d')
kappa = 0.3
cases = [(0.1, 'd = 0.1: species 1 excluded'), (0.35, 'd = 0.35: coexistence'),
         (0.8, 'd = 0.8: species 2 excluded'), (1.1, 'd = 1.1: predator extinct')]
for (d, label), color in zip(cases, ['C0', 'C2', 'C1', 'C3']):
    t, y = simulate(d, kappa, T=300.0)
    ax.plot(*y, color=color, lw=1.2, label=label)
    ax.scatter(*y[:, -1], color=color, s=30)
ax.scatter(0.3, 0.3, 0.1, color='k', s=20)
ax.set_xlabel('species 1 $u_1$')
ax.set_ylabel('species 2 $u_2$')
ax.set_zlabel('predator $v$')
ax.set_title(f'Trajectories from (0.3, 0.3, 0.1), kappa = {kappa}')
ax.view_init(elev=22, azim=-55)
ax.legend(loc='upper left', fontsize=8)

ax = fig.add_subplot(1, 2, 2)
ds = np.linspace(0.02, 1.2, 60)
ks = np.linspace(0.05, 0.95, 46)
grid = np.array([[outcome(d, k) for d in ds] for k in ks])
cmap = ListedColormap(['C3', 'C1', 'C2', 'C0'])
ax.pcolormesh(ds, ks, grid, cmap=cmap, vmin=-0.5, vmax=3.5, shading='nearest', alpha=0.55)
kk = np.linspace(0.05, 0.95, 200)
ax.plot(e1 * (1 - kk) / (b - kk), kk, 'k-', lw=1.5)
ax.plot(e2 * (1 - kk) / (1 - a * kk), kk, 'k--', lw=1.5)
ax.axvline(e1, color='k', ls=':', lw=1.5)
ax.text(0.04, 0.5, 'species 2\n+ predator', fontsize=9)
ax.text(0.27, 0.12, 'all three\ncoexist', fontsize=9)
ax.text(0.75, 0.3, 'species 1\n+ predator', fontsize=9)
ax.text(1.03, 0.5, 'species 1\nalone', fontsize=9)
ax.set_xlabel('predator mortality d')
ax.set_ylabel('kappa = c2 / c1')
ax.set_title('Long-term outcome (a = 0.5, b = 1.5, e1 = 1, e2 = 0.2)')

fig.tight_layout()

