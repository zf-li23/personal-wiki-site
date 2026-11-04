# The transcriptional cascade of DNA viruses.
# A: timelines for three programmes, with the onset of viral DNA synthesis and the regulators that drive
#    each transition. B: a minimal kinetic model of the same logic - an immediate-early regulator drives
#    early proteins, early proteins replicate the genome, and late promoters are active only in proportion
#    to the number of progeny genomes. The simulation reproduces the order and the sharp late burst.
import numpy as np
import wikibio as bio
from wikibio import quant

P = bio.P
fig, ax = bio.canvas(17, 8.4)

# --- A  three programmes ----------------------------------------------------------------------------------
bio.panel(ax, "A", (0.1, 8.2))
bio.label(ax, (4.6, 8.0), "Three transcriptional programmes", size="title", bold=True)
rows = [
    ("Simian virus 40", 6.6, [(0.6, 4.2, "Early (large T)", "positive"), (4.2, 8.6, "Late (capsid)", "virus")], 4.2,
     [(1.1, "large T")]),
    ("Adenovirus", 4.6, [(0.4, 1.6, "IE (E1A)", "highlight"), (1.6, 5.2, "Early (E2: replication)", "positive"),
                         (5.2, 8.6, "Late (structural)", "virus")], 5.2, [(0.7, "E1A"), (5.6, "IVa2")]),
    ("Herpes simplex virus 1", 2.6, [(0.4, 1.8, "IE (ICP4, ICP0)", "highlight"), (1.8, 5.0, "Early (replication)", "positive"),
                                     (5.0, 8.6, "Late (structural)", "virus")], 5.0, [(0.3, "VP16"), (2.0, "ICP4")]),
]
x0 = 0.7
for name, y, bands, dna, marks in rows:
    bio.label(ax, (x0, y + 0.72), name, size="small", bold=True, ha="left")
    for a, b, text, tok in bands:
        bio.box(ax, (x0 + (a + b) / 2, y), b - a, 0.62, tok, text=text, size="tiny", radius=0.08)
    ax.plot([x0 + dna, x0 + dna], [y - 0.55, y + 0.55], color=P.edge("dna"), lw=2.0, ls="--", zorder=14)
    for mx, mt in marks:
        bio.label(ax, (x0 + mx, y - 0.62), mt, size="tiny", color=P.muted(), ha="left")
bio.label(ax, (x0 + 5.0, 7.55), "viral DNA synthesis", size="tiny", color=P.edge("dna"))
bio.arrow(ax, (x0 + 0.2, 1.5), (x0 + 8.6, 1.5), kind="process", color=P.muted())
bio.label(ax, (x0 + 4.4, 1.05), "Time after infection", size="small", color=P.muted())
bio.label(ax, (x0 + 4.4, 0.4), "Late transcription requires replicated templates, so capsids appear\nonly when there are genomes to package",
          size="tiny", color=P.muted())

# --- B  a kinetic model of the cascade ---------------------------------------------------------------------
bio.panel(ax, "B", (9.6, 8.2))
bio.label(ax, (13.6, 8.0), "A minimal model", size="title", bold=True)


def simulate(t_end=24.0, n=2400):
    """dI/dt = a - dI;  dE/dt = kI - dE;  dG/dt = r E G (1 - G/K);  dL/dt = m (G/K) - dL."""
    dt = t_end / n
    I = E = L = 0.0
    G, K = 1.0, 500.0
    a, d, k, r, m = 1.0, 0.25, 0.9, 0.012, 9.0
    out = np.zeros((n, 5))
    for i in range(n):
        t = i * dt
        dI = a - d * I
        dE = k * I - d * E
        dG = r * E * G * (1 - G / K)
        dL = m * (G / K) - d * L
        I, E, G, L = I + dI * dt, E + dE * dt, G + dG * dt, L + dL * dt
        out[i] = (t, I, E, G, L)
    return out


s = simulate()
t, I, E, G, L = s.T
pl = quant.Plot(ax, (10.4, 2.3, 6.2, 4.9), xlim=(0, 24), ylim=(0, 1.05), xlabel="t / h",
                ylabel="relative amount", xticks=[0, 6, 12, 18, 24], yticks=[0, 0.5, 1])
pl.line(t, I / I.max(), "highlight", text="immediate-early", at=0.22)
pl.line(t, E / E.max(), "positive", text="early", at=0.58)
pl.line(t, G / G.max(), "dna", dashed=True, text="genomes", at=0.72)
pl.line(t, L / L.max(), "virus", text="late", at=0.86)
bio.label(ax, (13.6, 1.3), "$\\mathrm{d}G/\\mathrm{d}t = r\\,E\\,G\\,(1 - G/K)$ : replication needs early proteins;",
          size="tiny", color=P.muted())
bio.label(ax, (13.6, 0.85), "$\\mathrm{d}L/\\mathrm{d}t = m\\,(G/K) - \\delta L$ : late output follows template number",
          size="tiny", color=P.muted())
bio.label(ax, (13.6, 0.3), "A single feedback (early → genomes → late) orders the programme",
          size="tiny", color=P.muted())
