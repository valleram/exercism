"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = None
SUPERLIST = None
EQUAL = None
UNEQUAL = None


def sublist(list_one, list_two):
    if list_one == list_two:
        print("EQUAL")
        return EQUAL
    elif not list_one and (list_two):
        print("SUBLIST")
        return SUBLIST
    elif list_one and not list_two:
        print("SUPERLIST")
        return SUPERLIST
    else:
        print("UNEQUAL")
        return UNEQUAL


if __name__ == '__main__':
    sublist([], [])
    sublist([], [1, 2, 3])
    sublist([1, 2, 3], [])
    sublist([1, 2, 3], [1, 2, 3])
    sublist([1, 2, 3], [2, 3, 4])