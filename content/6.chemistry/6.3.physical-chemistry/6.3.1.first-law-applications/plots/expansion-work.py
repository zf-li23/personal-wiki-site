import numpy as np
import matplotlib.pyplot as plt

# Isothermal ideal gas, pV = 24 kJ: 4 kPa, 6 m^3 -> 1 kPa, 24 m^3 and back.
PV = 24.0  # kJ
V_rev = np.linspace(6, 24, 300)
p_rev = PV / V_rev


def staircase(pressures, start_v):
    """Return the external-pressure path and the work done on the gas."""
    vs, ps = [start_v], []
    work = 0.0
    v = start_v
    for p_ext in pressures:
        v_new = PV / p_ext
        work += -p_ext * (v_new - v)
        vs.append(v_new)
        ps.append(p_ext)
        v = v_new
    return vs, ps, work


colors = ["#dc2626", "#d97706", "#16a34a"]
fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), sharey=True)
cases_exp = [[1], [2, 1], [3, 2, 1]]
cases_cmp = [[4], [2, 4], [2, 3, 4]]
for ax, cases, start, title in [
    (axes[0], cases_exp, 6.0, "Expansion 4 kPa -> 1 kPa"),
    (axes[1], cases_cmp, 24.0, "Compression 1 kPa -> 4 kPa"),
]:
    ax.plot(V_rev, p_rev, color="#2563eb", lw=2, label=f"reversible, W = {(-1 if start < 10 else 1) * PV * np.log(4):+.1f} kJ")
    for k, (pressures, c) in enumerate(zip(cases, colors)):
        vs, ps, w = staircase(pressures, start)
        xs, ys = [], []
        for i, p_ext in enumerate(ps):
            xs += [vs[i], vs[i + 1]]
            ys += [p_ext, p_ext]
        ax.step(xs, ys, where="post", color=c, lw=1.6, label=f"{k + 1} step(s), W = {w:+.0f} kJ")
        ax.fill_between(xs, ys, color=c, alpha=0.08)
    ax.set_title(title, fontsize=11)
    ax.set_xlabel(r"$V$ / m$^3$")
    ax.set_xlim(0, 26)
    ax.set_ylim(0, 4.6)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8.5, loc="upper right")
axes[0].set_ylabel(r"$p$ (gas) or $p_{\mathrm{ex}}$ / kPa")
fig.suptitle("Work on an ideal gas at constant T: area under the external-pressure path", fontsize=11)
fig.tight_layout()
