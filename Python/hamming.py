def distance(strand_a, strand_b):
    diffPts = 0
    if len(strand_a) != len(strand_b):
        raise ValueError("Must be same length")
    else:
        for nucA, nucB in zip(strand_a, strand_b):
            if nucA != nucB:
                diffPts += 1
        return diffPts