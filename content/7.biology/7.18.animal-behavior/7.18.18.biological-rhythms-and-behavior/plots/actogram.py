"""Model: double-plotted actograms of simulated wheel running by a nocturnal rodent (activity counts in 15-min bins).
A: entrained to LD 12:12 (lights on 06:00), activity starts at lights-off; from day 11 in constant darkness (DD)
it free-runs with tau = 23.6 h, so onsets drift earlier each day. B: in DD from the start (tau = 23.6 h), a 1-h
light pulse in the early subjective night (day 8, star) delays the rhythm by 2.5 h, and a pulse in the late
subjective night (day 17) advances it by 1.5 h; the onset lines keep their slope (tau) but jump."""
import wikibio as bio
import wikibehav as wb

fig, ax = bio.canvas(26, 12.4)
t, c, ons = wb.simulate_activity(days=24, tau=24.0, onset=18.0, alpha=10.0, taus=[(10, 23.6)], seed=2)
bio.panel(ax, "A", (0.2, 12.1))
bio.label(ax, (1.5, 11.8), "LD 12:12, then DD (tau = 23.6 h)", size="small", bold=True, ha="left")
act = wb.Actogram(ax, (1.5, 1.4, 10.5, 9.6), t, c, light=(6, 18), dd_from=10)
act.onsets(ons, token="rna")
o0 = 18.0 + 10 * 23.6 + 5
t2, c2, ons2 = wb.simulate_activity(days=24, tau=23.6, onset=19.0, alpha=10.0, shifts=[(8, 2.5), (17, -1.5)], seed=5)
bio.panel(ax, "B", (13.6, 12.1))
bio.label(ax, (14.9, 11.8), "DD, light pulses on days 8 and 17", size="small", bold=True, ha="left")
rel = ons2 - 24 * __import__("numpy").arange(len(ons2))
act2 = wb.Actogram(ax, (14.9, 1.4, 10.5, 9.6), t2, c2, light=(6, 18), dd_from=0,
                   pulses=[(7, rel[7] + 1.0), (16, rel[16] + 9.0)], token="dna")
act2.onsets(ons2, token="rna")
ax.set_ylim(0.2, 12.4)
