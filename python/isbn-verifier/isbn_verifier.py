import re 

def is_valid(isbn):
    total = 0
    removing_dashes = re.findall(r'[0-9X+]', isbn)
    if len(removing_dashes) != 10:
        return False
    if removing_dashes[-1] == 'X':
        removing_dashes[-1] = '10'


    for i in range(10, 0, -1):
        for j in removing_dashes:
            if j.isalpha():
                return False
            else:
                total += int(j) * i

    if len(removing_dashes) == 10:
        if total % 11 == 0:
            return True
        elif total % 11 != 0:
            return False
    else:
        return False

