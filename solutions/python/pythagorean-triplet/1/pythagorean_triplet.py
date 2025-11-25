def triplets_with_sum(number):
    triplet_list = []
    for n in range(1, number+1):
        temp = [3*n, 4*n, 5*n]
        if temp[0] ** 2 + temp[1] ** 2 == temp[2] ** 2 and sum(temp) == number:
            triplet_list.append(temp)
    return triplet_list


def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    pass
