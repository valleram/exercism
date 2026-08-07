COLORS_MAPPING: dict[str, int] = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6,
    "violet": 7, "grey": 8, "white": 9}


def value(colors):
    '''
    :param colors:
    :return:
    '''
    result = [COLORS_MAPPING[item] for item in colors if item in COLORS_MAPPING]
    return int(str(result[0]) + str(result[1]))

