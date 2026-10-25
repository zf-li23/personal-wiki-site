"""Watson-Crick base pairs. A: adenine-thymine, two hydrogen bonds (N6-H...O4, N1...H-N3).
B: guanine-cytosine, three hydrogen bonds (O6...H-N4, N1-H...N3, N2-H...O2). dR marks the C-1' of
deoxyribose attached through the N-glycosyl bond (N9 of purines, N1 of pyrimidines). The edge of each
pair facing up (N7 and C6 substituents of the purine, C4 and C5 substituents of the pyrimidine) lines
the major groove of B-DNA, the opposite edge (N3 of the purine, C2 substituent of the pyrimidine) the
minor groove. Geometry: idealized 2D depictions aligned so that donor and acceptor atoms are about
2.9 angstrom apart; the C1'-C1' distance is nearly the same (about 1.05 nm) in both pairs."""

import numpy as np
from rdkit import Chem
from rdkit.Chem import rdDepictor
from wikichem import Scheme

BOND = 1.5  # RDKit depiction bond length (angstrom-like units)
HB = 2.9 / 1.45  # donor-acceptor distance in bond lengths


def coords(smiles):
    m = Chem.MolFromSmiles(smiles)
    rdDepictor.SetPreferCoordGen(True)
    rdDepictor.Compute2DCoords(m)
    c = m.GetConformer()
    return np.array([[c.GetAtomPosition(i).x, c.GetAtomPosition(i).y] for i in range(m.GetNumAtoms())]) / BOND, m


def outward(xy, mol, i):
    nb = [a.GetIdx() for a in mol.GetAtomWithIdx(i).GetNeighbors()]
    v = sum(xy[i] - xy[j] for j in nb)
    return v / np.linalg.norm(v)


def fit(src, dst, away):
    """Rigid transform (rotation, optional reflection, translation) taking points src onto dst; of
    equally good fits (two points fit either way) take the one placing the molecule farthest from away."""
    fits = []
    for flip in (1, -1):
        s = src * [1, flip]
        cs, cd = s.mean(axis=0), dst.mean(axis=0)
        h = (s - cs).T @ (dst - cd)
        u, _, vt = np.linalg.svd(h)
        r = (u @ vt).T
        if np.linalg.det(r) < 0:
            u[:, -1] *= -1
            r = (u @ vt).T
        err = np.sum(((s - cs) @ r.T + cd - dst) ** 2)
        fits.append((err, flip, r, cs, cd))
    emin = min(f[0] for f in fits)
    good = [f for f in fits if f[0] < emin + 0.05]

    def make(f):
        _, flip, r, cs, cd = f
        return lambda p: (p * [1, flip] - cs) @ r.T + cd

    return make, good


def pair(s, purine, pyrimidine, bonds, at, title):
    pu, mpu = coords(purine)
    py, mpy = coords(pyrimidine)
    pu = pu - pu.mean(axis=0)
    # orient the purine: glycosyl N (atom 1) to the lower left, Watson-Crick edge facing right
    ref = pu[[b[0] for b in bonds]].mean(axis=0) - pu[1]
    ang = -np.arctan2(ref[1], ref[0]) + np.radians(12)
    rot = np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
    pu = pu @ rot.T
    if pu[3][1] < pu[1][1]:  # N7 must face the major groove (up)
        pu[:, 1] *= -1
    targets = np.array([pu[i] + HB * outward(pu, mpu, i) for i, _ in bonds])
    make, good = fit(py[[j for _, j in bonds]], targets, None)
    cands = [make(f)(py) for f in good]
    py = max(cands, key=lambda c: np.linalg.norm(c.mean(axis=0) - pu.mean(axis=0)))
    pu, py = pu + at, py + at
    a = s.molecule(purine, coords=[tuple(p) for p in pu], labels={0: "dR"})
    b = s.molecule(pyrimidine, coords=[tuple(p) for p in py], labels={0: "dR"})
    for i, j in bonds:
        p, q = pu[i], py[j]
        d = (q - p) / np.linalg.norm(q - p)
        s.partial(p + 0.33 * d, q - 0.33 * d)
    top = max(pu[:, 1].max(), py[:, 1].max())
    low = min(pu[:, 1].min(), py[:, 1].min())
    mid = (pu[0] + py[0]) / 2
    s.text((mid[0], at[1] + 3.3), "major groove", size=9)
    s.text((mid[0], at[1] - 2.5), "minor groove", size=9)
    s.text((mid[0], at[1] + 4.4), title, size=11)
    return a, b


s = Scheme(scale=0.36)
pair(s, "Cn1cnc2c(N)ncnc21", "CN1C=C(C)C(=O)NC1=O", [(6, 6), (7, 7)], (0.0, 0.0), "A · T (2 H bonds)")
pair(s, "Cn1cnc2c(=O)[nH]c(N)nc21", "CN1C=CC(N)=NC1=O", [(6, 5), (7, 6), (9, 8)], (10.5, 0.0), "G · C (3 H bonds)")
s.draw()
