import string


def rotate(text, key):

    alphabet = list(string.ascii_lowercase)
    res = list()
    for i in text:
        upper = False
        if i.isupper():
            upper = True
        if i.isalpha():
            index = alphabet.index(i.lower()) + key
            #print(index)
            if index > len(alphabet)-1:
                #print(len(alphabet))
                index -= len(alphabet)
                #print(index)
                i = alphabet[index]
                #print(i)
            else:
                i = alphabet[index]
            if upper:
                res.append(i.upper())
            else:
                res.append(i)
        else:
            res.append(i)

    res = listToString(res)
    return res


def listToString(s):

    # initialize an empty string
    str1 = ""
    for ele in s:
        str1 += ele
    return str1





if __name__ == "__main__":
    rotate("hO2 laz", 5)
