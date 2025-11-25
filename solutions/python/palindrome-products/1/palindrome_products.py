def get_factors(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError("Error!")
    elif (max_factor - min_factor) <= 1:
        return []
    else:
        factors_list = [[i*j, [i, j]] for i in range(min_factor, max_factor + 1) for j in range(min_factor, max_factor + 1) if str(i*j) == str(i*j)[::-1] and i < max_factor]
        return factors_list

def largest(min_factor, max_factor):
    temp = 0
    lsto = get_factors(min_factor, max_factor)
    if lsto:
        ls2 = []
        for i in lsto:
            if i[0] > temp:
                temp = i[0]
                ls2.append(temp)
        temp = max(ls2)
        ls2 = []
        for i in lsto:
            if temp == i[0]:
                ls2.append(i[1])
        return (temp, ls2)
    else:
        return []

def smallest(min_factor, max_factor):
    lsto = get_factors(min_factor, max_factor)
    if lsto:
        return (lsto[0][0], [lsto[0][1]])
    else:
        return []

"""if __name__ == '__main__':
    smallest(min_factor=1, max_factor=9)
    smallest(min_factor=10, max_factor=99)
    smallest(min_factor=100, max_factor=999)
    value, factors = smallest(min_factor=1002, max_factor=1003)
    print(value, factors)

"""