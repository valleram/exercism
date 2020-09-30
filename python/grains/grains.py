def square(number):
    if 1 <= number <= 64:
        temp = 1
        grains = 1
        for i in range(2, number + 1):
            grains = temp * 2
            temp = grains
        return grains
    raise ValueError("Invalid number")


def total():
    pass
