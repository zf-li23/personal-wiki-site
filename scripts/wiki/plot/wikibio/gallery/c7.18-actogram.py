# wikibehav sample (7.18): actogram. Rendered with render_plot.py like any plot script.
import wikibio as bio
import wikibehav as wb

fig, ax = bio.canvas(26, 12)
t, c, ons = wb.simulate_activity(days=24, tau=24.0, onset=18.0, alpha=10.0, taus=[(10, 24.7)], seed=0)
bio.panel(ax, "A", (0.2, 11.8))
bio.label(ax, (1.5, 11.5), "LD 12:12, then DD", size="small", bold=True, ha="left")
act = wb.Actogram(ax, (1.5, 1.4, 10.5, 9.4), t, c, light=(6, 18), dd_from=10)
act.onsets(ons, token="rna")
t2, c2, ons2 = wb.simulate_activity(days=24, tau=23.6, onset=19.0, alpha=9.0, shifts=[(12, 3.0)], seed=3)
bio.panel(ax, "B", (13.6, 11.8))
bio.label(ax, (14.9, 11.5), "DD, light pulse on day 12", size="small", bold=True, ha="left")
act2 = wb.Actogram(ax, (14.9, 1.4, 10.5, 9.4), t2, c2, light=(6, 18), dd_from=0, pulses=[(11, 21.0)], token="dna")
