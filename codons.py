def create_codon_dict(file_path):
    with open(file_path, "r") file:
        rows = file.readlines()
    codons = {}
    for row in rows:
        columns = row.strip().split('\t')
        if len(columns) > 3:
            codons.update({columns[1]: columns[3]})
    return codons


