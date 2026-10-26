"""Simulated oxygen-electrode trace of isolated mitochondria (1 mg protein per mL, 37 C, air-saturated
medium with ~210 uM O2) oxidizing an NADH-linked substrate. Model: O2 consumption J = J4 + (J3 - J4)
[ADP]/(K + [ADP]) (nmol O2 per min per mL); each O2 consumed above the leak rate J4 phosphorylates
2 x (P/O) ADP. Additions: substrate (glutamate + malate), two pulses of ADP (state 3 -> state 4 when the
ADP is used up), oligomycin (ATP synthase blocked: back to the leak rate), DNP (uncoupled: maximal rate
without ATP synthesis), cyanide (Complex IV blocked). Parameters are illustrative: J4 = 8, J3 = 55,
Jmax(DNP) = 75, K = 15 uM, P/O = 2.5."""

import numpy as np

import wikibio as bio
from wikibio import charts

P = bio.P
dt = 0.005
t = np.arange(0, 16, dt)
O2 = np.empty_like(t)
o2, adp = 210.0, 0.0
J4, J3, Jdnp, K, PO = 8.0, 55.0, 75.0, 15.0, 2.5
events = {1.0: "substrate", 3.0: "ADP", 7.0: "ADP", 10.0: "oligomycin", 12.0: "DNP", 14.5: "CN⁻"}
state = {"substrate": False, "oligo": False, "dnp": False, "cn": False}
for i, ti in enumerate(t):
    for te, name in events.items():
        if abs(ti - te) < dt / 2:
            if name == "substrate":
                state["substrate"] = True
            elif name == "ADP":
                adp += 150.0
            elif name == "oligomycin":
                state["oligo"] = True
            elif name == "DNP":
                state["dnp"] = True
            else:
                state["cn"] = True
    if not state["substrate"] or state["cn"] or o2 <= 0:
        J = 0.6 if not state["cn"] else 0.0
    elif state["dnp"]:
        J = Jdnp
    elif state["oligo"]:
        J = J4 * 0.9
    else:
        J = J4 + (J3 - J4) * adp / (K + adp)
        adp = max(0.0, adp - 2 * PO * (J - J4) * dt)
    o2 = max(0.0, o2 - J * dt)
    O2[i] = o2

fig, ax = bio.canvas(17.0, 9.0)
a = charts.axes_at(ax, (2.0, 1.4, 14.2, 6.6))
a.plot(t, O2, color=charts.line("blood"), lw=2.0)
for te, name in events.items():
    y = np.interp(te, t, O2)
    a.annotate(name, (te, y + 3), (te, y + 30), ha="center", fontsize=bio.core.FONT["tiny"], color=P.ink(),
               arrowprops=dict(arrowstyle="->", color=P.muted(), lw=0.8))
# label the respiratory states
for x, y, s in ((1.4, 214, "state 2"), (3.55, 180, "state 3"), (4.9, 160, "state 4"), (7.55, 122, "state 3"),
                (8.6, 98, "state 4"), (10.4, 84, "leak only"), (12.75, 48, "uncoupled")):
    a.text(x, y, s, fontsize=bio.core.FONT["tiny"], color=P.muted(), ha="left")
a.set_xlim(0, 16)
a.set_ylim(0, 260)
charts.style_axes(a, "t / min", "[O₂] / µM")
charts.title(a, "Respiratory control: O₂ is consumed fast only while ADP is being phosphorylated")
