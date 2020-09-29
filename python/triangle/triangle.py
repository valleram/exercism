def equilateral(sides):
    if 0 in set(sides):
        return False
    else:
        return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    pass


def scalene(sides):
    pass

if __name__ == '__main__':
    print(equilateral([2, 2, 2]))
    equilateral([2, 3, 2])
    equilateral([5, 4, 6])
    equilateral([0, 0, 0])
    equilateral([0.5, 0.5, 0.5])
