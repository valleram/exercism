def flatten(iterable):
    result = list()


    for element in iterable:
        if element is None:
            continue
        if isinstance(element, list):
            flat_lst = flatten(element)
            result.extend(flat_lst)
        else:
            result.append(element)
    return result

