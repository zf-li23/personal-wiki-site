"""Ring strain of cycloalkanes (CH2)n from gas-phase heats of combustion: strain = n * (q_n - 658.6),
where q_n is the heat of combustion per CH2 and 658.6 kJ/mol the value for an unstrained CH2
(long open-chain alkanes). The dashed curve is what a planar ring (Baeyer) would predict from
angle strain alone, in arbitrary scaling: proportional to n * (109.5 - interior angle)^2."""

import numpy as np
import matplotlib.pyplot as plt

n = np.array([3, 4, 5, 6, 7, 8, 9, 10, 14])
q = np.array([2091, 2744, 3320, 3953, 4637, 5310, 5981, 6636, 9220])  # kJ/mol
strain = q - 658.6 * n
per = q / n

fig, ax = plt.subplots(figsize=(7.5, 3.8))
ax.bar([str(k) for k in n], strain, color="C0", width=0.6)
for i, (s, p) in enumerate(zip(strain, per)):
    ax.text(i, max(s, 0) + 3, f"{abs(s):.0f}", ha="center", fontsize=9)
    ax.text(i, -16, f"{p:.0f}", ha="center", fontsize=8, color="0.45")
interior = 180 - 360 / n
baeyer = n * (109.5 - interior) ** 2
baeyer = baeyer / baeyer[0] * strain[0]
ax.plot(range(len(n)), baeyer, "o--", color="C3", ms=4, label="planar-ring (Baeyer) estimate, scaled")
ax.set_ylim(-22, 140)
ax.axhline(0, color="0.6", lw=0.8)
ax.set_xlabel("ring size $n$ (number below bar: heat of combustion per CH$_2$ / kJ mol$^{-1}$)")
ax.set_ylabel(r"strain energy / (kJ mol$^{-1}$)")
ax.legend(frameon=False, fontsize=9)
fig.tight_layout()
