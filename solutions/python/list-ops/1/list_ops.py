def append(list1, list2):
    """Return a new list containing list1 followed by list2."""
    result = []

    for item in list1:
        result += [item]

    for item in list2:
        result += [item]

    return result


def concat(lists):
    """Flatten a list by one level."""
    result = []

    for current_list in lists:
        result = append(result, current_list)

    return result


def filter(function, values):
    """Return elements for which function returns True."""
    result = []

    for value in values:
        if function(value):
            result += [value]

    return result


def length(values):
    """Return the number of elements in a list."""
    count = 0

    for _ in values:
        count += 1

    return count


def map(function, values):
    """Apply function to every element in a list."""
    result = []

    for value in values:
        result += [function(value)]

    return result


def foldl(function, values, initial):
    """Apply the function from left to right."""
    accumulator = initial

    for value in values:
        accumulator = function(accumulator, value)

    return accumulator


def foldr(function, values, initial):
    """Apply the function from right to left."""
    accumulator = initial

    for index in range(len(values) - 1, -1, -1):
        accumulator = function(accumulator, values[index])

    return accumulator


def reverse(values):
    """Return a new list with the elements in reverse order."""
    result = []

    for index in range(length(values) - 1, -1, -1):
        result += [values[index]]

    return result