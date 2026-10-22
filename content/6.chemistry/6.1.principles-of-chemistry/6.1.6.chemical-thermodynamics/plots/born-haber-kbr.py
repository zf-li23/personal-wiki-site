import matplotlib.pyplot as plt

# Born-Haber cycle for KBr at 298.15 K (kJ/mol); zero = elements in their reference states.
d_sub, ie, half_vap, half_bond, ea, d_f = 89.0, 418.8, 15.5, 96.4, 324.5, -393.8
atomize_br = half_vap + half_bond
e0 = 0.0
e1 = d_sub
e2 = e1 + atomize_br
e3 = e2 + ie
e4 = e3 - ea
lattice = e4 - d_f

UP = "#dc2626"
DOWN = "#2563eb"
LINE = "#64748b"

fig, ax = plt.subplots(figsize=(10, 7.5))


def level(x0, e, name, left=True):
    ax.plot([x0, x0 + 1.6], [e, e], color=LINE, lw=2)
    if left:
        ax.text(x0 - 0.05, e, name, va="center", ha="right", fontsize=10)
    else:
        ax.text(x0 + 1.65, e, name, va="center", ha="left", fontsize=10)


def step(xpos, lo, hi, text, color):
    ax.annotate("", xy=(xpos, hi), xytext=(xpos, lo), arrowprops=dict(arrowstyle="-|>", color=color, lw=1.8))
    ax.text(xpos + 0.06, (lo + hi) / 2, text, va="center", fontsize=9.5, color=color)


level(0, e0, r"K(s) + 1/2 Br$_2$(l)")
level(0, e1, r"K(g) + 1/2 Br$_2$(l)")
level(0, e2, "K(g) + Br(g)")
level(0, e3, r"K$^+$(g) + e$^-$ + Br(g)")
level(2.4, e4, r"K$^+$(g) + Br$^-$(g)", left=False)
level(2.4, d_f, "KBr(s)", left=False)

step(0.25, e0, e1, f"sublimation of K  +{d_sub:.1f}", UP)
step(0.25, e1, e2, f"1/2 vaporization + 1/2 bond\nenthalpy of Br$_2$ +{atomize_br:.1f}", UP)
step(0.25, e2, e3, f"ionization energy\n$I_1$(K) +{ie:.1f}", UP)
ax.annotate("", xy=(2.4, e4), xytext=(1.6, e3), arrowprops=dict(arrowstyle="-|>", color=DOWN, lw=1.8))
ax.text(2.1, e3 - 40, f"electron gain of Br\n$-E_{{ea}}$ = $-${ea:.1f}", fontsize=9.5, color=DOWN, ha="left")
step(3.2, e4, d_f, f"$-\\Delta_{{latt}}H$ = $-${lattice:.1f}", DOWN)
ax.annotate("", xy=(1.2, d_f), xytext=(1.2, e0), arrowprops=dict(arrowstyle="-|>", color=DOWN, lw=1.8, ls="--"))
ax.text(1.27, d_f / 2, f"$\\Delta_f H$(KBr, s)\n= {d_f:.1f}", fontsize=9.5, color=DOWN, va="center")
ax.plot([0, 2.4], [d_f, d_f], color=LINE, lw=0.8, ls=":")

ax.set_xlim(-2.6, 5.6)
ax.set_ylim(-450, 680)
ax.set_ylabel(r"enthalpy relative to the elements / (kJ mol$^{-1}$)")
ax.set_xticks([])
for side in ("top", "right", "bottom"):
    ax.spines[side].set_visible(False)
ax.set_title(r"Born-Haber cycle for KBr: $\Delta_{latt}H$ = %.1f kJ mol$^{-1}$" % lattice, fontsize=12)
fig.tight_layout()
