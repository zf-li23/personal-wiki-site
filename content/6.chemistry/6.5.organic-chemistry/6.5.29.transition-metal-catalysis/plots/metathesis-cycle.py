"""Chauvin mechanism of olefin metathesis, shown for the self-metathesis of a terminal alkene
RCH=CH2 (the productive cycle of a ring-closing or cross metathesis has the same steps). The metal
methylidene [M]=CH2 and the alkene undergo a [2+2] cycloaddition to a metallacyclobutane, which
cleaves in the other direction (retro-[2+2]) to release ethylene and give the alkylidene [M]=CHR;
a second alkene molecule gives a 2,3-disubstituted metallacyclobutane that releases RCH=CHR and
regenerates [M]=CH2. Every step is reversible; removing volatile ethylene drives the reaction."""

exec(open("cycle.txt").read())

s = Scheme()
R = 5.4
M = {0: "[M]"}


def carbene(at, subst=None):
    if subst:
        return s.molecule("[Ru]=C*", coords=[(-0.75, 0), (0.55, 0), (1.15, 0.85)], at=at, labels={0: "[M]", 2: subst})
    return s.molecule("[Ru]=C", coords=[(-0.6, 0), (0.7, 0)], at=at, labels=M, show_carbons=[1])


def ring(at, two):
    """Metallacyclobutane: [M] top-left, C-alpha top-right (R), C-beta bottom-right (R if ``two``), C bottom-left."""
    sq = [(-0.6, 0.6), (0.6, 0.6), (0.6, -0.6), (-0.6, -0.6)]
    if two:
        return s.molecule("[Ru]1C(*)C(*)C1", coords=[sq[0], sq[1], (1.4, 1.2), sq[2], (1.4, -1.2), sq[3]], at=at,
                          labels={0: "[M]", 2: "R", 4: "R"})
    return s.molecule("[Ru]1C(*)CC1", coords=[sq[0], sq[1], (1.4, 1.2), sq[2], sq[3]], at=at, labels={0: "[M]", 2: "R"})


carbene(polar(R, 90))
ring(polar(R, 0) + np.array([-0.4, 0]), False)
carbene(polar(R, -90), "R")
ring(polar(R, 180) + np.array([0.2, 0]), True)
cycle_arc(s, R, 74, 20, step="[2+2]", enter="RCH=CH$_2$")
cycle_arc(s, R, -20, -72, step="retro-[2+2]", leave="CH$_2$=CH$_2$")
cycle_arc(s, R, -108, -160, step="[2+2]", enter="RCH=CH$_2$")
cycle_arc(s, R, 160, 106, step="retro-[2+2]", leave="RCH=CHR", leave_at=0.6)
s.text((0, 0.4), "Chauvin\nmechanism", size=14)
s.text((0, -1.3), "metallacyclobutane\nintermediates", size=10)
s.draw()
