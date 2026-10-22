import numpy as np
import matplotlib.pyplot as plt

# One mole of a monatomic ideal gas at fixed volume (arbitrary reference point):
# S = S0 + C_V ln(T/T0)  =>  U(S) = C_V T0 exp((S - S0)/C_V), a convex function.
R = 8.314
CV = 1.5 * R
T0, S0 = 300.0, 100.0


def U_of_S(s):
    return CV * T0 * np.exp((s - S0) / CV)


def T_of_S(s):
    return T0 * np.exp((s - S0) / CV)


S = np.linspace(85, 118, 300)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.8))

a1.plot(S, U_of_S(S) / 1e3, color="#2563eb", lw=2, label="$U(S)$ at fixed $V$")
s1 = 108.0
t1, u1 = T_of_S(s1), U_of_S(s1)
A1 = u1 - t1 * s1
s_line = np.linspace(0, 118, 50)
a1.plot(s_line, (u1 + t1 * (s_line - s1)) / 1e3, color="#d97706", lw=1.5, ls="--",
        label=f"tangent, slope $T$ = {t1:.0f} K")
a1.plot([s1], [u1 / 1e3], "o", color="#d97706")
a1.plot([0], [A1 / 1e3], "s", color="#dc2626")
a1.annotate("intercept $A = U - TS$", (0, A1 / 1e3), textcoords="offset points",
            xytext=(10, -4), fontsize=10, color="#dc2626")
a1.axvline(0, color="#94a3b8", lw=1)
a1.set_xlim(-5, 118)
a1.set_xlabel(r"$S$ / (J K$^{-1}$)")
a1.set_ylabel(r"$U$ / kJ (arbitrary zero)")
a1.set_title("Each tangent line is labelled by its slope $T$ and intercept $A$", fontsize=11)
a1.legend(fontsize=9, loc="upper left")
a1.grid(alpha=0.3)

# Right: the transform A(T) = U - TS as a function of T; its slope is -S.
Ss = np.linspace(85, 118, 300)
Ts = T_of_S(Ss)
As = U_of_S(Ss) - Ts * Ss
a2.plot(Ts, As / 1e3, color="#16a34a", lw=2, label="$A(T) = U - TS$")
tt = np.linspace(t1 - 150, t1 + 150, 20)
a2.plot(tt, (A1 - s1 * (tt - t1)) / 1e3, color="#d97706", lw=1.5, ls="--",
        label=f"slope $-S$ = {-s1:.0f} J K$^{{-1}}$")
a2.plot([t1], [A1 / 1e3], "o", color="#d97706")
a2.set_xlabel("$T$ / K")
a2.set_ylabel(r"$A$ / kJ (arbitrary zero)")
a2.set_title("The transformed function is concave in $T$", fontsize=11)
a2.legend(fontsize=9, loc="lower left")
a2.grid(alpha=0.3)
fig.tight_layout()
