def create_codon_dict(file_path):
    codon_dict = {}
    with open(file_path, 'r') as f:
        for line in f:
            clean_line = line.strip()
            if clean_line:
                parts = clean_line.split()
                if len(parts) == 2:
                    codon, amino_acid = parts
                    codon_dict[codon] = amino_acid
    return **codon_dict**
