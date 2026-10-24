"""Watson-Crick base pairs, with methyl groups in place of the sugars (attached at N9 of the purines
and N1 of the pyrimidines). Dashed lines join hydrogen-bond donor and acceptor atoms. Top: A-T, two
hydrogen bonds (T N3-H to A N1, A N6-H to T O4). Bottom: G-C, three hydrogen bonds (C N4-H to G O6,
G N1-H to C N3, G N2-H to C O2)."""

import numpy as np
from rdkit import Chem
from rdkit.Chem import rdDepictor

from wikichem import Scheme

GAP = 2.1  # donor-acceptor distance in bond lengths (about 2.9 angstrom)


def layout(smiles):
    """2D coordinates in bond lengths and the map-number -> atom-index table, as wikichem draws them."""
    mol = Chem.MolFromSmiles(smiles)
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(mol)
    conf = mol.GetConformer()
    xy = np.array([[conf.GetAtomPosition(i).x, conf.GetAtomPosition(i).y] for i in range(mol.GetNumAtoms())])
    bl = np.mean([np.linalg.norm(xy[b.GetBeginAtomIdx()] - xy[b.GetEndAtomIdx()]) for b in mol.GetBonds()])
    xy = (xy - xy.mean(axis=0)) / bl
    maps = {a.GetAtomMapNum(): a.GetIdx() for a in mol.GetAtoms() if a.GetAtomMapNum()}
    return xy, maps


def fit(xy, p, q, tp, tq):
    """Rotate and translate xy so that points p, q land on tp, tq (directions matched, centred)."""
    v, w = q - p, tq - tp
    ang = np.arctan2(w[1], w[0]) - np.arctan2(v[1], v[0])
    r = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
    out = (xy - (p + q) / 2) @ r.T + (tp + tq) / 2
    return out


def pair(s, y, purine, pyrimidine, links):
    """links: list of (purine map, pyrimidine map); the first and last fix the placement."""
    pxy, pmap = layout(purine)
    big = s.molecule(purine, at=(0, y), coords=pxy)
    a1, a2 = big.xy(links[0][0]), big.xy(links[-1][0])
    d = a2 - a1
    n = np.array([d[1], -d[0]]) / np.linalg.norm(d)
    if np.dot(n, big.coords.mean(axis=0) - a1) > 0:
        n = -n
    qxy, qmap = layout(pyrimidine)
    for mirror in (False, True):
        c = qxy * ([-1, 1] if mirror else [1, 1])
        placed = fit(c, c[qmap[links[0][1]]], c[qmap[links[-1][1]]], a1 + GAP * n, a2 + GAP * n)
        if np.dot(placed.mean(axis=0) - a1, n) > GAP:
            break
    small = s.molecule(pyrimidine, at=(0, 0), coords=placed)
    for i, j in links:
        s.partial(big.atom(i), small.atom(j))


s = Scheme()
pair(s, 0, "C[n:9]1c[n:7]c2c([NH2:6])[n:1]c[n:3]c12", "C[n:11]1cc(C)c(=[O:14])[nH:13]c1=O",
     [(1, 13), (6, 14)])
s.draw()

s = Scheme()
pair(s, 0, "C[n:9]1c[n:7]c2c1[n:3]c([NH2:2])[nH:1]c2=[O:6]", "C[n:21]1ccc([NH2:24])[n:23]c1=[O:22]",
     [(6, 24), (1, 23), (2, 22)])
s.draw()
