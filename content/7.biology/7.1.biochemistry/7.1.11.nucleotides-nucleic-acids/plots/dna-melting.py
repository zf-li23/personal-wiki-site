"""DNA melting. A: melting curves of long DNAs with 30 %, 50 % and 70 % G+C in standard saline citrate
(0.195 M Na+), drawn as two-state transitions f = 1/(1 + exp[-(dH/R)(1/Tm - 1/T)]) with the midpoint from
the Marmur-Doty relation Tm = 69.3 + 0.41 (%GC) deg C and an illustrative van 't Hoff enthalpy of the
cooperative unit (1100 kJ/mol, about 4 deg C between 10 % and 90 % melted); absorbance at 260 nm rises
by about 40 % (hyperchromic effect). B: Tm against G+C content at three Na+ concentrations,
Tm = 81.5 + 16.6 lg[Na+] + 0.41 (%GC) (Schildkraut-Lifson; long DNA, [Na+] up to about 0.2 M).
C: Tm of the 20-mer TAATACGACTCACTATAGGG paired with its complement, from the nearest-neighbour model
with the unified parameters of SantaLucia (1998): Tm = dH / (dS + R ln(C_T/4)) for two different strands
at equal concentration, total strand concentration C_T; salt correction of the entropy
dS([Na+]) = dS(1 M) + 0.368 (N - 1) ln[Na+] cal mol-1 K-1 (N = 20 base pairs)."""

import numpy as np
import wikibio as bio
from wikibio import charts

P = bio.P
R = 8.314

# SantaLucia (1998) unified nearest-neighbour parameters, 1 M NaCl: dH / kcal mol-1, dS / cal mol-1 K-1
NN = {"AA": (-7.9, -22.2), "TT": (-7.9, -22.2), "AT": (-7.2, -20.4), "TA": (-7.2, -21.3), "CA": (-8.5, -22.7),
      "TG": (-8.5, -22.7), "GT": (-8.4, -22.4), "AC": (-8.4, -22.4), "CT": (-7.8, -21.0), "AG": (-7.8, -21.0),
      "GA": (-8.2, -22.2), "TC": (-8.2, -22.2), "CG": (-10.6, -27.2), "GC": (-9.8, -24.4), "GG": (-8.0, -19.9),
      "CC": (-8.0, -19.9)}
INIT = {"G": (0.1, -2.8), "C": (0.1, -2.8), "A": (2.3, 4.1), "T": (2.3, 4.1)}


def nn_tm(seq, ct, na):
    dh = sum(NN[seq[i:i + 2]][0] for i in range(len(seq) - 1)) + INIT[seq[0]][0] + INIT[seq[-1]][0]
    ds = sum(NN[seq[i:i + 2]][1] for i in range(len(seq) - 1)) + INIT[seq[0]][1] + INIT[seq[-1]][1]
    ds += 0.368 * (len(seq) - 1) * np.log(na)
    dh, ds = dh * 4184.0, ds * 4.184  # to J
    return dh / (ds + R * np.log(ct / 4)) - 273.15


fig, ax = bio.canvas(24.0, 7.8)

# --- A: melting curves ---------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 7.7))
pa = charts.axes_at(ax, (1.5, 1.4, 5.8, 5.6))
T = np.linspace(55, 115, 600)
dH = 1.1e6
for gc, tok, ty in ((30, "dna2", 1.33), (50, "dna", 1.22), (70, "protein", 1.11)):
    tm = 69.3 + 0.41 * gc
    f = 1 / (1 + np.exp(-(dH / R) * (1 / (tm + 273.15) - 1 / (T + 273.15))))
    pa.plot(T, 1 + 0.4 * f, color=charts.line(tok), lw=1.8)
    pa.text(tm - 2.6, ty, f"{gc}% GC, $T_\\mathrm{{m}}$ = {tm:.0f} °C", ha="right", fontsize=bio.core.FONT["tiny"],
            color=charts.line(tok))
pa.set_xlim(55, 115)
pa.set_ylim(0.95, 1.48)
charts.style_axes(pa, "$T$ / °C", "relative $A_{260}$")

# --- B: Tm vs GC -------------------------------------------------------------------------------------
bio.panel(ax, "B", (8.3, 7.7))
pb = charts.axes_at(ax, (9.7, 1.4, 5.8, 5.6))
gc = np.linspace(20, 80, 50)
for na, tok in ((0.195, "dna"), (0.05, "enzyme"), (0.01, "drug")):
    pb.plot(gc, 81.5 + 16.6 * np.log10(na) + 0.41 * gc, color=charts.line(tok), lw=1.8)
    pb.text(81, 81.5 + 16.6 * np.log10(na) + 0.41 * 80, f"{na * 1000:.0f} mM Na⁺", fontsize=bio.core.FONT["tiny"],
            color=charts.line(tok), va="center")
pb.set_xlim(20, 80)
pb.set_ylim(40, 110)
charts.style_axes(pb, "G + C / %", "$T_\\mathrm{m}$ / °C")

# --- C: nearest-neighbour Tm of a primer -------------------------------------------------------------------
bio.panel(ax, "C", (16.6, 7.7))
pc = charts.axes_at(ax, (18.0, 1.4, 5.0, 5.6))
seq = "TAATACGACTCACTATAGGG"
ct = np.logspace(-8, -4, 60)
for na, tok in ((1.0, "dna"), (0.05, "enzyme")):
    tms = [nn_tm(seq, c, na) for c in ct]
    pc.semilogx(ct * 1e6, tms, color=charts.line(tok), lw=1.8, label=f"{na * 1000:.0f} mM Na⁺")
    v = nn_tm(seq, 5e-7, na)
    pc.plot([0.5], [v], "o", ms=4, color=charts.line(tok))
    pc.text(0.6, v - 1.6, f"{v:.0f} °C", fontsize=bio.core.FONT["tiny"], color=charts.line(tok), va="top")
pc.legend(frameon=False, fontsize=bio.core.FONT["tiny"], labelcolor=P.ink(), loc="upper left")
pc.set_ylim(30, 75)
charts.style_axes(pc, "total strand concentration / µM", "$T_\\mathrm{m}$ / °C")
bio.label(ax, (20.5, 7.4), "20-mer, nearest-neighbour model", size="small")
