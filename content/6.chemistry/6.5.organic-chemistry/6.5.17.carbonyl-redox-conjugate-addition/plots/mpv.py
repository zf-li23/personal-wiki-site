"""Meerwein-Ponndorf-Verley reduction. The ketone (left) is bound through its oxygen to aluminium
(dashed bond), which also carries an isopropoxide group (the two other alkoxy groups on aluminium are
written OiPr). In the chair-like six-membered transition state the C-H of the isopropoxide is
delivered as a hydride to the carbonyl carbon, the isopropoxide becomes acetone, and the substrate
becomes an aluminium alkoxide; exchange with propan-2-ol releases the product alcohol."""

import math

import numpy as np

from wikichem import Scheme

s = Scheme()


def hexagon(deg):
    t = math.radians(deg)
    return (math.cos(t), math.sin(t))


def labels(mol, centre, subs, text):
    """Write a group label at the ends of stand-in bonds."""
    for k in subs:
        u = mol.xy(k) - mol.xy(centre)
        u = u / np.linalg.norm(u)
        s.text(mol.xy(k) + 0.45 * u, text, size=13)


sub = s.molecule("CC(C)=O", coords=[(-1.8, -0.1), hexagon(210), (-1.1, -1.45), hexagon(150)], lone_pairs=[3])
al = s.molecule("[H]C(C)(C)O[Al](C)C",
                coords=[hexagon(270), hexagon(330), (1.8, -0.1), (1.2, -1.45), hexagon(30), hexagon(90),
                        (-0.7, 1.75), (0.7, 1.75)], lone_pairs=[4])
labels(al, 5, [6, 7], r"O$i$Pr")
s.partial(sub.atom(3), al.atom(5))
s.curly(al.atom(4), al.bond(1, 4), bend=-0.6)
s.curly(al.bond(0, 1), sub.atom(1), bend=-0.5)
s.curly(sub.bond(1, 3), sub.atom(3), bend=-0.6)
s.arrow((2.6, 0), (4.0, 0))

x = 6.2
prod = s.molecule("CC(C)O[Al](C)C", coords=[(-1.7, -0.6), (-0.87, -0.1), (-0.87, -1.1), (0.0, 0.4), (0.9, 0.0),
                                            (1.4, 0.87), (1.4, -0.87)], at=(x, 0))
labels(prod, 4, [5, 6], r"O$i$Pr")
s.plus((x + 3.0, 0))
s.molecule("CC(C)=O", at=(x + 4.2, 0))
s.draw()
