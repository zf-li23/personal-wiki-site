# From pollination to double fertilization. A: pollen on the stigma germinates; the pollen tube grows
# down the style and into an ovule, carrying two sperm cells. B: the ovule at fertilization: the pollen
# tube enters through the micropyle and discharges the two sperm into a synergid; one sperm fuses with the
# egg (zygote, later the embryo), the other with the two polar nuclei of the central cell (primary
# endosperm nucleus, later the triploid endosperm).
import wikibio as bio
from wikibio import plantmorph as PM

P = bio.P
fig, ax = bio.canvas(24.0, 12.0)
bio.panel(ax, "A", (0.2, 11.8))
PM.specimen(ax, "wikimedia/pistil-pollination", at=(4.2, 6.0), height=10.0, left=1.0, right=8.0, labels=[
    dict(part="pollen", text="Pollen grains on stigma", side="right", where="top"),
    dict(part="pollen-tube", text="Pollen tube", side="right"),
    dict(at=(0.55, 0.84), text="Stigma and style", side="left"),
    dict(at=(0.29, 0.31), text="Locule (ovary)", side="left"),
    dict(at=(0.39, 0.42), text="Ovules on placenta", side="right"),
])
bio.panel(ax, "B", (10.6, 11.8))
PM.specimen(ax, "wikimedia/ovule-double-fertilization", at=(16.8, 6.0), height=9.6, left=11.2, right=22.6, labels=[
    dict(part="antipodal", text="Antipodals", side="left"),
    dict(part="polar-nuclei", text="Polar nuclei (central cell)", side="right"),
    dict(part="central-cell", text="Central cell", side="left"),
    dict(at=(0.46, 0.29), text="Egg cell", side="left"),
    dict(at=(0.53, 0.31), text="Synergids", side="right"),
    dict(at=(0.54, 0.46), text="Sperm cell (to central cell)", side="right"),
    dict(at=(0.47, 0.19), text="Sperm cell (to egg)", side="right"),
    dict(at=(0.05, 0.58), text="Pollen tube", side="left"),
    dict(at=(0.89, 0.72), text="Integuments", side="right"),
])
