"""Minimum time to distribute a file to N peers: client-server versus peer-to-peer.

Units: F/u = 1 hour (u is the upload rate of a peer), u_s = 10u, d_min >= u_s.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb

dark = sum(to_rgb(plt.rcParams["figure.facecolor"])) < 1.5
C_CS, C_P2P = ("#3987e5", "#d95926") if dark else ("#2a78d6", "#eb6834")

F_over_u = 1.0          # hours to upload the file at peer rate u
us = 10.0               # server upload rate, in units of u
dmin = us               # slowest download rate, in units of u

N = np.arange(1, 36)
d_cs = np.maximum(N * F_over_u / us, F_over_u / dmin)
d_p2p = np.maximum.reduce([
    np.full(N.shape, F_over_u / us),
    np.full(N.shape, F_over_u / dmin),
    N * F_over_u / (us + N * 1.0),
])

fig, ax = plt.subplots(figsize=(6, 3.6), layout="constrained")
ax.plot(N, d_cs, "o-", ms=3, color=C_CS, label="client-server: $NF/u_s$")
ax.plot(N, d_p2p, "s-", ms=3, color=C_P2P, label="P2P: $NF/(u_s + \\sum u_i)$")
ax.axhline(1.0, color="gray", lw=0.8, ls=":")
ax.text(1, 1.05, "P2P limit $F/u$", fontsize=8, color="gray")
ax.set_xlabel("Number of peers $N$")
ax.set_ylabel("Minimum distribution time (hours)")
ax.set_xlim(0, 36)
ax.set_ylim(0, 3.6)
ax.legend(frameon=False, fontsize=9)
ax.spines[["top", "right"]].set_visible(False)
