from Bio.PDB import PDBList, PDBParser, PDBIO, Select # type: ignore

# 1. Download PDB 3KAS
pdbl = PDBList()
pdbl.retrieve_pdb_file('3KAS', pdir='data', file_format='pdb')

# 2. Define a filter to keep only the protein (no water, no ligands)
class ProteinSelect(Select):
    def accept_residue(self, residue):
        return residue.get_resname() not in ['HOH', 'WAT', 'NAG', 'MAN'] # Removes water and sugars

# 3. Save the clean version
parser = PDBParser()
structure = parser.get_structure('3KAS', 'data/pdb3kas.ent')
io = PDBIO()
io.set_structure(structure)
io.save('data/tfr_clean.pdb', ProteinSelect())

print("Target 3KAS is downloaded and cleaned as data/tfr_clean.pdb!")