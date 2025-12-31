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

## Project Results
**Sample 18** emerged as the superior design based on its combination of low energy scores and structural accuracy.

**Optimal Sequence:** `AGGPQYCKLDDNHYYLKYGDKVFLITVSDISVLDEKTDIKLTTPADLANCLPNPADAAGIAAFLTALGWDWAKDKPPLCRPKSSSTGTCIQLDISKQPETKEQGEKILAGLKKLFPGFVDKCKEGKKCYLNIYECGSPSSGNYCGPEYLDKCKFTR` (see `Sample18.pdb` for the folded structure)

### Technical Specifications: Sample 18 (Lead Candidate)

| Metric | Value | Interpretation |
| :--- | :--- | :--- |
| **Design ID** | **Sample 18** | Top-scoring candidate from ProteinMPNN generation. |
| **Sequence Recovery** | **$45.51$%** | Balanced optimization vs. template preservation. |
| **ProteinMPNN Score** | **$0.7647$** | High-probability sequence for the target fold. |
| **Backbone RMSD** | **$0.751$ Å** | Near-perfect atomic (<1.0 is excellent) mimicry of viral template. |
| **Fold Confidence** | **pLDDT $> 90$** | ESMFold "Blue" status; highly confident 3D prediction. |
| **Binding Interface** | **$8 \rightarrow 0$ Clashes** | Resolved via AM1-BCC charge assignment & H-bond optimization. |
| **Target Receptor** | **hTfR1** | Human Transferrin Receptor (Apical Domain). |
