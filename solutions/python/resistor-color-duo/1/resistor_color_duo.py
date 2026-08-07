COLORS_MAPPING = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }
def value(colors):
        result = [ COLORS_MAPPING[item] for item in colors if item in COLORS_MAPPING.keys()]
        if len(result) >= 2:
                # return int(str(result[0] + str(result[1])))
                return int(str(result[0]) + str(result[1]))
        else:
                return int(result[0])
