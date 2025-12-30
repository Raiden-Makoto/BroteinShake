def extract_best_design(fasta_file: str, output_file: str) -> None:
    best_score = float('inf')
    best_header = ""
    best_seq = ""
    
    with open(fasta_file, 'r') as f:
        lines = f.readlines()
        
    for i in range(0, len(lines), 2):
        header = lines[i].strip()
        sequence = lines[i+1].strip()
        
        # Skip the original native sequence (first entry)
        if "sample" not in header:
            continue
            
        # Parse the score: "score=0.7647"
        try:
            score_part = [p for p in header.split(',') if 'score' in p][0]
            score = float(score_part.split('=')[1])
            
            if score < best_score:
                best_score = score
                best_header = header
                best_seq = sequence
        except:
            continue

    if best_seq:
        with open(output_file, 'w') as f:
            f.write(f"{best_header}\n{best_seq}\n")
        print(f"Success! Best design ({best_score}) saved to {output_file}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Extract best design from ProteinMPNN output")
    parser.add_argument("--input_fa", type=str, default="bbb_designs_v1/seqs/tfr_clean.fa",
                        help="Input FASTA file path (relative to project root)")
    parser.add_argument("--output_fa", type=str, default="bbb_designs_v1/best_shuttle.fa",
                        help="Output FASTA file path (relative to project root)")
    
    args = parser.parse_args()
    extract_best_design(args.input_fa, args.output_fa)