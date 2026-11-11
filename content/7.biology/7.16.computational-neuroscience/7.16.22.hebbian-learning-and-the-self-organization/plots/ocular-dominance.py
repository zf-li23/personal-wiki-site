"""Development of ocular dominance stripes by correlation-based competition (Miller, Keller and Stryker 1989; Dayan and Abbott 8.3).

One-dimensional cortex of 96 cells (periodic). Cortical cell x receives weights from left-eye and right-eye afferents at
positions x + a, |a| <= 8. Afferents of the same eye are correlated, Q(d) = exp(-d^2 / (2 * 2.5^2)); afferents of
the two eyes are uncorrelated. The total weight of each pair of afferents is held fixed, w^R + w^L = 1, so the only
variable is the difference D(x, a) = w^R - w^L in [-1, 1] (Dayan and Abbott 8.3). The correlation rule gives
  dD(x,a)/dt = sum_x' B(x - x') sum_a' Q(x + a - x' - a') D(x', a'),
with a cortical interaction B that is a difference of Gaussians (excitation sigma 2, inhibition sigma 7,
amplitude 0.25), and D is clipped to [-1, 1] (saturation). Initial D: Gaussian noise with SD 0.05.
A: ocular dominance index OD(x) = mean over a of D at four times. B: D(x, a) at the end (image).
C: power spectrum of OD(x); the peak is the stripe period.
"""
import matplotlib.pyplot as plt
import numpy as np

import wikibio as bio

P = bio.P
rng = np.random.default_rng(1)
N, A = 96, 8
offs = np.arange(-A, A + 1)
na = len(offs)
xs = np.arange(N)


def circ(d):
    return (d + N / 2) % N - N / 2


Bm = np.zeros((N, N))
for i in range(N):
    d = circ(xs - i)
    Bm[i] = np.exp(-d**2 / (2 * 2.0**2)) - 0.25 * np.exp(-d**2 / (2 * 7.0**2))
Bm /= np.abs(Bm).sum(1).max()

pos = (xs[:, None] + offs[None, :]) % N  # afferent position of (x, a)
D = 0.05 * rng.normal(size=(N, na))
# Q between (x, a) and (x', a') for the same eye
Qfull = np.exp(-circ(pos[:, :, None, None] - pos[None, None, :, :]) ** 2 / (2 * 2.5**2))  # (x,a,x',a')


def od():
    return D.mean(1)


snaps = {0: od()}
n_steps, dt = 1500, 0.2
save = {0, 4, 8, 1500}
for it in range(1, n_steps + 1):
    tmp = np.einsum("xayb,yb->xay", Qfull, D)
    dD = np.einsum("xy,xay->xa", Bm, tmp)
    D = np.clip(D + dt * dD, -1, 1)
    if it in save:
        snaps[it] = od()

fig = plt.figure(figsize=(13, 4.2))
ax = fig.add_subplot(1, 3, 1)
for k, (it, col) in enumerate(zip((0, 4, 8, 1500), (P.edge("neutral"), P.edge("dna"), P.edge("rna"), P.edge("positive")))):
    ax.plot(xs, snaps[it] + 0 * k, color=col, lw=1.6 if it else 1.0, label=f"t = {it}" if it else "initial")
ax.axhline(0, color=P.muted(), lw=0.6)
ax.set_xlabel("Cortical position x")
ax.set_ylabel("Ocular dominance index")
ax.set_ylim(-1.15, 1.5)
ax.legend(frameon=False, fontsize=7.5, ncol=4, loc="upper center")
ax.set_title("A  Stripes grow from noise", loc="left", fontsize=10)

bx = fig.add_subplot(1, 3, 2)
bx.imshow(D, aspect="auto", cmap="RdBu", vmin=-1, vmax=1, extent=[-A - 0.5, A + 0.5, N - 0.5, -0.5])
bx.set_xlabel("Afferent offset a")
bx.set_ylabel("Cortical position x")
bx.set_title("B  D = right - left weights (red: left eye)", loc="left", fontsize=10)

cx = fig.add_subplot(1, 3, 3)
for it, col in ((4, P.edge("dna")), (8, P.edge("rna")), (1500, P.edge("positive"))):
    ps = np.abs(np.fft.rfft(snaps[it] - snaps[it].mean())) ** 2
    cx.plot(np.fft.rfftfreq(N)[1:], ps[1:] / ps[1:].max(), color=col, lw=1.6, label=f"t = {it}")
cx.set_xlabel("Spatial frequency (cycles per cortical unit)")
cx.set_ylabel("Power (normalized)")
cx.legend(frameon=False, fontsize=8)
cx.set_title("C  A preferred stripe period", loc="left", fontsize=10)
fig.tight_layout()
