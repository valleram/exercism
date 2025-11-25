def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands should be the same size')
    return sum([1 for i in zip(strand_a, strand_b) if i[0] != i[1]])
