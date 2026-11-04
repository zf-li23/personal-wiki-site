# The viral shunt in the marine microbial loop: where viral lysis diverts carbon.
# Grey arrows, the classical food chain; red arrows, the shunt created by lysis. Standing stocks are
# per millilitre of surface seawater (Madigan et al. 2019); the global lysis flux is of order 1e9 t C per day.
import wikibio as bio

P = bio.P
fig, ax = bio.canvas(17, 8.6)

GREY = P.edge("neutral")
RED = P.edge("negative")

bio.label(ax, (8.5, 8.3), "Carbon in the surface ocean: the food chain and the viral shunt",
          size="title", bold=True)


def node(center, w, h, token, title, sub=None):
    bio.box(ax, center, w, h, token=token, radius=0.22)
    dy = 0.22 if sub else 0.0
    bio.label(ax, (center[0], center[1] + dy), title, size="small", bold=True, color=P.on_fill())
    if sub:
        bio.label(ax, (center[0], center[1] - 0.34), sub, size="tiny", color=P.on_fill())
    return center


pp = node((3.0, 6.6), 4.4, 1.25, "plant", "Phytoplankton",
          "and cyanobacteria; $10^5$ cells ml$^{-1}$,\n$>30\\,\\%$ of global CO$_2$ fixation")
bact = node((3.0, 2.4), 4.4, 1.25, "bacterium", "Heterotrophic bacteria",
            "and archaea; $10^6$ cells ml$^{-1}$")
vir = node((8.5, 4.5), 3.1, 1.15, "virus", "Viruses", "$10^7$ particles ml$^{-1}$")
dom = node((8.5, 1.5), 3.6, 1.15, "metabolite", "Dissolved organic matter", "cell contents, lysate")
graz = node((13.4, 6.6), 3.3, 1.15, "animal", "Protist grazers", "flagellates, ciliates")
high = node((13.4, 3.9), 3.3, 1.15, "animal", "Zooplankton and fish", "higher trophic levels")
exp = node((13.4, 1.4), 3.3, 1.15, "neutral", "Export to depth", "sinking particles")

# --- the classical chain -------------------------------------------------------------------------------
bio.arrow(ax, (5.05, 6.95), (11.72, 6.95), kind="process", color=GREY)
bio.label(ax, (8.4, 7.25), "grazing", size="tiny", color=P.muted())
bio.arrow(ax, (13.4, 6.0), (13.4, 4.5), kind="process", color=GREY)
bio.arrow(ax, (13.4, 3.3), (13.4, 2.0), kind="process", color=GREY)
bio.arrow(ax, (4.9, 3.0), (11.8, 6.2), kind="process", color=GREY, bend=0.22)
bio.label(ax, (8.4, 6.05), "grazing on bacteria", size="tiny", color=P.muted())

# --- the shunt -----------------------------------------------------------------------------------------
bio.arrow(ax, (4.2, 5.95), (7.4, 5.0), kind="process", color=RED, bend=0.10)
bio.label(ax, (5.5, 5.85), "lysis", size="tiny", color=RED)
bio.arrow(ax, (4.2, 3.05), (7.4, 4.1), kind="process", color=RED, bend=-0.10)
bio.label(ax, (5.5, 3.1), "lysis: $5$–$50\\,\\%$ of the standing\nstock per day", size="tiny", color=RED)
bio.arrow(ax, (8.5, 3.9), (8.5, 2.1), kind="process", color=RED)
bio.label(ax, (9.35, 3.0), "cell contents\nreleased", size="tiny", color=RED)
bio.arrow(ax, (6.7, 1.5), (5.0, 2.0), kind="process", color=RED, bend=0.12)
bio.label(ax, (5.9, 1.15), "uptake", size="tiny", color=RED)
bio.arrow(ax, (2.0, 1.75), (2.0, 0.75), kind="process", color=RED)
bio.label(ax, (2.0, 0.45), "respired to CO$_2$", size="tiny", color=RED)
bio.arrow(ax, (10.3, 1.4), (11.75, 1.4), kind="inhibition", color=RED)
bio.label(ax, (11.0, 0.95), "export reduced", size="tiny", color=RED)

# --- legend and numbers ----------------------------------------------------------------------------------
bio.arrow(ax, (0.6, 7.9), (1.5, 7.9), kind="process", color=GREY)
bio.label(ax, (1.65, 7.9), "transfer up the food web", size="tiny", color=P.muted(), ha="left")
bio.arrow(ax, (0.6, 7.45), (1.5, 7.45), kind="process", color=RED)
bio.label(ax, (1.65, 7.45), "the viral shunt", size="tiny", color=RED, ha="left")

bio.box(ax, (6.6, 0.42), 5.4, 0.72, token="highlight", radius=0.16)
bio.label(ax, (6.6, 0.42), color=P.on_fill(), text="globally $\\sim 10^{23}$ infections s$^{-1}$,\n"
                           "$\\sim 10^{9}$ t of carbon released per day", size="tiny")
