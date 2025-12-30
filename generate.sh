#!/bin/bash

# Create output directory if it doesn't exist
mkdir -p candidates

# Activate conda env if not activated
# Uncomment and modify the line below if you need to activate a conda environment
# conda activate your_env_name

# Run ProteinMPNN
# To fix chain A and design only chain B, use: --pdb_path_chains "B"
python ProteinMPNN/protein_mpnn_run.py \
        --pdb_path "data/tfr_clean.pdb" \
        --out_folder "./bbb_designs_v1" \
        --pdb_path_chains "B" \
        --num_seq_per_target 20 \
        --sampling_temp "0.1"

# Evaluate the best design
python evaluate.py \
        --input_fa "bbb_designs_v1/seqs/tfr_clean.fa" \
        --output_fa "bbb_designs_v1/best_shuttle.fa"