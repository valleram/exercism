def sum_of_multiples(limit, multiples):
    lst_of_multiples = [ i * multiples[j] for i in range(1, limit)
                         for j in range(len(multiples))
                         if i * multiples[j] < limit ]
    return sum(set(lst_of_multiples))
