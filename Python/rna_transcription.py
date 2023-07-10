def to_rna(dna_strand):
    result = ''
    for nucleotide in dna_strand:
        if nucleotide == 'G':
            result += 'C'
        elif nucleotide == 'C':
            result += 'G'
        elif nucleotide == 'T':
            result += 'A'
        elif nucleotide == 'A':
            result += 'U'
        else:
            raise ValueError('Invalid nucleotide')
    return result
