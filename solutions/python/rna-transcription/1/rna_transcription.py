def to_rna(dna_strand):
    dna_to_rna = {"G": "C", "C": "G", "T": "A", "A": "U"}
    rna_strand = ""
    for i in dna_strand:
        rna_strand += dna_to_rna[i]
    return rna_strand
