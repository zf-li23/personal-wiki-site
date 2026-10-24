"""Keto-enol tautomerism of acetylacetone (pentane-2,4-dione). The enol is a conjugated
O=C-C=C-OH system whose OH donates an intramolecular hydrogen bond (dashed) to the other carbonyl
oxygen, closing a planar six-membered ring; only the (Z)-enol can form it. Conjugation plus this
hydrogen bond make the enol about 80 % of the neat liquid."""

import math

from wikichem import Scheme


def ring(angle_deg, r=1.0):
    t = math.radians(angle_deg)
    return (r * math.cos(t), r * math.sin(t))


s = Scheme()
s.molecule("CC(=O)CC(C)=O", at=(0, 0))
s.text((0, -1.8), "keto form")
s.arrow((2.2, 0), (3.8, 0), kind="equilibrium")
# atoms: 0 CH3, 1 C, 2 O, 3 CH, 4 C, 5 CH3, 6 O, 7 H; ring C1, O2, H7, O6, C4, C3
c1, o2, h7, o6, c4, c3 = (ring(a) for a in (210, 150, 90, 30, 330, 270))
me0 = (c1[0] + math.cos(math.radians(210)), c1[1] + math.sin(math.radians(210)))
me5 = (c4[0] + math.cos(math.radians(330)), c4[1] + math.sin(math.radians(330)))
en = s.molecule("CC(=O)C=C(C)O[H]", coords=[me0, c1, o2, c3, c4, me5, o6, h7], at=(6.2, 0.2))
s.partial(en.atom(2), en.atom(7))
s.text((6.2, -1.8), "(Z)-enol, intramolecular H-bond")
s.draw()
