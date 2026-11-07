# Ion composition of saliva and pancreatic juice against secretion rate (two-stage models).
# A, saliva: acini secrete a plasma-like primary fluid (Na+ 145, K+ 4, Cl- 120 mM; HCO3- rises with
# stimulation from 25 to 75 mM). The water-impermeable striated ducts modify it during a residence
# time tau = 1/Q (min, Q = flow in mL/min): saturable Na+ and Cl- reabsorption toward a floor of 3 mM,
#   dC/dtau = -Vm (C - 3) / (Km + C - 3),  Na+: Vm = 250, Cl-: Vm = 220 mM/min, Km = 100 mM,
# and K+ secretion that saturates, C_K = 4 + 30 (1 - exp(-tau / 0.72 min)). At low flow saliva is
# strongly hypotonic and K+-rich; at high flow it approaches plasma.
# B, pancreatic juice: acinar fluid (fixed 0.2 mL/min; Cl- 125, HCO3- 25 mM) mixes with secretin-
# stimulated ductal fluid (HCO3- 145, Cl- 10 mM). Cl- and HCO3- change reciprocally; their sum and
# Na+ (about 150 mM) are nearly constant. Plasma values shown as dotted lines.
import matplotlib.pyplot as plt
import numpy as np

Q = np.linspace(0.05, 4, 80)


def duct(C0, Vm, tau, Km=100.0, floor=3.0, n=400):
    C = C0
    h = tau / n
    for _ in range(n):
        C -= h * Vm * (C - floor) / (Km + C - floor)
    return C


tau = 1 / Q
na = np.array([duct(145.0, 250.0, s) for s in tau])
cl = np.array([duct(120.0, 220.0, s) for s in tau])
k = 4 + 30 * (1 - np.exp(-tau / 0.72))
hco3 = 25 + 50 * Q / (Q + 0.8)

fig, (axa, axb) = plt.subplots(1, 2, figsize=(11, 4.3))
for y, c, lab, pl in ((na, "#2f6fb5", "Na$^+$", 142), (cl, "#2a9d8f", "Cl$^-$", 104),
                      (k, "#c0392b", "K$^+$", 4.5), (hco3, "#d9822b", "HCO$_3^-$", 24)):
    axa.plot(Q, y, color=c, lw=2, label=lab)
axa.axhline(142, color="#2f6fb5", lw=0.8, ls=":")
axa.text(0.1, 146, "plasma Na$^+$", fontsize=8, color="#2f6fb5")
axa.set_xlim(0, 4.2)
axa.set_xlabel("Salivary flow / (mL/min)")
axa.set_ylabel("Concentration / (mmol/L)")
axa.set_ylim(0, 160)
axa.set_title("A  Saliva: ducts modify a primary fluid", loc="left", fontsize=11, fontweight="bold")
axa.legend(frameon=False, fontsize=8.5, loc="upper left", bbox_to_anchor=(0.0, 0.85))

Qd = np.linspace(0, 4, 80)
Qa = 0.2
F = Qa + Qd
h2 = (Qa * 25 + Qd * 145) / F
c2 = (Qa * 125 + Qd * 10) / F
axb.plot(F, np.full_like(F, 152), color="#2f6fb5", lw=2, label="Na$^+$")
axb.plot(F, c2, color="#2a9d8f", lw=2, label="Cl$^-$")
axb.plot(F, h2, color="#d9822b", lw=2, label="HCO$_3^-$")
axb.plot(F, np.full_like(F, 5), color="#c0392b", lw=2, label="K$^+$")
axb.axhline(24, color="#d9822b", lw=0.8, ls=":")
axb.text(4.1, 26, "plasma HCO$_3^-$", ha="right", fontsize=8, color="#d9822b")
axb.set_xlabel("Pancreatic flow / (mL/min)")
axb.set_ylabel("Concentration / (mmol/L)")
axb.set_ylim(0, 160)
axb.set_xlim(0, 4.2)
axb.set_title("B  Pancreatic juice: Cl$^-$ for HCO$_3^-$", loc="left", fontsize=11, fontweight="bold")
axb.legend(frameon=False, fontsize=8.5, loc="center right")
fig.tight_layout()
