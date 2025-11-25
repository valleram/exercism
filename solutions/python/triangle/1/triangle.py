def equilateral(sides):
    if 0 in set(sides):
        return False
    else:
        return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    sides = sorted(sides)
    if 0 in set(sides):
        return False
    elif sides[0] + sides[1] <= sides[2]:
        return False
    elif len(set(sides)) <= 2:
        return True
    else:
        return False



def scalene(sides):
    sides = sorted(sides)
    if sides[0] + sides[1] <= sides[2]:
        return False
    elif not sides[0] == sides[1] == sides[2]:
        return True
    elif len(set(sides)) > 0:
        return False



if __name__ == '__main__':
    print(equilateral([2, 2, 2]))
    equilateral([2, 3, 2])
    equilateral([5, 4, 6])
    equilateral([0, 0, 0])
    equilateral([0.5, 0.5, 0.5])
