"""Voltage transfer characteristic of a CMOS inverter (square-law MOSFET model,
VDD = 1.8 V, |Vt| = 0.45 V, matched transistors, channel-length modulation 0.1/V).
VIL and VIH are the points where the slope is -1; the supply current flows only
while the input is between the two thresholds."""

import numpy as np
import matplotlib.pyplot as plt

VDD, VT, K, LAM = 1.8, 0.45, 1.0, 0.1


def ids(vgs, vds):
    """Drain current of a MOSFET (normalized), level-1 model."""
    vov = vgs - VT
    if vov <= 0:
        return 0.0
    if vds < vov:
        i = K * (vov * vds - vds ** 2 / 2)
    else:
        i = K / 2 * vov ** 2
    return i * (1 + LAM * vds)


def vout(vin):
    lo, hi = 0.0, VDD
    for _ in range(60):
        mid = (lo + hi) / 2
        if ids(vin, mid) > ids(VDD - vin, VDD - mid):
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


vin = np.linspace(0, VDD, 721)
vo = np.array([vout(v) for v in vin])
cur = np.array([ids(v, o) for v, o in zip(vin, vo)])
slope = np.gradient(vo, vin)
mid = len(vin) // 2
vil = vin[:mid][np.argmin(np.abs(slope[:mid] + 1))]
vih = vin[mid:][np.argmin(np.abs(slope[mid:] + 1))]
vm = vin[np.argmin(np.abs(vo - vin))]

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
ax = axes[0]
ax.plot(vin, vo, color="C0", lw=2)
ax.plot([0, VDD], [0, VDD], color="gray", lw=0.8, ls=":")
for v, name in ((vil, "VIL"), (vih, "VIH"), (vm, "VM")):
    ax.axvline(v, color="gray", lw=0.8, ls="--")
    ax.text(v + 0.02, 1.05, f"{name} = {v:.2f} V", rotation=90, ha="left", va="bottom", fontsize=8)
ax.text(0.05, VDD - 0.05, "N off, P on\noutput = VDD", va="top", fontsize=8)
ax.text(VDD - 0.05, 0.08, "N on, P off\noutput = 0", ha="right", fontsize=8)
ax.set_xlabel("input voltage Vin (V)")
ax.set_ylabel("output voltage Vout (V)")
ax.set_title("voltage transfer characteristic")
ax.set_xlim(0, VDD)
ax.set_ylim(-0.05, VDD + 0.05)
ax.grid(alpha=0.3)
ax = axes[1]
ax.plot(vin, cur / cur.max(), color="C1", lw=2)
ax.set_xlabel("input voltage Vin (V)")
ax.set_ylabel("supply current (normalized)")
ax.set_title("current drawn from VDD")
ax.set_xlim(0, VDD)
ax.grid(alpha=0.3)
fig.tight_layout()
