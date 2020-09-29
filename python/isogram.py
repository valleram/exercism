only_letters = [i for i in string if i.isalpha()]
return len(only_letters) == len(set(only_letters))
