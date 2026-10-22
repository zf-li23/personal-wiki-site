"""Error of the approximation [H+] = sqrt(Ka c) for a monoprotic weak acid (water autoionization
neglected), against the exact root of x^2 + Ka x - Ka c = 0, as a function of c/Ka."""

import numpy as np
import matplotlib.pyplot as plt

r = np.logspace(0, 5, 400)                 # c / Ka
exact = (-1 + np.sqrt(1 + 4 * r)) / 2      # [H+] / Ka
approx = np.sqrt(r)
err = (approx / exact - 1) * 100
alpha = exact / r * 100                    # degree of dissociation in percent

fig, ax = plt.subplots(figsize=(6, 3.8))
ax.loglog(r, err, color="C0", lw=1.8, label=r"relative error of $\sqrt{K_a c}$ (%)")
ax.loglog(r, alpha, color="C1", lw=1.8, ls="--", label=r"degree of dissociation $\alpha$ (%)")
ax.axvline(400, color="0.5", lw=0.9, ls=":")
ax.plot([400, 400], [2.53, 4.88], "o", color="0.3", ms=4)
ax.annotate("c/Ka = 400:\nerror 2.5 %, alpha 4.9 %", (400, 2.53), xytext=(1500, 12), fontsize=9,
            arrowprops=dict(arrowstyle="-", color="0.5"))
ax.set_xlabel(r"$c/K_a$")
ax.set_ylabel("percent")
ax.legend(frameon=False, fontsize=9, loc="lower left")
fig.tight_layout()
