def to_rna(dna_strand):
    rna_strand = ""
    if dna_strand.isalpha():
        for nuc in dna_strand:
            if nuc == "A":
                rna_strand = rna_strand + "U"
            elif nuc == "C":
                rna_strand = rna_strand + "G"
            elif nuc == "G":
                rna_strand = rna_strand + "C"
            elif nuc == "T":
                rna_strand = rna_strand + "A"
            else:
                return False

    return rna_strand
