"""Carbon skeletons of trans- and cis-decalin, adamantane and 5alpha-androstane (steroid nucleus),
embedded in 3D with RDKit (ETKDG, then MMFF94 minimisation; fixed seed). Only the hydrogens at the
ring-fusion carbons are drawn (orange); angular methyl groups of the steroid are green."""

import numpy as np
import matplotlib.pyplot as plt
from rdkit import Chem
from rdkit.Chem import AllChem

FUSE, METHYL = "#d97706", "#16a34a"
MOLS = [
    ("trans-decalin", "C1CC[C@@H]2CCCC[C@H]2C1"),
    ("cis-decalin", "C1CC[C@H]2CCCC[C@H]2C1"),
    ("adamantane", "C1C2CC3CC1CC(C2)C3"),
    # 5alpha-androstane: the stereocentres of testosterone, with the A ring saturated (5alpha-H)
    ("5$\\alpha$-androstane", "C[C@]12CC[C@H]3[C@H]([C@@H]1CCC2)CC[C@H]4CCCC[C@]34C"),
]


def embed(smiles):
    mol = Chem.AddHs(Chem.MolFromSmiles(smiles))
    params = AllChem.ETKDGv3()
    params.randomSeed = 7
    AllChem.EmbedMolecule(mol, params)
    AllChem.MMFFOptimizeMolecule(mol)
    return mol, mol.GetConformer().GetPositions()


def orient(xyz, idx):
    """Principal axes of the carbon skeleton: largest extent along x, smallest along z."""
    c = xyz[idx] - xyz[idx].mean(axis=0)
    _, _, vt = np.linalg.svd(c)
    return (xyz - xyz[idx].mean(axis=0)) @ vt.T


fig = plt.figure(figsize=(12, 3.6))
ink = plt.rcParams["text.color"]
for k, (name, smi) in enumerate(MOLS):
    mol, xyz = embed(smi)
    carbons = [a.GetIdx() for a in mol.GetAtoms() if a.GetSymbol() == "C"]
    xyz = orient(xyz, carbons)
    ring_c = {i for r in mol.GetRingInfo().AtomRings() for i in r}
    fusion = [i for i in carbons if sum(i in r for r in mol.GetRingInfo().AtomRings()) >= 2 and mol.GetAtomWithIdx(i).GetTotalNumHs(includeNeighbors=True) == 1]
    if name == "adamantane":
        fusion = []
    ax = fig.add_subplot(1, 4, k + 1, projection="3d")
    for b in mol.GetBonds():
        i, j = b.GetBeginAtomIdx(), b.GetEndAtomIdx()
        ai, aj = mol.GetAtomWithIdx(i), mol.GetAtomWithIdx(j)
        if ai.GetSymbol() == "C" and aj.GetSymbol() == "C":
            col = METHYL if (i not in ring_c or j not in ring_c) else ink
            ax.plot(*zip(xyz[i], xyz[j]), color=col, lw=2.6)
        else:
            c, h = (i, j) if ai.GetSymbol() == "C" else (j, i)
            if c in fusion:
                ax.plot(*zip(xyz[c], xyz[h]), color=FUSE, lw=2)
                ax.scatter(*xyz[h], s=28, color=FUSE, depthshade=False)
    ax.scatter(*xyz[carbons].T, s=22, color="0.4", depthshade=False)
    span = np.abs(xyz[carbons]).max() + 0.4
    ax.set_xlim(-span, span)
    ax.set_ylim(-span, span)
    ax.set_zlim(-span, span)
    ax.set_box_aspect((1, 1, 1))
    ax.view_init(elev=38, azim=-75)
    ax.set_axis_off()
    ax.set_title(name, fontsize=11)
fig.subplots_adjust(left=0, right=1, bottom=0, top=0.9, wspace=0)
