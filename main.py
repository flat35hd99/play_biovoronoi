from biovoronoi.core import Core
from Bio.PDB import PDBParser


def main():
    structure = PDBParser(QUIET=True).get_structure("nve400", "./nve400_wraped.pdb")
    core = Core()
    core.set_structure(structure)
    core.calculate_voronoi_obejct()
    core.calculate_voronoi_volumes()
    core.create_df()
    core.groupby_residue()
    df = core.get_residue_df()
    df.to_csv("output.csv")


if __name__ == "__main__":
    main()
