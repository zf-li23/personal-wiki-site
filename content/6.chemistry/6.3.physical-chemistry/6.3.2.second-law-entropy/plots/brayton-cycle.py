import numpy as np
import matplotlib.pyplot as plt

# Ideal Brayton cycle with air (ideal gas): ambient T1, burner outlet T2.
T1, T2 = 300.0, 1500.0
GAMMA = 1.4
CP = GAMMA / (GAMMA - 1) * 8.314  # J K^-1 mol^-1

tc = np.linspace(T1, T2, 400)  # temperature after adiabatic compression
t3 = T2 * T1 / tc  # temperature after adiabatic expansion
eta = 1 - T1 / tc
work = CP * ((T2 - t3) - (tc - T1)) / 1e3  # net work per mole of air, kJ
ratio = (tc / T1) ** (GAMMA / (GAMMA - 1))  # pressure ratio

fig, ax1 = plt.subplots(figsize=(7.4, 4.6))
ax1.plot(tc, eta, color="#2563eb", lw=2, label=r"efficiency $\eta = 1 - T_1/T_{\mathrm{comp}}$")
ax1.axhline(1 - T1 / T2, color="#2563eb", lw=0.8, ls="--")
ax1.text(T2 - 10, 1 - T1 / T2 + 0.02, f"Carnot limit 1 - T1/T2 = {1 - T1 / T2:.2f}", fontsize=9, color="#2563eb", ha="right")
ax1.set_xlabel(r"temperature after compression $T_{\mathrm{comp}}$ / K")
ax1.set_ylabel("efficiency", color="#2563eb")
ax1.set_ylim(0, 1)
ax2 = ax1.twinx()
ax2.plot(tc, work, color="#dc2626", lw=2, label="net work per mol of air")
i = np.argmax(work)
ax2.plot([tc[i]], [work[i]], "o", color="#dc2626")
ax2.annotate(r"max work at $T_{\mathrm{comp}} = \sqrt{T_1T_2}$" + f", pressure ratio {ratio[i]:.0f}",
             (tc[i], work[i]), xytext=(720, 2.0), fontsize=9,
             arrowprops=dict(arrowstyle="->", color="#94a3b8"))
ax2.set_ylabel("net work / (kJ per mol)", color="#dc2626")
ax2.set_ylim(0, 1.6 * work.max())
lines = ax1.get_lines()[:1] + ax2.get_lines()[:1]
ax1.legend(lines, [l.get_label() for l in lines], fontsize=9, loc="upper left")
ax1.set_title(f"Ideal Brayton cycle, T1 = {T1:.0f} K, T2 = {T2:.0f} K", fontsize=11)
ax1.grid(alpha=0.3)
fig.tight_layout()
