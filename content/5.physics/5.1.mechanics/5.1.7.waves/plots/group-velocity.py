"""A deep-water wave packet: the envelope moves at the group velocity, a crest at the phase velocity."""

import numpy as np
import matplotlib.pyplot as plt

g = 9.8
k0 = 2 * np.pi  # wavelength 1 m
w0 = np.sqrt(g * k0)
u = w0 / k0          # phase velocity
vg = 0.5 * u         # group velocity
sig_k = 0.12 * k0

ks = np.linspace(k0 - 4 * sig_k, k0 + 4 * sig_k, 401)
amp = np.exp(-((ks - k0) ** 2) / (2 * sig_k ** 2))
amp /= amp.sum()
x = np.linspace(-6, 16, 3000)


def field(t):
    ph = np.outer(x, ks) - np.sqrt(g * ks)[None, :] * t
    return (np.cos(ph) * amp[None, :]).sum(axis=1)


fig, ax = plt.subplots(figsize=(10.0, 4.2))
times = [0.0, 2.0 * 1.0 / u * 2.5]
offsets = [1.6, 0.0]
for i, (t, off) in enumerate(zip(times, offsets)):
    y = field(t)
    ymax = np.abs(y).max()
    ax.plot(x, y / ymax + off, color=f"C{i}", lw=1.2, label=f"t = {t:.1f} s")
    env = np.exp(-(sig_k ** 2) * (x - vg * t) ** 2 / 2)
    ax.plot(x, env + off, color="0.55", lw=0.8, ls="--")
    ax.plot(x, -env + off, color="0.55", lw=0.8, ls="--")
    # one carrier crest that starts at x = -1 (a crest at t = 0 since k0 = 2 pi)
    xc = -1.0 + u * t
    ax.plot([xc], [1.0 + off + 0.12], "o", color="C3", ms=5)
    ax.plot([vg * t], [off - 1.25], "^", color="0.3", ms=6)

ax.text(0.0, -1.55, "packet centre moves at v_g = u/2", fontsize=9)
ax.set_xlabel("x / m")
ax.set_yticks([])
ax.set_ylim(-1.8, 2.9)
ax.set_title("Deep-water wave packet: crest (dot) at u, envelope at v_g")
ax.legend(loc="upper right", fontsize=8)
fig.tight_layout()
