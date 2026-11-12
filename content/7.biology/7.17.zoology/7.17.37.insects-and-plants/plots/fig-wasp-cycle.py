# Life cycle of a pollinating fig wasp in a monoecious fig (schematic). Phases of the syconium:
# receptive (female flowers open, foundress enters), oviposition and pollination, interfloral development
# (galls and seeds), male phase (males emerge, mate, chew exit hole; females load pollen), departure and
# search for a receptive syconium on another tree. Ovules with short styles become galls, long-styled ones seeds.
import wikibio as bio
from wikibio import ecology

P = bio.P
fig, ax = bio.canvas(22, 15)
steps = [
    dict(text="Receptive syconium", sub="scent attracts females", token="plant"),
    dict(text="Foundress enters", sub="through ostiole; loses wings", token="enzyme"),
    dict(text="Pollination + oviposition", sub="eggs in short-styled ovules;\nfoundress dies", token="positive"),
    dict(text="Interfloral phase", sub="galls (wasps) and seeds\ndevelop, several weeks", token="ovule"),
    dict(text="Males emerge", sub="wingless; mate with females\nin galls; chew exit hole", token="negative"),
    dict(text="Females load pollen", sub="male flowers now open", token="enzyme"),
    dict(text="Dispersal flight", sub="1-2 days to find\nanother tree", token="positive"),
]
ecology.cycle(ax, (11, 7.4), 5.3, steps, start=90, clockwise=True, size="small",
              arrow_labels=["", "", "", "", "", "", ""],
              sectors=[dict(start=-0.5, end=2.5, token="plant"), dict(start=3.5, end=5.5, token="bract")],
              center_text=None)
bio.label(ax, (11, 8.1), "Inside one syconium:", size="small", bold=True, color=P.muted())
bio.label(ax, (11, 7.5), "short style -> gall -> wasp", size="small", color=P.muted())
bio.label(ax, (11, 6.9), "long style -> seed", size="small", color=P.muted())
bio.label(ax, (19.4, 13.9), "Female phase", size="small", bold=True, color=P.edge("plant"))
bio.label(ax, (2.8, 1.2), "Male phase", size="small", bold=True, color=P.edge("bract"))
