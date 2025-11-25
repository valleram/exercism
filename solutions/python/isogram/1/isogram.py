def is_isogram(string):
    only_letters = [i.lower() for i in string if i.isalpha()]
    return len(only_letters) == len(set(only_letters))
