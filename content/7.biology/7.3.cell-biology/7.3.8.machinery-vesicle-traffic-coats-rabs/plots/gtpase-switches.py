# Two GTPase switches of vesicle traffic, each with the GDP-bound form on the left, the GTP-bound form on the
# right, nucleotide exchange above (GEF) and hydrolysis below (GAP); the membrane is drawn under both.
# A: Sar1. The ER membrane protein Sec12 is its GEF; Sar1-GTP inserts an amphipathic helix into the
# membrane and recruits the inner COPII coat Sec23/24, whose Sec23 subunit (stimulated by Sec31) is the GAP,
# so the coat contains the timer of its own disassembly. B: a Rab protein. GDI holds Rab-GDP in the cytosol
# and delivers it to a membrane; a compartment-specific GEF activates it there, Rab-GTP recruits effectors
# (tethers, motors, kinases), and a GAP turns it off, after which GDI extracts it.
import wikibio as bio
from wikibio import traffic as T

fig, ax = bio.canvas(21, 6.4)
bio.panel(ax, "A", (0.2, 6.2))
T.gtpase_cycle(ax, (4.6, 2.9), w=3.8, name="Sar1", gef="Sec12", gap="Sec23 + Sec31", effector="Sec23/24 coat", gdp_anchored=False)
bio.label(ax, (1.2, 1.0), "ER membrane", size="tiny", color=bio.P.muted(), ha="left")
bio.panel(ax, "B", (10.8, 6.2))
T.gtpase_cycle(ax, (15.6, 2.9), w=3.8, name="Rab", gdi="GDI", effector="effectors")
bio.label(ax, (12.2, 1.0), "donor or target membrane", size="tiny", color=bio.P.muted(), ha="left")
