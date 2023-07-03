from rdkit import Geometry
from rdkit import Chem
from rdkit.Chem import AllChem, rdMolTransforms


class TreeNode:
    """
    Class containing a node of the SyGMa tree

    :key mol:
        RDKit Molecule
    :key parents:
        Dictonary {inchikey_of_parent: rulename_transforming_parent_to_self}
    :key children:
        List of inchikeys of the child nodes
    :key score:
        Value between 0 and 1
    :key pathway:
        String describing the pathway from parent to self
    :key n_original_atoms:
        Integer, number of atoms originating from parent or None if not yet determined
    """

    def __init__(self, mol, parent="", rule=None, score=None, pathway="", uniqueIdent=""):
        self.mol = mol
        self.reactants = [Chem.MolFromSmiles(part) for part in Chem.MolToSmiles(mol).split('.')]
        self.parents = {parent: rule}
        self.children = []
        try:
            self.ikey = AllChem.InchiToInchiKey(AllChem.MolToInchi(mol))[:14]
        except Exception as e:
            self.ikey = Chem.MolToSmiles(mol, 1)
            # print("some error in treenode_init_")
        # self.ikey = AllChem.InchiToInchiKey(AllChem.MolToInchi(mol))[:14]
        self.score = score
        self.pathway = pathway
        self.uniqueIdent = uniqueIdent
        self.n_original_atoms = None

    def gen_coords(self):
        """
        Calculate 2D positions for atoms in self.mol without coordinates
        """
        # print(Chem.MolToSmiles(self.mol))
        # if self.mol.GetNumConformers() == 0:
        #     Chem.AddHs(self.mol)
        #     AllChem.EmbedMolecule(self.mol)
        #     Chem.RemoveHs(self.mol)
        try:
            conf = self.mol.GetConformer(0)		
            coord_dict = {}
            # Put known coordinates in coordDict
            for i in range(self.mol.GetNumAtoms()):
                pos = conf.GetAtomPosition(i)
                if pos.x != 0.0 or pos.y != 0.0:
                    coord_dict[i] = Geometry.Point2D(pos.x, pos.y)
            # Currently the presence of coordinates is used to determine n_original_atoms
            # This requires SyGMa to always work with structures with atomic coordinates
            # TODO: Derive n_original_atoms independent from the calculation of coordinates
            self.n_original_atoms = len(coord_dict)
            if self.n_original_atoms > 1:
                # calculate average length of all bonds with coordinates
                total = 0.0
                n = 0
                for bond in self.mol.GetBonds():
                    b = bond.GetBeginAtomIdx()
                    e = bond.GetEndAtomIdx()
                    if b in coord_dict and e in coord_dict:
                        n += 1
                        total += rdMolTransforms.GetBondLength(conf, b, e)
                av = total / n
                # compute coordinates for new atoms, keeping known coordinates
                AllChem.Compute2DCoords(self.mol, coordMap=coord_dict, bondLength=av)
            else:
                AllChem.Compute2DCoords(self.mol)

        except (ValueError, ZeroDivisionError):
            AllChem.Compute2DCoords(self.mol)
            self.n_original_atoms = self.mol.GetNumAtoms()