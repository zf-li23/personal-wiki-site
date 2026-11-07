# Countercurrent multiplication in the loop of Henle: the classic stepwise model (illustrative).
# The loop is divided into N levels. The descending limb is water-permeable and equilibrates with the
# interstitium at each level; the ascending limb is water-impermeable and pumps NaCl into the interstitium
# until, at each level, it is a fixed "single effect" D (mOsm/kg) below the descending limb and interstitium.
# The two steps alternate: (1) pump: at each level the mean m of the two limbs is kept and they are set to
# m + D/2 (descending, interstitium) and m - D/2 (ascending); (2) flow: fluid moves down the descending limb
# by one level (fresh 300 mOsm/kg fluid enters at the top), turns at the tip and moves up the ascending limb
# by one level (the top level leaves toward the distal tubule). In each cycle the vasa recta remove a fraction
# k = 0.03 of the excess solute (above 300) at every level; without this washout the gradient would grow
# without bound, with it the profile reaches a steady state.
# A: profiles of the interstitium (solid) and the ascending limb (dashed) after increasing numbers of
# cycles, N = 10, D = 200 (the ascending limb leaves hypo-osmotic, about 150). B: steady-state tip osmolality against the single effect, for three loop lengths:
# a small transverse gradient is multiplied into a large axial one, more so in a longer loop.
import matplotlib.pyplot as plt
import numpy as np


def simulate(N=10, D=200.0, cycles=1500, record=(), k=0.03):
    desc = np.full(N, 300.0)
    asc = np.full(N, 300.0)
    snaps = {}
    for c in range(1, cycles + 1):
        m = (desc + asc) / 2
        desc, asc = m + D / 2, m - D / 2
        desc = desc - k * (desc - 300.0)
        if c in record:
            snaps[c] = (desc.copy(), asc.copy())
        tip = desc[-1]
        desc = np.concatenate([[300.0], desc[:-1]])
        asc = np.concatenate([asc[1:], [tip]])
    m = (desc + asc) / 2
    return m + D / 2, m - D / 2, snaps


fig, (axa, axb) = plt.subplots(1, 2, figsize=(10.5, 4.4))
rec = (1, 3, 8, 20, 60, 1500)
_, _, snaps = simulate(record=rec)
cmap = plt.get_cmap("viridis")
depth = (np.arange(10) + 0.5) / 10
for j, k in enumerate(rec):
    d, a = snaps[k]
    c = cmap(0.1 + 0.8 * j / (len(rec) - 1))
    lab = f"cycle {k}" if k < 1500 else "steady state"
    axa.plot(d, depth, color=c, lw=2, label=lab)
    axa.plot(a, depth, color=c, lw=1.2, ls="--")
axa.invert_yaxis()
axa.set_xlim(0, 1400)
axa.set_xlabel("Osmolality (mOsm/kg)")
axa.set_ylabel("Depth (cortex 0 to papillary tip 1)")
axa.set_title("A  Building the gradient", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="lower left")
axa.text(1380, 0.06, "solid: descending limb = interstitium\ndashed: ascending limb", fontsize=8, ha="right", va="top")

Ds = np.linspace(25, 250, 30)
for N, c in [(5, "#7a4fb3"), (10, "#2f6fb5"), (20, "#3c9a5f")]:
    tips = [simulate(N=N, D=D)[0][-1] for D in Ds]
    axb.plot(Ds, tips, color=c, lw=2, label=f"N = {N} levels")
axb.axhline(1200, color="#9e9e9e", lw=0.8, ls=":")
axb.text(30, 1250, "human maximum, 1200", fontsize=8.5)
axb.set_xlim(0, 260)
axb.set_ylim(0, 2500)
axb.set_xlabel("Single effect D (mOsm/kg)")
axb.set_ylabel("Tip osmolality (mOsm/kg)")
axb.set_title("B  Multiplication of the single effect", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="upper left", bbox_to_anchor=(0, 0.92))
for ax in (axa, axb):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
fig.tight_layout()
