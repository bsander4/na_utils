"""
Convert DNA sequences to RNA.
"""

def rna(seq):
    """convert dna to rna"""

    #determine if seq is uppercase
    seq_upper = seq.isupper()

    #convert to lowercase
    seq = seq.lower()

    #swap out t for u

    seq = seq.replace('t', 'u')

    #return upper or lower, depending on input
    if seq_upper:
        return seq.upper()
    else:
        return seq


def reverse_rna_complement(seq):
    """convert DNA seq into its rev complement as RNA"""

    #determine if original sequnece was upper
    seq_upper = seq.isupper()

    #rev sequence
    seq = seq[::-1]

    #convert uppercase
    seq = seq.upper()

    #compute complement
    seq = seq.replace('A', 'u')
    seq = seq.replace('T', 'a')
    seq = seq.replace('G', 'c')
    seq = seq.replace('C', 'g')

    #return in appropriate case
    if seq_upper:
        return seq.upper()
    else:
        return seq    
