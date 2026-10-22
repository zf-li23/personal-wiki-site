import numpy as np
import matplotlib.pyplot as plt

# Liquid water at 1 bar: density and isothermal compressibility from Kell (1975) fits.
M = 18.01528e-3  # kg/mol


def rho(t):
    num = (999.83952 + 16.945176 * t - 7.9870401e-3 * t**2 - 46.170461e-6 * t**3
           + 105.56302e-9 * t**4 - 280.54253e-12 * t**5)
    return num / (1 + 16.879850e-3 * t)  # kg/m^3


def kappa_T(t):
    num = (50.88496 + 0.6163813 * t + 1.459187e-3 * t**2 + 20.08438e-6 * t**3
           - 58.47727e-9 * t**4 + 410.4110e-12 * t**5)
    return num / (1 + 19.67348e-3 * t) * 1e-11  # 1/Pa (fit gives 1e-6 per bar)


t = np.linspace(0, 100, 401)
h = 1e-3
alpha = -(rho(t + h) - rho(t - h)) / (2 * h) / rho(t)  # 1/K
Vm = M / rho(t)
T = t + 273.15
diff = T * Vm * alpha**2 / kappa_T(t)  # J/(K mol)

fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.6))
a1.plot(t, alpha * 1e4, color="#2563eb", lw=2)
a1.axhline(0, color="#94a3b8", lw=1)
t_max = t[np.argmin(np.abs(alpha))]
a1.plot([t_max], [0], "o", color="#dc2626")
a1.annotate(f"density maximum, {t_max:.2f} $^\\circ$C", (t_max, 0), textcoords="offset points",
            xytext=(10, -18), fontsize=9, color="#dc2626")
a1.set_xlabel(r"$t$ / $^\circ$C")
a1.set_ylabel(r"$\alpha_V$ / (10$^{-4}$ K$^{-1}$)")
a1.set_title("Expansion coefficient of liquid water", fontsize=11)
a1.grid(alpha=0.3)

a2.plot(t, diff, color="#16a34a", lw=2)
a2.plot([25], [np.interp(25, t, diff)], "o", color="#d97706")
a2.annotate(f"25 $^\\circ$C: {np.interp(25, t, diff):.2f}", (25, np.interp(25, t, diff)),
            textcoords="offset points", xytext=(8, 6), fontsize=9, color="#d97706")
a2.set_xlabel(r"$t$ / $^\circ$C")
a2.set_ylabel(r"$C_{p,\mathrm{m}} - C_{V,\mathrm{m}}$ / (J K$^{-1}$ mol$^{-1}$)")
a2.set_title(r"$T V_\mathrm{m}\alpha_V^2/\kappa_T$ (compare $C_{p,\mathrm{m}} \approx 75.3$)", fontsize=11)
a2.grid(alpha=0.3)
fig.tight_layout()
