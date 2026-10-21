"""Speed distributions in reduced speed u = v/v_p: gas (u^2), effusive beam (u^3) and Miller-Kusch detector (u^4)."""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

u = np.linspace(0, 3.5, 700)
fig, ax = plt.subplots(figsize=(6.4, 4))

labels = {2: r"gas: $u^2 e^{-u^2}$", 3: r"effusive beam: $u^3 e^{-u^2}$", 4: r"detector: $u^4 e^{-u^2}$"}
for i, n in enumerate([2, 3, 4]):
    norm = quad(lambda x: x**n * np.exp(-x**2), 0, np.inf)[0]
    y = u**n * np.exp(-u**2) / norm
    ax.plot(u, y, color=f"C{i}", lw=1.6, label=labels[n])
    peak = np.sqrt(n / 2)
    ax.axvline(peak, color=f"C{i}", ls=":", lw=1)

ax.set_xlim(0, 3.5)
ax.set_ylim(bottom=0)
ax.set_xlabel(r"reduced speed $u = v/v_{\mathrm{p}}$")
ax.set_ylabel("normalized density")
ax.set_title(r"Each factor of $v$ shifts the peak (dotted) to the right")
ax.legend(fontsize=9)
fig.tight_layout()
