# BroteinShake
![ProteinGIF](sample18spin.gif)

**BroteinShake** is a computational protein engineering project focused on designing a synthetic peptide "shuttle" capable of crossing the human Blood-Brain Barrier. Drawing inspiration from the entry mechanism of the Machupo virus (MAPV), we engineered a non-viral protein lead—Sample 18—that binds to the apical domain of the Human Transferrin Receptor (hTfR1).

This project utilized a generative **"Sequence Repainting"** workflow to optimize the viral binding interface for increased stability, reduced immunogenicity, and high-fidelity structural mimicry.

## Design Methodology
The lead candidate was developed using an integrated machine learning and physics-based pipeline:

1. Template Selection: Derived the binding interface from the cryo-EM structure of the Machupo virus GPC in complex with hTfR1 (PDB ID: 3KAS).

2. Inverse Folding (ProteinMPNN): Generated 20 optimized sequences for the shuttle backbone while keeping the human receptor (Chain A) fixed.

3. Structure Prediction (ESMFold): Validated the 3D folding of the top candidates using a 3-billion parameter protein language model.

4. Structural Refinement (ChimeraX): Performed energy minimization and hydrogen-bond optimization to resolve steric clashes.