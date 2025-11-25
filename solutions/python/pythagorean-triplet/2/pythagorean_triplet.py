def triplets_with_sum(number):
    triplets_list = list()
    for a in range(1, number // 2):
        for b in range(a + 1, number):
            c = number - a - b
            triplet = [a, b, c]
            if is_triplet(triplet):
                triplets_list.append(triplet)
    return triplets_list


def is_triplet(triplet):
    [a, b, c] = triplet
    if a < b and b < c:
        return a ** 2 + b ** 2 == c ** 2
    else:
        return False