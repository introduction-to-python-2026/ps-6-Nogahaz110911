def create_codon_dict(file_path):
    file = open(file_path, "r")
    rows = file.readlines()
    file.close()
    codons = {}
    for row in rows:
        row.strip().split('\t')
        codons.update({row[1] : row[3]})
    return codons


